#!/usr/bin/env python3
"""
Transform the Polish national offshore wind project compilation (national-windfarm-source,
CSV from gramwzielone.pl) into windfarm designated areas (common-windfarm-designated-area),
driven by the alignment in national-windfarm-source/ontology.ttl.

The ontology declares, for every target property, an ns:ColumnMapping: the source columns
(as the properties of this block's context.jsonld, e.g. ns:reportedCapacityMW = column
`capacity_mw`), a conversion, ordered value rules or a constant. This script only interprets
that alignment and applies the record-level rules documented in the ontology:

* one CSV row -> one Feature, id urn:baltic-ses:national:{row}:{slug}, source_record_id national-{row};
* the source has no coordinates -> geometry null, location_status "unmatched";
* optional location crosswalk (metadata `crosswalk`, `emodnet_snapshot`): the project's EMODnet
  sites become `same_as` links (EMODnet WFS feature URLs, the ids used by the EMODnet records of
  the common model), the geometry their centroid with location_status "mapped"; a separately
  documented approximate point gives location_status "anticipated".

Concepts are written as the target block's JSON terms (owf:NationalSource -> "national",
seadots-emodnet:Construction -> "Construction"), read from the target context.

OGC Building Blocks Python transform compatibility:
* when `input_data` is provided, assigns `output_data`;
* standalone: python3 national_to_windfarm_area.py [--crosswalk mapping.json --emodnet snapshot.geojson] < pipeline.csv > areas.geojson
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Any

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.collection import Collection

NS = Namespace("https://w3id.org/ogc/hosted/seadots/national-windfarm-source#")
ONTOLOGY_IRI = URIRef("https://w3id.org/ogc/hosted/seadots/national-windfarm-source")
BLOCK_DIR = "_sources/national-windfarm-source"
TARGET_CONTEXT = "_sources/windfarms/common-windfarm-designated-area/context.jsonld"
EMODNET_WFS = ("https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature"
               "&typeNames=emodnet:windfarms&featureID=")

FIELDS = ["name", "country", "n_turbines", "power_mw", "status", "status_detail", "status_as_of",
          "type_inst", "offshore", "year", "year_semantics", "year_is_assumed", "updateyear",
          "operational_date", "dist_coast", "area_sqkm", "operator", "owner", "developer",
          "licence_status", "licensing_case", "admin_units", "electricity_price_area",
          "mean_annual_production_gwh", "notes", "source_type", "source_dataset", "source_reference",
          "source_record_id", "source_snapshot_date", "last_updated", "location_status",
          "location_method", "location_reference", "same_as"]


# ---------------------------------------------------------------- locating block files

def _meta(meta: Any, key: str):
    if not meta or not hasattr(meta, "get"):
        return None
    inner = meta.get("metadata")
    return meta.get(key) or (inner.get(key) if hasattr(inner, "get") else None)


def _find(meta: Any, key: str, *defaults: Path) -> Path | None:
    candidates = [Path(p) for p in [_meta(meta, key)] if p] + list(defaults)
    return next((c for c in candidates if c.is_file()), None)


def _here() -> Path | None:
    return Path(__file__).resolve().parent.parent if "__file__" in globals() else None


def block_file(meta: Any, key: str, name: str) -> Path:
    here = _here()
    found = _find(meta, key, Path(BLOCK_DIR) / name, *([here / name] if here else []))
    if not found:
        raise FileNotFoundError(f"{name} of national-windfarm-source not found")
    return found


# ---------------------------------------------------------------- alignment

def rlist(g: Graph, node) -> list:
    return list(Collection(g, node)) if node is not None else []


def column_names(context_path: Path) -> dict[str, str]:
    """Property IRI -> CSV column, from the source block's JSON-LD context."""
    ctx = json.loads(context_path.read_text(encoding="utf-8"))["@context"]
    vocab = ctx.get("@vocab", "")
    out = {}
    for term, value in ctx.items():
        iri = value if isinstance(value, str) else value.get("@id") if isinstance(value, dict) else None
        if not iri or term.startswith("@"):
            continue
        out[iri if ":" in iri and "/" in iri else vocab + iri] = term
    return out


