"""Generic bridge between feature data, RDF and OGC Building Blocks.

    lift(data, block)          raw features + the block's JSON-LD context  ->  RDF graph
    lower(graph, block, type)  RDF graph + the block's JSON-LD context     ->  GeoJSON features in the block's terms
    block.validate(features)   GeoJSON features                            ->  JSON Schema errors per feature

Nothing in this module knows about wind farms. Standard libraries do the work: rdflib (RDF, SPARQL),
PyLD (JSON-LD framing and compaction), shapely (WKT <-> GeoJSON), geopandas (tabular / GeoParquet input),
jsonschema (block schemas), pyshacl (SHACL).

Geometry convention: GeoJSON geometry is carried in RDF as GeoSPARQL ``geo:hasGeometry / geo:asWKT``
(CRS84 axis order), so that spatial values survive the round trip as one literal.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
from urllib.request import urlopen

import rdflib
from rdflib import BNode, Literal, URIRef
from rdflib.namespace import RDF

GEO = rdflib.Namespace("http://www.opengis.net/ont/geosparql#")
GEOMETRY_CONTEXT = {"@version": 1.1, "geo": str(GEO),
                    "geometry": {"@id": "geo:hasGeometry"},
                    "wkt": {"@id": "geo:asWKT", "@type": "geo:wktLiteral"}}
REGISTER_URL = "https://ogcincubator.github.io/bblocks-seadots/register.json"


# ------------------------------------------------------------------ building blocks
class BuildingBlock:
    """An OGC Building Block's machine-readable parts: JSON-LD context, JSON Schema, SHACL shapes.

    Resolve a block from a local ``_sources/<name>`` directory (a bblocks repository checkout) or,
    failing that, from the published register. ``context_patches`` are extra JSON-LD contexts applied
    after the block's own, for local fixes or extensions; they are reported in ``repr``.
    """

    def __init__(self, name, context, schema=None, shapes=None, source=None, context_patches=()):
        self.name, self.source = name, source
        self._context, self.schema, self.shapes = context, schema, shapes
        self.context_patches = list(context_patches)

    @property
    def context(self):
        """The block context followed by any patches, as one JSON-LD context array."""
        base = self._context if isinstance(self._context, list) else [self._context]
        return base + self.context_patches

    def __repr__(self):
        patches = f", {len(self.context_patches)} context patch(es)" if self.context_patches else ""
        return f"<BuildingBlock {self.name} from {self.source}{patches}>"

    @classmethod
    def load(cls, name, sources_dir=None, register_url=REGISTER_URL, context_patches=()):
        """Load ``name`` (short name or full id such as ``ogc.hosted.seadots.<name>``)."""
        short = name.rsplit(".", 1)[-1] if name.startswith("ogc.") else name
        if sources_dir and (Path(sources_dir) / short).is_dir():
            return cls.from_directory(Path(sources_dir) / short, context_patches)
        return cls.from_register(short, register_url, context_patches)

    @classmethod
    def from_directory(cls, path, context_patches=()):
        import yaml
        path = Path(path)
        context = json.loads((path / "context.jsonld").read_text(encoding="utf-8"))["@context"]
        schema_file = next((p for p in [path / "schema.yaml", path / "schema.json"] if p.exists()), None)
        schema = yaml.safe_load(schema_file.read_text(encoding="utf-8")) if schema_file else None
        shapes_files = sorted(path.glob("*.shacl")) + sorted(path.glob("rules.shacl*"))
        shapes = rdflib.Graph()
        for f in shapes_files:
            shapes.parse(f, format="turtle")
        return cls(path.name, context, schema, shapes if len(shapes) else None, str(path), context_patches)

    @classmethod
    def from_register(cls, name, register_url=REGISTER_URL, context_patches=()):
        register = json.load(urlopen(register_url, timeout=60))
        entry = next(b for b in register["bblocks"] if b["itemIdentifier"].endswith("." + name))
        context = json.load(urlopen(entry["ldContext"], timeout=60))["@context"]
        schema = json.load(urlopen(entry["schema"]["application/json"], timeout=60)) if entry.get("schema") else None
        return cls(name, context, schema, None, entry["itemIdentifier"], context_patches)

    @classmethod
    def from_context(cls, name, context, schema=None, context_patches=()):
        """A context that is not (yet) a published block, e.g. an exercise-local source vocabulary."""
        if isinstance(context, (str, Path)):
            context = json.loads(Path(context).read_text(encoding="utf-8"))["@context"]
        return cls(name, context, schema, None, "local context", context_patches)

    def validate(self, features, definition=None):
        """JSON Schema errors per feature id; ``definition`` selects a ``$defs`` entry (e.g. sparseFeature)."""
        import jsonschema
        schema = self.schema if definition is None else {"$schema": self.schema.get("$schema"),
                                                           **self.schema["$defs"][definition]}
        validator = jsonschema.Draft202012Validator(schema)
        return {f.get("id"): [e.message for e in validator.iter_errors(f)] for f in _features(features)}


# ------------------------------------------------------------------ data in
def read_features(data):
    """GeoJSON dict, list of features, GeoDataFrame, or a path to .geojson/.json/.parquet -> list of GeoJSON features."""
    return _features(data)


def _features(data):
    if isinstance(data, (str, Path)):
        path = Path(data)
        if path.suffix in (".parquet", ".geoparquet"):
            import geopandas as gpd
            data = gpd.read_parquet(path)
        else:
            data = json.loads(path.read_text(encoding="utf-8"))
    if hasattr(data, "to_json"):                                   # GeoDataFrame
        return json.loads(data.to_json(drop_id=False))["features"]
    if isinstance(data, dict):
        return data["features"] if data.get("type") == "FeatureCollection" else [data]
    return list(data)


def lift(data, block, id_fn=None):
    """Features + a building block's JSON-LD context -> RDF graph.

    ``id_fn(feature) -> IRI`` gives each feature a global identifier (default: its ``id``).
    The block's context is applied unchanged, so the RDF says exactly what the block says the
    fields mean; geometry is added as GeoSPARQL WKT.
    """
    from shapely.geometry import shape
    items = []
    for f in _features(data):
        item = {k: v for k, v in f.items() if k not in ("geometry", "geometry_name", "bbox")}
        item["id"] = id_fn(f) if id_fn else str(f.get("id"))
        if f.get("geometry"):
            item["geometry"] = {"wkt": shape(f["geometry"]).wkt}
        items.append(item)
    context = block.context + [GEOMETRY_CONTEXT]
    return rdflib.Graph().parse(data=json.dumps({"@context": context, "@graph": items}), format="json-ld")


# ------------------------------------------------------------------ data out
def lower(graph, block, rdf_type, geometry=True, drop=("type",), select=None, embed=()):
    """RDF graph + a building block's JSON-LD context -> GeoJSON features in the block's terms.

    Every resource of ``rdf_type`` becomes one feature. Properties are compacted with the block's
    context by JSON-LD framing (PyLD): an RDF property with no term in the block is kept under its
    compact IRI, so nothing is lost silently; ``select`` keeps only the listed terms (a view of the block).
    Blank nodes and ``#``-child resources are embedded; ``embed`` lists further properties whose objects
    are embedded as nested objects (e.g. the source records of a feature).
    ``geo:hasGeometry/geo:asWKT`` becomes the GeoJSON geometry.
    """
    from pyld import jsonld
    from shapely import wkt as shapely_wkt
    from shapely.geometry import mapping

    graph = _subgraph_of_type(graph, URIRef(rdf_type), {URIRef(p) for p in embed})
    geometries = {}
    for subject, geom in list(graph.subject_objects(GEO.hasGeometry)):
        literal = graph.value(geom, GEO.asWKT)
        if literal is not None:
            geometries[str(subject)] = mapping(shapely_wkt.loads(str(literal)))
        graph.remove((subject, GEO.hasGeometry, geom))
        graph.remove((geom, GEO.asWKT, None))
    expanded = _native_numbers(json.loads(graph.serialize(format="json-ld", auto_compact=False)))
    context = block.context
    framed = jsonld.frame(expanded, {"@context": context, "@type": str(rdf_type), "@embed": "@once"},
                          {"omitGraph": False, "processingMode": "json-ld-1.1"})
    nodes = framed.get("@graph", [])
    id_key = _alias(context, "@id")
    properties_key = _term_for(context, "https://purl.org/geojson/vocab#properties")
    features = []
    for node in nodes:
        identifier = node.pop(id_key, None) or node.pop("@id", None)
        props = {k: _plain(v) for k, v in node.items() if k not in drop and not k.startswith("@")}
        nested = props.get(properties_key)
        if isinstance(nested, dict):                               # GeoJSON-LD blocks model properties as a node
            props = {k: v for k, v in nested.items() if k != id_key and k not in drop}
        props = _rename_to_terms(props, context)
        if select is not None:
            props = {k: props[k] for k in select if k in props}
        features.append({"type": "Feature", "id": identifier,
                         "geometry": geometries.get(_expand_id(identifier, expanded)) if geometry else None,
                         "properties": props})
    return {"type": "FeatureCollection", "features": sorted(features, key=lambda f: str(f["id"]))}


def _subgraph_of_type(graph, rdf_type, embed=frozenset()):
    """Resources of ``rdf_type`` with everything reachable through blank nodes and geometry links."""
    out = rdflib.Graph()
    for prefix, ns in graph.namespaces():
        out.bind(prefix, ns)
    todo = list(graph.subjects(RDF.type, rdf_type))
    seen = set()
    while todo:
        s = todo.pop()
        if s in seen:
            continue
        seen.add(s)
        for p, o in graph.predicate_objects(s):
            out.add((s, p, o))
            if isinstance(o, BNode) or p == GEO.hasGeometry or p in embed or str(o).startswith(str(s) + "#"):
                todo.append(o)                                     # blank nodes and '#'-child nodes belong to the resource
    return out


def _alias(context, keyword):
    for ctx in (context if isinstance(context, list) else [context]):
        if isinstance(ctx, dict):
            for term, value in ctx.items():
                if value == keyword:
                    return term
    return keyword


def _term_for(context, iri):
    """The term a context uses for a full IRI (resolving one level of prefixes), or None."""
    contexts = context if isinstance(context, list) else [context]
    prefixes = {k: v for c in contexts if isinstance(c, dict) for k, v in c.items() if isinstance(v, str) and v.endswith(("/", "#"))}
    for c in contexts:
        if not isinstance(c, dict):
            continue
        for term, value in c.items():
            target = value.get("@id") if isinstance(value, dict) else value
            if isinstance(target, str) and ":" in target:
                prefix, local = target.split(":", 1)
                target = prefixes.get(prefix, prefix + ":") + local if prefix in prefixes else target
            if target == iri:
                return term
    return None


def _context_maps(context):
    """(prefixes, @vocab, {full IRI: term}) of a context array, resolving compact IRIs one level."""
    contexts = [c for c in (context if isinstance(context, list) else [context]) if isinstance(c, dict)]
    prefixes, vocab, index = {}, None, {}
    for c in contexts:
        vocab = c.get("@vocab", vocab)
        prefixes.update({k: v for k, v in c.items() if isinstance(v, str) and v.endswith(("/", "#"))})
    for c in contexts:
        for term, value in c.items():
            if term.startswith("@") or (isinstance(value, dict) and "@reverse" in value):
                continue
            target = value.get("@id") if isinstance(value, dict) else value
            if isinstance(target, str) and not target.startswith("@"):
                index[_expand(target, prefixes, vocab)] = term
    return prefixes, vocab, index


def _expand(key, prefixes, vocab):
    if ":" in key:
        prefix, local = key.split(":", 1)
        return prefixes[prefix] + local if prefix in prefixes else key
    return (vocab or "") + key


def _rename_to_terms(props, context):
    """Keys that compaction left as compact IRIs (e.g. a datatype mismatch with the term's coercion)
    are renamed to the block's term for the same IRI, so the output uses the block's names wherever they exist."""
    prefixes, vocab, index = _context_maps(context)
    out = {}
    for key, value in props.items():
        term = key if key in index.values() else index.get(_expand(key, prefixes, vocab), key)
        out[term] = value if term not in out else out[term]
    return out


def _expand_id(identifier, expanded):
    return identifier                                             # ids are absolute IRIs throughout


_XSD = "http://www.w3.org/2001/XMLSchema#"
_NATIVE = {_XSD + t: float for t in ("decimal", "double", "float")} | \
          {_XSD + t: int for t in ("integer", "int", "long", "nonNegativeInteger")} | {_XSD + "boolean": None}


def _native_numbers(node):
    """Typed numeric and boolean literals -> native JSON values, so compaction yields numbers, not strings."""
    if isinstance(node, list):
        return [_native_numbers(n) for n in node]
    if isinstance(node, dict):
        if "@value" in node and node.get("@type") in _NATIVE:
            cast, v = _NATIVE[node["@type"]], node["@value"]
            return {"@value": (v in (True, "true")) if cast is None else cast(v)}
        return {k: _native_numbers(v) for k, v in node.items()}
    return node


def _plain(value):
    """JSON-LD value objects -> plain JSON values ({'@value': 3} -> 3, {'@id': x} -> x)."""
    if isinstance(value, list):
        return [_plain(v) for v in value]
    if isinstance(value, dict):
        if "@value" in value:
            v = value["@value"]
            datatype = str(value.get("@type", ""))
            if isinstance(v, str) and datatype.endswith(("decimal", "double", "float")):
                return float(v)
            if isinstance(v, str) and datatype.endswith(("integer", "int", "long")):
                return int(v)
            if isinstance(v, str) and datatype.endswith("boolean"):
                return v == "true"
            return v
        if set(value) == {"@id"}:
            return value["@id"]
        if "@json" in str(value.get("@type", "")):
            return value.get("@value")
        return {k: _plain(v) for k, v in value.items()}
    return value


# ------------------------------------------------------------------ rules over RDF
def construct(graph, query, bindings=None, prefixes=""):
    """Run a SPARQL CONSTRUCT and return the resulting graph."""
    result = rdflib.Graph()
    for prefix, ns in graph.namespaces():
        result.bind(prefix, ns)
    for triple in graph.query(prefixes + query, initBindings=bindings or {}):
        result.add(triple)
    return result


def select(graph, query, prefixes="", init_ns=None):
    """Run a SPARQL SELECT and return a pandas DataFrame of plain Python values."""
    import pandas as pd
    rows = []
    for r in graph.query(prefixes + query, initNs=init_ns or {}):
        rows.append({k: (None if r[k] is None else r[k].toPython() if isinstance(r[k], Literal) else str(r[k]))
                     for k in r.labels})
    return pd.DataFrame(rows)


def shacl_report(graph, shapes, ontology=None):
    """SHACL validation -> (conforms, DataFrame of results with severity, focus node, path and message)."""
    import pandas as pd
    import pyshacl
    conforms, report, _ = pyshacl.validate(graph, shacl_graph=shapes, ont_graph=ontology, advanced=True,
                                           allow_warnings=True)
    SH = rdflib.Namespace("http://www.w3.org/ns/shacl#")
    rows = [{"severity": str(report.value(r, SH.resultSeverity)).split("#")[-1],
             "focus": str(report.value(r, SH.focusNode)),
             "path": str(report.value(r, SH.resultPath) or ""),
             "message": str(report.value(r, SH.resultMessage) or "")}
            for r in report.subjects(RDF.type, SH.ValidationResult)]
    columns = ["severity", "focus", "path", "message"]
    return conforms, pd.DataFrame(rows, columns=columns).sort_values(columns).reset_index(drop=True)
