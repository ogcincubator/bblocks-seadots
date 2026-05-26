#!/usr/bin/env python3
"""
Transform an OBIS checklist or occurrence response into the
`benthic-biomass-density-mareano` example shape.

OBIS checklist and occurrence rows provide occurrence records, not biomass or
sampled area. This transformer therefore emits an occurrence-weighted proxy for
`density_kg_m2` so the result can be carried by the target bblock, and it
records the limitation in provenance. When occurrence rows are provided, the
output also carries per-observation output rows.

OGC Building Blocks Python transform compatibility:
* when `input_data` is provided, assigns `output_data`;
* when run standalone, reads JSON from stdin and writes JSON to stdout.
"""
from __future__ import annotations

import datetime as dt
import json
import sys
from typing import Any


SOURCE_ENDPOINT = (
    "https://api.obis.org/v3/checklist?size=10&skip=20&datasetid="
    "d556b9d4-7625-4aa2-894d-441eabae47f7,"
    "152259dc-9c20-4c1a-9644-8e4b509d4f73,"
    "14fa3c3e-259c-4af9-9314-eee1dc3a119b"
)
OCCURRENCE_ENDPOINT = (
    "https://api.obis.org/v3/occurrence?size=10&skip=20&datasetid="
    "d556b9d4-7625-4aa2-894d-441eabae47f7,"
    "152259dc-9c20-4c1a-9644-8e4b509d4f73,"
    "14fa3c3e-259c-4af9-9314-eee1dc3a119b"
)
SOURCE_BLOCK = "bblocks://ogc.hosted.seadots.obis-mareano-checklist"
TARGET_BLOCK = "bblocks://ogc.hosted.seadots.benthic-biomass-density-mareano"
CHECKLIST_TARGET_ID = "https://example.org/norwegian-ses/benthic-biomass-density-mareano/obis-checklist-proxy"
OCCURRENCE_TARGET_ID = "https://example.org/norwegian-ses/benthic-biomass-density-mareano/obis-occurrence-proxy"
OBSERVED_PROPERTY = "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano"

MAREANO_FOOTPRINT = {
    "type": "Polygon",
    "coordinates": [[
        [-5.0, 56.0],
        [33.0, 56.0],
        [33.0, 82.0],
        [-5.0, 82.0],
        [-5.0, 56.0],
    ]],
}


def _as_int(value: Any, default: int = 0) -> int:
    if isinstance(value, bool):
        return default
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str):
        try:
            return int(float(value))
        except ValueError:
            return default
    return default


