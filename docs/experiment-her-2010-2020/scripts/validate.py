"""Validate the POSEIDON 11-yr hindcast against ICES SAG SSB.

Reads:
  output/pilot/result.yaml          POSEIDON run output (FishState.Species 0 Biomass yearly)
  data/sag_her27_2532.csv           ICES SAG SSB tonnes for her.27.25-2932 2010-2020
  data/sst_anom_2010_2020.nc        NOAA OISST annual SST anomaly over pilot bbox
Writes:
  output/manifest.json              poseidon-output target schema manifest
                                    (timeSeries, validationLinks, runMetadata)
"""
import csv
import datetime as dt
import json
import math
import os

import numpy as np
import xarray as xr
import yaml

ROOT = "/tmp/poseidon-run/experiments/her-2010-2020"
RUNID = "her-2010-2020-pilot-001"

with open(f"{ROOT}/output/pilot/result.yaml") as f:
    r = yaml.safe_load(f)

# Modelled species 0 yearly biomass (kg in POSEIDON internals -> convert to t)
bio_keys = [k for k in (r.get("FishState") or {}).keys() if "Biomass" in k and "Species 0" in k]
print("FishState biomass keys:", bio_keys)
bio = r["FishState"][bio_keys[0]]
# POSEIDON yearly aggregates: list of stringified floats, one entry per simulated year (year 0 first)
model_t = {}
for year_idx, v in enumerate(bio):
    # POSEIDON reports biomass in kg by default; convert to tonnes
    model_t[2010 + year_idx] = float(v) / 1000.0

print("\nModelled Species 0 Biomass (tonnes) per simulated year:")
for y, t in sorted(model_t.items()):
    print(f"  {y}: {t:,.0f} t")

# Observed SAG SSB
obs = {}
with open(f"{ROOT}/data/sag_her27_2532.csv") as f:
    for row in csv.DictReader(f):
        try:
            y = int(row["year"])
            obs[y] = float(row["ssb_t"]) if row.get("ssb_t") else None
        except Exception:
            pass

# Validation metrics
pairs = [(y, model_t[y], obs.get(y)) for y in sorted(model_t) if obs.get(y) is not None]
print("\nYear | model_t | SAG SSB t")
for y, m, o in pairs:
    print(f"  {y}: {m:,.0f} | {o:,.0f}")

xs = np.array([p[1] for p in pairs], dtype=float)
ys = np.array([p[2] for p in pairs], dtype=float)
# Pearson
mu_x, mu_y = xs.mean(), ys.mean()
sx, sy = xs.std(ddof=0), ys.std(ddof=0)
pearson = float(((xs - mu_x) * (ys - mu_y)).mean() / (sx * sy)) if sx > 0 and sy > 0 else None
# NRMSE (normalised by mean SAG)
rmse = float(np.sqrt(((xs - ys) ** 2).mean()))
nrmse = rmse / mu_y if mu_y else None
# Spearman (rank correlation)
def rank(a):
    order = np.argsort(a)
    ranks = np.empty_like(order, dtype=float)
    ranks[order] = np.arange(len(a))
    return ranks
spear = None
if len(xs) > 2:
    rx, ry = rank(xs), rank(ys)
    mrx, mry = rx.mean(), ry.mean()
    spear = float(((rx - mrx) * (ry - mry)).mean() / (rx.std(ddof=0) * ry.std(ddof=0)))

print(f"\nValidation: Pearson r = {pearson:.3f}  Spearman = {spear:.3f}  NRMSE = {nrmse:.3f}")

# Emit poseidon-output manifest (truncated, with provenance)
manifest = {
    "runId": RUNID,
    "runConfigRef": "file://" + f"{ROOT}/inputs/pilot.yaml",
    "stacCollection": "poseidon-output-north-gotland",
    "runMetadata": {
        "startedAt": dt.datetime.utcnow().isoformat() + "Z",
        "finishedAt": dt.datetime.utcnow().isoformat() + "Z",
        "simulatedFromYear": 2010,
        "simulatedToYear": 2020,
        "timeStepUnit": "day",
        "seed": 42,
        "modelVersion": "POSEIDON main @ HEAD (built 2026-05-17, 13b31638)",
        "hostEnvironment": "claude-sandbox",
    },
    "timeSeries": [
        {
            "name": "Species 0 Biomass",
            "asset": f"file://{ROOT}/output/pilot/result.yaml",
            "mediaType": "application/x-yaml",
            "cadence": "yearly",
            "unit": "kg",
            "dimension": "global",
            "lineage": {
                "carryingCapacityFrom": "ICES SAG getStockDownloadData assessmentKey=17816, MSY-Btrigger × 1.0",
                "carryingCapacityValueTonnes": 1_034_000,
                "carryingCapacitySourceDOI": "https://doi.org/10.17895/ices.advice.21820506.v1",
                "steepnessRangeFrom": "calibrated bracket centred on FishBase k=0.39 prior with ±15% spread for SST coupling proxy",
                "fuelPriceEURperL": 0.65,
                "fuelPriceSource": "EU Weekly Oil Bulletin, Sweden diesel 2010-2020 mean (proxy scalar)",
                "marketPriceEURperKg": 0.27,
                "marketPriceSource": "EUMOFA Sweden herring industrial first-sale 2010-2020 mean (proxy scalar)",
            },
        },
    ],
    "validationLinks": [
        {
            "modelProductRef": "Species 0 Biomass",
            "empiricalRef": "ICES SAG her.27.25-2932 assessmentKey=17816 SSB tonnes",
            "empiricalSourceDOI": "https://doi.org/10.17895/ices.advice.21820506.v1",
            "metric": "Pearson_r",
            "value": pearson,
        },
        {
            "modelProductRef": "Species 0 Biomass",
            "empiricalRef": "ICES SAG her.27.25-2932 assessmentKey=17816 SSB tonnes",
            "empiricalSourceDOI": "https://doi.org/10.17895/ices.advice.21820506.v1",
            "metric": "Spearman_r",
            "value": spear,
        },
        {
            "modelProductRef": "Species 0 Biomass",
            "empiricalRef": "ICES SAG her.27.25-2932 assessmentKey=17816 SSB tonnes",
            "empiricalSourceDOI": "https://doi.org/10.17895/ices.advice.21820506.v1",
            "metric": "NRMSE",
            "value": nrmse,
        },
    ],
    "environmentalDriver": {
        "name": "SST annual anomaly (area mean) 2010-2020",
        "asset": f"file://{ROOT}/data/sst_anom_2010_2020.nc",
        "source": "NOAA OISST v2.1 highres monthly, PSL THREDDS OPeNDAP",
        "sourceURL": "https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.mon.mean.nc",
        "note": "Used as Copernicus BAL SST proxy because Copernicus ARCO Zarr chunks are auth-gated; OISST is open.",
    },
    "spatialFrame": {
        "bbox": [16.0, 56.5, 21.5, 60.0],
        "gridCells": "56 x 36",
        "bathySource": "Copernicus BAL static bathymetry BALTICSEA_MULTIYEAR_PHY_003_011 (EDITO STAC, native NetCDF)",
        "bathyURL": "https://s3.waw3-1.cloudferro.com/mdl-native-11/native/BALTICSEA_MULTIYEAR_PHY_003_011/cmems_mod_bal_phy_my_static_202303/BAL-MFC_003_011_mask_bathy.nc",
    },
}

OUT = f"{ROOT}/output/manifest.json"
with open(OUT, "w") as f:
    json.dump(manifest, f, indent=2)
print(f"\nWrote manifest: {OUT}")
