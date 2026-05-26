#!/usr/bin/env python3
"""
Transform IMR / MAREANO Marbunn raw observation points into the
`benthic-biomass-density-mareano` aggregate observation shape.

The source FeatureCollection contains catch-sample weights in kilograms. The
target block expects density in kg m-2, so this transformer first applies
explicit per-gear sampled-area assumptions to estimate point densities, then
extrapolates each taxon over the AOI with inverse distance weighting (IDW).

OGC Building Blocks Python transform compatibility:
* when executed by the postprocessor, `input_data` is provided and this file
  assigns `output_data`;
* when run standalone, it reads JSON from stdin and writes JSON to stdout.
"""
from __future__ import annotations

import datetime as dt
import json
import math
import sys
from collections import defaultdict
from typing import Any


OBS_BLOCK = "bblocks://ogc.hosted.seadots.benthic-biomass-observations-imr"
TARGET_BLOCK = "bblocks://ogc.hosted.seadots.benthic-biomass-density-mareano"
TARGET_ID = "https://example.org/norwegian-ses/benthic-biomass-density-mareano/from-imr-observations"

# Area assumptions are intentionally conservative and explicit. They are not a
# replacement for cruise-level swept-area metadata.
DEFAULT_GEAR_AREAS_M2 = {
    "Small VV grab": 0.1,
    "VVgrab020": 0.2,
    "Large VV grab": 0.25,
    "Boxcorer": 0.1,
    "Bioboks": 0.1,
    "Beamtrawl": 100.0,
    "RP-sledge": 50.0,
    "Videograb": 0.1,
}
FALLBACK_SAMPLE_AREA_M2 = 0.1
IDW_POWER = 2.0
IDW_GRID_SIZE = 25


def _as_number(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)) and math.isfinite(float(value)):
        return float(value)
    if isinstance(value, str):
        try:
            parsed = float(value)
        except ValueError:
            return None
        return parsed if math.isfinite(parsed) else None
    return None


