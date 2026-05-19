
# POSEIDON Run Control Input (Schema)

`ogc.hosted.seadots.poseidon-input-run-control` *v0.1*

Schema for the top-level run controls consumed by the POSEIDON Java implementation: scenario file, optional policy or shock files, seed, run length, replicate count, output directory, and output-selection input.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# POSEIDON Run Control Input

This building block describes the top-level controls needed to execute the implemented POSEIDON model: which scenario YAML to load, whether an additional policy or shock file is applied, how long to run, which random seed and replicate count to use, and where outputs are written.

It intentionally references the other POSEIDON input blocks instead of expanding every scenario component inline.

## Role within the input stack

Run-control is the **orchestration glue**: it does not carry external observational data itself. Instead, it composes upstream input bblocks ([poseidon-input-scenario], [poseidon-input-regulation-policy], [poseidon-input-observation-output]) into a launchable bundle and decides three orthogonal axes:

- **Time horizon** — `yearsToRun` and the implied calendar window.
- **Stochasticity** — `randomSeed` + `replicates`.
- **Output sink** — `outputDirectory` (EDITO S3 prefix) and `outputSelection` (which observations).

Because the data inputs live in upstream bblocks, the R/S/V classification used elsewhere does not apply here in the same way. Instead, this bblock has **time-window constraints** imposed by the availability windows of upstream V-role sources.

## Time-window constraints inherited from upstream sources

| Constraint | Origin bblock | Available range | Effect on `yearsToRun` / scenario start |
|---|---|---|---|
| Copernicus BAL physics reanalysis | [poseidon-input-scenario] (via [poseidon-input-biology]/[poseidon-input-map]) | 1993 → present minus 1 year | Earliest hindcast start year = 1993 |
| Copernicus BAL physics forecast | [poseidon-input-scenario] | Present → ~10 days ahead; seasonal forecast extends further | Forecast horizon caps `yearsToRun` for prospective runs unless climate downscaling is plugged in |
| ICES WGBFAS SAG time series | [poseidon-input-biology] (R) and [poseidon-input-optimization] (objective) | Typically 1980s → present for major Baltic stocks | Calibration window upper-bounded by latest assessment year |
| DATRAS BITS quarterly trawl survey | [poseidon-input-biology] (R for Abundance initializer) | 2001 (Q4 series) / 1985 (Q1 series) → present | Length-structure calibration starts no earlier than 2001 for full Q1+Q4 |
| ICES VMS / Logbook DB | [poseidon-input-fleet] (R) | 2009 → present | Spatial-effort prior earliest = 2009 (or 2012 if GFW used instead) |
| Global Fishing Watch | [poseidon-input-fleet] (S) | 2012 → 2024 (current public release) | AIS-based effort prior starts 2012 |
| EUMOFA monthly first-sale prices | [poseidon-input-port-market] (R) | 2009 → present | Revenue calibration starts no earlier than 2009 |
| EU Council Baltic TAC Regulation | [poseidon-input-regulation-policy] (R) | Annual since 1983 | TACs available across the entire reanalysis window |

The **runner-enforced rule** is: the *intersection* of the year-ranges of every R-role source actually used in the run defines the legal `yearsToRun` window. The runner validates this before launching.

## Sources specific to run-control

These do not deliver scientific data; they are run-time references.

| Source | Role | Provides | Feeds field(s) | Related bblock(s) |
|---|---|---|---|---|
| EDITO Data Lake S3 conventions | required | `s3://edito-pilot/<area>/output/<runId>/` path layout | `outputDirectory` | [poseidon-output] |
| STAC catalogue endpoint (`stac.marine.copernicus.eu`) | required | Collection / Item resolver | `scenario` URI when scenario is a STAC Item | [poseidon-input-scenario] |
| POSEIDON release version | required | Java JAR / Docker image tag | (runner metadata, not a schema field) | [poseidon-model] |
| OGC Processes API endpoint (EDITO Model Lab) | optional | Job submission endpoint | – (not in schema; recorded in `runMetadata` of [poseidon-output]) | [poseidon-output] |
| Compute environment specification | optional | CPU/RAM/replicate parallelism plan | – (advisory) | – |

