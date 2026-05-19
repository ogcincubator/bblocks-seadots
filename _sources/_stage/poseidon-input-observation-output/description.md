# POSEIDON Observation and Output Selection Input

POSEIDON runs consume output-selection inputs that determine which indicators, columns, time series, or logger products are written. This input is important for reproducibility because optimization objectives and reported policy outcomes depend on which observations are collected and at what cadence.

## Target building block

The chosen observations are materialised in EDITO-compliant form by the companion target bblock [poseidon-output]. There:

- Each `columns[]` entry here becomes one entry under `timeSeries[]` or `agentLogs[]` there.
- Each `loggers[]` entry here becomes one or more `gridded[]` / `events[]` entries there, depending on the logger type (heatmap loggers → GeoZarr; event loggers → GeoParquet event log).
- Each `outputProducts[]` STAC pointer here resolves to a STAC Item under the run's output Collection.

The two bblocks are bound by `runId` (chosen at run start) and the input bundle `runConfigRef` (set at output-manifest write time).

[poseidon-output]: ../poseidon-output/

## Raw POSEIDON output → EDITO target transform

POSEIDON natively writes plain CSV and ASCII-grid files into a run directory. The transform below converts those raw files into the EDITO-compliant products declared by [poseidon-output]. A single transformer (one Python or Java step at end-of-run) is enough; nothing in POSEIDON itself needs to change.

| Raw artefact written by POSEIDON | Selection that triggers it (this bblock) | EDITO target (`poseidon-output`) | Transformation |
|---|---|---|---|
| `<run>/<column>.csv` — single time-series per `columns[]` entry, one row per step | `columns: [...]` + `cadence` | `timeSeries[]` entry, GeoParquet | Read CSV → cast to typed columns `(year, step, value)` (or `(year, species, value)` for per-species); emit Parquet partitioned by `year`. Set `dimension` based on whether the column name carries a species/fisher/segment qualifier (parsed from POSEIDON column-name conventions). |
| `<run>/yearly-results.csv` — multi-column annual table | `cadence: yearly` (default) | One `timeSeries[]` entry **per column** | Pivot wide CSV to long; produce one Parquet per column so STAC Items remain single-indicator and indexable. |
| `<run>/daily-results.csv` — multi-column daily table | `cadence: daily` | One `timeSeries[]` entry per column, `cadence: daily` | Same pivot; partition Parquet by `year`. |
| `<run>/<fisher>.csv` per fisher — trip records | `loggers: [{type: "Trip Logger"}]` or `"Detailed Fisher Logger"` | One `agentLogs[]` entry, GeoParquet | Concatenate all fisher CSVs; rebuild trip geometries (LINESTRING from successive `(lon, lat)` rows per `trip_id`); columns `cfr_id, trip_id, departure_locode, return_locode, gear, catch_kg, revenue_eur, geometry`. |
| `<run>/heatmap-<metric>-<year>.csv` or ASCII grid | `loggers: [{type: "Heatmap Logger", variable: "..."}]` | One `gridded[]` entry, GeoZarr | Stack per-year files along `time`; reproject to EPSG:4326 if not already; align to `gridRef` = canonical grid Item from [poseidon-input-map]; write Zarr v3 with `_ARRAY_DIMENSIONS`, `spatial_ref`, both `timeChunked` and `geoChunked` variants. |
| `<run>/events.csv` — discrete events | `loggers: [{type: "Event Logger"}]` | One or more `events[]` entries | Filter by `event_type`; emit one Parquet per event class (e.g. `closures.parquet`, `exits.parquet`). |
| `<run>/snapshot-<year>.yaml` / final-state CSVs | `loggers: [{type: "Snapshot Logger"}]` | `gridded[]` entry for spatial state; `timeSeries[]` entry with `cadence: end-of-run` for scalars | Per-cell snapshot → Zarr; scalar snapshot → Parquet row. |
| `<run>/config-resolved.yaml` — the parameters POSEIDON actually used | always written | `runMetadata` + `runConfigRef` on the target manifest | Parse YAML; compute SHA-256 over canonicalised form; publish as a sibling STAC Item; set `runConfigRef` to that Item's URI. |

### STAC publication

After the transform, the runner:

1. Creates STAC Collection `poseidon-output-<area>` if it does not yet exist.
2. Creates one STAC Item per Parquet/Zarr asset, with:
   - `id` = `<runId>-<productName>`
   - `properties.processing:lineage` = list of upstream input-bblock STAC Item URIs and the POSEIDON git commit hash
   - `assets.data.href` = S3 URI of the Parquet/Zarr file
   - `assets.data.type` = `application/vnd.apache.parquet` or `application/vnd.zarr`
3. Writes a top-level `manifest.json` conforming to [poseidon-output]; that JSON is what downstream consumers read.

### Validation pairing

For back-cast runs, the transformer additionally populates `validationLinks[]` on the target manifest:

- For every `columns[]` entry that has an empirical analogue declared in [poseidon-input-biology] or [poseidon-input-fleet] (V-role sources), compute the requested metric (RMSE / Pearson r / KS / IoU) against the held-out series.
- Emit one `validationLinks[]` row per pairing, referencing the empirical STAC Item and recording the metric value.

This is how the back-cast harness materialises: empirical V-role data declared as input becomes the comparison target for the output declared here.

## Selection conventions

To make the raw→target transform deterministic:

- `columns[]` strings MUST use POSEIDON's column naming convention (e.g. `"Species 0 Biomass"`, `"Average Cash-Flow"`). The transformer parses these to set `dimension` on the target.
- `loggers[].type` strings MUST match POSEIDON logger class names (see the POSEIDON repository). Unknown logger types are skipped (with a warning) rather than silently dropped.
- `cadence` set here is propagated 1:1 to the target's `cadence` field.
- `outputProducts[]` STAC pointers are passed through to the target Collection's `assets` listing; this is the place to attach derived products (figures, dashboards, reports) that the transformer itself does not generate.

## What changed vs the previous version of this bblock

Earlier versions of this bblock described only the *selection* of POSEIDON outputs (column names, cadence, logger types). The selection itself is unchanged. New here:

- An explicit **target bblock** ([poseidon-output]) that declares the EDITO-compliant shape every selected product takes on disk.
- An explicit **raw → target transform** table so a runner can deterministically convert a POSEIDON run directory into a STAC-indexed Collection of GeoParquet + GeoZarr assets.
- A **validation pairing** rule that closes the loop with the V-role sources declared in [poseidon-input-biology] and [poseidon-input-fleet].
