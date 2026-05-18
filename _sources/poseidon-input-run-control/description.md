# POSEIDON Run Control Input

This building block describes the top-level controls needed to execute the implemented POSEIDON model: which scenario YAML to load, whether an additional policy or shock file is applied, how long to run, which random seed and replicate count to use, and where outputs are written.

It intentionally references the other POSEIDON input blocks instead of expanding every scenario component inline.

## Role within the input stack

Run-control is the **orchestration glue**: it does not carry external observational data itself. Instead, it composes upstream input bblocks ([poseidon-input-scenario], [poseidon-input-regulation-policy], [poseidon-input-observation-output]) into a launchable bundle and decides three orthogonal axes:

- **Time horizon** — `yearsToRun` and the implied calendar window.
- **Stochasticity** — `randomSeed` + `replicates`.
- **Output sink** — `outputDirectory` (EDITO S3 prefix) and `outputSelection` (which observations).

Because the data inputs live in upstream bblocks, the R/S/V classification used elsewhere does not apply here in the same way. Instead, this bblock has **time-window constraints** imposed by the availability windows of upstream V-role sources.

## Time-window constraints inherited from upstream sources

| Constraint | Origin bblock | Available range | Effect on `yearsToRun` / scenario start |
|---|---|---|---|
| Copernicus BAL physics reanalysis | [poseidon-input-scenario] (via [poseidon-input-biology]/[poseidon-input-map]) | 1993 → present minus 1 year | Earliest hindcast start year = 1993 |
| Copernicus BAL physics forecast | [poseidon-input-scenario] | Present → ~10 days ahead; seasonal forecast extends further | Forecast horizon caps `yearsToRun` for prospective runs unless climate downscaling is plugged in |
| ICES WGBFAS SAG time series | [poseidon-input-biology] (R) and [poseidon-input-optimization] (objective) | Typically 1980s → present for major Baltic stocks | Calibration window upper-bounded by latest assessment year |
| DATRAS BITS quarterly trawl survey | [poseidon-input-biology] (R for Abundance initializer) | 2001 (Q4 series) / 1985 (Q1 series) → present | Length-structure calibration starts no earlier than 2001 for full Q1+Q4 |
| ICES VMS / Logbook DB | [poseidon-input-fleet] (R) | 2009 → present | Spatial-effort prior earliest = 2009 (or 2012 if GFW used instead) |
| Global Fishing Watch | [poseidon-input-fleet] (S) | 2012 → 2024 (current public release) | AIS-based effort prior starts 2012 |
| EUMOFA monthly first-sale prices | [poseidon-input-port-market] (R) | 2009 → present | Revenue calibration starts no earlier than 2009 |
| EU Council Baltic TAC Regulation | [poseidon-input-regulation-policy] (R) | Annual since 1983 | TACs available across the entire reanalysis window |

The **runner-enforced rule** is: the *intersection* of the year-ranges of every R-role source actually used in the run defines the legal `yearsToRun` window. The runner validates this before launching.

## Sources specific to run-control

These do not deliver scientific data; they are run-time references.

| Source | Role | Provides | Feeds field(s) | Related bblock(s) |
|---|---|---|---|---|
| EDITO Data Lake S3 conventions | required | `s3://edito-pilot/<area>/output/<runId>/` path layout | `outputDirectory` | [poseidon-output] |
| STAC catalogue endpoint (`stac.marine.copernicus.eu`) | required | Collection / Item resolver | `scenario` URI when scenario is a STAC Item | [poseidon-input-scenario] |
| POSEIDON release version | required | Java JAR / Docker image tag | (runner metadata, not a schema field) | [poseidon-model] |
| OGC Processes API endpoint (EDITO Model Lab) | optional | Job submission endpoint | – (not in schema; recorded in `runMetadata` of [poseidon-output]) | [poseidon-output] |
| Compute environment specification | optional | CPU/RAM/replicate parallelism plan | – (advisory) | – |

[poseidon-input-scenario]: ../poseidon-input-scenario/
[poseidon-input-biology]: ../poseidon-input-biology/
[poseidon-input-fleet]: ../poseidon-input-fleet/
[poseidon-input-map]: ../poseidon-input-map/
[poseidon-input-port-market]: ../poseidon-input-port-market/
[poseidon-input-regulation-policy]: ../poseidon-input-regulation-policy/
[poseidon-input-observation-output]: ../poseidon-input-observation-output/
[poseidon-input-optimization]: ../poseidon-input-optimization/
[poseidon-output]: ../poseidon-output/
[poseidon-model]: ../poseidon-model/