def _as_float(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return None
    return None


def _taxon_name(row: dict[str, Any]) -> str | None:
    value = row.get("acceptedNameUsage") or row.get("scientificName")
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _aphia_id(row: dict[str, Any]) -> int | None:
    value = row.get("aphiaID") or row.get("acceptedNameUsageID") or row.get("taxonID")
    parsed = _as_int(value, -1)
    return parsed if parsed >= 0 else None


def _is_occurrence_row(row: dict[str, Any]) -> bool:
    return any(key in row for key in ("occurrenceID", "basisOfRecord", "decimalLatitude", "decimalLongitude", "eventDate"))


def _occurrence_output(row: dict[str, Any], density_proxy: float) -> dict[str, Any]:
    item = {
        "id": row.get("id") or row.get("occurrenceID"),
        "occurrenceID": row.get("occurrenceID"),
        "scientificName": _taxon_name(row),
        "density_kg_m2": round(density_proxy, 10),
        "eventDate": row.get("eventDate"),
        "datasetName": row.get("datasetName"),
        "samplingProtocol": row.get("samplingProtocol"),
    }
    aphia_id = _aphia_id(row)
    if aphia_id is not None:
        item["aphiaID"] = aphia_id
    lon = _as_float(row.get("decimalLongitude"))
    lat = _as_float(row.get("decimalLatitude"))
    depth = _as_float(row.get("depth") or row.get("minimumDepthInMeters"))
    if lon is not None:
        item["decimalLongitude"] = lon
    if lat is not None:
        item["decimalLatitude"] = lat
    if depth is not None:
        item["depth_m"] = depth
    return {k: v for k, v in item.items() if v is not None}


def transform(raw_json: str) -> str:
    source = json.loads(raw_json)
    rows = source.get("results")
    if not isinstance(rows, list):
        raise ValueError("Expected OBIS checklist JSON with a results array")

    usable_rows = [row for row in rows if isinstance(row, dict) and _taxon_name(row)]
    occurrence_mode = any(_is_occurrence_row(row) for row in usable_rows)
    if occurrence_mode:
        record_total = len(usable_rows)
    else:
        record_total = sum(_as_int(row.get("records")) for row in usable_rows)
    if record_total <= 0:
        record_total = 1

    grouped: dict[str, dict[str, Any]] = {}
    observation_outputs = []
    for row in usable_rows:
        records = 1 if occurrence_mode else _as_int(row.get("records"))
        density_proxy = records / record_total
        name = _taxon_name(row)
        if name not in grouped:
            grouped[name] = {"records": 0, "row": row}
        grouped[name]["records"] += records
        if occurrence_mode:
            observation_outputs.append(_occurrence_output(row, density_proxy))

    per_taxon = []
    for name, grouped_row in grouped.items():
        row = grouped_row["row"]
        records = grouped_row["records"]
        density_proxy = records / record_total
        item = {
            "scientificName": name,
            "density_kg_m2": round(density_proxy, 10),
            "habitat": "marine benthic occurrence taxon" if occurrence_mode else "marine benthic checklist taxon",
            "depthBand_m": "occurrence depth varies" if occurrence_mode else "unknown",
            "nSamples": records,
            "obisRecords": records,
            "taxonRank": row.get("taxonRank"),
        }
        aphia_id = _aphia_id(row)
        if aphia_id is not None:
            item["aphiaID"] = aphia_id
        per_taxon.append(item)

    per_taxon.sort(key=lambda item: (-item["density_kg_m2"], item["scientificName"]))
    aggregate_density = round(sum(item["density_kg_m2"] for item in per_taxon), 10)
    today = dt.date.today().isoformat()

    result = {
        "id": OCCURRENCE_TARGET_ID if occurrence_mode else CHECKLIST_TARGET_ID,
        "type": "Feature",
        "geometry": MAREANO_FOOTPRINT,
        "properties": {
            "type": "Dataset",
            "title": "MAREANO benthic biomass density proxy from OBIS occurrence data" if occurrence_mode else "MAREANO benthic biomass density proxy from OBIS checklist",
            "description": (
                "Occurrence-weighted proxy derived from OBIS records for selected "
                "MAREANO datasets. OBIS records do not provide biomass, sampled "
                "area or station geometry; this output is a schema-compatible proxy, not "
                "a physical biomass-density measurement."
            ),
            "created": today,
            "updated": today,
            "language": {"code": "en"},
            "license": "https://creativecommons.org/licenses/by/4.0/",
            "themes": [{
                "concepts": [{"id": "benthic-biomass", "label": "Benthic biomass density"}],
                "scheme": "https://id3.seadots.eu/themes",
            }],
            "keywords": ["OBIS", "MAREANO", "occurrence", "benthic biomass", "proxy"],
            "formats": [{"mediaType": "application/json"}],
            "conformsTo": [
                "http://www.w3.org/ns/sosa/Observation",
                "https://ogcincubator.github.io/geodcat-ogcapi-records/",
            ],
            "benthicBiomassDensity": {
                "name": "OBIS occurrence proxy for MAREANO benthic biomass density",
                "description": "Per-taxon normalized OBIS occurrence records carried as a density proxy.",
                "role": "primary baseline proxy",
                "source": OCCURRENCE_ENDPOINT if occurrence_mode else SOURCE_ENDPOINT,
                "format": "application/json",
                "vocabularyTerm": OBSERVED_PROPERTY,
                "observedProperty": OBSERVED_PROPERTY,
                "phenomenonTime": "unknown",
                "data": {
                    "units": "dimensionless occurrence share encoded in kg m-2 field",
                    "samplePeriod": "unknown",
                    "samplingProgramme": "OBIS / MAREANO",
                    "perTaxon": per_taxon,
                    "aggregateDensity_kg_m2": aggregate_density,
                    "observationOutputs": observation_outputs,
                    "provenance": {
                        "values": "mixed",
                        "retrievalApiCall": OCCURRENCE_ENDPOINT if occurrence_mode else SOURCE_ENDPOINT,
                        "verifiedOn": today,
                        "primarySource": {
                            "name": "OBIS checklist API",
                            "url": OCCURRENCE_ENDPOINT if occurrence_mode else SOURCE_ENDPOINT,
                        },
                        "nearestAuthoritativeSource": {
                            "url": "https://obis.org/",
                            "note": "OBIS occurrence/checklist endpoints for selected MAREANO dataset identifiers.",
                        },
                        "verificationGap": (
                            "The source OBIS response contains occurrence records or occurrence record counts. "
                            "It does not contain biomass, sampled area, station effort "
                            "or physical density measurements. `density_kg_m2` is therefore a normalized "
                            "occurrence-count proxy for testing target bblock interoperability."
                        ),
                        "note": (
                            f"Transformed {len(usable_rows)} OBIS {'occurrence' if occurrence_mode else 'checklist'} rows from a response with "
                            f"total={source.get('total')} into a MAREANO biomass-density proxy example. "
                            f"Proxy density is {'occurrence count' if occurrence_mode else 'records'} / "
                            f"{'number of occurrence rows in this page' if occurrence_mode else 'sum(records in this page)'}; "
                            f"aggregate={aggregate_density}."
                        ),
                    },
                },
            },
        },
        "links": [
            {"rel": "describedby", "href": TARGET_BLOCK, "type": "application/schema+json", "title": "MAREANO Benthic Biomass Density Observation bblock"},
            {"rel": "derivedFrom", "href": SOURCE_BLOCK, "type": "application/schema+json", "title": "OBIS MAREANO Checklist bblock"},
            {"rel": "cite-as", "href": "https://obis.org/", "title": "OBIS"},
            {"rel": "cite-as", "href": "https://mareano.no/", "title": "MAREANO programme"},
        ],
    }
    return json.dumps(result, indent=2, ensure_ascii=False)


def main() -> int:
    sys.stdout.write(transform(sys.stdin.read()))
    sys.stdout.write("\n")
    return 0


if "input_data" in globals():
    output_data = transform(input_data)
elif __name__ == "__main__":
    raise SystemExit(main())
