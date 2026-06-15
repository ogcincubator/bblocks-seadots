
# Reef Effect (Schema)

`ogc.hosted.seadots.reef-effect` *v0.2*

OGC API Records profile for describing the executable reef-effect calculation realising a documented model. Points at the code that runs the calculation and binds it to the ODD record, evidence equation, input records, and reef-effect-output records.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Reef Effect

SeaDOTs Catalog Workflow profile for describing one computational experiment that realises a documented model.

A computational experiment is the executable counterpart of an ODD Protocol description: it commits to specific software, specific inputs and a specific output target. This block extends [`catalog-workflow`](../catalog-workflow/) so it carries the generic catalog workflow fields (`type: Workflow`, `applicationCategory`, `version`, `method`, `applicationPackage`, `inputs`, and `outputs`) and then adds the reef-effect-specific `experiment` object. The record points at the executable code (Python script, Jupyter notebook, R script, etc.) that runs the experiment, and at standalone per-class input records (e.g. `area-of-interest`, `floating-wind-infrastructure`, `benthic-biomass-density-mareano`, …) and `reef-effect-output` records by URI so they can be reused across runs.

## What an experiment record carries

At the catalog workflow level:

```
properties:
  type                — Workflow
  applicationCategory — DigitalTwinApplication | Workflow | Transform | Model | Service
  version             — workflow/profile version
  method              — reusable method implemented by the workflow
  applicationPackage  — runnable package, script, notebook, or package description
  inputs[]            — accepted input profile declarations
  outputs[]           — produced output profile declarations
```

The reef-effect extension then carries:

```
experiment:
  kind                — computational | observational | mesocosm | in-situ
  purpose             — research question being addressed
  application         — link to the executable (any language / format that exists and runs)
  modelledBy          — link to the ODD record realised by this experiment
  evidenceEquation    — link to the equation-property-relationship record
  parameters[]        — parameter definitions
  inputs[]            — link[] to per-class input records (NOT inlined)
                          each entry MAY carry an equationBinding symbol
  outputs[]           — link[] to reef-effect-output records (NOT inlined)
  execution           — language, languageVersion, dependencies, entrypoint,
                          scheduling, reproducibility flags
  successCriteria[]   — assertions the run must satisfy to be considered successful
```

## Composition pattern

The experiment record references inputs and outputs **by URI** rather than embedding them. This matches the cross-bblock composition already used by `odd-protocol` (which references `equation-property-relationship` records by URI) and keeps the experiment record stable when the input set is revised.

- Each input is a standalone instance of the matching per-class bblock: [`area-of-interest`](../area-of-interest/), [`floating-wind-infrastructure`](../floating-wind-infrastructure/), [`benthic-biomass-density-mareano`](../benthic-biomass-density-mareano/), [`benthic-biomass-density-imr`](../benthic-biomass-density-imr/), [`reef-aggregation-index`](../reef-aggregation-index/), [`colonisation-time-factor`](../colonisation-time-factor/).
- Each output is a standalone instance of [`reef-effect-output`](../reef-effect-output/).
- The equation is a standalone instance of [`equation-property-relationship`](../equation-property-relationship/).
- The model documentation is a standalone instance of [`odd-protocol`](../odd-protocol/).

## Application

The `application` field MUST point to an executable artefact that **exists and runs**. Acceptable forms:

- A Python script committed to the same repository (the case in the worked example).
- A Jupyter notebook with explicit kernel + dependencies.
- An R script or RMarkdown document with explicit `sessionInfo()` capture.
- Any other self-contained executable for which an `entrypoint` command exists.

Do not link to placeholder workflows that reference containers or tools that have not been built and published. The record should reflect what is actually runnable today, not what is intended in the future.

## Reproducibility

`execution.language` and `execution.languageVersion` identify the runtime; `execution.dependencies` lists the packages and versions; `execution.entrypoint` gives the exact command to invoke from the repository root. `execution.reproducibility.seedPolicy` SHOULD state whether the experiment is deterministic or how randomness is controlled. A PROV-O record (referenced as one of the `outputs`) closes the loop back to the inputs and the modelled equation.

## Examples

