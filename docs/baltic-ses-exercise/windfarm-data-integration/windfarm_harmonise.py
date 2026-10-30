"""Multi-source wind-farm harmonisation: raw sources -> common TBox -> projections served by OGC API.

    raw file (as fetched)
      --uplift-->   RDF with the source's own JSON-LD context (a published building block where one exists)
      --align-->    common TBox (config/multisource/tbox) via one SPARQL CONSTRUCT per source shape
      --link-->     crosswalk: which records describe which real-world farm
      --validate--> SHACL (config/multisource/shapes)
      --project-->  GeoJSON collections for target profiles (emodnet-compliant-windfarm-pl and common views)
      --serve-->    pygeoapi: raw-* collections unchanged, harmonised collections through HarmonisedProvider

Used by baltic_windfarm_sources_harmonisation.ipynb and by the pygeoapi service it generates.
Needs rdflib; pyshacl and jsonschema only for validation.
"""
from __future__ import annotations

import csv
import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path

import rdflib
from rdflib import Literal, Namespace, URIRef
from rdflib.namespace import RDF, XSD

ROOT = Path(__file__).resolve().parent                 # windfarm-data-integration/
EXERCISE = ROOT.parent                                 # baltic-ses-exercise/
REPO = ROOT.parents[2]                                 # bblocks-seadots/ (building-block sources)
CONFIG = ROOT / "config" / "multisource"

OWC = Namespace("urn:baltic-ses:owc#")
EM = Namespace("https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#")
SES = Namespace("https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm-pl#")
SEM = Namespace("https://w3id.org/ogc/hosted/seadots/emodnet/")
OSMR = Namespace("urn:baltic-ses:osm-raw#")
GEO = Namespace("http://www.opengis.net/ont/geosparql#")
PROV = Namespace("http://www.w3.org/ns/prov#")
DCT = Namespace("http://purl.org/dc/terms/")
SCHEMA = Namespace("https://schema.org/")