[poseidon-input-scenario]: ../poseidon-input-scenario/
[poseidon-input-biology]: ../poseidon-input-biology/
[poseidon-input-fleet]: ../poseidon-input-fleet/
[poseidon-input-map]: ../poseidon-input-map/
[poseidon-input-port-market]: ../poseidon-input-port-market/
[poseidon-input-regulation-policy]: ../poseidon-input-regulation-policy/
[poseidon-input-observation-output]: ../poseidon-input-observation-output/
[poseidon-input-optimization]: ../poseidon-input-optimization/
[poseidon-output]: ../poseidon-output/
[poseidon-model]: ../poseidon-model/

## EDITO orchestration contract

When the run is launched on EDITO Model Lab via OGC Processes API:

1. **Scenario resolution** — `scenario` is a STAC Item URI that aggregates the input-bblock Items used. The runner downloads / mounts each referenced asset (Parquet, Zarr).
2. **Output path** — `outputDirectory` MUST be of the form `s3://edito-pilot/<area>/output/<runId>/` where `<runId>` is the value emitted as `runId` in the [poseidon-output] manifest.
3. **Manifest writing** — at end of run the transformer described in [poseidon-input-observation-output] writes `manifest.json` conforming to [poseidon-output] under that prefix and publishes one STAC Item per asset under `poseidon-output-<area>`.
4. **Provenance** — `runMetadata.modelVersion` and the SHA-256 of the resolved scenario config are written into the manifest; the runner also pushes a `runConfigRef` STAC Item that re-resolves to the *exact* scenario actually executed.
5. **Replicates** — `replicates > 1` produces one [poseidon-output] manifest per replicate, all sharing the same Collection; the replicate index is encoded in the Item id suffix.

## Two-stage transformation pipeline

For this bblock the "two-stage" pattern degenerates: there are no raw → EDITO transforms because run-control consumes no external observational data. The relevant pipeline is:

### Stage A — input bundle assembly (Source → EDITO)

| Input | EDITO artefact | Transformation |
|---|---|---|
| Resolved [poseidon-input-scenario] + all transitively referenced input-bblock Items | `runs/<runId>/scenario-bundle.json` (STAC Item) | Walk the scenario tree; emit a STAC Item with one `assets.<bblockname>` link per input bblock; `properties.processing:lineage` records the upstream STAC Item URIs. |

### Stage B — EDITO → POSEIDON

| EDITO artefact | POSEIDON field(s) | Transformation |
|---|---|---|
| `scenario-bundle.json` | `scenario` | Set to the bundle Item URI. |
| Optional policy bundle Item | `policy` | Set if a regulation-only Item is supplied as override. |
| `outputDirectory` | `outputDirectory` | `s3://edito-pilot/<area>/output/<runId>/` |
| `outputSelection` | `outputSelection` | URI of the [poseidon-input-observation-output] Item used. |

### Run-control choices that are *not* data-driven

| Field | Decision rule for the pilot |
|---|---|
| `yearsToRun` | 30-year back-cast (typically 1993–2023 or 2001–2023 depending on whether BITS Q4 series is used) for calibration; 30-year forecast (2025–2055) for projection. |
| `randomSeed` | Fixed for reproducibility (e.g. 42); randomised across replicates only via internal seed offsets. |
| `replicates` | 3 for production runs; 10 for noise-sensitive optimization evaluations (set by [poseidon-input-optimization]). |

## Required vs substitutable vs validation-only

The R/S/V dimension does not apply to run-control directly — it inherits constraints from upstream bblocks. The user-facing required set per run is simply:

1. A resolved `scenario` reference (R).
2. `yearsToRun` (R).
3. `outputDirectory` (R for any non-throwaway run).
4. `outputSelection` (R when [poseidon-output] is consumed downstream).

## Minimal viable bundle

