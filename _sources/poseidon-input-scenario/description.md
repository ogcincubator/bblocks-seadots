# POSEIDON Scenario YAML Input

POSEIDON scenarios are YAML configuration documents loaded by the Java implementation. A scenario composes the spatial map, biological initializer, fleet/fisher definitions, ports and markets, regulation or policy configuration, optional plugins, and output selections.

This schema captures that composition layer and delegates detailed input structures to the dedicated POSEIDON input blocks.

## Role within the input stack

Scenario is a **composition layer**, not a data layer. It bundles references to:

- [poseidon-input-map] (spatial frame)
- [poseidon-input-biology] (population dynamics)
- [poseidon-input-fleet] (fishing agents)
- [poseidon-input-port-market] (ports, prices, fuel)
- [poseidon-input-regulation-policy] (TACs, closures, gear rules)
- [poseidon-input-observation-output] (what is logged)

Beyond composition, the scenario bblock fixes a small number of **scenario-level axes** that cannot live in a single upstream bblock because they cross several:

- **Time axis** — hindcast (Copernicus reanalysis) vs forecast (Copernicus analysis-forecast or climate-projection downscaling).
- **Climate axis** — current-climate (single realisation) vs future-climate (CMIP6 SSP scenario).
- **Regulation axis** — status-quo (current EU + national rules) vs proposed (CFP reform / BSAP-target overlay).
- **Fleet axis** — current capacity vs EMFAF-supported capacity changes vs voluntary exit programmes.

The R/S/V classification is used here only for **scenario-axis sources** — the upstream data sources are already classified inside their own bblocks.

## Source availability for the pilot area

| Source | Role | Coverage of SD 27 / 29 | Provides | Feeds POSEIDON field(s) | Related bblock(s) | Format at origin | Licence |
|---|---|---|---|---|---|---|---|
| Copernicus BAL physics reanalysis (`BALTICSEA_MULTIYEAR_PHY_003_011`) | **R** for hindcast | Whole Baltic, 1993 → present | Hindcast SST/SSS/currents | Drives `biology.diffusion`, `biology.recruitment` env-coupling | [poseidon-input-biology], [poseidon-input-map] | NetCDF + ARCO Zarr | Copernicus Licence |
| Copernicus BAL physics forecast (`BALTICSEA_ANALYSISFORECAST_PHY_003_006`) | **S** alternative for prospective runs | Whole Baltic, near-real-time → ~10 days | Forecast SST/SSS/currents | Same as reanalysis but forward-looking | [poseidon-input-biology] | NetCDF + ARCO Zarr | Copernicus Licence |
| CMIP6 / Bio-ORACLE v3 climate projections | **R / S** for climate-projection forecasts | Global incl. Baltic, multi-decadal | Downscaled SST/Chl-a projections per SSP | Long-horizon forecast forcing | [poseidon-input-biology] | NetCDF + Zarr (via Bio-ORACLE) | CC-BY 4.0 |
| EU CFP reform proposals (EUR-Lex Cellar) | **S** for "proposed regulation" scenarios | EU-wide | Proposed rule changes | Triggers `regulations` and `shocks[]` overlay in [poseidon-input-regulation-policy] | [poseidon-input-regulation-policy] | EUR-Lex Cellar JSON-LD | EC Open |
| HELCOM BSAP 2021 targets | **S** for "GES-target" scenarios | Whole Baltic | Long-horizon environmental targets | Drives objective in [poseidon-input-optimization] policy search | [poseidon-input-regulation-policy], [poseidon-input-optimization] | PDF + Indicators API | CC-BY 4.0 |
| EMFAF (European Maritime, Fisheries & Aquaculture Fund) — Sweden plan | **S** for fleet-capacity scenarios | Sweden | Planned vessel-decommissioning / SSCF support | Adjusts [poseidon-input-fleet] `fishers[].count` in scenario overlay | [poseidon-input-fleet] | PDF / DG MARE portal | EC Open |
| ICES advice (forward-looking projections) | **S** for stock-projection scenarios | Baltic stocks | Short-term forecast of SSB / R / F | Validation / reference for forecast scenarios | [poseidon-input-biology] | PDF + SAG JSON | ICES Data Policy (open) |
| Held-out years of all V-role sources | **V** | Same as upstream | Out-of-sample series | Validation of scenario realism | [poseidon-input-observation-output] | mixed | mixed |

[poseidon-input-map]: ../poseidon-input-map/
[poseidon-input-biology]: ../poseidon-input-biology/
[poseidon-input-fleet]: ../poseidon-input-fleet/
[poseidon-input-port-market]: ../poseidon-input-port-market/
[poseidon-input-regulation-policy]: ../poseidon-input-regulation-policy/
[poseidon-input-observation-output]: ../poseidon-input-observation-output/
[poseidon-input-optimization]: ../poseidon-input-optimization/
[poseidon-input-run-control]: ../poseidon-input-run-control/
[poseidon-output]: ../poseidon-output/

## Two-stage transformation pipeline

### Stage A — Source → EDITO