def concept_terms(context_path: Path | None) -> dict[str, str]:
    """Concept IRI -> JSON term of the target block (e.g. owf:NationalSource -> 'national')."""
    if not context_path:
        return {}
    ctx = json.loads(context_path.read_text(encoding="utf-8"))["@context"]
    prefixes = {k: v for k, v in ctx.items() if isinstance(v, str) and v.endswith(("#", "/"))}

    def expand(v: str) -> str:
        p, _, local = v.partition(":")
        return prefixes[p] + local if p in prefixes else v
    return {expand(v): k for k, v in ctx.items()
            if isinstance(v, str) and not k.startswith("@") and k not in prefixes and k[:1].islower()}


def load_alignment(ontology: Path, context: Path) -> list[dict]:
    g = Graph().parse(str(ontology), format="turtle")
    cols = column_names(context)

    def col(iri) -> str:
        # the source context writes dcterms as https://purl.org/dc/terms/; accept either scheme
        for candidate in (str(iri), re.sub(r"^http:", "https:", str(iri)), re.sub(r"^https:", "http:", str(iri))):
            if candidate in cols:
                return cols[candidate]
        if str(iri) not in cols:
            raise ValueError(f"{iri} is not a column of the source context")
        return cols[str(iri)]

    mappings = []
    for m in rlist(g, g.value(ONTOLOGY_IRI, NS.columnMappings)):
        mappings.append({
            "key": str(g.value(m, NS.targetKey)),
            "columns": [col(c) for c in rlist(g, g.value(m, NS.sourceColumns))],
            "conversion": g.value(m, NS.conversion),
            "constant": g.value(m, NS.constant),
            "rules": [(col(g.value(r, NS.ruleColumn)), str(g.value(r, NS.rulePattern)), g.value(r, NS.yields))
                      for r in rlist(g, g.value(m, NS.valueRules))],
        })
    if not mappings:
        raise ValueError(f"no ns:columnMappings found in {ontology}")
    return mappings


# ---------------------------------------------------------------- conversions

DATE = re.compile(r"(\d{1,2})\s+([A-Za-z]{3})[a-z]*\.?\s+(\d{4})")


def convert(conversion: URIRef | None, value: str) -> Any:
    value = value.strip()
    if conversion is None or conversion == NS.Copy:
        return value or None
    if conversion == NS.ParseDecimal:
        try:
            number = float(value.replace(",", "."))
        except ValueError:
            return None
        return int(number) if number.is_integer() else number
    if conversion == NS.ParenthesisText:
        m = re.search(r"\(([^)]*)\)", value)
        return m.group(1).strip() if m else None
    if conversion in (NS.ParseReportDate, NS.ParseReportYear):
        m = DATE.search(value)
        if not m:
            return None
        day = datetime.strptime(f"{m.group(1)} {m.group(2)[:3].title()} {m.group(3)}", "%d %b %Y").date()
        return day.isoformat() if conversion == NS.ParseReportDate else str(day.year)
    raise ValueError(f"unsupported conversion {conversion}")


def as_json(node: Any, terms: dict[str, str]) -> Any:
    if node is None:
        return None
    if isinstance(node, Literal):
        return node.toPython()
    return terms.get(str(node)) or re.split(r"[/#]", str(node))[-1]   # concept -> JSON term / code


def apply(mapping: dict, row: dict[str, str], terms: dict[str, str]) -> Any:
    if mapping["constant"] is not None:
        return as_json(mapping["constant"], terms)
    for column, pattern, yields in mapping["rules"]:
        if re.search(pattern, row.get(column) or "", re.IGNORECASE):
            return as_json(yields, terms)
    for column in mapping["columns"]:
        if (row.get(column) or "").strip():
            return convert(mapping["conversion"], row[column])
    return None


# ---------------------------------------------------------------- record-level rules

