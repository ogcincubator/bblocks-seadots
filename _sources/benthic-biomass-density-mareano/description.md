# MAREANO Benthic Biomass Density Observation

OGC Feature + SOSA Observation profile for per-taxon benthic biomass density (kg m⁻²) sourced from the MAREANO programme.

Each record is a SOSA Observation:
- `sosa:observedProperty` → `indo:benthic-biomass-density-mareano`
- `sosa:hasFeatureOfInterest` → the AOI polygon URI (or inline polygon)
- `sosa:phenomenonTime` → the sampling period
- `sosa:hasResult` → the structured `data.perTaxon[]` array

`data.perTaxon[]` rows carry `scientificName`, `aphiaID` (WoRMS), `density_kg_m2`, `habitat`, `depthBand_m`, `nSamples`. `data.aggregateDensity_kg_m2` is the sum-over-taxa convenience scalar.

## Dependency

Extends `ogc.hosted.iliad.api.features.oim-obs` (SOSA observation profile in iliad-apis-features).

## Required fields for script consumption

The calculator `_sources/reef-effect/scripts/utsira_reef_biomass.py` reads `data.perTaxon[].scientificName` and `data.perTaxon[].density_kg_m2` to populate `D_pre,i`. Both are marked `required` in the schema.

## Retrieval

MAREANO does not expose a single REST endpoint that returns per-taxon biomass density aggregated over an arbitrary AOI. The realistic retrieval path is the OBIS occurrence API (per-record observations, aggregated off-line) — recorded under `data.provenance.nearestAuthoritativeSource`.
