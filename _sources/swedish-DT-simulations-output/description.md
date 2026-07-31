# Swedish DT Simulations Output

This building block describes Swedish Digital Twin fisheries simulation output
rows for herring and sprat fishery state, produced by an agent-based model.

The source artifact is preserved as supplied in
`examples/eurostat nuts regions.qgz`: a whitespace-delimited simulation table
with 60,000 data rows and 63 columns, of which 46 are populated fishery,
market, and management-scenario indicators/parameters and 17 (`fu_01` ..
`fu_17`) are reserved-for-future-use placeholder columns, always 0 in the
supplied data (see `indp:reserved-for-future-use` in the
[OIM Variables](../oim-variables/) building block). The `fu_` prefix is a
naming artifact of the source model, not a resolved region or NUTS code; the
placeholder columns should not be treated as region indicators until the model
owner defines their intended meaning. The profile also documents two
interoperable views over the same artifact:

- a SensorThings `Observation` view that treats a selected simulation row as an
  observation of herring and sprat fishery state;
- a GeoParquet representation header that declares the tabular columns and the
  expected GeoParquet metadata for a geometry-joined conversion.

The GeoParquet header is intentionally metadata-only: the supplied source does
not embed row-level geometry, and no region geometry is currently joined via
the reserved placeholder columns. The examples therefore include an
approximate Swedish case-region footprint spanning northern Baltic/Bothnian Sea
case waters southward to Gotland Island as a single-region placeholder. A
production GeoParquet file should replace or refine this footprint with
authoritative region geometry once the reserved columns are given real
semantics.

## Regenerating the GeoParquet example

`examples/simulation_1.geoparquet` is a derived build artifact and is **not**
committed to this repository — regenerate it locally when you need it.

Prerequisites:

```bash
python3 -m pip install pyarrow          # required
python3 -m pip install pyproj geopandas # optional, only to generate/validate the crs block
```

Two converters are available:

- `examples/convert_csv_to_geoparquet.py` — the original project-local
  script; defaults match this block's files (`simulation_1.csv` +
  `simulation_1.geoparquet-header.json`), so it runs with no flags:

  ```bash
  python3 examples/convert_csv_to_geoparquet.py
  ```

- the generalized, parameterized version, `csv-to-geoparquet` (ogcaibb
  `skills/csv-to-geoparquet/scripts/csv_to_geoparquet.py`) — recommended,
  since it also runs a CRS sanity check that catches an invalid PROJJSON
  `crs` block before a real reader rejects the file (the bug this header
  originally shipped with):

  ```bash
  python3 <path-to-ogcaibb>/skills/csv-to-geoparquet/scripts/csv_to_geoparquet.py \
    --csv examples/simulation_1.csv \
    --header examples/simulation_1.geoparquet-header.json \
    --delimiter " "
  ```

Either way, sanity-check the output actually opens before trusting it:

```bash
python3 -c "import geopandas as gpd; print(gpd.read_parquet('examples/simulation_1.geoparquet').shape)"
```
