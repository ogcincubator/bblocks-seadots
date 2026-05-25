# IMR Benthic Biomass Density Observation

OGC Feature + SOSA Observation profile for per-taxon benthic biomass density (kg m⁻²) sourced from the Institute of Marine Research (IMR / Havforskningsinstituttet) regional baseline series.

Used as the **fallback** `D_{pre,i}` binding when MAREANO has no taxon coverage at index `i`. Compared to the MAREANO bblock, this record carries:
- explicit per-taxon `uncertainty_kg_m2` (MAREANO's row does not);
- an `icesDivision` annotation (e.g. `IVa`);
- a `method` description.

Otherwise the shape mirrors MAREANO so the two are interchangeable downstream.

## Dependency

Extends `ogc.hosted.iliad.api.features.oim-obs`.

## Required fields for script consumption

`_sources/reef-effect/scripts/utsira_reef_biomass.py` reads `data.perTaxon[].scientificName`, `data.perTaxon[].density_kg_m2`, and `data.perTaxon[].uncertainty_kg_m2`. All three are marked `required` in the schema.

## Retrieval

IMR does not expose a single REST endpoint for "per-taxon baseline density on an AOI". Cruise sample series are distributed via the Norwegian Marine Data Centre (NMD) as discrete datasets. The `data.source` URL in the example is a NOTIONAL endpoint — flagged in `data.provenance.verificationGap`.
