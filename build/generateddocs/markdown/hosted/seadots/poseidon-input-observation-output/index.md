
# POSEIDON Observation and Output Selection Input (Schema)

`ogc.hosted.seadots.poseidon-input-observation-output` *v0.1*

Schema for POSEIDON inputs that select observations, indicators, output columns, output cadence, and loggers consumed by a run.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# POSEIDON Observation and Output Selection Input

POSEIDON runs consume output-selection inputs that determine which indicators, columns, time series, or logger products are written. This input is important for reproducibility because optimization objectives and reported policy outcomes depend on which observations are collected and at what cadence.

## Target building block

The chosen observations are materialised in EDITO-compliant form by the companion target bblock [poseidon-output]. There:

- Each `columns[]` entry here becomes one entry under `timeSeries[]` or `agentLogs[]` there.
- Each `loggers[]` entry here becomes one or more `gridded[]` / `events[]` entries there, depending on the logger type (heatmap loggers → GeoZarr; event loggers → GeoParquet event log).
- Each `outputProducts[]` STAC pointer here resolves to a STAC Item under the run's output Collection.

The two bblocks are bound by `runId` (chosen at run start) and the input bundle `runConfigRef` (set at output-manifest write time).

[poseidon-output]: ../poseidon-output/

## Raw POSEIDON output → EDITO target transform

POSEIDON natively writes plain CSV and ASCII-grid files into a run directory. The transform below converts those raw files into the EDITO-compliant products declared by [poseidon-output]. A single transformer (one Python or Java step at end-of-run) is enough; nothing in POSEIDON itself needs to change.

| Raw artefact written by POSEIDON | Selection that triggers it (this bblock) | EDITO target (`poseidon-output`) | Transformation |
|---|---|---|---|
| `<run>/<column>.csv` — single time-series per `columns[]` entry, one row per step | `columns: [...]` + `cadence` | `timeSeries[]` entry, GeoParquet | Read CSV → cast to typed columns `(year, step, value)` (or `(year, species, value)` for per-species); emit Parquet partitioned by `year`. Set `dimension` based on whether the column name carries a species/fisher/segment qualifier (parsed from POSEIDON column-name conventions). |
| `<run>/yearly-results.csv` — multi-column annual table | `cadence: yearly` (default) | One `timeSeries[]` entry **per column** | Pivot wide CSV to long; produce one Parquet per column so STAC Items remain single-indicator and indexable. |
| `<run>/daily-results.csv` — multi-column daily table | `cadence: daily` | One `timeSeries[]` entry per column, `cadence: daily` | Same pivot; partition Parquet by `year`. |
| `<run>/<fisher>.csv` per fisher — trip records | `loggers: [{type: "Trip Logger"}]` or `"Detailed Fisher Logger"` | One `agentLogs[]` entry, GeoParquet | Concatenate all fisher CSVs; rebuild trip geometries (LINESTRING from successive `(lon, lat)` rows per `trip_id`); columns `cfr_id, trip_id, departure_locode, return_locode, gear, catch_kg, revenue_eur, geometry`. |
| `<run>/heatmap-<metric>-<year>.csv` or ASCII grid | `loggers: [{type: "Heatmap Logger", variable: "..."}]` | One `gridded[]` entry, GeoZarr | Stack per-year files along `time`; reproject to EPSG:4326 if not already; align to `gridRef` = canonical grid Item from [poseidon-input-map]; write Zarr v3 with `_ARRAY_DIMENSIONS`, `spatial_ref`, both `timeChunked` and `geoChunked` variants. |
| `<run>/events.csv` — discrete events | `loggers: [{type: "Event Logger"}]` | One or more `events[]` entries | Filter by `event_type`; emit one Parquet per event class (e.g. `closures.parquet`, `exits.parquet`). |
| `<run>/snapshot-<year>.yaml` / final-state CSVs | `loggers: [{type: "Snapshot Logger"}]` | `gridded[]` entry for spatial state; `timeSeries[]` entry with `cadence: end-of-run` for scalars | Per-cell snapshot → Zarr; scalar snapshot → Parquet row. |
| `<run>/config-resolved.yaml` — the parameters POSEIDON actually used | always written | `runMetadata` + `runConfigRef` on the target manifest | Parse YAML; compute SHA-256 over canonicalised form; publish as a sibling STAC Item; set `runConfigRef` to that Item's URI. |

