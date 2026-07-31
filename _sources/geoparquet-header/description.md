# GeoParquet Header

This building block defines the generic, reusable envelope shape for a CSVW +
GeoParquet 1.1 metadata header: `fileName`, `encoding`, `source`
(`href`/`sourceFormat`/`rowCount`/`columnCount`), `parquetSchema` (per-column
`name`/`type`/`nullable`/`description`/`propertyUrl`), and `geo`
(`version`/`primary_column`/`columns`, including a `crs` block that must be
either omitted, a CRS identifier string, or a full PROJJSON object).

It exists so that dataset-specific GeoParquet profiles — such as
[Swedish DT Simulations Output](../swedish-DT-simulations-output/) and
[Harvest time series scenario Scen M3 — GeoParquet representation](../harvest-timeseries-scen-m3-geoparquet/)
— can `$ref` a single shared envelope definition instead of each redefining
it inline. The envelope was factored out of `swedish-DT-simulations-output`'s
`schema.yaml`, where it was originally defined ad hoc.

## Why `crs` is constrained

A previous dataset-specific header shipped a hand-written CRS shorthand
(`{"type": "GeographicCRS", "name": "WGS 84", "id": {"authority": "EPSG",
"code": 4326}}`) that parses as valid JSON but is not valid PROJJSON — it is
missing the `datum`/`datum_ensemble` (or `base_crs`/`source_crs`) keys a real
CRS definition requires. That header validated fine against a schema with no
`crs` constraint, but `geopandas.read_parquet()` (via `proj`) rejected the
resulting file outright with a `CRSError`. This schema's `crs` property
requires either `null` (the GeoParquet-spec default, meaning OGC:CRS84), a
plain identifier string, or an object that at minimum claims one of the keys
that makes a CRS definition complete — catching that exact mistake at schema
validation time instead of at read time.

## Producing a conformant header

- `csv-to-geoparquet` and `geojson-to-geoparquet` (ogcaibb skills) both emit
  headers that validate against this schema, and both refuse to emit the
  invalid CRS shorthand described above.
