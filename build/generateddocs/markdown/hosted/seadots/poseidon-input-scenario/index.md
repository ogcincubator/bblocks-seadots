
# POSEIDON Scenario YAML Input (Schema)

`ogc.hosted.seadots.poseidon-input-scenario` *v0.1*

Schema for the POSEIDON scenario YAML input that wires together map, biology, fleet, ports, market, regulations, plugins, and output components.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# POSEIDON Scenario YAML Input

POSEIDON scenarios are YAML configuration documents loaded by the Java implementation. A scenario composes the spatial map, biological initializer, fleet/fisher definitions, ports and markets, regulation or policy configuration, optional plugins, and output selections.

This schema captures that composition layer and delegates detailed input structures to the dedicated POSEIDON input blocks.

## Role within the input stack

Scenario is a **composition layer**, not a data layer. It bundles references to:

- [poseidon-input-map] (spatial frame)
- [poseidon-input-biology] (population dynamics)
- [poseidon-input-fleet] (fishing agents)
- [poseidon-input-port-market] (ports, prices, fuel)
- [poseidon-input-regulation-policy] (TACs, closures, gear rules)
- [poseidon-input-observation-output] (what is logged)

Beyond composition, the scenario bblock fixes a small number of **scenario-level axes** that cannot live in a single upstream bblock because they cross several:

- **Time axis** — hindcast (Copernicus reanalysis) vs forecast (Copernicus analysis-forecast or climate-projection downscaling).
- **Climate axis** — current-climate (single realisation) vs future-climate (CMIP6 SSP scenario).
- **Regulation axis** — status-quo (current EU + national rules) vs proposed (CFP reform / BSAP-target overlay).
- **Fleet axis** — current capacity vs EMFAF-supported capacity changes vs voluntary exit programmes.

The R/S/V classification is used here only for **scenario-axis sources** — the upstream data sources are already classified inside their own bblocks.

## Source availability for the pilot area

| Source | Role | Coverage of SD 27 / 29 | Provides | Feeds POSEIDON field(s) | Related bblock(s) | Format at origin | Licence |
|---|---|---|---|---|---|---|---|
| Copernicus BAL physics reanalysis (`BALTICSEA_MULTIYEAR_PHY_003_011`) | **R** for hindcast | Whole Baltic, 1993 → present | Hindcast SST/SSS/currents | Drives `biology.diffusion`, `biology.recruitment` env-coupling | [poseidon-input-biology], [poseidon-input-map] | NetCDF + ARCO Zarr | Copernicus Licence |
| Copernicus BAL physics forecast (`BALTICSEA_ANALYSISFORECAST_PHY_003_006`) | **S** alternative for prospective runs | Whole Baltic, near-real-time → ~10 days | Forecast SST/SSS/currents | Same as reanalysis but forward-looking | [poseidon-input-biology] | NetCDF + ARCO Zarr | Copernicus Licence |
| CMIP6 / Bio-ORACLE v3 climate projections | **R / S** for climate-projection forecasts | Global incl. Baltic, multi-decadal | Downscaled SST/Chl-a projections per SSP | Long-horizon forecast forcing | [poseidon-input-biology] | NetCDF + Zarr (via Bio-ORACLE) | CC-BY 4.0 |
| EU CFP reform proposals (EUR-Lex Cellar) | **S** for "proposed regulation" scenarios | EU-wide | Proposed rule changes | Triggers `regulations` and `shocks[]` overlay in [poseidon-input-regulation-policy] | [poseidon-input-regulation-policy] | EUR-Lex Cellar JSON-LD | EC Open |
| HELCOM BSAP 2021 targets | **S** for "GES-target" scenarios | Whole Baltic | Long-horizon environmental targets | Drives objective in [poseidon-input-optimization] policy search | [poseidon-input-regulation-policy], [poseidon-input-optimization] | PDF + Indicators API | CC-BY 4.0 |
| EMFAF (European Maritime, Fisheries & Aquaculture Fund) — Sweden plan | **S** for fleet-capacity scenarios | Sweden | Planned vessel-decommissioning / SSCF support | Adjusts [poseidon-input-fleet] `fishers[].count` in scenario overlay | [poseidon-input-fleet] | PDF / DG MARE portal | EC Open |
| ICES advice (forward-looking projections) | **S** for stock-projection scenarios | Baltic stocks | Short-term forecast of SSB / R / F | Validation / reference for forecast scenarios | [poseidon-input-biology] | PDF + SAG JSON | ICES Data Policy (open) |
| Held-out years of all V-role sources | **V** | Same as upstream | Out-of-sample series | Validation of scenario realism | [poseidon-input-observation-output] | mixed | mixed |