def slug(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def locate(name: str, crosswalk: dict | None, emodnet: dict | None) -> dict:
    """Geometry and location properties of one project from the optional crosswalk."""
    if not crosswalk:
        return {"geometry": None, "location_status": "unmatched",
                "location_method": "The national source has no coordinates and no location crosswalk was applied."}
    by_name = {f["properties"].get("name"): f for f in (emodnet or {}).get("features", [])}
    sites = [by_name[n] for n in crosswalk.get("mappings", {}).get(name, []) if n in by_name]
    if sites:
        ids = [str(f["id"]) for f in sites]
        xs = [f["geometry"]["coordinates"][0] for f in sites]
        ys = [f["geometry"]["coordinates"][1] for f in sites]
        names = ", ".join(f["properties"]["name"] for f in sites)
        return {"geometry": {"type": "Point", "coordinates": [round(sum(xs) / len(xs), 6), round(sum(ys) / len(ys), 6)]},
                "location_status": "mapped",
                "location_method": (f"Explicit name crosswalk to EMODnet site(s) {names}; "
                                    + ("centroid of their EMODnet points." if len(sites) > 1 else "its EMODnet point.")),
                "location_reference": EMODNET_WFS + ",".join(ids),
                "same_as": [EMODNET_WFS + i for i in ids]}
    anticipated = crosswalk.get("anticipated_locations", {}).get(name)
    if anticipated:
        confidence = anticipated.get("confidence")
        return {"geometry": anticipated["geometry"], "location_status": "anticipated",
                "location_method": anticipated["method"] + (f" Confidence: {confidence}." if confidence else ""),
                "location_reference": anticipated.get("reference")}
    reason = crosswalk.get("unmatched_reasons", {}).get(name)
    return {"geometry": None, "location_status": "unmatched",
            "location_method": reason or "No EMODnet site listed for this project in the location crosswalk."}


def transform_rows(rows: list[dict], mappings: list[dict], terms: dict[str, str],
                   crosswalk: dict | None = None, emodnet: dict | None = None) -> dict:
    features = []
    for n, row in enumerate(rows, start=1):
        props: dict[str, Any] = dict.fromkeys(FIELDS)
        for m in mappings:
            props[m["key"]] = apply(m, row, terms)
        loc = locate(props["name"] or "", crosswalk, emodnet)
        geometry = loc.pop("geometry")
        props.update(loc)
        props["source_record_id"] = f"national-{n}"
        features.append({"type": "Feature", "id": f"urn:baltic-ses:national:{n}:{slug(props['name'] or str(n))}",
                         "geometry": geometry, "properties": props})
    return {"type": "FeatureCollection", "features": features}


def transform(raw_csv: str, meta: Any = None) -> str:
    ontology = block_file(meta, "ontology", "ontology.ttl")
    context = block_file(meta, "source_context", "context.jsonld")
    here = _here()
    target = _find(meta, "target_context", Path(TARGET_CONTEXT),
                   *([here.parent / "windfarms/common-windfarm-designated-area/context.jsonld"] if here else []))
    crosswalk_path = _find(meta, "crosswalk") if _meta(meta, "crosswalk") else None
    emodnet_path = _find(meta, "emodnet_snapshot") if _meta(meta, "emodnet_snapshot") else None
    load = lambda p: json.loads(p.read_text(encoding="utf-8")) if p else None
    rows = list(csv.DictReader(io.StringIO(raw_csv)))
    out = transform_rows(rows, load_alignment(ontology, context), concept_terms(target),
                         load(crosswalk_path), load(emodnet_path))
    return json.dumps(out, indent=2, ensure_ascii=False)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--ontology"); ap.add_argument("--source-context"); ap.add_argument("--target-context")
    ap.add_argument("--crosswalk"); ap.add_argument("--emodnet", dest="emodnet_snapshot")
    args = {k: v for k, v in vars(ap.parse_args()).items() if v}
    sys.stdout.write(transform(sys.stdin.read(), args) + "\n")
    return 0


if "input_data" in globals():
    output_data = transform(input_data, globals().get("metadata"))  # noqa: F821
elif __name__ == "__main__":
    raise SystemExit(main())
