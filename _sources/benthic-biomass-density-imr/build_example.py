#!/usr/bin/env python3
"""
Build the `imr_ices_iva_fallback.json` example from live MAREANO data.

Pipeline
--------
1. Fetch the global list of catch species from MAREANO Marbunn
     GET https://marbunn-ekstern.hi.no/apps/marbunn/v1/catchspecies
2. For every species, fetch its catch-sample GeoJSON
     GET https://marbunn-ekstern.hi.no/apps/marbunn/v1/getmapforcatch?species={name}&cruise=
3. Filter sample points to an AOI bbox (default: -5,56 → 33,82 — the same
   polygon the placeholder file used).
4. Aggregate per species: total catch weight (kg), in-AOI sample count,
   contributing cruises, contributing gear types.
5. Emit a GeoJSON-Feature wrapping the AOI polygon, the aggregation, and
   honest provenance/caveats.

Run
---
    python build_example.py
        # uses defaults — writes ./examples/imr_ices_iva_fallback.json
        # cache lives next to the script as _marbunn_cache.json
    python build_example.py --aoi -5 56 33 82 --workers 16
    python build_example.py --refresh    # ignore the cache, re-fetch all
    python build_example.py --top 50     # keep only the 50 heaviest species

Data licence: CC BY 4.0 / NLOD  © Institute of Marine Research / MAREANO.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API     = "https://marbunn-ekstern.hi.no/apps/marbunn/v1"
SP_LIST = f"{API}/catchspecies"
SP_DATA = f"{API}/getmapforcatch?species={{}}&cruise="

DEFAULT_AOI = (-5.0, 56.0, 33.0, 82.0)   # min_lon, min_lat, max_lon, max_lat
SCRIPT_DIR  = Path(__file__).resolve().parent
DEFAULT_OUT = SCRIPT_DIR / "examples" / "imr_ices_iva_fallback.json"
DEFAULT_CACHE = SCRIPT_DIR / "_marbunn_cache.json"


def _http_json(url: str, timeout: int = 30) -> dict | list | None:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return json.load(r)
    except (urllib.error.URLError, urllib.error.HTTPError,
            json.JSONDecodeError, TimeoutError):
        return None


def fetch_species_list() -> list[str]:
    sp = _http_json(SP_LIST)
    if not isinstance(sp, list):
        raise RuntimeError(f"Marbunn species-list endpoint returned no JSON list: {SP_LIST}")
    return sorted(set(sp))


def aggregate_species(name: str, fc: dict | None, aoi: tuple[float, float, float, float]) -> dict:
    """Reduce a Marbunn FeatureCollection into a per-species summary, filtered to AOI."""
    out = {
        "species":          name,
        "n_records":        0,
        "n_records_in_aoi": 0,
        "n_with_weight":    0,
        "total_weight_kg":  0.0,
        "n_with_number":    0,
        "total_number":     0,
        "cruises":          [],
        "equipment":        [],
    }
    if not fc or fc.get("type") != "FeatureCollection":
        return out
    feats = fc.get("features", [])
    out["n_records"] = len(feats)
    min_lon, min_lat, max_lon, max_lat = aoi
    cruises, equip = set(), set()
    for f in feats:
        g = f.get("geometry") or {}
        if g.get("type") != "Point":
            continue
        c = g.get("coordinates") or []
        if len(c) < 2:
            continue
        lon, lat = c[0], c[1]
        if not (min_lon <= lon <= max_lon and min_lat <= lat <= max_lat):
            continue
        p = f.get("properties") or {}
        out["n_records_in_aoi"] += 1
        w = p.get("Weight")
        if isinstance(w, (int, float)):
            out["n_with_weight"] += 1
            out["total_weight_kg"] += float(w)
        n = p.get("Number")
        if isinstance(n, (int, float)):
            out["n_with_number"] += 1
            out["total_number"] += int(n)
        if p.get("Cruise"):
            cruises.add(str(p["Cruise"]))
        if p.get("Equipment"):
            equip.add(str(p["Equipment"]))
    out["cruises"]   = sorted(cruises)
    out["equipment"] = sorted(equip)
    return out


def fetch_all(species: list[str], aoi, cache: dict, workers: int) -> dict:
    """Populate `cache` (species → aggregate dict) using concurrent HTTP."""
    todo = [s for s in species if s not in cache]
    if not todo:
        return cache
    t0, done = time.time(), 0
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(_http_json, SP_DATA.format(urllib.parse.quote(s))): s for s in todo}
        for fut in cf.as_completed(futs):
            sp = futs[fut]
            try:
                fc = fut.result()
            except Exception:
                fc = None
            cache[sp] = aggregate_species(sp, fc, aoi)
            done += 1
            if done % 100 == 0 or done == len(todo):
                _save_cache_atomic(cache)
                el = time.time() - t0
                rate = done / el if el else 0
                eta  = (len(todo) - done) / rate if rate else 0
                print(f"  {done}/{len(todo)}  rate={rate:.1f}/s  ETA={eta:.0f}s", file=sys.stderr)
    return cache


def _save_cache_atomic(cache: dict) -> None:
    tmp = DEFAULT_CACHE.with_suffix(".tmp")
    tmp.write_text(json.dumps(cache))
    tmp.replace(DEFAULT_CACHE)


def build_document(cache: dict, aoi, args) -> dict:
    """Shape the cache into the final example-file structure."""
    aoi_rows = [v for v in cache.values() if v["n_records_in_aoi"] > 0]
    aoi_rows.sort(key=lambda r: (-r["total_weight_kg"], -r["n_records_in_aoi"], r["species"]))
    if args.top is not None:
        aoi_rows = aoi_rows[: args.top]

    per_taxon = [{
        "scientificName":     r["species"],
        "totalWeight_kg":     round(r["total_weight_kg"], 3),
        "samplesWithWeight":  r["n_with_weight"],
        "samplesInAOI":       r["n_records_in_aoi"],
        "totalIndividuals":   r["total_number"] if r["n_with_number"] else None,
        "cruises":            r["cruises"],
        "equipment":          r["equipment"],
    } for r in aoi_rows]

    species_with_weights = sum(1 for r in cache.values() if r["n_with_weight"] > 0 and r["n_records_in_aoi"] > 0)
    species_in_aoi       = sum(1 for r in cache.values() if r["n_records_in_aoi"] > 0)
    total_records_in_aoi = sum(r["n_records_in_aoi"] for r in cache.values())
    total_weight         = round(sum(r["total_weight_kg"] for r in cache.values()), 3)
    cruise_span          = sorted({c for r in cache.values() for c in r["cruises"]})

    today = dt.date.today().isoformat()
    return {
        "id": "https://example.org/norwegian-ses/benthic-biomass-density-imr/mareano-aoi-aggregate",
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [[
                [aoi[0], aoi[1]], [aoi[2], aoi[1]],
                [aoi[2], aoi[3]], [aoi[0], aoi[3]],
                [aoi[0], aoi[1]],
            ]],
        },
        "properties": {
            "type":        "Dataset",
            "title":       "MAREANO benthic catch-sample biomass, aggregated per species over a North Sea / Norwegian Sea / Barents Sea AOI",
            "description": ("Per-species sum of weighed catch-sample mass from the MAREANO Marbunn database, "
                            "filtered to the AOI polygon. All numbers are real Marbunn-API responses fetched at "
                            "file generation time."),
            "created":     today,
            "updated":     today,
            "language":    {"code": "en"},
            "license":     "https://creativecommons.org/licenses/by/4.0/",
            "attribution": "Institute of Marine Research (IMR) / MAREANO programme. CC BY 4.0 / NLOD.",
            "themes":      [{"concepts": [{"id": "benthic-biomass", "label": "Benthic biomass density"}],
                             "scheme":   "https://id3.seadots.eu/themes"}],
            "keywords":    ["MAREANO", "Marbunn", "IMR", "benthic biomass", "catch samples", "Norway"],
            "formats":     [{"mediaType": "application/json"}],
            "conformsTo": [
                "http://www.w3.org/ns/sosa/Observation",
                "https://ogcincubator.github.io/geodcat-ogcapi-records/",
            ],
            "benthicBiomassDensity": {
                "name":             "MAREANO catch-sample biomass aggregation",
                "description":      ("Catch weight summed across every weighed Marbunn sample whose station "
                                     "point falls inside the AOI polygon, grouped by species."),
                "role":             "real measured baseline (catch-weight; NOT area-normalised density)",
                "source":           SP_DATA.replace("{}", "{scientificName}"),
                "format":           "application/geo+json",
                "vocabularyTerm":   "https://w3id.org/indicators/marine/obs/benthic-biomass-density-imr-baseline",
                "observedProperty": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-imr-baseline",
                "phenomenonTime":   f"{cruise_span[0]}/{cruise_span[-1]}" if cruise_span else None,
                "data": {
                    "units":  "kg (per-sample catch weight, summed across samples; NOT kg m-2)",
                    "method": ("For every species in MAREANO's catch-species list, fetched /getmapforcatch as "
                               "GeoJSON, filtered to the AOI bbox by station coordinate, summed the per-sample "
                               "Weight property (kg) and counted samples."),
                    "samplingGear":             sorted({e for r in cache.values() for e in r["equipment"]}),
                    "cruisesContributing":      cruise_span,
                    "speciesQueried":           len(cache),
                    "speciesWithRecordsInAOI":  species_in_aoi,
                    "speciesWithWeighedSamples": species_with_weights,
                    "totalRecordsInAOI":        total_records_in_aoi,
                    "totalWeight_kg":           total_weight,
                    "perTaxon":                 per_taxon,
                    "provenance": {
                        "values": "real",
                        "source": {
                            "name":                "MAREANO Marbunn (IMR catch-samples viewer)",
                            "api":                 API + "/",
                            "speciesListEndpoint": SP_LIST,
                            "perSpeciesEndpoint":  SP_DATA.replace("{}", "{name}"),
                            "portal":              "https://mareano.no/",
                            "license":             "CC BY 4.0 / NLOD",
                        },
                        "fetched_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                        "generator":   f"{Path(__file__).name}",
                        "caveats": [
                            "Marbunn returns catch-sample weights in kilograms; the values here are SUMS of those per-sample weights — not areal densities. Converting to kg m-2 would require the swept area of every sample, which Marbunn does not expose.",
                            "Many catch records have Weight=null (sample identified but not weighed); they are excluded from totalWeight_kg but counted in samplesInAOI so coverage gaps stay visible.",
                            "Cruise IDs are MAREANO/IMR internal cruise codes; the same physical cruise may use multiple gear types.",
                            "The AOI polygon is a wide bbox; it overlaps but does not equal any single ICES Division.",
                        ],
                    },
                },
            },
        },
        "links": [
            {"rel": "describedby", "href": "bblocks://ogc.hosted.seadots.benthic-biomass-density-imr", "type": "application/schema+json", "title": "IMR Benthic Biomass Density Observation bblock"},
            {"rel": "profile",     "href": "bblocks://ogc.hosted.iliad.api.features.oim-obs",         "type": "application/schema+json", "title": "OIM Observations profile"},
            {"rel": "cite-as",     "href": "https://mareano.no/",                                     "title": "MAREANO programme"},
            {"rel": "cite-as",     "href": "https://www.hi.no/",                                      "title": "Institute of Marine Research"},
        ],
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--out", type=Path, default=DEFAULT_OUT,
                   help=f"output GeoJSON path (default: {DEFAULT_OUT})")
    p.add_argument("--aoi", nargs=4, type=float, default=list(DEFAULT_AOI),
                   metavar=("MIN_LON", "MIN_LAT", "MAX_LON", "MAX_LAT"),
                   help=f"AOI bbox (default: {DEFAULT_AOI})")
    p.add_argument("--workers", type=int, default=16, help="concurrent HTTP fetchers (default: 16)")
    p.add_argument("--top", type=int, default=None,
                   help="if set, keep only the N species with the heaviest summed biomass in perTaxon")
    p.add_argument("--refresh", action="store_true", help="ignore the species-aggregate cache and re-fetch all species")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    aoi = tuple(args.aoi)

    print(f"AOI: {aoi}", file=sys.stderr)
    print(f"OUT: {args.out}", file=sys.stderr)
    args.out.parent.mkdir(parents=True, exist_ok=True)

    print("→ fetching catch-species list", file=sys.stderr)
    species = fetch_species_list()
    print(f"  {len(species)} species advertised by Marbunn", file=sys.stderr)

    cache: dict = {}
    if DEFAULT_CACHE.exists() and not args.refresh:
        try:
            cache = json.loads(DEFAULT_CACHE.read_text())
            print(f"  cache hit: {len(cache)} species", file=sys.stderr)
        except json.JSONDecodeError:
            cache = {}

    if args.refresh:
        cache = {}

    print("→ fetching per-species GeoJSON & aggregating", file=sys.stderr)
    cache = fetch_all(species, aoi, cache, args.workers)
    _save_cache_atomic(cache)

    print("→ building example document", file=sys.stderr)
    doc = build_document(cache, aoi, args)
    args.out.write_text(json.dumps(doc, indent=2, ensure_ascii=False))
    size_kb = args.out.stat().st_size / 1024
    n_taxa  = len(doc["properties"]["benthicBiomassDensity"]["data"]["perTaxon"])
    totals  = doc["properties"]["benthicBiomassDensity"]["data"]
    print(f"  wrote {args.out} ({size_kb:.1f} KB)", file=sys.stderr)
    print(f"  perTaxon rows               : {n_taxa}", file=sys.stderr)
    print(f"  species with records in AOI : {totals['speciesWithRecordsInAOI']}", file=sys.stderr)
    print(f"  species with weighed samples: {totals['speciesWithWeighedSamples']}", file=sys.stderr)
    print(f"  total weight aggregated     : {totals['totalWeight_kg']} kg", file=sys.stderr)
    print(f"  records in AOI              : {totals['totalRecordsInAOI']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