| Source | EDITO artefact | Transformation |
|---|---|---|
| Copernicus reanalysis vs forecast Items | already EDITO-compliant (`BALTICSEA_MULTIYEAR_PHY_003_011`, `BALTICSEA_ANALYSISFORECAST_PHY_003_006`) | No copy; the scenario records which Item URI is the active forcing. |
| CMIP6 / Bio-ORACLE projections | `scenario/climate_<ssp>.zarr` | If using climate projection, regrid the chosen Bio-ORACLE / CMIP6 variable to the canonical map grid; write GeoZarr; one Item per SSP. |
| EU CFP proposals | re-uses `regulation/cfp_proposals.parquet` from [poseidon-input-regulation-policy] | No copy. |
| HELCOM BSAP indicators | re-uses `regulation/bsap_targets.parquet` | No copy. |
| EMFAF Sweden plan | `scenario/emfaf_se.parquet` | Curated table of planned capacity changes; columns `year, segment_id, vessels_added, vessels_decommissioned`. |
| ICES advice (forward) | re-uses `regulation/ices_advice.parquet` | No copy. |
| The scenario itself (composition) | `scenarios/<scenarioId>.json` (STAC Item) | Build a STAC Item whose `assets` are links to each upstream bblock Item; `properties.scenario:axes` records the chosen values along the four scenario axes (time, climate, regulation, fleet). |

### Stage B — EDITO → POSEIDON

| EDITO artefact | POSEIDON field(s) | Transformation |
|---|---|---|
| `scenarios/<scenarioId>.json` STAC Item | `scenarioType` + each top-level scenario field | The runner reads the Item, follows each asset link, and emits the corresponding POSEIDON YAML section by delegating to the relevant input bblock's Stage B. |
| Active forcing Item (reanalysis / forecast / climate) | `biology.species[].diffusion`, `biology.species[].recruitment` env-coupling | Same Stage B as in [poseidon-input-biology] — only the *source Item URI* differs across scenarios. |
| Regulation overlay (`cfp_proposals.parquet` or `bsap_targets.parquet`) | `regulations.shocks[]` | Each row → one `shocks[]` element with `applyAtYear`. |
| `emfaf_se.parquet` | `fleet` overlay (additive / subtractive over the baseline `fishers[]`) | Per `year`, modify `fishers[].count` of the matching segment. |

## Scenario axes — values used in the pilot

| Axis | Status-quo / current | Alternative |
|---|---|---|
| Time | Hindcast 2010–2023 driven by reanalysis | Forecast 2025–2055 driven by analysis-forecast (short) or CMIP6 SSP2-4.5 / SSP5-8.5 (long) |
| Climate | Current-climate (no SST trend beyond observed) | Future-climate (Bio-ORACLE SST + Chl-a under chosen SSP) |
| Regulation | Status-quo (Council TAC + MAP HCR + Tech Measures + HELCOM/Natura closures) | Proposed: + CFP reform `shocks[]`, **or** + HELCOM BSAP `shocks[]`, **or** + Sweden national MPA extension `shocks[]` |
| Fleet | Current CFR snapshot | EMFAF-supported decommissioning trajectory, **or** voluntary-exit programme |

Each scenario picks **one value per axis**; the cartesian product enumerates the runnable scenarios for sensitivity analysis.

## Required vs substitutable vs validation-only

### Required path

- A hindcast scenario requires the reanalysis forcing Item (R), all six upstream input bblocks resolved against their R-role sources, and `regulations` = status-quo (R).
- A short-horizon forecast scenario requires the analysis-forecast forcing Item (R) and may keep `regulations` = status-quo.
- A long-horizon forecast scenario requires a chosen CMIP6 SSP forcing (R) and at least one alternative `regulations` overlay (S, but mandatory for "what-if" runs).

### Substitutable (XOR per axis)

- **Time-axis forcing**: reanalysis **xor** analysis-forecast **xor** CMIP6 SSP.
- **Regulation overlay**: status-quo **xor** CFP-proposed **xor** BSAP-target **xor** national-MPA-extension. (Multiple overlays may be sequenced through `shocks[]`, but each shock is one source.)
- **Fleet overlay**: status-quo CFR snapshot **xor** EMFAF trajectory **xor** voluntary-exit programme.

### Validation-only

- ICES forward projections — sanity check that scenario SSB trajectories are bracketed by ICES short-term advice envelopes.
- Held-out years from upstream V-role series — out-of-sample comparison.

### Minimal viable scenario for the pilot

1. Map Item: north-of-Gotland 1 nm grid, EMODnet bathymetry + HELCOM + Natura 2000 closures.
2. Biology Item: FishBase + WGBFAS SAG for herring + sprat + cod.
3. Fleet Item: Swedish CFR + STECF AER + VMS-derived destination prior.
4. Port-market Item: Simrishamn + Karlskrona + Slite + Stockholm-Frihamnen + EUMOFA prices + Oil Bulletin fuel.
5. Regulation Item: 2023 Council Baltic TAC + Tech Measures + HELCOM MPA closures.
6. Observation-output Item: SSB / landings / cash-flow / effort heatmap.

The scenario STAC Item carries the four axis values: `(time=hindcast, climate=current, regulation=status-quo, fleet=status-quo)`.

## Cross-bblock contract

- `scenarioType` is a free-text class name for the POSEIDON Java factory; the **machine-readable** axis state lives in `properties.scenario:axes` of the scenario STAC Item.
- Every embedded `$ref` to an upstream bblock MUST resolve to an Item whose `proj:epsg = 4326` and whose `grid:cell_size_nm` matches the map bblock's reference grid.
- A forecast scenario MUST NOT reference V-role series whose year-range extends past `simulatedFromYear` (the runner enforces this — see [poseidon-input-run-control]).
- Climate-projection scenarios MUST also override `regulations` to *not* assume current-climate TACs — at minimum, ICES forward advice (or BSAP targets) should be wired through `shocks[]`.
- The scenario Item is the carrier consumed by [poseidon-input-run-control]'s `scenario` field — it is the single handle through which a whole run is reproduced.
