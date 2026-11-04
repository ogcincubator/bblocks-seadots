#!/usr/bin/env python3
"""
Transform EMODnet Human Activities wind farm features (windfarm-designated-area-emodnet: WFS GeoJSON
output of emodnet:windfarms points and/or emodnet:windfarmspoly polygons) into windfarm designated
areas (common-windfarm-designated-area), driven by the alignment in
windfarm-designated-area-emodnet/ontology.ttl.

The ontology declares an emodnet:PropertyMapping for every target property (source JSON key,
conversion or constant, optionally limited to one WFS feature type). Status and country are looked
up among the seadots-emodnet: concepts by their English label. This script only interprets that
alignment and applies the record-level rules documented in the ontology:

* feature id windfarms.268 -> id = WFS GetFeature URL of that feature, source_record_id windfarms.268;
* geometry is kept as published;
* source_snapshot_date from metadata `source_snapshot_date`, else the date of the response timeStamp.

Concepts are written as the target block's JSON terms (owf:EmodnetSource -> "emodnet",
seadots-emodnet:Construction -> "Construction"), read from the target context.

OGC Building Blocks Python transform compatibility:
* when `input_data` is provided, assigns `output_data`;
* standalone: python3 emodnet_to_windfarm_area.py [--snapshot-date 2026-10-30] < wfs.geojson > areas.geojson
  (several WFS responses can be passed as files: ... a.geojson b.geojson > areas.geojson)
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
from rdflib.namespace import RDFS

EM = Namespace("https://w3id.org/ogc/hosted/seadots/emodnet/windfarm#")
SEM = "https://w3id.org/ogc/hosted/seadots/emodnet/"
ONTOLOGY_IRI = URIRef("https://w3id.org/ogc/hosted/seadots/offshore-windfarm")
BLOCK_DIR = "_sources/windfarms/windfarm-designated-area-emodnet"
TARGET_CONTEXT = "_sources/windfarms/common-windfarm-designated-area/context.jsonld"
WFS = "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:{type}&featureID={id}"

FIELDS = ["name", "country", "n_turbines", "power_mw", "status", "status_detail", "status_as_of",
          "type_inst", "offshore", "year", "year_semantics", "year_is_assumed", "updateyear",
          "operational_date", "valid_from", "dist_coast", "area_sqkm", "operator", "owner", "developer",
          "licence_status", "licensing_case", "admin_units", "electricity_price_area",
          "mean_annual_production_gwh", "notes", "source_type", "source_dataset", "source_reference",
          "source_record_id", "source_snapshot_date", "last_updated", "update_date", "metadata_record",
          "location_status", "location_method", "location_reference", "positional_accuracy_m", "same_as"]


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

def rlist(g: Graph, node) -> list:
    return list(Collection(g, node)) if node is not None else []


def concept_terms(context_path: Path | None) -> dict[str, str]:
    """Concept IRI -> JSON term of the target block (e.g. owf:EmodnetSource -> 'emodnet')."""
    if not context_path:
        return {}
    ctx = json.loads(context_path.read_text(encoding="utf-8"))["@context"]
    prefixes = {k: v for k, v in ctx.items() if isinstance(v, str) and v.endswith(("#", "/"))}

    def expand(v: str) -> str:
        p, _, local = v.partition(":")
        return prefixes[p] + local if p in prefixes else v
    return {expand(v): k for k, v in ctx.items()
            if isinstance(v, str) and not k.startswith("@") and k not in prefixes and k[:1].islower()}


def load_alignment(ontology: Path) -> dict:
    g = Graph().parse(str(ontology), format="turtle")
    labels = {str(label).lower(): s for s, label in g.subject_objects(RDFS.label)
              if str(s).startswith(SEM) and isinstance(label, Literal) and label.language == "en"}
    mappings = []
    for m in rlist(g, g.value(ONTOLOGY_IRI, EM.propertyMappings)):
        get = lambda p: g.value(m, p)
        mappings.append({"key": str(get(EM.targetKey)),
                         "source": str(get(EM.sourceKey)) if get(EM.sourceKey) is not None else None,
                         "conversion": get(EM.conversion), "constant": get(EM.constant),
                         "when_present": get(EM.whenPresent),
                         "feature_type": str(get(EM.forFeatureType)) if get(EM.forFeatureType) is not None else None})
    if not mappings:
        raise ValueError(f"no emodnet:propertyMappings found in {ontology}")
    return {"mappings": mappings, "labels": labels}


# ---------------------------------------------------------------- conversions

def as_json(node: Any, terms: dict[str, str]) -> Any:
    if node is None:
        return None
    if isinstance(node, Literal):
        return node.toPython()
    return terms.get(str(node)) or re.split(r"[/#]", str(node))[-1]


def convert(conversion: URIRef | None, value: Any, labels: dict, terms: dict) -> Any:
    if value is None or (isinstance(value, str) and not value.strip()):
        return None
    if conversion is None or conversion == EM.Copy:
        return value.strip() if isinstance(value, str) else value
    if conversion in (EM.ParseNumber, EM.ParseInteger):
        try:
            number = float(value)
        except (TypeError, ValueError):
            return None
        if conversion == EM.ParseInteger:
            return int(number) if number.is_integer() else None
        return int(number) if number.is_integer() and isinstance(value, int) else number
    if conversion == EM.YearString:
        m = re.fullmatch(r"\s*(\d{4})(?:\.0+)?\s*", str(value))
        return m.group(1) if m else str(value)
    if conversion == EM.ConceptByLabel:
        concept = labels.get(str(value).strip().lower())
        return as_json(concept, terms) if concept is not None else None
    raise ValueError(f"unsupported conversion {conversion}")


# ---------------------------------------------------------------- transform

def transform_features(responses: list[dict], alignment: dict, terms: dict[str, str],
                       snapshot_date: str | None = None) -> dict:
    features = []
    for response in responses:
        stamp = snapshot_date or (str(response.get("timeStamp", ""))[:10] or None)
        for f in response.get("features", []):
            fid = str(f["id"])
            ftype = fid.split(".", 1)[0]
            src = f.get("properties") or {}
            props: dict[str, Any] = dict.fromkeys(FIELDS)
            for m in alignment["mappings"]:
                if m["feature_type"] and m["feature_type"] != ftype:
                    continue
                if m["constant"] is not None:
                    props[m["key"]] = as_json(m["constant"], terms)
                elif m["when_present"] is not None:
                    if src.get(m["source"]) not in (None, ""):
                        props[m["key"]] = as_json(m["when_present"], terms)
                else:
                    props[m["key"]] = convert(m["conversion"], src.get(m["source"]), alignment["labels"], terms)
            props["source_record_id"] = fid
            props["source_snapshot_date"] = stamp
            features.append({"type": "Feature", "id": WFS.format(type=ftype, id=fid),
                             "geometry": f.get("geometry"), "properties": props})
    return {"type": "FeatureCollection", "features": features}


def transform(raw_json: str | list, meta: Any = None) -> str:
    here = _here()
    ontology = _find(meta, "ontology", Path(BLOCK_DIR) / "ontology.ttl", *([here / "ontology.ttl"] if here else []))
    if not ontology:
        raise FileNotFoundError("ontology.ttl of windfarm-designated-area-emodnet not found")
    target = _find(meta, "target_context", Path(TARGET_CONTEXT),
                   *([here.parent / "common-windfarm-designated-area/context.jsonld"] if here else []))
    responses = raw_json if isinstance(raw_json, list) else [json.loads(raw_json)]
    responses = [json.loads(r) if isinstance(r, str) else r for r in responses]
    out = transform_features(responses, load_alignment(ontology), concept_terms(target),
                             _meta(meta, "source_snapshot_date"))
    return json.dumps(out, indent=2, ensure_ascii=False)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("files", nargs="*", help="WFS GeoJSON responses (default: stdin)")
    ap.add_argument("--ontology"); ap.add_argument("--target-context"); ap.add_argument("--snapshot-date", dest="source_snapshot_date")
    args = vars(ap.parse_args())
    files = args.pop("files")
    inputs = [Path(p).read_text(encoding="utf-8") for p in files] if files else [sys.stdin.read()]
    sys.stdout.write(transform(inputs, {k: v for k, v in args.items() if v}) + "\n")
    return 0


if "input_data" in globals():
    output_data = transform(input_data, globals().get("metadata"))  # noqa: F821
elif __name__ == "__main__":
    raise SystemExit(main())
