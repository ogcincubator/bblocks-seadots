# IMR Benthic Biomass Density Observation

OGC Feature + SOSA Observation profile for per-taxon benthic biomass density (kg m⁻²) sourced from the Institute of Marine Research (IMR / Havforskningsinstituttet) regional baseline series.

Used as the **fallback** `D_{pre,i}` binding when MAREANO has no taxon coverage at index `i`. Compared to the MAREANO bblock, this record carries:
- explicit per-taxon `uncertainty_kg_m2` (MAREANO's row does not);
- an `icesDivision` annotation (e.g. `IVa`);
- a `method` description.

Otherwise the shape mirrors MAREANO so the two are interchangeable downstream.

The raw per-sample Marbunn FeatureCollection and its collector script live in
the companion block [`benthic-biomass-observations-imr`](../benthic-biomass-observations-imr/).
This block keeps only the aggregate per-taxon observation used by downstream
reef-effect calculations.

## Dependency

Extends `ogc.hosted.iliad.api.features.oim-obs`.

## Required fields for script consumption

`_sources/reef-effect/scripts/utsira_reef_biomass.py` reads `data.perTaxon[].scientificName`, `data.perTaxon[].density_kg_m2`, and `data.perTaxon[].uncertainty_kg_m2`. All three are marked `required` in the schema.

## Retrieval

The aggregate example is built from the MAREANO Marbunn API using
`build_example.py`. It groups catch-sample records by species and summarizes
their weights, while the raw block preserves the individual point features.