[poseidon-input-map]: ../poseidon-input-map/
[poseidon-input-biology]: ../poseidon-input-biology/
[poseidon-input-fleet]: ../poseidon-input-fleet/
[poseidon-input-port-market]: ../poseidon-input-port-market/
[poseidon-input-regulation-policy]: ../poseidon-input-regulation-policy/
[poseidon-input-observation-output]: ../poseidon-input-observation-output/
[poseidon-input-optimization]: ../poseidon-input-optimization/
[poseidon-input-run-control]: ../poseidon-input-run-control/
[poseidon-output]: ../poseidon-output/

## Two-stage transformation pipeline

### Stage A — Source → EDITO

| Source | EDITO artefact | Transformation |
|---|---|---|
| Copernicus reanalysis vs forecast Items | already EDITO-compliant (`BALTICSEA_MULTIYEAR_PHY_003_011`, `BALTICSEA_ANALYSISFORECAST_PHY_003_006`) | No copy; the scenario records which Item URI is the active forcing. |
| CMIP6 / Bio-ORACLE projections | `scenario/climate_<ssp>.zarr` | If using climate projection, regrid the chosen Bio-ORACLE / CMIP6 variable to the canonical map grid; write GeoZarr; one Item per SSP. |
| EU CFP proposals | re-uses `regulation/cfp_proposals.parquet` from [poseidon-input-regulation-policy] | No copy. |
| HELCOM BSAP indicators | re-uses `regulation/bsap_targets.parquet` | No copy. |
| EMFAF Sweden plan | `scenario/emfaf_se.parquet` | Curated table of planned capacity changes; columns `year, segment_id, vessels_added, vessels_decommissioned`. |
| ICES advice (forward) | re-uses `regulation/ices_advice.parquet` | No copy. |
| The scenario itself (composition) | `scenarios/<scenarioId>.json` (STAC Item) | Build a STAC Item whose `assets` are links to each upstream bblock Item; `properties.scenario:axes` records the chosen values along the four scenario axes (time, climate, regulation, fleet). |

### Stage B — EDITO → POSEIDON

| EDITO artefact | POSEIDON field(s) | Transformation |
|---|---|---|
| `scenarios/<scenarioId>.json` STAC Item | `scenarioType` + each top-level scenario field | The runner reads the Item, follows each asset link, and emits the corresponding POSEIDON YAML section by delegating to the relevant input bblock's Stage B. |
| Active forcing Item (reanalysis / forecast / climate) | `biology.species[].diffusion`, `biology.species[].recruitment` env-coupling | Same Stage B as in [poseidon-input-biology] — only the *source Item URI* differs across scenarios. |
| Regulation overlay (`cfp_proposals.parquet` or `bsap_targets.parquet`) | `regulations.shocks[]` | Each row → one `shocks[]` element with `applyAtYear`. |
| `emfaf_se.parquet` | `fleet` overlay (additive / subtractive over the baseline `fishers[]`) | Per `year`, modify `fishers[].count` of the matching segment. |

## Scenario axes — values used in the pilot

| Axis | Status-quo / current | Alternative |
|---|---|---|
| Time | Hindcast 2010–2023 driven by reanalysis | Forecast 2025–2055 driven by analysis-forecast (short) or CMIP6 SSP2-4.5 / SSP5-8.5 (long) |
| Climate | Current-climate (no SST trend beyond observed) | Future-climate (Bio-ORACLE SST + Chl-a under chosen SSP) |
| Regulation | Status-quo (Council TAC + MAP HCR + Tech Measures + HELCOM/Natura closures) | Proposed: + CFP reform `shocks[]`, **or** + HELCOM BSAP `shocks[]`, **or** + Sweden national MPA extension `shocks[]` |
| Fleet | Current CFR snapshot | EMFAF-supported decommissioning trajectory, **or** voluntary-exit programme |

Each scenario picks **one value per axis**; the cartesian product enumerates the runnable scenarios for sensitivity analysis.

## Required vs substitutable vs validation-only

### Required path

- A hindcast scenario requires the reanalysis forcing Item (R), all six upstream input bblocks resolved against their R-role sources, and `regulations` = status-quo (R).
- A short-horizon forecast scenario requires the analysis-forecast forcing Item (R) and may keep `regulations` = status-quo.
- A long-horizon forecast scenario requires a chosen CMIP6 SSP forcing (R) and at least one alternative `regulations` overlay (S, but mandatory for "what-if" runs).

### Substitutable (XOR per axis)

- **Time-axis forcing**: reanalysis **xor** analysis-forecast **xor** CMIP6 SSP.
- **Regulation overlay**: status-quo **xor** CFP-proposed **xor** BSAP-target **xor** national-MPA-extension. (Multiple overlays may be sequenced through `shocks[]`, but each shock is one source.)
- **Fleet overlay**: status-quo CFR snapshot **xor** EMFAF trajectory **xor** voluntary-exit programme.

### Validation-only

- ICES forward projections — sanity check that scenario SSB trajectories are bracketed by ICES short-term advice envelopes.
- Held-out years from upstream V-role series — out-of-sample comparison.

