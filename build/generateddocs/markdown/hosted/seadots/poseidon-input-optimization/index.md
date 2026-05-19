
# POSEIDON Optimization Input (Schema)

`ogc.hosted.seadots.poseidon-input-optimization` *v0.1*

Schema for POSEIDON optimization-problem inputs: base scenario, tunable parameters, parameter adaptors, objective or fitness function, run budget, seeds, and policy outputs.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# POSEIDON Optimization Input

POSEIDON optimization inputs define a base scenario, tunable parameters or adaptors, an objective or fitness metric, run budget, seeds, and replicate strategy. They are used for policy and parameter search, including the Bayesian optimization workflow described in the POSEIDON paper and represented in the repository's EVA examples.

## Pilot use cases (north of Gotland)

Two canonical optimization tasks for the pilot:

1. **Model calibration (back-cast)**: tune unobservable parameters (gear catchability, exploration probability, social-network density, diffusion coefficients) so that POSEIDON outputs reproduce 2010–2023 observed series — SAG SSB, BITS length frequencies, VMS effort distribution, HaV landings, EUMOFA revenue.
2. **Policy search (forecast)**: hold the calibrated parameters fixed; search over policy parameters (TAC tonnes per stock, closure dates, gear-mesh size) to maximise an objective such as multi-stock GES achievement under a fleet-profit floor.

Both reduce to the same schema; only `baseScenario`, `parameters[]`, and `objective` differ.

## Source availability for the pilot area

Role classification:
- **R** = *Required* — optimization run cannot start without it.
- **S** = *Substitutable* — pick one per role; do not stack.
- **V** = *Validation-only* — used for post-hoc verification of the optimizer's selection, not for the objective.

| Source | Role | Coverage of SD 27 / 29 | Provides | Feeds POSEIDON field(s) | Related bblock(s) | Format at origin | Licence |
|---|---|---|---|---|---|---|---|
| ICES WGBFAS SAG SSB time series | **R** for calibration objective | Central Baltic herring, sprat, E. Baltic cod | Annual SSB, recruitment, F | `objective.expression` target series | [poseidon-input-biology] | XML/CSV (SAG) | ICES Data Policy (open) |
| DATRAS BITS length frequencies | **R** for length-structure calibration | SD 27/28/29 | Length-frequency by year × stratum | `objective.expression` target distribution | [poseidon-input-biology] | CSV | ICES Data Policy (open) |
| ICES VMS / GFW spatial effort | **R** for spatial calibration | Whole Baltic | Effort heatmap by year | `objective.expression` target raster (IoU / Spearman) | [poseidon-input-fleet] | CSV / Parquet | ICES / CC-BY-NC |
| HaV landings & first-sale | **R** for revenue/landings calibration | Sweden | Per-trip catch and value | Revenue and landings target series | [poseidon-input-fleet], [poseidon-input-port-market] | CSV | Swedish PSI Open |
| EUMOFA prices | **S** for revenue calibration | EU + Sweden | Monthly first-sale price | Revenue calibration target (alternative to HaV) | [poseidon-input-port-market] | CSV | EC Open |
| FishBase / RAM Legacy CI on biological parameters | **R** for parameter bounds | Target species | Confidence intervals on `Linf, K, M, h` | `parameters[].lowerBound`, `.upperBound` | [poseidon-input-biology] | CSV / SQLite | CC-BY-NC / CC-BY |
| STECF AER segment variance | **R** for fleet-parameter bounds | EU + Sweden | Segment-level fuel intensity, GVA variance | Bounds on fleet adaptation parameters | [poseidon-input-fleet] | Excel | EC Open |
| HELCOM BSAP indicators (GES thresholds) | **S** for policy objective | Whole Baltic | GES threshold values | `objective.expression` for policy search | [poseidon-input-regulation-policy] | CSV / API | CC-BY 4.0 |
| EU MAP F_msy ranges | **S** for policy objective | Baltic stocks | F target ranges | Constraint in policy-search objective | [poseidon-input-regulation-policy] | EUR-Lex | EC Open |
| BoTorch / Ax library defaults | **R** for BO algorithm | – | Acquisition functions, GP priors | `algorithm` selection, kernel choice | – | Python package | MIT |
| OpenMDAO / pymoo (multi-objective) | **S** for multi-objective policy search | – | NSGA-II, MOEA/D | `algorithm` selection | – | Python | Apache-2 |
| Held-out years of SAG / BITS / VMS | **V** | Same as above | Out-of-sample target | Cross-validation of calibration result | [poseidon-input-observation-output] | CSV / Parquet | ICES Data Policy (open) |