def _as_string(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _feature_species(props: dict[str, Any]) -> str | None:
    return (
        _as_string(props.get("scientificName"))
        or _as_string(props.get("Scientific name"))
        or _as_string(props.get("species"))
        or _as_string(props.get("sourceSpeciesQuery"))
    )


def _feature_equipment(props: dict[str, Any]) -> str | None:
    return _as_string(props.get("equipment")) or _as_string(props.get("Equipment"))


def _feature_cruise(props: dict[str, Any]) -> str | None:
    return _as_string(props.get("cruise")) or _as_string(props.get("Cruise"))


def _sample_area_m2(equipment: str | None) -> tuple[float, bool]:
    if equipment in DEFAULT_GEAR_AREAS_M2:
        return DEFAULT_GEAR_AREAS_M2[equipment], False
    return FALLBACK_SAMPLE_AREA_M2, True


def _bbox_polygon(source: dict[str, Any]) -> dict[str, Any]:
    props = source.get("properties") or {}
    aoi = props.get("aoi") or {}
    geometry = aoi.get("geometry")
    if isinstance(geometry, dict) and geometry.get("type") == "Polygon":
        return geometry

    bbox = source.get("bbox") or aoi.get("bbox")
    if isinstance(bbox, list) and len(bbox) >= 4:
        min_lon, min_lat, max_lon, max_lat = [float(v) for v in bbox[:4]]
        return {
            "type": "Polygon",
            "coordinates": [[
                [min_lon, min_lat],
                [max_lon, min_lat],
                [max_lon, max_lat],
                [min_lon, max_lat],
                [min_lon, min_lat],
            ]],
        }

    return {"type": "Polygon", "coordinates": [[[-5.0, 56.0], [33.0, 56.0], [33.0, 82.0], [-5.0, 82.0], [-5.0, 56.0]]]}


def _geometry_bbox(geometry: dict[str, Any]) -> tuple[float, float, float, float]:
    rings = geometry.get("coordinates") or []
    points = []
    for ring in rings:
        if isinstance(ring, list):
            for point in ring:
                if isinstance(point, list) and len(point) >= 2:
                    lon = _as_number(point[0])
                    lat = _as_number(point[1])
                    if lon is not None and lat is not None:
                        points.append((lon, lat))
    if not points:
        return (-5.0, 56.0, 33.0, 82.0)
    lons = [p[0] for p in points]
    lats = [p[1] for p in points]
    return (min(lons), min(lats), max(lons), max(lats))


def _feature_xy(feature: dict[str, Any]) -> tuple[float, float] | None:
    geometry = feature.get("geometry") or {}
    if geometry.get("type") != "Point":
        return None
    coordinates = geometry.get("coordinates") or []
    if len(coordinates) < 2:
        return None
    lon = _as_number(coordinates[0])
    lat = _as_number(coordinates[1])
    if lon is None or lat is None:
        return None
    return lon, lat


def _grid_points(bounds: tuple[float, float, float, float], size: int) -> list[tuple[float, float]]:
    min_lon, min_lat, max_lon, max_lat = bounds
    if size < 1 or min_lon == max_lon or min_lat == max_lat:
        return [((min_lon + max_lon) / 2, (min_lat + max_lat) / 2)]
    lon_step = (max_lon - min_lon) / size
    lat_step = (max_lat - min_lat) / size
    return [
        (min_lon + (col + 0.5) * lon_step, min_lat + (row + 0.5) * lat_step)
        for row in range(size)
        for col in range(size)
    ]


def _idw_area_mean(
    observations: list[tuple[float, float, float]],
    grid_points: list[tuple[float, float]],
    power: float,
) -> float:
    if not observations:
        return 0.0
    if len(observations) == 1:
        return observations[0][2]

    estimates = []
    for gx, gy in grid_points:
        numerator = 0.0
        denominator = 0.0
        exact = None
        for ox, oy, value in observations:
            distance = math.hypot(gx - ox, gy - oy)
            if distance == 0:
                exact = value
                break
            weight = 1 / (distance ** power)
            numerator += weight * value
            denominator += weight
        estimates.append(exact if exact is not None else numerator / denominator)
    return sum(estimates) / len(estimates)


def _phenomenon_time(source: dict[str, Any], cruises: set[str]) -> str | dict[str, str] | None:
    props = source.get("properties") or {}
    phenomenon_time = props.get("phenomenonTime")
    if isinstance(phenomenon_time, dict) and phenomenon_time.get("start") and phenomenon_time.get("end"):
        return {"start": str(phenomenon_time["start"]), "end": str(phenomenon_time["end"])}
    if isinstance(phenomenon_time, str) and phenomenon_time:
        return phenomenon_time
    if cruises:
        ordered = sorted(cruises)
        return f"{ordered[0]}/{ordered[-1]}"
    return None


def transform(raw_json: str) -> str:
    source = json.loads(raw_json)
    if source.get("type") != "FeatureCollection":
        raise ValueError("Expected a GeoJSON FeatureCollection from benthic-biomass-observations-imr")

    grouped: dict[str, dict[str, Any]] = defaultdict(lambda: {
        "weight_kg": 0.0,
        "area_m2": 0.0,
        "n_samples": 0,
        "n_weighted": 0,
        "fallback_area_samples": 0,
        "equipment": set(),
        "cruises": set(),
        "depths": [],
        "observations": [],
    })
    all_cruises: set[str] = set()
    all_equipment: set[str] = set()
    ignored_features = 0

    for feature in source.get("features") or []:
        if not isinstance(feature, dict):
            ignored_features += 1
            continue
        props = feature.get("properties") or {}
        species = _feature_species(props)
        if not species:
            ignored_features += 1
            continue

        row = grouped[species]
        row["n_samples"] += 1

        equipment = _feature_equipment(props)
        if equipment:
            row["equipment"].add(equipment)
            all_equipment.add(equipment)

        cruise = _feature_cruise(props)
        if cruise:
            row["cruises"].add(cruise)
            all_cruises.add(cruise)

        depth = _as_number(props.get("Bottom depth"))
        if depth is not None:
            row["depths"].append(depth)

        weight = _as_number(props.get("Weight"))
        if weight is None:
            continue
        xy = _feature_xy(feature)
        area, used_fallback = _sample_area_m2(equipment)
        point_density = weight / area
        row["weight_kg"] += weight
        row["area_m2"] += area
        row["n_weighted"] += 1
        if xy is not None:
            row["observations"].append((xy[0], xy[1], point_density))
        if used_fallback:
            row["fallback_area_samples"] += 1

    per_taxon = []
    geometry = _bbox_polygon(source)
    grid_points = _grid_points(_geometry_bbox(geometry), IDW_GRID_SIZE)
    total_weighted_samples = 0
    total_fallback_area_samples = 0
    for species, row in grouped.items():
        density = _idw_area_mean(row["observations"], grid_points, IDW_POWER)
        observed_mean_density = row["weight_kg"] / row["area_m2"] if row["area_m2"] > 0 else 0.0
        total_weighted_samples += int(row["n_weighted"])
        total_fallback_area_samples += int(row["fallback_area_samples"])
        depths = row["depths"]
        per_taxon.append({
            "scientificName": species,
            "density_kg_m2": round(density, 8),
            "habitat": "unclassified",
            "depthBand_m": (
                f"{round(min(depths))}-{round(max(depths))}"
                if depths else "unknown"
            ),
            "nSamples": int(row["n_samples"]),
            "observedMeanDensity_kg_m2": round(observed_mean_density, 8),
        })

    per_taxon.sort(key=lambda item: (-item["density_kg_m2"], item["scientificName"]))
    aggregate_density = round(sum(item["density_kg_m2"] for item in per_taxon), 8)
    today = dt.date.today().isoformat()
    source_props = source.get("properties") or {}
    source_prov = source_props.get("provenance") or {}

    result = {
        "id": TARGET_ID,
        "type": "Feature",
        "geometry": geometry,
        "properties": {
            "type": "Dataset",
            "title": "MAREANO benthic biomass density derived from IMR/Marbunn observations",
                "description": (
                    "Per-taxon benthic biomass density estimate derived from raw IMR / "
                    "MAREANO Marbunn catch-sample observations by converting catch "
                    "weights to point densities and extrapolating over the AOI with IDW."
                ),
            "created": today,
            "updated": today,
            "language": {"code": "en"},
            "license": "https://creativecommons.org/licenses/by/4.0/",
            "themes": [{
                "concepts": [{"id": "benthic-biomass", "label": "Benthic biomass density"}],
                "scheme": "https://id3.seadots.eu/themes",
            }],
            "keywords": ["MAREANO", "Marbunn", "IMR", "benthic biomass", "density", "transform"],
            "formats": [{"mediaType": "application/json"}],
            "conformsTo": [
                "http://www.w3.org/ns/sosa/Observation",
                "https://ogcincubator.github.io/geodcat-ogcapi-records/",
            ],
            "benthicBiomassDensity": {
                "name": "MAREANO benthic biomass density from IMR observations",
                "description": "Aggregate per-taxon density estimate transformed from raw Marbunn observation points using IDW interpolation over the AOI.",
                "role": "primary baseline",
                "source": source.get("id") or "bblocks://ogc.hosted.seadots.benthic-biomass-observations-imr",
                "format": "application/json",
                "vocabularyTerm": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano",
                "observedProperty": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano",
                "phenomenonTime": _phenomenon_time(source, all_cruises),
                "data": {
                    "units": "kg m-2",
                    "samplePeriod": _phenomenon_time(source, all_cruises),
                    "samplingProgramme": "MAREANO / IMR Marbunn",
                        "perTaxon": per_taxon,
                        "aggregateDensity_kg_m2": aggregate_density,
                        "provenance": {
                        "values": "mixed",
                        "retrievalApiCall": (source_props.get("source") or {}).get("perSpeciesEndpoint"),
                        "verifiedOn": today,
                        "primarySource": source_props.get("source"),
                        "nearestAuthoritativeSource": {
                            "url": "https://mareano.no/",
                            "note": "Raw observations come from IMR / MAREANO Marbunn catch-sample point features.",
                        },
                        "verificationGap": (
                            "Source observations provide catch weight in kg. The target block requires kg m-2. "
                            "This transform first uses per-gear sampled-area assumptions rather than authoritative "
                            "cruise-level swept-area metadata, then extrapolates point densities with IDW. "
                            "Ordinary Kriging or Regression-Kriging would be preferable once variograms, "
                            "environmental covariates and geostatistical dependencies are available."
                        ),
                        "note": (
                            f"Transformed {len(source.get('features') or [])} source features into "
                            f"{len(per_taxon)} per-taxon rows. Ignored {ignored_features} malformed or "
                            f"unnamed features. IDW grid={IDW_GRID_SIZE}x{IDW_GRID_SIZE}, power={IDW_POWER}, "
                            f"weighted samples={total_weighted_samples}, samples using fallback area="
                            f"{total_fallback_area_samples}. Gear-area assumptions m2: "
                            f"{json.dumps(DEFAULT_GEAR_AREAS_M2, sort_keys=True)}; fallback="
                            f"{FALLBACK_SAMPLE_AREA_M2}. Source fetched_utc="
                            f"{source_prov.get('fetched_utc', 'unknown')}."
                        ),
                    },
                },
            },
        },
        "links": [
            {"rel": "describedby", "href": TARGET_BLOCK, "type": "application/schema+json", "title": "MAREANO Benthic Biomass Density Observation bblock"},
            {"rel": "derivedFrom", "href": OBS_BLOCK, "type": "application/schema+json", "title": "IMR Benthic Biomass Observations bblock"},
            {"rel": "cite-as", "href": "https://mareano.no/", "title": "MAREANO programme"},
            {"rel": "cite-as", "href": "https://www.hi.no/", "title": "Institute of Marine Research"},
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
