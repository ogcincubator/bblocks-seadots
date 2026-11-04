#!/usr/bin/env python3
"""
Transform an OSM API 0.6 map response (windfarm-openstreetmap) into wind turbines
(common-windfarm-turbine), driven by the alignment in windfarm-openstreetmap/ontology.ttl.

The ontology declares which nodes are turbines (osmdata:TurbineElement and its selection rules)
and how their tags map onto owf: properties (osmdata:turbineTagMappings, with the same
TagMapping / ValueRule vocabulary as the wind farm areas). This script only interprets that
alignment and applies the element-level rules documented in the ontology: node -> Point
feature, membership of a wind farm relation (osmdata:WindfarmElement) -> windfarm and
windfarm_name, node timestamp -> last_updated.

Concepts are written as the target block's JSON terms (owf:HorizontalAxis -> "horizontal_axis",
inspire-cofv:underConstruction -> "underConstruction"), read from the target context.

OGC Building Blocks Python transform compatibility:
* when `input_data` is provided, assigns `output_data`;
* standalone: python3 osm_to_windfarm_turbine.py [--ontology ontology.ttl] < osm.json > turbines.geojson
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.collection import Collection

OSMD = Namespace("https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source/")
ONTOLOGY_IRI = URIRef("https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source")
KEY_NS = "https://www.openstreetmap.org/wiki/Key:"
OSM = "https://www.openstreetmap.org/"
BLOCK_DIR = "_sources/windfarms/windfarm-openstreetmap"
TARGET_CONTEXT = "_sources/windfarms/common-windfarm-turbine/context.jsonld"

FIELDS = ["ref", "windfarm_name", "windfarm", "manufacturer", "model", "rated_power_mw", "hub_height_m",
          "rotor_diameter_m", "rotor_axis", "offshore", "operator", "status", "last_updated"]


# ---------------------------------------------------------------- locating block files

def _meta(meta: Any, key: str):
    if not meta or not hasattr(meta, "get"):
        return None
    inner = meta.get("metadata")
    return meta.get(key) or (inner.get(key) if hasattr(inner, "get") else None)


def _here() -> Path | None:
    return Path(__file__).resolve().parent.parent if "__file__" in globals() else None


def _find(meta: Any, key: str, *defaults: Path) -> Path | None:
    candidates = [Path(p) for p in [_meta(meta, key)] if p] + list(defaults)
    return next((c for c in candidates if c.is_file()), None)


# ---------------------------------------------------------------- alignment

def tag_key(iri: URIRef) -> str:
    """Key IRI -> JSON tag key. Bare keys that are also prefixes carry a trailing colon."""
    key = str(iri)[len(KEY_NS):]
    return key[:-1] if key.endswith(":") else key


def rlist(g: Graph, node) -> list:
    return list(Collection(g, node)) if node is not None else []


def concept_terms(context_path: Path | None) -> dict[str, str]:
    """Concept IRI -> JSON term of the target block (e.g. owf:HorizontalAxis -> 'horizontal_axis')."""
    if not context_path:
        return {}
    ctx = json.loads(context_path.read_text(encoding="utf-8"))["@context"]
    prefixes = {k: v for k, v in ctx.items() if isinstance(v, str) and v.endswith(("#", "/"))}

    def expand(v: str) -> str:
        p, _, local = v.partition(":")
        return prefixes[p] + local if p in prefixes else v
    return {expand(v): k for k, v in ctx.items()
            if isinstance(v, str) and not k.startswith("@") and k not in prefixes and k[:1].islower()}


def _rules(g: Graph, node) -> list:
    out = []
    for r in rlist(g, node):
        value = g.value(r, OSMD.ruleValue)
        out.append((tag_key(g.value(r, OSMD.ruleKey)), str(value) if value is not None else None, g.value(r, OSMD.yields)))
    return out


def load_alignment(path: str | Path) -> dict[str, Any]:
    g = Graph().parse(str(path), format="turtle")
    mappings = [{"key": str(g.value(m, OSMD.targetKey)),
                 "sources": [tag_key(k) for k in rlist(g, g.value(m, OSMD.sourceKeys))],
                 "conversion": g.value(m, OSMD.conversion),
                 "rules": _rules(g, g.value(m, OSMD.valueRules))}
                for m in rlist(g, g.value(ONTOLOGY_IRI, OSMD.turbineTagMappings))]
    turbine = [(k, v) for k, v, _ in _rules(g, g.value(OSMD.TurbineElement, OSMD.selectionRules))]
    windfarm = [(k, v) for k, v, _ in _rules(g, g.value(OSMD.WindfarmElement, OSMD.selectionRules))]
    if not mappings or not turbine:
        raise ValueError(f"no turbine alignment found in {path}")
    return {"mappings": mappings, "turbine": turbine, "windfarm": windfarm}


# ---------------------------------------------------------------- conversions

def convert(conversion: URIRef | None, value: str) -> Any:
    if conversion is None or conversion == OSMD.Copy:
        return value
    if conversion == OSMD.ParseMegawatts:
        m = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*(?:MW)?\s*", value)
        return float(m.group(1)) if m else None
    if conversion == OSMD.ParseNumber:
        m = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*(?:m)?\s*", value)
        return float(m.group(1)) if m else None
    if conversion == OSMD.SplitSemicolon:
        return [v.strip() for v in value.split(";") if v.strip()] or None
    raise ValueError(f"unsupported conversion {conversion}")


def rule_result(yields: Any, terms: dict[str, str], value: str) -> Any:
    if yields == OSMD.Copy:
        return value
    if isinstance(yields, Literal):
        return yields.toPython()
    return terms.get(str(yields)) or re.split(r"[/#]", str(yields))[-1]


# ---------------------------------------------------------------- transform

def transform_response(src: dict, alignment: dict, terms: dict[str, str]) -> dict:
    elements = src["elements"]
    matches = lambda e, rules: any(e.get("tags", {}).get(k) == v for k, v in rules)
    farm_of = {}
    for rel in elements:
        if rel["type"] == "relation" and matches(rel, alignment["windfarm"]):
            for m in rel.get("members", []):
                if m["type"] == "node":
                    farm_of.setdefault(m["ref"], rel)
    features = []
    for el in elements:
        if el["type"] != "node" or not matches(el, alignment["turbine"]):
            continue
        tags = el.get("tags", {})
        props: dict[str, Any] = dict.fromkeys(FIELDS)
        for m in alignment["mappings"]:
            value = None
            raw = next((tags[k] for k in m["sources"] if k in tags), None)
            if raw is not None:
                value = convert(m["conversion"], raw)
            for key, match, yields in m["rules"]:
                if key in tags and (match is None or tags[key] == match):
                    value = rule_result(yields, terms, tags[key])
                    break
            props[m["key"]] = value
        farm = farm_of.get(el["id"])
        if farm:
            props["windfarm"] = f"{OSM}relation/{farm['id']}"
            props["windfarm_name"] = farm.get("tags", {}).get("name")
        props["last_updated"] = el.get("timestamp")
        features.append({"type": "Feature", "id": f"{OSM}node/{el['id']}",
                         "geometry": {"type": "Point", "coordinates": [el["lon"], el["lat"]]},
                         "properties": props})
    return {"type": "FeatureCollection", "features": features}


def transform(raw_json: str, meta: Any = None) -> str:
    here = _here()
    ontology = _find(meta, "ontology", Path(BLOCK_DIR) / "ontology.ttl", *([here / "ontology.ttl"] if here else []))
    if not ontology:
        raise FileNotFoundError("ontology.ttl of windfarm-openstreetmap not found")
    target = _find(meta, "target_context", Path(TARGET_CONTEXT),
                   *([here.parent / "common-windfarm-turbine/context.jsonld"] if here else []))
    out = transform_response(json.loads(raw_json), load_alignment(ontology), concept_terms(target))
    return json.dumps(out, indent=2, ensure_ascii=False)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--ontology"); ap.add_argument("--target-context")
    args = {k: v for k, v in vars(ap.parse_args()).items() if v}
    sys.stdout.write(transform(sys.stdin.read(), args) + "\n")
    return 0


if "input_data" in globals():
    output_data = transform(input_data, globals().get("metadata"))  # noqa: F821
elif __name__ == "__main__":
    raise SystemExit(main())