[poseidon-input-biology]: ../poseidon-input-biology/
[poseidon-input-fleet]: ../poseidon-input-fleet/
[poseidon-input-map]: ../poseidon-input-map/
[poseidon-input-port-market]: ../poseidon-input-port-market/
[poseidon-input-regulation-policy]: ../poseidon-input-regulation-policy/
[poseidon-input-scenario]: ../poseidon-input-scenario/
[poseidon-input-observation-output]: ../poseidon-input-observation-output/

## Two-stage transformation pipeline

Stage A in this bblock is unusual: the optimization target series are already EDITO-compliant (they were produced as V-role artefacts by other bblocks' Stage A). Stage A here therefore:

1. Registers a new STAC Collection `poseidon-optimization-north-gotland` that *aggregates* the V-role targets via STAC links.
2. Persists the optimizer's Design-of-Experiments (DoE) ledger and per-iteration evaluation results as Parquet.

Stage B compiles the YAML optimization configuration POSEIDON consumes.

### Stage A — Source → EDITO

| Source | EDITO artefact | Transformation |
|---|---|---|
| V-role series from biology / fleet / port-market | `optimization/targets.json` (STAC links) | Build a STAC Collection that *references* the existing Items (no copy); each link tagged with `role=target` and the metric to be computed against. |
| FishBase / RAM Legacy CI for `Linf, K, M, h` | `optimization/parameter_bounds.parquet` | One row per `(species, parameter, lower, upper, prior_mean, prior_sd, source)`; the CI is parsed from FishBase `popgrowth.PopulationsRef` notes and RAM `bioparams` confidence columns. |
| STECF AER segment variance | `optimization/fleet_parameter_bounds.parquet` | Same shape, keyed on `(fleet_segment_id, parameter, lower, upper)`. |
| HELCOM BSAP indicators (GES thresholds) | `optimization/policy_objectives.parquet` | One row per `(indicator_id, threshold, comparison_op, weight)`. |
| Optimizer DoE ledger (output) | `optimization/doe.parquet` (written per iteration during the optimization run) | Columns `iteration, parameters_json, objective_value, replicates_seeds[], wall_clock_s`. |
| Optimizer best-so-far (output) | `optimization/best.parquet` | One row per Pareto-front member (or one row total for single-objective). |

### Stage B — EDITO → POSEIDON

| EDITO artefact | POSEIDON field(s) | Transformation |
|---|---|---|
| `parameter_bounds.parquet` + `fleet_parameter_bounds.parquet` | `parameters[]` with `name, adaptor, lowerBound, upperBound` | One row per parameter; `adaptor` is the POSEIDON parameter-adaptor path (e.g. `species[0].growth.steepness`). |
| `targets.json` + `policy_objectives.parquet` | `objective` (and optional `objective.expression`) | Build a single scalar (or vector for multi-objective) expression: `Σ_i w_i * metric_i(model_output_i, target_i)`. For calibration: weighted sum of NRMSE on SSB + KS on length-freq + IoU on effort heatmap. For policy: BSAP indicator achievement minus profit-floor penalty. |
| `baseScenario` (input) | `baseScenario` reference | Set to the STAC Item URI of the calibrated scenario for policy search; or to a status-quo scenario for calibration. |
| – | `algorithm` | `"Bayesian optimization"` (default, BoTorch/Ax) for single-objective; `"NSGA-II"` for multi-objective policy search. |
| – | `simulationBudget` | Computed from wall-clock target ÷ mean per-run cost (from previous DoE iterations) and capped by user budget. |
| – | `replicatesPerEvaluation` | 3 by default for stochastic POSEIDON; up to 10 for noisy objectives. |

## Required vs substitutable vs validation-only

### Required path

| Optimization task | Minimum required sources |
|---|---|
| Calibration (back-cast) | SAG SSB (R) + BITS length-freq (R) + VMS/GFW effort (R) + HaV landings (R) + FishBase/RAM CI for bounds (R) + STECF AER variance for fleet bounds (R) + BoTorch/Ax (R) |
| Policy search (forecast, single-objective) | A calibrated `baseScenario` (R) + at least one policy parameter bound table (R) + a single-metric `objective.expression` (R) |
| Policy search (multi-objective) | Same + HELCOM BSAP indicators (S) + pymoo / NSGA-II (S) |

### Substitutable

- **Optimization algorithm**: BoTorch/Ax (preferred for single-objective with ≤ ~30 parameters, expensive evaluations) **xor** NSGA-II via pymoo (preferred for multi-objective ≥ 2 metrics) **xor** CMA-ES (fallback for high-dim, less-expensive evaluations).
- **Policy objective**: HELCOM BSAP indicator achievement **xor** EU MAP F_msy compliance — different normative frames; pick one per run.
- **Revenue calibration target**: Swedish HaV (preferred, vessel-level) **xor** EUMOFA (coarser).

### Validation-only

- Held-out years of SAG / BITS / VMS / HaV — used post-optimization to score generalisation.
- ICES retrospective patterns — sanity check that the calibrated model does not over-fit a single assessment year.

### Minimal viable bundle for the pilot

For **calibration**:
1. SAG SSB time series for Central Baltic herring + sprat (2010–2023).
2. BITS Q1 length frequencies (2010–2023).
3. VMS C-square effort for SE flag (2010–2023).
4. FishBase 95% CI on `Linf, K, M` for the two species.
5. STECF AER 2010–2023 segment fuel intensity variance for pelagic-trawl segment.
6. BoTorch/Ax with default acquisition function.

For **policy search**, the calibrated scenario from above + a TAC parameter table + a single GVA-vs-SSB objective.

## Cross-bblock contract

- `baseScenario` MUST resolve to a STAC Item exported by [poseidon-input-scenario] (a scenario Item bundling all input bblocks).
- `parameters[].adaptor` paths MUST exist in the bundled scenario — the runner statically validates each adaptor path before launching.
- `objective.metric` MUST be the **name** of a `timeSeries[]` or `gridded[]` entry declared in [poseidon-input-observation-output] (and therefore present in the [poseidon-output] manifest of each evaluation).
- Calibration replicates' outputs are written to one [poseidon-output] manifest per evaluation under a sub-Collection `poseidon-output-<runId>` — the DoE ledger records the run IDs so the optimizer's best-so-far is reproducible.
- Held-out V-role years are *not* allowed in `objective.expression`; the runner enforces this by checking the year-range of each referenced target Item against [poseidon-input-run-control]'s `yearsToRun`.

## Examples

### Seasonal closure optimization input
#### json
```json
{
  "baseScenario": "inputs/easy.yaml",
  "algorithm": "Bayesian optimization",
  "parameters": [
    {
      "name": "seasonStart",
      "adaptor": "regulations[0].startDay",
      "lowerBound": 1,
      "upperBound": 365
    },
    {
      "name": "seasonEnd",
      "adaptor": "regulations[0].endDay",
      "lowerBound": 1,
      "upperBound": 365
    }
  ],
  "objective": {
    "metric": "policy score",
    "direction": "maximize",
    "expression": "catch - biomass_penalty"
  },
  "simulationBudget": 100,
  "seed": 12345,
  "replicatesPerEvaluation": 10
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-optimization/context.jsonld",
  "baseScenario": "inputs/easy.yaml",
  "algorithm": "Bayesian optimization",
  "parameters": [
    {
      "name": "seasonStart",
      "adaptor": "regulations[0].startDay",
      "lowerBound": 1,
      "upperBound": 365
    },
    {
      "name": "seasonEnd",
      "adaptor": "regulations[0].endDay",
      "lowerBound": 1,
      "upperBound": 365
    }
  ],
  "objective": {
    "metric": "policy score",
    "direction": "maximize",
    "expression": "catch - biomass_penalty"
  },
  "simulationBudget": 100,
  "seed": 12345,
  "replicatesPerEvaluation": 10
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/iliad/seadots/poseidon/input#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] prov:used "inputs/easy.yaml" ;
    schema:algorithm "Bayesian optimization" ;
    schema:target [ :direction "maximize" ;
            :expression "catch - biomass_penalty" ;
            :metric "policy score" ] ;
    schema:variableMeasured ( [ rdfs:label "seasonStart" ;
                :adaptor "regulations[0].startDay" ;
                :lowerBound 1 ;
                :upperBound 365 ] [ rdfs:label "seasonEnd" ;
                :adaptor "regulations[0].endDay" ;
                :lowerBound 1 ;
                :upperBound 365 ] ) ;
    :replicatesPerEvaluation 10 ;
    :seed 12345 ;
    :simulationBudget 100 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: POSEIDON Optimization Input
description: Optimization experiment input for POSEIDON policy and parameter search.
type: object
required:
- baseScenario
- parameters
- objective
properties:
  baseScenario:
    oneOf:
    - type: string
    - $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-scenario/schema.yaml
    x-jsonld-id: http://www.w3.org/ns/prov#used
  algorithm:
    type: string
    default: Bayesian optimization
    x-jsonld-id: https://schema.org/algorithm
  parameters:
    type: array
    minItems: 1
    items:
      type: object
      required:
      - name
      - adaptor
      properties:
        name:
          type: string
        adaptor:
          type: string
          description: POSEIDON parameter adaptor path or implementation name.
        lowerBound:
          type: number
        upperBound:
          type: number
        values:
          type: array
    x-jsonld-id: https://schema.org/variableMeasured
    x-jsonld-container: '@list'
  objective:
    type: object
    required:
    - metric
    properties:
      metric:
        type: string
      direction:
        type: string
        enum:
        - minimize
        - maximize
      expression:
        type: string
    additionalProperties: true
    x-jsonld-id: https://schema.org/target
  simulationBudget:
    type: integer
    minimum: 1
  seed:
    type: integer
  replicatesPerEvaluation:
    type: integer
    minimum: 1
additionalProperties: true
x-jsonld-vocab: https://w3id.org/iliad/seadots/poseidon/input#
x-jsonld-prefixes:
  prov: http://www.w3.org/ns/prov#
  schema: https://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-optimization/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-optimization/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/iliad/seadots/poseidon/input#",
    "baseScenario": {
      "@context": {
        "@vocab": "https://w3id.org/iliad/seadots/poseidon/input#",
        "map": {
          "@context": {
            "@vocab": "https://w3id.org/iliad/seadots/poseidon/input#",
            "mapFile": "dcterms:source",
            "stacItem": {
              "@context": {
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
                    "type": "dcterms:type",
                    "hreflang": "dcterms:language",
                    "title": "rdfs:label",
                    "length": "dcterms:extent"
                  },
                  "@id": "rdfs:seeAlso"
                },
                "linkTemplates": {
                  "@context": {
                    "rel": {
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      },
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id"
                    },
                    "type": "dcterms:format",
                    "hreflang": "dcterms:language",
                    "title": "rdfs:label",
                    "length": "dcterms:extent",
                    "uriTemplate": {
                      "@type": "xsd:string",
                      "@id": "rec:uriTemplate"
                    },
                    "varBase": "rec:varBase",
                    "variables": {
                      "@id": "rec:hasVariable",
                      "@container": "@index",
                      "@index": "dcterms:identifier"
                    }
                  },
                  "@id": "rec:hasLinkTemplate"
                },
                "stac_extensions": "stac:core/hasExtension",
                "assets": {
                  "@context": {
                    "type": "dcterms:format",
                    "roles": {
                      "@id": "stac:core/roles",
                      "@container": "@set"
                    }
                  },
                  "@id": "stac:core/hasAsset",
                  "@container": "@set"
                },
                "title": {
                  "@id": "dcterms:title",
                  "@container": "@set"
                },
                "description": {
                  "@id": "dcterms:description",
                  "@container": "@set"
                },
                "keywords": {
                  "@id": "dcat:keyword",
                  "@container": "@set"
                },
                "license": "dcat:license",
                "formats": {
                  "@context": {
                    "name": "rec:name",
                    "mediaType": "rec:mediaType"
                  },
                  "@container": "@set",
                  "@id": "rec:format",
                  "@type": "@id"
                },
                "contacts": {
                  "@context": {
                    "logo": {
                      "@context": {
                        "rel": {
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          },
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id"
                        },
                        "type": "dcterms:type",
                        "hreflang": "dcterms:language",
                        "title": "rdfs:label",
                        "length": "dcterms:extent"
                      }
                    }
                  },
                  "@container": "@set",
                  "@id": "dcat:contactPoint",
                  "@type": "@id"
                },
                "rights": "dcat:rights"
              },
              "@id": "stac:Item",
              "@type": "@id"
            },
            "stacCollection": {
              "@context": {
                "stac_extensions": "stac:core/hasExtension",
                "links": {
                  "@context": {
                    "rel": {
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      },
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id"
                    },
                    "type": "dcterms:type",
                    "hreflang": "dcterms:language",
                    "title": "rdfs:label",
                    "length": "dcterms:extent"
                  },
                  "@id": "rdfs:seeAlso"
                },
                "assets": {
                  "@context": {
                    "type": "dcterms:format",
                    "roles": {
                      "@id": "stac:core/roles",
                      "@container": "@set"
                    }
                  },
                  "@id": "stac:core/hasAsset",
                  "@container": "@set"
                }
              },
              "@id": "stac:Collection",
              "@type": "@id"
            }
          },
          "@id": "prov:used"
        },
        "biology": {
          "@context": {
            "@vocab": "https://w3id.org/iliad/seadots/poseidon/input#",
            "species": {
              "@context": {
                "name": "schema:name",
                "dataFiles": {
                  "@id": "schema:encoding",
                  "@container": "@list"
                }
              },
              "@id": "schema:about",
              "@container": "@list"
            },
            "stacItems": {
              "@context": {
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
                    "type": "dcterms:type",
                    "hreflang": "dcterms:language",
                    "title": "rdfs:label",
                    "length": "dcterms:extent"
                  },
                  "@id": "rdfs:seeAlso"
                },
                "linkTemplates": {
                  "@context": {
                    "rel": {
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      },
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id"
                    },
                    "type": "dcterms:format",
                    "hreflang": "dcterms:language",
                    "title": "rdfs:label",
                    "length": "dcterms:extent",
                    "uriTemplate": {
                      "@type": "xsd:string",
                      "@id": "rec:uriTemplate"
                    },
                    "varBase": "rec:varBase",
                    "variables": {
                      "@id": "rec:hasVariable",
                      "@container": "@index",
                      "@index": "dcterms:identifier"
                    }
                  },
                  "@id": "rec:hasLinkTemplate"
                },
                "stac_extensions": "stac:core/hasExtension",
                "assets": {
                  "@context": {
                    "type": "dcterms:format",
                    "roles": {
                      "@id": "stac:core/roles",
                      "@container": "@set"
                    }
                  },
                  "@id": "stac:core/hasAsset",
                  "@container": "@set"
                },
                "title": {
                  "@id": "dcterms:title",
                  "@container": "@set"
                },
                "description": {
                  "@id": "dcterms:description",
                  "@container": "@set"
                },
                "keywords": {
                  "@id": "dcat:keyword",
                  "@container": "@set"
                },
                "license": "dcat:license",
                "formats": {
                  "@context": {
                    "name": "rec:name",
                    "mediaType": "rec:mediaType"
                  },
                  "@container": "@set",
                  "@id": "rec:format",
                  "@type": "@id"
                },
                "contacts": {
                  "@context": {
                    "logo": {
                      "@context": {
                        "rel": {
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          },
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id"
                        },
                        "type": "dcterms:type",
                        "hreflang": "dcterms:language",
                        "title": "rdfs:label",
                        "length": "dcterms:extent"
                      }
                    }
                  },
                  "@container": "@set",
                  "@id": "dcat:contactPoint",
                  "@type": "@id"
                },
                "rights": "dcat:rights"
              },
              "@id": "stac:Item",
              "@container": "@list"
            }
          },
          "@id": "prov:used"
        },
        "fleet": {
          "@context": {
            "@vocab": "https://w3id.org/iliad/seadots/poseidon/input#",
            "fishers": {
              "@context": {
                "name": "schema:name",
                "homePort": "schema:homeLocation"
              },
              "@id": "schema:agent",
              "@container": "@list"
            }
          },
          "@id": "prov:used"
        },
        "portsAndMarkets": {
          "@context": {
            "@vocab": "https://w3id.org/iliad/seadots/poseidon/input#",
            "ports": {
              "@context": {
                "name": "schema:name",
                "longitude": "schema:longitude",
                "latitude": "schema:latitude"
              },
              "@id": "schema:location",
              "@container": "@list"
            },
            "market": "schema:offers"
          },
          "@id": "prov:used"
        },
        "regulations": {
          "@context": {
            "@vocab": "https://w3id.org/iliad/seadots/poseidon/input#",
            "regulations": {
              "@context": {
                "species": {
                  "@id": "schema:about",
                  "@container": "@list"
                }
              },
              "@id": "schema:legislation",
              "@container": "@list"
            },
            "shocks": {
              "@id": "schema:event",
              "@container": "@list"
            }
          },
          "@id": "prov:used"
        },
        "output": {
          "@context": {
            "@vocab": "https://w3id.org/iliad/seadots/poseidon/input#",
            "columns": {
              "@id": "schema:variableMeasured",
              "@container": "@list"
            },
            "loggers": {
              "@id": "schema:instrument",
              "@container": "@list"
            },
            "outputProducts": {
              "@context": {
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
                    "type": "dcterms:type",
                    "hreflang": "dcterms:language",
                    "title": "rdfs:label",
                    "length": "dcterms:extent"
                  },
                  "@id": "rdfs:seeAlso"
                },
                "linkTemplates": {
                  "@context": {
                    "rel": {
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      },
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id"
                    },
                    "type": "dcterms:format",
                    "hreflang": "dcterms:language",
                    "title": "rdfs:label",
                    "length": "dcterms:extent",
                    "uriTemplate": {
                      "@type": "xsd:string",
                      "@id": "rec:uriTemplate"
                    },
                    "varBase": "rec:varBase",
                    "variables": {
                      "@id": "rec:hasVariable",
                      "@container": "@index",
                      "@index": "dcterms:identifier"
                    }
                  },
                  "@id": "rec:hasLinkTemplate"
                },
                "title": {
                  "@container": "@set",
                  "@id": "dcterms:title"
                },
                "description": {
                  "@container": "@set",
                  "@id": "dcterms:description"
                },
                "keywords": {
                  "@container": "@set",
                  "@id": "dcat:keyword"
                },
                "formats": {
                  "@id": "rec:format",
                  "@context": {
                    "name": "rec:name",
                    "mediaType": "rec:mediaType"
                  },
                  "@container": "@set",
                  "@type": "@id"
                },
                "contacts": {
                  "@container": "@set",
                  "@id": "dcat:contactPoint",
                  "@type": "@id",
                  "@context": {
                    "logo": {
                      "@context": {
                        "rel": {
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          },
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id"
                        },
                        "type": "dcterms:type",
                        "hreflang": "dcterms:language",
                        "title": "rdfs:label",
                        "length": "dcterms:extent"
                      }
                    }
                  }
                },
                "license": "dcat:license",
                "stac_extensions": "stac:core/hasExtension",
                "assets": {
                  "@context": {
                    "type": "dcterms:format",
                    "roles": {
                      "@id": "stac:core/roles",
                      "@container": "@set"
                    }
                  },
                  "@id": "stac:core/hasAsset",
                  "@container": "@set"
                },
                "name": "stac:cf/name",
                "rights": "dcat:rights"
              },
              "@id": "schema:result",
              "@container": "@list"
            }
          },
          "@id": "prov:used"
        },
        "plugins": {
          "@id": "prov:used",
          "@container": "@list"
        }
      },
      "@id": "prov:used"
    },
    "algorithm": "schema:algorithm",
    "parameters": {
      "@id": "schema:variableMeasured",
      "@container": "@list"
    },
    "objective": "schema:target",
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
    "properties": "@nest",
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "stac_version": "stac:core/version",
    "type": "@type",
    "title": "dcterms:title",
    "description": "dcterms:description",
    "keywords": "dcterms:subject",
    "license": "dcterms:license",
    "start_datetime": {
      "@id": "stac:core/start_datetime",
      "@type": "xsd:dateTime"
    },
    "end_datetime": {
      "@id": "stac:core/end_datetime",
      "@type": "xsd:dateTime"
    },
    "providers": "stac:core/hasProvider",
    "media_type": "dcterms:format",
    "datetime": {
      "@id": "dcterms:date",
      "@type": "xsd:dateTime"
    },
    "time": {
      "@id": "dcterms:temporal",
      "@context": {
        "interval": {
          "@id": "w3ctime:hasTime",
          "@container": "@list"
        },
        "resolution": "rec:iso8601period"
      }
    },
    "created": "dcterms:created",
    "updated": "dcterms:modified",
    "conformsTo": {
      "@container": "@set",
      "@id": "dcterms:conformsTo",
      "@type": "@id"
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
          "@id": "stac:themes/concepts",
          "@context": {
            "id": {
              "@type": "xsd:string",
              "@id": "stac:themes/id"
            },
            "url": {
              "@type": "@id",
              "@id": "@id"
            }
          },
          "@container": "@set"
        }
      }
    },
    "formats": {
      "@id": "rec:format",
      "@context": {
        "name": "rec:name",
        "mediaType": "rec:mediaType"
      }
    },
    "contacts": {
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "accessrights": "dcterms:accessRights",
    "linkTemplates": "rec:hasLinkTemplate",
    "variables": {
      "@container": "@id",
      "@id": "rec:hasVariable",
      "@context": {
        "@base": "http://example.com/variables/",
        "@vocab": "https://www.opengis.net/def/ogc-api/records/"
      }
    },
    "stac_extensions": "stac:core/extensions",
    "extent": "dcterms:extent",
    "links": "rdfs:seeAlso",
    "assets": {
      "@id": "stac:core/hasAsset",
      "@container": "@id",
      "@context": {
        "href": {
          "@id": "dcat:downloadURL",
          "@type": "@id"
        },
        "type": "dcterms:format"
      }
    },
    "concepts": {
      "@id": "stac:themes/concepts",
      "@container": "@set",
      "@context": {
        "name": "stac:themes/name",
        "id": "stac:themes/id",
        "url": "@id"
      }
    },
    "scheme": "stac:themes/scheme",
    "activityType": "@type",
    "agentType": "@type",
    "entityType": "@type",
    "featureType": "@type",
    "provType": "@type",
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
    "alternateOf": {
      "@id": "prov:alternateOf",
      "@type": "@id"
    },
    "atLocation": {
      "@id": "prov:atLocation",
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
    "hadMember": {
      "@id": "prov:hadMember",
      "@type": "@id"
    },
    "hadPlan": {
      "@id": "prov:hadPlan",
      "@type": "@id"
    },
    "hadPrimarySource": {
      "@id": "prov:hadPrimarySource",
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
    "qualifiedAttribution": {
      "@id": "prov:qualifiedAttribution",
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
    "qualifiedDerivation": {
      "@id": "prov:qualifiedDerivation",
      "@type": "@id"
    },
    "qualifiedEnd": {
      "@id": "prov:qualifiedEnd",
      "@type": "@id"
    },
    "qualifiedGeneration": {
      "@id": "prov:qualifiedGeneration",
      "@type": "@id"
    },
    "qualifiedInfluence": {
      "@id": "prov:qualifiedInfluence",
      "@type": "@id"
    },
    "qualifiedInvalidation": {
      "@id": "prov:qualifiedInvalidation",
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
    "specializationOf": {
      "@id": "prov:specializationOf",
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
    "wasAttributedTo": {
      "@id": "prov:wasAttributedTo",
      "@type": "@id"
    },
    "wasDerivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@type": "@id"
    },
    "wasEndedBy": {
      "@id": "prov:wasEndedBy",
      "@type": "@id"
    },
    "wasGeneratedBy": {
      "@id": "prov:wasGeneratedBy",
      "@type": "@id"
    },
    "wasInfluencedBy": {
      "@id": "prov:wasInfluencedBy",
      "@type": "@id"
    },
    "wasInformedBy": {
      "@id": "prov:wasInformedBy",
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
    "wasStartedBy": {
      "@id": "prov:wasStartedBy",
      "@type": "@id"
    },
    "has_anchor": {
      "@id": "prov:has_anchor",
      "@type": "@id"
    },
    "has_provenance": {
      "@id": "dcterms:provenance",
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
    "id": "@id",
    "name": "rdfs:label",
    "unit": {
      "@id": "qudt:hasUnit",
      "@context": {
        "@base": "http://qudt.org/vocab/unit/"
      }
    },
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "https://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "stac": "https://w3id.org/ogc/stac/",
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
    "foaf": "http://xmlns.com/foaf/0.1/",
    "thns": "stac:themes/",
    "cf": "stac:cf/",
    "qudt": "http://qudt.org/schema/qudt/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-optimization/context.jsonld)

## Sources

* [POSEIDON EVA optimization examples](https://github.com/poseidon-fisheries/POSEIDON/tree/main/POSEIDON/eva)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/_stage/poseidon-input-optimization`

