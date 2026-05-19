
# Computational Experiment (Schema)

`ogc.hosted.seadots.experiment` *v0.2*

OGC API Records profile for describing a computational experiment realising a documented model. Points at the executable code that runs the experiment (any language / format that exists and runs — Python, Jupyter, R, …), and binds it to the documented model (an ODD record), the evidence equation (an `equation-property-relationship` record), and to standalone input records (one per data class) and `experiment-output` records, all referenced by URI.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Computational Experiment

OGC API Records profile for describing one computational experiment that realises a documented model.

A computational experiment is the executable counterpart of an ODD Protocol description: it commits to specific software, specific inputs and a specific output target. The record points at the executable code (Python script, Jupyter notebook, R script, etc.) that runs the experiment, and at standalone per-class input records (e.g. `area-of-interest`, `floating-wind-infrastructure`, `benthic-biomass-density-mareano`, …) and `experiment-output` records by URI so they can be reused across runs.

## What an experiment record carries

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
  outputs[]           — link[] to experiment-output records (NOT inlined)
  execution           — language, languageVersion, dependencies, entrypoint,
                          scheduling, reproducibility flags
  successCriteria[]   — assertions the run must satisfy to be considered successful
```

## Composition pattern

The experiment record references inputs and outputs **by URI** rather than embedding them. This matches the cross-bblock composition already used by `odd-protocol` (which references `equation-property-relationship` records by URI) and keeps the experiment record stable when the input set is revised.

- Each input is a standalone instance of the matching per-class bblock: [`area-of-interest`](../area-of-interest/), [`floating-wind-infrastructure`](../floating-wind-infrastructure/), [`benthic-biomass-density-mareano`](../benthic-biomass-density-mareano/), [`benthic-biomass-density-imr`](../benthic-biomass-density-imr/), [`reef-aggregation-index`](../reef-aggregation-index/), [`colonisation-time-factor`](../colonisation-time-factor/).
- Each output is a standalone instance of [`experiment-output`](../experiment-output/).
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
  "id": "https://example.org/norwegian-ses/experiment/utsira-reef-biomass-surroundings-v1",
  "type": "Feature",
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
    "type": "SoftwareSourceCode",
    "title": "Utsira surroundings — reef-biomass experiment",
    "description": "Experiment record for an executable run of the Utsira reef-biomass calculation over the surroundings of Utsira island. Realises the one-submodel ODD demonstrator `utsira_reef_biomass_demonstrator` and the canonical equation record `reef-biomass-equation`. Inputs and outputs are referenced by URI as standalone per-class input records and `experiment-output` records. The executable is a self-contained Python reproducibility script (`scripts/utsira_reef_biomass.py`).",
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
    "keywords": ["experiment", "Utsira", "surroundings", "reef biomass", "SeaDOTs", "Python"],
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
      "purpose": "Evaluate the reef-biomass equation B_reef = sum_i (A_sub . D_pre,i . AF_i . C_t) for the surroundings of Utsira island under the Norwegian SES scenario. Inputs are the six per-class input records cited below; outputs are the three experiment-output records cited below.",

      "application": {
        "href": "../scripts/utsira_reef_biomass.py",
        "type": "text/x-python",
        "rel": "https://w3id.org/ogc/hosted/seadots/experiment#application",
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
          "schema": { "format": "application/geo+json" },
          "vocabularyTerm": "http://www.opengis.net/def/property/OGC/0/area-of-interest"
        },
        {
          "name": "taxon_groups",
          "title": "TaxonGroup index values",
          "description": "Scientific names iterated by index i.",
          "schema": { "type": "array", "items": { "type": "string" } },
          "vocabularyTerm": "http://rs.tdwg.org/dwc/terms/scientificName"
        },
        {
          "name": "scenario_t0",
          "title": "Scenario start date",
          "schema": { "type": "string", "format": "date" }
        },
        {
          "name": "colonisation_months",
          "title": "Months since installation",
          "schema": { "type": "integer", "minimum": 0 }
        }
      ],

      "inputs": [
        {
          "href": "https://example.org/norwegian-ses/area-of-interest/utsira-surroundings",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#input",
          "title": "AOI — surroundings of Utsira island",
          "equationBinding": null
        },
        {
          "href": "https://example.org/norwegian-ses/floating-wind-infrastructure/utsira-nord-60x15mw",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#input",
          "title": "Submerged infrastructure layout — Utsira Nord 60 × 15 MW",
          "equationBinding": "A_{sub}"
        },
        {
          "href": "https://example.org/norwegian-ses/benthic-biomass-density-mareano/norwegian-shelf",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#input",
          "title": "MAREANO benthic biomass density — primary baseline",
          "equationBinding": "D_{pre,i}"
        },
        {
          "href": "https://example.org/norwegian-ses/benthic-biomass-density-imr/ices-iva-fallback",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#input",
          "title": "IMR benthic biomass baseline — fallback",
          "equationBinding": "D_{pre,i}"
        },
        {
          "href": "https://example.org/norwegian-ses/reef-aggregation-index/degraer2020-bindings",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#input",
          "title": "Reef aggregation index bindings",
          "equationBinding": "AF_i"
        },
        {
          "href": "https://example.org/norwegian-ses/colonisation-time-factor/default-sigmoid",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#input",
          "title": "Colonisation time factor",
          "equationBinding": "C_t"
        }
      ],

      "outputs": [
        {
          "href": "https://example.org/norwegian-ses/experiment-output/reef-biomass-result",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#output",
          "title": "Reef-associated biomass — structured result"
        },
        {
          "href": "https://example.org/norwegian-ses/experiment-output/stac-catalog",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#output",
          "title": "STAC catalog for the run"
        },
        {
          "href": "https://example.org/norwegian-ses/experiment-output/prov-record",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#output",
          "title": "PROV-O provenance (JSON-LD)"
        }
      ],

      "execution": {
        "language": "python",
        "languageVersion": ">=3.9",
        "dependencies": [],
        "entrypoint": "python3 _sources/experiment/scripts/utsira_reef_biomass.py",
        "scheduling": "single deterministic pass over taxon_groups (ODD processOverview.scheduling)",
        "reproducibility": {
          "seedPolicy": "deterministic — equation is closed-form, no stochastic submodels",
          "provenance": "PROV-O record emitted as one of the outputs"
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
    { "rel": "describedby", "href": "bblocks://ogc.hosted.seadots.experiment", "type": "application/schema+json", "title": "Experiment bblock" },
    { "rel": "alternate", "href": "../scripts/utsira_reef_biomass.py", "type": "text/x-python", "title": "Reproducibility script — runs the worked example end-to-end" },
    { "rel": "related", "href": "https://w3id.org/ogc/hosted/seadots/odd-protocol/examples/utsira_reef_biomass_demonstrator", "type": "application/json", "title": "ODD demonstrator that this experiment realises" },
    { "rel": "cite-as", "href": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation", "type": "application/ld+json", "title": "Reef-biomass equation record" }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/experiment/context.jsonld",
  "id": "https://example.org/norwegian-ses/experiment/utsira-reef-biomass-surroundings-v1",
  "type": "Feature",
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
    "type": "SoftwareSourceCode",
    "title": "Utsira surroundings \u2014 reef-biomass experiment",
    "description": "Experiment record for an executable run of the Utsira reef-biomass calculation over the surroundings of Utsira island. Realises the one-submodel ODD demonstrator `utsira_reef_biomass_demonstrator` and the canonical equation record `reef-biomass-equation`. Inputs and outputs are referenced by URI as standalone per-class input records and `experiment-output` records. The executable is a self-contained Python reproducibility script (`scripts/utsira_reef_biomass.py`).",
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
      "experiment",
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
      "purpose": "Evaluate the reef-biomass equation B_reef = sum_i (A_sub . D_pre,i . AF_i . C_t) for the surroundings of Utsira island under the Norwegian SES scenario. Inputs are the six per-class input records cited below; outputs are the three experiment-output records cited below.",
      "application": {
        "href": "../scripts/utsira_reef_biomass.py",
        "type": "text/x-python",
        "rel": "https://w3id.org/ogc/hosted/seadots/experiment#application",
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
          "schema": {
            "format": "application/geo+json"
          },
          "vocabularyTerm": "http://www.opengis.net/def/property/OGC/0/area-of-interest"
        },
        {
          "name": "taxon_groups",
          "title": "TaxonGroup index values",
          "description": "Scientific names iterated by index i.",
          "schema": {
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
          "schema": {
            "type": "string",
            "format": "date"
          }
        },
        {
          "name": "colonisation_months",
          "title": "Months since installation",
          "schema": {
            "type": "integer",
            "minimum": 0
          }
        }
      ],
      "inputs": [
        {
          "href": "https://example.org/norwegian-ses/area-of-interest/utsira-surroundings",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#input",
          "title": "AOI \u2014 surroundings of Utsira island",
          "equationBinding": null
        },
        {
          "href": "https://example.org/norwegian-ses/floating-wind-infrastructure/utsira-nord-60x15mw",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#input",
          "title": "Submerged infrastructure layout \u2014 Utsira Nord 60 \u00d7 15 MW",
          "equationBinding": "A_{sub}"
        },
        {
          "href": "https://example.org/norwegian-ses/benthic-biomass-density-mareano/norwegian-shelf",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#input",
          "title": "MAREANO benthic biomass density \u2014 primary baseline",
          "equationBinding": "D_{pre,i}"
        },
        {
          "href": "https://example.org/norwegian-ses/benthic-biomass-density-imr/ices-iva-fallback",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#input",
          "title": "IMR benthic biomass baseline \u2014 fallback",
          "equationBinding": "D_{pre,i}"
        },
        {
          "href": "https://example.org/norwegian-ses/reef-aggregation-index/degraer2020-bindings",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#input",
          "title": "Reef aggregation index bindings",
          "equationBinding": "AF_i"
        },
        {
          "href": "https://example.org/norwegian-ses/colonisation-time-factor/default-sigmoid",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#input",
          "title": "Colonisation time factor",
          "equationBinding": "C_t"
        }
      ],
      "outputs": [
        {
          "href": "https://example.org/norwegian-ses/experiment-output/reef-biomass-result",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#output",
          "title": "Reef-associated biomass \u2014 structured result"
        },
        {
          "href": "https://example.org/norwegian-ses/experiment-output/stac-catalog",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#output",
          "title": "STAC catalog for the run"
        },
        {
          "href": "https://example.org/norwegian-ses/experiment-output/prov-record",
          "type": "application/json",
          "rel": "https://w3id.org/ogc/hosted/seadots/experiment#output",
          "title": "PROV-O provenance (JSON-LD)"
        }
      ],
      "execution": {
        "language": "python",
        "languageVersion": ">=3.9",
        "dependencies": [],
        "entrypoint": "python3 _sources/experiment/scripts/utsira_reef_biomass.py",
        "scheduling": "single deterministic pass over taxon_groups (ODD processOverview.scheduling)",
        "reproducibility": {
          "seedPolicy": "deterministic \u2014 equation is closed-form, no stochastic submodels",
          "provenance": "PROV-O record emitted as one of the outputs"
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
      "href": "bblocks://ogc.hosted.seadots.experiment",
      "type": "application/schema+json",
      "title": "Experiment bblock"
    },
    {
      "rel": "alternate",
      "href": "../scripts/utsira_reef_biomass.py",
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
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/experiment#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/norwegian-ses/experiment/utsira-reef-biomass-surroundings-v1> a geojson:Feature ;
    dcterms:temporal [ dcterms:temporal "2026-05-13",
                "2028-05-13" ;
            dcat:temporalResolution "P12M" ] ;
    rdfs:seeAlso [ rdfs:label "Experiment bblock" ;
            dcterms:format "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.experiment> ],
        [ rdfs:label "Reproducibility script — runs the worked example end-to-end" ;
            dcterms:format "text/x-python" ;
            ns1:relation <http://www.iana.org/assignments/relation/alternate> ;
            oa:hasTarget <file:///github/scripts/utsira_reef_biomass.py> ],
        [ rdfs:label "ODD demonstrator that this experiment realises" ;
            dcterms:format "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://w3id.org/ogc/hosted/seadots/odd-protocol/examples/utsira_reef_biomass_demonstrator> ],
        [ rdfs:label "Reef-biomass equation record" ;
            dcterms:format "application/ld+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation> ] ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 4.2e+00 5.91e+01 ) ( 5.3e+00 5.91e+01 ) ( 5.3e+00 5.97e+01 ) ( 4.2e+00 5.97e+01 ) ( 4.2e+00 5.91e+01 ) ) ) ] ;
    geojson:properties [ a seadots:SoftwareSourceCode ;
            dcterms:conformsTo <https://ogcincubator.github.io/geodcat-ogcapi-records/> ;
            dcterms:created "2026-05-18" ;
            dcterms:description "Experiment record for an executable run of the Utsira reef-biomass calculation over the surroundings of Utsira island. Realises the one-submodel ODD demonstrator `utsira_reef_biomass_demonstrator` and the canonical equation record `reef-biomass-equation`. Inputs and outputs are referenced by URI as standalone per-class input records and `experiment-output` records. The executable is a self-contained Python reproducibility script (`scripts/utsira_reef_biomass.py`)." ;
            dcterms:license "https://creativecommons.org/licenses/by/4.0/" ;
            dcterms:modified "2026-05-19" ;
            dcterms:title "Utsira surroundings — reef-biomass experiment" ;
            dcat:contactPoint [ dcat:hadRole "author" ;
                    seadots:name "Utsira biomass upscaler v1" ;
                    seadots:parameterSchemaaffiliation "SINTEF Ocean (SeaDOTs)" ] ;
            dcat:keyword "Python",
                "SeaDOTs",
                "Utsira",
                "experiment",
                "reef biomass",
                "surroundings" ;
            seadots:experiment [ dcterms:purpose "Evaluate the reef-biomass equation B_reef = sum_i (A_sub . D_pre,i . AF_i . C_t) for the surroundings of Utsira island under the Norwegian SES scenario. Inputs are the six per-class input records cited below; outputs are the three experiment-output records cited below." ;
                    seadots:application <file:///github/scripts/utsira_reef_biomass.py> ;
                    seadots:evidenceEquation <https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation> ;
                    seadots:execution [ dcterms:language "python" ;
                            seadots:entrypoint "python3 _sources/experiment/scripts/utsira_reef_biomass.py" ;
                            seadots:languageVersion ">=3.9" ;
                            seadots:reproducibility [ prov:wasGeneratedBy "PROV-O record emitted as one of the outputs" ;
                                    seadots:seedPolicy "deterministic — equation is closed-form, no stochastic submodels" ] ;
                            seadots:scheduling "single deterministic pass over taxon_groups (ODD processOverview.scheduling)" ] ;
                    seadots:input <https://example.org/norwegian-ses/area-of-interest/utsira-surroundings>,
                        <https://example.org/norwegian-ses/benthic-biomass-density-imr/ices-iva-fallback>,
                        <https://example.org/norwegian-ses/benthic-biomass-density-mareano/norwegian-shelf>,
                        <https://example.org/norwegian-ses/colonisation-time-factor/default-sigmoid>,
                        <https://example.org/norwegian-ses/floating-wind-infrastructure/utsira-nord-60x15mw>,
                        <https://example.org/norwegian-ses/reef-aggregation-index/degraer2020-bindings> ;
                    seadots:kind "computational" ;
                    seadots:modelledBy <https://w3id.org/ogc/hosted/seadots/odd-protocol/examples/utsira_reef_biomass_demonstrator> ;
                    seadots:output <https://example.org/norwegian-ses/experiment-output/prov-record>,
                        <https://example.org/norwegian-ses/experiment-output/reef-biomass-result>,
                        <https://example.org/norwegian-ses/experiment-output/stac-catalog> ;
                    seadots:parameter [ dcterms:title "Scenario start date",
                                "scenario_t0" ;
                            seadots:parameterSchema [ a seadots:string ;
                                    dcterms:format "date" ] ],
                        [ dcterms:description "Scientific names iterated by index i." ;
                            dcterms:title "TaxonGroup index values",
                                "taxon_groups" ;
                            skos:exactMatch <http://rs.tdwg.org/dwc/terms/scientificName> ;
                            seadots:parameterSchema [ a seadots:array ;
                                    seadots:items [ a seadots:string ] ] ],
                        [ dcterms:title "Months since installation",
                                "colonisation_months" ;
                            seadots:parameterSchema [ a seadots:integer ;
                                    seadots:minimum 0 ] ],
                        [ dcterms:description "Polygon delimiting the study area. Defaults to the surroundings of Utsira island." ;
                            dcterms:title "Area of interest",
                                "aoi" ;
                            skos:exactMatch <http://www.opengis.net/def/property/OGC/0/area-of-interest> ;
                            seadots:parameterSchema [ dcterms:format "application/geo+json" ] ] ;
                    seadots:successCriterion "B_reef_total > 0 and finite",
                        "Every TaxonGroup has either a MAREANO primary binding or an IMR fallback for every AOI cell; uncovered cells are flagged in PROV",
                        "PROV-O record resolves the equation record and the ODD record by URI",
                        "STAC catalog validates against the SeaDOTs EDITO output conventions" ] ;
            rec:format [ dcterms:format "application/geo+json" ],
                [ dcterms:format "application/json" ],
                [ dcterms:format "text/x-python" ] ;
            rec:language [ rec:languageCode "en" ] ;
            rec:themes [ rec:concept [ skos:prefLabel "Floating-wind reef effect" ;
                            rec:conceptID "reef-effect"^^xsd:string ],
                        [ skos:prefLabel "Computational experiment" ;
                            rec:conceptID "computational-experiment"^^xsd:string ] ;
                    rec:scheme "https://id3.seadots.eu/themes" ] ] .

<https://example.org/norwegian-ses/area-of-interest/utsira-surroundings> a <https://w3id.org/ogc/hosted/seadots/experiment#application/json> ;
    dcterms:title "AOI — surroundings of Utsira island" ;
    geojson:rel "https://w3id.org/ogc/hosted/seadots/experiment#input" .

<https://example.org/norwegian-ses/benthic-biomass-density-imr/ices-iva-fallback> a <https://w3id.org/ogc/hosted/seadots/experiment#application/json> ;
    dcterms:title "IMR benthic biomass baseline — fallback" ;
    geojson:rel "https://w3id.org/ogc/hosted/seadots/experiment#input" ;
    seadots:equationBinding "D_{pre,i}" .

<https://example.org/norwegian-ses/benthic-biomass-density-mareano/norwegian-shelf> a <https://w3id.org/ogc/hosted/seadots/experiment#application/json> ;
    dcterms:title "MAREANO benthic biomass density — primary baseline" ;
    geojson:rel "https://w3id.org/ogc/hosted/seadots/experiment#input" ;
    seadots:equationBinding "D_{pre,i}" .

<https://example.org/norwegian-ses/colonisation-time-factor/default-sigmoid> a <https://w3id.org/ogc/hosted/seadots/experiment#application/json> ;
    dcterms:title "Colonisation time factor" ;
    geojson:rel "https://w3id.org/ogc/hosted/seadots/experiment#input" ;
    seadots:equationBinding "C_t" .

<https://example.org/norwegian-ses/experiment-output/prov-record> a <https://w3id.org/ogc/hosted/seadots/experiment#application/json> ;
    dcterms:title "PROV-O provenance (JSON-LD)" ;
    geojson:rel "https://w3id.org/ogc/hosted/seadots/experiment#output" .

<https://example.org/norwegian-ses/experiment-output/reef-biomass-result> a <https://w3id.org/ogc/hosted/seadots/experiment#application/json> ;
    dcterms:title "Reef-associated biomass — structured result" ;
    geojson:rel "https://w3id.org/ogc/hosted/seadots/experiment#output" .

<https://example.org/norwegian-ses/experiment-output/stac-catalog> a <https://w3id.org/ogc/hosted/seadots/experiment#application/json> ;
    dcterms:title "STAC catalog for the run" ;
    geojson:rel "https://w3id.org/ogc/hosted/seadots/experiment#output" .

<https://example.org/norwegian-ses/floating-wind-infrastructure/utsira-nord-60x15mw> a <https://w3id.org/ogc/hosted/seadots/experiment#application/json> ;
    dcterms:title "Submerged infrastructure layout — Utsira Nord 60 × 15 MW" ;
    geojson:rel "https://w3id.org/ogc/hosted/seadots/experiment#input" ;
    seadots:equationBinding "A_{sub}" .

<https://example.org/norwegian-ses/reef-aggregation-index/degraer2020-bindings> a <https://w3id.org/ogc/hosted/seadots/experiment#application/json> ;
    dcterms:title "Reef aggregation index bindings" ;
    geojson:rel "https://w3id.org/ogc/hosted/seadots/experiment#input" ;
    seadots:equationBinding "AF_i" .

<file:///github/scripts/utsira_reef_biomass.py> a <https://w3id.org/ogc/hosted/seadots/experiment#text/x-python> ;
    dcterms:title "Utsira reef-biomass calculator (Python script)" ;
    geojson:rel "https://w3id.org/ogc/hosted/seadots/experiment#application" .

<https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation> dcterms:title "Reef-biomass equation — symbol table, bindings, provenance" ;
    geojson:rel "cite-as" .

<https://w3id.org/ogc/hosted/seadots/odd-protocol/examples/utsira_reef_biomass_demonstrator> dcterms:title "ODD record for the reef-biomass demonstrator" ;
    geojson:rel "describedby" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Computational Experiment
description: 'OGC API Records profile for a computational experiment realising a documented
  model. Extends GeoDCAT-Records with an `experiment` sub-object that points to the
  executable code (`application`) that runs the experiment, the documented model (`modelledBy`),
  the evidence equation (`evidenceEquation`), and standalone per-class input and `experiment-output`
  records referenced by URI.

  '
allOf:
- $ref: https://ogcincubator.github.io/geodcat-ogcapi-records/build/annotated/geo/geodcat/geodcat-records/schema.yaml
$defs:
  Link:
    type: object
    required:
    - href
    properties:
      href:
        type: string
        format: uri
        x-jsonld-id: '@id'
      rel:
        type: string
        x-jsonld-id: https://purl.org/geojson/vocab#rel
      type:
        type: string
        x-jsonld-id: '@type'
      title:
        type: string
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
        x-jsonld-id: '@id'
      rel:
        type: string
        x-jsonld-id: https://purl.org/geojson/vocab#rel
      type:
        type: string
        x-jsonld-id: '@type'
      title:
        type: string
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
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#equationBinding
properties:
  properties:
    type: object
    required:
    - experiment
    properties:
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
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#kind
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
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#application
            x-jsonld-type: '@id'
          modelledBy:
            $ref: '#/$defs/Link'
            description: Link to the model documentation (e.g. an ODD record) this
              experiment realises.
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#modelledBy
            x-jsonld-type: '@id'
          evidenceEquation:
            $ref: '#/$defs/Link'
            description: Link to an `equation-property-relationship` record carrying
              the symbol table.
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#evidenceEquation
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
                  x-jsonld-id: http://purl.org/dc/terms/title
                title:
                  type: string
                  x-jsonld-id: http://purl.org/dc/terms/title
                description:
                  type: string
                  x-jsonld-id: http://purl.org/dc/terms/description
                schema:
                  type: object
                  description: Inline JSON Schema fragment for the parameter value.
                  x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#parameterSchema
                vocabularyTerm:
                  type: string
                  format: uri
                  x-jsonld-id: http://www.w3.org/2004/02/skos/core#exactMatch
                  x-jsonld-type: '@id'
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#parameter
            x-jsonld-container: '@set'
          inputs:
            type: array
            description: 'References to per-class input records. Each entry MAY carry
              an `equationBinding` symbol. MUST NOT inline the input record itself.

              '
            items:
              $ref: '#/$defs/InputBinding'
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#input
            x-jsonld-container: '@set'
          outputs:
            type: array
            description: References to `experiment-output` records. MUST NOT be inlined.
            items:
              $ref: '#/$defs/Link'
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#output
            x-jsonld-type: '@id'
            x-jsonld-container: '@set'
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
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#languageVersion
              dependencies:
                type: array
                description: Runtime dependencies (e.g. PyPI packages with version
                  specs).
                items:
                  type: string
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#dependency
                x-jsonld-container: '@set'
              entrypoint:
                type: string
                description: 'Command line to invoke the application from the repository
                  root (e.g. `python3 _sources/experiment/scripts/foo.py`).

                  '
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#entrypoint
              scheduling:
                type: string
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#scheduling
              reproducibility:
                type: object
                properties:
                  seedPolicy:
                    type: string
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#seedPolicy
                  provenance:
                    type: string
                    x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#reproducibility
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#execution
          successCriteria:
            type: array
            items:
              type: string
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#successCriterion
            x-jsonld-container: '@set'
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#experiment
    x-jsonld-id: https://purl.org/geojson/vocab#properties
x-jsonld-extra-terms:
  id: '@id'
  geometry: https://purl.org/geojson/vocab#geometry
  coordinates: https://purl.org/geojson/vocab#coordinates
  Feature: https://purl.org/geojson/vocab#Feature
  Polygon: https://purl.org/geojson/vocab#Polygon
  bbox: https://purl.org/geojson/vocab#bbox
  links:
    x-jsonld-id: http://www.w3.org/ns/iana/link-relations/relation
    x-jsonld-container: '@set'
  mediaType: http://purl.org/dc/terms/format
  created: http://purl.org/dc/terms/created
  updated: http://purl.org/dc/terms/modified
  license: http://purl.org/dc/terms/license
  keywords:
    x-jsonld-id: http://www.w3.org/ns/dcat#keyword
    x-jsonld-container: '@set'
  themes:
    x-jsonld-id: http://www.w3.org/ns/dcat#theme
    x-jsonld-container: '@set'
  concepts:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#Concept
    x-jsonld-container: '@set'
  scheme: http://www.w3.org/2004/02/skos/core#inScheme
  label: http://www.w3.org/2004/02/skos/core#prefLabel
  formats:
    x-jsonld-id: http://purl.org/dc/terms/format
    x-jsonld-container: '@set'
  format: http://purl.org/dc/terms/format
  conformsTo:
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
    x-jsonld-container: '@set'
  contacts:
    x-jsonld-id: http://www.w3.org/ns/dcat#contactPoint
    x-jsonld-container: '@set'
  roles:
    x-jsonld-id: http://www.w3.org/ns/dcat#hadRole
    x-jsonld-container: '@set'
  organization: https://w3id.org/ogc/hosted/seadots/experiment#parameterSchemaaffiliation
  time: http://purl.org/dc/terms/temporal
  interval: http://purl.org/dc/terms/temporal
  resolution: http://www.w3.org/ns/dcat#temporalResolution
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/experiment#
x-jsonld-prefixes:
  seadots: https://w3id.org/ogc/hosted/seadots/experiment#
  dcterms: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#
  skos: http://www.w3.org/2004/02/skos/core#
  schema: https://w3id.org/ogc/hosted/seadots/experiment#parameterSchema
  prov: http://www.w3.org/ns/prov#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/experiment/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/experiment/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/experiment#",
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
    "properties": {
      "@context": {
        "experiment": {
          "@context": {
            "kind": "seadots:kind",
            "purpose": "dct:purpose",
            "application": {
              "@context": {
                "href": "@id",
                "rel": "geojson:rel"
              },
              "@id": "seadots:application",
              "@type": "@id"
            },
            "modelledBy": {
              "@context": {
                "href": "@id",
                "rel": "geojson:rel"
              },
              "@id": "seadots:modelledBy",
              "@type": "@id"
            },
            "evidenceEquation": {
              "@context": {
                "href": "@id",
                "rel": "geojson:rel"
              },
              "@id": "seadots:evidenceEquation",
              "@type": "@id"
            },
            "parameters": {
              "@context": {
                "name": "dct:title",
                "vocabularyTerm": {
                  "@id": "skos:exactMatch",
                  "@type": "@id"
                }
              },
              "@id": "seadots:parameter",
              "@container": "@set"
            },
            "inputs": {
              "@context": {
                "href": "@id",
                "rel": "geojson:rel",
                "equationBinding": "seadots:equationBinding"
              },
              "@id": "seadots:input",
              "@container": "@set"
            },
            "outputs": {
              "@context": {
                "href": "@id",
                "rel": "geojson:rel"
              },
              "@id": "seadots:output",
              "@type": "@id",
              "@container": "@set"
            },
            "execution": {
              "@context": {
                "language": "dct:language",
                "languageVersion": "seadots:languageVersion",
                "dependencies": {
                  "@id": "seadots:dependency",
                  "@container": "@set"
                },
                "entrypoint": "seadots:entrypoint",
                "scheduling": "seadots:scheduling",
                "reproducibility": {
                  "@context": {
                    "seedPolicy": "seadots:seedPolicy",
                    "provenance": "prov:wasGeneratedBy"
                  },
                  "@id": "seadots:reproducibility"
                }
              },
              "@id": "seadots:execution"
            },
            "successCriteria": {
              "@id": "seadots:successCriterion",
              "@container": "@set"
            }
          },
          "@id": "seadots:experiment"
        }
      },
      "@id": "geojson:properties"
    },
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
        "type": "dct:format",
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
    "coordinates": "geojson:coordinates",
    "mediaType": "dct:format",
    "concepts": {
      "@id": "skos:Concept",
      "@container": "@set"
    },
    "scheme": "skos:inScheme",
    "label": "skos:prefLabel",
    "format": "dct:format",
    "roles": {
      "@id": "dcat:hadRole",
      "@container": "@set"
    },
    "organization": "seadots:parameterSchemaaffiliation",
    "interval": "dct:temporal",
    "resolution": "dcat:temporalResolution",
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
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
    "seadots": "https://w3id.org/ogc/hosted/seadots/experiment#",
    "dcterms": "http://purl.org/dc/terms/",
    "schema": "seadots:parameterSchema",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/experiment/context.jsonld)

## Sources

* [GeoDCAT-Records](https://ogcincubator.github.io/geodcat-ogcapi-records/)
* [ODD Protocol Description Record bblock](https://w3id.org/ogc/hosted/seadots/odd-protocol)
* [Equation Property Relationship bblock](https://w3id.org/ogc/hosted/seadots/equation-property-relationship)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/experiment`

