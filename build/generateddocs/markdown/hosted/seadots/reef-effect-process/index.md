
# Reef Effect Process (Schema)

`ogc.hosted.seadots.reef-effect-process` *v0.1*

OGC API Processes Part 1 process description for the reef-effect biomass calculation, aligned with the OSPD pattern (ogc.osc.api-profiles.processes.ospd). Wraps the deterministic Python reproducibility script utsira_reef_biomass.py as an executable Process whose inputs are per-class SeaDOTs records (area-of-interest, floating-wind-infrastructure, benthic-biomass-density-mareano, benthic-biomass-density-imr, reef-aggregation-index, colonisation-time-factor) and whose output is a reef-effect-output record.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Reef Effect Process

OGC API Processes Part 1 process description for the reef-effect biomass calculation, aligned with the OSPD profile (`ogc.osc.api-profiles.processes.ospd`).

The block wraps the deterministic reproducibility script `_sources/reef-effect/scripts/utsira_reef_biomass.py` as an executable Process. Its inputs and outputs are typed by per-class SeaDOTs building blocks rather than primitive JSON Schemas, so the process is declaratively wired to the same records that the `reef-effect` experiment record links by URI.

## Why a separate block

The `reef-effect` block is an OGC API Records profile that describes the experiment as a discoverable resource (purpose, ODD, equation, success criteria, inputs/outputs by URI). It is the descriptive record.

`reef-effect-process` is the executable counterpart: a process description that an OGC API Processes endpoint can serve at `GET /processes/utsira-reef-biomass` and that clients can invoke at `POST /processes/utsira-reef-biomass/execution`. The two blocks complement each other and the experiment Record SHOULD reference the process by URI once both are deployed.

## Composition

The schema is composed using upstream OGC API Processes building blocks (register `bblocks-ogcapi-processes`):

| Aspect | Source |
|---|---|
| Process summary (id, version, title, description, keywords, jobControlOptions, outputTransmission, links) | `bblocks://ogc.api.processes.v1.schemas.processSummary` |
| Each input description (title, description, minOccurs, maxOccurs, schema) | `bblocks://ogc.api.processes.v1.schemas.inputDescription` |
| Each output description (title, description, schema) | `bblocks://ogc.api.processes.v1.schemas.outputDescription` |

Following the OSPD `buffer-geometry` pattern, every input/output `schema` is a `bblocks://` reference to the JSON Schema of the corresponding per-class record:

| Input id | Equation symbol | Bound to bblock |
|---|---|---|
| `aoi` | — | `ogc.hosted.seadots.area-of-interest` |
| `infrastructure` | A_sub | `ogc.hosted.seadots.floating-wind-infrastructure` |
| `benthicBiomassPrimary` | D_pre,i | `ogc.hosted.seadots.benthic-biomass-density-mareano` |
| `benthicBiomassFallback` | D_pre,i (fallback) | `ogc.hosted.seadots.benthic-biomass-density-imr` |
| `reefAggregationIndex` | AF_i | `ogc.hosted.seadots.reef-aggregation-index` |
| `colonisationTimeFactor` | C_t | `ogc.hosted.seadots.colonisation-time-factor` |
| `asOfMonths` | t | inline scalar (integer, default 24) |

| Output id | Bound to bblock |
|---|---|
| `reefBiomassResult` | `ogc.hosted.seadots.reef-effect-output` |
| `provenance` | inline `application/ld+json` PROV-O record |

## Execution unit

The `executionUnit` link in the process description points at the script:

```
_sources/reef-effect/scripts/utsira_reef_biomass.py
```

with `type: text/x-python`. The example process description declares `language: python`, `languageVersion: ">=3.9"`, and the exact `entrypoint` command. The script is deterministic (closed-form equation), so `reproducibility.seedPolicy: deterministic`.

## What the process emits

Successful execution produces a `reef-effect-output` record carrying:

- `headline.B_reef_kg`, `sigma_kg`, `CV`, 95% CI;
- `perTaxonAtT24` — per-taxon contributions;
- `timeSeries` — B_reef at the C(t) lookup points;
- `uncertainty.varianceAttribution` — share of CV² across A_sub, C_t, S=Σ(D·AF).

The `provenance` output is a PROV-O record linking the run to the six per-class input records, the equation record, and the ODD record by URI.

## Examples

