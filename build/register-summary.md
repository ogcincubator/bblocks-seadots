# Seadots project

This is a collection of OGC Blocks for the [SeaDOTs project](http://seadots-project.eu).
It defines the indicator model, property relationship schema, and supporting ontologies
used across the three SeaDOTs Digital Twin demonstrators (Germany, Norway, Sweden).
See also: [iliad-apis-features](https://github.com/ogcincubator/iliad-apis-features) for data types and DT processes.


## Building Blocks

### `ogc.hosted.seadots.ontology` — Property relationship ontology

**Type:** model

This ontology provides classes and properties to model property relationships with magnitude

### `ogc.hosted.seadots.properties` — Seadots Properties

**Type:** model

Defines seadots properties

### `ogc.hosted.seadots.property-relationship` — Property relationship

**Type:** schema

Provides a common model for defining property relationships bound to the ontology

### `ogc.hosted.seadots.equation-property-relationship` — Equation property relationship

**Type:** schema

Specialised property relationship profile for declaring that a source property is an explicit term in the canonical equation of a derived target property.

### `ogc.hosted.seadots.colonisation-time-factor` — Colonisation Time Factor (C_t)

**Type:** schema

OGC Feature + OIM Variable profile for the dimensionless time factor C_t in the reef-biomass equation. Encodes the colonisation curve as a closed-form expression (typically a logistic sigmoid) with its parameters plus an evaluated lookup table at discrete time points. Mandatory provenance flags whether the curve parameters are calibrated or illustrative.

### `ogc.hosted.seadots.experiment-output` — Computational Experiment Output

**Type:** schema

OGC API Records profile for describing a single output artefact produced by a computational experiment. Captures the kind of output (primary result, catalog, provenance), the format, the vocabulary term for the produced quantity, and the URI of the experiment that produced it. Carries inline result values with mandatory provenance (computed / retrieved / illustrative / mixed). Designed to be referenced by an `experiment` record so that one output definition can be reused across runs and audits.

### `ogc.hosted.seadots.reef-aggregation-index` — Reef Aggregation Index (AF_i)

**Type:** schema

OGC Feature profile carrying per-taxon dimensionless reef aggregation index AF_i used by the reef-biomass equation. Treated as an OIM variable / indicator binding — one record per evidence basis (e.g. Degraer 2020 prior). Per-taxon rows carry scientificName, AphiaID, AF_i value, validityScope, and evidence URI.

### `ogc.hosted.seadots.benthic-biomass-density-imr` — IMR Benthic Biomass Density Observation

**Type:** schema

OGC Feature + SOSA observation profile for per-taxon benthic biomass density (kg m-2) sourced from the Institute of Marine Research (IMR / Havforskningsinstituttet) regional baseline series. Acts as the fallback `D_{pre,i}` binding when MAREANO has no taxon coverage at index i. Carries per-taxon density with explicit `uncertainty_kg_m2`, ICES area annotation, and mandatory provenance.

### `ogc.hosted.seadots.benthic-biomass-density-mareano` — MAREANO Benthic Biomass Density Observation

**Type:** schema

OGC Feature + SOSA observation profile for per-taxon benthic biomass density (kg m-2) derived from the MAREANO programme. Each record is a SOSA Observation of `benthic-biomass-density` over a polygon footprint and a sampling period, with the per-taxon values carried inline by `data.perTaxon[]` and mandatory provenance describing whether the values are retrieved or illustrative.

### `ogc.hosted.seadots.area-of-interest` — Marine Area of Interest

**Type:** schema

OGC Feature profile for a polygon delimiting a marine area of interest (AOI) used by experiments, monitoring programmes, or impact assessments. Carries the bbox, centroid, area, and CRS as a self-contained inline `data` block with mandatory provenance. Geometry travels in the top-level GeoJSON `geometry` field.

### `ogc.hosted.seadots.floating-wind-infrastructure` — Floating-Wind Submerged Infrastructure

**Type:** schema

OGC Feature profile describing per-unit submerged geometry (wetted hull + mooring + anchor surfaces) of a floating-wind farm layout. Used as the feature-of-interest geometry input to reef-effect biomass equations (drives the A_sub aggregate). Inline `data` block carries per-unit areas, count, design label, aggregate submerged area, and sample unit coordinates; geometry travels in the top-level GeoJSON Polygon.

### `ogc.hosted.seadots.oim-variable-observation` — OIM Variable Observation

**Type:** schema

Schema profile for OIM/SOSA observations of SEADOTS variables and indicators, including numeric values mapped to observed-property IRIs from the OIM Variables building block.

### `ogc.hosted.seadots.odd-protocol` — ODD Protocol Description Record

**Type:** schema

OGC API Records profile for simulation model publications using the ODD Protocol (Overview, Design concepts, Details). Provides a structured, open-ended scaffold for describing agent-based and individual-based models; domain-specific vocabularies (NERC, CF, Darwin Core, ICES) are injected at the entity and variable level by domain profiles.

### `ogc.hosted.seadots.experiment` — Computational Experiment

**Type:** schema

OGC API Records profile for describing a computational experiment realising a documented model. Points at the executable code that runs the experiment (any language / format that exists and runs — Python, Jupyter, R, …), and binds it to the documented model (an ODD record), the evidence equation (an `equation-property-relationship` record), and to standalone input records (one per data class) and `experiment-output` records, all referenced by URI.

