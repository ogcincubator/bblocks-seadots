# Swedish DT Simulations Output

This building block describes Swedish Digital Twin fisheries simulation output
rows keyed by Eurostat NUTS-region indicator columns.

The source artifact is preserved as supplied in
`examples/eurostat nuts regions.qgz`: a whitespace-delimited simulation table
with 60,000 data rows and 63 columns. The profile also documents two
interoperable views over the same artifact:

- a SensorThings `Observation` view that treats a selected simulation row as an
  observation of herring and sprat fishery state for the active NUTS-region
  indicator set;
- a GeoParquet representation header that declares the tabular columns, NUTS
  region attributes, and the expected GeoParquet metadata for a geometry-joined
  conversion.

The GeoParquet header is intentionally metadata-only: the supplied source does
not embed row-level NUTS geometries. The examples therefore include an
approximate Swedish case-region footprint spanning northern Baltic/Bothnian Sea
case waters southward to Gotland Island. A production GeoParquet file should
replace or refine this footprint with authoritative Eurostat NUTS geometries
before writing WKB geometry.
