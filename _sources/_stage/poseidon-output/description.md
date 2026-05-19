# POSEIDON Output (EDITO target)

This building block declares the **target schema** for the outputs of a POSEIDON run, published in EDITO-compliant form. Every product is one of:

- **Tabular / time-series** → GeoParquet 1.1 (non-spatial allowed; `geometry` column present where the indicator has a spatial dimension, CRS EPSG:4326, WKB encoding).
- **Per-agent log** → GeoParquet 1.1 (`geometry` carries fisher home-port POINT, trip LINESTRING, or POLYGON of operating zone).
- **Gridded** → GeoZarr (Zarr v3 store, CF coords `time, lat, lon`, `_ARRAY_DIMENSIONS`, `spatial_ref` aux coord, time-chunked and geo-chunked variants).
- **Event log** → GeoParquet 1.1 (timestamped discrete events: closures triggered, vessel exits, regulation invocations).

All products of a single run share one **STAC Collection** (`stacCollection`); each product is its own **STAC Item**. The manifest object described by this schema is the JSON payload conventionally stored alongside the Collection as `manifest.json`.

## Relation to other bblocks

- **Input side** — [poseidon-input-observation-output] selects which `columns`, `loggers`, `cadence`, and `outputProducts` POSEIDON writes during a run. Each selection there projects to one entry of `timeSeries[]`, `agentLogs[]`, `gridded[]`, or `events[]` here.
- **Spatial frame** — `gridded[].gridRef` MUST point at the canonical grid Item declared in [poseidon-input-map]. POSEIDON gridded outputs are written on that same grid; no resampling at output time.
- **Validation** — `validationLinks[]` references the empirical series listed in [poseidon-input-biology] (V-role sources: SAG SSB time series, BITS length frequencies, OBIS occurrences) and [poseidon-input-fleet] (V-role sources: HELCOM fishing-intensity grids, AIS tracks). The model→empirical pairs and the comparison metric form the validation harness.
- **Run config provenance** — `runConfigRef` MUST resolve to the STAC Item bundling the input configuration (a Collection or Item that aggregates the `poseidon-input-*` bblocks for the run).
- **Regulation feedback** — `events[]` of type `ClosureInvocation` are co-keyed with closure IDs declared in [poseidon-input-regulation-policy] and [poseidon-input-map].

[poseidon-input-observation-output]: ../poseidon-input-observation-output/
[poseidon-input-biology]: ../poseidon-input-biology/
[poseidon-input-fleet]: ../poseidon-input-fleet/
[poseidon-input-map]: ../poseidon-input-map/
[poseidon-input-regulation-policy]: ../poseidon-input-regulation-policy/

## Container conventions

- **Object store layout**: `s3://edito-pilot/<area>/output/<runId>/<product>.{parquet|zarr}` for pilot runs.
- **STAC Collection ID**: `poseidon-output-<area>` (one Collection per pilot area; per-run Items inside).
- **MIME types**:
  - `application/vnd.apache.parquet` for GeoParquet
  - `application/vnd.zarr` (directory store) or `application/vnd.zarr+zip` (single-file)
- **GeoParquet partitioning**: `year` for long simulations; never partition on agent ID (low-cardinality fields preferred).
- **GeoZarr chunking**: `timeChunked` (1 × 720 × 512) when downstream use is spatial maps; `geoChunked` (138 × 32 × 64) when downstream use is per-cell time series. Both variants are encouraged for the fishing-effort heatmap because viewers and validation pipelines have different access patterns.
- **CRS**: EPSG:4326 across the board.

## Schema highlights

- `runId` (required) — UUID-style identifier for the run, used as the S3 prefix and as the STAC Item id suffix.
- `runConfigRef` — URI of the input bundle Item; closes the provenance loop.
- `timeSeries[]` (required, ≥1) — every selected column from the input observation-output bblock surfaces here, one per indicator. `dimension` distinguishes `global` (single series), `per-species`, `per-fisher`, `per-port`, `per-segment`.
- `agentLogs[]` — optional but recommended for fleet-rich runs; each log carries the agent type and spatial geometry.
- `gridded[]` — at least one entry for any run that uses spatial regulation, MPA evaluation, or diffusion calibration.
- `events[]` — required when regulation is enabled; carries closure-invocation, quota-binding, vessel-exit events.
- `validationLinks[]` — populated only for back-cast runs; lists model→empirical pairings and the score.

See `examples/output.json` for a complete pilot manifest.
