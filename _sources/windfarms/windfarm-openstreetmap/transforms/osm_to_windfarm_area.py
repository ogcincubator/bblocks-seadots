#!/usr/bin/env python3
"""
Transform an OSM API 0.6 map response (windfarm-openstreetmap) into windfarm
designated areas (common-windfarm-designated-area), driven by the alignment in
windfarm-openstreetmap/ontology.ttl.

The ontology declares which elements are wind farms (osmdata:WindfarmElement and
its osmdata:selectionRules) and how tags map onto owf: properties
(osmdata:windfarmTagMappings: source keys, value rules, conversions). This script
only interprets that alignment and applies the element-level rules documented in
the ontology (merging relation parts, geometry, provenance).

OGC Building Blocks Python transform compatibility:
* when `input_data` is provided, assigns `output_data`;
* when run standalone: python3 osm_to_windfarm_area.py [ontology.ttl] < osm.json > areas.json

The ontology is located from transform metadata `ontology`, then
_sources/windfarms/windfarm-openstreetmap/ontology.ttl relative to the working
directory, then next to this script.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

from pyproj import Geod
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.collection import Collection
from rdflib.namespace import RDF

OSMD = Namespace("https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source/")
ONTOLOGY_IRI = URIRef("https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source")
KEY_NS = "https://www.openstreetmap.org/wiki/Key:"
OSM = "https://www.openstreetmap.org/"
ONTOLOGY_PATH = "_sources/windfarms/windfarm-openstreetmap/ontology.ttl"

FIELDS = ["name", "country", "n_turbines", "power_mw", "status", "status_detail", "status_as_of",
          "type_inst", "offshore", "year", "year_semantics", "year_is_assumed", "updateyear",
          "operational_date", "valid_from", "dist_coast", "area_sqkm", "operator", "owner", "developer",
          "licence_status", "licensing_case", "admin_units", "electricity_price_area",
          "mean_annual_production_gwh", "notes", "source_type", "source_dataset", "source_reference",
          "source_record_id", "source_snapshot_date", "last_updated", "update_date", "metadata_record",
          "location_status", "location_method", "location_reference", "positional_accuracy_m", "same_as"]


# ---------------------------------------------------------------- alignment

def tag_key(iri: URIRef) -> str:
    """Key IRI -> JSON tag key. Bare keys that are also prefixes carry a trailing colon."""
    key = str(iri)[len(KEY_NS):]
    return key[:-1] if key.endswith(":") else key


def local_name(iri: URIRef) -> str:
    return re.split(r"[/#]", str(iri))[-1]


def rlist(g: Graph, node) -> list:
    return list(Collection(g, node)) if node is not None else []


def load_alignment(path: str | Path) -> dict[str, Any]:
    g = Graph().parse(str(path), format="turtle")
    selection = [(tag_key(g.value(r, OSMD.ruleKey)), str(g.value(r, OSMD.ruleValue)))
                 for r in rlist(g, g.value(OSMD.WindfarmElement, OSMD.selectionRules))]
    mappings = []
    for m in rlist(g, g.value(ONTOLOGY_IRI, OSMD.windfarmTagMappings)):
        rules = []
        for r in rlist(g, g.value(m, OSMD.valueRules)):
            value = g.value(r, OSMD.ruleValue)
            rules.append((tag_key(g.value(r, OSMD.ruleKey)), str(value) if value is not None else None,
                          g.value(r, OSMD.yields)))
        when = g.value(m, OSMD.whenPresent)
        mappings.append({
            "key": str(g.value(m, OSMD.targetKey)),
            "sources": [tag_key(k) for k in rlist(g, g.value(m, OSMD.sourceKeys))],
            "conversion": g.value(m, OSMD.conversion),
            "fallback": g.value(m, OSMD.fallback),
            "rules": rules,
            "when_present": str(when) if when is not None else None,
        })
    if not selection or not mappings:
        raise ValueError(f"no windfarm alignment found in {path}")
    return {"selection": selection, "mappings": mappings}


def find_ontology(meta: Any) -> Path:
    candidates = []
    if meta:
        inner = meta.get("metadata") if hasattr(meta, "get") else None
        for src in (meta, inner):
            if src and hasattr(src, "get") and src.get("ontology"):
                candidates.append(Path(src.get("ontology")))
    candidates.append(Path(ONTOLOGY_PATH))
    if "__file__" in globals():
        candidates.append(Path(__file__).resolve().parent.parent / "ontology.ttl")
    for c in candidates:
        if c.is_file():
            return c
    raise FileNotFoundError(f"ontology with the windfarm alignment not found; tried {candidates}")


# ---------------------------------------------------------------- conversions

def convert(conversion: URIRef | None, value: str) -> Any:
    if conversion is None or conversion == OSMD.Copy:
        return value
    if conversion == OSMD.ParseInteger:
        return int(value) if re.fullmatch(r"\s*\d+\s*", value) else None
    if conversion == OSMD.ParseMegawatts:
        m = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*(?:MW)?\s*", value)
        return float(m.group(1)) if m else None
    if conversion == OSMD.SplitSemicolon:
        return [v.strip() for v in value.split(";") if v.strip()] or None
    raise ValueError(f"unsupported conversion {conversion}")


def rule_result(yields: Any, key: str, value: str) -> Any:
    if yields == OSMD.Copy:
        return value
    if yields == OSMD.KeyEqualsValue:
        return f"{key}={value}"
    if isinstance(yields, Literal):
        return yields.toPython()
    return local_name(yields)          # concept -> its code, e.g. seadots-emodnet:Construction -> "Construction"


# ---------------------------------------------------------------- transform

def transform_response(src: dict, alignment: dict, snapshot_date: str | None = None) -> dict:
    elements = src["elements"]
    index = {(e["type"], e["id"]): e for e in elements}
    selected = [e for e in elements if e["type"] in ("way", "relation")
                and any(e.get("tags", {}).get(k) == v for k, v in alignment["selection"])]
    relations = [e for e in selected if e["type"] == "relation"]

    def outer_ways(rel):
        return [index[("way", m["ref"])] for m in rel["members"]
                if m["type"] == "way" and m["role"] == "outer" and ("way", m["ref"]) in index]

    def same_name_ways(rel):
        name = rel.get("tags", {}).get("name")
        return [w for w in selected if w["type"] == "way" and name and w.get("tags", {}).get("name") == name
                and w not in outer_ways(rel)]

    merged = {w["id"] for r in relations for w in outer_ways(r) + same_name_ways(r)}
    primaries = relations + [w for w in selected if w["type"] == "way" and w["id"] not in merged]

    b = src["bounds"]
    source_reference = (f"https://api.openstreetmap.org/api/0.6/map.json?bbox="
                        f"{b['minlon']},{b['minlat']},{b['maxlon']},{b['maxlat']}")
    geod = Geod(ellps="WGS84")
    features = []
    for el in primaries:
        parts = outer_ways(el) + same_name_ways(el) if el["type"] == "relation" else []
        chain = [el] + parts

        def tag(key):
            for p in chain:
                if key in p.get("tags", {}):
                    return p["tags"][key]
            return None

        props: dict[str, Any] = {k: None for k in FIELDS}
        for m in alignment["mappings"]:
            value = None
            if m["sources"]:
                raw = next((tag(k) for k in m["sources"] if tag(k) is not None), None)
                if raw is not None:
                    value = m["when_present"] if m["when_present"] else convert(m["conversion"], raw)
                elif m["fallback"] == OSMD.CountGeneratorMembers:
                    n = sum(1 for x in el.get("members", []) if x["role"] == "generator")
                    value = n or None
            for key, match, yields in m["rules"]:
                v = tag(key)
                if v is not None and (match is None or v == match):
                    value = rule_result(yields, key, v)
                    break
            props[m["key"]] = value

        area_way = el if el["type"] == "way" else (outer_ways(el) or [None])[0]
        geometry = None
        if area_way:
            ring = [[index[("node", n)]["lon"], index[("node", n)]["lat"]] for n in area_way["nodes"]]
            geometry = {"type": "Polygon", "coordinates": [ring]}
            area, _ = geod.polygon_area_perimeter([c[0] for c in ring], [c[1] for c in ring])
            props["area_sqkm"] = round(abs(area) / 1e6, 3)
        props.update({
            "source_type": "osm",
            "source_dataset": "OpenStreetMap",
            "source_reference": source_reference,
            "source_record_id": f"{el['type']}/{el['id']}",
            "source_snapshot_date": snapshot_date,
            "last_updated": max(p["timestamp"] for p in chain),
            "location_status": "source-provided" if geometry else "unmatched",
            "location_method": (f"outer way {area_way['id']} of the OSM element" if geometry else
                                "no OSM area contains this wind farm's turbines; geometry left null"),
            "same_as": [f"{OSM}way/{p['id']}" for p in parts] or None,
        })
        features.append({"type": "Feature", "id": f"{OSM}{el['type']}/{el['id']}",
                         "geometry": geometry, "properties": props})
    return {"type": "FeatureCollection", "features": features}


def transform(raw_json: str, meta: Any = None) -> str:
    alignment = load_alignment(find_ontology(meta))
    snapshot = None
    if meta and hasattr(meta, "get"):
        inner = meta.get("metadata") or {}
        snapshot = meta.get("source_snapshot_date") or (inner.get("source_snapshot_date") if hasattr(inner, "get") else None)
    return json.dumps(transform_response(json.loads(raw_json), alignment, snapshot), indent=2, ensure_ascii=False)


def main() -> int:
    meta = {"ontology": sys.argv[1]} if len(sys.argv) > 1 else {}
    if len(sys.argv) > 2:
        meta["source_snapshot_date"] = sys.argv[2]
    sys.stdout.write(transform(sys.stdin.read(), meta) + "\n")
    return 0


if "input_data" in globals():
    output_data = transform(input_data, globals().get("metadata"))  # noqa: F821
elif __name__ == "__main__":
    raise SystemExit(main())