# ------------------------------------------------------------------ helpers
def slug(text):
    text = unicodedata.normalize("NFKD", str(text).replace("+", " plus")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def to_wkt(geometry):
    """GeoJSON geometry -> WKT (Point, Polygon, MultiPolygon), lon lat order (CRS84)."""
    if not geometry:
        return None
    ring = lambda r: "(" + ", ".join(f"{x} {y}" for x, y in r) + ")"
    kind, coords = geometry["type"], geometry["coordinates"]
    if kind == "Point":
        return f"POINT ({coords[0]} {coords[1]})"
    if kind == "Polygon":
        return "POLYGON (" + ", ".join(ring(r) for r in coords) + ")"
    if kind == "MultiPolygon":
        return "MULTIPOLYGON (" + ", ".join("(" + ", ".join(ring(r) for r in p) + ")" for p in coords) + ")"
    raise ValueError(kind)


def rings(geometry):
    """Outer rings of a Polygon/MultiPolygon as lists of (lon, lat)."""
    if not geometry:
        return []
    if geometry["type"] == "Polygon":
        return [geometry["coordinates"][0]]
    if geometry["type"] == "MultiPolygon":
        return [p[0] for p in geometry["coordinates"]]
    return []


def point_in_ring(lon, lat, ring):
    inside, j = False, len(ring) - 1
    for i in range(len(ring)):
        (xi, yi), (xj, yj) = ring[i], ring[j]
        if (yi > lat) != (yj > lat) and lon < (xj - xi) * (lat - yi) / (yj - yi) + xi:
            inside = not inside
        j = i
    return inside


def bbox_of(geometry):
    if not geometry:
        return None
    flat = []
    def walk(c):
        if isinstance(c[0], (int, float)):
            flat.append(c)
        else:
            for x in c:
                walk(x)
    walk(geometry["coordinates"])
    xs, ys = [p[0] for p in flat], [p[1] for p in flat]
    return [min(xs), min(ys), max(xs), max(ys)]


# ------------------------------------------------------------------ sources
def load_sources(config=CONFIG):
    return json.loads((config / "sources.json").read_text(encoding="utf-8"))["sources"]


def resolve_context(ref, config=CONFIG):
    """'bblock:<name>' -> the published building block's context; anything else -> config/contexts/<ref>."""
    path = REPO / "_sources" / ref.split(":", 1)[1] / "context.jsonld" if ref.startswith("bblock:") \
        else config / "contexts" / ref
    return json.loads(path.read_text(encoding="utf-8"))["@context"]


def read_raw(source, exercise=EXERCISE):
    """Read a source file and return it as a GeoJSON FeatureCollection, values untouched.

    CSV rows become features with null geometry; the HubOcean vector-tile decode becomes
    Point / MultiPolygon features (polygon parts stay split at tile edges, as served).
    """
    path = exercise / source["file"]
    fmt = source["format"]
    if fmt == "geojson":
        return json.loads(path.read_text(encoding="utf-8"))
    if fmt == "csv":
        with path.open(newline="", encoding="utf-8") as stream:
            rows = list(csv.DictReader(stream))
        return {"type": "FeatureCollection", "features": [
            {"type": "Feature", "id": slug(r["farm"]), "geometry": None, "properties": r} for r in rows]}
    odp = json.loads(path.read_text(encoding="utf-8"))
    if fmt == "odp-points":
        return {"type": "FeatureCollection", "features": [
            {"type": "Feature", "id": slug(p["props"]["name"]), "geometry": {"type": "Point", "coordinates": p["ll"]},
             "properties": p["props"]} for p in odp["points"]]}
    if fmt == "odp-polygons":
        features = []
        for z in odp["polygons"]:
            parts = []
            for part in z["parts"]:
                ring = [pt for pt in part["ll"] if pt is not None]
                parts.append([ring + [ring[0]]])
            features.append({"type": "Feature", "id": slug(z["props"]["name"]),
                             "geometry": {"type": "MultiPolygon", "coordinates": parts},
                             "properties": {**z["props"], "tiles": [p["tile"] for p in z["parts"]]}})
        return {"type": "FeatureCollection", "features": features}
    raise ValueError(fmt)


def feature_iri(source, feature):
    name = feature["properties"].get("name") or feature["properties"].get("farm") or feature.get("id")
    return source["id_template"].format(id=feature.get("id"), slug=slug(name))


def uplift(source, collection, config=CONFIG):
    """Raw GeoJSON -> RDF using the source's own JSON-LD context; geometry is carried as GeoSPARQL WKT."""
    graph_items = []
    for feature in collection["features"]:
        item = {k: v for k, v in feature.items() if k not in ("geometry", "geometry_name")}
        item["id"] = feature_iri(source, feature)
        if feature.get("geometry"):
            item["geometry"] = {"wkt": to_wkt(feature["geometry"])}
        graph_items.append(item)
    doc = {"@context": [resolve_context(c, config) for c in source["contexts"]], "@graph": graph_items}
    return rdflib.Graph().parse(data=json.dumps(doc), format="json-ld")


# ------------------------------------------------------------------ crosswalk
def crosswalk_graph(raw, config=CONFIG):
    """Canonical farms and zones with the source keys of the records that describe them."""
    cw = json.loads((config / "farm-crosswalk.json").read_text(encoding="utf-8"))
    mapping = json.loads((config / cw["national_to_emodnet"]).resolve().read_text(encoding="utf-8"))
    g = rdflib.Graph()
    g.bind("owc", OWC)
    farm_iri = lambda name: URIRef("urn:baltic-ses:farm:" + slug(name))
    zone_iri = lambda name: URIRef("urn:baltic-ses:zone:" + slug(name))
    linked = set()

    def add_farm(name, keys):
        iri = farm_iri(name)
        g.add((iri, RDF.type, OWC.WindFarm)); g.add((iri, SCHEMA.name, Literal(name)))
        for key in keys:
            g.add((iri, OWC.hasSourceKey, Literal(key)))
        return iri

    for f in raw["national"]["features"]:
        name = f["properties"]["farm"]
        emodnet = mapping["mappings"].get(name, [])
        keys = [f"national|{name}"] + [f"emodnet-wfs|{n}" for n in emodnet] + [f"odp-points|{n}" for n in emodnet]
        linked.update(emodnet)
        iri = add_farm(name, keys)
        osm = cw["osm"].get(name, {})
        for element in osm.get("elements", []):
            g.add((iri, OWC.hasSourceKey, Literal(f"osm|{element}")))
        rule = osm.get("turbines", {})
        if "model" in rule:
            g.add((iri, OWC.osmTurbineModel, Literal(rule["model"])))
        for prefix in rule.get("ref_prefix", []):
            g.add((iri, OWC.osmRefPrefix, Literal(prefix)))
        if "relation" in rule:
            g.add((iri, OWC.osmRelation, URIRef("https://www.openstreetmap.org/" + rule["relation"])))
    names = {f["properties"]["name"] for f in raw["emodnet-wfs"]["features"]} | \
            {f["properties"]["name"] for f in raw["odp-points"]["features"]}
    for name in sorted(names - linked):
        add_farm(name, [f"emodnet-wfs|{name}", f"odp-points|{name}"])
    zones = {f["properties"]["name"] for key in ("emodnet-wfs-zones", "odp-zones") for f in raw[key]["features"]}
    for name in sorted(zones):
        iri = zone_iri(name)
        g.add((iri, RDF.type, OWC.PlanningZone)); g.add((iri, SCHEMA.name, Literal(name)))
        for key in ("emodnet-wfs-zones", "odp-zones"):
            g.add((iri, OWC.hasSourceKey, Literal(f"{key}|{name}")))
    return g


# ------------------------------------------------------------------ alignment
def _query(name, config=CONFIG):
    return (config / "alignments" / "_prefixes.rq").read_text() + (config / "alignments" / name).read_text()


def align(sources, raw_graphs, crosswalk, config=CONFIG):
    """Run each source's CONSTRUCT queries on its own graph, then the crosswalk link query."""
    common = rdflib.Graph()
    for prefix, ns in [("owc", OWC), ("em", EM), ("ses", SES), ("sem", SEM), ("geo", GEO), ("prov", PROV),
                       ("dcterms", DCT), ("schema", SCHEMA)]:
        common.bind(prefix, ns)
    counts = {}
    for source in sources:
        before = len(common)
        bindings = {"sourceKey": Literal(source["key"]), "dataset": URIRef(source["dataset"]),
                    "snapshot": Literal(source["snapshot"], datatype=XSD.date)}
        for name in source["alignments"]:
            for triple in raw_graphs[source["key"]].query(_query(name, config), initBindings=bindings):
                common.add(triple)
        counts[source["key"]] = len(common) - before
    common += crosswalk
    union = rdflib.Graph()
    for g in list(raw_graphs.values()) + [common]:
        union += g
    for triple in union.query(_query("link.rq", config)):
        common.add(triple)
    return common, counts


def add_zone_links(common, raw):
    """Spatial rule: a farm lies within a zone if its reference point is inside the zone (EMODnet WFS geometry)."""
    zones = [(URIRef("urn:baltic-ses:zone:" + slug(f["properties"]["name"])), rings(f["geometry"]))
             for f in raw["emodnet-wfs-zones"]["features"]]
    links = 0
    for farm, lon, lat in farm_reference_points(common):
        for zone, zone_rings in zones:
            if any(point_in_ring(lon, lat, r) for r in zone_rings):
                common.add((farm, OWC.withinZone, zone)); links += 1
    return links


def farm_reference_points(common):
    """Centroid of the farm's OSM turbines, else its first EMODnet point."""
    q = """SELECT ?farm (AVG(?x) AS ?lon) (AVG(?y) AS ?lat) WHERE {
             ?t owc:partOfFarm ?farm ; geo:hasGeometry/geo:asWKT ?w .
             BIND(xsd:decimal(STRBEFORE(STRAFTER(STR(?w), "POINT ("), " ")) AS ?x)
             BIND(xsd:decimal(STRBEFORE(STRAFTER(STRAFTER(STR(?w), "POINT ("), " "), ")")) AS ?y) } GROUP BY ?farm"""
    points = {row.farm: (float(row.lon), float(row.lat)) for row in common.query(q, initNs=NS)}
    q2 = """SELECT ?farm ?w WHERE { ?r owc:describes ?farm ; owc:sourceKey ?k ; geo:hasGeometry/geo:asWKT ?w .
              ?farm a owc:WindFarm . FILTER(STRSTARTS(?k, "emodnet-wfs|") && STRSTARTS(STR(?w), "POINT")) }"""
    for row in common.query(q2, initNs=NS):
        if row.farm not in points:
            x, y = str(row.w)[7:-1].split()
            points[row.farm] = (float(x), float(y))
    return [(farm, lon, lat) for farm, (lon, lat) in points.items()]


NS = {"owc": OWC, "em": EM, "ses": SES, "sem": SEM, "geo": GEO, "prov": PROV, "dcterms": DCT,
      "schema": SCHEMA, "xsd": XSD, "osmr": OSMR}


# ------------------------------------------------------------------ validation
def validate(common, config=CONFIG):
    """SHACL validation of the common graph; returns (conforms, list of result dicts)."""
    import pyshacl
    shapes = rdflib.Graph().parse(config / "shapes" / "offshore-wind-common.shacl.ttl")
    conforms, report, _ = pyshacl.validate(common, shacl_graph=shapes, advanced=True, allow_warnings=True)
    SH = Namespace("http://www.w3.org/ns/shacl#")
    results = [{"severity": str(report.value(r, SH.resultSeverity)).split("#")[-1],
                "focus": str(report.value(r, SH.focusNode)),
                "path": str(report.value(r, SH.resultPath) or "").split("#")[-1].split("/")[-1],
                "message": str(report.value(r, SH.resultMessage) or "")}
               for r in report.subjects(RDF.type, SH.ValidationResult)]
    return conforms, sorted(results, key=lambda r: (r["severity"], r["focus"], r["message"]))


# ------------------------------------------------------------------ projection
def _records(common):
    q = """SELECT ?target ?kind ?rec ?key ?name ?mw ?n ?status ?statusText ?year ?uy ?dist ?inst ?dev ?assumed ?area
                  ?loc ?derived ?dataset ?snap WHERE {
             ?rec owc:describes ?target ; owc:recordKind ?kind ; owc:sourceKey ?key ; prov:wasDerivedFrom ?derived ;
                  dcterms:source ?dataset ; ses:sourceSnapshotDate ?snap .
             OPTIONAL { ?rec schema:name ?name } OPTIONAL { ?rec em:powerMW ?mw } OPTIONAL { ?rec em:nTurbines ?n }
             OPTIONAL { ?rec owc:status ?status } OPTIONAL { ?rec owc:sourceStatusText ?statusText }
             OPTIONAL { ?rec em:year ?year } OPTIONAL { ?rec em:updateYear ?uy }
             OPTIONAL { ?rec em:distanceToCoast ?dist } OPTIONAL { ?rec schema:additionalType ?inst }
             OPTIONAL { ?rec schema:creator ?dev } OPTIONAL { ?rec ses:yearIsAssumed ?assumed }
             OPTIONAL { ?rec owc:areaKm2 ?area } OPTIONAL { ?rec owc:locationKind ?loc } }"""
    out = []
    for r in common.query(q, initNs=NS):
        row = {k: (None if r[k] is None else r[k].toPython() if isinstance(r[k], Literal) else str(r[k]))
               for k in r.labels}
        row["source"] = row["key"].split("|", 1)[0]
        row["status"] = row["status"].rsplit("/", 1)[-1] if row["status"] else None
        out.append(row)
    return out


def _turbines(common):
    q = """SELECT ?t ?farm ?model ?man ?rotor ?hub ?rated ?ref ?op ?st ?derived ?snap WHERE {
             ?t a owc:WindTurbine ; prov:wasDerivedFrom ?derived ; ses:sourceSnapshotDate ?snap .
             OPTIONAL { ?t owc:partOfFarm ?farm } OPTIONAL { ?t owc:turbineModel ?model } OPTIONAL { ?t owc:manufacturer ?man }
             OPTIONAL { ?t owc:rotorDiameterM ?rotor } OPTIONAL { ?t owc:hubHeightM ?hub } OPTIONAL { ?t owc:ratedPowerMW ?rated }
             OPTIONAL { ?t owc:turbineRef ?ref } OPTIONAL { ?t owc:operatorName ?op } OPTIONAL { ?t owc:sourceStatusText ?st } }"""
    return [{k: (None if r[k] is None else r[k].toPython() if isinstance(r[k], Literal) else str(r[k])) for k in r.labels}
            for r in common.query(q, initNs=NS)]


def _num(value):
    return None if value is None else float(value)


def project(common, raw, sources, config=CONFIG):
    """Return the projected collections: farms-common, farms-pl, turbines and zones."""
    policy = json.loads((config / "projection.json").read_text(encoding="utf-8"))
    src = {s["key"]: s for s in sources}
    raw_geometry = {}
    for s in sources:
        for f in raw[s["key"]]["features"]:
            raw_geometry[feature_iri(s, f)] = f.get("geometry")
    records, turbines = _records(common), _turbines(common)
    farms = {str(f): str(common.value(f, SCHEMA.name)) for f in common.subjects(RDF.type, OWC.WindFarm)}
    zones_of = {}
    for farm, zone in common.subject_objects(OWC.withinZone):
        zones_of.setdefault(str(farm), []).append(str(zone))
    by_farm = {}
    for t in turbines:
        if t["farm"]:
            by_farm.setdefault(t["farm"], []).append(t)
    mapping = json.loads((config / json.loads((config / "farm-crosswalk.json").read_text())["national_to_emodnet"])
                         .resolve().read_text(encoding="utf-8"))

    farms_common, farms_pl = [], []
    for farm, canonical_name in sorted(farms.items(), key=lambda kv: kv[1]):
        recs = [r for r in records if r["target"] == farm]
        tur = by_farm.get(farm, [])
        chosen, sources_used = {}, {}

        def pick(prop, field):
            for s in policy["farms"][prop]:
                if s == "osm-count":
                    if tur:
                        return len(tur), s
                    continue
                values = [r[field] for r in recs if r["source"] == s and r[field] is not None]
                if values:
                    if field in ("mw", "n") and len({r["derived"] for r in recs if r["source"] == s}) > 1:
                        return sum(values), s                       # e.g. Baltyk II + Baltyk III in EMODnet
                    return values[0], s
            return None, None

        for prop, field in [("name", "name"), ("power_mw", "mw"), ("n_turbines", "n"), ("status", "status"),
                            ("year", "year"), ("updateyear", "uy"), ("dist_coast", "dist"), ("type_inst", "inst"),
                            ("developer", "dev")]:
            chosen[prop], sources_used[prop] = pick(prop, field)
        chosen["name"] = chosen["name"] or canonical_name
        geometry, geometry_source = None, None
        for s in policy["farms"]["geometry"]:
            if s == "osm-turbine-centroid" and tur:
                pts = [raw_geometry[t["derived"]]["coordinates"] for t in tur]
                geometry = {"type": "Point", "coordinates": [round(sum(p[0] for p in pts) / len(pts), 5),
                                                             round(sum(p[1] for p in pts) / len(pts), 5)]}
                geometry_source = s; break
            pts = [raw_geometry[r["derived"]] for r in recs if r["source"] == s and raw_geometry.get(r["derived"])]
            if pts:
                xy = [p["coordinates"] for p in pts]
                geometry = {"type": "Point", "coordinates": [round(sum(p[0] for p in xy) / len(xy), 5),
                                                             round(sum(p[1] for p in xy) / len(xy), 5)]}
                geometry_source = s if len(pts) == 1 else f"{s} (centroid of {len(pts)} points)"; break
        anticipated = mapping.get("anticipated_locations", {}).get(canonical_name)
        if geometry is None and anticipated:
            geometry, geometry_source = anticipated["geometry"], "anticipated (location-mapping.json)"
        sources_used["geometry"] = geometry_source
        record_list = [{"record": r["rec"], "source_key": r["key"], "power_mw": _num(r["mw"]), "n_turbines": r["n"],
                        "status": r["status"], "status_text": r["statusText"], "year": r["year"],
                        "location_kind": r["loc"], "derived_from": r["derived"], "source": r["dataset"],
                        "source_snapshot_date": str(r["snap"])} for r in sorted(recs, key=lambda r: r["key"])]
        farms_common.append({"type": "Feature", "id": farm, "geometry": geometry, "properties": {
            "kind": "WindFarm", "name": chosen["name"], "power_mw": _num(chosen["power_mw"]),
            "n_turbines": chosen["n_turbines"], "n_turbines_mapped": len(tur) or None, "status": chosen["status"],
            "year": chosen["year"], "updateyear": chosen["updateyear"], "zones": zones_of.get(farm, []),
            "value_sources": {k: v for k, v in sources_used.items() if v}, "records": record_list}})

        primary = "national" if any(r["source"] == "national" for r in recs) else "emodnet-wfs"
        prim = next((r for r in recs if r["source"] == primary), None)
        emodnet_ids = sorted({r["derived"] for r in recs if r["source"] == "emodnet-wfs"})
        if geometry is None:
            loc_status, loc_method, loc_ref = "unmatched", None, None
        elif geometry_source.startswith("anticipated"):
            loc_status, loc_method, loc_ref = "anticipated", anticipated["method"], anticipated["reference"]
        elif geometry_source == "osm-turbine-centroid":
            loc_status, loc_method = "mapped", f"centroid of {len(tur)} OpenStreetMap turbine positions"
            loc_ref = "https://www.openstreetmap.org/" + next(iter(osm_relation_of(recs) or [None])) if osm_relation_of(recs) \
                else min(t["derived"] for t in tur)
        else:
            loc_status = "source-provided" if primary.startswith("emodnet") else "mapped"
            loc_method, loc_ref = f"{geometry_source} point(s)", src["emodnet-wfs"]["dataset"]
        notes = "; ".join(f"{k} from {v}" for k, v in sources_used.items() if v and v != primary and k != "name")
        status_text = (prim or {}).get("statusText") if primary == "national" else None
        farms_pl.append({"type": "Feature", "id": farm, "geometry": geometry, "properties": {
            "name": chosen["name"], "country": "Poland",
            "n_turbines": chosen["n_turbines"], "power_mw": _num(chosen["power_mw"]),
            "status": chosen["status"], "type_inst": chosen["type_inst"], "updateyear": chosen["updateyear"],
            "year": None if chosen["year"] is None else str(chosen["year"]),
            "dist_coast": _num(chosen["dist_coast"]), "notes": ("values merged from several sources: " + notes) if notes else None,
            "developer": chosen["developer"], "status_detail": status_text or chosen["status"],
            "status_as_of": src[primary]["snapshot"] if primary == "national" else None,
            "year_semantics": "planned first-power or completion year" if sources_used["year"] == "national"
                              else ("year reported by EMODnet" if chosen["year"] else None),
            "year_is_assumed": (prim or {}).get("assumed") if sources_used["year"] == "national" else (False if chosen["year"] else None),
            "source_type": "national" if primary == "national" else "emodnet",
            "source_dataset": src[primary]["title"], "source_reference": src[primary]["dataset"],
            "source_snapshot_date": src[primary]["snapshot"], "source_record_id": (prim or {}).get("name"),
            "location_status": loc_status, "location_method": loc_method, "location_reference": loc_ref,
            "location_emodnet_ids": emodnet_ids}})

    turbine_features = [{"type": "Feature", "id": t["t"], "geometry": raw_geometry[t["derived"]], "properties": {
        "kind": "WindTurbine", "farm": t["farm"], "ref": t["ref"], "model": t["model"], "manufacturer": t["man"],
        "rated_power_mw": _num(t["rated"]), "rotor_diameter_m": _num(t["rotor"]), "hub_height_m": _num(t["hub"]),
        "operator": t["op"], "status_text": t["st"], "derived_from": t["derived"], "source": src["osm"]["dataset"],
        "source_snapshot_date": str(t["snap"])}} for t in sorted(turbines, key=lambda t: (t["farm"] or "", t["ref"] or ""))]

    zone_features = []
    zone_iris = sorted({str(z) for z in common.subjects(RDF.type, OWC.PlanningZone)})
    for zone in zone_iris:
        recs = [r for r in records if r["target"] == zone]
        first = lambda field: next((r[field] for s in policy["zones"]["attributes"] for r in recs
                                    if r["source"] == s and r[field] is not None), None)
        geom_rec = next((r for s in policy["zones"]["geometry"] for r in recs if r["source"] == s), None)
        zone_features.append({"type": "Feature", "id": zone, "geometry": raw_geometry.get(geom_rec["derived"]) if geom_rec else None,
            "properties": {"kind": "PlanningZone", "name": first("name"), "power_mw": _num(first("mw")),
                           "area_km2": _num(first("area")), "status": first("status"), "updateyear": first("uy"),
                           "farms": sorted(f for f, zs in zones_of.items() if zone in zs),
                           "value_sources": {"geometry": geom_rec["source"] if geom_rec else None},
                           "records": [{"record": r["rec"], "source_key": r["key"], "power_mw": _num(r["mw"]),
                                        "updateyear": r["uy"], "derived_from": r["derived"]} for r in recs]}})
    fc = lambda feats: {"type": "FeatureCollection", "features": feats}
    return {"farms-common": fc(farms_common), "farms-pl": fc(farms_pl),
            "turbines": fc(turbine_features), "zones": fc(zone_features)}


def osm_relation_of(recs):
    """OSM plant relations among a farm's records (the most specific OSM reference for a farm)."""
    return sorted(r["derived"].split("openstreetmap.org/")[1] for r in recs
                  if r["source"] == "osm" and "/relation/" in r["derived"])


def validate_target_profile(farms_pl, repo=REPO):
    """Check projected farms against the published emodnet-compliant-windfarm-pl JSON Schema (sparse branch)."""
    import jsonschema, yaml
    schema = yaml.safe_load((repo / "_sources/emodnet-compliant-windfarm-pl/schema.yaml").read_text(encoding="utf-8"))
    sparse = {"$schema": schema["$schema"], **schema["$defs"]["sparseFeature"]}
    validator = jsonschema.Draft202012Validator(sparse)
    return {f["properties"]["name"]: [e.message for e in validator.iter_errors(f)] for f in farms_pl["features"]}


# ------------------------------------------------------------------ whole pipeline
def run(config=CONFIG, exercise=EXERCISE, with_validation=False):
    sources = load_sources(config)
    raw = {s["key"]: read_raw(s, exercise) for s in sources}
    raw_graphs = {s["key"]: uplift(s, raw[s["key"]], config) for s in sources}
    crosswalk = crosswalk_graph(raw, config)
    common, counts = align(sources, raw_graphs, crosswalk, config)
    add_zone_links(common, raw)
    result = {"sources": sources, "raw": raw, "raw_graphs": raw_graphs, "common": common, "triples": counts,
              "collections": project(common, raw, sources, config)}
    if with_validation:
        result["shacl"] = validate(common, config)
    return result


@lru_cache(maxsize=4)
def _cached_collections(stamp):
    return run()["collections"]


def _stamp():
    files = [EXERCISE / s["file"] for s in load_sources()] + sorted(CONFIG.rglob("*.*"))
    return tuple((str(p), p.stat().st_mtime) for p in files)


# ------------------------------------------------------------------ pygeoapi provider
try:
    from pygeoapi.provider.base import BaseProvider, ProviderItemNotFoundError
except ImportError:                                     # the notebook can import this module without pygeoapi
    BaseProvider, ProviderItemNotFoundError = object, KeyError


class HarmonisedProvider(BaseProvider):
    """pygeoapi feature provider that translates the raw sources on request (cached until a file changes).

    Configure with ``name: windfarm_harmonise.HarmonisedProvider``, ``data: <collection key>``
    (farms-pl, farms-common, turbines or zones) and ``id_field: id``.
    """

    def __init__(self, provider_def):
        super().__init__(provider_def)
        self.collection = provider_def["data"]
        self.get_fields()

    def _features(self):
        return _cached_collections(_stamp())[self.collection]["features"]

    def get_fields(self):
        if not self._fields:
            sample = self._features()[0]["properties"]
            for key, value in sample.items():
                kind = "number" if isinstance(value, float) else "integer" if isinstance(value, int) and not isinstance(value, bool) \
                    else "boolean" if isinstance(value, bool) else "array" if isinstance(value, list) \
                    else "object" if isinstance(value, dict) else "string"
                self._fields[key] = {"type": kind}
        return self._fields

    def query(self, offset=0, limit=10, resulttype="results", bbox=[], datetime_=None, properties=[], sortby=[],
              select_properties=[], skip_geometry=False, q=None, **kwargs):
        feats = self._features()
        if bbox:
            minx, miny, maxx, maxy = [float(v) for v in bbox]
            def hit(f):
                b = bbox_of(f["geometry"])
                return b is not None and not (b[2] < minx or b[0] > maxx or b[3] < miny or b[1] > maxy)
            feats = [f for f in feats if hit(f)]
        for name, value in properties:
            feats = [f for f in feats if str(f["properties"].get(name)) == str(value)]
        if q:
            feats = [f for f in feats if q.lower() in json.dumps(f["properties"], ensure_ascii=False).lower()]
        for sort in reversed(sortby or []):
            feats = sorted(feats, key=lambda f: (f["properties"].get(sort["property"]) is None,
                                                 f["properties"].get(sort["property"])), reverse=sort["order"] == "-")
        out = []
        for f in feats:
            f = json.loads(json.dumps(f))
            if skip_geometry:
                f["geometry"] = None
            if select_properties:
                f["properties"] = {k: v for k, v in f["properties"].items() if k in select_properties}
            out.append(f)
        result = {"type": "FeatureCollection", "numberMatched": len(out), "features": []}
        if resulttype != "hits":
            result["features"] = out[offset:offset + limit]
            result["numberReturned"] = len(result["features"])
        return result

    def get(self, identifier, **kwargs):
        for f in self._features():
            if f["id"] == identifier or f["id"].rsplit(":", 1)[-1] == identifier:
                return json.loads(json.dumps(f))
        raise ProviderItemNotFoundError(f"item {identifier} not found")


# ------------------------------------------------------------------ service generation
RAW_COLLECTIONS = {"national": "raw-national", "emodnet-wfs": "raw-emodnet-points", "emodnet-wfs-zones": "raw-emodnet-zones",
                   "odp-points": "raw-odp-points", "odp-zones": "raw-odp-zones", "osm": "raw-osm"}
HARMONISED = {
    "farms-pl": ("Wind farms, harmonised (emodnet-compliant-windfarm-pl)",
                 "One record per real-world farm in the published Polish target profile; values chosen by the projection policy.",
                 "bblock:emodnet-compliant-windfarm-pl"),
    "farms-common": ("Wind farms, common model with all source records",
                     "Every farm with the records of each source side by side and the source of each chosen value.", "common.jsonld"),
    "turbines": ("Wind turbines (common model)", "Turbine positions with model, rotor and hub height, linked to their farm.", "common.jsonld"),
    "zones": ("Planning zones (common model)", "Maritime spatial planning zones for offshore wind, with the farms they contain.", "common.jsonld"),
}


def write_service(out_dir, result, config=CONFIG, port=5001):
    """Write raw collections, the pygeoapi configuration and a launcher into ``out_dir``."""
    import yaml
    out_dir = Path(out_dir)
    (out_dir / "data").mkdir(parents=True, exist_ok=True)
    resources = {}
    extent = {"spatial": {"bbox": [14.0, 54.0, 19.0, 56.0], "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"}}
    for source in result["sources"]:
        name = RAW_COLLECTIONS[source["key"]]
        fc = json.loads(json.dumps(result["raw"][source["key"]]))
        for f in fc["features"]:
            f["id"] = str(f.get("id")).replace("/", "-")          # OSM ids such as node/123 are not URL-path safe
        (out_dir / "data" / f"{name}.geojson").write_text(json.dumps(fc, ensure_ascii=False), encoding="utf-8")
        resources[name] = {
            "type": "collection", "title": f"RAW · {source['title']}",
            "description": f"Source records exactly as fetched on {source['snapshot']} ({source['licence']}). "
                           "f=jsonld applies the source's own context: the uplift step of the pipeline.",
            "keywords": ["raw", source["key"]], "links": [{"type": "text/html", "rel": "canonical", "title": "source", "href": source["dataset"]}],
            "extents": extent, "itemType": "feature",
            "providers": [{"type": "feature", "name": "GeoJSON", "data": f"data/{name}.geojson", "id_field": "id"}],
            "linked-data": {"context": [resolve_context(c, config) for c in source["contexts"]]}}
    for name, (title, description, context) in HARMONISED.items():
        resources[name] = {
            "type": "collection", "title": title, "description": description,
            "keywords": ["harmonised", "windfarm"], "links": [], "extents": extent, "itemType": "feature",
            "providers": [{"type": "feature", "name": "windfarm_harmonise.HarmonisedProvider", "data": name, "id_field": "id"}],
            "linked-data": {"context": [resolve_context(context, config)]}}
        (out_dir / "data" / f"{name}.geojson").write_text(
            json.dumps(result["collections"][name], ensure_ascii=False, indent=1), encoding="utf-8")
    cfg = {"server": {"bind": {"host": "127.0.0.1", "port": port}, "url": f"http://localhost:{port}",
                      "mimetype": "application/json; charset=UTF-8", "encoding": "utf-8", "language": "en-US",
                      "limit": 100, "max_limit": 10000,
                      "map": {"url": "https://tile.openstreetmap.org/{z}/{x}/{y}.png", "attribution": "© OpenStreetMap contributors"}},
           "logging": {"level": "ERROR"},
           "metadata": {"identification": {"title": "Polish offshore wind: four sources, one model",
                                           "description": "Raw OSM, EMODnet, HubOcean ODP and national records next to their harmonised projection.",
                                           "keywords": ["Baltic", "offshore wind", "linked data"], "keywords_type": "theme",
                                           "terms_of_service": "https://creativecommons.org/licenses/by/4.0/",
                                           "url": "https://github.com/ogcincubator/bblocks-seadots"},
                        "license": {"name": "Mixed: see each collection (ODbL for OpenStreetMap-derived data)",
                                    "url": "https://www.openstreetmap.org/copyright"},
                        "provider": {"name": "SeaDOTs", "url": "https://www.sintef.no/projectweb/seadots/"},
                        "contact": {"name": "SeaDOTs", "url": "https://www.sintef.no/projectweb/seadots/", "role": "pointOfContact"}},
           "resources": resources}
    (out_dir / "pygeoapi-config.yml").write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True), encoding="utf-8")
    run_sh = out_dir / "run.sh"
    run_sh.write_text('#!/bin/sh\nset -eu\nHERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)\n'
                      'EXERCISE=$(CDPATH= cd -- "$HERE/.." && pwd)\nPYGEOAPI="${PYGEOAPI:-$EXERCISE/.venv/bin/pygeoapi}"\n'
                      'if [ ! -x "$PYGEOAPI" ]; then\n  echo "Missing exercise environment. Run $EXERCISE/setup_pygeoapi.sh first." >&2\n  exit 1\nfi\n'
                      'cd "$HERE"\nexport PYTHONPATH="$EXERCISE${PYTHONPATH:+:$PYTHONPATH}"\n'
                      'export PYGEOAPI_CONFIG="$HERE/pygeoapi-config.yml"\nexport PYGEOAPI_OPENAPI="$HERE/openapi.yml"\n'
                      '"$PYGEOAPI" openapi generate "$PYGEOAPI_CONFIG" --output-file "$PYGEOAPI_OPENAPI"\nexec "$PYGEOAPI" serve\n',
                      encoding="utf-8")
    run_sh.chmod(0o755)
    return resources
