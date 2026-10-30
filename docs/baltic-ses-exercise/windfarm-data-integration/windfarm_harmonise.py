"""Multi-source wind-farm harmonisation, one function per step.

    read_raw        raw file as fetched                       -> GeoJSON FeatureCollection
    uplift          raw features + the source's building block -> RDF            (bblocks_ld.lift)
    align           source RDF + CONSTRUCT queries + crosswalk  -> common-TBox RDF
    link_zones      common RDF + zone geometries                -> farm-in-zone links
    validate        common RDF + SHACL shapes                   -> report
    resolve         common RDF + projection policy              -> one resolved value set per farm / zone (RDF)
    to_profile      resolved RDF + mapping query + target block -> GeoJSON in the block's terms (bblocks_ld.lower)
    write_service   all of the above                            -> pygeoapi configuration (raw + harmonised collections)

Domain choices live in config/multisource/; generic RDF <-> building-block code lives in bblocks_ld.py.
"""
from __future__ import annotations

import csv
import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path

import pandas as pd
import rdflib
from rdflib import Literal, Namespace, URIRef
from rdflib.namespace import RDF, XSD

import bblocks_ld as bl

ROOT = Path(__file__).resolve().parent                 # windfarm-data-integration/
EXERCISE = ROOT.parent                                 # baltic-ses-exercise/
REPO = ROOT.parents[2]                                 # bblocks-seadots/
BLOCKS = REPO / "_sources"                             # building-block sources in this repository
CONFIG = ROOT / "config" / "multisource"

OWC = Namespace("urn:baltic-ses:owc#")
EM = Namespace("https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#")
SES = Namespace("https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm-pl#")
SEM = Namespace("https://w3id.org/ogc/hosted/seadots/emodnet/")
GEO = Namespace("http://www.opengis.net/ont/geosparql#")
PROV = Namespace("http://www.w3.org/ns/prov#")
DCT = Namespace("http://purl.org/dc/terms/")
SCHEMA = Namespace("https://schema.org/")
GEOJSON = Namespace("https://purl.org/geojson/vocab#")
NS = {"owc": OWC, "em": EM, "ses": SES, "sem": SEM, "geo": GEO, "prov": PROV, "dcterms": DCT,
      "schema": SCHEMA, "xsd": XSD, "geojson": GEOJSON, "osmr": Namespace("urn:baltic-ses:osm-raw#")}


