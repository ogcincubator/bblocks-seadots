
# POSEIDON Fisheries Model ODD Record (Schema)

`ogc.hosted.seadots.poseidon-model` *v0.1*

Schema profile for describing the implemented POSEIDON coupled human-environment fisheries model using the ODD Protocol, with explicit model-input building blocks, STAC assets, and Open Science workflow, experiment, product, and provenance links.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# POSEIDON Fisheries Model ODD Record

This building block profiles the local [ODD Protocol Description Record](bblocks://ogc.hosted.seadots.odd-protocol) for the implemented POSEIDON model of ocean fisheries described by Bailey et al. in Sustainability Science and maintained at <https://github.com/poseidon-fisheries/POSEIDON>.

POSEIDON is a coupled human-environment simulation for fisheries policy design. It represents fishing boats as adaptive agents coupled to a spatial fish biomass model, then uses repeated simulation runs and Bayesian optimization to search policy parameter spaces against user-defined objectives.

The implementation is a Java fishery agent-based model licensed under GPL-3.0-or-later. Its current repository README notes that the code is being refactored under the SURIMI project, and points users who want the old tutorial or GUI workflow to the `poseidon-gui` repository. This block therefore records both the published model description and the executable implementation lineage.

The schema keeps the ODD sections as the primary description:

- Overview: purpose, empirical or stylized patterns, entities, and process scheduling.
- Design concepts: adaptation, objectives, sensing, interaction, stochasticity, observation, and the other ODD concepts.
- Details: initialization, input data, and submodels.

The profile adds POSEIDON-specific metadata for:

- explicit input blocks consumed by the implementation;
- policy optimization method, objective function, decision variables, and outputs;
- STAC collections or items used as spatial support assets, using imported STAC building blocks;
- Open Science workflows, experiments, products, and application packages, using imported Open Science building blocks;
- reproducibility notes for run protocols, random seeds, calibration, and implementation status.

## Model Inputs

The implemented model consumes a scenario and related configuration inputs. These are represented as separate building blocks so they can be reused by workflows and validation pipelines:

- `ogc.hosted.seadots.poseidon-input-run-control`: scenario file, policy file, random seed, run length, replicates, and output directory.
- `ogc.hosted.seadots.poseidon-input-scenario`: scenario YAML composition layer.
- `ogc.hosted.seadots.poseidon-input-map`: generated or file-backed spatial map, grid, bathymetry/depth, and STAC spatial assets.
- `ogc.hosted.seadots.poseidon-input-biology`: biomass, abundance, recruitment, growth, mortality, diffusion, OSMOSE, and species parameter inputs.
- `ogc.hosted.seadots.poseidon-input-fleet`: fishers, vessels, gear, behavioural strategies, social network, logbook, and adaptation inputs.
- `ogc.hosted.seadots.poseidon-input-port-market`: ports, landing infrastructure, market prices, and fuel or gas prices.
- `ogc.hosted.seadots.poseidon-input-regulation-policy`: regulations, closures, quotas, gear restrictions, and shocks.
- `ogc.hosted.seadots.poseidon-input-optimization`: base scenario, tunable parameters, objective function, simulation budget, seeds, and replicate strategy.
- `ogc.hosted.seadots.poseidon-input-observation-output`: indicators, output columns, output cadence, and logger selection.

## Imported Building Blocks

The schema is based on `ogc.hosted.seadots.odd-protocol` and imports the following external blocks:

- `ogc.contrib.stac.item`, `ogc.contrib.stac.collection`, and `ogc.contrib.stac.item-prov` for spatial catalog assets and provenance-bearing STAC items.
- `ogc.osc.geodcat-stac-earthcode.workflows`, `ogc.osc.geodcat-stac-earthcode.experiments`, and `ogc.osc.geodcat-stac-earthcode.products` for Open Science catalog metadata.
- `ogc.osc.application-package` for workflow packaging.

## Source

Bailey, R. M., Carrella, E., Axtell, R. et al. (2019). *A computational approach to managing coupled human-environmental systems: the POSEIDON model of ocean fisheries*. Sustainability Science, 14, 259-275. <https://doi.org/10.1007/s11625-018-0579-9>

Implementation repository: <https://github.com/poseidon-fisheries/POSEIDON>

## Examples

### POSEIDON conceptual fisheries policy model
#### json
```json
{
  "id": "https://doi.org/10.1007/s11625-018-0579-9",
  "type": "Feature",
  "geometry": null,
  "links": [
    {
      "rel": "self",
      "href": "https://doi.org/10.1007/s11625-018-0579-9",
      "type": "text/html",
      "title": "POSEIDON model publication"
    },
      {
        "rel": "describedby",
        "href": "https://link.springer.com/article/10.1007/s11625-018-0579-9",
        "type": "text/html",
        "title": "Springer article page"
    },
    {
      "rel": "code",
      "href": "https://github.com/poseidon-fisheries/POSEIDON",
      "type": "text/html",
      "title": "POSEIDON implementation repository"
    }
  ],
  "time": {
    "date": "2018-06-09"
  },
  "properties": {
    "type": "SoftwareApplication",
    "title": "POSEIDON model of ocean fisheries: ODD Protocol Description",
    "description": "POSEIDON is a conceptual coupled human-environment model for ocean fisheries policy design. It couples adaptive fishing-boat agents to a spatial fish biomass model and uses Bayesian optimization over policy parameters to search for policies that satisfy specified management objectives.",
    "created": "2018-06-09T00:00:00Z",
    "updated": "2019-03-01T00:00:00Z",
    "language": {
      "code": "en",
      "name": "English",
      "dir": "ltr"
    },
    "externalIds": [
      {
        "scheme": "doi",
        "value": "10.1007/s11625-018-0579-9"
      },
      {
        "scheme": "url",
        "value": "https://link.springer.com/article/10.1007/s11625-018-0579-9"
      },
      {
        "scheme": "github",
        "value": "https://github.com/poseidon-fisheries/POSEIDON"
      }
    ],
    "contacts": [
      {
        "name": "Richard M. Bailey",
        "roles": ["author", "pointOfContact"],
        "organization": "University of Oxford"
      },
      {
        "name": "Ernesto Carrella",
        "roles": ["author"],
        "organization": "University of Oxford"
      },
      {
        "name": "Steven Saul",
        "roles": ["author"]
      }
    ],
    "themes": [
      {
        "concepts": [
          {
            "id": "agent-based-modelling",
            "label": "Agent-based modelling"
          },
          {
            "id": "fisheries-policy",
            "label": "Fisheries policy"
          },
          {
            "id": "coupled-human-environment-system",
            "label": "Coupled human-environment system"
          },
          {
            "id": "bayesian-optimization",
            "label": "Bayesian optimization"
          }
        ],
        "scheme": "https://w3id.org/iliad/seadots/poseidon/themes/"
      }
    ],
    "keywords": [
      "POSEIDON",
      "fisheries",
      "agent-based model",
      "policy optimization",
      "coupled human-environment system",
      "adaptive fleet behaviour",
      "Bayesian optimization"
    ],
      "license": "https://www.gnu.org/licenses/gpl-3.0.html",
    "formats": [
      {
        "mediaType": "application/json",
        "title": "ODD record"
      }
    ],
    "odd": {
      "purpose": "POSEIDON was developed to support computational policy design for ocean fisheries as coupled human-environment systems. The conceptual model is intended to explore how adaptive fishing fleets respond to policy constraints and incentives, and how automated optimization can identify parameterized policies that meet user-defined management objectives.",
      "patterns": [
        {
          "name": "Adaptive fleet redistribution under policy constraints",
          "description": "Fishing agents alter whether, where, and how they fish in response to profit opportunities, social information, biomass depletion, and imposed policy constraints.",
          "reference": "https://doi.org/10.1007/s11625-018-0579-9"
        },
        {
          "name": "Explore-exploit-imitate decision behaviour",
          "description": "Fishing boats choose between continuing successful behaviour, copying more successful peers, or exploring alternatives, producing group-level adaptation without policy-specific response rules.",
          "reference": "https://doi.org/10.1007/s11625-018-0579-9"
        },
        {
          "name": "Policy objective trade-offs",
          "description": "Different scoring functions and constraints can produce trade-offs among catch, conservation, equity, and other management outcomes.",
          "reference": "https://doi.org/10.1007/s11625-018-0579-9"
        }
      ],
      "entities": [
        {
          "name": "Fishing boat",
          "entityType": "agent",
          "stateVariables": [
            {
              "name": "location",
              "type": "string",
              "unit": "grid cell",
              "range": "ocean cells and port",
              "description": "Current position of the vessel in the spatial fishery domain."
            },
            {
              "name": "profit",
              "type": "real",
              "unit": "currency",
              "range": "real",
              "description": "Economic return used to reinforce or change fishing decisions."
            },
            {
              "name": "gear",
              "type": "string",
              "unit": "dimensionless",
              "range": "available gear choices",
              "description": "Fishing gear selected by the agent for a trip."
            },
            {
              "name": "socialNetwork",
              "type": "list",
              "unit": "dimensionless",
              "range": "other fishing boat agents",
              "description": "Peers whose outcomes may be observed or imitated."
            }
          ],
          "scales": {
            "spatial": "Near-shore capture fishery with one port and a spatial ocean grid.",
            "temporal": "Daily agent decision cycle over multi-year policy simulations."
          }
        },
        {
          "name": "Fish biomass cell",
          "entityType": "grid-cell",
          "stateVariables": [
            {
              "name": "biomass",
              "type": "real",
              "unit": "mass",
              "range": "non-negative",
              "description": "Fish biomass available in the cell and depleted by fishing."
            },
            {
              "name": "intrinsicGrowthRate",
              "type": "real",
              "unit": "per time",
              "range": "non-negative",
              "description": "Local logistic growth parameter for the conceptual biology option."
            },
            {
              "name": "diffusionGradient",
              "type": "real",
              "unit": "mass per area",
              "range": "real",
              "description": "Spatial redistribution pressure following local biomass gradients."
            }
          ],
          "scales": {
            "spatial": "Spatially explicit ocean grid.",
            "temporal": "Updated during each model step."
          }
        },
        {
          "name": "Policy",
          "entityType": "other",
          "stateVariables": [
            {
              "name": "restrictionParameters",
              "type": "list",
              "unit": "dimensionless",
              "range": "policy-specific parameter space",
              "description": "Parameters defining restrictions or incentives such as closures, quotas, taxes, or gear controls."
            },
            {
              "name": "scoringFunction",
              "type": "string",
              "unit": "dimensionless",
              "range": "user-defined objective",
              "description": "Objective used by the optimizer to score simulated policies."
            }
          ],
          "scales": {
            "spatial": "May apply to the whole fishery or selected spatial cells.",
            "temporal": "Policy periods defined by scenario parameters."
          }
        }
      ],
      "processOverview": {
        "scheduling": "At each daily step, fishing agents decide whether to fish, where to fish, and which gear to use; fishing depletes local biomass; biomass grows and diffuses according to the selected ecology submodel; policy rules constrain or incentivize choices; policy optimization runs multiple simulations and updates candidate parameters between runs.",
        "processes": [
          {
            "name": "Choose fishing activity",
            "executedBy": "Fishing boat",
            "description": "Agent decides whether to leave port and participate in fishing for the day."
          },
          {
            "name": "Choose fishing location and gear",
            "executedBy": "Fishing boat",
            "description": "Agent applies an explore-exploit-imitate decision routine using its own outcomes and social-network information."
          },
          {
            "name": "Harvest and profit accounting",
            "executedBy": "Fishing boat",
            "description": "Catch, costs, policy effects, and sales revenue determine the outcome that reinforces future choices."
          },
          {
            "name": "Biomass growth and diffusion",
            "executedBy": "Fish biomass cell",
            "description": "Local fish biomass grows according to a logistic model and diffuses spatially along gradients in the conceptual implementation."
          },
          {
            "name": "Policy parameter optimization",
            "executedBy": "Policy",
            "description": "Bayesian optimization proposes policy parameters, evaluates model runs with a scoring function, and searches for high-scoring policy designs."
          }
        ]
      },
      "designConcepts": {
        "basicPrinciples": "The model uses agent-based modelling to represent heterogeneous fishers and mechanistic ecological dynamics to avoid hard-wiring policy-specific behavioural responses. Policy design is cast as optimization over parameterized regulations.",
        "emergence": "Fleet-level spatial effort patterns, catch outcomes, profit distributions, biomass depletion, and policy performance emerge from local fishing decisions, social imitation, and ecological feedbacks.",
        "adaptation": "Fishing agents adapt through an explore-exploit-imitate routine that reinforces profitable choices, copies successful peers, or explores alternatives.",
        "objectives": "Fishing agents seek profitable choices in the conceptual model. The policy optimizer seeks high scores under user-defined management objectives, such as catch, conservation, or hybrid objectives.",
        "learning": "Agents update behaviour from experience and social comparison rather than using policy-specific programmed responses.",
        "prediction": "Agents use limited, decaying knowledge of prior outcomes and social information rather than perfect forecasts of the simulated world.",
        "sensing": "Agents sense their own past outcomes, selected information from social-network peers, and policy constraints that affect feasible or profitable actions.",
        "interaction": "Fishing boats interact indirectly through competition for biomass and directly or socially through imitation of more successful agents. Boats interact with the ecological environment through harvest and with governance through policy constraints and incentives.",
        "stochasticity": "Initial choices and exploratory decisions can be stochastic; optimization and simulation ensembles require explicit random seed policies for reproducibility.",
        "collectives": "The fleet is represented as a collective outcome of individual fishing boat agents, with social-network structure enabling imitation.",
        "observation": "Model observations include catch, profit, effort distribution, biomass, policy scores, and optimized policy parameter sets across repeated simulation runs."
      },
      "initialization": {
        "description": "The conceptual model initializes a near-shore fishery with a shoreline, one port, a spatial ocean grid containing distributed fish biomass, and a fleet of fishing boat agents. Environmental and external market modules are held constant in the conceptual examples described by the paper.",
        "seed": "Random seeds should be recorded for each simulation run and optimization replicate."
      },
      "inputData": [
        {
          "name": "Spatial fishery domain",
          "description": "POSEIDON map initializer input: generated grid or file-backed map with cell size, map dimensions, coordinates, depth/bathymetry, coastline or land state, and optional STAC-referenced spatial assets.",
          "source": "bblocks://ogc.hosted.seadots.poseidon-input-map",
          "format": "YAML component, CSV map, or STAC item",
          "temporalCoverage": "scenario-specific"
        },
        {
          "name": "Biology initializer and species parameters",
          "description": "POSEIDON biology input: species names, biomass or abundance state, carrying capacity, recruitment, growth, mortality, diffusion, OSMOSE configuration, and species parameter files.",
          "source": "bblocks://ogc.hosted.seadots.poseidon-input-biology",
          "format": "YAML component, CSV parameter table, directory, or STAC item",
          "temporalCoverage": "t0"
        },
        {
          "name": "Fleet and fisher definitions",
          "description": "POSEIDON fleet input: fisher groups, vessel properties, gear, destination/departure/fishing strategies, social network, adaptation probabilities, and logbook settings.",
          "source": "bblocks://ogc.hosted.seadots.poseidon-input-fleet",
          "format": "YAML component",
          "temporalCoverage": "simulation period"
        },
        {
          "name": "Ports, markets, and fuel prices",
          "description": "POSEIDON port and market input: port locations, market price configuration, landing assumptions, and fuel or gas-price configuration.",
          "source": "bblocks://ogc.hosted.seadots.poseidon-input-port-market",
          "format": "YAML component or CSV price table",
          "temporalCoverage": "simulation period"
        },
        {
          "name": "Regulations, policy files, and shocks",
          "description": "POSEIDON management input: closures, quotas, protected areas, gear restrictions, action-specific regulations, conditional rules, and exogenous shocks.",
          "source": "bblocks://ogc.hosted.seadots.poseidon-input-regulation-policy",
          "format": "YAML component or policy file",
          "temporalCoverage": "simulation period"
        },
        {
          "name": "Optimization problem",
          "description": "POSEIDON EVA optimization input: base scenario, parameter adaptors, parameter bounds, objective function, simulation budget, seeds, and replicate strategy.",
          "source": "bblocks://ogc.hosted.seadots.poseidon-input-optimization",
          "format": "YAML optimization problem",
          "temporalCoverage": "experiment period"
        },
        {
          "name": "Observation and output selection",
          "description": "POSEIDON output-selection input: indicators, output columns, time-series cadence, loggers, and output product declarations.",
          "source": "bblocks://ogc.hosted.seadots.poseidon-input-observation-output",
          "format": "YAML or command/run configuration",
          "temporalCoverage": "simulation period"
        }
      ],
      "submodels": [
        {
          "name": "Explore-exploit-imitate fleet behaviour",
          "description": "Fishing agents select actions by continuing a successful option, copying a more successful member of their social network, or exploring another option.",
          "equations": "Algorithmic multi-armed bandit style decision rule; see supplementary material for pseudocode.",
          "parameterization": "Requires probabilities or hyper-parameters controlling exploration, exploitation, imitation, memory decay, and social-network influence.",
          "links": [
            {
              "href": "https://doi.org/10.1007/s11625-018-0579-9",
              "rel": "describedby",
              "title": "POSEIDON paper"
            }
          ]
        },
        {
          "name": "Spatial fish biomass",
          "description": "Conceptual examples use local logistic biomass growth and diffusion along spatial gradients, with fishing pressure depleting biomass.",
          "equations": "Local logistic growth plus spatial diffusion and harvest loss.",
          "parameterization": "Growth, carrying capacity, diffusion, catchability, and harvest parameters are scenario-specific; the paper also notes OSMOSE as a more sophisticated biology option.",
          "links": [
            {
              "href": "https://doi.org/10.1007/s11625-018-0579-9",
              "rel": "describedby",
              "title": "POSEIDON paper"
            }
          ]
        },
        {
          "name": "Bayesian policy optimization",
          "description": "An optimizer iteratively selects policy parameter combinations, runs the model, updates a surrogate meta-model of policy performance, and searches for high-scoring policies.",
          "equations": "Black-box optimization of a scoring function over policy parameter space.",
          "parameterization": "Requires a scoring function, policy parameter bounds, simulation budget, convergence criteria, and replicate design.",
          "links": [
            {
              "href": "https://doi.org/10.1007/s11625-018-0579-9",
              "rel": "describedby",
              "title": "POSEIDON paper"
            }
          ]
        }
      ]
    },
    "poseidon": {
      "modelRole": "coupled-human-environment-fisheries-policy-model",
      "publication": {
        "doi": "https://doi.org/10.1007/s11625-018-0579-9",
        "citation": "Bailey, R.M., Carrella, E., Axtell, R. et al. A computational approach to managing coupled human-environmental systems: the POSEIDON model of ocean fisheries. Sustainability Science 14, 259-275 (2019).",
        "published": "2018-06-09",
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "supplementaryMaterial": [
          {
            "href": "https://link.springer.com/article/10.1007/s11625-018-0579-9#Sec25",
            "rel": "describedby",
            "title": "Electronic supplementary material"
          }
        ]
      },
      "policyOptimization": {
        "method": "Bayesian optimization",
        "objectiveFunction": "User-defined scoring function over simulated policy outcomes.",
        "decisionVariables": [
          {
            "name": "seasonStart",
            "description": "Start day of a seasonal fishery closure policy.",
            "unit": "day-of-year",
            "range": "1..365"
          },
          {
            "name": "seasonEnd",
            "description": "End day of a seasonal fishery closure policy.",
            "unit": "day-of-year",
            "range": "1..365"
          },
          {
            "name": "policyHybridParameters",
            "description": "Additional tunable policy controls for hybrid policies.",
            "unit": "dimensionless",
            "range": "scenario-specific"
          }
        ],
        "outputs": [
          "policy score",
          "catch",
          "effort distribution",
          "profit",
          "fish biomass",
          "optimized policy parameters"
        ]
      },
      "spatialSupport": {
        "stacCollections": [
          {
            "href": "https://example.org/stac/collections/poseidon-fishery-domain",
            "rel": "derived-from",
            "title": "Example STAC collection for POSEIDON spatial domain assets",
            "type": "application/json"
          }
        ],
        "stacItems": [
          {
            "href": "https://example.org/stac/collections/poseidon-fishery-domain/items/initial-biomass",
            "rel": "input",
            "title": "Example initial biomass raster item",
            "type": "application/geo+json"
          }
        ]
      },
      "openScience": {
        "workflow": {
          "href": "https://example.org/ogcapi/processes/poseidon-policy-optimization",
          "rel": "workflow",
          "title": "Example POSEIDON policy optimization workflow",
          "type": "application/json"
        },
        "experiments": [
          {
            "href": "https://example.org/records/poseidon-seasonal-closure-experiment",
            "rel": "experiment",
            "title": "Example seasonal closure optimization experiment",
            "type": "application/geo+json"
          }
        ],
        "products": [
          {
            "href": "https://example.org/records/poseidon-optimized-policy-products",
            "rel": "result",
            "title": "Example optimized policy outputs",
            "type": "application/geo+json"
          }
        ]
      },
      "reproducibility": {
        "implementationStatus": "executable-implementation",
        "randomSeedPolicy": "Record a seed for each model run and optimization replicate.",
        "runProtocol": "Define policy parameter bounds, initialize the spatial fishery and fleet, run replicate simulations for proposed policies, evaluate the scoring function, and update the Bayesian optimizer until the configured simulation budget or convergence condition is met.",
        "calibration": "The implementation is executable; site-specific deployments should calibrate biological, economic, behavioural, spatial, and policy parameters against local data."
      },
      "implementation": {
        "repository": "https://github.com/poseidon-fisheries/POSEIDON",
        "language": "Java",
        "license": "https://www.gnu.org/licenses/gpl-3.0.html",
        "inputBlocks": {
          "runControl": {
            "scenario": "inputs/easy.yaml",
            "policy": "inputs/policies/seasonal_closure.yaml",
            "yearsToRun": 50,
            "randomSeed": 12345,
            "replicates": 20,
            "outputDirectory": "runs/seasonal-closure",
            "outputSelection": "inputs/output_columns.yaml"
          },
          "scenario": {
            "scenarioType": "Flexible Scenario",
            "map": {
              "initializerType": "From File Map",
              "mapFile": "inputs/indonesia/indonesia_latlong.csv",
              "gridWidthInCell": 100,
              "header": true,
              "latLong": true
            },
            "biology": {
              "initializerType": "Single Species Biomass",
              "species": [
                {
                  "name": "Species 0",
                  "modelType": "biomass",
                  "carryingCapacity": 5000
                }
              ]
            },
            "fleet": {
              "fishers": [
                {
                  "name": "small-vessel-fleet",
                  "count": 50,
                  "gear": {
                    "type": "Random Catchability"
                  }
                }
              ]
            }
          },
          "map": {
            "initializerType": "From File Map",
            "mapFile": "inputs/indonesia/indonesia_latlong.csv",
            "gridWidthInCell": 100,
            "header": true,
            "latLong": true
          },
          "biology": {
            "initializerType": "Single Species Biomass",
            "species": [
              {
                "name": "Species 0",
                "modelType": "biomass",
                "carryingCapacity": 5000
              }
            ]
          },
          "fleet": {
            "fishers": [
              {
                "name": "small-vessel-fleet",
                "count": 50,
                "gear": {
                  "type": "Random Catchability"
                }
              }
            ]
          },
          "portMarket": {
            "portInitializerType": "One Port",
            "ports": [
              {
                "name": "Main Port",
                "x": 40,
                "y": 25,
                "usingGridCoordinates": true
              }
            ]
          },
          "regulationPolicy": {
            "regulations": [
              {
                "type": "Seasonal Closure",
                "startDay": 120,
                "endDay": 200
              }
            ]
          },
          "optimization": {
            "baseScenario": "inputs/easy.yaml",
            "algorithm": "Bayesian optimization",
            "parameters": [
              {
                "name": "seasonStart",
                "adaptor": "regulations[0].startDay",
                "lowerBound": 1,
                "upperBound": 365
              }
            ],
            "objective": {
              "metric": "policy score",
              "direction": "maximize"
            }
          },
          "observationOutput": {
            "columns": [
              "Species 0 Landings",
              "Species 0 Biomass",
              "Average Cash-Flow"
            ],
            "cadence": "yearly"
          }
        }
      }
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-model/context.jsonld",
  "id": "https://doi.org/10.1007/s11625-018-0579-9",
  "type": "Feature",
  "geometry": null,
  "links": [
    {
      "rel": "self",
      "href": "https://doi.org/10.1007/s11625-018-0579-9",
      "type": "text/html",
      "title": "POSEIDON model publication"
    },
    {
      "rel": "describedby",
      "href": "https://link.springer.com/article/10.1007/s11625-018-0579-9",
      "type": "text/html",
      "title": "Springer article page"
    },
    {
      "rel": "code",
      "href": "https://github.com/poseidon-fisheries/POSEIDON",
      "type": "text/html",
      "title": "POSEIDON implementation repository"
    }
  ],
  "time": {
    "date": "2018-06-09"
  },
  "properties": {
    "type": "SoftwareApplication",
    "title": "POSEIDON model of ocean fisheries: ODD Protocol Description",
    "description": "POSEIDON is a conceptual coupled human-environment model for ocean fisheries policy design. It couples adaptive fishing-boat agents to a spatial fish biomass model and uses Bayesian optimization over policy parameters to search for policies that satisfy specified management objectives.",
    "created": "2018-06-09T00:00:00Z",
    "updated": "2019-03-01T00:00:00Z",
    "language": {
      "code": "en",
      "name": "English",
      "dir": "ltr"
    },
    "externalIds": [
      {
        "scheme": "doi",
        "value": "10.1007/s11625-018-0579-9"
      },
      {
        "scheme": "url",
        "value": "https://link.springer.com/article/10.1007/s11625-018-0579-9"
      },
      {
        "scheme": "github",
        "value": "https://github.com/poseidon-fisheries/POSEIDON"
      }
    ],
    "contacts": [
      {
        "name": "Richard M. Bailey",
        "roles": [
          "author",
          "pointOfContact"
        ],
        "organization": "University of Oxford"
      },
      {
        "name": "Ernesto Carrella",
        "roles": [
          "author"
        ],
        "organization": "University of Oxford"
      },
      {
        "name": "Steven Saul",
        "roles": [
          "author"
        ]
      }
    ],
    "themes": [
      {
        "concepts": [
          {
            "id": "agent-based-modelling",
            "label": "Agent-based modelling"
          },
          {
            "id": "fisheries-policy",
            "label": "Fisheries policy"
          },
          {
            "id": "coupled-human-environment-system",
            "label": "Coupled human-environment system"
          },
          {
            "id": "bayesian-optimization",
            "label": "Bayesian optimization"
          }
        ],
        "scheme": "https://w3id.org/iliad/seadots/poseidon/themes/"
      }
    ],
    "keywords": [
      "POSEIDON",
      "fisheries",
      "agent-based model",
      "policy optimization",
      "coupled human-environment system",
      "adaptive fleet behaviour",
      "Bayesian optimization"
    ],
    "license": "https://www.gnu.org/licenses/gpl-3.0.html",
    "formats": [
      {
        "mediaType": "application/json",
        "title": "ODD record"
      }
    ],
    "odd": {
      "purpose": "POSEIDON was developed to support computational policy design for ocean fisheries as coupled human-environment systems. The conceptual model is intended to explore how adaptive fishing fleets respond to policy constraints and incentives, and how automated optimization can identify parameterized policies that meet user-defined management objectives.",
      "patterns": [
        {
          "name": "Adaptive fleet redistribution under policy constraints",
          "description": "Fishing agents alter whether, where, and how they fish in response to profit opportunities, social information, biomass depletion, and imposed policy constraints.",
          "reference": "https://doi.org/10.1007/s11625-018-0579-9"
        },
        {
          "name": "Explore-exploit-imitate decision behaviour",
          "description": "Fishing boats choose between continuing successful behaviour, copying more successful peers, or exploring alternatives, producing group-level adaptation without policy-specific response rules.",
          "reference": "https://doi.org/10.1007/s11625-018-0579-9"
        },
        {
          "name": "Policy objective trade-offs",
          "description": "Different scoring functions and constraints can produce trade-offs among catch, conservation, equity, and other management outcomes.",
          "reference": "https://doi.org/10.1007/s11625-018-0579-9"
        }
      ],
      "entities": [
        {
          "name": "Fishing boat",
          "entityType": "agent",
          "stateVariables": [
            {
              "name": "location",
              "type": "string",
              "unit": "grid cell",
              "range": "ocean cells and port",
              "description": "Current position of the vessel in the spatial fishery domain."
            },
            {
              "name": "profit",
              "type": "real",
              "unit": "currency",
              "range": "real",
              "description": "Economic return used to reinforce or change fishing decisions."
            },
            {
              "name": "gear",
              "type": "string",
              "unit": "dimensionless",
              "range": "available gear choices",
              "description": "Fishing gear selected by the agent for a trip."
            },
            {
              "name": "socialNetwork",
              "type": "list",
              "unit": "dimensionless",
              "range": "other fishing boat agents",
              "description": "Peers whose outcomes may be observed or imitated."
            }
          ],
          "scales": {
            "spatial": "Near-shore capture fishery with one port and a spatial ocean grid.",
            "temporal": "Daily agent decision cycle over multi-year policy simulations."
          }
        },
        {
          "name": "Fish biomass cell",
          "entityType": "grid-cell",
          "stateVariables": [
            {
              "name": "biomass",
              "type": "real",
              "unit": "mass",
              "range": "non-negative",
              "description": "Fish biomass available in the cell and depleted by fishing."
            },
            {
              "name": "intrinsicGrowthRate",
              "type": "real",
              "unit": "per time",
              "range": "non-negative",
              "description": "Local logistic growth parameter for the conceptual biology option."
            },
            {
              "name": "diffusionGradient",
              "type": "real",
              "unit": "mass per area",
              "range": "real",
              "description": "Spatial redistribution pressure following local biomass gradients."
            }
          ],
          "scales": {
            "spatial": "Spatially explicit ocean grid.",
            "temporal": "Updated during each model step."
          }
        },
        {
          "name": "Policy",
          "entityType": "other",
          "stateVariables": [
            {
              "name": "restrictionParameters",
              "type": "list",
              "unit": "dimensionless",
              "range": "policy-specific parameter space",
              "description": "Parameters defining restrictions or incentives such as closures, quotas, taxes, or gear controls."
            },
            {
              "name": "scoringFunction",
              "type": "string",
              "unit": "dimensionless",
              "range": "user-defined objective",
              "description": "Objective used by the optimizer to score simulated policies."
            }
          ],
          "scales": {
            "spatial": "May apply to the whole fishery or selected spatial cells.",
            "temporal": "Policy periods defined by scenario parameters."
          }
        }
      ],
      "processOverview": {
        "scheduling": "At each daily step, fishing agents decide whether to fish, where to fish, and which gear to use; fishing depletes local biomass; biomass grows and diffuses according to the selected ecology submodel; policy rules constrain or incentivize choices; policy optimization runs multiple simulations and updates candidate parameters between runs.",
        "processes": [
          {
            "name": "Choose fishing activity",
            "executedBy": "Fishing boat",
            "description": "Agent decides whether to leave port and participate in fishing for the day."
          },
          {
            "name": "Choose fishing location and gear",
            "executedBy": "Fishing boat",
            "description": "Agent applies an explore-exploit-imitate decision routine using its own outcomes and social-network information."
          },
          {
            "name": "Harvest and profit accounting",
            "executedBy": "Fishing boat",
            "description": "Catch, costs, policy effects, and sales revenue determine the outcome that reinforces future choices."
          },
          {
            "name": "Biomass growth and diffusion",
            "executedBy": "Fish biomass cell",
            "description": "Local fish biomass grows according to a logistic model and diffuses spatially along gradients in the conceptual implementation."
          },
          {
            "name": "Policy parameter optimization",
            "executedBy": "Policy",
            "description": "Bayesian optimization proposes policy parameters, evaluates model runs with a scoring function, and searches for high-scoring policy designs."
          }
        ]
      },
      "designConcepts": {
        "basicPrinciples": "The model uses agent-based modelling to represent heterogeneous fishers and mechanistic ecological dynamics to avoid hard-wiring policy-specific behavioural responses. Policy design is cast as optimization over parameterized regulations.",
        "emergence": "Fleet-level spatial effort patterns, catch outcomes, profit distributions, biomass depletion, and policy performance emerge from local fishing decisions, social imitation, and ecological feedbacks.",
        "adaptation": "Fishing agents adapt through an explore-exploit-imitate routine that reinforces profitable choices, copies successful peers, or explores alternatives.",
        "objectives": "Fishing agents seek profitable choices in the conceptual model. The policy optimizer seeks high scores under user-defined management objectives, such as catch, conservation, or hybrid objectives.",
        "learning": "Agents update behaviour from experience and social comparison rather than using policy-specific programmed responses.",
        "prediction": "Agents use limited, decaying knowledge of prior outcomes and social information rather than perfect forecasts of the simulated world.",
        "sensing": "Agents sense their own past outcomes, selected information from social-network peers, and policy constraints that affect feasible or profitable actions.",
        "interaction": "Fishing boats interact indirectly through competition for biomass and directly or socially through imitation of more successful agents. Boats interact with the ecological environment through harvest and with governance through policy constraints and incentives.",
        "stochasticity": "Initial choices and exploratory decisions can be stochastic; optimization and simulation ensembles require explicit random seed policies for reproducibility.",
        "collectives": "The fleet is represented as a collective outcome of individual fishing boat agents, with social-network structure enabling imitation.",
        "observation": "Model observations include catch, profit, effort distribution, biomass, policy scores, and optimized policy parameter sets across repeated simulation runs."
      },
      "initialization": {
        "description": "The conceptual model initializes a near-shore fishery with a shoreline, one port, a spatial ocean grid containing distributed fish biomass, and a fleet of fishing boat agents. Environmental and external market modules are held constant in the conceptual examples described by the paper.",
        "seed": "Random seeds should be recorded for each simulation run and optimization replicate."
      },
      "inputData": [
        {
          "name": "Spatial fishery domain",
          "description": "POSEIDON map initializer input: generated grid or file-backed map with cell size, map dimensions, coordinates, depth/bathymetry, coastline or land state, and optional STAC-referenced spatial assets.",
          "source": "bblocks://ogc.hosted.seadots.poseidon-input-map",
          "format": "YAML component, CSV map, or STAC item",
          "temporalCoverage": "scenario-specific"
        },
        {
          "name": "Biology initializer and species parameters",
          "description": "POSEIDON biology input: species names, biomass or abundance state, carrying capacity, recruitment, growth, mortality, diffusion, OSMOSE configuration, and species parameter files.",
          "source": "bblocks://ogc.hosted.seadots.poseidon-input-biology",
          "format": "YAML component, CSV parameter table, directory, or STAC item",
          "temporalCoverage": "t0"
        },
        {
          "name": "Fleet and fisher definitions",
          "description": "POSEIDON fleet input: fisher groups, vessel properties, gear, destination/departure/fishing strategies, social network, adaptation probabilities, and logbook settings.",
          "source": "bblocks://ogc.hosted.seadots.poseidon-input-fleet",
          "format": "YAML component",
          "temporalCoverage": "simulation period"
        },
        {
          "name": "Ports, markets, and fuel prices",
          "description": "POSEIDON port and market input: port locations, market price configuration, landing assumptions, and fuel or gas-price configuration.",
          "source": "bblocks://ogc.hosted.seadots.poseidon-input-port-market",
          "format": "YAML component or CSV price table",
          "temporalCoverage": "simulation period"
        },
        {
          "name": "Regulations, policy files, and shocks",
          "description": "POSEIDON management input: closures, quotas, protected areas, gear restrictions, action-specific regulations, conditional rules, and exogenous shocks.",
          "source": "bblocks://ogc.hosted.seadots.poseidon-input-regulation-policy",
          "format": "YAML component or policy file",
          "temporalCoverage": "simulation period"
        },
        {
          "name": "Optimization problem",
          "description": "POSEIDON EVA optimization input: base scenario, parameter adaptors, parameter bounds, objective function, simulation budget, seeds, and replicate strategy.",
          "source": "bblocks://ogc.hosted.seadots.poseidon-input-optimization",
          "format": "YAML optimization problem",
          "temporalCoverage": "experiment period"
        },
        {
          "name": "Observation and output selection",
          "description": "POSEIDON output-selection input: indicators, output columns, time-series cadence, loggers, and output product declarations.",
          "source": "bblocks://ogc.hosted.seadots.poseidon-input-observation-output",
          "format": "YAML or command/run configuration",
          "temporalCoverage": "simulation period"
        }
      ],
      "submodels": [
        {
          "name": "Explore-exploit-imitate fleet behaviour",
          "description": "Fishing agents select actions by continuing a successful option, copying a more successful member of their social network, or exploring another option.",
          "equations": "Algorithmic multi-armed bandit style decision rule; see supplementary material for pseudocode.",
          "parameterization": "Requires probabilities or hyper-parameters controlling exploration, exploitation, imitation, memory decay, and social-network influence.",
          "links": [
            {
              "href": "https://doi.org/10.1007/s11625-018-0579-9",
              "rel": "describedby",
              "title": "POSEIDON paper"
            }
          ]
        },
        {
          "name": "Spatial fish biomass",
          "description": "Conceptual examples use local logistic biomass growth and diffusion along spatial gradients, with fishing pressure depleting biomass.",
          "equations": "Local logistic growth plus spatial diffusion and harvest loss.",
          "parameterization": "Growth, carrying capacity, diffusion, catchability, and harvest parameters are scenario-specific; the paper also notes OSMOSE as a more sophisticated biology option.",
          "links": [
            {
              "href": "https://doi.org/10.1007/s11625-018-0579-9",
              "rel": "describedby",
              "title": "POSEIDON paper"
            }
          ]
        },
        {
          "name": "Bayesian policy optimization",
          "description": "An optimizer iteratively selects policy parameter combinations, runs the model, updates a surrogate meta-model of policy performance, and searches for high-scoring policies.",
          "equations": "Black-box optimization of a scoring function over policy parameter space.",
          "parameterization": "Requires a scoring function, policy parameter bounds, simulation budget, convergence criteria, and replicate design.",
          "links": [
            {
              "href": "https://doi.org/10.1007/s11625-018-0579-9",
              "rel": "describedby",
              "title": "POSEIDON paper"
            }
          ]
        }
      ]
    },
    "poseidon": {
      "modelRole": "coupled-human-environment-fisheries-policy-model",
      "publication": {
        "doi": "https://doi.org/10.1007/s11625-018-0579-9",
        "citation": "Bailey, R.M., Carrella, E., Axtell, R. et al. A computational approach to managing coupled human-environmental systems: the POSEIDON model of ocean fisheries. Sustainability Science 14, 259-275 (2019).",
        "published": "2018-06-09",
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "supplementaryMaterial": [
          {
            "href": "https://link.springer.com/article/10.1007/s11625-018-0579-9#Sec25",
            "rel": "describedby",
            "title": "Electronic supplementary material"
          }
        ]
      },
      "policyOptimization": {
        "method": "Bayesian optimization",
        "objectiveFunction": "User-defined scoring function over simulated policy outcomes.",
        "decisionVariables": [
          {
            "name": "seasonStart",
            "description": "Start day of a seasonal fishery closure policy.",
            "unit": "day-of-year",
            "range": "1..365"
          },
          {
            "name": "seasonEnd",
            "description": "End day of a seasonal fishery closure policy.",
            "unit": "day-of-year",
            "range": "1..365"
          },
          {
            "name": "policyHybridParameters",
            "description": "Additional tunable policy controls for hybrid policies.",
            "unit": "dimensionless",
            "range": "scenario-specific"
          }
        ],
        "outputs": [
          "policy score",
          "catch",
          "effort distribution",
          "profit",
          "fish biomass",
          "optimized policy parameters"
        ]
      },
      "spatialSupport": {
        "stacCollections": [
          {
            "href": "https://example.org/stac/collections/poseidon-fishery-domain",
            "rel": "derived-from",
            "title": "Example STAC collection for POSEIDON spatial domain assets",
            "type": "application/json"
          }
        ],
        "stacItems": [
          {
            "href": "https://example.org/stac/collections/poseidon-fishery-domain/items/initial-biomass",
            "rel": "input",
            "title": "Example initial biomass raster item",
            "type": "application/geo+json"
          }
        ]
      },
      "openScience": {
        "workflow": {
          "href": "https://example.org/ogcapi/processes/poseidon-policy-optimization",
          "rel": "workflow",
          "title": "Example POSEIDON policy optimization workflow",
          "type": "application/json"
        },
        "experiments": [
          {
            "href": "https://example.org/records/poseidon-seasonal-closure-experiment",
            "rel": "experiment",
            "title": "Example seasonal closure optimization experiment",
            "type": "application/geo+json"
          }
        ],
        "products": [
          {
            "href": "https://example.org/records/poseidon-optimized-policy-products",
            "rel": "result",
            "title": "Example optimized policy outputs",
            "type": "application/geo+json"
          }
        ]
      },
      "reproducibility": {
        "implementationStatus": "executable-implementation",
        "randomSeedPolicy": "Record a seed for each model run and optimization replicate.",
        "runProtocol": "Define policy parameter bounds, initialize the spatial fishery and fleet, run replicate simulations for proposed policies, evaluate the scoring function, and update the Bayesian optimizer until the configured simulation budget or convergence condition is met.",
        "calibration": "The implementation is executable; site-specific deployments should calibrate biological, economic, behavioural, spatial, and policy parameters against local data."
      },
      "implementation": {
        "repository": "https://github.com/poseidon-fisheries/POSEIDON",
        "language": "Java",
        "license": "https://www.gnu.org/licenses/gpl-3.0.html",
        "inputBlocks": {
          "runControl": {
            "scenario": "inputs/easy.yaml",
            "policy": "inputs/policies/seasonal_closure.yaml",
            "yearsToRun": 50,
            "randomSeed": 12345,
            "replicates": 20,
            "outputDirectory": "runs/seasonal-closure",
            "outputSelection": "inputs/output_columns.yaml"
          },
          "scenario": {
            "scenarioType": "Flexible Scenario",
            "map": {
              "initializerType": "From File Map",
              "mapFile": "inputs/indonesia/indonesia_latlong.csv",
              "gridWidthInCell": 100,
              "header": true,
              "latLong": true
            },
            "biology": {
              "initializerType": "Single Species Biomass",
              "species": [
                {
                  "name": "Species 0",
                  "modelType": "biomass",
                  "carryingCapacity": 5000
                }
              ]
            },
            "fleet": {
              "fishers": [
                {
                  "name": "small-vessel-fleet",
                  "count": 50,
                  "gear": {
                    "type": "Random Catchability"
                  }
                }
              ]
            }
          },
          "map": {
            "initializerType": "From File Map",
            "mapFile": "inputs/indonesia/indonesia_latlong.csv",
            "gridWidthInCell": 100,
            "header": true,
            "latLong": true
          },
          "biology": {
            "initializerType": "Single Species Biomass",
            "species": [
              {
                "name": "Species 0",
                "modelType": "biomass",
                "carryingCapacity": 5000
              }
            ]
          },
          "fleet": {
            "fishers": [
              {
                "name": "small-vessel-fleet",
                "count": 50,
                "gear": {
                  "type": "Random Catchability"
                }
              }
            ]
          },
          "portMarket": {
            "portInitializerType": "One Port",
            "ports": [
              {
                "name": "Main Port",
                "x": 40,
                "y": 25,
                "usingGridCoordinates": true
              }
            ]
          },
          "regulationPolicy": {
            "regulations": [
              {
                "type": "Seasonal Closure",
                "startDay": 120,
                "endDay": 200
              }
            ]
          },
          "optimization": {
            "baseScenario": "inputs/easy.yaml",
            "algorithm": "Bayesian optimization",
            "parameters": [
              {
                "name": "seasonStart",
                "adaptor": "regulations[0].startDay",
                "lowerBound": 1,
                "upperBound": 365
              }
            ],
            "objective": {
              "metric": "policy score",
              "direction": "maximize"
            }
          },
          "observationOutput": {
            "columns": [
              "Species 0 Landings",
              "Species 0 Biomass",
              "Average Cash-Flow"
            ],
            "cadence": "yearly"
          }
        }
      }
    }
  }
}
```

#### ttl
```ttl
@prefix bibo: <http://purl.org/ontology/bibo/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix odd: <https://w3id.org/iliad/odd#> .
@prefix osc: <https://github.com/ILIAD-ocean-twin/OIM/blob/main/openscience#> .
@prefix pos: <https://w3id.org/iliad/seadots/poseidon#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix schema: <https://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix stac: <https://w3id.org/ogc/stac/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://doi.org/10.1007/s11625-018-0579-9> dcterms:created "2018-06-09T00:00:00Z" ;
    dcterms:description "POSEIDON is a conceptual coupled human-environment model for ocean fisheries policy design. It couples adaptive fishing-boat agents to a spatial fish biomass model and uses Bayesian optimization over policy parameters to search for policies that satisfy specified management objectives." ;
    dcterms:license "https://www.gnu.org/licenses/gpl-3.0.html" ;
    dcterms:modified "2019-03-01T00:00:00Z" ;
    dcterms:temporal [ ] ;
    dcterms:title "POSEIDON model of ocean fisheries: ODD Protocol Description" ;
    rdfs:seeAlso [ rdfs:label "Springer article page" ;
            dcterms:format "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <https://link.springer.com/article/10.1007/s11625-018-0579-9> ],
        [ rdfs:label "POSEIDON implementation repository" ;
            dcterms:format "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/code> ;
            oa:hasTarget <https://github.com/poseidon-fisheries/POSEIDON> ],
        [ rdfs:label "POSEIDON model publication" ;
            dcterms:format "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <https://doi.org/10.1007/s11625-018-0579-9> ] ;
    dcat:contactPoint [ rdfs:label "Ernesto Carrella" ],
        [ rdfs:label "Richard M. Bailey" ],
        [ rdfs:label "Steven Saul" ] ;
    dcat:keyword "Bayesian optimization",
        "POSEIDON",
        "adaptive fleet behaviour",
        "agent-based model",
        "coupled human-environment system",
        "fisheries",
        "policy optimization" ;
    odd: [ odd:designConcepts [ odd:adaptation "Fishing agents adapt through an explore-exploit-imitate routine that reinforces profitable choices, copies successful peers, or explores alternatives." ;
                    odd:basicPrinciples "The model uses agent-based modelling to represent heterogeneous fishers and mechanistic ecological dynamics to avoid hard-wiring policy-specific behavioural responses. Policy design is cast as optimization over parameterized regulations." ;
                    odd:collectives "The fleet is represented as a collective outcome of individual fishing boat agents, with social-network structure enabling imitation." ;
                    odd:emergence "Fleet-level spatial effort patterns, catch outcomes, profit distributions, biomass depletion, and policy performance emerge from local fishing decisions, social imitation, and ecological feedbacks." ;
                    odd:interaction "Fishing boats interact indirectly through competition for biomass and directly or socially through imitation of more successful agents. Boats interact with the ecological environment through harvest and with governance through policy constraints and incentives." ;
                    odd:learning "Agents update behaviour from experience and social comparison rather than using policy-specific programmed responses." ;
                    odd:objectives "Fishing agents seek profitable choices in the conceptual model. The policy optimizer seeks high scores under user-defined management objectives, such as catch, conservation, or hybrid objectives." ;
                    odd:observation "Model observations include catch, profit, effort distribution, biomass, policy scores, and optimized policy parameter sets across repeated simulation runs." ;
                    odd:prediction "Agents use limited, decaying knowledge of prior outcomes and social information rather than perfect forecasts of the simulated world." ;
                    odd:sensing "Agents sense their own past outcomes, selected information from social-network peers, and policy constraints that affect feasible or profitable actions." ;
                    odd:stochasticity "Initial choices and exploratory decisions can be stochastic; optimization and simulation ensembles require explicit random seed policies for reproducibility." ] ;
            odd:entities ( [ dcterms:title "Fishing boat" ;
                        odd:entityType "agent" ;
                        odd:scales [ odd:spatialScale "Near-shore capture fishery with one port and a spatial ocean grid." ;
                                odd:temporalScale "Daily agent decision cycle over multi-year policy simulations." ] ;
                        odd:stateVariables ( [ dcterms:description "Current position of the vessel in the spatial fishery domain." ;
                                    dcterms:title "location" ;
                                    qudt:unit "grid cell" ;
                                    odd:range "ocean cells and port" ;
                                    odd:variableType "string" ] [ dcterms:description "Economic return used to reinforce or change fishing decisions." ;
                                    dcterms:title "profit" ;
                                    qudt:unit "currency" ;
                                    odd:range "real" ;
                                    odd:variableType "real" ] [ dcterms:description "Fishing gear selected by the agent for a trip." ;
                                    dcterms:title "gear" ;
                                    qudt:unit "dimensionless" ;
                                    odd:range "available gear choices" ;
                                    odd:variableType "string" ] [ dcterms:description "Peers whose outcomes may be observed or imitated." ;
                                    dcterms:title "socialNetwork" ;
                                    qudt:unit "dimensionless" ;
                                    odd:range "other fishing boat agents" ;
                                    odd:variableType "list" ] ) ] [ dcterms:title "Fish biomass cell" ;
                        odd:entityType "grid-cell" ;
                        odd:scales [ odd:spatialScale "Spatially explicit ocean grid." ;
                                odd:temporalScale "Updated during each model step." ] ;
                        odd:stateVariables ( [ dcterms:description "Fish biomass available in the cell and depleted by fishing." ;
                                    dcterms:title "biomass" ;
                                    qudt:unit "mass" ;
                                    odd:range "non-negative" ;
                                    odd:variableType "real" ] [ dcterms:description "Local logistic growth parameter for the conceptual biology option." ;
                                    dcterms:title "intrinsicGrowthRate" ;
                                    qudt:unit "per time" ;
                                    odd:range "non-negative" ;
                                    odd:variableType "real" ] [ dcterms:description "Spatial redistribution pressure following local biomass gradients." ;
                                    dcterms:title "diffusionGradient" ;
                                    qudt:unit "mass per area" ;
                                    odd:range "real" ;
                                    odd:variableType "real" ] ) ] [ dcterms:title "Policy" ;
                        odd:entityType "other" ;
                        odd:scales [ odd:spatialScale "May apply to the whole fishery or selected spatial cells." ;
                                odd:temporalScale "Policy periods defined by scenario parameters." ] ;
                        odd:stateVariables ( [ dcterms:description "Parameters defining restrictions or incentives such as closures, quotas, taxes, or gear controls." ;
                                    dcterms:title "restrictionParameters" ;
                                    qudt:unit "dimensionless" ;
                                    odd:range "policy-specific parameter space" ;
                                    odd:variableType "list" ] [ dcterms:description "Objective used by the optimizer to score simulated policies." ;
                                    dcterms:title "scoringFunction" ;
                                    qudt:unit "dimensionless" ;
                                    odd:range "user-defined objective" ;
                                    odd:variableType "string" ] ) ] ) ;
            odd:initialization [ dcterms:description "The conceptual model initializes a near-shore fishery with a shoreline, one port, a spatial ocean grid containing distributed fish biomass, and a fleet of fishing boat agents. Environmental and external market modules are held constant in the conceptual examples described by the paper." ;
                    odd:randomSeed "Random seeds should be recorded for each simulation run and optimization replicate." ] ;
            odd:inputData ( [ dcterms:description "POSEIDON map initializer input: generated grid or file-backed map with cell size, map dimensions, coordinates, depth/bathymetry, coastline or land state, and optional STAC-referenced spatial assets." ;
                        dcterms:format "YAML component, CSV map, or STAC item" ;
                        dcterms:temporal "scenario-specific" ;
                        dcterms:title "Spatial fishery domain" ;
                        dcat:accessURL <bblocks://ogc.hosted.seadots.poseidon-input-map> ] [ dcterms:description "POSEIDON biology input: species names, biomass or abundance state, carrying capacity, recruitment, growth, mortality, diffusion, OSMOSE configuration, and species parameter files." ;
                        dcterms:format "YAML component, CSV parameter table, directory, or STAC item" ;
                        dcterms:temporal "t0" ;
                        dcterms:title "Biology initializer and species parameters" ;
                        dcat:accessURL <bblocks://ogc.hosted.seadots.poseidon-input-biology> ] [ dcterms:description "POSEIDON fleet input: fisher groups, vessel properties, gear, destination/departure/fishing strategies, social network, adaptation probabilities, and logbook settings." ;
                        dcterms:format "YAML component" ;
                        dcterms:temporal "simulation period" ;
                        dcterms:title "Fleet and fisher definitions" ;
                        dcat:accessURL <bblocks://ogc.hosted.seadots.poseidon-input-fleet> ] [ dcterms:description "POSEIDON port and market input: port locations, market price configuration, landing assumptions, and fuel or gas-price configuration." ;
                        dcterms:format "YAML component or CSV price table" ;
                        dcterms:temporal "simulation period" ;
                        dcterms:title "Ports, markets, and fuel prices" ;
                        dcat:accessURL <bblocks://ogc.hosted.seadots.poseidon-input-port-market> ] [ dcterms:description "POSEIDON management input: closures, quotas, protected areas, gear restrictions, action-specific regulations, conditional rules, and exogenous shocks." ;
                        dcterms:format "YAML component or policy file" ;
                        dcterms:temporal "simulation period" ;
                        dcterms:title "Regulations, policy files, and shocks" ;
                        dcat:accessURL <bblocks://ogc.hosted.seadots.poseidon-input-regulation-policy> ] [ dcterms:description "POSEIDON EVA optimization input: base scenario, parameter adaptors, parameter bounds, objective function, simulation budget, seeds, and replicate strategy." ;
                        dcterms:format "YAML optimization problem" ;
                        dcterms:temporal "experiment period" ;
                        dcterms:title "Optimization problem" ;
                        dcat:accessURL <bblocks://ogc.hosted.seadots.poseidon-input-optimization> ] [ dcterms:description "POSEIDON output-selection input: indicators, output columns, time-series cadence, loggers, and output product declarations." ;
                        dcterms:format "YAML or command/run configuration" ;
                        dcterms:temporal "simulation period" ;
                        dcterms:title "Observation and output selection" ;
                        dcat:accessURL <bblocks://ogc.hosted.seadots.poseidon-input-observation-output> ] ) ;
            odd:patterns ( [ dcterms:description "Fishing agents alter whether, where, and how they fish in response to profit opportunities, social information, biomass depletion, and imposed policy constraints." ;
                        dcterms:references <https://doi.org/10.1007/s11625-018-0579-9> ;
                        dcterms:title "Adaptive fleet redistribution under policy constraints" ] [ dcterms:description "Fishing boats choose between continuing successful behaviour, copying more successful peers, or exploring alternatives, producing group-level adaptation without policy-specific response rules." ;
                        dcterms:references <https://doi.org/10.1007/s11625-018-0579-9> ;
                        dcterms:title "Explore-exploit-imitate decision behaviour" ] [ dcterms:description "Different scoring functions and constraints can produce trade-offs among catch, conservation, equity, and other management outcomes." ;
                        dcterms:references <https://doi.org/10.1007/s11625-018-0579-9> ;
                        dcterms:title "Policy objective trade-offs" ] ) ;
            odd:processOverview [ odd:processes ( [ dcterms:description "Agent decides whether to leave port and participate in fishing for the day." ;
                                dcterms:title "Choose fishing activity" ;
                                odd:executedBy "Fishing boat" ] [ dcterms:description "Agent applies an explore-exploit-imitate decision routine using its own outcomes and social-network information." ;
                                dcterms:title "Choose fishing location and gear" ;
                                odd:executedBy "Fishing boat" ] [ dcterms:description "Catch, costs, policy effects, and sales revenue determine the outcome that reinforces future choices." ;
                                dcterms:title "Harvest and profit accounting" ;
                                odd:executedBy "Fishing boat" ] [ dcterms:description "Local fish biomass grows according to a logistic model and diffuses spatially along gradients in the conceptual implementation." ;
                                dcterms:title "Biomass growth and diffusion" ;
                                odd:executedBy "Fish biomass cell" ] [ dcterms:description "Bayesian optimization proposes policy parameters, evaluates model runs with a scoring function, and searches for high-scoring policy designs." ;
                                dcterms:title "Policy parameter optimization" ;
                                odd:executedBy "Policy" ] ) ;
                    odd:scheduling "At each daily step, fishing agents decide whether to fish, where to fish, and which gear to use; fishing depletes local biomass; biomass grows and diffuses according to the selected ecology submodel; policy rules constrain or incentivize choices; policy optimization runs multiple simulations and updates candidate parameters between runs." ] ;
            odd:purpose "POSEIDON was developed to support computational policy design for ocean fisheries as coupled human-environment systems. The conceptual model is intended to explore how adaptive fishing fleets respond to policy constraints and incentives, and how automated optimization can identify parameterized policies that meet user-defined management objectives." ;
            odd:submodels ( [ dcterms:description "Fishing agents select actions by continuing a successful option, copying a more successful member of their social network, or exploring another option." ;
                        dcterms:title "Explore-exploit-imitate fleet behaviour" ;
                        rdfs:seeAlso ( [ dcterms:title "POSEIDON paper" ;
                                    schema:url <https://doi.org/10.1007/s11625-018-0579-9> ;
                                    odd:linkRel "describedby" ] ) ;
                        odd:equations "Algorithmic multi-armed bandit style decision rule; see supplementary material for pseudocode." ;
                        odd:parameterization "Requires probabilities or hyper-parameters controlling exploration, exploitation, imitation, memory decay, and social-network influence." ] [ dcterms:description "Conceptual examples use local logistic biomass growth and diffusion along spatial gradients, with fishing pressure depleting biomass." ;
                        dcterms:title "Spatial fish biomass" ;
                        rdfs:seeAlso ( [ dcterms:title "POSEIDON paper" ;
                                    schema:url <https://doi.org/10.1007/s11625-018-0579-9> ;
                                    odd:linkRel "describedby" ] ) ;
                        odd:equations "Local logistic growth plus spatial diffusion and harvest loss." ;
                        odd:parameterization "Growth, carrying capacity, diffusion, catchability, and harvest parameters are scenario-specific; the paper also notes OSMOSE as a more sophisticated biology option." ] [ dcterms:description "An optimizer iteratively selects policy parameter combinations, runs the model, updates a surrogate meta-model of policy performance, and searches for high-scoring policies." ;
                        dcterms:title "Bayesian policy optimization" ;
                        rdfs:seeAlso ( [ dcterms:title "POSEIDON paper" ;
                                    schema:url <https://doi.org/10.1007/s11625-018-0579-9> ;
                                    odd:linkRel "describedby" ] ) ;
                        odd:equations "Black-box optimization of a scoring function over policy parameter space." ;
                        odd:parameterization "Requires a scoring function, policy parameter bounds, simulation budget, convergence criteria, and replicate design." ] ) ] ;
    odd:variableType "Feature",
        "SoftwareApplication" ;
    pos:metadata [ dcterms:source [ dcterms:bibliographicCitation "Bailey, R.M., Carrella, E., Axtell, R. et al. A computational approach to managing coupled human-environmental systems: the POSEIDON model of ocean fisheries. Sustainability Science 14, 259-275 (2019)." ;
                    dcterms:issued "2018-06-09"^^xsd:date ;
                    dcterms:license "https://creativecommons.org/licenses/by/4.0/" ;
                    bibo:doi <https://doi.org/10.1007/s11625-018-0579-9> ;
                    schema:encoding ( [ dcterms:title "Electronic supplementary material" ;
                                schema:url <https://link.springer.com/article/10.1007/s11625-018-0579-9#Sec25> ;
                                odd:linkRel "describedby" ] ) ] ;
            osc:OpenScienceResource [ prov:generated ( [ a <http://purl.org/wf4ever/wfprov#application/geo+json> ;
                                dcterms:title "Example optimized policy outputs" ;
                                schema:url <https://example.org/records/poseidon-optimized-policy-products> ;
                                odd:linkRel "result" ] ) ;
                    prov:used [ dcterms:title "Example POSEIDON policy optimization workflow" ;
                            schema:url <https://example.org/ogcapi/processes/poseidon-policy-optimization> ;
                            odd:linkRel "workflow" ;
                            odd:variableType "application/json" ] ;
                    prov:wasGeneratedBy ( [ a <http://purl.org/wf4ever/wfprov#application/geo+json> ;
                                dcterms:title "Example seasonal closure optimization experiment" ;
                                schema:url <https://example.org/records/poseidon-seasonal-closure-experiment> ;
                                odd:linkRel "experiment" ] ) ] ;
            osc:reproducibility [ pos:calibration "The implementation is executable; site-specific deployments should calibrate biological, economic, behavioural, spatial, and policy parameters against local data." ;
                    pos:implementationStatus "executable-implementation" ;
                    pos:randomSeedPolicy "Record a seed for each model run and optimization replicate." ;
                    pos:runProtocol "Define policy parameter bounds, initialize the spatial fishery and fleet, run replicate simulations for proposed policies, evaluate the scoring function, and update the Bayesian optimizer until the configured simulation budget or convergence condition is met." ] ;
            pos:modelRole "coupled-human-environment-fisheries-policy-model" ;
            pos:policyOptimization [ pos:decisionVariables ( [ dcterms:description "Start day of a seasonal fishery closure policy." ;
                                dcterms:title "seasonStart" ;
                                qudt:unit "day-of-year" ;
                                odd:range "1..365" ] [ dcterms:description "End day of a seasonal fishery closure policy." ;
                                dcterms:title "seasonEnd" ;
                                qudt:unit "day-of-year" ;
                                odd:range "1..365" ] [ dcterms:description "Additional tunable policy controls for hybrid policies." ;
                                dcterms:title "policyHybridParameters" ;
                                qudt:unit "dimensionless" ;
                                odd:range "scenario-specific" ] ) ;
                    pos:objectiveFunction "User-defined scoring function over simulated policy outcomes." ;
                    pos:optimizationMethod "Bayesian optimization" ;
                    pos:outputs ( "policy score" "catch" "effort distribution" "profit" "fish biomass" "optimized policy parameters" ) ] ;
            pos:spatialSupport [ stac:Collection ( [ a <file:///github/workspace/application/json> ;
                                dcterms:title "Example STAC collection for POSEIDON spatial domain assets" ;
                                schema:url <https://example.org/stac/collections/poseidon-fishery-domain> ;
                                odd:linkRel "derived-from" ] ) ;
                    stac:Item ( [ dcterms:title "Example initial biomass raster item" ;
                                schema:url <https://example.org/stac/collections/poseidon-fishery-domain/items/initial-biomass> ;
                                odd:linkRel "input" ;
                                odd:variableType "application/geo+json" ] ) ] ] ;
    rec:format [ dcterms:title "ODD record" ] ;
    rec:language [ skos:prefLabel "English" ;
            rec:languageCode "en" ] ;
    rec:scopedIdentifier [ rec:id "https://github.com/poseidon-fisheries/POSEIDON" ;
            rec:scheme "github" ],
        [ rec:id "10.1007/s11625-018-0579-9" ;
            rec:scheme "doi" ],
        [ rec:id "https://link.springer.com/article/10.1007/s11625-018-0579-9" ;
            rec:scheme "url" ] ;
    rec:themes [ rec:concept [ rec:conceptID "coupled-human-environment-system"^^xsd:string ],
                [ rec:conceptID "agent-based-modelling"^^xsd:string ],
                [ rec:conceptID "fisheries-policy"^^xsd:string ],
                [ rec:conceptID "bayesian-optimization"^^xsd:string ] ;
            rec:scheme "https://w3id.org/iliad/seadots/poseidon/themes/" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: POSEIDON Fisheries Model ODD Record
description: 'Profile of the SeaDOTs ODD Protocol Description Record for the implemented
  POSEIDON coupled human-environment fisheries model described by Bailey et al. (2019)
  and maintained at https://github.com/poseidon-fisheries/POSEIDON. The profile keeps
  the ODD structure as the normative model description and adds constrained hooks
  for explicit model inputs, STAC spatial assets, and Open Science reproducibility
  resources.

  '
allOf:
- $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/odd-protocol/schema.yaml
type: object
required:
- id
- type
- properties
properties:
  id:
    type: string
    format: uri
  type:
    const: Feature
    x-jsonld-id: https://w3id.org/iliad/odd#variableType
  geometry:
    description: 'Spatial footprint of the model domain. Use null when the record
      describes the generic conceptual model rather than a site-specific deployment.

      '
    oneOf:
    - type: 'null'
    - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/schema.yaml
  properties:
    type: object
    required:
    - title
    - description
    - odd
    - poseidon
    properties:
      odd:
        type: object
        required:
        - purpose
        - entities
        - processOverview
        - designConcepts
        - initialization
        - inputData
        - submodels
        x-jsonld-id: https://w3id.org/iliad/odd#
      poseidon:
        type: object
        description: 'POSEIDON-specific metadata that complements, but does not replace,
          the ODD description.

          '
        required:
        - modelRole
        - publication
        - policyOptimization
        - reproducibility
        - implementation
        properties:
          modelRole:
            type: string
            const: coupled-human-environment-fisheries-policy-model
            x-jsonld-id: https://w3id.org/iliad/seadots/poseidon#modelRole
          publication:
            type: object
            required:
            - doi
            - citation
            - published
            - license
            properties:
              doi:
                type: string
                const: https://doi.org/10.1007/s11625-018-0579-9
                x-jsonld-id: http://purl.org/ontology/bibo/doi
                x-jsonld-type: '@id'
              citation:
                type: string
                x-jsonld-id: http://purl.org/dc/terms/bibliographicCitation
              published:
                type: string
                format: date
                x-jsonld-id: http://purl.org/dc/terms/issued
                x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
              license:
                type: string
                format: uri
              supplementaryMaterial:
                type: array
                items:
                  $ref: '#/$defs/link'
                x-jsonld-id: https://schema.org/encoding
                x-jsonld-container: '@list'
            x-jsonld-id: http://purl.org/dc/terms/source
          policyOptimization:
            type: object
            required:
            - method
            - objectiveFunction
            - decisionVariables
            - outputs
            properties:
              method:
                type: string
                enum:
                - Bayesian optimization
                - management strategy evaluation
                - other
                x-jsonld-id: https://w3id.org/iliad/seadots/poseidon#optimizationMethod
              objectiveFunction:
                type: string
                x-jsonld-id: https://w3id.org/iliad/seadots/poseidon#objectiveFunction
              decisionVariables:
                type: array
                minItems: 1
                items:
                  type: object
                  required:
                  - name
                  - description
                  properties:
                    name:
                      type: string
                      x-jsonld-id: http://purl.org/dc/terms/title
                    description:
                      type: string
                      x-jsonld-id: http://purl.org/dc/terms/description
                    unit:
                      type: string
                      x-jsonld-id: http://qudt.org/schema/qudt/unit
                    range:
                      type: string
                      x-jsonld-id: https://w3id.org/iliad/odd#range
                x-jsonld-id: https://w3id.org/iliad/seadots/poseidon#decisionVariables
                x-jsonld-container: '@list'
              outputs:
                type: array
                minItems: 1
                items:
                  type: string
                x-jsonld-id: https://w3id.org/iliad/seadots/poseidon#outputs
                x-jsonld-container: '@list'
            x-jsonld-id: https://w3id.org/iliad/seadots/poseidon#policyOptimization
          spatialSupport:
            type: object
            description: 'STAC-based description of rasters, grids, domains, or other
              spatial assets that parameterize a POSEIDON deployment.

              '
            properties:
              stacCollections:
                type: array
                items:
                  oneOf:
                  - $ref: '#/$defs/link'
                  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
                x-jsonld-id: https://w3id.org/ogc/stac/Collection
                x-jsonld-container: '@list'
              stacItems:
                type: array
                items:
                  oneOf:
                  - $ref: '#/$defs/link'
                  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
                  - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item-prov/schema.yaml
                x-jsonld-id: https://w3id.org/ogc/stac/Item
                x-jsonld-container: '@list'
            x-jsonld-id: https://w3id.org/iliad/seadots/poseidon#spatialSupport
          openScience:
            type: object
            description: 'References to Open Science building block resources used
              to package repeatable POSEIDON runs, experiments, workflows, and outputs.

              '
            properties:
              workflow:
                oneOf:
                - $ref: '#/$defs/link'
                - $ref: https://ogcincubator.github.io/bblocks-openscience/build/annotated/osc/geodcat-stac-earthcode/workflows/schema.yaml
                - $ref: https://ogcincubator.github.io/bblocks-openscience/build/annotated/osc/application-package/schema.yaml
                x-jsonld-id: http://www.w3.org/ns/prov#used
              experiments:
                type: array
                items:
                  oneOf:
                  - $ref: '#/$defs/link'
                  - $ref: https://ogcincubator.github.io/bblocks-openscience/build/annotated/osc/geodcat-stac-earthcode/experiments/schema.yaml
                x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
                x-jsonld-container: '@list'
              products:
                type: array
                items:
                  oneOf:
                  - $ref: '#/$defs/link'
                  - $ref: https://ogcincubator.github.io/bblocks-openscience/build/annotated/osc/geodcat-stac-earthcode/products/schema.yaml
                x-jsonld-id: http://www.w3.org/ns/prov#generated
                x-jsonld-container: '@list'
            x-jsonld-id: https://github.com/ILIAD-ocean-twin/OIM/blob/main/openscience#OpenScienceResource
          reproducibility:
            type: object
            required:
            - implementationStatus
            - randomSeedPolicy
            - runProtocol
            properties:
              implementationStatus:
                type: string
                enum:
                - conceptual-paper
                - executable-implementation
                - site-specific-deployment
                x-jsonld-id: https://w3id.org/iliad/seadots/poseidon#implementationStatus
              randomSeedPolicy:
                type: string
                x-jsonld-id: https://w3id.org/iliad/seadots/poseidon#randomSeedPolicy
              runProtocol:
                type: string
                x-jsonld-id: https://w3id.org/iliad/seadots/poseidon#runProtocol
              calibration:
                type: string
                x-jsonld-id: https://w3id.org/iliad/seadots/poseidon#calibration
            x-jsonld-id: https://github.com/ILIAD-ocean-twin/OIM/blob/main/openscience#reproducibility
          implementation:
            type: object
            required:
            - repository
            - language
            - license
            - inputBlocks
            properties:
              repository:
                type: string
                format: uri
              language:
                type: string
              license:
                type: string
                format: uri
              inputBlocks:
                type: object
                required:
                - runControl
                - scenario
                - map
                - biology
                - fleet
                - portMarket
                - regulationPolicy
                - optimization
                - observationOutput
                properties:
                  runControl:
                    $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-run-control/schema.yaml
                  scenario:
                    $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-scenario/schema.yaml
                  map:
                    $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-map/schema.yaml
                  biology:
                    $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-biology/schema.yaml
                  fleet:
                    $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-fleet/schema.yaml
                  portMarket:
                    $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-port-market/schema.yaml
                  regulationPolicy:
                    $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-regulation-policy/schema.yaml
                  optimization:
                    $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-optimization/schema.yaml
                  observationOutput:
                    $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-observation-output/schema.yaml
        x-jsonld-id: https://w3id.org/iliad/seadots/poseidon#metadata
$defs:
  link:
    type: object
    required:
    - href
    properties:
      href:
        type: string
        format: uri
        x-jsonld-id: https://schema.org/url
        x-jsonld-type: '@id'
      rel:
        type: string
        x-jsonld-id: https://w3id.org/iliad/odd#linkRel
      title:
        type: string
        x-jsonld-id: http://purl.org/dc/terms/title
      type:
        type: string
        x-jsonld-id: https://w3id.org/iliad/odd#variableType
    additionalProperties: true
x-jsonld-extra-terms:
  purpose: https://w3id.org/iliad/odd#purpose
  patterns:
    x-jsonld-id: https://w3id.org/iliad/odd#patterns
    x-jsonld-container: '@list'
  entities:
    x-jsonld-id: https://w3id.org/iliad/odd#entities
    x-jsonld-container: '@list'
  processOverview: https://w3id.org/iliad/odd#processOverview
  designConcepts: https://w3id.org/iliad/odd#designConcepts
  initialization: https://w3id.org/iliad/odd#initialization
  inputData:
    x-jsonld-id: https://w3id.org/iliad/odd#inputData
    x-jsonld-container: '@list'
  submodels:
    x-jsonld-id: https://w3id.org/iliad/odd#submodels
    x-jsonld-container: '@list'
  reference:
    x-jsonld-id: http://purl.org/dc/terms/references
    x-jsonld-type: '@id'
  entityType: https://w3id.org/iliad/odd#entityType
  stateVariables:
    x-jsonld-id: https://w3id.org/iliad/odd#stateVariables
    x-jsonld-container: '@list'
  scales: https://w3id.org/iliad/odd#scales
  spatial: https://w3id.org/iliad/odd#spatialScale
  temporal: https://w3id.org/iliad/odd#temporalScale
  vocabularyTerm:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#exactMatch
    x-jsonld-type: '@id'
  scheduling: https://w3id.org/iliad/odd#scheduling
  processes:
    x-jsonld-id: https://w3id.org/iliad/odd#processes
    x-jsonld-container: '@list'
  executedBy: https://w3id.org/iliad/odd#executedBy
  basicPrinciples: https://w3id.org/iliad/odd#basicPrinciples
  emergence: https://w3id.org/iliad/odd#emergence
  adaptation: https://w3id.org/iliad/odd#adaptation
  objectives: https://w3id.org/iliad/odd#objectives
  learning: https://w3id.org/iliad/odd#learning
  prediction: https://w3id.org/iliad/odd#prediction
  sensing: https://w3id.org/iliad/odd#sensing
  interaction: https://w3id.org/iliad/odd#interaction
  stochasticity: https://w3id.org/iliad/odd#stochasticity
  collectives: https://w3id.org/iliad/odd#collectives
  observation: https://w3id.org/iliad/odd#observation
  seed: https://w3id.org/iliad/odd#randomSeed
  source:
    x-jsonld-id: http://www.w3.org/ns/dcat#accessURL
    x-jsonld-type: '@id'
  format: http://purl.org/dc/terms/format
  temporalCoverage: http://purl.org/dc/terms/temporal
  equations: https://w3id.org/iliad/odd#equations
  parameterization: https://w3id.org/iliad/odd#parameterization
  links:
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
    x-jsonld-type: '@id'
    x-jsonld-container: '@list'
x-jsonld-prefixes:
  bibo: http://purl.org/ontology/bibo/
  xsd: http://www.w3.org/2001/XMLSchema#
  odd: https://w3id.org/iliad/odd#
  dcterms: http://purl.org/dc/terms/
  qudt: http://qudt.org/schema/qudt/
  skos: http://www.w3.org/2004/02/skos/core#
  dcat: http://www.w3.org/ns/dcat#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  schema: https://schema.org/
  pos: https://w3id.org/iliad/seadots/poseidon#
  stac: https://w3id.org/ogc/stac/
  osc: https://github.com/ILIAD-ocean-twin/OIM/blob/main/openscience#
  prov: http://www.w3.org/ns/prov#
  sosa: http://www.w3.org/ns/sosa/
  foaf: http://xmlns.com/foaf/0.1/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-model/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-model/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
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
    "type": "https://w3id.org/iliad/odd#variableType",
    "id": "@id",
    "properties": "@nest",
    "geometry": {
      "@context": {
        "type": "@type",
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
    "purpose": "https://w3id.org/iliad/odd#purpose",
    "patterns": {
      "@id": "https://w3id.org/iliad/odd#patterns",
      "@container": "@list"
    },
    "entities": {
      "@id": "https://w3id.org/iliad/odd#entities",
      "@container": "@list"
    },
    "processOverview": "https://w3id.org/iliad/odd#processOverview",
    "designConcepts": "https://w3id.org/iliad/odd#designConcepts",
    "initialization": "https://w3id.org/iliad/odd#initialization",
    "inputData": {
      "@id": "https://w3id.org/iliad/odd#inputData",
      "@container": "@list"
    },
    "submodels": {
      "@id": "https://w3id.org/iliad/odd#submodels",
      "@container": "@list"
    },
    "reference": {
      "@id": "dct:references",
      "@type": "@id"
    },
    "entityType": "https://w3id.org/iliad/odd#entityType",
    "stateVariables": {
      "@id": "https://w3id.org/iliad/odd#stateVariables",
      "@container": "@list"
    },
    "scales": "https://w3id.org/iliad/odd#scales",
    "spatial": "https://w3id.org/iliad/odd#spatialScale",
    "temporal": "https://w3id.org/iliad/odd#temporalScale",
    "vocabularyTerm": {
      "@id": "skos:exactMatch",
      "@type": "@id"
    },
    "scheduling": "https://w3id.org/iliad/odd#scheduling",
    "processes": {
      "@id": "https://w3id.org/iliad/odd#processes",
      "@container": "@list"
    },
    "executedBy": "https://w3id.org/iliad/odd#executedBy",
    "basicPrinciples": "https://w3id.org/iliad/odd#basicPrinciples",
    "emergence": "https://w3id.org/iliad/odd#emergence",
    "adaptation": "https://w3id.org/iliad/odd#adaptation",
    "objectives": "https://w3id.org/iliad/odd#objectives",
    "learning": "https://w3id.org/iliad/odd#learning",
    "prediction": "https://w3id.org/iliad/odd#prediction",
    "sensing": "https://w3id.org/iliad/odd#sensing",
    "interaction": "https://w3id.org/iliad/odd#interaction",
    "stochasticity": "https://w3id.org/iliad/odd#stochasticity",
    "collectives": "https://w3id.org/iliad/odd#collectives",
    "observation": "https://w3id.org/iliad/odd#observation",
    "seed": "https://w3id.org/iliad/odd#randomSeed",
    "source": {
      "@id": "dcat:accessURL",
      "@type": "@id"
    },
    "format": "dct:format",
    "temporalCoverage": "dct:temporal",
    "equations": "https://w3id.org/iliad/odd#equations",
    "parameterization": "https://w3id.org/iliad/odd#parameterization",
    "odd": {
      "@context": {
        "patterns": {
          "@context": {
            "name": "dct:title"
          },
          "@id": "https://w3id.org/iliad/odd#patterns",
          "@container": "@list"
        },
        "entities": {
          "@context": {
            "name": "dct:title",
            "stateVariables": {
              "@context": {
                "unit": "qudt:unit",
                "range": "https://w3id.org/iliad/odd#range"
              },
              "@id": "https://w3id.org/iliad/odd#stateVariables",
              "@container": "@list"
            }
          },
          "@id": "https://w3id.org/iliad/odd#entities",
          "@container": "@list"
        },
        "processOverview": {
          "@context": {
            "processes": {
              "@context": {
                "name": "dct:title"
              },
              "@id": "https://w3id.org/iliad/odd#processes",
              "@container": "@list"
            }
          },
          "@id": "https://w3id.org/iliad/odd#processOverview"
        },
        "initialization": {
          "@context": {
            "links": {
              "@context": {
                "href": {
                  "@id": "schema:url",
                  "@type": "@id"
                }
              },
              "@id": "rdfs:seeAlso",
              "@type": "@id",
              "@container": "@list"
            }
          },
          "@id": "https://w3id.org/iliad/odd#initialization"
        },
        "inputData": {
          "@context": {
            "name": "dct:title"
          },
          "@id": "https://w3id.org/iliad/odd#inputData",
          "@container": "@list"
        },
        "submodels": {
          "@context": {
            "name": "dct:title",
            "links": {
              "@context": {
                "href": {
                  "@id": "schema:url",
                  "@type": "@id"
                },
                "rel": "https://w3id.org/iliad/odd#linkRel"
              },
              "@id": "rdfs:seeAlso",
              "@type": "@id",
              "@container": "@list"
            }
          },
          "@id": "https://w3id.org/iliad/odd#submodels",
          "@container": "@list"
        }
      },
      "@id": "https://w3id.org/iliad/odd#"
    },
    "poseidon": {
      "@context": {
        "modelRole": "pos:modelRole",
        "publication": {
          "@context": {
            "doi": {
              "@id": "bibo:doi",
              "@type": "@id"
            },
            "citation": "dct:bibliographicCitation",
            "published": {
              "@id": "dct:issued",
              "@type": "xsd:date"
            },
            "supplementaryMaterial": {
              "@context": {
                "href": {
                  "@id": "schema:url",
                  "@type": "@id"
                },
                "rel": "https://w3id.org/iliad/odd#linkRel"
              },
              "@id": "schema:encoding",
              "@container": "@list"
            }
          },
          "@id": "dct:source"
        },
        "policyOptimization": {
          "@context": {
            "method": "pos:optimizationMethod",
            "objectiveFunction": "pos:objectiveFunction",
            "decisionVariables": {
              "@context": {
                "name": "dct:title",
                "unit": "qudt:unit",
                "range": "https://w3id.org/iliad/odd#range"
              },
              "@id": "pos:decisionVariables",
              "@container": "@list"
            },
            "outputs": {
              "@id": "pos:outputs",
              "@container": "@list"
            }
          },
          "@id": "pos:policyOptimization"
        },
        "spatialSupport": {
          "@context": {
            "stacCollections": {
              "@context": {
                "href": {
                  "@id": "schema:url",
                  "@type": "@id"
                },
                "rel": "https://w3id.org/iliad/odd#linkRel",
                "type": "@type",
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
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  },
                  "@id": "rdfs:seeAlso"
                },
                "assets": {
                  "@context": {
                    "type": "dct:format",
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
              "@container": "@list"
            },
            "stacItems": {
              "@context": {
                "href": {
                  "@id": "schema:url",
                  "@type": "@id"
                },
                "rel": "https://w3id.org/iliad/odd#linkRel",
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
                "stac_extensions": "stac:core/hasExtension",
                "assets": {
                  "@context": {
                    "type": "dct:format",
                    "roles": {
                      "@id": "stac:core/roles",
                      "@container": "@set"
                    }
                  },
                  "@id": "stac:core/hasAsset",
                  "@container": "@set"
                },
                "entityType": "@type"
              },
              "@id": "stac:Item",
              "@container": "@list"
            }
          },
          "@id": "pos:spatialSupport"
        },
        "openScience": {
          "@context": {
            "workflow": {
              "@context": {
                "href": {
                  "@id": "schema:url",
                  "@type": "@id"
                },
                "rel": "https://w3id.org/iliad/odd#linkRel",
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
                "entityType": "@type"
              },
              "@id": "prov:used"
            },
            "experiments": {
              "@context": {
                "href": {
                  "@id": "schema:url",
                  "@type": "@id"
                },
                "rel": "https://w3id.org/iliad/odd#linkRel",
                "type": "@type",
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
                      },
                      "@container": "@set"
                    },
                    "scheme": "rec:scheme"
                  }
                },
                "stac_extensions": "stac:core/hasExtension",
                "assets": {
                  "@context": {
                    "type": "dct:format",
                    "roles": {
                      "@id": "stac:core/roles",
                      "@container": "@set"
                    }
                  },
                  "@id": "stac:core/hasAsset",
                  "@container": "@set"
                },
                "@vocab": "http://purl.org/wf4ever/wfprov#",
                "entityType": "@type",
                "describedByProcess": {
                  "@id": "wfprov:describedByProcess",
                  "@type": "@id"
                },
                "usedInput": {
                  "@id": "wfprov:usedInput",
                  "@type": "@id",
                  "@container": "@set"
                },
                "wasPartOfWorkflowRun": {
                  "@id": "wfprov:wasPartOfWorkflowRun",
                  "@type": "@id"
                },
                "wasEnactedBy": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "describedByWorkflow": {
                  "@id": "wfprov:describedByWorkflow",
                  "@type": "@id"
                },
                "hadSubProcessRun": {
                  "@reverse": "wfprov:wasPartOfWorkflowRun",
                  "@type": "@id",
                  "@container": "@set"
                }
              },
              "@id": "prov:wasGeneratedBy",
              "@container": "@list"
            },
            "products": {
              "@context": {
                "href": {
                  "@id": "schema:url",
                  "@type": "@id"
                },
                "rel": "https://w3id.org/iliad/odd#linkRel",
                "type": "@type",
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
                      },
                      "@container": "@set"
                    },
                    "scheme": "rec:scheme"
                  }
                },
                "stac_extensions": "stac:core/hasExtension",
                "assets": {
                  "@context": {
                    "type": "dct:format",
                    "roles": {
                      "@id": "stac:core/roles",
                      "@container": "@set"
                    }
                  },
                  "@id": "stac:core/hasAsset",
                  "@container": "@set"
                },
                "entityType": "@type",
                "@vocab": "http://purl.org/wf4ever/wfprov#",
                "describedByProcess": {
                  "@id": "wfprov:describedByProcess",
                  "@type": "@id"
                },
                "usedInput": {
                  "@id": "wfprov:usedInput",
                  "@type": "@id",
                  "@container": "@set"
                },
                "wasPartOfWorkflowRun": {
                  "@id": "wfprov:wasPartOfWorkflowRun",
                  "@type": "@id"
                },
                "wasEnactedBy": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "describedByWorkflow": {
                  "@id": "wfprov:describedByWorkflow",
                  "@type": "@id"
                },
                "hadSubProcessRun": {
                  "@reverse": "wfprov:wasPartOfWorkflowRun",
                  "@type": "@id",
                  "@container": "@set"
                }
              },
              "@id": "prov:generated",
              "@container": "@list"
            }
          },
          "@id": "osc:OpenScienceResource"
        },
        "reproducibility": {
          "@context": {
            "implementationStatus": "pos:implementationStatus",
            "randomSeedPolicy": "pos:randomSeedPolicy",
            "runProtocol": "pos:runProtocol",
            "calibration": "pos:calibration"
          },
          "@id": "osc:reproducibility"
        }
      },
      "@id": "pos:metadata"
    },
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "stac_version": "stac:core/version",
    "datetime": {
      "@id": "dct:date",
      "@type": "xsd:dateTime"
    },
    "start_datetime": {
      "@id": "stac:core/start_datetime",
      "@type": "xsd:dateTime"
    },
    "end_datetime": {
      "@id": "stac:core/end_datetime",
      "@type": "xsd:dateTime"
    },
    "providers": "stac:core/hasProvider",
    "media_type": "dct:format",
    "activityType": "@type",
    "agentType": "@type",
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
      "@id": "dct:provenance",
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
    "stac_extensions": "stac:core/extensions",
    "extent": "dct:extent",
    "assets": {
      "@id": "stac:core/hasAsset",
      "@container": "@id",
      "@context": {
        "href": {
          "@id": "dcat:downloadURL",
          "@type": "@id"
        },
        "type": "dct:format"
      }
    },
    "concepts": {
      "@id": "thns:concepts",
      "@container": "@set",
      "@context": {
        "name": "thns:name",
        "id": "thns:id",
        "url": "@id"
      }
    },
    "scheme": "thns:scheme",
    "ProcessRun": "wfprov:ProcessRun",
    "WorkflowRun": "wfprov:WorkflowRun",
    "wasOutputFrom": {
      "@id": "prov:generated",
      "@type": "@id",
      "@container": "@set"
    },
    "unit": {
      "@id": "qudt:hasUnit",
      "@context": {
        "@base": "http://qudt.org/vocab/unit/"
      }
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
    "thns": "stac:themes/",
    "dcterms": "http://purl.org/dc/terms/",
    "qudt": "http://qudt.org/schema/qudt/",
    "schema": "https://schema.org/",
    "sosa": "http://www.w3.org/ns/sosa/",
    "bibo": "http://purl.org/ontology/bibo/",
    "osc": "https://github.com/ILIAD-ocean-twin/OIM/blob/main/openscience#",
    "pos": "https://w3id.org/iliad/seadots/poseidon#",
    "stac": "https://w3id.org/ogc/stac/",
    "proc": "https://w3id.org/ogc/api/processes/",
    "wfprov": "http://purl.org/wf4ever/wfprov#",
    "wfdesc": "http://purl.org/wf4ever/wfdesc#",
    "cf": "stac:cf/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-model/context.jsonld)

## Sources

* [A computational approach to managing coupled human-environmental systems: the POSEIDON model of ocean fisheries](https://doi.org/10.1007/s11625-018-0579-9)
* [POSEIDON implementation repository](https://github.com/poseidon-fisheries/POSEIDON)
* [ODD Protocol Description Record](bblocks://ogc.hosted.seadots.odd-protocol)
* [OGC Building Blocks for STAC](https://ogcincubator.github.io/bblocks-stac/)
* [Open Science Workflows Building Blocks](https://ogcincubator.github.io/bblocks-openscience/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/_stage/poseidon-model`