### Utsira surroundings reef-biomass experiment
#### json
```json
{
  "id": "https://example.org/norwegian-ses/reef-effect/utsira-reef-biomass-surroundings-v1",
  "type": "Feature",
  "itemType": "record",
  "conformsTo": [
    "https://docs.ogc.org/is/20-004/20-004.html",
    "http://www.w3.org/TR/prov-o/",
    "bblocks://ogc.hosted.seadots.catalog-workflow",
    "bblocks://ogc.hosted.seadots.reef-effect"
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [4.20, 59.10],
      [5.30, 59.10],
      [5.30, 59.70],
      [4.20, 59.70],
      [4.20, 59.10]
    ]]
  },
  "time": {
    "interval": ["2026-05-13", "2028-05-13"],
    "resolution": "P12M"
  },
  "properties": {
    "type": "Workflow",
    "softwareType": "SoftwareSourceCode",
    "title": "Utsira surroundings — reef-biomass experiment",
    "description": "Experiment record for an executable run of the Utsira reef-biomass calculation over the surroundings of Utsira island. Realises the one-submodel ODD demonstrator `utsira_reef_biomass_demonstrator` and the canonical equation record `reef-biomass-equation`. Inputs and outputs are referenced by URI as standalone per-class input records and `reef-effect-output` records. The executable is a self-contained Python reproducibility script (`scripts/utsira_reef_biomass.py`).",
    "applicationCategory": "DigitalTwinApplication",
    "version": "0.2",
    "method": "Evaluate the deterministic reef-biomass equation B_reef = sum_i (A_sub . D_pre,i . AF_i . C_t) over the Utsira surroundings area using linked per-class input records and produce reef-effect-output records.",
    "activity": "https://w3id.org/ogc/hosted/seadots/catalog/activity/reef-effect-calculation",
    "softwareVersion": "0.2",
    "programmingLanguage": "Python",
    "applicationPackage": "../scripts/utsira_reef_biomass.py",
    "inputs": [
      {
        "profileId": "ogc.hosted.seadots.area-of-interest",
        "required": true,
        "role": "area-of-interest",
        "description": "Polygon delimiting the study area; defaults to the surroundings of Utsira island."
      },
      {
        "profileId": "ogc.hosted.seadots.floating-wind-infrastructure",
        "required": true,
        "role": "submerged-infrastructure",
        "description": "Floating wind infrastructure layout bound to A_{sub}."
      },
      {
        "profileId": "ogc.hosted.seadots.benthic-biomass-density-mareano",
        "required": true,
        "role": "primary-benthic-biomass-density",
        "description": "Primary MAREANO biomass-density baseline bound to D_{pre,i}."
      },
      {
        "profileId": "ogc.hosted.seadots.benthic-biomass-density-imr",
        "required": false,
        "role": "fallback-benthic-biomass-density",
        "description": "IMR fallback biomass-density baseline bound to D_{pre,i}."
      },
      {
        "profileId": "ogc.hosted.seadots.reef-aggregation-index",
        "required": true,
        "role": "reef-aggregation-index",
        "description": "Taxon-specific aggregation factor bound to AF_i."
      },
      {
        "profileId": "ogc.hosted.seadots.colonisation-time-factor",
        "required": true,
        "role": "colonisation-time-factor",
        "description": "Colonisation time factor bound to C_t."
      }
    ],
    "outputs": [
      {
        "profileId": "ogc.hosted.seadots.reef-effect-output",
        "required": true,
        "role": "reef-biomass-result",
        "description": "Structured reef-associated biomass output."
      },
      {
        "profileId": "ogc.hosted.seadots.catalog-output",
        "required": false,
        "role": "stac-catalog-output",
        "description": "Optional catalog/STAC representation for the run output."
      }
    ],
    "created": "2026-05-18",
    "updated": "2026-05-19",
    "language": { "code": "en" },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "contacts": [
      {
        "name": "Utsira biomass upscaler v1",
        "roles": ["author"],
        "organization": "SINTEF Ocean (SeaDOTs)"
      }
    ],
    "themes": [
      {
        "concepts": [
          { "id": "reef-effect",              "label": "Floating-wind reef effect" },
          { "id": "computational-experiment", "label": "Computational experiment" }
        ],
        "scheme": "https://id3.seadots.eu/themes"
      }
    ],
    "keywords": ["reef-effect", "Utsira", "surroundings", "reef biomass", "SeaDOTs", "Python"],
    "formats": [
      { "mediaType": "text/x-python" },
      { "mediaType": "application/geo+json" },
      { "mediaType": "application/json" }
    ],
    "conformsTo": [
      "https://ogcincubator.github.io/geodcat-ogcapi-records/"
    ],

    "experiment": {
      "kind": "computational",
      "purpose": "Evaluate the reef-biomass equation B_reef = sum_i (A_sub . D_pre,i . AF_i . C_t) for the surroundings of Utsira island under the Norwegian SES scenario. Inputs are the six per-class input records cited below; outputs are the two reef-effect-output records cited below. The PROV-O provenance record is embedded in the structured result output.",

      "application": {
        "href": "bblocks://ogc.hosted.seadots.reef-effect/scripts/utsira_reef_biomass.py",
        "type": "text/x-python",
        "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#application",
        "title": "Utsira reef-biomass calculator (Python script)"
      },

      "modelledBy": {
        "href": "https://w3id.org/ogc/hosted/seadots/odd-protocol/examples/utsira_reef_biomass_demonstrator",
        "rel": "describedby",
        "title": "ODD record for the reef-biomass demonstrator"
      },

      "evidenceEquation": {
        "href": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
        "rel": "cite-as",
        "title": "Reef-biomass equation — symbol table, bindings, provenance"
      },

      "parameters": [
        {
          "name": "aoi",
          "title": "Area of interest",
          "description": "Polygon delimiting the study area. Defaults to the surroundings of Utsira island.",
          "parameterSchema": { "format": "application/geo+json" },
          "vocabularyTerm": "http://www.opengis.net/def/property/OGC/0/area-of-interest"
        },
        {
          "name": "taxon_groups",
          "title": "TaxonGroup index values",
          "description": "Scientific names iterated by index i.",
          "parameterSchema": { "type": "array", "items": { "type": "string" } },
          "vocabularyTerm": "http://rs.tdwg.org/dwc/terms/scientificName"
        },
        {
          "name": "scenario_t0",
          "title": "Scenario start date",
          "parameterSchema": { "type": "string", "format": "date" }
        },
        {
          "name": "colonisation_months",
          "title": "Months since installation",
          "parameterSchema": { "type": "integer", "minimum": 0 }
        }
      ],

      "inputs": [
        {
          "href": "https://example.org/norwegian-ses/area-of-interest/utsira-surroundings",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#input",
          "title": "AOI — surroundings of Utsira island",
          "equationBinding": null
        },
        {
          "href": "https://example.org/norwegian-ses/floating-wind-infrastructure/utsira-nord-60x15mw",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#input",
          "title": "Submerged infrastructure layout — Utsira Nord 60 × 15 MW",
          "equationBinding": "A_{sub}"
        },
        {
          "href": "https://example.org/norwegian-ses/benthic-biomass-density-mareano/norwegian-shelf",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#input",
          "title": "MAREANO benthic biomass density — primary baseline",
          "equationBinding": "D_{pre,i}"
        },
        {
          "href": "https://example.org/norwegian-ses/benthic-biomass-density-imr/ices-iva-fallback",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#input",
          "title": "IMR benthic biomass baseline — fallback",
          "equationBinding": "D_{pre,i}"
        },
        {
          "href": "https://example.org/norwegian-ses/reef-aggregation-index/degraer2020-bindings",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#input",
          "title": "Reef aggregation index bindings",
          "equationBinding": "AF_i"
        },
        {
          "href": "https://example.org/norwegian-ses/colonisation-time-factor/default-sigmoid",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#input",
          "title": "Colonisation time factor",
          "equationBinding": "C_t"
        }
      ],

      "outputs": [
        {
          "href": "https://example.org/norwegian-ses/reef-effect-output/reef-biomass-result",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#output",
          "title": "Reef-associated biomass — structured result"
        },
        {
          "href": "https://example.org/norwegian-ses/reef-effect-output/stac-catalog",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#output",
          "title": "STAC catalog for the run"
        }
      ],

      "execution": {
        "language": "python",
        "languageVersion": ">=3.9",
        "dependencies": [],
        "entrypoint": "python3 _sources/reef-effect/scripts/utsira_reef_biomass.py",
        "scheduling": "single deterministic pass over taxon_groups (ODD processOverview.scheduling)",
        "reproducibility": {
          "seedPolicy": "deterministic — equation is closed-form, no stochastic submodels",
          "provenance": "PROV-O record embedded in the structured result output"
        }
      },

      "successCriteria": [
        "B_reef_total > 0 and finite",
        "Every TaxonGroup has either a MAREANO primary binding or an IMR fallback for every AOI cell; uncovered cells are flagged in PROV",
        "STAC catalog validates against the SeaDOTs EDITO output conventions",
        "PROV-O record resolves the equation record and the ODD record by URI"
      ]
    }
  },
  "links": [
    { "rel": "describedby", "href": "bblocks://ogc.hosted.seadots.reef-effect", "type": "application/schema+json", "title": "Experiment bblock" },
    { "rel": "alternate", "href": "bblocks://ogc.hosted.seadots.reef-effect/scripts/utsira_reef_biomass.py", "type": "text/x-python", "title": "Reproducibility script — runs the worked example end-to-end" },
    { "rel": "related", "href": "https://w3id.org/ogc/hosted/seadots/odd-protocol/examples/utsira_reef_biomass_demonstrator", "type": "application/json", "title": "ODD demonstrator that this experiment realises" },
    { "rel": "cite-as", "href": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation", "type": "application/ld+json", "title": "Reef-biomass equation record" }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/reef-effect/context.jsonld",
  "id": "https://example.org/norwegian-ses/reef-effect/utsira-reef-biomass-surroundings-v1",
  "type": "Feature",
  "itemType": "record",
  "conformsTo": [
    "https://docs.ogc.org/is/20-004/20-004.html",
    "http://www.w3.org/TR/prov-o/",
    "bblocks://ogc.hosted.seadots.catalog-workflow",
    "bblocks://ogc.hosted.seadots.reef-effect"
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          4.2,
          59.1
        ],
        [
          5.3,
          59.1
        ],
        [
          5.3,
          59.7
        ],
        [
          4.2,
          59.7
        ],
        [
          4.2,
          59.1
        ]
      ]
    ]
  },
  "time": {
    "interval": [
      "2026-05-13",
      "2028-05-13"
    ],
    "resolution": "P12M"
  },
  "properties": {
    "type": "Workflow",
    "softwareType": "SoftwareSourceCode",
    "title": "Utsira surroundings \u2014 reef-biomass experiment",
    "description": "Experiment record for an executable run of the Utsira reef-biomass calculation over the surroundings of Utsira island. Realises the one-submodel ODD demonstrator `utsira_reef_biomass_demonstrator` and the canonical equation record `reef-biomass-equation`. Inputs and outputs are referenced by URI as standalone per-class input records and `reef-effect-output` records. The executable is a self-contained Python reproducibility script (`scripts/utsira_reef_biomass.py`).",
    "applicationCategory": "DigitalTwinApplication",
    "version": "0.2",
    "method": "Evaluate the deterministic reef-biomass equation B_reef = sum_i (A_sub . D_pre,i . AF_i . C_t) over the Utsira surroundings area using linked per-class input records and produce reef-effect-output records.",
    "activity": "https://w3id.org/ogc/hosted/seadots/catalog/activity/reef-effect-calculation",
    "softwareVersion": "0.2",
    "programmingLanguage": "Python",
    "applicationPackage": "../scripts/utsira_reef_biomass.py",
    "inputs": [
      {
        "profileId": "ogc.hosted.seadots.area-of-interest",
        "required": true,
        "role": "area-of-interest",
        "description": "Polygon delimiting the study area; defaults to the surroundings of Utsira island."
      },
      {
        "profileId": "ogc.hosted.seadots.floating-wind-infrastructure",
        "required": true,
        "role": "submerged-infrastructure",
        "description": "Floating wind infrastructure layout bound to A_{sub}."
      },
      {
        "profileId": "ogc.hosted.seadots.benthic-biomass-density-mareano",
        "required": true,
        "role": "primary-benthic-biomass-density",
        "description": "Primary MAREANO biomass-density baseline bound to D_{pre,i}."
      },
      {
        "profileId": "ogc.hosted.seadots.benthic-biomass-density-imr",
        "required": false,
        "role": "fallback-benthic-biomass-density",
        "description": "IMR fallback biomass-density baseline bound to D_{pre,i}."
      },
      {
        "profileId": "ogc.hosted.seadots.reef-aggregation-index",
        "required": true,
        "role": "reef-aggregation-index",
        "description": "Taxon-specific aggregation factor bound to AF_i."
      },
      {
        "profileId": "ogc.hosted.seadots.colonisation-time-factor",
        "required": true,
        "role": "colonisation-time-factor",
        "description": "Colonisation time factor bound to C_t."
      }
    ],
    "outputs": [
      {
        "profileId": "ogc.hosted.seadots.reef-effect-output",
        "required": true,
        "role": "reef-biomass-result",
        "description": "Structured reef-associated biomass output."
      },
      {
        "profileId": "ogc.hosted.seadots.catalog-output",
        "required": false,
        "role": "stac-catalog-output",
        "description": "Optional catalog/STAC representation for the run output."
      }
    ],
    "created": "2026-05-18",
    "updated": "2026-05-19",
    "language": {
      "code": "en"
    },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "contacts": [
      {
        "name": "Utsira biomass upscaler v1",
        "roles": [
          "author"
        ],
        "organization": "SINTEF Ocean (SeaDOTs)"
      }
    ],
    "themes": [
      {
        "concepts": [
          {
            "id": "reef-effect",
            "label": "Floating-wind reef effect"
          },
          {
            "id": "computational-experiment",
            "label": "Computational experiment"
          }
        ],
        "scheme": "https://id3.seadots.eu/themes"
      }
    ],
    "keywords": [
      "reef-effect",
      "Utsira",
      "surroundings",
      "reef biomass",
      "SeaDOTs",
      "Python"
    ],
    "formats": [
      {
        "mediaType": "text/x-python"
      },
      {
        "mediaType": "application/geo+json"
      },
      {
        "mediaType": "application/json"
      }
    ],
    "conformsTo": [
      "https://ogcincubator.github.io/geodcat-ogcapi-records/"
    ],
    "experiment": {
      "kind": "computational",
      "purpose": "Evaluate the reef-biomass equation B_reef = sum_i (A_sub . D_pre,i . AF_i . C_t) for the surroundings of Utsira island under the Norwegian SES scenario. Inputs are the six per-class input records cited below; outputs are the two reef-effect-output records cited below. The PROV-O provenance record is embedded in the structured result output.",
      "application": {
        "href": "bblocks://ogc.hosted.seadots.reef-effect/scripts/utsira_reef_biomass.py",
        "type": "text/x-python",
        "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#application",
        "title": "Utsira reef-biomass calculator (Python script)"
      },
      "modelledBy": {
        "href": "https://w3id.org/ogc/hosted/seadots/odd-protocol/examples/utsira_reef_biomass_demonstrator",
        "rel": "describedby",
        "title": "ODD record for the reef-biomass demonstrator"
      },
      "evidenceEquation": {
        "href": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
        "rel": "cite-as",
        "title": "Reef-biomass equation \u2014 symbol table, bindings, provenance"
      },
      "parameters": [
        {
          "name": "aoi",
          "title": "Area of interest",
          "description": "Polygon delimiting the study area. Defaults to the surroundings of Utsira island.",
          "parameterSchema": {
            "format": "application/geo+json"
          },
          "vocabularyTerm": "http://www.opengis.net/def/property/OGC/0/area-of-interest"
        },
        {
          "name": "taxon_groups",
          "title": "TaxonGroup index values",
          "description": "Scientific names iterated by index i.",
          "parameterSchema": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "vocabularyTerm": "http://rs.tdwg.org/dwc/terms/scientificName"
        },
        {
          "name": "scenario_t0",
          "title": "Scenario start date",
          "parameterSchema": {
            "type": "string",
            "format": "date"
          }
        },
        {
          "name": "colonisation_months",
          "title": "Months since installation",
          "parameterSchema": {
            "type": "integer",
            "minimum": 0
          }
        }
      ],
      "inputs": [
        {
          "href": "https://example.org/norwegian-ses/area-of-interest/utsira-surroundings",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#input",
          "title": "AOI \u2014 surroundings of Utsira island",
          "equationBinding": null
        },
        {
          "href": "https://example.org/norwegian-ses/floating-wind-infrastructure/utsira-nord-60x15mw",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#input",
          "title": "Submerged infrastructure layout \u2014 Utsira Nord 60 \u00d7 15 MW",
          "equationBinding": "A_{sub}"
        },
        {
          "href": "https://example.org/norwegian-ses/benthic-biomass-density-mareano/norwegian-shelf",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#input",
          "title": "MAREANO benthic biomass density \u2014 primary baseline",
          "equationBinding": "D_{pre,i}"
        },
        {
          "href": "https://example.org/norwegian-ses/benthic-biomass-density-imr/ices-iva-fallback",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#input",
          "title": "IMR benthic biomass baseline \u2014 fallback",
          "equationBinding": "D_{pre,i}"
        },
        {
          "href": "https://example.org/norwegian-ses/reef-aggregation-index/degraer2020-bindings",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#input",
          "title": "Reef aggregation index bindings",
          "equationBinding": "AF_i"
        },
        {
          "href": "https://example.org/norwegian-ses/colonisation-time-factor/default-sigmoid",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#input",
          "title": "Colonisation time factor",
          "equationBinding": "C_t"
        }
      ],
      "outputs": [
        {
          "href": "https://example.org/norwegian-ses/reef-effect-output/reef-biomass-result",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#output",
          "title": "Reef-associated biomass \u2014 structured result"
        },
        {
          "href": "https://example.org/norwegian-ses/reef-effect-output/stac-catalog",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/reef-effect#output",
          "title": "STAC catalog for the run"
        }
      ],
      "execution": {
        "language": "python",
        "languageVersion": ">=3.9",
        "dependencies": [],
        "entrypoint": "python3 _sources/reef-effect/scripts/utsira_reef_biomass.py",
        "scheduling": "single deterministic pass over taxon_groups (ODD processOverview.scheduling)",
        "reproducibility": {
          "seedPolicy": "deterministic \u2014 equation is closed-form, no stochastic submodels",
          "provenance": "PROV-O record embedded in the structured result output"
        }
      },
      "successCriteria": [
        "B_reef_total > 0 and finite",
        "Every TaxonGroup has either a MAREANO primary binding or an IMR fallback for every AOI cell; uncovered cells are flagged in PROV",
        "STAC catalog validates against the SeaDOTs EDITO output conventions",
        "PROV-O record resolves the equation record and the ODD record by URI"
      ]
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.reef-effect",
      "type": "application/schema+json",
      "title": "Experiment bblock"
    },
    {
      "rel": "alternate",
      "href": "bblocks://ogc.hosted.seadots.reef-effect/scripts/utsira_reef_biomass.py",
      "type": "text/x-python",
      "title": "Reproducibility script \u2014 runs the worked example end-to-end"
    },
    {
      "rel": "related",
      "href": "https://w3id.org/ogc/hosted/seadots/odd-protocol/examples/utsira_reef_biomass_demonstrator",
      "type": "application/json",
      "title": "ODD demonstrator that this experiment realises"
    },
    {
      "rel": "cite-as",
      "href": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
      "type": "application/ld+json",
      "title": "Reef-biomass equation record"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix schema: <https://schema.org/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .
@prefix seadotsReef: <https://w3id.org/ogc/hosted/seadots/reef-effect#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/norwegian-ses/reef-effect/utsira-reef-biomass-surroundings-v1> a prov:Plan,
        geojson:Feature ;
    dcterms:conformsTo <bblocks://ogc.hosted.seadots.catalog-workflow>,
        <bblocks://ogc.hosted.seadots.reef-effect>,
        <http://www.w3.org/TR/prov-o/>,
        <https://docs.ogc.org/is/20-004/20-004.html>,
        <https://ogcincubator.github.io/geodcat-ogcapi-records/> ;
    dcterms:created "2026-05-18" ;
    dcterms:description "Experiment record for an executable run of the Utsira reef-biomass calculation over the surroundings of Utsira island. Realises the one-submodel ODD demonstrator `utsira_reef_biomass_demonstrator` and the canonical equation record `reef-biomass-equation`. Inputs and outputs are referenced by URI as standalone per-class input records and `reef-effect-output` records. The executable is a self-contained Python reproducibility script (`scripts/utsira_reef_biomass.py`)." ;
    dcterms:hasVersion "0.2" ;
    dcterms:license "https://creativecommons.org/licenses/by/4.0/" ;
    dcterms:method "Evaluate the deterministic reef-biomass equation B_reef = sum_i (A_sub . D_pre,i . AF_i . C_t) over the Utsira surroundings area using linked per-class input records and produce reef-effect-output records." ;
    dcterms:modified "2026-05-19" ;
    dcterms:temporal [ dcterms:temporal "2026-05-13",
                "2028-05-13" ;
            dcat:temporalResolution "P12M" ] ;
    dcterms:title "Utsira surroundings — reef-biomass experiment" ;
    dcterms:type "SoftwareSourceCode" ;
    rdfs:seeAlso [ rdfs:label "Reproducibility script — runs the worked example end-to-end" ;
            dcterms:type "text/x-python" ;
            ns1:relation <http://www.iana.org/assignments/relation/alternate> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.reef-effect/scripts/utsira_reef_biomass.py> ],
        [ rdfs:label "Experiment bblock" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.reef-effect> ],
        [ rdfs:label "Reef-biomass equation record" ;
            dcterms:type "application/ld+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation> ],
        [ rdfs:label "ODD demonstrator that this experiment realises" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://w3id.org/ogc/hosted/seadots/odd-protocol/examples/utsira_reef_biomass_demonstrator> ] ;
    dcat:contactPoint [ rdfs:label "Utsira biomass upscaler v1" ;
            dcat:hadRole "author" ;
            schema:affiliation "SINTEF Ocean (SeaDOTs)" ] ;
    dcat:keyword "Python",
        "SeaDOTs",
        "Utsira",
        "reef biomass",
        "reef-effect",
        "surroundings" ;
    prov:activity <https://w3id.org/ogc/hosted/seadots/catalog/activity/reef-effect-calculation> ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 4.2e+00 5.91e+01 ) ( 5.3e+00 5.91e+01 ) ( 5.3e+00 5.97e+01 ) ( 4.2e+00 5.97e+01 ) ( 4.2e+00 5.91e+01 ) ) ) ] ;
    schema:applicationCategory "DigitalTwinApplication" ;
    schema:programmingLanguage "Python" ;
    schema:softwareVersion "0.2" ;
    seadots:applicationPackage <file:///github/scripts/utsira_reef_biomass.py> ;
    seadots:inputs [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.benthic-biomass-density-mareano> ;
            dcterms:description "Primary MAREANO biomass-density baseline bound to D_{pre,i}." ;
            seadots:required true ;
            seadots:role "primary-benthic-biomass-density" ],
        [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.benthic-biomass-density-imr> ;
            dcterms:description "IMR fallback biomass-density baseline bound to D_{pre,i}." ;
            seadots:required false ;
            seadots:role "fallback-benthic-biomass-density" ],
        [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.reef-aggregation-index> ;
            dcterms:description "Taxon-specific aggregation factor bound to AF_i." ;
            seadots:required true ;
            seadots:role "reef-aggregation-index" ],
        [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.floating-wind-infrastructure> ;
            dcterms:description "Floating wind infrastructure layout bound to A_{sub}." ;
            seadots:required true ;
            seadots:role "submerged-infrastructure" ],
        [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.area-of-interest> ;
            dcterms:description "Polygon delimiting the study area; defaults to the surroundings of Utsira island." ;
            seadots:required true ;
            seadots:role "area-of-interest" ],
        [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.colonisation-time-factor> ;
            dcterms:description "Colonisation time factor bound to C_t." ;
            seadots:required true ;
            seadots:role "colonisation-time-factor" ] ;
    seadots:itemType "record" ;
    seadots:outputs [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.reef-effect-output> ;
            dcterms:description "Structured reef-associated biomass output." ;
            seadots:required true ;
            seadots:role "reef-biomass-result" ],
        [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.catalog-output> ;
            dcterms:description "Optional catalog/STAC representation for the run output." ;
            seadots:required false ;
            seadots:role "stac-catalog-output" ] ;
    seadotsReef:experiment [ dcterms:purpose "Evaluate the reef-biomass equation B_reef = sum_i (A_sub . D_pre,i . AF_i . C_t) for the surroundings of Utsira island under the Norwegian SES scenario. Inputs are the six per-class input records cited below; outputs are the two reef-effect-output records cited below. The PROV-O provenance record is embedded in the structured result output." ;
            seadotsReef:application [ a <https://w3id.org/ogc/hosted/seadots/catalog#text/x-python> ;
                    dcterms:title "Utsira reef-biomass calculator (Python script)" ;
                    oa:hasTarget <bblocks://ogc.hosted.seadots.reef-effect/scripts/utsira_reef_biomass.py> ;
                    seadots:rel "https://w3id.org/ogc/hosted/seadots/reef-effect#application" ] ;
            seadotsReef:evidenceEquation [ dcterms:title "Reef-biomass equation — symbol table, bindings, provenance" ;
                    oa:hasTarget <https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation> ;
                    seadots:rel "cite-as" ] ;
            seadotsReef:execution [ dcterms:language "python" ;
                    seadotsReef:entrypoint "python3 _sources/reef-effect/scripts/utsira_reef_biomass.py" ;
                    seadotsReef:languageVersion ">=3.9" ;
                    seadotsReef:reproducibility [ prov:wasGeneratedBy "PROV-O record embedded in the structured result output" ;
                            seadotsReef:seedPolicy "deterministic — equation is closed-form, no stochastic submodels" ] ;
                    seadotsReef:scheduling "single deterministic pass over taxon_groups (ODD processOverview.scheduling)" ] ;
            seadotsReef:input [ a <https://w3id.org/ogc/hosted/seadots/catalog#application/json> ;
                    dcterms:title "Reef aggregation index bindings" ;
                    oa:hasTarget <https://example.org/norwegian-ses/reef-aggregation-index/degraer2020-bindings> ;
                    seadots:rel "https://w3id.org/ogc/hosted/seadots/reef-effect#input" ;
                    seadotsReef:equationBinding "AF_i" ],
                [ a <https://w3id.org/ogc/hosted/seadots/catalog#application/json> ;
                    dcterms:title "AOI — surroundings of Utsira island" ;
                    oa:hasTarget <https://example.org/norwegian-ses/area-of-interest/utsira-surroundings> ;
                    seadots:rel "https://w3id.org/ogc/hosted/seadots/reef-effect#input" ],
                [ a <https://w3id.org/ogc/hosted/seadots/catalog#application/json> ;
                    dcterms:title "IMR benthic biomass baseline — fallback" ;
                    oa:hasTarget <https://example.org/norwegian-ses/benthic-biomass-density-imr/ices-iva-fallback> ;
                    seadots:rel "https://w3id.org/ogc/hosted/seadots/reef-effect#input" ;
                    seadotsReef:equationBinding "D_{pre,i}" ],
                [ a <https://w3id.org/ogc/hosted/seadots/catalog#application/json> ;
                    dcterms:title "Colonisation time factor" ;
                    oa:hasTarget <https://example.org/norwegian-ses/colonisation-time-factor/default-sigmoid> ;
                    seadots:rel "https://w3id.org/ogc/hosted/seadots/reef-effect#input" ;
                    seadotsReef:equationBinding "C_t" ],
                [ a <https://w3id.org/ogc/hosted/seadots/catalog#application/json> ;
                    dcterms:title "MAREANO benthic biomass density — primary baseline" ;
                    oa:hasTarget <https://example.org/norwegian-ses/benthic-biomass-density-mareano/norwegian-shelf> ;
                    seadots:rel "https://w3id.org/ogc/hosted/seadots/reef-effect#input" ;
                    seadotsReef:equationBinding "D_{pre,i}" ],
                [ a <https://w3id.org/ogc/hosted/seadots/catalog#application/json> ;
                    dcterms:title "Submerged infrastructure layout — Utsira Nord 60 × 15 MW" ;
                    oa:hasTarget <https://example.org/norwegian-ses/floating-wind-infrastructure/utsira-nord-60x15mw> ;
                    seadots:rel "https://w3id.org/ogc/hosted/seadots/reef-effect#input" ;
                    seadotsReef:equationBinding "A_{sub}" ] ;
            seadotsReef:kind "computational" ;
            seadotsReef:modelledBy [ dcterms:title "ODD record for the reef-biomass demonstrator" ;
                    oa:hasTarget <https://w3id.org/ogc/hosted/seadots/odd-protocol/examples/utsira_reef_biomass_demonstrator> ;
                    seadots:rel "describedby" ] ;
            seadotsReef:output [ a <https://w3id.org/ogc/hosted/seadots/catalog#application/json> ;
                    dcterms:title "Reef-associated biomass — structured result" ;
                    oa:hasTarget <https://example.org/norwegian-ses/reef-effect-output/reef-biomass-result> ;
                    seadots:rel "https://w3id.org/ogc/hosted/seadots/reef-effect#output" ],
                [ a <https://w3id.org/ogc/hosted/seadots/catalog#application/json> ;
                    dcterms:title "STAC catalog for the run" ;
                    oa:hasTarget <https://example.org/norwegian-ses/reef-effect-output/stac-catalog> ;
                    seadots:rel "https://w3id.org/ogc/hosted/seadots/reef-effect#output" ] ;
            seadotsReef:parameter [ rdfs:label "scenario_t0" ;
                    dcterms:title "Scenario start date" ;
                    seadotsReef:parameterSchema [ a seadots:string ;
                            dcterms:format "date" ] ],
                [ rdfs:label "colonisation_months" ;
                    dcterms:title "Months since installation" ;
                    seadotsReef:parameterSchema [ a seadots:integer ;
                            seadots:minimum 0 ] ],
                [ rdfs:label "taxon_groups" ;
                    dcterms:description "Scientific names iterated by index i." ;
                    dcterms:title "TaxonGroup index values" ;
                    skos:exactMatch <http://rs.tdwg.org/dwc/terms/scientificName> ;
                    seadotsReef:parameterSchema [ a seadots:array ;
                            seadots:items [ a seadots:string ] ] ],
                [ rdfs:label "aoi" ;
                    dcterms:description "Polygon delimiting the study area. Defaults to the surroundings of Utsira island." ;
                    dcterms:title "Area of interest" ;
                    skos:exactMatch <http://www.opengis.net/def/property/OGC/0/area-of-interest> ;
                    seadotsReef:parameterSchema [ dcterms:format "application/geo+json" ] ] ;
            seadotsReef:successCriterion "B_reef_total > 0 and finite",
                "Every TaxonGroup has either a MAREANO primary binding or an IMR fallback for every AOI cell; uncovered cells are flagged in PROV",
                "PROV-O record resolves the equation record and the ODD record by URI",
                "STAC catalog validates against the SeaDOTs EDITO output conventions" ] ;
    rec:format [ dcterms:format "text/x-python" ],
        [ dcterms:format "application/json" ],
        [ dcterms:format "application/geo+json" ] ;
    rec:language [ rec:languageCode "en" ] ;
    rec:themes [ rec:concept [ skos:prefLabel "Floating-wind reef effect" ;
                    rec:conceptID "reef-effect"^^xsd:string ],
                [ skos:prefLabel "Computational experiment" ;
                    rec:conceptID "computational-experiment"^^xsd:string ] ;
            rec:scheme "https://id3.seadots.eu/themes" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Reef Effect
description: 'SeaDOTs Catalog Workflow profile for a reef-effect computational experiment
  realising a documented model. Extends the generic catalog workflow with an `experiment`
  sub-object that points to the executable code (`application`) that runs the experiment,
  the documented model (`modelledBy`), the evidence equation (`evidenceEquation`),
  and standalone per-class input and `reef-effect-output` records referenced by URI.

  '
allOf:
- $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-workflow/schema.yaml
$defs:
  Link:
    type: object
    required:
    - href
    properties:
      href:
        type: string
        format: uri
        x-jsonld-type: '@id'
        x-jsonld-id: http://www.w3.org/ns/oa#hasTarget
      rel:
        type: string
      type:
        type: string
        x-jsonld-id: '@type'
      title:
        type: string
        x-jsonld-container: '@set'
        x-jsonld-id: http://purl.org/dc/terms/title
  InputBinding:
    description: 'Reference to a per-class input record (`href`) plus the wiring that
      ties it to this experiment. The referenced record is reusable and carries no
      wiring of its own.

      '
    type: object
    required:
    - href
    properties:
      href:
        type: string
        format: uri
        description: URI of the per-class input record being consumed.
        x-jsonld-type: '@id'
        x-jsonld-id: http://www.w3.org/ns/oa#hasTarget
      rel:
        type: string
      type:
        type: string
        x-jsonld-id: '@type'
      title:
        type: string
        x-jsonld-container: '@set'
        x-jsonld-id: http://purl.org/dc/terms/title
      equationBinding:
        type:
        - string
        - 'null'
        description: 'Symbol from the linked equation-property-relationship record
          that this input parameterises in this experiment (e.g. `A_{sub}`, `D_{pre,i}`,
          `AF_i`, `C_t`). Omit or set to `null` when the input is not bound to an
          equation symbol (e.g. the AOI).

          '
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#equationBinding
properties:
  properties:
    type: object
    required:
    - experiment
    properties:
      softwareType:
        type: string
        description: 'More specific software/catalog type retained from the specialised
          reef-effect workflow record, e.g. schema.org SoftwareSourceCode.

          '
        x-jsonld-id: http://purl.org/dc/terms/type
      experiment:
        type: object
        required:
        - kind
        - application
        properties:
          kind:
            type: string
            enum:
            - computational
            - observational
            - mesocosm
            - in-situ
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#kind
          purpose:
            type: string
            x-jsonld-id: http://purl.org/dc/terms/purpose
          application:
            $ref: '#/$defs/Link'
            description: 'Link to the executable code that runs this experiment. Any
              language or format that exists and runs (Python script, Jupyter notebook,
              R script, etc.). The `type` field SHOULD carry the media type (e.g.
              `text/x-python`).

              '
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#application
            x-jsonld-type: '@id'
          modelledBy:
            $ref: '#/$defs/Link'
            description: Link to the model documentation (e.g. an ODD record) this
              experiment realises.
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#modelledBy
            x-jsonld-type: '@id'
          evidenceEquation:
            $ref: '#/$defs/Link'
            description: Link to an `equation-property-relationship` record carrying
              the symbol table.
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#evidenceEquation
            x-jsonld-type: '@id'
          parameters:
            type: array
            items:
              type: object
              required:
              - name
              properties:
                name:
                  type: string
                  x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#label
                title:
                  type: string
                  x-jsonld-container: '@set'
                  x-jsonld-id: http://purl.org/dc/terms/title
                description:
                  type: string
                  x-jsonld-container: '@set'
                  x-jsonld-id: http://purl.org/dc/terms/description
                parameterSchema:
                  type: object
                  description: Inline JSON Schema fragment for the parameter value.
                  x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#parameterSchema
                vocabularyTerm:
                  type: string
                  format: uri
                  x-jsonld-id: http://www.w3.org/2004/02/skos/core#exactMatch
                  x-jsonld-type: '@id'
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#parameter
            x-jsonld-container: '@set'
          inputs:
            type: array
            description: 'References to per-class input records. Each entry MAY carry
              an `equationBinding` symbol. MUST NOT inline the input record itself.

              '
            items:
              $ref: '#/$defs/InputBinding'
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#input
            x-jsonld-container: '@set'
          outputs:
            type: array
            description: References to `reef-effect-output` records. MUST NOT be inlined.
            items:
              $ref: '#/$defs/Link'
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#output
            x-jsonld-container: '@set'
            x-jsonld-type: '@id'
          execution:
            type: object
            properties:
              language:
                type: string
                description: 'Language or runtime the application is written in (e.g.
                  `python`, `r`, `jupyter`, `bash`).

                  '
                x-jsonld-id: http://purl.org/dc/terms/language
              languageVersion:
                type: string
                description: Minimum interpreter / runtime version.
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#languageVersion
              dependencies:
                type: array
                description: Runtime dependencies (e.g. PyPI packages with version
                  specs).
                items:
                  type: string
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#dependency
                x-jsonld-container: '@set'
              entrypoint:
                type: string
                description: 'Command line to invoke the application from the repository
                  root (e.g. `python3 _sources/reef-effect/scripts/foo.py`).

                  '
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#entrypoint
              scheduling:
                type: string
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#scheduling
              reproducibility:
                type: object
                properties:
                  seedPolicy:
                    type: string
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#seedPolicy
                  provenance:
                    type: string
                    x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#reproducibility
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#execution
          successCriteria:
            type: array
            items:
              type: string
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#successCriterion
            x-jsonld-container: '@set'
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-effect#experiment
    x-jsonld-id: '@nest'
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
  FeatureCollection: https://purl.org/geojson/vocab#FeatureCollection
  GeometryCollection: https://purl.org/geojson/vocab#GeometryCollection
  LineString: https://purl.org/geojson/vocab#LineString
  MultiLineString: https://purl.org/geojson/vocab#MultiLineString
  MultiPoint: https://purl.org/geojson/vocab#MultiPoint
  MultiPolygon: https://purl.org/geojson/vocab#MultiPolygon
  Point: https://purl.org/geojson/vocab#Point
  Polygon: https://purl.org/geojson/vocab#Polygon
  features:
    x-jsonld-container: '@set'
    x-jsonld-id: https://purl.org/geojson/vocab#features
  id: '@id'
  geometry:
    x-jsonld-context:
      coordinates:
        '@container': '@list'
        '@id': https://purl.org/geojson/vocab#coordinates
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
  bbox:
    x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#bbox
  links:
    x-jsonld-context:
      rel:
        '@context':
          '@base': http://www.iana.org/assignments/relation/
        '@id': http://www.iana.org/assignments/relation
        '@type': '@id'
      type: http://purl.org/dc/terms/type
      hreflang: http://purl.org/dc/terms/language
      title: http://www.w3.org/2000/01/rdf-schema#label
      length: http://purl.org/dc/terms/extent
      href:
        '@type': '@id'
        '@id': http://www.w3.org/ns/oa#hasTarget
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
  conformsTo:
    x-jsonld-container: '@set'
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
  time: http://purl.org/dc/terms/temporal
  linkTemplates:
    x-jsonld-context:
      rel:
        '@context':
          '@base': http://www.iana.org/assignments/relation/
        '@id': http://www.iana.org/assignments/relation
        '@type': '@id'
      type: http://purl.org/dc/terms/format
      hreflang: http://purl.org/dc/terms/language
      title: http://www.w3.org/2000/01/rdf-schema#label
      length: http://purl.org/dc/terms/extent
      uriTemplate:
        '@type': http://www.w3.org/2001/XMLSchema#string
        '@id': https://www.opengis.net/def/ogc-api/records/uriTemplate
      varBase: https://www.opengis.net/def/ogc-api/records/varBase
      variables:
        '@id': https://www.opengis.net/def/ogc-api/records/hasVariable
        '@container': '@index'
        '@index': http://purl.org/dc/terms/identifier
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/hasLinkTemplate
  created: http://purl.org/dc/terms/created
  updated: http://purl.org/dc/terms/modified
  keywords:
    x-jsonld-container: '@set'
    x-jsonld-id: http://www.w3.org/ns/dcat#keyword
  languages:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/languages
    x-jsonld-context:
      code: https://www.opengis.net/def/ogc-api/records/languageCode
      name: http://www.w3.org/2004/02/skos/core#prefLabel
  resourceLanguages:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/resourceLanguages
    x-jsonld-context:
      code: https://www.opengis.net/def/ogc-api/records/languageCode
      name: http://www.w3.org/2004/02/skos/core#prefLabel
  externalIds:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/scopedIdentifier
    x-jsonld-context:
      scheme: https://www.opengis.net/def/ogc-api/records/scheme
      value: https://www.opengis.net/def/ogc-api/records/id
  themes:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/themes
    x-jsonld-context:
      concepts:
        '@id': https://w3id.org/ogc/stac/themes/concepts
        '@context':
          id:
            '@type': http://www.w3.org/2001/XMLSchema#string
            '@id': https://w3id.org/ogc/stac/themes/id
          url:
            '@type': '@id'
            '@id': '@id'
        '@container': '@set'
      scheme: https://w3id.org/ogc/stac/themes/scheme
  formats:
    x-jsonld-id: http://purl.org/dc/terms/format
    x-jsonld-context:
      name: https://www.opengis.net/def/ogc-api/records/name
      mediaType: https://www.opengis.net/def/ogc-api/records/mediaType
    x-jsonld-container: '@set'
    x-jsonld-type: '@id'
  contacts:
    x-jsonld-container: '@set'
    x-jsonld-id: http://www.w3.org/ns/dcat#contactPoint
    x-jsonld-type: '@id'
  license: http://www.w3.org/ns/dcat#license
  accessrights: http://purl.org/dc/terms/accessRights
  variables:
    x-jsonld-container: '@id'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/hasVariable
    x-jsonld-context:
      '@base': http://example.com/variables/
      '@vocab': https://www.opengis.net/def/ogc-api/records/
  rights: http://www.w3.org/ns/dcat#rights
  wasInfluencedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasInfluencedBy
    x-jsonld-type: '@id'
  qualifiedInfluence:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInfluence
    x-jsonld-type: '@id'
  hadMember:
    x-jsonld-id: http://www.w3.org/ns/prov#hadMember
    x-jsonld-type: '@id'
  provType: '@type'
  featureType: '@type'
  entityType: '@type'
  has_provenance:
    x-jsonld-id: http://purl.org/dc/terms/provenance
    x-jsonld-type: '@id'
  wasGeneratedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
    x-jsonld-type: '@id'
  wasAttributedTo:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAttributedTo
    x-jsonld-type: '@id'
  wasDerivedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
    x-jsonld-type: '@id'
  alternateOf:
    x-jsonld-id: http://www.w3.org/ns/prov#alternateOf
    x-jsonld-type: '@id'
  hadPrimarySource:
    x-jsonld-id: http://www.w3.org/ns/prov#hadPrimarySource
    x-jsonld-type: '@id'
  specializationOf:
    x-jsonld-id: http://www.w3.org/ns/prov#specializationOf
    x-jsonld-type: '@id'
  wasInvalidatedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasInvalidatedBy
    x-jsonld-type: '@id'
  wasQuotedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasQuotedFrom
    x-jsonld-type: '@id'
  wasRevisionOf:
    x-jsonld-id: http://www.w3.org/ns/prov#wasRevisionOf
    x-jsonld-type: '@id'
  atLocation:
    x-jsonld-id: http://www.w3.org/ns/prov#atLocation
    x-jsonld-type: '@id'
  qualifiedGeneration:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedGeneration
    x-jsonld-type: '@id'
  qualifiedInvalidation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInvalidation
    x-jsonld-type: '@id'
  qualifiedDerivation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedDerivation
    x-jsonld-type: '@id'
  qualifiedAttribution:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedAttribution
    x-jsonld-type: '@id'
  activityType: '@type'
  agentType: '@type'
  Activity: http://www.w3.org/ns/prov#Activity
  ActivityInfluence: http://www.w3.org/ns/prov#ActivityInfluence
  Agent: http://www.w3.org/ns/prov#Agent
  AgentInfluence: http://www.w3.org/ns/prov#AgentInfluence
  Association: http://www.w3.org/ns/prov#Association
  Attribution: http://www.w3.org/ns/prov#Attribution
  Bundle: http://www.w3.org/ns/prov#Bundle
  Collection: http://www.w3.org/ns/prov#Collection
  Communication: http://www.w3.org/ns/prov#Communication
  Delegation: http://www.w3.org/ns/prov#Delegation
  Derivation: http://www.w3.org/ns/prov#Derivation
  EmptyCollection: http://www.w3.org/ns/prov#EmptyCollection
  End: http://www.w3.org/ns/prov#End
  Entity: http://www.w3.org/ns/prov#Entity
  EntityInfluence: http://www.w3.org/ns/prov#EntityInfluence
  Generation: http://www.w3.org/ns/prov#Generation
  Influence: http://www.w3.org/ns/prov#Influence
  InstantaneousEvent: http://www.w3.org/ns/prov#InstantaneousEvent
  Invalidation: http://www.w3.org/ns/prov#Invalidation
  Location: http://www.w3.org/ns/prov#Location
  Organization: http://www.w3.org/ns/prov#Organization
  Person: http://www.w3.org/ns/prov#Person
  Plan: http://www.w3.org/ns/prov#Plan
  PrimarySource: http://www.w3.org/ns/prov#PrimarySource
  Quotation: http://www.w3.org/ns/prov#Quotation
  Revision: http://www.w3.org/ns/prov#Revision
  Role: http://www.w3.org/ns/prov#Role
  SoftwareAgent: http://www.w3.org/ns/prov#SoftwareAgent
  Start: http://www.w3.org/ns/prov#Start
  Usage: http://www.w3.org/ns/prov#Usage
  ServiceDescription: http://www.w3.org/ns/prov#ServiceDescription
  DirectQueryService: http://www.w3.org/ns/prov#DirectQueryService
  Accept: http://www.w3.org/ns/prov#Accept
  Contribute: http://www.w3.org/ns/prov#Contribute
  Contributor: http://www.w3.org/ns/prov#Contributor
  Copyright: http://www.w3.org/ns/prov#Copyright
  Create: http://www.w3.org/ns/prov#Create
  Creator: http://www.w3.org/ns/prov#Creator
  Modify: http://www.w3.org/ns/prov#Modify
  Publish: http://www.w3.org/ns/prov#Publish
  Publisher: http://www.w3.org/ns/prov#Publisher
  Replace: http://www.w3.org/ns/prov#Replace
  RightsAssignment: http://www.w3.org/ns/prov#RightsAssignment
  RightsHolder: http://www.w3.org/ns/prov#RightsHolder
  Submit: http://www.w3.org/ns/prov#Submit
  Dictionary: http://www.w3.org/ns/prov#Dictionary
  EmptyDictionary: http://www.w3.org/ns/prov#EmptyDictionary
  KeyEntityPair: http://www.w3.org/ns/prov#KeyEntityPair
  Insertion: http://www.w3.org/ns/prov#Insertion
  Removal: http://www.w3.org/ns/prov#Removal
  atTime:
    x-jsonld-id: http://www.w3.org/ns/prov#atTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  endedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#endedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  generatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#generatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  invalidatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#invalidatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  startedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#startedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  value: http://www.w3.org/ns/prov#value
  provenanceUriTemplate: http://www.w3.org/ns/prov#provenanceUriTemplate
  pairKey:
    x-jsonld-id: http://www.w3.org/ns/prov#pairKey
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  removedKey:
    x-jsonld-id: http://www.w3.org/ns/prov#removedKey
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  actedOnBehalfOf:
    x-jsonld-id: http://www.w3.org/ns/prov#actedOnBehalfOf
    x-jsonld-type: '@id'
  agent:
    x-jsonld-id: http://www.w3.org/ns/prov#agent
    x-jsonld-type: '@id'
  entity:
    x-jsonld-id: http://www.w3.org/ns/prov#entity
    x-jsonld-type: '@id'
  generated:
    x-jsonld-id: http://www.w3.org/ns/prov#generated
    x-jsonld-type: '@id'
  hadActivity:
    x-jsonld-id: http://www.w3.org/ns/prov#hadActivity
    x-jsonld-type: '@id'
  activity:
    x-jsonld-id: http://www.w3.org/ns/prov#activity
    x-jsonld-type: '@id'
  hadGeneration:
    x-jsonld-id: http://www.w3.org/ns/prov#hadGeneration
    x-jsonld-type: '@id'
  hadPlan:
    x-jsonld-id: http://www.w3.org/ns/prov#hadPlan
    x-jsonld-type: '@id'
  hadRole:
    x-jsonld-id: http://www.w3.org/ns/prov#hadRole
    x-jsonld-type: '@id'
  hadUsage:
    x-jsonld-id: http://www.w3.org/ns/prov#hadUsage
    x-jsonld-type: '@id'
  influenced:
    x-jsonld-id: http://www.w3.org/ns/prov#influenced
    x-jsonld-type: '@id'
  influencer:
    x-jsonld-id: http://www.w3.org/ns/prov#influencer
    x-jsonld-type: '@id'
  invalidated:
    x-jsonld-id: http://www.w3.org/ns/prov#invalidated
    x-jsonld-type: '@id'
  qualifiedAssociation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedAssociation
    x-jsonld-type: '@id'
  qualifiedCommunication:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedCommunication
    x-jsonld-type: '@id'
  qualifiedDelegation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedDelegation
    x-jsonld-type: '@id'
  qualifiedEnd:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedEnd
    x-jsonld-type: '@id'
  qualifiedPrimarySource:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedPrimarySource
    x-jsonld-type: '@id'
  qualifiedQuotation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedQuotation
    x-jsonld-type: '@id'
  qualifiedRevision:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedRevision
    x-jsonld-type: '@id'
  qualifiedStart:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedStart
    x-jsonld-type: '@id'
  qualifiedUsage:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedUsage
    x-jsonld-type: '@id'
  used:
    x-jsonld-id: http://www.w3.org/ns/prov#used
    x-jsonld-type: '@id'
  wasAssociatedWith:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAssociatedWith
    x-jsonld-type: '@id'
  wasEndedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasEndedBy
    x-jsonld-type: '@id'
  wasInformedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasInformedBy
    x-jsonld-type: '@id'
  wasStartedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasStartedBy
    x-jsonld-type: '@id'
  has_anchor:
    x-jsonld-id: http://www.w3.org/ns/prov#has_anchor
    x-jsonld-type: '@id'
  has_query_service:
    x-jsonld-id: http://www.w3.org/ns/prov#has_query_service
    x-jsonld-type: '@id'
  describesService:
    x-jsonld-id: http://www.w3.org/ns/prov#describesService
    x-jsonld-type: '@id'
  pingback:
    x-jsonld-id: http://www.w3.org/ns/prov#pingback
    x-jsonld-type: '@id'
  dictionary:
    x-jsonld-id: http://www.w3.org/ns/prov#dictionary
    x-jsonld-type: '@id'
  derivedByInsertionFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#derivedByInsertionFrom
    x-jsonld-type: '@id'
  derivedByRemovalFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#derivedByRemovalFrom
    x-jsonld-type: '@id'
  insertedKeyEntityPair:
    x-jsonld-id: http://www.w3.org/ns/prov#insertedKeyEntityPair
    x-jsonld-type: '@id'
  hadDictionaryMember:
    x-jsonld-id: http://www.w3.org/ns/prov#hadDictionaryMember
    x-jsonld-type: '@id'
  pairEntity:
    x-jsonld-id: http://www.w3.org/ns/prov#pairEntity
    x-jsonld-type: '@id'
  qualifiedInsertion:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInsertion
    x-jsonld-type: '@id'
  qualifiedRemoval:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedRemoval
    x-jsonld-type: '@id'
  asInBundle:
    x-jsonld-id: http://www.w3.org/ns/prov#asInBundle
    x-jsonld-type: '@id'
  mentionOf:
    x-jsonld-id: http://www.w3.org/ns/prov#mentionOf
    x-jsonld-type: '@id'
  Workflow: http://www.w3.org/ns/prov#Plan
  applicationCategory: https://schema.org/applicationCategory
  version: http://purl.org/dc/terms/hasVersion
  method: http://purl.org/dc/terms/method
  softwareVersion: https://schema.org/softwareVersion
  programmingLanguage: https://schema.org/programmingLanguage
  applicationPackage:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#applicationPackage
    x-jsonld-type: '@id'
  profileId:
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
  required:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#required
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
  role: https://w3id.org/ogc/hosted/seadots/catalog#role
  code: http://purl.org/dc/terms/identifier
  roles:
    x-jsonld-id: http://www.w3.org/ns/dcat#hadRole
    x-jsonld-container: '@set'
  organization: https://schema.org/affiliation
  interval: http://purl.org/dc/terms/temporal
  resolution: http://www.w3.org/ns/dcat#temporalResolution
  concepts:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#Concept
    x-jsonld-container: '@set'
  scheme: http://www.w3.org/2004/02/skos/core#inScheme
  label: http://www.w3.org/2004/02/skos/core#prefLabel
  format: http://purl.org/dc/terms/format
  mediaType: http://purl.org/dc/terms/format
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/reef-effect#
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  dct: http://purl.org/dc/terms/
  rec: https://www.opengis.net/def/ogc-api/records/
  xsd: http://www.w3.org/2001/XMLSchema#
  dcat: http://www.w3.org/ns/dcat#
  skos: http://www.w3.org/2004/02/skos/core#
  thns: https://w3id.org/ogc/stac/themes/
  oa: http://www.w3.org/ns/oa#
  prov: http://www.w3.org/ns/prov#
  schema: https://schema.org/
  dcterms: http://purl.org/dc/terms/
  seadots: https://w3id.org/ogc/hosted/seadots/catalog#
  apkg: https://w3id.org/apkg/terms/
  seadotsReef: https://w3id.org/ogc/hosted/seadots/reef-effect#
  owl: http://www.w3.org/2002/07/owl#
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  w3ctime: http://www.w3.org/2006/time#
  dctype: http://purl.org/dc/dcmitype/
  vcard: http://www.w3.org/2006/vcard/ns#
  foaf: http://xmlns.com/foaf/0.1/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/reef-effect/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/reef-effect/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/catalog#",
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "features": {
      "@container": "@set",
      "@id": "geojson:features"
    },
    "type": "@type",
    "id": "@id",
    "properties": "@nest",
    "geometry": {
      "@context": {
        "coordinates": {
          "@container": "@list",
          "@id": "geojson:coordinates"
        }
      },
      "@id": "geojson:geometry"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "links": {
      "@context": {
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "conformsTo": {
      "@container": "@set",
      "@id": "dct:conformsTo",
      "@type": "@id"
    },
    "time": "dct:temporal",
    "linkTemplates": {
      "@context": {
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:format",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent",
        "uriTemplate": {
          "@type": "xsd:string",
          "@id": "rec:uriTemplate"
        },
        "varBase": "rec:varBase",
        "variables": {
          "@id": "rec:hasVariable",
          "@container": "@index",
          "@index": "dct:identifier"
        }
      },
      "@id": "rec:hasLinkTemplate"
    },
    "created": "dct:created",
    "updated": "dct:modified",
    "title": {
      "@container": "@set",
      "@id": "dct:title"
    },
    "description": {
      "@container": "@set",
      "@id": "dct:description"
    },
    "keywords": {
      "@container": "@set",
      "@id": "dcat:keyword"
    },
    "language": {
      "@id": "rec:language",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "languages": {
      "@container": "@set",
      "@id": "rec:languages",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "resourceLanguages": {
      "@container": "@set",
      "@id": "rec:resourceLanguages",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "externalIds": {
      "@container": "@set",
      "@id": "rec:scopedIdentifier",
      "@context": {
        "scheme": "rec:scheme",
        "value": "rec:id"
      }
    },
    "themes": {
      "@container": "@set",
      "@id": "rec:themes",
      "@context": {
        "concepts": {
          "@id": "rec:concept",
          "@context": {
            "id": {
              "@type": "xsd:string",
              "@id": "rec:conceptID"
            },
            "url": {
              "@type": "@id",
              "@id": "dcat:theme"
            }
          }
        },
        "scheme": "rec:scheme"
      }
    },
    "formats": {
      "@id": "rec:format",
      "@context": {
        "name": "rec:name"
      }
    },
    "contacts": {
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "license": "dct:license",
    "accessrights": "dct:accessRights",
    "variables": {
      "@container": "@id",
      "@id": "rec:hasVariable",
      "@context": {
        "@base": "http://example.com/variables/",
        "@vocab": "https://www.opengis.net/def/ogc-api/records/"
      }
    },
    "wasInfluencedBy": {
      "@id": "prov:wasInfluencedBy",
      "@type": "@id"
    },
    "qualifiedInfluence": {
      "@id": "prov:qualifiedInfluence",
      "@type": "@id"
    },
    "hadMember": {
      "@id": "prov:hadMember",
      "@type": "@id"
    },
    "provType": "@type",
    "featureType": "@type",
    "entityType": "@type",
    "has_provenance": {
      "@id": "dct:provenance",
      "@type": "@id"
    },
    "wasGeneratedBy": {
      "@id": "prov:wasGeneratedBy",
      "@type": "@id"
    },
    "wasAttributedTo": {
      "@id": "prov:wasAttributedTo",
      "@type": "@id"
    },
    "wasDerivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@type": "@id"
    },
    "alternateOf": {
      "@id": "prov:alternateOf",
      "@type": "@id"
    },
    "hadPrimarySource": {
      "@id": "prov:hadPrimarySource",
      "@type": "@id"
    },
    "specializationOf": {
      "@id": "prov:specializationOf",
      "@type": "@id"
    },
    "wasInvalidatedBy": {
      "@id": "prov:wasInvalidatedBy",
      "@type": "@id"
    },
    "wasQuotedFrom": {
      "@id": "prov:wasQuotedFrom",
      "@type": "@id"
    },
    "wasRevisionOf": {
      "@id": "prov:wasRevisionOf",
      "@type": "@id"
    },
    "atLocation": {
      "@id": "prov:atLocation",
      "@type": "@id"
    },
    "qualifiedGeneration": {
      "@id": "prov:qualifiedGeneration",
      "@type": "@id"
    },
    "qualifiedInvalidation": {
      "@id": "prov:qualifiedInvalidation",
      "@type": "@id"
    },
    "qualifiedDerivation": {
      "@id": "prov:qualifiedDerivation",
      "@type": "@id"
    },
    "qualifiedAttribution": {
      "@id": "prov:qualifiedAttribution",
      "@type": "@id"
    },
    "activityType": "@type",
    "agentType": "@type",
    "Activity": "prov:Activity",
    "ActivityInfluence": "prov:ActivityInfluence",
    "Agent": "prov:Agent",
    "AgentInfluence": "prov:AgentInfluence",
    "Association": "prov:Association",
    "Attribution": "prov:Attribution",
    "Bundle": "prov:Bundle",
    "Collection": "prov:Collection",
    "Communication": "prov:Communication",
    "Delegation": "prov:Delegation",
    "Derivation": "prov:Derivation",
    "EmptyCollection": "prov:EmptyCollection",
    "End": "prov:End",
    "Entity": "prov:Entity",
    "EntityInfluence": "prov:EntityInfluence",
    "Generation": "prov:Generation",
    "Influence": "prov:Influence",
    "InstantaneousEvent": "prov:InstantaneousEvent",
    "Invalidation": "prov:Invalidation",
    "Location": "prov:Location",
    "Organization": "prov:Organization",
    "Person": "prov:Person",
    "Plan": "prov:Plan",
    "PrimarySource": "prov:PrimarySource",
    "Quotation": "prov:Quotation",
    "Revision": "prov:Revision",
    "Role": "prov:Role",
    "SoftwareAgent": "prov:SoftwareAgent",
    "Start": "prov:Start",
    "Usage": "prov:Usage",
    "ServiceDescription": "prov:ServiceDescription",
    "DirectQueryService": "prov:DirectQueryService",
    "Accept": "prov:Accept",
    "Contribute": "prov:Contribute",
    "Contributor": "prov:Contributor",
    "Copyright": "prov:Copyright",
    "Create": "prov:Create",
    "Creator": "prov:Creator",
    "Modify": "prov:Modify",
    "Publish": "prov:Publish",
    "Publisher": "prov:Publisher",
    "Replace": "prov:Replace",
    "RightsAssignment": "prov:RightsAssignment",
    "RightsHolder": "prov:RightsHolder",
    "Submit": "prov:Submit",
    "Dictionary": "prov:Dictionary",
    "EmptyDictionary": "prov:EmptyDictionary",
    "KeyEntityPair": "prov:KeyEntityPair",
    "Insertion": "prov:Insertion",
    "Removal": "prov:Removal",
    "atTime": {
      "@id": "prov:atTime",
      "@type": "xsd:dateTime"
    },
    "endedAtTime": {
      "@id": "prov:endedAtTime",
      "@type": "xsd:dateTime"
    },
    "generatedAtTime": {
      "@id": "prov:generatedAtTime",
      "@type": "xsd:dateTime"
    },
    "invalidatedAtTime": {
      "@id": "prov:invalidatedAtTime",
      "@type": "xsd:dateTime"
    },
    "startedAtTime": {
      "@id": "prov:startedAtTime",
      "@type": "xsd:dateTime"
    },
    "value": "prov:value",
    "provenanceUriTemplate": "prov:provenanceUriTemplate",
    "pairKey": {
      "@id": "prov:pairKey",
      "@type": "rdfs:Literal"
    },
    "removedKey": {
      "@id": "prov:removedKey",
      "@type": "rdfs:Literal"
    },
    "actedOnBehalfOf": {
      "@id": "prov:actedOnBehalfOf",
      "@type": "@id"
    },
    "agent": {
      "@id": "prov:agent",
      "@type": "@id"
    },
    "entity": {
      "@id": "prov:entity",
      "@type": "@id"
    },
    "generated": {
      "@id": "prov:generated",
      "@type": "@id"
    },
    "hadActivity": {
      "@id": "prov:hadActivity",
      "@type": "@id"
    },
    "activity": {
      "@id": "prov:activity",
      "@type": "@id"
    },
    "hadGeneration": {
      "@id": "prov:hadGeneration",
      "@type": "@id"
    },
    "hadPlan": {
      "@id": "prov:hadPlan",
      "@type": "@id"
    },
    "hadRole": {
      "@id": "prov:hadRole",
      "@type": "@id"
    },
    "hadUsage": {
      "@id": "prov:hadUsage",
      "@type": "@id"
    },
    "influenced": {
      "@id": "prov:influenced",
      "@type": "@id"
    },
    "influencer": {
      "@id": "prov:influencer",
      "@type": "@id"
    },
    "invalidated": {
      "@id": "prov:invalidated",
      "@type": "@id"
    },
    "qualifiedAssociation": {
      "@id": "prov:qualifiedAssociation",
      "@type": "@id"
    },
    "qualifiedCommunication": {
      "@id": "prov:qualifiedCommunication",
      "@type": "@id"
    },
    "qualifiedDelegation": {
      "@id": "prov:qualifiedDelegation",
      "@type": "@id"
    },
    "qualifiedEnd": {
      "@id": "prov:qualifiedEnd",
      "@type": "@id"
    },
    "qualifiedPrimarySource": {
      "@id": "prov:qualifiedPrimarySource",
      "@type": "@id"
    },
    "qualifiedQuotation": {
      "@id": "prov:qualifiedQuotation",
      "@type": "@id"
    },
    "qualifiedRevision": {
      "@id": "prov:qualifiedRevision",
      "@type": "@id"
    },
    "qualifiedStart": {
      "@id": "prov:qualifiedStart",
      "@type": "@id"
    },
    "qualifiedUsage": {
      "@id": "prov:qualifiedUsage",
      "@type": "@id"
    },
    "used": {
      "@id": "prov:used",
      "@type": "@id"
    },
    "wasAssociatedWith": {
      "@id": "prov:wasAssociatedWith",
      "@type": "@id"
    },
    "wasEndedBy": {
      "@id": "prov:wasEndedBy",
      "@type": "@id"
    },
    "wasInformedBy": {
      "@id": "prov:wasInformedBy",
      "@type": "@id"
    },
    "wasStartedBy": {
      "@id": "prov:wasStartedBy",
      "@type": "@id"
    },
    "has_anchor": {
      "@id": "prov:has_anchor",
      "@type": "@id"
    },
    "has_query_service": {
      "@id": "prov:has_query_service",
      "@type": "@id"
    },
    "describesService": {
      "@id": "prov:describesService",
      "@type": "@id"
    },
    "pingback": {
      "@id": "prov:pingback",
      "@type": "@id"
    },
    "dictionary": {
      "@id": "prov:dictionary",
      "@type": "@id"
    },
    "derivedByInsertionFrom": {
      "@id": "prov:derivedByInsertionFrom",
      "@type": "@id"
    },
    "derivedByRemovalFrom": {
      "@id": "prov:derivedByRemovalFrom",
      "@type": "@id"
    },
    "insertedKeyEntityPair": {
      "@id": "prov:insertedKeyEntityPair",
      "@type": "@id"
    },
    "hadDictionaryMember": {
      "@id": "prov:hadDictionaryMember",
      "@type": "@id"
    },
    "pairEntity": {
      "@id": "prov:pairEntity",
      "@type": "@id"
    },
    "qualifiedInsertion": {
      "@id": "prov:qualifiedInsertion",
      "@type": "@id"
    },
    "qualifiedRemoval": {
      "@id": "prov:qualifiedRemoval",
      "@type": "@id"
    },
    "asInBundle": {
      "@id": "prov:asInBundle",
      "@type": "@id"
    },
    "mentionOf": {
      "@id": "prov:mentionOf",
      "@type": "@id"
    },
    "name": "rdfs:label",
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "rights": "dcat:rights",
    "Workflow": "prov:Plan",
    "applicationCategory": "schema:applicationCategory",
    "version": "dct:hasVersion",
    "method": "dct:method",
    "softwareVersion": "schema:softwareVersion",
    "programmingLanguage": "schema:programmingLanguage",
    "applicationPackage": {
      "@id": "seadots:applicationPackage",
      "@type": "@id"
    },
    "profileId": {
      "@id": "dct:conformsTo",
      "@type": "@id"
    },
    "required": {
      "@id": "seadots:required",
      "@type": "xsd:boolean"
    },
    "role": "seadots:role",
    "code": "dct:identifier",
    "roles": {
      "@id": "dcat:hadRole",
      "@container": "@set"
    },
    "organization": "schema:affiliation",
    "interval": "dct:temporal",
    "resolution": "dcat:temporalResolution",
    "concepts": {
      "@id": "skos:Concept",
      "@container": "@set"
    },
    "scheme": "skos:inScheme",
    "label": "skos:prefLabel",
    "format": "dct:format",
    "mediaType": "dct:format",
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "rec": "https://www.opengis.net/def/ogc-api/records/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "w3ctime": "http://www.w3.org/2006/time#",
    "dctype": "http://purl.org/dc/dcmitype/",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "prov": "http://www.w3.org/ns/prov#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "thns": "https://w3id.org/ogc/stac/themes/",
    "schema": "https://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "seadots": "https://w3id.org/ogc/hosted/seadots/catalog#",
    "apkg": "https://w3id.org/apkg/terms/",
    "seadotsReef": "https://w3id.org/ogc/hosted/seadots/reef-effect#",
    "softwareType": "dct:type",
    "experiment": {
      "@context": {
        "kind": "seadotsReef:kind",
        "purpose": "dct:purpose",
        "application": {
          "@id": "seadotsReef:application",
          "@type": "@id"
        },
        "modelledBy": {
          "@id": "seadotsReef:modelledBy",
          "@type": "@id"
        },
        "evidenceEquation": {
          "@id": "seadotsReef:evidenceEquation",
          "@type": "@id"
        },
        "parameters": {
          "@context": {
            "parameterSchema": "seadotsReef:parameterSchema",
            "vocabularyTerm": {
              "@id": "skos:exactMatch",
              "@type": "@id"
            }
          },
          "@id": "seadotsReef:parameter",
          "@container": "@set"
        },
        "inputs": {
          "@context": {
            "equationBinding": "seadotsReef:equationBinding"
          },
          "@id": "seadotsReef:input",
          "@container": "@set"
        },
        "outputs": {
          "@id": "seadotsReef:output",
          "@container": "@set",
          "@type": "@id"
        },
        "execution": {
          "@context": {
            "language": "dct:language",
            "languageVersion": "seadotsReef:languageVersion",
            "dependencies": {
              "@id": "seadotsReef:dependency",
              "@container": "@set"
            },
            "entrypoint": "seadotsReef:entrypoint",
            "scheduling": "seadotsReef:scheduling",
            "reproducibility": {
              "@context": {
                "seedPolicy": "seadotsReef:seedPolicy",
                "provenance": "prov:wasGeneratedBy"
              },
              "@id": "seadotsReef:reproducibility"
            }
          },
          "@id": "seadotsReef:execution"
        },
        "successCriteria": {
          "@id": "seadotsReef:successCriterion",
          "@container": "@set"
        }
      },
      "@id": "seadotsReef:experiment"
    },
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/reef-effect/context.jsonld)

## Sources

* [GeoDCAT-Records](https://ogcincubator.github.io/geodcat-ogcapi-records/)
* [ODD Protocol Description Record bblock](https://w3id.org/ogc/hosted/seadots/odd-protocol)
* [Equation Property Relationship bblock](https://w3id.org/ogc/hosted/seadots/equation-property-relationship)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/reef-effect`