### STAC publication

After the transform, the runner:

1. Creates STAC Collection `poseidon-output-<area>` if it does not yet exist.
2. Creates one STAC Item per Parquet/Zarr asset, with:
   - `id` = `<runId>-<productName>`
   - `properties.processing:lineage` = list of upstream input-bblock STAC Item URIs and the POSEIDON git commit hash
   - `assets.data.href` = S3 URI of the Parquet/Zarr file
   - `assets.data.type` = `application/vnd.apache.parquet` or `application/vnd.zarr`
3. Writes a top-level `manifest.json` conforming to [poseidon-output]; that JSON is what downstream consumers read.

### Validation pairing

For back-cast runs, the transformer additionally populates `validationLinks[]` on the target manifest:

- For every `columns[]` entry that has an empirical analogue declared in [poseidon-input-biology] or [poseidon-input-fleet] (V-role sources), compute the requested metric (RMSE / Pearson r / KS / IoU) against the held-out series.
- Emit one `validationLinks[]` row per pairing, referencing the empirical STAC Item and recording the metric value.

This is how the back-cast harness materialises: empirical V-role data declared as input becomes the comparison target for the output declared here.

## Selection conventions

To make the raw→target transform deterministic:

- `columns[]` strings MUST use POSEIDON's column naming convention (e.g. `"Species 0 Biomass"`, `"Average Cash-Flow"`). The transformer parses these to set `dimension` on the target.
- `loggers[].type` strings MUST match POSEIDON logger class names (see the POSEIDON repository). Unknown logger types are skipped (with a warning) rather than silently dropped.
- `cadence` set here is propagated 1:1 to the target's `cadence` field.
- `outputProducts[]` STAC pointers are passed through to the target Collection's `assets` listing; this is the place to attach derived products (figures, dashboards, reports) that the transformer itself does not generate.

## What changed vs the previous version of this bblock

Earlier versions of this bblock described only the *selection* of POSEIDON outputs (column names, cadence, logger types). The selection itself is unchanged. New here:

- An explicit **target bblock** ([poseidon-output]) that declares the EDITO-compliant shape every selected product takes on disk.
- An explicit **raw → target transform** table so a runner can deterministically convert a POSEIDON run directory into a STAC-indexed Collection of GeoParquet + GeoZarr assets.
- A **validation pairing** rule that closes the loop with the V-role sources declared in [poseidon-input-biology] and [poseidon-input-fleet].

## Examples

