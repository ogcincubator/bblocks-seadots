# SeaDOTs interoperability specifications

This repository is the workspace where interoperability specifications for the [SeaDOTs project](http://seadots-project.eu) are defined, tested and published. The specifications take the form of [OGC Blocks](https://ogcincubator.github.io/bblocks-docs/) (also known as OGC Building Blocks), and support the three SeaDOTs Digital Twin demonstrators (Germany, Norway, Sweden).

- **Browse the register:** <https://ogcincubator.github.io/bblocks-seadots/>
- **Validation report:** <https://ogcincubator.github.io/bblocks-seadots/build/tests/report.html>

> **Status:** this is a working space, not a set of finished standards. All 55 blocks currently have the status `under-development`, so identifiers and models may still change.

## What the blocks do

Each block packages some of the following for one data type, model or process: a JSON Schema, a JSON-LD context, an ontology or SHACL rules, validated examples and transforms. Across the register, they are used to:

- **Describe source data as supplied**, using source-faithful profiles of national, regional and community datasets.
- **Harmonise data to common models**, with declared transforms from source profiles to shared targets such as EMODnet-compliant features.
- **Define shared meaning**, through ontologies, indicators, observable properties and the relationships between them.
- **Make Digital Twin work reproducible**, through catalogue records that link workflows, inputs, outputs and executions with provenance.

The register builds on blocks from other registers, including the main OGC register, OGC API Features, Records and Processes, STAC, SensorThings, the Cross-Domain Model, Open Science and [ILIAD](https://github.com/ogcincubator/iliad-apis-features). The full list of imports is in [`bblocks-config.yaml`](bblocks-config.yaml).

## Block index

Blocks are organised into the groups below, using the `group` field in each block's `bblock.json`. The register viewer uses this field to group related blocks. Give any new block one of these groups.

| Group | Blocks | Scope |
|---|---|---|
| [Core Models & Shared Components](#core-models--shared-components) | 8 | Properties, indicators and relationships, plus components reused across themes |
| [Data & Workflow Catalogue](#data--workflow-catalogue) | 8 | Discovery records for data, workflows, executions and models |
| [Reef Effect](#reef-effect) | 7 | The reef-effect biomass calculation, its inputs, outputs and Utsira run |
| [Benthic Observations](#benthic-observations) | 4 | Benthic biomass and species data from IMR, MAREANO and OBIS |
| [Offshore Windfarms](#offshore-windfarms) | 7 | Common windfarm model, source profiles and EMODnet alignment |
| [Protected Areas](#protected-areas) | 7 | EMODnet-compliant protected areas and source profiles that transform to them |
| [Fisheries & Simulation Outputs](#fisheries--simulation-outputs) | 3 | Harvest scenario and Digital Twin simulation outputs |
| [Fuzzy Cognitive Maps](#fuzzy-cognitive-maps) | 7 | Exchanging, solving and sequencing fuzzy cognitive maps |
| [Marine Protection Linked Data](#marine-protection-linked-data) | 4 | Example of a dataset described with an ontology and semantic uplift |

### Core Models & Shared Components

- [Property relationship ontology](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.ontology)
- [Seadots Properties](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.properties)
- [Property relationship](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.property-relationship)
- [Equation property relationship](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.equation-property-relationship)
- [OIM Variables](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.oim-variables)
- [OIM Variable Observation](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.oim-variable-observation)
- [Marine Area of Interest](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.area-of-interest)
- [GeoParquet Header](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.geoparquet-header)

### Data & Workflow Catalogue

- [SeaDOTs Catalog Data](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.catalog-data)
- [SeaDOTs Catalog Data Multidimensional](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.catalog-data-multidim)
- [SeaDOTs Catalog Data Tabular](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.catalog-data-tabular)
- [SeaDOTs Catalog Data Tabular Survey](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.catalog-data-tabular-survey)
- [SeaDOTs Catalog Workflow](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.catalog-workflow)
- [SeaDOTs Catalog Execution](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.catalog-execution)
- [SeaDOTs Catalog Application Package](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.catalog-application-package)
- [ODD Protocol Description Record](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.odd-protocol)

### Reef Effect

- [Reef Effect](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.reef-effect)
- [Reef Effect Process](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.reef-effect-process)
- [Reef Effect Output](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.reef-effect-output)
- [Reef Effect Utsira Execution](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.reef-effect-utsira)
- [Reef Aggregation Index (AF_i)](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.reef-aggregation-index)
- [Colonisation Time Factor (C_t)](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.colonisation-time-factor)
- [Floating-Wind Submerged Infrastructure](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.floating-wind-infrastructure)

### Benthic Observations

- [IMR Benthic Biomass Observations](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.benthic-biomass-observations-imr)
- [IMR Benthic Biomass Density Observation](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.benthic-biomass-density-imr)
- [MAREANO Benthic Biomass Density Observation](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.benthic-biomass-density-mareano)
- [OBIS MAREANO Checklist](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.obis-mareano-checklist)

### Offshore Windfarms

- [Windfarm ontology (designated areas and wind turbines)](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.windfarms.common-windfarm-ontology)
- [Windfarm designated area](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.windfarms.common-windfarm-designated-area)
- [Wind turbine](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.windfarms.common-windfarm-turbine)
- [EMODnet windfarm](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.windfarms.windfarm-designated-area-emodnet)
- [Polish windfarm extension for EMODnet](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.windfarms.emodnet-compliant-windfarm-pl)
- [Polish national offshore windfarm source record](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.windfarms.crowdsourced-designated-area-pl)
- [OpenStreetMap offshore wind source feature collection](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.windfarms.windfarm-openstreetmap)

### Protected Areas

- [EMODnet-compliant protected area (common)](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.emodnet-protected-area)
- [EMODnet-compliant nationally designated area](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.emodnet-protected-area.nationally-designated-area)
- [EMODnet-compliant Regional Sea Convention MPA](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.emodnet-protected-area.rsc-mpa)
- [EMODnet-view collection description](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.emodnet-protected-area.api-collection)
- [HELCOM MPA source profile with EMODnet transform](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.protected-area.source-helcom-mpa)
- [Norwegian protected sites (Naturvernområder) source profile with EMODnet transform](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.protected-area.source-norway-naturvernomrade)
- [Protected-area transform report](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.protected-area.transform-report)

### Fisheries & Simulation Outputs

- [Swedish DT Simulations Output](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.swedish-DT-simulations-output)
- [Harvest time series scenario Scen M3: source GeoJSON](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.harvest-timeseries-scen-m3-source)
- [Harvest time series scenario Scen M3: GeoParquet representation](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.harvest-timeseries-scen-m3-geoparquet)

### Fuzzy Cognitive Maps

These blocks are kept under `_sources/_staging/`, but they are published in the register. `_staging` isn't part of their identifiers.

- [Fuzzy Cognitive Map ontology](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.fcm-ontology)
- [FCM activation and inference scheme](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.fcm-activation-scheme)
- [Fuzzy Cognitive Map](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.fcm)
- [FCM solution](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.fcm-solution)
- [FCM sequence](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.fcm-sequence)
- [FCM time specification](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.fcm-timespec)
- [FCM solver workflow](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.fcm-workflow)

### Marine Protection Linked Data

- [Marine Protections Ontology](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.linkeddata.marine-protection-ontology)
- [Marine Protection Feature](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.linkeddata.marineProtectionFeature)
- [Marine Protection Properties](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.linkeddata.marineProtectionProperties)
- [Marine Protection Dataset Record](https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.linkeddata.marineProtectionRecord)

## Repository layout

| Path | Contents |
|---|---|
| [`_sources/`](_sources) | Block sources. **Make all block changes here.** |
| `build/` | Generated register, annotated schemas, documentation and test reports. Don't edit by hand. |
| [`bblocks-config.yaml`](bblocks-config.yaml) | Register name, identifier prefix (`ogc.hosted.seadots.`), imports and SPARQL endpoints |
| [`docs/`](docs) | Supporting reports and worked material, including the [Baltic SES exercise](docs/baltic-ses-exercise/README.md) and the [Central Baltic herring hindcast](docs/experiment-her-2010-2020/run-report.md) |
| [`app/`](app/README.md) | SeaDOTs Concept Editor, for browsing and editing OIM concepts in the triplestore without writing RDF |
| [`tools/`](tools) | Helper scripts |
| [`data_sources_for_EMODnet_Human_Activities.md`](data_sources_for_EMODnet_Human_Activities.md) | Inventory of demonstrator data sources for EMODnet Human Activities |
| [`emodnet_human_activities_bblock_mapping.md`](emodnet_human_activities_bblock_mapping.md) | Mapping from those sources to blocks (marked in the file as needing updates) |

## Working with the blocks

A block's identifier comes from `ogc.hosted.seadots.` plus its path under `_sources/`, so moving a block normally changes its identifier.

To build and view the register locally, using Docker:

```shell
./build.sh   # process the blocks
./view.sh    # serve the register viewer on http://localhost:9090
```

On GitHub, `validate-pr.yml` checks pull requests without changing anything, and `process-bblocks.yml` regenerates and publishes the register. Ontologies are also pushed to the SPARQL endpoint set in [`bblocks-config.yaml`](bblocks-config.yaml).

### Namespace convention

SeaDOTs namespaces end in `/` rather than `#`, for example `https://w3id.org/ogc/hosted/seadots/windfarm/`. Each term then has its own resolvable IRI, which lets Linked Data viewers look up and display its label and description. Use this form for new ontologies and JSON-LD contexts.

### Authoring references

- [OGC Blocks documentation](https://ogcincubator.github.io/bblocks-docs/)
- [Block structure and configuration](USAGE.md) (the template's guide, kept in this repository)
- [Example register](https://github.com/ogcincubator/bblocks-examples)
