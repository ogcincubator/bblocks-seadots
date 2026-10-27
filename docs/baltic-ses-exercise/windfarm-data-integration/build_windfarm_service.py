#!/usr/bin/env python3
"""Build the standalone windfarm source-comparison pygeoapi exercise."""
from __future__ import annotations

import csv
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent
EXERCISE = ROOT.parent
DATA = EXERCISE / "data"
OUT = ROOT / "service"
NATIONAL = DATA / "polish_offshore_wind_pipeline.csv"
EMODNET = DATA / "emodnet_windfarms_poland_2026-10-26.csv"
MAPPING = ROOT / "config/location-mapping.json"
REPO = Path(__file__).resolve().parents[3]
TARGET_CONTEXT = REPO / "_sources/emodnet-compliant-windfarm/baltic-project-extension/context.jsonld"
NATIONAL_CONTEXT = REPO / "_sources/national-windfarm-source/context.jsonld"
EMODNET_CONTEXT = REPO / "_sources/emodnet-windfarm-source/context.jsonld"
TARGET_SCHEMA = REPO / "_sources/emodnet-compliant-windfarm/baltic-project-extension/schema.yaml"
NATIONAL_TRANSLATION = REPO / "_sources/national-windfarm-source/translation.json"
EMODNET_TRANSLATION = REPO / "_sources/emodnet-windfarm-source/translation.json"
NATIONAL_REFERENCE = "https://www.gramwzielone.pl/?p=20373718"
EMODNET_REFERENCE = "https://ows.emodnet-humanactivities.eu/wfs"
SNAPSHOT = "2026-10-26"


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def number(value):
    return None if value in (None, "") else float(value)


def integer(value):
    return None if value in (None, "") else int(float(value))


def feature(identifier, geometry, properties):
    return {"type": "Feature", "id": identifier, "geometry": geometry, "properties": properties}