def slug(text):
    text = unicodedata.normalize("NFKD", str(text).replace("+", " plus")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def _json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _prefixes():
    return (CONFIG / "alignments" / "_prefixes.rq").read_text()


# ------------------------------------------------------------------ 1. sources and building blocks
def load_sources(config=CONFIG):
    return _json(config / "sources.json")["sources"]


def block(ref, config=CONFIG, patches=()):
    """``bblock:<name>`` -> a published block from this repository; ``<file>`` -> a local context in config/contexts."""
    patches = [_json(config / "contexts" / p)["@context"] for p in patches]
    if ref.startswith("bblock:"):
        return bl.BuildingBlock.load(ref.split(":", 1)[1], sources_dir=BLOCKS, context_patches=patches)
    return bl.BuildingBlock.from_context(ref, config / "contexts" / ref, context_patches=patches)


def target_blocks(config=CONFIG):
    """Output profiles: the published Polish wind-farm block (with the status-term patch) and the exercise's common model."""
    return {"farms-pl": block("bblock:emodnet-compliant-windfarm-pl", config, patches=["pl-status-terms.jsonld"]),
            "common": block("common.jsonld", config)}


def read_raw(source, exercise=EXERCISE):
    """Read a source file as a GeoJSON FeatureCollection, values untouched.

    CSV rows become features with null geometry; decoded HubOcean vector tiles become Point / MultiPolygon
    features (polygon parts stay split at tile edges, as served).
    """
    path, fmt = exercise / source["file"], source["format"]
    if fmt == "geojson":
        return _json(path)
    if fmt == "csv":
        with path.open(newline="", encoding="utf-8") as stream:
            rows = list(csv.DictReader(stream))
        return {"type": "FeatureCollection", "features": [
            {"type": "Feature", "id": slug(r["farm"]), "geometry": None, "properties": r} for r in rows]}
    odp = _json(path)
    if fmt == "odp-points":
        return {"type": "FeatureCollection", "features": [
            {"type": "Feature", "id": slug(p["props"]["name"]), "geometry": {"type": "Point", "coordinates": p["ll"]},
             "properties": p["props"]} for p in odp["points"]]}
    if fmt == "odp-polygons":
        def part(ll):
            ring = [pt for pt in ll if pt is not None]
            return [ring + [ring[0]]]
        return {"type": "FeatureCollection", "features": [
            {"type": "Feature", "id": slug(z["props"]["name"]),
             "geometry": {"type": "MultiPolygon", "coordinates": [part(p["ll"]) for p in z["parts"]]},
             "properties": {**z["props"], "tiles": [p["tile"] for p in z["parts"]]}} for z in odp["polygons"]]}
    raise ValueError(fmt)


def read_all(sources, exercise=EXERCISE):
    return {s["key"]: read_raw(s, exercise) for s in sources}


def feature_iri(source, feature):
    name = feature["properties"].get("name") or feature["properties"].get("farm") or feature.get("id")
    return source["id_template"].format(id=feature.get("id"), slug=slug(name))


# ------------------------------------------------------------------ 2. uplift
def uplift(source, collection, config=CONFIG):
    """Raw features -> RDF with the source's own building block (or local context)."""
    return bl.lift(collection, block(source["block"], config), id_fn=lambda f: feature_iri(source, f))


def uplift_all(sources, raw, config=CONFIG):
    return {s["key"]: uplift(s, raw[s["key"]], config) for s in sources}


# ------------------------------------------------------------------ 3. crosswalk and alignment
def crosswalk_graph(raw, config=CONFIG):
    """Canonical farms and zones, with the source keys of the records that describe them."""
    cw = _json(config / "farm-crosswalk.json")
    mapping = _json((config / cw["national_to_emodnet"]).resolve())
    g = rdflib.Graph()
    farm_iri = lambda name: URIRef("urn:baltic-ses:farm:" + slug(name))
    linked = set()

    def add(iri, kind, name, keys):
        g.add((iri, RDF.type, kind)); g.add((iri, SCHEMA.name, Literal(name)))
        for key in keys:
            g.add((iri, OWC.hasSourceKey, Literal(key)))

    for f in raw["national"]["features"]:
        name = f["properties"]["farm"]
        emodnet = mapping["mappings"].get(name, [])
        linked.update(emodnet)
        osm = cw["osm"].get(name, {})
        iri = farm_iri(name)
        add(iri, OWC.WindFarm, name, [f"national|{name}"] + [f"emodnet-wfs|{n}" for n in emodnet]
            + [f"odp-points|{n}" for n in emodnet] + [f"osm|{e}" for e in osm.get("elements", [])])
        rule = osm.get("turbines", {})
        if "model" in rule:
            g.add((iri, OWC.osmTurbineModel, Literal(rule["model"])))
        for prefix in rule.get("ref_prefix", []):
            g.add((iri, OWC.osmRefPrefix, Literal(prefix)))
        if "relation" in rule:
            g.add((iri, OWC.osmRelation, URIRef("https://www.openstreetmap.org/" + rule["relation"])))
    names = {f["properties"]["name"] for k in ("emodnet-wfs", "odp-points") for f in raw[k]["features"]}
    for name in sorted(names - linked):
        add(farm_iri(name), OWC.WindFarm, name, [f"emodnet-wfs|{name}", f"odp-points|{name}"])
    zones = {f["properties"]["name"] for k in ("emodnet-wfs-zones", "odp-zones") for f in raw[k]["features"]}
    for name in sorted(zones):
        add(URIRef("urn:baltic-ses:zone:" + slug(name)), OWC.PlanningZone, name,
            [f"emodnet-wfs-zones|{name}", f"odp-zones|{name}"])
    return g


def align(sources, raw_graphs, crosswalk, config=CONFIG):
    """Each source's CONSTRUCT queries on its own graph, then the crosswalk link query over everything."""
    common, counts = rdflib.Graph(), {}
    for prefix, ns in NS.items():
        common.bind(prefix, ns)
    for source in sources:
        bindings = {"sourceKey": Literal(source["key"]), "dataset": URIRef(source["dataset"]),
                    "snapshot": Literal(source["snapshot"], datatype=XSD.date)}
        before = len(common)
        for name in source["alignments"]:
            common += bl.construct(raw_graphs[source["key"]], (config / "alignments" / name).read_text(),
                                   bindings, _prefixes())
        counts[source["key"]] = len(common) - before
    common += crosswalk
    union = rdflib.Graph()
    for g in list(raw_graphs.values()) + [common]:
        union += g
    common += bl.construct(union, (config / "alignments" / "link.rq").read_text(), prefixes=_prefixes())
    return common, counts


def link_zones(common, raw):
    """Spatial rule: a farm is within a zone if its reference point lies in the zone (EMODnet WFS geometry)."""
    import geopandas as gpd
    zones = gpd.GeoDataFrame.from_features(raw["emodnet-wfs-zones"]["features"], crs="EPSG:4326")
    zones["zone"] = ["urn:baltic-ses:zone:" + slug(n) for n in zones["name"]]
    points = farm_reference_points(common)
    joined = gpd.sjoin(points, zones[["zone", "geometry"]], predicate="within")
    for farm, zone in zip(joined.farm, joined.zone):
        common.add((URIRef(farm), OWC.withinZone, URIRef(zone)))
    return len(joined)


def farm_reference_points(common):
    """GeoDataFrame of one point per farm: centroid of its OSM turbines, else of its EMODnet points."""
    import geopandas as gpd
    from shapely import wkt
    turbines = bl.select(common, """SELECT ?farm ?w WHERE { ?t owc:partOfFarm ?farm ; geo:hasGeometry/geo:asWKT ?w }""",
                         init_ns=NS)
    records = bl.select(common, """SELECT ?farm ?w WHERE { ?r owc:describes ?farm ; owc:sourceKey ?k ;
                                     geo:hasGeometry/geo:asWKT ?w . ?farm a owc:WindFarm .
                                     FILTER(STRSTARTS(?k, "emodnet-wfs|")) }""", init_ns=NS)
    rows = []
    for name, frame in (("osm-turbine-centroid", turbines), ("emodnet-wfs", records)):
        if frame.empty:
            continue
        frame = frame.assign(geometry=frame.w.map(wkt.loads))
        for farm, g in frame.groupby("farm"):
            if farm not in {r["farm"] for r in rows}:
                pts = gpd.GeoSeries(g.geometry.tolist(), crs="EPSG:4326")
                rows.append({"farm": farm, "method": name, "n_points": len(pts),
                             "geometry": pts.to_crs("EPSG:2180").union_all().centroid})
    return gpd.GeoDataFrame(rows, geometry="geometry", crs="EPSG:2180").to_crs("EPSG:4326")


# ------------------------------------------------------------------ 4. validation
def validate(common, config=CONFIG):
    shapes = rdflib.Graph().parse(config / "shapes" / "offshore-wind-common.shacl.ttl")
    conforms, report = bl.shacl_report(common, shapes)
    report["focus"] = report.focus.str.rsplit(":", n=1).str[-1]
    report["path"] = report.path.str.rsplit("#", n=1).str[-1]
    return conforms, report


# ------------------------------------------------------------------ 5. resolution (policy) -> RDF
RECORD_FIELDS = {"name": SCHEMA.name, "power_mw": EM.powerMW, "n_turbines": EM.nTurbines, "status": OWC.status,
                 "year": EM.year, "updateyear": EM.updateYear, "dist_coast": EM.distanceToCoast,
                 "type_inst": SCHEMA.additionalType, "developer": SCHEMA.creator, "area_km2": OWC.areaKm2}


def records(common):
    """All source records as a DataFrame: target, source, values in common terms, provenance."""
    q = """SELECT ?target ?rec ?key ?name ?power_mw ?n_turbines ?status ?statusText ?year ?updateyear ?dist_coast
                  ?type_inst ?developer ?assumed ?area_km2 ?wkt ?derived ?dataset ?snapshot WHERE {
             ?rec owc:describes ?target ; owc:sourceKey ?key ; prov:wasDerivedFrom ?derived ;
                  dcterms:source ?dataset ; ses:sourceSnapshotDate ?snapshot .
             OPTIONAL { ?rec schema:name ?name } OPTIONAL { ?rec em:powerMW ?power_mw } OPTIONAL { ?rec em:nTurbines ?n_turbines }
             OPTIONAL { ?rec owc:status ?status } OPTIONAL { ?rec owc:sourceStatusText ?statusText }
             OPTIONAL { ?rec em:year ?year } OPTIONAL { ?rec em:updateYear ?updateyear }
             OPTIONAL { ?rec em:distanceToCoast ?dist_coast } OPTIONAL { ?rec schema:additionalType ?type_inst }
             OPTIONAL { ?rec schema:creator ?developer } OPTIONAL { ?rec ses:yearIsAssumed ?assumed }
             OPTIONAL { ?rec owc:areaKm2 ?area_km2 } OPTIONAL { ?rec geo:hasGeometry/geo:asWKT ?wkt } }"""
    frame = bl.select(common, q, init_ns=NS)
    frame["source"] = frame.key.str.split("|").str[0]
    return frame


def turbines_table(common):
    q = """SELECT ?turbine ?farm ?model ?manufacturer ?rotor ?hub ?rated ?ref ?wkt ?derived WHERE {
             ?turbine a owc:WindTurbine ; prov:wasDerivedFrom ?derived ; geo:hasGeometry/geo:asWKT ?wkt .
             OPTIONAL { ?turbine owc:partOfFarm ?farm } OPTIONAL { ?turbine owc:turbineModel ?model }
             OPTIONAL { ?turbine owc:manufacturer ?manufacturer } OPTIONAL { ?turbine owc:rotorDiameterM ?rotor }
             OPTIONAL { ?turbine owc:hubHeightM ?hub } OPTIONAL { ?turbine owc:ratedPowerMW ?rated }
             OPTIONAL { ?turbine owc:turbineRef ?ref } }"""
    return bl.select(common, q, init_ns=NS)


def _pick(recs, sources, field, turbines=None):
    """First source in ``sources`` with a value; values of several records of one source are summed for counts/MW."""
    for s in sources:
        if s == "osm-count":
            if turbines is not None and len(turbines):
                return len(turbines), s
            continue
        vals = recs[(recs.source == s) & recs[field].notna()][field]
        if len(vals):
            if field in ("power_mw", "n_turbines") and len(vals) > 1:
                return vals.astype(float).sum(), s
            return vals.iloc[0], s
    return None, None


def _centroid_wkt(wkts):
    import geopandas as gpd
    from shapely import wkt
    pts = gpd.GeoSeries([wkt.loads(w) for w in wkts], crs="EPSG:4326").to_crs("EPSG:2180")
    return gpd.GeoSeries([pts.union_all().centroid], crs="EPSG:2180").to_crs("EPSG:4326").iloc[0].wkt


def resolve(common, sources, config=CONFIG):
    """Apply projection.json: one resolved value per property per farm and zone, written as RDF.

    The result is the common graph plus, on each farm and zone, the chosen values (common terms), the
    source of each choice (``owc:valueSource``) and the provenance fields of the Polish profile (``ses:``).
    """
    policy = _json(config / "projection.json")
    mapping = _json((config / _json(config / "farm-crosswalk.json")["national_to_emodnet"]).resolve())
    src = {s["key"]: s for s in sources}
    recs, turbines = records(common), turbines_table(common)
    out = rdflib.Graph()
    for prefix, ns in NS.items():
        out.bind(prefix, ns)
    out += common

    def put(subject, prop, value, datatype=None):
        if value is None or (isinstance(value, float) and pd.isna(value)):
            return
        if isinstance(value, str) and value.startswith(("http://", "https://", "urn:")) and datatype == "iri":
            out.add((subject, prop, URIRef(value)))
        else:
            out.add((subject, prop, Literal(value, datatype=datatype) if datatype not in (None, "iri") else Literal(value)))

    for farm in sorted(set(common.subjects(RDF.type, OWC.WindFarm))):
        r = recs[recs.target == str(farm)]
        tur = turbines[turbines.farm == str(farm)]
        name = str(common.value(farm, SCHEMA.name))
        chosen, used = {}, {}
        for field, prop in RECORD_FIELDS.items():
            if field in policy["farms"]:
                chosen[field], used[field] = _pick(r, policy["farms"][field], field, tur)
        chosen["name"] = chosen.get("name") or name
        for field in ("name", "power_mw", "n_turbines", "status", "year", "updateyear", "dist_coast", "type_inst", "developer"):
            value = chosen.get(field)
            if field == "status" and value:
                out.add((farm, OWC.status, URIRef(value)))
            elif field in ("power_mw", "dist_coast") and value is not None:
                put(farm, RECORD_FIELDS[field], float(value), XSD.decimal)
            elif field == "n_turbines" and value is not None:
                put(farm, RECORD_FIELDS[field], int(value), XSD.integer)
            elif value is not None:
                out.set((farm, RECORD_FIELDS[field], Literal(str(value))))
        if len(tur):
            put(farm, OWC.nTurbinesMapped, len(tur), XSD.integer)

        geometry_wkt, geometry_source = None, None
        for s in policy["farms"]["geometry"]:
            if s == "osm-turbine-centroid" and len(tur):
                geometry_wkt, geometry_source = _centroid_wkt(tur.wkt), s
                break
            pts = r[(r.source == s) & r.wkt.notna()].wkt
            if len(pts):
                geometry_wkt = _centroid_wkt(pts)
                geometry_source = s if len(pts) == 1 else f"{s} (centroid of {len(pts)} points)"
                break
        anticipated = mapping.get("anticipated_locations", {}).get(name)
        if geometry_wkt is None and anticipated:
            from shapely.geometry import shape
            geometry_wkt, geometry_source = shape(anticipated["geometry"]).wkt, "anticipated (location-mapping.json)"
        if geometry_wkt:
            geom = URIRef(str(farm) + "#geometry")
            out.add((farm, GEO.hasGeometry, geom)); out.add((geom, GEO.asWKT, Literal(geometry_wkt, datatype=GEO.wktLiteral)))
        used["geometry"] = geometry_source
        for field, s in used.items():
            if s:
                out.add((farm, OWC.valueSource, Literal(f"{field}: {s}")))

        # provenance fields of the Polish profile
        primary = "national" if (r.source == "national").any() else "emodnet-wfs"
        prim = r[r.source == primary].iloc[0] if (r.source == primary).any() else None
        put(farm, SES.sourceType, "national" if primary == "national" else "emodnet")
        put(farm, SES.sourceDataset, src[primary]["title"])
        put(farm, SES.sourceReference, src[primary]["dataset"], "iri")
        put(farm, SES.sourceSnapshotDate, src[primary]["snapshot"], XSD.date)
        if prim is not None:
            put(farm, SES.sourceRecordId, prim["name"])
        if primary == "national" and prim is not None:
            put(farm, SES.statusDetail, prim.statusText)
            put(farm, SES.statusAsOf, src["national"]["snapshot"], XSD.date)
        elif chosen.get("status"):
            put(farm, SES.statusDetail, str(chosen["status"]).rsplit("/", 1)[-1])
        if used.get("year") == "national":
            put(farm, SES.yearSemantics, "planned first-power or completion year")
            if prim is not None and prim.assumed is not None:
                put(farm, SES.yearIsAssumed, bool(prim.assumed), XSD.boolean)
        elif chosen.get("year"):
            put(farm, SES.yearSemantics, "year reported by EMODnet")
            put(farm, SES.yearIsAssumed, False, XSD.boolean)
        if geometry_source is None:
            put(farm, SES.locationStatus, "unmatched")
        elif geometry_source.startswith("anticipated"):
            put(farm, SES.locationStatus, "anticipated")
            put(farm, SES.locationMethod, anticipated["method"])
            put(farm, SES.locationReference, anticipated["reference"], "iri")
        elif geometry_source == "osm-turbine-centroid":
            put(farm, SES.locationStatus, "mapped")
            put(farm, SES.locationMethod, f"centroid of {len(tur)} OpenStreetMap turbine positions")
            relation = r[(r.source == "osm") & r.derived.str.contains("/relation/")].derived
            put(farm, SES.locationReference, relation.iloc[0] if len(relation) else min(tur.derived), "iri")
        else:
            put(farm, SES.locationStatus, "source-provided" if primary.startswith("emodnet") else "mapped")
            put(farm, SES.locationMethod, f"{geometry_source} point(s)")
            put(farm, SES.locationReference, src["emodnet-wfs"]["dataset"], "iri")
        for derived in sorted(r[r.source == "emodnet-wfs"].derived):
            put(farm, SES.locationEmodnetIds, derived)
        merged = [f"{k} from {v}" for k, v in used.items() if v and v != primary and k != "name"]
        if merged:
            put(farm, DCT.description, "values merged from several sources: " + "; ".join(merged))

    for record, target in common.subject_objects(OWC.describes):
        out.add((target, OWC.hasRecord, record))                  # inverse links: features carry their records
    for farm, zone in common.subject_objects(OWC.withinZone):
        out.add((zone, OWC.containsFarm, farm))
    for zone in sorted(set(common.subjects(RDF.type, OWC.PlanningZone))):
        r = recs[recs.target == str(zone)]
        for field in ("power_mw", "area_km2", "status", "updateyear"):
            value, _ = _pick(r, policy["zones"]["attributes"], field)
            if field == "status" and value:
                out.add((zone, OWC.status, URIRef(value)))
            elif field in ("power_mw", "area_km2") and value is not None:
                put(zone, RECORD_FIELDS[field], float(value), XSD.decimal)
            elif value is not None:
                put(zone, RECORD_FIELDS[field], str(value))
        for s in policy["zones"]["geometry"]:
            w = r[(r.source == s) & r.wkt.notna()].wkt
            if len(w):
                geom = URIRef(str(zone) + "#geometry")
                out.add((zone, GEO.hasGeometry, geom)); out.add((geom, GEO.asWKT, Literal(w.iloc[0], datatype=GEO.wktLiteral)))
                out.add((zone, OWC.valueSource, Literal(f"geometry: {s}")))
                break
    return out


# ------------------------------------------------------------------ 6. projection onto building blocks
FARMS_COMMON_VIEW = ["name", "power_mw", "n_turbines", "n_turbines_mapped", "status", "year", "updateyear",
                     "zones", "value_source", "records"]
TURBINE_VIEW = ["farm", "ref", "model", "manufacturer", "rated_power_mw", "rotor_diameter_m", "hub_height_m",
                "operator", "status_text", "derived_from", "source", "source_snapshot_date"]
ZONE_VIEW = ["name", "power_mw", "area_km2", "status", "updateyear", "farms", "value_source", "records"]


def to_profile(resolved, config=CONFIG):
    """Resolved RDF -> GeoJSON collections in the target blocks' terms (bblocks_ld.lower)."""
    blocks = target_blocks(config)
    pl_graph = bl.construct(resolved, (config / "projections" / "farms-pl.rq").read_text(), prefixes=_prefixes())
    return {"farms-pl": bl.lower(pl_graph, blocks["farms-pl"], GEOJSON.Feature),
            "farms-common": bl.lower(resolved, blocks["common"], OWC.WindFarm, select=FARMS_COMMON_VIEW,
                                     embed=[OWC.hasRecord]),
            "turbines": bl.lower(resolved, blocks["common"], OWC.WindTurbine, select=TURBINE_VIEW),
            "zones": bl.lower(resolved, blocks["common"], OWC.PlanningZone, select=ZONE_VIEW, embed=[OWC.hasRecord])}


def validate_profile(collection, config=CONFIG):
    """JSON Schema check of projected farms against the published Polish profile (sparse-feature branch)."""
    return target_blocks(config)["farms-pl"].validate(collection, definition="sparseFeature")


# ------------------------------------------------------------------ whole pipeline
def run(config=CONFIG, exercise=EXERCISE, with_validation=False):
    sources = load_sources(config)
    raw = read_all(sources, exercise)
    raw_graphs = uplift_all(sources, raw, config)
    common, counts = align(sources, raw_graphs, crosswalk_graph(raw, config), config)
    link_zones(common, raw)
    resolved = resolve(common, sources, config)
    result = {"sources": sources, "raw": raw, "raw_graphs": raw_graphs, "common": common, "resolved": resolved,
              "triples": counts, "collections": to_profile(resolved, config)}
    if with_validation:
        result["shacl"] = validate(common, config)
    return result


# ------------------------------------------------------------------ analysis helpers for the notebook
def source_inventory(sources, raw):
    return pd.DataFrame([{"key": s["key"], "title": s["title"], "records": len(raw[s["key"]]["features"]),
                          "geometry": ", ".join(sorted({(f["geometry"] or {"type": "none"})["type"] for f in raw[s["key"]]["features"]})),
                          "block / context": s["block"], "snapshot": s["snapshot"], "licence": s["licence"]}
                         for s in sources]).set_index("key")


def compare_sources(common, kind=OWC.WindFarm, names=None):
    """Side-by-side raw values per farm and source, read from the common graph (one row per farm)."""
    recs = records(common)
    farms = {str(f): str(common.value(f, SCHEMA.name)) for f in common.subjects(RDF.type, kind)}
    recs = recs[recs.target.isin(farms)]
    recs["farm"] = recs.target.map(farms)
    recs["status"] = recs.status.str.rsplit("/", n=1).str[-1]
    agg = recs.groupby(["farm", "source"]).agg(MW=("power_mw", lambda v: v.astype(float).sum(min_count=1)),
                                              turbines=("n_turbines", lambda v: v.astype(float).sum(min_count=1)),
                                              status=("status", lambda v: "/".join(sorted(set(v.dropna())))),
                                              year=("year", lambda v: "/".join(sorted(set(map(str, v.dropna()))))))
    wide = agg.unstack("source")
    wide.columns = [f"{a} {b}" for a, b in wide.columns]
    t = turbines_table(common)
    wide["turbines mapped (OSM)"] = t.groupby(t.farm.map(farms)).size()
    if names is not None:
        wide = wide.loc[[n for n in names if n in wide.index]]
    return wide.dropna(axis=1, how="all")


def point_offsets(raw, a="emodnet-wfs", b="odp-points"):
    """Distance in metres between same-named points of two sources (Polish national grid EPSG:2180)."""
    import geopandas as gpd
    ga = gpd.GeoDataFrame.from_features(raw[a]["features"], crs="EPSG:4326").set_index("name").to_crs("EPSG:2180")
    gb = gpd.GeoDataFrame.from_features(raw[b]["features"], crs="EPSG:4326").set_index("name").to_crs("EPSG:2180")
    common_names = ga.index.intersection(gb.index)
    table = pd.DataFrame({f"in {b}": ga.index.isin(gb.index),
                          f"updateyear {a}": ga.updateyear, f"updateyear {b}": gb.updateyear.reindex(ga.index),
                          f"MW {a}": ga.power_mw, f"MW {b}": gb.power_mw.reindex(ga.index)}, index=ga.index)
    table.loc[common_names, "offset (m)"] = ga.loc[common_names].distance(gb.loc[common_names]).round(0)
    return table.sort_values(f"in {b}")


def turbine_to_point_distance(common):
    """Distance (km) between each farm's EMODnet point(s) centroid and its OSM turbine centroid."""
    pts = farm_reference_points(common)
    emodnet = pts[pts.method == "emodnet-wfs"]
    out = []
    recs = records(common)
    for _, row in pts[pts.method == "osm-turbine-centroid"].iterrows():
        e = recs[(recs.target == row.farm) & (recs.source == "emodnet-wfs") & recs.wkt.notna()].wkt
        if len(e):
            import geopandas as gpd
            from shapely import wkt
            c = gpd.GeoSeries([wkt.loads(_centroid_wkt(e)), row.geometry], crs="EPSG:4326").to_crs("EPSG:2180")
            out.append({"farm": row.farm.rsplit(":", 1)[-1], "EMODnet point → OSM turbine centroid (km)": round(c.iloc[0].distance(c.iloc[1]) / 1000, 2)})
    return pd.DataFrame(out).set_index("farm") if out else pd.DataFrame()


def value_choices(collection):
    """Which source supplied each chosen value, per farm (from ``value_source`` of farms-common)."""
    rows = {}
    for f in collection["features"]:
        vs = f["properties"].get("value_source") or []
        vs = [vs] if isinstance(vs, str) else vs
        rows[f["properties"]["name"]] = dict(v.split(": ", 1) for v in vs)
    return pd.DataFrame(rows).T


def layers(raw, collections=None):
    """Named map layers (GeoJSON collections) for viz.explore: raw sources and, optionally, harmonised output."""
    osm = raw["osm"]["features"]
    out = {"OSM farm areas": {"type": "FeatureCollection", "features": [f for f in osm if f["geometry"] and f["geometry"]["type"] == "Polygon"]},
           "OSM turbines": {"type": "FeatureCollection", "features": [f for f in osm if f["properties"]["tags"].get("power") == "generator"]},
           "EMODnet zones (WFS)": raw["emodnet-wfs-zones"], "EMODnet points (WFS)": raw["emodnet-wfs"],
           "ODP zones (tiles)": raw["odp-zones"], "ODP points (tiles)": raw["odp-points"]}
    if collections:
        out.update({f"harmonised {k}": v for k, v in collections.items() if k in ("farms-pl", "zones")})
    return out


# ------------------------------------------------------------------ pygeoapi
@lru_cache(maxsize=4)
def _cached_collections(stamp):
    return run()["collections"]


def _stamp():
    files = [EXERCISE / s["file"] for s in load_sources()] + sorted(CONFIG.rglob("*.*"))
    return tuple((str(p), p.stat().st_mtime) for p in files)


try:
    from pygeoapi.provider.base import BaseProvider, ProviderItemNotFoundError
except ImportError:                                     # the notebook can import this module without pygeoapi
    BaseProvider, ProviderItemNotFoundError = object, KeyError


class HarmonisedProvider(BaseProvider):
    """pygeoapi feature provider that runs the pipeline on the raw files on request (cached until a file changes).

    Configure with ``name: windfarm_harmonise.HarmonisedProvider``, ``data: farms-pl | farms-common | turbines | zones``.
    """

    def __init__(self, provider_def):
        super().__init__(provider_def)
        self.collection = provider_def["data"]
        self.get_fields()

    def _features(self):
        return _cached_collections(_stamp())[self.collection]["features"]

    def get_fields(self):
        if not self._fields:
            types = {float: "number", int: "integer", bool: "boolean", list: "array", dict: "object"}
            for f in self._features():
                for key, value in f["properties"].items():
                    self._fields.setdefault(key, {"type": types.get(type(value), "string")})
        return self._fields

    def query(self, offset=0, limit=10, resulttype="results", bbox=[], datetime_=None, properties=[], sortby=[],
              select_properties=[], skip_geometry=False, q=None, **kwargs):
        from shapely.geometry import box, shape
        feats = self._features()
        if bbox:
            area = box(*[float(v) for v in bbox])
            feats = [f for f in feats if f["geometry"] and shape(f["geometry"]).intersects(area)]
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
            if f["id"] == identifier or str(f["id"]).rsplit(":", 1)[-1] == identifier:
                return json.loads(json.dumps(f))
        raise ProviderItemNotFoundError(f"item {identifier} not found")


RAW_COLLECTIONS = {"national": "raw-national", "emodnet-wfs": "raw-emodnet-points", "emodnet-wfs-zones": "raw-emodnet-zones",
                   "odp-points": "raw-odp-points", "odp-zones": "raw-odp-zones", "osm": "raw-osm"}
HARMONISED = {
    "farms-pl": ("Wind farms, harmonised (emodnet-compliant-windfarm-pl)",
                 "One record per real-world farm in the published Polish target profile; values chosen by the projection policy.", "farms-pl"),
    "farms-common": ("Wind farms, common model with all source records",
                     "Every farm with the records of each source side by side and the source of each chosen value.", "common"),
    "turbines": ("Wind turbines (common model)", "Turbine positions with model, rotor and hub height, linked to their farm.", "common"),
    "zones": ("Planning zones (common model)", "Maritime spatial planning zones for offshore wind, with the farms they contain.", "common"),
}


def write_service(out_dir, result, config=CONFIG, port=5001):
    """Write raw collections, harmonised snapshots, the pygeoapi configuration and a launcher into ``out_dir``."""
    import yaml
    out_dir = Path(out_dir)
    (out_dir / "data").mkdir(parents=True, exist_ok=True)
    extent = {"spatial": {"bbox": [14.0, 54.0, 19.0, 56.0], "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"}}
    resources, blocks = {}, target_blocks(config)
    for source in result["sources"]:
        name = RAW_COLLECTIONS[source["key"]]
        fc = json.loads(json.dumps(result["raw"][source["key"]]))
        for f in fc["features"]:
            f["id"] = str(f.get("id")).replace("/", "-")          # OSM ids such as node/123 are not URL-path safe
        (out_dir / "data" / f"{name}.geojson").write_text(json.dumps(fc, ensure_ascii=False), encoding="utf-8")
        resources[name] = {
            "type": "collection", "title": f"RAW · {source['title']}",
            "description": f"Source records exactly as fetched on {source['snapshot']} ({source['licence']}). "
                           "f=jsonld applies the source's own building-block context: the uplift step.",
            "keywords": ["raw", source["key"]], "links": [{"type": "text/html", "rel": "canonical", "title": "source", "href": source["dataset"]}],
            "extents": extent, "itemType": "feature",
            "providers": [{"type": "feature", "name": "GeoJSON", "data": f"data/{name}.geojson", "id_field": "id"}],
            "linked-data": {"context": block(source["block"], config).context}}
    for name, (title, description, target) in HARMONISED.items():
        resources[name] = {
            "type": "collection", "title": title, "description": description,
            "keywords": ["harmonised", "windfarm"], "links": [], "extents": extent, "itemType": "feature",
            "providers": [{"type": "feature", "name": "windfarm_harmonise.HarmonisedProvider", "data": name, "id_field": "id"}],
            "linked-data": {"context": blocks[target].context}}
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


def start_service(service_dir, pygeoapi, port=5001, timeout=60):
    """Start pygeoapi from ``service_dir/run.sh`` and wait until it answers; returns the process (or None)."""
    import os, subprocess, time, urllib.request
    if not Path(pygeoapi).exists():
        return None
    process = subprocess.Popen(["sh", str(Path(service_dir) / "run.sh")], env={**os.environ, "PYGEOAPI": str(pygeoapi)},
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(timeout):
        try:
            urllib.request.urlopen(f"http://localhost:{port}/?f=json", timeout=2)
            return process
        except Exception:
            time.sleep(1)
    process.terminate()
    return None


def api_get(path, base="http://localhost:5001"):
    import urllib.request
    with urllib.request.urlopen(base + path, timeout=60) as response:
        return json.loads(response.read())
