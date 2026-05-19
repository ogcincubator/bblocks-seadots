# Reef Aggregation Index (AF_i)

OGC Feature + OIM Variable profile for per-taxon dimensionless reef aggregation index `AF_i` consumed by the reef-biomass equation `B_reef = sum_i (A_sub · D_pre,i · AF_i · C_t)`.

Each record collects a set of `AF_i` bindings sharing one evidence basis (e.g. Degraer 2020 synthesis). Per-taxon rows carry `scientificName`, WoRMS `aphiaID`, the dimensionless `AF_i` value, a `validityScope` annotation (e.g. depth band, substrate type), and an `evidence` URI.

## Dependency

Extends `ogc.hosted.iliad.api.features.oim-variables` — `AF_i` is an indicator/variable in the OIM sense.

## Required fields for script consumption

`_sources/experiment/scripts/utsira_reef_biomass.py` reads `data.perTaxon[].scientificName` and `data.perTaxon[].AF_i`. Both are marked `required` in the schema.

## Vocabulary

The indicator concept `indo:reef-aggregation-index` is local to the SeaDOTs indicator namespace. No external community vocabulary defines a per-m² reef-effect aggregation coefficient at the time of writing — flagged in `context-validation-report.md`.