def collection(features):
    return {"type": "FeatureCollection", "features": features}


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main():
    national = read_csv(NATIONAL)
    emodnet = read_csv(EMODNET)
    mapping = json.loads(MAPPING.read_text(encoding="utf-8"))
    national_map = json.loads(NATIONAL_TRANSLATION.read_text(encoding="utf-8"))["field_map"]
    emodnet_map = json.loads(EMODNET_TRANSLATION.read_text(encoding="utf-8"))["field_map"]
    target_schema = yaml.safe_load(TARGET_SCHEMA.read_text(encoding="utf-8"))
    target_properties = target_schema["$defs"]["sparseFeature"]["properties"]["properties"]["properties"]
    sites = {row["name"]: row for row in emodnet}
    site_ids = {row["name"]: f"emodnet-{i}" for i, row in enumerate(emodnet, 1)}

    # Raw collections deliberately retain source field names and values.
    raw_national = [feature(f"national-{i+1}", None, row) for i, row in enumerate(national)]
    raw_emodnet = []
    for i, row in enumerate(emodnet, 1):
        geom = None if not row.get("lon") or not row.get("lat") else {
            "type": "Point", "coordinates": [float(row["lon"]), float(row["lat"])]
        }
        raw_emodnet.append(feature(f"emodnet-{i}", geom, row))

    canonical = []
    for i, row in enumerate(emodnet, 1):
        canonical.append(feature(
            f"http://localhost:5000/collections/harmonized-windfarms/items/emodnet-{i}",
            raw_emodnet[i-1]["geometry"],
            {**{key: None for key in target_properties}, "name": row[emodnet_map["name"]], "country": "Poland",
             "n_turbines": integer(row[emodnet_map["n_turbines"]]),
             "power_mw": number(row[emodnet_map["power_mw"]]), "status": row[emodnet_map["status"]] or None,
             "updateyear": row[emodnet_map["updateyear"]] or None, "year": row[emodnet_map["year"]] or None,
             "dist_coast": number(row[emodnet_map["dist_coast"]]),
             "status_detail": row[emodnet_map["status"]] or None,
             "year_semantics": "year reported by EMODnet", "year_is_assumed": False,
             "source_type": "emodnet", "source_dataset": "EMODnet Human Activities windfarms, Poland snapshot",
             "source_reference": EMODNET_REFERENCE, "source_snapshot_date": SNAPSHOT,
             "source_record_id": row["name"], "location_status": "source-provided",
             "location_method": "EMODnet source point", "location_reference": EMODNET_REFERENCE,
             "location_emodnet_ids": []}
        ))

    for i, row in enumerate(national, 1):
        national_name = row[national_map["name"]]
        names = mapping["mappings"].get(national_name, [])
        matched = [sites[name] for name in names if name in sites]
        geom = None
        loc_status, method = "unmatched", None
        if matched:
            lon = sum(float(s["lon"]) for s in matched) / len(matched)
            lat = sum(float(s["lat"]) for s in matched) / len(matched)
            geom = {"type": "Point", "coordinates": [lon, lat]}
            loc_status = "mapped"
            method = "centroid of mapped EMODnet point(s); explicit project-name crosswalk"
        anticipated = mapping.get("anticipated_locations", {}).get(national_name)
        if not matched and anticipated:
            geom = anticipated["geometry"]
            loc_status = "anticipated"
            method = anticipated["method"]
        status_detail = row[national_map["status_detail"]]
        status = status_detail.split("(", 1)[0].strip().title() or None
        canonical.append(feature(
            f"http://localhost:5000/collections/harmonized-windfarms/items/national-{i}", geom,
            {**{key: None for key in target_properties}, "name": national_name, "country": "Poland",
             "power_mw": number(row[national_map["power_mw"]]), "status": status,
             "updateyear": "2026", "year": row[national_map["year"]] or None,
             "dist_coast": (sum(float(s["dist_coast_m"]) for s in matched if s.get("dist_coast_m")) /
                            sum(1 for s in matched if s.get("dist_coast_m"))) if any(s.get("dist_coast_m") for s in matched) else None,
             "notes": row[national_map["notes"]], "developer": row[national_map["developer"]], "status_detail": status_detail,
             "status_as_of": "2026-08-26", "year_semantics": "planned first-power or completion year",
             "year_is_assumed": "assumed" in row["source"].lower(), "source_type": "national",
             "source_dataset": "Polish national offshore wind project compilation",
             "source_reference": NATIONAL_REFERENCE, "source_snapshot_date": "2026-08-26",
             "source_record_id": national_name, "location_status": loc_status,
             "location_method": method,
             "location_reference": (anticipated["reference"] if not matched and anticipated else
                                    EMODNET_REFERENCE if matched else None),
            "location_emodnet_ids": [f"http://localhost:5000/collections/emodnet-source/items/{site_ids[name]}" for name in names if name in site_ids]}
        ))

    write_json(OUT / "data/national-source.geojson", collection(raw_national))
    write_json(OUT / "data/emodnet-source.geojson", collection(raw_emodnet))
    write_json(OUT / "data/harmonized-windfarms.geojson", collection(canonical))

    contexts = [json.loads(p.read_text(encoding="utf-8"))["@context"] for p in (NATIONAL_CONTEXT, EMODNET_CONTEXT, TARGET_CONTEXT)]
    resources = {}
    for name, title, desc, datafile, context in [
        ("national-source", "National source (raw)", "Raw national project records; source geometry is absent.", "national-source.geojson", contexts[0]),
        ("emodnet-source", "EMODnet source (raw)", "Raw EMODnet windfarm features for Poland.", "emodnet-source.geojson", contexts[1]),
        ("harmonized-windfarms", "Harmonized windfarms", "Canonical target records with explicit provenance and location matching.", "harmonized-windfarms.geojson", contexts[2]),
    ]:
        resources[name] = {"type": "collection", "title": title, "description": desc,
                          "keywords": ["windfarm", "Baltic", "harmonisation"],
                          "links": [], "extents": {"spatial": {"bbox": [13.0, 53.0, 21.0, 58.0], "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"}},
                          "itemType": "feature", "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84",
                          "providers": [{"type": "feature", "name": "GeoJSON", "data": f"data/{datafile}", "id_field": "id"}],
                          "linked-data": {"context": [context]}}
    config = {"server": {"bind": {"host": "127.0.0.1", "port": 5000}, "url": "http://localhost:5000", "mimetype": "application/json; charset=UTF-8",
                          "encoding": "utf-8", "language": "en-US", "limit": 100, "max_limit": 10000,
                          "map": {"url": "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                                  "attribution": "© OpenStreetMap contributors"},
                          "templates": {"path": "templates", "static": "static"}},
              "logging": {"level": "ERROR"},
              "metadata": {"identification": {"title": "Baltic windfarm source comparison",
                 "description": "Exercise API for comparing raw national and EMODnet data with a harmonized linked-data view.",
                 "keywords": ["Baltic", "windfarms", "linked data"], "keywords_type": "theme",
                 "terms_of_service": "https://creativecommons.org/licenses/by/4.0/",
                 "url": "https://github.com/opengeospatial/bblocks-seadots"},
                 "license": {"name": "CC-BY-4.0", "url": "https://creativecommons.org/licenses/by/4.0/"},
                 "provider": {"name": "SeaDOTs", "url": "https://www.sintef.no/projectweb/seadots/"},
                 "contact": {"name": "SeaDOTs", "email": "info@example.org", "url": "https://www.sintef.no/projectweb/seadots/", "role": "pointOfContact"}},
              "resources": resources}
    (OUT / "pygeoapi-config.yml").write_text(__import__("yaml").safe_dump(config, sort_keys=False, allow_unicode=True), encoding="utf-8")
    (OUT / "run.sh").write_text('#!/bin/sh\nset -eu\nHERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)\nEXERCISE=$(CDPATH= cd -- "$HERE/.." && pwd)\nPYGEOAPI="$EXERCISE/.venv/bin/pygeoapi"\nif [ ! -x "$PYGEOAPI" ]; then\n  echo "Missing exercise environment. Run $EXERCISE/setup_pygeoapi.sh first." >&2\n  exit 1\nfi\ncd "$HERE"\nexport PYGEOAPI_CONFIG="$HERE/pygeoapi-config.yml"\nexport PYGEOAPI_OPENAPI="$HERE/openapi.yml"\n"$PYGEOAPI" openapi generate "$PYGEOAPI_CONFIG" --output-file "$PYGEOAPI_OPENAPI"\nexec "$PYGEOAPI" serve\n', encoding="utf-8")
    print(f"Built {len(raw_national)} national, {len(raw_emodnet)} EMODnet and {len(canonical)} harmonized features in {OUT}")


if __name__ == "__main__":
    main()
