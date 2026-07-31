# Harvest time series scenario Scen M3 — GeoParquet representation

GeoParquet representation of the same source data as
[harvest-timeseries-scen-m3-source](../harvest-timeseries-scen-m3-source/):
19,920 Point features (83 spatial-series identifiers × 240 timestamps), each
with a numeric `bwmus` value and a `time` string, unchanged from the source.
This block adds no properties and resolves no additional semantics beyond
what `harvest-timeseries-scen-m3-source`'s own `context.jsonld` already
defines — it exists to declare a GeoParquet physical representation of the
same data, built on the shared [GeoParquet Header](../geoparquet-header/)
envelope schema.

## Provenance

The example header (`examples/harvest-timeseries-scen-m3-header.json`) was
generated directly from
`harvest-timeseries-scen-m3-source/examples/harvest-timeseries-scen-m3-sample.geojson`
using the `geojson-to-geoparquet` skill (ogcaibb
`skills/geojson-to-geoparquet/scripts/geojson_to_geoparquet.py`):

```bash
python3 <path-to-ogcaibb>/skills/geojson-to-geoparquet/scripts/geojson_to_geoparquet.py \
  --input ../harvest-timeseries-scen-m3-source/examples/harvest-timeseries-scen-m3-sample.geojson \
  --output harvest-timeseries-scen-m3.geoparquet \
  --write-header examples/harvest-timeseries-scen-m3-header.json \
  --source-href "../harvest-timeseries-scen-m3-source/examples/harvest-timeseries-scen-m3-sample.geojson" \
  --context ../harvest-timeseries-scen-m3-source/context.jsonld
```

`geometry_types` (`["Point"]`), the `bbox`, and the row/column counts in the
header are computed from the real 19,920-feature source, not asserted by
hand. The `crs` is a full PROJJSON `OGC:CRS84` object (the script's built-in
default) — never the hand-typed shorthand that, in an earlier revision of
the sibling `swedish-DT-simulations-output` block, parsed as JSON but broke
real GeoParquet readers at read time; the shared `geoparquet-header` schema
now rejects that shape outright.

`examples/harvest-timeseries-scen-m3.geoparquet` itself is a derived build
artifact and is **not** committed — regenerate it with the command above
(drop `--write-header` if you only need the Parquet file) and sanity-check
it opens before trusting it:

```bash
python3 -c "import geopandas as gpd; print(gpd.read_parquet('harvest-timeseries-scen-m3.geoparquet').shape)"
```

## Known gaps (inherited from the source)

Same as `harvest-timeseries-scen-m3-source`: `bwmus` has no authoritative
scientific definition or unit, and `time` has no declared timezone or
calendar. This block does not resolve either — see that block's description
for details and recommended fallbacks.