1. **Scenario STAC Item** — bundle of map + biology + fleet + port-market + regulation-policy + observation-output for the pilot.
2. **`yearsToRun`** — set to the intersection of upstream V-role year-ranges (typically 2010–2023 for a Baltic back-cast).
3. **`outputDirectory`** — `s3://edito-pilot/north-gotland/output/<runId>/`.
4. **`outputSelection`** STAC Item URI — points at the [poseidon-input-observation-output] configuration used.

## Cross-bblock contract

- `scenario` MUST resolve to a [poseidon-input-scenario] Item whose `map.gridRef` matches the canonical grid used by all transitively referenced bblocks.
- `policy`, when supplied, overrides any `regulations` embedded inside `scenario` — both must use the same closure-ID space declared in [poseidon-input-map].
- `outputSelection` MUST refer to a [poseidon-input-observation-output] Item that lists exactly the columns / loggers consumed by the objective in [poseidon-input-optimization] (if optimization is used).
- The runner enforces year-range consistency by intersecting upstream R-role source windows against `yearsToRun`; a mismatch fails the job before launch.
- The [poseidon-output] manifest written under `outputDirectory` is the single artefact carried back into validation, optimization, and downstream analysis.

## Examples

### POSEIDON batch run controls
#### json
```json
{
  "scenario": "inputs/easy.yaml",
  "policy": "inputs/policies/seasonal_closure.yaml",
  "yearsToRun": 50,
  "randomSeed": 12345,
  "replicates": 20,
  "outputDirectory": "runs/seasonal-closure",
  "outputSelection": "inputs/output_columns.yaml"
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-run-control/context.jsonld",
  "scenario": "inputs/easy.yaml",
  "policy": "inputs/policies/seasonal_closure.yaml",
  "yearsToRun": 50,
  "randomSeed": 12345,
  "replicates": 20,
  "outputDirectory": "runs/seasonal-closure",
  "outputSelection": "inputs/output_columns.yaml"
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/iliad/seadots/poseidon/input#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] prov:used "inputs/easy.yaml",
        "inputs/output_columns.yaml",
        "inputs/policies/seasonal_closure.yaml" ;
    schema:contentLocation "runs/seasonal-closure" ;
    :randomSeed 12345 ;
    :replicates 20 ;
    :yearsToRun 50 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: POSEIDON Run Control Input
description: Top-level execution controls for a POSEIDON run or batch of runs.
type: object
required:
- scenario
- yearsToRun
properties:
  scenario:
    oneOf:
    - type: string
      description: Path or URI to a POSEIDON scenario YAML file.
    - $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-scenario/schema.yaml
    x-jsonld-id: http://www.w3.org/ns/prov#used
  policy:
    oneOf:
    - type: 'null'
    - type: string
      description: Path or URI to an optional policy, regulation, or shock YAML file.
    - $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-regulation-policy/schema.yaml
    x-jsonld-id: http://www.w3.org/ns/prov#used
  yearsToRun:
    type: integer
    minimum: 1
  randomSeed:
    type: integer
    description: Seed used for reproducible stochastic runs.
  replicates:
    type: integer
    minimum: 1
    default: 1
  outputDirectory:
    type: string
    x-jsonld-id: https://schema.org/contentLocation
  outputSelection:
    oneOf:
    - type: 'null'
    - type: string
    - $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-observation-output/schema.yaml
    x-jsonld-id: http://www.w3.org/ns/prov#used
additionalProperties: true
x-jsonld-vocab: https://w3id.org/iliad/seadots/poseidon/input#
x-jsonld-prefixes:
  prov: http://www.w3.org/ns/prov#
  schema: https://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-run-control/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-run-control/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/iliad/seadots/poseidon/input#",
    "scenario": {
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
    "policy": {
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
    "outputDirectory": "schema:contentLocation",
    "outputSelection": {
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
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-run-control/context.jsonld)

## Sources

* [POSEIDON implementation repository](https://github.com/poseidon-fisheries/POSEIDON)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/_stage/poseidon-input-run-control`