- `examples/utsira_reef_biomass_process.json` — the **process description** document (validated against this bblock's schema).
- `examples/utsira_reef_biomass_execute.json` — a **matching Execute request body** for `POST /processes/utsira-reef-biomass/execution`. It conforms to OGC API Processes `execute.yaml`, not to this bblock's schema, so it is shipped as documentation only and is not validated here. A future companion bblock (mirroring `ogc.osc.api-profiles.processes.ipt.execute`) can wrap it as a schema.

## Examples

### Utsira reef-biomass process description
#### json
```json
{
  "id": "utsira-reef-biomass",
  "version": "0.1.0",
  "title": "Utsira reef-biomass calculator",
  "description": "Deterministic computation of reef-associated biomass B_reef(t) = sum_i (A_sub * D_pre,i * AF_i * C_t) for the surroundings of Utsira island, with log-linear CV uncertainty propagation. Inputs are per-class SeaDOTs records; the output is a reef-effect-output record plus a PROV-O provenance document. Realises the ODD demonstrator utsira_reef_biomass_demonstrator and cites the canonical reef-biomass equation record.",
  "keywords": [
    "reef-effect",
    "Utsira",
    "reef biomass",
    "ogcapi-processes",
    "ospd",
    "SeaDOTs",
    "deterministic"
  ],
  "metadata": [
    {
      "role": "https://www.opengis.net/def/metadata-role/ogcapi-processes/ospd",
      "title": "Aligned with the OSPD profile (ogc.osc.api-profiles.processes.ospd)",
      "href": "https://ogcincubator.github.io/bblocks-openscience/bblock/ogc.osc.api-profiles.processes.ospd"
    },
    {
      "role": "http://www.w3.org/ns/dcat#theme",
      "title": "Floating-wind reef effect",
      "href": "https://id3.seadots.eu/themes/reef-effect"
    }
  ],
  "jobControlOptions": ["sync-execute", "async-execute"],
  "outputTransmission": ["value", "reference"],
  "inputs": {
    "aoi": {
      "title": "Area of interest",
      "description": "Polygon delimiting the study area. Defaults to the surroundings of Utsira island.",
      "minOccurs": 1,
      "maxOccurs": 1,
      "schema": {
        "$ref": "https://w3id.org/ogc/hosted/seadots/area-of-interest/schema.json",
        "contentMediaType": "application/json"
      }
    },
    "infrastructure": {
      "title": "Floating wind infrastructure",
      "description": "Submerged-area description bound to the equation symbol A_sub.",
      "minOccurs": 1,
      "maxOccurs": 1,
      "schema": {
        "$ref": "https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure/schema.json",
        "contentMediaType": "application/json"
      },
      "additionalParameters": {
        "parameters": [
          { "name": "equationBinding", "value": ["A_{sub}"] }
        ]
      }
    },
    "benthicBiomassPrimary": {
      "title": "Primary benthic biomass density (MAREANO)",
      "description": "Per-taxon pre-existing density bound to the equation symbol D_pre,i.",
      "minOccurs": 1,
      "maxOccurs": 1,
      "schema": {
        "$ref": "https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano/schema.json",
        "contentMediaType": "application/json"
      },
      "additionalParameters": {
        "parameters": [
          { "name": "equationBinding", "value": ["D_{pre,i}"] }
        ]
      }
    },
    "benthicBiomassFallback": {
      "title": "Fallback benthic biomass density (IMR)",
      "description": "Fallback baseline used where the primary baseline has no coverage; also supplies sigma_kg_m2 for uncertainty propagation.",
      "minOccurs": 0,
      "maxOccurs": 1,
      "schema": {
        "$ref": "https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr/schema.json",
        "contentMediaType": "application/json"
      },
      "additionalParameters": {
        "parameters": [
          { "name": "equationBinding", "value": ["D_{pre,i}"] }
        ]
      }
    },
    "reefAggregationIndex": {
      "title": "Reef aggregation index",
      "description": "Per-taxon AF_i bindings.",
      "minOccurs": 1,
      "maxOccurs": 1,
      "schema": {
        "$ref": "https://w3id.org/ogc/hosted/seadots/reef-aggregation-index/schema.json",
        "contentMediaType": "application/json"
      },
      "additionalParameters": {
        "parameters": [
          { "name": "equationBinding", "value": ["AF_i"] }
        ]
      }
    },
    "colonisationTimeFactor": {
      "title": "Colonisation time factor",
      "description": "Sigmoid parameters L, k, t0 (months); evaluated to C_t for the equation.",
      "minOccurs": 1,
      "maxOccurs": 1,
      "schema": {
        "$ref": "https://w3id.org/ogc/hosted/seadots/colonisation-time-factor/schema.json",
        "contentMediaType": "application/json"
      },
      "additionalParameters": {
        "parameters": [
          { "name": "equationBinding", "value": ["C_t"] }
        ]
      }
    },
    "asOfMonths": {
      "title": "Evaluation time (months since installation)",
      "description": "Scalar t in C(t); defaults to 24 months in the worked example.",
      "minOccurs": 0,
      "maxOccurs": 1,
      "schema": {
        "type": "integer",
        "minimum": 0,
        "default": 24
      }
    }
  },
  "outputs": {
    "reefBiomassResult": {
      "title": "Reef-associated biomass — structured result",
      "description": "Reef-effect-output record carrying headline B_reef(t), per-taxon contributions, time series, and uncertainty propagation.",
      "schema": {
        "$ref": "https://w3id.org/ogc/hosted/seadots/reef-effect-output/schema.json",
        "contentMediaType": "application/json"
      }
    },
    "provenance": {
      "title": "PROV-O provenance (JSON-LD)",
      "description": "PROV-O record linking the run to its six input records, the equation record, and the ODD record.",
      "schema": {
        "type": "object",
        "contentMediaType": "application/ld+json"
      }
    }
  },
  "links": [
    {
      "rel": "execute",
      "href": "https://example.org/norwegian-ses/processes/utsira-reef-biomass/execution",
      "type": "application/json",
      "title": "Execute endpoint"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/execution-unit",
      "href": "../../reef-effect/scripts/utsira_reef_biomass.py",
      "type": "text/x-python",
      "title": "Python reproducibility script (executionUnit)"
    },
    {
      "rel": "describedby",
      "href": "https://w3id.org/ogc/hosted/seadots/odd-protocol/examples/utsira_reef_biomass_demonstrator",
      "type": "application/json",
      "title": "ODD demonstrator realised by this process"
    },
    {
      "rel": "cite-as",
      "href": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
      "type": "application/ld+json",
      "title": "Reef-biomass equation record"
    },
    {
      "rel": "related",
      "href": "https://w3id.org/ogc/hosted/seadots/reef-effect/examples/utsira_surroundings_experiment",
      "type": "application/geo+json",
      "title": "Experiment record (OGC API Records) that realises this process"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/conformance",
      "href": "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/core",
      "title": "OGC API - Processes - Part 1: Core"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/reef-effect-process/context.jsonld",
  "id": "utsira-reef-biomass",
  "version": "0.1.0",
  "title": "Utsira reef-biomass calculator",
  "description": "Deterministic computation of reef-associated biomass B_reef(t) = sum_i (A_sub * D_pre,i * AF_i * C_t) for the surroundings of Utsira island, with log-linear CV uncertainty propagation. Inputs are per-class SeaDOTs records; the output is a reef-effect-output record plus a PROV-O provenance document. Realises the ODD demonstrator utsira_reef_biomass_demonstrator and cites the canonical reef-biomass equation record.",
  "keywords": [
    "reef-effect",
    "Utsira",
    "reef biomass",
    "ogcapi-processes",
    "ospd",
    "SeaDOTs",
    "deterministic"
  ],
  "metadata": [
    {
      "role": "https://www.opengis.net/def/metadata-role/ogcapi-processes/ospd",
      "title": "Aligned with the OSPD profile (ogc.osc.api-profiles.processes.ospd)",
      "href": "https://ogcincubator.github.io/bblocks-openscience/bblock/ogc.osc.api-profiles.processes.ospd"
    },
    {
      "role": "http://www.w3.org/ns/dcat#theme",
      "title": "Floating-wind reef effect",
      "href": "https://id3.seadots.eu/themes/reef-effect"
    }
  ],
  "jobControlOptions": [
    "sync-execute",
    "async-execute"
  ],
  "outputTransmission": [
    "value",
    "reference"
  ],
  "inputs": {
    "aoi": {
      "title": "Area of interest",
      "description": "Polygon delimiting the study area. Defaults to the surroundings of Utsira island.",
      "minOccurs": 1,
      "maxOccurs": 1,
      "schema": {
        "$ref": "https://w3id.org/ogc/hosted/seadots/area-of-interest/schema.json",
        "contentMediaType": "application/json"
      }
    },
    "infrastructure": {
      "title": "Floating wind infrastructure",
      "description": "Submerged-area description bound to the equation symbol A_sub.",
      "minOccurs": 1,
      "maxOccurs": 1,
      "schema": {
        "$ref": "https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure/schema.json",
        "contentMediaType": "application/json"
      },
      "additionalParameters": {
        "parameters": [
          {
            "name": "equationBinding",
            "value": [
              "A_{sub}"
            ]
          }
        ]
      }
    },
    "benthicBiomassPrimary": {
      "title": "Primary benthic biomass density (MAREANO)",
      "description": "Per-taxon pre-existing density bound to the equation symbol D_pre,i.",
      "minOccurs": 1,
      "maxOccurs": 1,
      "schema": {
        "$ref": "https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano/schema.json",
        "contentMediaType": "application/json"
      },
      "additionalParameters": {
        "parameters": [
          {
            "name": "equationBinding",
            "value": [
              "D_{pre,i}"
            ]
          }
        ]
      }
    },
    "benthicBiomassFallback": {
      "title": "Fallback benthic biomass density (IMR)",
      "description": "Fallback baseline used where the primary baseline has no coverage; also supplies sigma_kg_m2 for uncertainty propagation.",
      "minOccurs": 0,
      "maxOccurs": 1,
      "schema": {
        "$ref": "https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr/schema.json",
        "contentMediaType": "application/json"
      },
      "additionalParameters": {
        "parameters": [
          {
            "name": "equationBinding",
            "value": [
              "D_{pre,i}"
            ]
          }
        ]
      }
    },
    "reefAggregationIndex": {
      "title": "Reef aggregation index",
      "description": "Per-taxon AF_i bindings.",
      "minOccurs": 1,
      "maxOccurs": 1,
      "schema": {
        "$ref": "https://w3id.org/ogc/hosted/seadots/reef-aggregation-index/schema.json",
        "contentMediaType": "application/json"
      },
      "additionalParameters": {
        "parameters": [
          {
            "name": "equationBinding",
            "value": [
              "AF_i"
            ]
          }
        ]
      }
    },
    "colonisationTimeFactor": {
      "title": "Colonisation time factor",
      "description": "Sigmoid parameters L, k, t0 (months); evaluated to C_t for the equation.",
      "minOccurs": 1,
      "maxOccurs": 1,
      "schema": {
        "$ref": "https://w3id.org/ogc/hosted/seadots/colonisation-time-factor/schema.json",
        "contentMediaType": "application/json"
      },
      "additionalParameters": {
        "parameters": [
          {
            "name": "equationBinding",
            "value": [
              "C_t"
            ]
          }
        ]
      }
    },
    "asOfMonths": {
      "title": "Evaluation time (months since installation)",
      "description": "Scalar t in C(t); defaults to 24 months in the worked example.",
      "minOccurs": 0,
      "maxOccurs": 1,
      "schema": {
        "type": "integer",
        "minimum": 0,
        "default": 24
      }
    }
  },
  "outputs": {
    "reefBiomassResult": {
      "title": "Reef-associated biomass \u2014 structured result",
      "description": "Reef-effect-output record carrying headline B_reef(t), per-taxon contributions, time series, and uncertainty propagation.",
      "schema": {
        "$ref": "https://w3id.org/ogc/hosted/seadots/reef-effect-output/schema.json",
        "contentMediaType": "application/json"
      }
    },
    "provenance": {
      "title": "PROV-O provenance (JSON-LD)",
      "description": "PROV-O record linking the run to its six input records, the equation record, and the ODD record.",
      "schema": {
        "type": "object",
        "contentMediaType": "application/ld+json"
      }
    }
  },
  "links": [
    {
      "rel": "execute",
      "href": "https://example.org/norwegian-ses/processes/utsira-reef-biomass/execution",
      "type": "application/json",
      "title": "Execute endpoint"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/execution-unit",
      "href": "../../reef-effect/scripts/utsira_reef_biomass.py",
      "type": "text/x-python",
      "title": "Python reproducibility script (executionUnit)"
    },
    {
      "rel": "describedby",
      "href": "https://w3id.org/ogc/hosted/seadots/odd-protocol/examples/utsira_reef_biomass_demonstrator",
      "type": "application/json",
      "title": "ODD demonstrator realised by this process"
    },
    {
      "rel": "cite-as",
      "href": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
      "type": "application/ld+json",
      "title": "Reef-biomass equation record"
    },
    {
      "rel": "related",
      "href": "https://w3id.org/ogc/hosted/seadots/reef-effect/examples/utsira_surroundings_experiment",
      "type": "application/geo+json",
      "title": "Experiment record (OGC API Records) that realises this process"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/conformance",
      "href": "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/core",
      "title": "OGC API - Processes - Part 1: Core"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.w3.org/ns/iana/link-relations/> .
@prefix ns2: <https://purl.org/geojson/vocab#> .
@prefix ogcapi-proc: <http://www.opengis.net/def/ogcapi-processes/1.0/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/reef-effect-process#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///reef-effect/scripts/utsira_reef_biomass.py> dct:format "text/x-python" ;
    dct:title "Python reproducibility script (executionUnit)" ;
    ns2:rel "http://www.opengis.net/def/rel/ogc/1.0/execution-unit" .

<http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/core> dct:title "OGC API - Processes - Part 1: Core" ;
    ns2:rel "http://www.opengis.net/def/rel/ogc/1.0/conformance" .

<https://example.org/norwegian-ses/processes/utsira-reef-biomass/execution> dct:format "application/json" ;
    dct:title "Execute endpoint" ;
    ns2:rel "execute" .

<https://id3.seadots.eu/themes/reef-effect> dct:title "Floating-wind reef effect" ;
    seadots:role "http://www.w3.org/ns/dcat#theme" .

<https://ogcincubator.github.io/bblocks-openscience/bblock/ogc.osc.api-profiles.processes.ospd> dct:title "Aligned with the OSPD profile (ogc.osc.api-profiles.processes.ospd)" ;
    seadots:role "https://www.opengis.net/def/metadata-role/ogcapi-processes/ospd" .

<https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation> dct:format "application/ld+json" ;
    dct:title "Reef-biomass equation record" ;
    ns2:rel "cite-as" .

<https://w3id.org/ogc/hosted/seadots/odd-protocol/examples/utsira_reef_biomass_demonstrator> dct:format "application/json" ;
    dct:title "ODD demonstrator realised by this process" ;
    ns2:rel "describedby" .

<https://w3id.org/ogc/hosted/seadots/reef-effect/examples/utsira_surroundings_experiment> dct:format "application/geo+json" ;
    dct:title "Experiment record (OGC API Records) that realises this process" ;
    ns2:rel "related" .

[] dct:description "Deterministic computation of reef-associated biomass B_reef(t) = sum_i (A_sub * D_pre,i * AF_i * C_t) for the surroundings of Utsira island, with log-linear CV uncertainty propagation. Inputs are per-class SeaDOTs records; the output is a reef-effect-output record plus a PROV-O provenance document. Realises the ODD demonstrator utsira_reef_biomass_demonstrator and cites the canonical reef-biomass equation record." ;
    dct:hasVersion "0.1.0" ;
    dct:source <https://id3.seadots.eu/themes/reef-effect>,
        <https://ogcincubator.github.io/bblocks-openscience/bblock/ogc.osc.api-profiles.processes.ospd> ;
    dct:title "Utsira reef-biomass calculator" ;
    ogcapi-proc:id "utsira-reef-biomass" ;
    ogcapi-proc:input [ dct:conformsTo [ dct:format "integer" ;
                    proc:default "24"^^rdf:JSON ;
                    seadots:minimum 0 ] ;
            dct:description "Scalar t in C(t); defaults to 24 months in the worked example." ;
            dct:title "Evaluation time (months since installation)" ;
            proc:maxOccurs 1 ;
            proc:minOccurs 0 ],
        [ dct:conformsTo [ proc:ref <https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure/schema.json> ;
                    seadots:contentMediaType "application/json" ] ;
            dct:description "Submerged-area description bound to the equation symbol A_sub." ;
            dct:title "Floating wind infrastructure" ;
            ogcapi-proc:additionalParameters [ seadots:parameters [ seadots:name "equationBinding" ;
                            seadots:value "A_{sub}" ] ] ;
            proc:maxOccurs 1 ;
            proc:minOccurs 1 ],
        [ dct:conformsTo [ proc:ref <https://w3id.org/ogc/hosted/seadots/reef-aggregation-index/schema.json> ;
                    seadots:contentMediaType "application/json" ] ;
            dct:description "Per-taxon AF_i bindings." ;
            dct:title "Reef aggregation index" ;
            ogcapi-proc:additionalParameters [ seadots:parameters [ seadots:name "equationBinding" ;
                            seadots:value "AF_i" ] ] ;
            proc:maxOccurs 1 ;
            proc:minOccurs 1 ],
        [ dct:conformsTo [ proc:ref <https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr/schema.json> ;
                    seadots:contentMediaType "application/json" ] ;
            dct:description "Fallback baseline used where the primary baseline has no coverage; also supplies sigma_kg_m2 for uncertainty propagation." ;
            dct:title "Fallback benthic biomass density (IMR)" ;
            ogcapi-proc:additionalParameters [ seadots:parameters [ seadots:name "equationBinding" ;
                            seadots:value "D_{pre,i}" ] ] ;
            proc:maxOccurs 1 ;
            proc:minOccurs 0 ],
        [ dct:conformsTo [ proc:ref <https://w3id.org/ogc/hosted/seadots/colonisation-time-factor/schema.json> ;
                    seadots:contentMediaType "application/json" ] ;
            dct:description "Sigmoid parameters L, k, t0 (months); evaluated to C_t for the equation." ;
            dct:title "Colonisation time factor" ;
            ogcapi-proc:additionalParameters [ seadots:parameters [ seadots:name "equationBinding" ;
                            seadots:value "C_t" ] ] ;
            proc:maxOccurs 1 ;
            proc:minOccurs 1 ],
        [ dct:conformsTo [ proc:ref <https://w3id.org/ogc/hosted/seadots/area-of-interest/schema.json> ;
                    seadots:contentMediaType "application/json" ] ;
            dct:description "Polygon delimiting the study area. Defaults to the surroundings of Utsira island." ;
            dct:title "Area of interest" ;
            proc:maxOccurs 1 ;
            proc:minOccurs 1 ],
        [ dct:conformsTo [ proc:ref <https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano/schema.json> ;
                    seadots:contentMediaType "application/json" ] ;
            dct:description "Per-taxon pre-existing density bound to the equation symbol D_pre,i." ;
            dct:title "Primary benthic biomass density (MAREANO)" ;
            ogcapi-proc:additionalParameters [ seadots:parameters [ seadots:name "equationBinding" ;
                            seadots:value "D_{pre,i}" ] ] ;
            proc:maxOccurs 1 ;
            proc:minOccurs 1 ] ;
    ogcapi-proc:jobControlOptions "async-execute",
        "sync-execute" ;
    ogcapi-proc:output [ dct:conformsTo [ dct:format "object" ;
                    seadots:contentMediaType "application/ld+json" ] ;
            dct:description "PROV-O record linking the run to its six input records, the equation record, and the ODD record." ;
            dct:title "PROV-O provenance (JSON-LD)" ],
        [ dct:conformsTo [ proc:ref <https://w3id.org/ogc/hosted/seadots/reef-effect-output/schema.json> ;
                    seadots:contentMediaType "application/json" ] ;
            dct:description "Reef-effect-output record carrying headline B_reef(t), per-taxon contributions, time series, and uncertainty propagation." ;
            dct:title "Reef-associated biomass — structured result" ] ;
    ogcapi-proc:outputTransmission "reference",
        "value" ;
    dcat:keyword "SeaDOTs",
        "Utsira",
        "deterministic",
        "ogcapi-processes",
        "ospd",
        "reef biomass",
        "reef-effect" ;
    ns1:relation <file:///reef-effect/scripts/utsira_reef_biomass.py>,
        <http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/core>,
        <https://example.org/norwegian-ses/processes/utsira-reef-biomass/execution>,
        <https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation>,
        <https://w3id.org/ogc/hosted/seadots/odd-protocol/examples/utsira_reef_biomass_demonstrator>,
        <https://w3id.org/ogc/hosted/seadots/reef-effect/examples/utsira_surroundings_experiment> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Reef Effect Process
description: 'OGC API Processes - Part 1 process description for the reef-effect biomass
  calculation. Composed from the upstream `processSummary`, `inputDescription` and
  `outputDescription` building blocks (register `bblocks-ogcapi-processes`) and aligned
  with the OSPD profile (`ogc.osc.api-profiles.processes.ospd`). Each declared input/output
  is expected to carry a JSON Schema document (via the standard OGC API Processes
  `schema` slot) pointing at the corresponding per-class SeaDOTs building block; the
  per-class wiring is captured by `dependsOn` at the bblock level and by the `$ref`
  URLs in the example. This bblock does not re-constrain the `schema` slot beyond
  what the upstream `inputDescription`/ `outputDescription` schemas already mandate.

  '
allOf:
- $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/processSummary/schema.yaml
- type: object
  required:
  - inputs
  - outputs
  properties:
    inputs:
      type: object
      description: 'Input descriptions for the reef-effect process. Keys are the input
        identifiers used in the `Execute` request `inputs` object.

        '
      additionalProperties: false
      required:
      - aoi
      - infrastructure
      - benthicBiomassPrimary
      - reefAggregationIndex
      - colonisationTimeFactor
      properties:
        aoi:
          allOf:
          - $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/inputDescription/schema.yaml
          - type: object
            properties:
              title:
                type: string
                const: Area of interest
                x-jsonld-id: http://purl.org/dc/terms/title
              description:
                type: string
                x-jsonld-id: http://purl.org/dc/terms/description
              minOccurs:
                type: integer
                const: 1
                x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/minOccurs
              maxOccurs:
                type: integer
                const: 1
                x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/maxOccurs
        infrastructure:
          allOf:
          - $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/inputDescription/schema.yaml
          - type: object
            properties:
              title:
                type: string
                const: Floating wind infrastructure
                x-jsonld-id: http://purl.org/dc/terms/title
              description:
                type: string
                x-jsonld-id: http://purl.org/dc/terms/description
              minOccurs:
                type: integer
                const: 1
                x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/minOccurs
              maxOccurs:
                type: integer
                const: 1
                x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/maxOccurs
        benthicBiomassPrimary:
          allOf:
          - $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/inputDescription/schema.yaml
          - type: object
            properties:
              title:
                type: string
                const: Primary benthic biomass density (MAREANO)
                x-jsonld-id: http://purl.org/dc/terms/title
              description:
                type: string
                x-jsonld-id: http://purl.org/dc/terms/description
              minOccurs:
                type: integer
                const: 1
                x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/minOccurs
              maxOccurs:
                type: integer
                const: 1
                x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/maxOccurs
        benthicBiomassFallback:
          allOf:
          - $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/inputDescription/schema.yaml
          - type: object
            properties:
              title:
                type: string
                const: Fallback benthic biomass density (IMR)
                x-jsonld-id: http://purl.org/dc/terms/title
              description:
                type: string
                x-jsonld-id: http://purl.org/dc/terms/description
              minOccurs:
                type: integer
                const: 0
                x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/minOccurs
              maxOccurs:
                type: integer
                const: 1
                x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/maxOccurs
        reefAggregationIndex:
          allOf:
          - $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/inputDescription/schema.yaml
          - type: object
            properties:
              title:
                type: string
                const: Reef aggregation index
                x-jsonld-id: http://purl.org/dc/terms/title
              description:
                type: string
                x-jsonld-id: http://purl.org/dc/terms/description
              minOccurs:
                type: integer
                const: 1
                x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/minOccurs
              maxOccurs:
                type: integer
                const: 1
                x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/maxOccurs
        colonisationTimeFactor:
          allOf:
          - $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/inputDescription/schema.yaml
          - type: object
            properties:
              title:
                type: string
                const: Colonisation time factor
                x-jsonld-id: http://purl.org/dc/terms/title
              description:
                type: string
                x-jsonld-id: http://purl.org/dc/terms/description
              minOccurs:
                type: integer
                const: 1
                x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/minOccurs
              maxOccurs:
                type: integer
                const: 1
                x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/maxOccurs
        asOfMonths:
          allOf:
          - $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/inputDescription/schema.yaml
          - type: object
            properties:
              title:
                type: string
                const: Evaluation time (months since installation)
                x-jsonld-id: http://purl.org/dc/terms/title
              description:
                type: string
                x-jsonld-id: http://purl.org/dc/terms/description
              minOccurs:
                type: integer
                const: 0
                x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/minOccurs
              maxOccurs:
                type: integer
                const: 1
                x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/maxOccurs
      x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/input
      x-jsonld-container: '@index'
    outputs:
      type: object
      description: 'Output descriptions. The canonical structured result is a reef-effect-output
        record carrying B_reef(t), per-taxon contributions, time series, and uncertainty
        propagation.

        '
      additionalProperties: false
      required:
      - reefBiomassResult
      properties:
        reefBiomassResult:
          allOf:
          - $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/outputDescription/schema.yaml
          - type: object
            properties:
              title:
                type: string
                const: "Reef-associated biomass \u2014 structured result"
                x-jsonld-id: http://purl.org/dc/terms/title
              description:
                type: string
                x-jsonld-id: http://purl.org/dc/terms/description
        provenance:
          allOf:
          - $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/outputDescription/schema.yaml
          - type: object
            properties:
              title:
                type: string
                const: PROV-O provenance (JSON-LD)
                x-jsonld-id: http://purl.org/dc/terms/title
              description:
                type: string
                x-jsonld-id: http://purl.org/dc/terms/description
          x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
      x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/output
      x-jsonld-container: '@index'
x-jsonld-extra-terms:
  id: http://www.opengis.net/def/ogcapi-processes/1.0/id
  version: http://purl.org/dc/terms/hasVersion
  keywords:
    x-jsonld-id: http://www.w3.org/ns/dcat#keyword
    x-jsonld-container: '@set'
  metadata:
    x-jsonld-id: http://purl.org/dc/terms/source
    x-jsonld-container: '@set'
  additionalParameters: http://www.opengis.net/def/ogcapi-processes/1.0/additionalParameters
  jobControlOptions:
    x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/jobControlOptions
    x-jsonld-container: '@set'
  outputTransmission:
    x-jsonld-id: http://www.opengis.net/def/ogcapi-processes/1.0/outputTransmission
    x-jsonld-container: '@set'
  links:
    x-jsonld-id: http://www.w3.org/ns/iana/link-relations/relation
    x-jsonld-container: '@set'
  href: '@id'
  rel: https://purl.org/geojson/vocab#rel
  type: http://purl.org/dc/terms/format
  mediaType: http://purl.org/dc/terms/format
  executionUnit:
    x-jsonld-id: http://purl.org/dc/terms/conformsTosoftwareSourceCode
    x-jsonld-type: '@id'
  language: http://purl.org/dc/terms/language
  languageVersion: http://purl.org/dc/terms/conformsToruntimePlatform
  dependencies:
    x-jsonld-id: http://purl.org/dc/terms/conformsTosoftwareRequirements
    x-jsonld-container: '@set'
  entrypoint: http://purl.org/dc/terms/conformsTopotentialAction
  reproducibility: https://w3id.org/ogc/hosted/seadots/reef-effect-process#reproducibility
  seedPolicy: https://w3id.org/ogc/hosted/seadots/reef-effect-process#seedPolicy
  modelledBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasInformedBy
    x-jsonld-type: '@id'
  evidenceEquation:
    x-jsonld-id: http://www.w3.org/ns/prov#hadPlan
    x-jsonld-type: '@id'
  conformsTo:
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
    x-jsonld-container: '@set'
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/reef-effect-process#
x-jsonld-prefixes:
  dcterms: http://purl.org/dc/terms/
  ogcapi-proc: http://www.opengis.net/def/ogcapi-processes/1.0/
  dcat: http://www.w3.org/ns/dcat#
  schema: http://purl.org/dc/terms/conformsTo
  seadots: https://w3id.org/ogc/hosted/seadots/reef-effect-process#
  prov: http://www.w3.org/ns/prov#
  skos: http://www.w3.org/2004/02/skos/core#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/reef-effect-process/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/reef-effect-process/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/reef-effect-process#",
    "inputs": {
      "@context": {
        "aoi": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/processes/",
            "maxOccurs": "ogcapi-proc:maxOccurs",
            "minOccurs": "ogcapi-proc:minOccurs",
            "schema": {
              "@context": {
                "@vocab": "https://w3id.org/ogc/api/schema/"
              },
              "@id": "proc:schema"
            },
            "keywords": "proc:keywords",
            "type": "proc:type"
          }
        },
        "infrastructure": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/processes/",
            "maxOccurs": "ogcapi-proc:maxOccurs",
            "minOccurs": "ogcapi-proc:minOccurs",
            "schema": {
              "@context": {
                "@vocab": "https://w3id.org/ogc/api/schema/"
              },
              "@id": "proc:schema"
            },
            "keywords": "proc:keywords",
            "type": "proc:type"
          }
        },
        "benthicBiomassPrimary": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/processes/",
            "maxOccurs": "ogcapi-proc:maxOccurs",
            "minOccurs": "ogcapi-proc:minOccurs",
            "schema": {
              "@context": {
                "@vocab": "https://w3id.org/ogc/api/schema/"
              },
              "@id": "proc:schema"
            },
            "keywords": "proc:keywords",
            "type": "proc:type"
          }
        },
        "benthicBiomassFallback": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/processes/",
            "maxOccurs": "ogcapi-proc:maxOccurs",
            "minOccurs": "ogcapi-proc:minOccurs",
            "schema": {
              "@context": {
                "@vocab": "https://w3id.org/ogc/api/schema/"
              },
              "@id": "proc:schema"
            },
            "keywords": "proc:keywords",
            "type": "proc:type"
          }
        },
        "reefAggregationIndex": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/processes/",
            "maxOccurs": "ogcapi-proc:maxOccurs",
            "minOccurs": "ogcapi-proc:minOccurs",
            "schema": {
              "@context": {
                "@vocab": "https://w3id.org/ogc/api/schema/"
              },
              "@id": "proc:schema"
            },
            "keywords": "proc:keywords",
            "type": "proc:type"
          }
        },
        "colonisationTimeFactor": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/processes/",
            "maxOccurs": "ogcapi-proc:maxOccurs",
            "minOccurs": "ogcapi-proc:minOccurs",
            "schema": {
              "@context": {
                "@vocab": "https://w3id.org/ogc/api/schema/"
              },
              "@id": "proc:schema"
            },
            "keywords": "proc:keywords",
            "type": "proc:type"
          }
        },
        "asOfMonths": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/processes/",
            "maxOccurs": "ogcapi-proc:maxOccurs",
            "minOccurs": "ogcapi-proc:minOccurs",
            "schema": {
              "@context": {
                "@vocab": "https://w3id.org/ogc/api/schema/"
              },
              "@id": "proc:schema"
            },
            "keywords": "proc:keywords",
            "type": "proc:type"
          }
        }
      },
      "@id": "ogcapi-proc:input",
      "@container": "@index"
    },
    "outputs": {
      "@context": {
        "reefBiomassResult": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/processes/",
            "schema": {
              "@context": {
                "@vocab": "https://w3id.org/ogc/api/schema/"
              },
              "@id": "proc:schema"
            },
            "keywords": "proc:keywords",
            "type": "proc:type"
          }
        },
        "provenance": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/processes/",
            "schema": {
              "@context": {
                "@vocab": "https://w3id.org/ogc/api/schema/"
              },
              "@id": "proc:schema"
            },
            "keywords": "proc:keywords",
            "type": "proc:type"
          },
          "@id": "prov:wasGeneratedBy"
        }
      },
      "@id": "ogcapi-proc:output",
      "@container": "@index"
    },
    "id": "ogcapi-proc:id",
    "version": "dcterms:hasVersion",
    "keywords": {
      "@id": "dcat:keyword",
      "@container": "@set"
    },
    "metadata": {
      "@id": "dcterms:source",
      "@container": "@set"
    },
    "additionalParameters": "ogcapi-proc:additionalParameters",
    "jobControlOptions": {
      "@id": "ogcapi-proc:jobControlOptions",
      "@container": "@set"
    },
    "outputTransmission": {
      "@id": "ogcapi-proc:outputTransmission",
      "@container": "@set"
    },
    "links": {
      "@id": "http://www.w3.org/ns/iana/link-relations/relation",
      "@container": "@set"
    },
    "href": "@id",
    "rel": "https://purl.org/geojson/vocab#rel",
    "type": "dcterms:format",
    "mediaType": "dcterms:format",
    "executionUnit": {
      "@id": "dcterms:conformsTosoftwareSourceCode",
      "@type": "@id"
    },
    "language": "dcterms:language",
    "languageVersion": "dcterms:conformsToruntimePlatform",
    "dependencies": {
      "@id": "dcterms:conformsTosoftwareRequirements",
      "@container": "@set"
    },
    "entrypoint": "dcterms:conformsTopotentialAction",
    "reproducibility": "seadots:reproducibility",
    "seedPolicy": "seadots:seedPolicy",
    "modelledBy": {
      "@id": "prov:wasInformedBy",
      "@type": "@id"
    },
    "evidenceEquation": {
      "@id": "prov:hadPlan",
      "@type": "@id"
    },
    "conformsTo": {
      "@id": "dcterms:conformsTo",
      "@type": "@id",
      "@container": "@set"
    },
    "title": "dcterms:title",
    "description": "dcterms:description",
    "nullable": "proc:nullable",
    "$ref": {
      "@id": "proc:ref",
      "@type": "@id"
    },
    "default": {
      "@id": "proc:default",
      "@type": "@json"
    },
    "enum": {
      "@id": "proc:enum",
      "@container": "@set"
    },
    "minOccurs": "proc:minOccurs",
    "maxOccurs": "proc:maxOccurs",
    "dcterms": "http://purl.org/dc/terms/",
    "ogcapi-proc": "http://www.opengis.net/def/ogcapi-processes/1.0/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "schema": "dcterms:conformsTo",
    "seadots": "https://w3id.org/ogc/hosted/seadots/reef-effect-process#",
    "prov": "http://www.w3.org/ns/prov#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dct": "http://purl.org/dc/terms/",
    "proc": "https://w3id.org/ogc/api/processes/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/reef-effect-process/context.jsonld)

## Sources

* [OGC API - Processes - Part 1: Core](https://docs.ogc.org/is/18-062r2/18-062r2.html)
* [OGC API Processes building blocks register](https://ogcincubator.github.io/bblocks-ogcapi-processes/)
* [OSPD profile (Open Science Process Description)](https://ogcincubator.github.io/bblocks-openscience/bblock/ogc.osc.api-profiles.processes.ospd)
* [OSPD sample-implementation buffer-geometry processDescription](https://ogcincubator.github.io/bblocks-openscience/bblock/ogc.osc.api-profiles.processes.sample-implementation.schemas.buffer-geometry.processDescription)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/reef-effect-process`