## EDITO orchestration contract

When the run is launched on EDITO Model Lab via OGC Processes API:

1. **Scenario resolution** — `scenario` is a STAC Item URI that aggregates the input-bblock Items used. The runner downloads / mounts each referenced asset (Parquet, Zarr).
2. **Output path** — `outputDirectory` MUST be of the form `s3://edito-pilot/<area>/output/<runId>/` where `<runId>` is the value emitted as `runId` in the [poseidon-output] manifest.
3. **Manifest writing** — at end of run the transformer described in [poseidon-input-observation-output] writes `manifest.json` conforming to [poseidon-output] under that prefix and publishes one STAC Item per asset under `poseidon-output-<area>`.
4. **Provenance** — `runMetadata.modelVersion` and the SHA-256 of the resolved scenario config are written into the manifest; the runner also pushes a `runConfigRef` STAC Item that re-resolves to the *exact* scenario actually executed.
5. **Replicates** — `replicates > 1` produces one [poseidon-output] manifest per replicate, all sharing the same Collection; the replicate index is encoded in the Item id suffix.

## Two-stage transformation pipeline

For this bblock the "two-stage" pattern degenerates: there are no raw → EDITO transforms because run-control consumes no external observational data. The relevant pipeline is:

### Stage A — input bundle assembly (Source → EDITO)

| Input | EDITO artefact | Transformation |
|---|---|---|
| Resolved [poseidon-input-scenario] + all transitively referenced input-bblock Items | `runs/<runId>/scenario-bundle.json` (STAC Item) | Walk the scenario tree; emit a STAC Item with one `assets.<bblockname>` link per input bblock; `properties.processing:lineage` records the upstream STAC Item URIs. |

### Stage B — EDITO → POSEIDON

| EDITO artefact | POSEIDON field(s) | Transformation |
|---|---|---|
| `scenario-bundle.json` | `scenario` | Set to the bundle Item URI. |
| Optional policy bundle Item | `policy` | Set if a regulation-only Item is supplied as override. |
| `outputDirectory` | `outputDirectory` | `s3://edito-pilot/<area>/output/<runId>/` |
| `outputSelection` | `outputSelection` | URI of the [poseidon-input-observation-output] Item used. |

### Run-control choices that are *not* data-driven

| Field | Decision rule for the pilot |
|---|---|
| `yearsToRun` | 30-year back-cast (typically 1993–2023 or 2001–2023 depending on whether BITS Q4 series is used) for calibration; 30-year forecast (2025–2055) for projection. |
| `randomSeed` | Fixed for reproducibility (e.g. 42); randomised across replicates only via internal seed offsets. |
| `replicates` | 3 for production runs; 10 for noise-sensitive optimization evaluations (set by [poseidon-input-optimization]). |

## Required vs substitutable vs validation-only

The R/S/V dimension does not apply to run-control directly — it inherits constraints from upstream bblocks. The user-facing required set per run is simply:

1. A resolved `scenario` reference (R).
2. `yearsToRun` (R).
3. `outputDirectory` (R for any non-throwaway run).
4. `outputSelection` (R when [poseidon-output] is consumed downstream).

## Minimal viable bundle

1. **Scenario STAC Item** — bundle of map + biology + fleet + port-market + regulation-policy + observation-output for the pilot.
2. **`yearsToRun`** — set to the intersection of upstream V-role year-ranges (typically 2010–2023 for a Baltic back-cast).
3. **`outputDirectory`** — `s3://edito-pilot/north-gotland/output/<runId>/`.
4. **`outputSelection`** STAC Item URI — points at the [poseidon-input-observation-output] configuration used.

## Cross-bblock contract

- `scenario` MUST resolve to a [poseidon-input-scenario] Item whose `map.gridRef` matches the canonical grid used by all transitively referenced bblocks.
- `policy`, when supplied, overrides any `regulations` embedded inside `scenario` — both must use the same closure-ID space declared in [poseidon-input-map].
- `outputSelection` MUST refer to a [poseidon-input-observation-output] Item that lists exactly the columns / loggers consumed by the objective in [poseidon-input-optimization] (if optimization is used).
- The runner enforces year-range consistency by intersecting upstream R-role source windows against `yearsToRun`; a mismatch fails the job before launch.
- The [poseidon-output] manifest written under `outputDirectory` is the single artefact carried back into validation, optimization, and downstream analysis.
