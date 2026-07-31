# Seadots project

This is a collection of OGC Blocks for the [SeaDOTs project](http://seadots-project.eu).
It defines the indicator model, property relationship schema, and supporting ontologies
used across the three SeaDOTs Digital Twin demonstrators (Germany, Norway, Sweden).
See also: [iliad-apis-features](https://github.com/ogcincubator/iliad-apis-features) for data types and DT processes.


## Building Blocks

### `ogc.hosted.seadots.area-of-interest` — Marine Area of Interest

**Type:** schema

Simple GeoJSON Feature profile for a polygon delimiting a marine area of interest (AOI) used by experiments, monitoring programmes, or impact assessments. The polygon is carried only in the top-level GeoJSON `geometry`; `properties` carries a human-readable `title` and `description`.

### `ogc.hosted.seadots.benthic-biomass-observations-imr` — IMR Benthic Biomass Observations

**Type:** schema

GeoJSON FeatureCollection profile for raw IMR / MAREANO Marbunn benthic biomass observation point features across species and cruises. This block preserves individual sample records, while benthic-biomass-density-imr provides the aggregate per-taxon observation derived from those raw features.

### `ogc.hosted.seadots.geoparquet-header` — GeoParquet Header

**Type:** schema

Generic, reusable CSVW + GeoParquet 1.1 metadata header envelope shape (fileName, source, parquetSchema, geo). Dataset-specific GeoParquet profiles reference this schema via $ref rather than redefining the envelope inline.

### `ogc.hosted.seadots.obis-mareano-checklist` — OBIS MAREANO Checklist

**Type:** schema

Raw OBIS checklist response for selected MAREANO dataset identifiers. The example preserves the OBIS API payload as returned by the checklist endpoint and is used as source material for derived SeaDOTs biomass-density proxy examples.

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

### `ogc.hosted.seadots.catalog-application-package` — SeaDOTs Catalog Application Package

**Type:** schema

Generic APKG/CWL-aligned profile for the executable package attached to a SeaDOTs application record.

### `ogc.hosted.seadots.oim-variables` — OIM Variables

**Type:** model

Defines the OIM variable and indicator concept model for SEADOTS and ILIAD variable observations.

### `ogc.hosted.seadots.colonisation-time-factor` — Colonisation Time Factor (C_t)

**Type:** schema

OGC Feature + OIM Variable profile for the dimensionless time factor C_t in the reef-biomass equation. Encodes the colonisation curve as a closed-form expression (typically a logistic sigmoid) with its parameters plus an evaluated lookup table at discrete time points. Mandatory provenance flags whether the curve parameters are calibrated or illustrative.

### `ogc.hosted.seadots.emodnet-compliant-windfarm` — EMODnet-compliant windfarm

**Type:** schema

GeoJSON Feature profile aligned to the official EMODnet Human Activities windfarms XSD. It preserves the service's published field names and primitive types for country, turbine count, power output, status, installation type, year fields, distance to coast, and notes.

### `ogc.hosted.seadots.reef-aggregation-index` — Reef Aggregation Index (AF_i)

**Type:** schema

OGC Feature profile carrying per-taxon dimensionless reef aggregation index AF_i used by the reef-biomass equation. Treated as an OIM variable / indicator binding — one record per evidence basis (e.g. Degraer 2020 prior). Per-taxon rows carry scientificName, AphiaID, AF_i value, validityScope, and evidence URI.

### `ogc.hosted.seadots.reef-effect-output` — Reef Effect Output

**Type:** schema

OGC API Records profile for describing a single output artefact produced by the reef-effect calculation. Captures the output role, format, vocabulary term for the produced quantity, producing experiment URI, conformance classes, and inline result values with provenance.

### `ogc.hosted.seadots.benthic-biomass-density-imr` — IMR Benthic Biomass Density Observation

**Type:** schema

OGC Feature + SOSA observation profile for per-taxon benthic biomass density (kg m-2) sourced from the Institute of Marine Research (IMR / Havforskningsinstituttet) regional baseline series. Acts as the fallback `D_{pre,i}` binding when MAREANO has no taxon coverage at index i. Carries per-taxon density with explicit `uncertainty_kg_m2`, ICES area annotation, and mandatory provenance.

### `ogc.hosted.seadots.benthic-biomass-density-mareano` — MAREANO Benthic Biomass Density Observation

**Type:** schema

OGC Feature + SOSA observation profile for per-taxon benthic biomass density (kg m-2) derived from the MAREANO programme. Each record is a SOSA Observation of `benthic-biomass-density` over a polygon footprint and a sampling period, with the per-taxon values carried inline by `data.perTaxon[]` and mandatory provenance describing whether the values are retrieved or illustrative.

### `ogc.hosted.seadots.swedish-DT-simulations-output` — Swedish DT Simulations Output

**Type:** schema

Profile for Swedish Digital Twin herring/sprat fishery simulation output rows, with examples for the raw tabular artifact, a SensorThings Observation view, and a GeoParquet representation header. 17 of the 63 source columns are reserved-for-future-use placeholders, not region indicators.

### `ogc.hosted.seadots.floating-wind-infrastructure` — Floating-Wind Submerged Infrastructure

**Type:** schema

OGC Feature profile describing per-unit submerged geometry (wetted hull + mooring + anchor surfaces) of a floating-wind farm layout. Used as the feature-of-interest geometry input to reef-effect biomass equations (drives the A_sub aggregate). Inline `data` block carries per-unit areas, count, design label, aggregate submerged area, and sample unit coordinates; geometry travels in the top-level GeoJSON Polygon.

### `ogc.hosted.seadots.oim-variable-observation` — OIM Variable Observation

**Type:** schema

Schema profile for OIM/SOSA observations of SEADOTS variables and indicators, including numeric values mapped to observed-property IRIs from the OIM Variables building block.

### `ogc.hosted.seadots.odd-protocol` — ODD Protocol Description Record

**Type:** schema

OGC API Records profile for simulation model publications using the ODD Protocol (Overview, Design concepts, Details). Provides a structured, open-ended scaffold for describing agent-based and individual-based models; domain-specific vocabularies (NERC, CF, Darwin Core, ICES) are injected at the entity and variable level by domain profiles.

### `ogc.hosted.seadots.reef-effect-process` — Reef Effect Process

**Type:** schema

OGC API Processes Part 1 process description for the reef-effect biomass calculation, aligned with the OSPD pattern (ogc.osc.api-profiles.processes.ospd). Wraps the deterministic Python reproducibility script utsira_reef_biomass.py as an executable Process whose inputs are per-class SeaDOTs records (area-of-interest, floating-wind-infrastructure, benthic-biomass-density-mareano, benthic-biomass-density-imr, reef-aggregation-index, colonisation-time-factor) and whose output is a reef-effect-output record.

### `ogc.hosted.seadots.harvest-timeseries-scen-m3-source` — Harvest time series scenario Scen M3 — source GeoJSON

**Type:** schema

Source-faithful GeoJSON point time-series profile for the supplied harvest_timeseries_scenario_Scen_M3 export. It preserves the source feature identifier, Point geometry, bwmus numeric measurement and time string without assigning undocumented scientific meaning or units.

### `ogc.hosted.seadots.catalog-data` — SeaDOTs Catalog Data

**Type:** schema

Generic Records/DCAT, STAC Item, CF, and provenance profile for SeaDOTs catalog records that describe data artefacts independent of their workflow role or data type.

### `ogc.hosted.seadots.harvest-timeseries-scen-m3-geoparquet` — Harvest time series scenario Scen M3 — GeoParquet representation

**Type:** schema

GeoParquet representation of the source-faithful harvest_timeseries_scenario_Scen_M3 point time series: id, Point geometry, bwmus and time, unchanged from harvest-timeseries-scen-m3-source. geometry_types, bbox and CRS are derived from the actual data, not declared placeholders.

### `ogc.hosted.seadots.catalog-data-multidim` — SeaDOTs Catalog Data Multidimensional

**Type:** schema

OGC API Records profile for catalog records that describe multidimensional gridded or array-oriented data products, reusing the ILIAD STAC/DCAT multidimensional data profile.

### `ogc.hosted.seadots.catalog-data-tabular` — SeaDOTs Catalog Data Tabular

**Type:** schema

OGC API Records profile for catalog records that describe tabular data products (CSV/TSV, GeoParquet, Parquet, attribute tables), reusing the shared SeaDOTs catalog-data profile and adding tabular structural metadata (STAC table extension columns and GeoParquet column metadata).

### `ogc.hosted.seadots.catalog-workflow` — SeaDOTs Catalog Workflow

**Type:** schema

Generic OGC API Records and PROV-O profile for a discoverable reusable workflow, model, transformer, or digital-twin application.

### `ogc.hosted.seadots.catalog-data-tabular-survey` — SeaDOTs Catalog Data Tabular Survey

**Type:** schema

Tabular survey-data profile for the saltmarsh perceptions questionnaire, designed to carry ELSST thesaurus mappings, CESSDA controlled-vocabulary references, and DDI-style descriptive metadata for questionnaire variables and response categories.

### `ogc.hosted.seadots.catalog-execution` — SeaDOTs Catalog Execution

**Type:** schema

Generic OGC API Records and PROV-O profile for one concrete execution, experiment run, or digital twin run represented as links to workflow, input, and output records.

### `ogc.hosted.seadots.reef-effect` — Reef Effect

**Type:** schema

OGC API Records profile for describing the executable reef-effect calculation realising a documented model. Points at the code that runs the calculation and binds it to the ODD record, evidence equation, input records, and reef-effect-output records.

### `ogc.hosted.seadots.reef-effect-utsira` — Reef Effect Utsira Execution

**Type:** schema

Concrete catalog execution record for the Utsira reef-effect biomass run. Instantiates the reusable reef-effect workflow, links the Utsira input and output records, and carries run-specific bindings, runtime details, and success criteria.