### Minimal viable scenario for the pilot

1. Map Item: north-of-Gotland 1 nm grid, EMODnet bathymetry + HELCOM + Natura 2000 closures.
2. Biology Item: FishBase + WGBFAS SAG for herring + sprat + cod.
3. Fleet Item: Swedish CFR + STECF AER + VMS-derived destination prior.
4. Port-market Item: Simrishamn + Karlskrona + Slite + Stockholm-Frihamnen + EUMOFA prices + Oil Bulletin fuel.
5. Regulation Item: 2023 Council Baltic TAC + Tech Measures + HELCOM MPA closures.
6. Observation-output Item: SSB / landings / cash-flow / effort heatmap.

The scenario STAC Item carries the four axis values: `(time=hindcast, climate=current, regulation=status-quo, fleet=status-quo)`.

## Cross-bblock contract

- `scenarioType` is a free-text class name for the POSEIDON Java factory; the **machine-readable** axis state lives in `properties.scenario:axes` of the scenario STAC Item.
- Every embedded `$ref` to an upstream bblock MUST resolve to an Item whose `proj:epsg = 4326` and whose `grid:cell_size_nm` matches the map bblock's reference grid.
- A forecast scenario MUST NOT reference V-role series whose year-range extends past `simulatedFromYear` (the runner enforces this — see [poseidon-input-run-control]).
- Climate-projection scenarios MUST also override `regulations` to *not* assume current-climate TACs — at minimum, ICES forward advice (or BSAP targets) should be wired through `shocks[]`.
- The scenario Item is the carrier consumed by [poseidon-input-run-control]'s `scenario` field — it is the single handle through which a whole run is reproduced.

## Examples

### Minimal POSEIDON scenario composition
#### json
```json
{
  "scenarioType": "Flexible Scenario",
  "map": {
    "initializerType": "Simple Map",
    "cellSizeInKilometers": 10,
    "width": 50,
    "height": 50
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
        "name": "fleet-0",
        "count": 50,
        "gear": {"type": "Random Catchability"}
      }
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-scenario/context.jsonld",
  "scenarioType": "Flexible Scenario",
  "map": {
    "initializerType": "Simple Map",
    "cellSizeInKilometers": 10,
    "width": 50,
    "height": 50
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
        "name": "fleet-0",
        "count": 50,
        "gear": {
          "type": "Random Catchability"
        }
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/iliad/seadots/poseidon/input#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] prov:used [ :cellSizeInKilometers 10 ;
            :height 50 ;
            :initializerType "Simple Map" ;
            :width 50 ],
        [ schema:about ( [ schema:name "Species 0" ;
                        :carryingCapacity 5000 ;
                        :modelType "biomass" ] ) ;
            :initializerType "Single Species Biomass" ],
        [ schema:agent ( [ schema:name "fleet-0" ;
                        :count 50 ;
                        :gear [ ] ] ) ] ;
    :scenarioType "Flexible Scenario" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: POSEIDON Scenario YAML Input
description: Main scenario document consumed by POSEIDON's YAML scenario loader.
type: object
properties:
  scenarioType:
    type: string
    description: Human-readable or implementation class name for the scenario factory.
  map:
    $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-map/schema.yaml
    x-jsonld-id: http://www.w3.org/ns/prov#used
  biology:
    $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-biology/schema.yaml
    x-jsonld-id: http://www.w3.org/ns/prov#used
  fleet:
    $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-fleet/schema.yaml
    x-jsonld-id: http://www.w3.org/ns/prov#used
  portsAndMarkets:
    $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-port-market/schema.yaml
    x-jsonld-id: http://www.w3.org/ns/prov#used
  regulations:
    $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-regulation-policy/schema.yaml
    x-jsonld-id: http://www.w3.org/ns/prov#used
  output:
    $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-observation-output/schema.yaml
    x-jsonld-id: http://www.w3.org/ns/prov#used
  plugins:
    type: array
    description: Optional POSEIDON startables, loggers, adaptors, or extensions.
    items:
      type: object
      additionalProperties: true
    x-jsonld-id: http://www.w3.org/ns/prov#used
    x-jsonld-container: '@list'
required:
- map
- biology
- fleet
additionalProperties: true
x-jsonld-vocab: https://w3id.org/iliad/seadots/poseidon/input#
x-jsonld-prefixes:
  prov: http://www.w3.org/ns/prov#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-scenario/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-scenario/schema.yaml)


# JSON-LD Context

```jsonld
{
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
    },
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
    "schema": "https://schema.org/",
    "cf": "stac:cf/",
    "qudt": "http://qudt.org/schema/qudt/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-scenario/context.jsonld)

## Sources

* [POSEIDON YAML samples](https://github.com/poseidon-fisheries/POSEIDON/tree/main/POSEIDON/inputs/YAML%20Samples)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/_stage/poseidon-input-scenario`

