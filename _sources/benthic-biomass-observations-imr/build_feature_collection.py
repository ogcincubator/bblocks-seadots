#!/usr/bin/env python3
"""
Build one GeoJSON FeatureCollection containing every IMR/MAREANO catch-sample
feature returned for all species and cruises, filtered to an AOI bbox.

This is the raw-feature companion to build_example.py:

* ../benthic-biomass-density-imr/build_example.py aggregates Marbunn samples
  per species into one bblock example Feature.
* build_feature_collection.py keeps the individual Marbunn sample Features,
  adds stable species/cruise helper properties, and writes them into one
  FeatureCollection.

Run
---
    python build_feature_collection.py
    python build_feature_collection.py --aoi -5 56 33 82 --workers 16
    python build_feature_collection.py --time-boundaries 2006-01-01 2026-12-31
    python build_feature_collection.py --species "Mytilus edulis" --species "Asterias rubens"
    python build_feature_collection.py --cruise 2022006006
    python build_feature_collection.py --refresh

Data licence: CC BY 4.0 / NLOD, Institute of Marine Research / MAREANO.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import hashlib
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Iterable

API = "https://marbunn-ekstern.hi.no/apps/marbunn/v1"
SP_LIST = f"{API}/catchspecies"
SP_DATA = f"{API}/getmapforcatch?species={{}}&cruise={{}}"

DEFAULT_AOI = (-5.0, 56.0, 33.0, 82.0)
SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_OUT = SCRIPT_DIR / "examples" / "imr_all_species_cruises_features.json"
DEFAULT_CACHE_DIR = SCRIPT_DIR / "_marbunn_feature_cache"


def _iso_date(value: str) -> str:
    try:
        return dt.date.fromisoformat(value).isoformat()
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"{value!r} is not an ISO date (YYYY-MM-DD)") from exc


def _http_json(url: str, timeout: int = 60) -> dict | list | None:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return json.load(r)
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, TimeoutError):
        return None


def _cache_path(cache_dir: Path, species: str, cruise: str) -> Path:
    key = f"{species}\0{cruise}".encode("utf-8")
    digest = hashlib.sha1(key).hexdigest()
    return cache_dir / f"{digest}.json"


def _read_cache(cache_dir: Path, species: str, cruise: str) -> dict | None:
    path = _cache_path(cache_dir, species, cruise)
    if not path.exists():
        return None
    try:
        cached = json.loads(path.read_text())
    except json.JSONDecodeError:
        return None
    payload = cached.get("payload")
    if isinstance(payload, dict):
        return payload
    return None


def _write_cache(cache_dir: Path, species: str, cruise: str, payload: dict | None) -> None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = _cache_path(cache_dir, species, cruise)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps({
        "species": species,
        "cruise": cruise,
        "fetched_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "payload": payload if isinstance(payload, dict) else {"type": "FeatureCollection", "features": []},
    }, ensure_ascii=False))
    tmp.replace(path)


def fetch_species_list() -> list[str]:
    species = _http_json(SP_LIST)
    if not isinstance(species, list):
        raise RuntimeError(f"Marbunn species-list endpoint returned no JSON list: {SP_LIST}")
    return sorted({str(s) for s in species if str(s).strip()})


def fetch_species_features(species: str, cruise: str, cache_dir: Path, refresh: bool) -> dict:
    if not refresh:
        cached = _read_cache(cache_dir, species, cruise)
        if cached is not None:
            return cached

    url = SP_DATA.format(urllib.parse.quote(species), urllib.parse.quote(cruise))
    payload = _http_json(url)
    if not isinstance(payload, dict) or payload.get("type") != "FeatureCollection":
        payload = {"type": "FeatureCollection", "features": []}
    _write_cache(cache_dir, species, cruise, payload)
    return payload


def _in_aoi(feature: dict, aoi: tuple[float, float, float, float]) -> bool:
    geometry = feature.get("geometry") or {}
    if geometry.get("type") != "Point":
        return False
    coordinates = geometry.get("coordinates") or []
    if len(coordinates) < 2:
        return False
    lon, lat = coordinates[0], coordinates[1]
    if not isinstance(lon, (int, float)) or not isinstance(lat, (int, float)):
        return False
    min_lon, min_lat, max_lon, max_lat = aoi
    return min_lon <= lon <= max_lon and min_lat <= lat <= max_lat


def _copy_feature(feature: dict, species: str, query_cruise: str) -> dict:
    out = {
        "type": "Feature",
        "geometry": feature.get("geometry"),
        "properties": dict(feature.get("properties") or {}),
    }
    props = out["properties"]
    props.setdefault("scientificName", species)
    props.setdefault("species", species)
    props.setdefault("sourceSpeciesQuery", species)
    if query_cruise:
        props.setdefault("sourceCruiseQuery", query_cruise)
    if props.get("Cruise") is not None:
        props.setdefault("cruise", str(props["Cruise"]))
    if props.get("Equipment") is not None:
        props.setdefault("equipment", str(props["Equipment"]))
    return out


def collect_features(
    species: Iterable[str],
    cruises: Iterable[str],
    aoi: tuple[float, float, float, float],
    cache_dir: Path,
    workers: int,
    refresh: bool,
) -> tuple[list[dict], dict]:
    jobs = [(sp, cruise) for sp in species for cruise in cruises]
    features: list[dict] = []
    stats = {
        "speciesQueried": len({sp for sp, _ in jobs}),
        "cruiseQueries": sorted({cruise for _, cruise in jobs}),
        "apiQueries": len(jobs),
        "sourceFeatures": 0,
        "featuresInAOI": 0,
        "speciesInAOI": set(),
        "cruisesInAOI": set(),
        "equipmentInAOI": set(),
    }

    t0 = time.time()
    done = 0
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        future_to_job = {
            ex.submit(fetch_species_features, sp, cruise, cache_dir, refresh): (sp, cruise)
            for sp, cruise in jobs
        }
        for future in cf.as_completed(future_to_job):
            sp, cruise = future_to_job[future]
            try:
                feature_collection = future.result()
            except Exception:
                feature_collection = {"type": "FeatureCollection", "features": []}

            source_features = feature_collection.get("features") or []
            stats["sourceFeatures"] += len(source_features)
            for feature in source_features:
                if not isinstance(feature, dict) or not _in_aoi(feature, aoi):
                    continue
                copied = _copy_feature(feature, sp, cruise)
                props = copied["properties"]
                features.append(copied)
                stats["featuresInAOI"] += 1
                stats["speciesInAOI"].add(str(props.get("scientificName") or sp))
                if props.get("Cruise") is not None:
                    stats["cruisesInAOI"].add(str(props["Cruise"]))
                if props.get("Equipment") is not None:
                    stats["equipmentInAOI"].add(str(props["Equipment"]))

            done += 1
            if done % 100 == 0 or done == len(jobs):
                elapsed = time.time() - t0
                rate = done / elapsed if elapsed else 0
                eta = (len(jobs) - done) / rate if rate else 0
                print(f"  {done}/{len(jobs)} queries  rate={rate:.1f}/s  ETA={eta:.0f}s", file=sys.stderr)

    features.sort(key=lambda f: (
        str((f.get("properties") or {}).get("scientificName") or ""),
        str((f.get("properties") or {}).get("Cruise") or ""),
        json.dumps(f.get("geometry") or {}, sort_keys=True),
    ))
    stats["speciesInAOI"] = sorted(stats["speciesInAOI"])
    stats["cruisesInAOI"] = sorted(stats["cruisesInAOI"])
    stats["equipmentInAOI"] = sorted(stats["equipmentInAOI"])
    return features, stats


def build_collection(features: list[dict], stats: dict, aoi, args: argparse.Namespace) -> dict:
    time_boundaries = list(args.time_boundaries) if args.time_boundaries else None
    return {
        "type": "FeatureCollection",
        "id": "https://example.org/norwegian-ses/benthic-biomass-observations-imr/all-species-cruises-features",
        "bbox": list(aoi),
        "properties": {
            "title": "IMR/MAREANO benthic catch-sample features, all species and cruises",
            "description": (
                "Merged GeoJSON FeatureCollection of Marbunn catch-sample point features "
                "for all requested species and cruise queries, filtered to the AOI bbox."
            ),
            "created": dt.date.today().isoformat(),
            "source": {
                "name": "MAREANO Marbunn",
                "api": API + "/",
                "speciesListEndpoint": SP_LIST,
                "perSpeciesEndpoint": SP_DATA.replace("{}", "{value}", 1).replace("{}", "{cruise}", 1),
                "license": "CC BY 4.0 / NLOD",
            },
            "aoi": {
                "bbox": list(aoi),
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[
                        [aoi[0], aoi[1]],
                        [aoi[2], aoi[1]],
                        [aoi[2], aoi[3]],
                        [aoi[0], aoi[3]],
                        [aoi[0], aoi[1]],
                    ]],
                },
            },
            "phenomenonTime": {
                "start": time_boundaries[0],
                "end": time_boundaries[1],
            } if time_boundaries else None,
            "summary": stats,
            "provenance": {
                "values": "retrieved",
                "generator": Path(__file__).name,
                "fetched_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "cacheDirectory": str(args.cache_dir),
                "timeBoundaryNote": (
                    "The current script records --time-boundaries as collection-level phenomenonTime; "
                    "it does not filter by date because the Marbunn catch-sample payload used here "
                    "exposes cruise identifiers, not normalized per-feature dates."
                ) if time_boundaries else "No explicit --time-boundaries supplied.",
            },
        },
        "links": [
            {
                "rel": "describedby",
                "href": "bblocks://ogc.hosted.seadots.benthic-biomass-observations-imr",
                "type": "application/schema+json",
                "title": "IMR Benthic Biomass Observations bblock",
            },
            {
                "rel": "derived",
                "href": "bblocks://ogc.hosted.seadots.benthic-biomass-density-imr",
                "type": "application/schema+json",
                "title": "Aggregate IMR benthic biomass observation bblock",
            },
        ],
        "features": features,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help=f"output path (default: {DEFAULT_OUT})")
    parser.add_argument("--aoi", nargs=4, type=float, default=list(DEFAULT_AOI),
                        metavar=("MIN_LON", "MIN_LAT", "MAX_LON", "MAX_LAT"),
                        help=f"AOI bbox (default: {DEFAULT_AOI})")
    parser.add_argument("--workers", type=int, default=16, help="concurrent HTTP fetchers (default: 16)")
    parser.add_argument("--species", action="append",
                        help="limit to one species; repeat for several. Defaults to all species.")
    parser.add_argument("--cruise", action="append", default=[],
                        help="limit to one cruise query; repeat for several. Defaults to empty cruise query, meaning all cruises.")
    parser.add_argument("--time-boundaries", nargs=2, type=_iso_date, metavar=("START_DATE", "END_DATE"),
                        help="collection-level phenomenon-time bounds as ISO dates (YYYY-MM-DD YYYY-MM-DD)")
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE_DIR,
                        help=f"raw per-species FeatureCollection cache directory (default: {DEFAULT_CACHE_DIR})")
    parser.add_argument("--refresh", action="store_true", help="ignore cached per-species FeatureCollections")
    args = parser.parse_args(argv)
    if args.time_boundaries and args.time_boundaries[0] > args.time_boundaries[1]:
        parser.error("--time-boundaries START_DATE must be earlier than or equal to END_DATE")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    aoi = tuple(args.aoi)

    if args.species:
        species = sorted({s.strip() for s in args.species if s.strip()})
    else:
        print("-> fetching catch-species list", file=sys.stderr)
        species = fetch_species_list()

    cruises = sorted({str(c).strip() for c in args.cruise if str(c).strip()}) or [""]

    print(f"AOI: {aoi}", file=sys.stderr)
    if args.time_boundaries:
        print(f"TIME: {args.time_boundaries[0]} -> {args.time_boundaries[1]}", file=sys.stderr)
    print(f"SPECIES: {len(species)}", file=sys.stderr)
    print(f"CRUISE QUERIES: {', '.join(cruises) if cruises != [''] else '(all cruises)'}", file=sys.stderr)
    print(f"OUT: {args.out}", file=sys.stderr)

    print("-> fetching per-species GeoJSON and collecting features", file=sys.stderr)
    features, stats = collect_features(species, cruises, aoi, args.cache_dir, args.workers, args.refresh)

    print("-> writing merged FeatureCollection", file=sys.stderr)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    collection = build_collection(features, stats, aoi, args)
    args.out.write_text(json.dumps(collection, indent=2, ensure_ascii=False))

    size_kb = args.out.stat().st_size / 1024
    print(f"  wrote {args.out} ({size_kb:.1f} KB)", file=sys.stderr)
    print(f"  source features seen : {stats['sourceFeatures']}", file=sys.stderr)
    print(f"  features in AOI      : {stats['featuresInAOI']}", file=sys.stderr)
    print(f"  species in AOI       : {len(stats['speciesInAOI'])}", file=sys.stderr)
    print(f"  cruises in AOI       : {len(stats['cruisesInAOI'])}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