### Output column selection
#### json
```json
{
  "columns": [
    "Species 0 Landings",
    "Species 0 Biomass",
    "Average Cash-Flow",
    "Number Of Active Fishers"
  ],
  "cadence": "yearly",
  "loggers": [
    {
      "type": "CSV Time Series Logger"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-observation-output/context.jsonld",
  "columns": [
    "Species 0 Landings",
    "Species 0 Biomass",
    "Average Cash-Flow",
    "Number Of Active Fishers"
  ],
  "cadence": "yearly",
  "loggers": [
    {
      "type": "CSV Time Series Logger"
    }
  ]
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/iliad/seadots/poseidon/input#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .

[] schema:instrument ( [ dct:type <file:///github/workspace/> ] ) ;
    schema:variableMeasured ( "Species 0 Landings" "Species 0 Biomass" "Average Cash-Flow" "Number Of Active Fishers" ) ;
    :cadence "yearly" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: POSEIDON Observation and Output Selection Input
description: Input selecting which POSEIDON observations and output series are written.
type: object
properties:
  columns:
    type: array
    items:
      type: string
    description: Names of POSEIDON output columns, indicators, or time series.
    x-jsonld-id: https://schema.org/variableMeasured
    x-jsonld-container: '@list'
  cadence:
    type: string
    enum:
    - daily
    - yearly
    - end-of-run
    - custom
  loggers:
    type: array
    items:
      type: object
      required:
      - type
      properties:
        type:
          type: string
      additionalProperties: true
    x-jsonld-id: https://schema.org/instrument
    x-jsonld-container: '@list'
  outputProducts:
    type: array
    items:
      oneOf:
      - type: string
        format: uri
      - $ref: https://ogcincubator.github.io/bblocks-openscience/build/annotated/osc/geodcat-stac-earthcode/products/schema.yaml
    x-jsonld-id: https://schema.org/result
    x-jsonld-container: '@list'
additionalProperties: true
x-jsonld-vocab: https://w3id.org/iliad/seadots/poseidon/input#
x-jsonld-prefixes:
  schema: https://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-observation-output/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-observation-output/schema.yaml)


# JSON-LD Context

```jsonld
{
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
        "type": "@type",
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
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent"
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
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent"
              }
            }
          }
        },
        "license": "dcat:license",
        "stac_extensions": "stac:hasExtension",
        "assets": {
          "@context": {
            "type": "dct:format",
            "roles": {
              "@id": "stac:roles",
              "@container": "@set"
            }
          },
          "@id": "stac:hasAsset",
          "@container": "@set"
        },
        "name": "cf:name",
        "rights": "dcat:rights"
      },
      "@id": "schema:result",
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
    "time": {
      "@id": "dct:temporal",
      "@context": {
        "interval": {
          "@id": "w3ctime:hasTime",
          "@container": "@list"
        },
        "resolution": "rec:iso8601period"
      }
    },
    "created": "dct:created",
    "updated": "dct:modified",
    "type": {
      "@id": "dct:type",
      "@type": "@id"
    },
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
    "conformsTo": {
      "@container": "@set",
      "@id": "dct:conformsTo",
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
          "@id": "thns:concepts",
          "@context": {
            "id": {
              "@type": "xsd:string",
              "@id": "thns:id"
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
    "license": "dct:license",
    "accessrights": "dct:accessRights",
    "linkTemplates": "rec:hasLinkTemplate",
    "variables": {
      "@container": "@id",
      "@id": "rec:hasVariable",
      "@context": {
        "@base": "http://example.com/variables/",
        "@vocab": "https://www.opengis.net/def/ogc-api/records/"
      }
    },
    "stac_version": "stac:version",
    "stac_extensions": "stac:extensions",
    "extent": "dct:extent",
    "links": "rdfs:seeAlso",
    "assets": {
      "@id": "stac:hasAsset",
      "@container": "@id",
      "@context": {
        "href": {
          "@id": "dcat:downloadURL",
          "@type": "@id"
        },
        "type": "dct:format"
      }
    },
    "start_datetime": {
      "@id": "stac:start_datetime",
      "@type": "xsd:dateTime"
    },
    "end_datetime": {
      "@id": "stac:end_datetime",
      "@type": "xsd:dateTime"
    },
    "providers": "stac:hasProvider",
    "media_type": "dct:format",
    "datetime": {
      "@id": "dct:date",
      "@type": "xsd:dateTime"
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
    "id": "@id",
    "name": "rdfs:label",
    "unit": {
      "@id": "qudt:hasUnit",
      "@context": {
        "@base": "http://qudt.org/vocab/unit/"
      }
    },
    "schema": "https://schema.org/",
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
    "stac": "https://w3id.org/ogc/stac/core/",
    "cf": "https://w3id.org/ogc/stac/cf/",
    "qudt": "http://qudt.org/schema/qudt/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-observation-output/context.jsonld)

## Sources

* [POSEIDON implementation repository](https://github.com/poseidon-fisheries/POSEIDON)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/_stage/poseidon-input-observation-output`

