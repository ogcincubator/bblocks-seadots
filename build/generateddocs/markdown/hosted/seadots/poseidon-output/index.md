
# POSEIDON Output (EDITO target) (Schema)

`ogc.hosted.seadots.poseidon-output` *v0.1*

Target schema for POSEIDON run outputs published in EDITO-compliant form: tabular time-series and agent logs as GeoParquet, gridded fields as GeoZarr, indexed by STAC. Receives the products selected by poseidon-input-observation-output.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# POSEIDON Output (EDITO target)

This building block declares the **target schema** for the outputs of a POSEIDON run, published in EDITO-compliant form. Every product is one of:

- **Tabular / time-series** → GeoParquet 1.1 (non-spatial allowed; `geometry` column present where the indicator has a spatial dimension, CRS EPSG:4326, WKB encoding).
- **Per-agent log** → GeoParquet 1.1 (`geometry` carries fisher home-port POINT, trip LINESTRING, or POLYGON of operating zone).
- **Gridded** → GeoZarr (Zarr v3 store, CF coords `time, lat, lon`, `_ARRAY_DIMENSIONS`, `spatial_ref` aux coord, time-chunked and geo-chunked variants).
- **Event log** → GeoParquet 1.1 (timestamped discrete events: closures triggered, vessel exits, regulation invocations).

All products of a single run share one **STAC Collection** (`stacCollection`); each product is its own **STAC Item**. The manifest object described by this schema is the JSON payload conventionally stored alongside the Collection as `manifest.json`.

## Relation to other bblocks

- **Input side** — [poseidon-input-observation-output] selects which `columns`, `loggers`, `cadence`, and `outputProducts` POSEIDON writes during a run. Each selection there projects to one entry of `timeSeries[]`, `agentLogs[]`, `gridded[]`, or `events[]` here.
- **Spatial frame** — `gridded[].gridRef` MUST point at the canonical grid Item declared in [poseidon-input-map]. POSEIDON gridded outputs are written on that same grid; no resampling at output time.
- **Validation** — `validationLinks[]` references the empirical series listed in [poseidon-input-biology] (V-role sources: SAG SSB time series, BITS length frequencies, OBIS occurrences) and [poseidon-input-fleet] (V-role sources: HELCOM fishing-intensity grids, AIS tracks). The model→empirical pairs and the comparison metric form the validation harness.
- **Run config provenance** — `runConfigRef` MUST resolve to the STAC Item bundling the input configuration (a Collection or Item that aggregates the `poseidon-input-*` bblocks for the run).
- **Regulation feedback** — `events[]` of type `ClosureInvocation` are co-keyed with closure IDs declared in [poseidon-input-regulation-policy] and [poseidon-input-map].

[poseidon-input-observation-output]: ../poseidon-input-observation-output/
[poseidon-input-biology]: ../poseidon-input-biology/
[poseidon-input-fleet]: ../poseidon-input-fleet/
[poseidon-input-map]: ../poseidon-input-map/
[poseidon-input-regulation-policy]: ../poseidon-input-regulation-policy/

## Container conventions

- **Object store layout**: `s3://edito-pilot/<area>/output/<runId>/<product>.{parquet|zarr}` for pilot runs.
- **STAC Collection ID**: `poseidon-output-<area>` (one Collection per pilot area; per-run Items inside).
- **MIME types**:
  - `application/vnd.apache.parquet` for GeoParquet
  - `application/vnd.zarr` (directory store) or `application/vnd.zarr+zip` (single-file)
- **GeoParquet partitioning**: `year` for long simulations; never partition on agent ID (low-cardinality fields preferred).
- **GeoZarr chunking**: `timeChunked` (1 × 720 × 512) when downstream use is spatial maps; `geoChunked` (138 × 32 × 64) when downstream use is per-cell time series. Both variants are encouraged for the fishing-effort heatmap because viewers and validation pipelines have different access patterns.
- **CRS**: EPSG:4326 across the board.

## Schema highlights

- `runId` (required) — UUID-style identifier for the run, used as the S3 prefix and as the STAC Item id suffix.
- `runConfigRef` — URI of the input bundle Item; closes the provenance loop.
- `timeSeries[]` (required, ≥1) — every selected column from the input observation-output bblock surfaces here, one per indicator. `dimension` distinguishes `global` (single series), `per-species`, `per-fisher`, `per-port`, `per-segment`.
- `agentLogs[]` — optional but recommended for fleet-rich runs; each log carries the agent type and spatial geometry.
- `gridded[]` — at least one entry for any run that uses spatial regulation, MPA evaluation, or diffusion calibration.
- `events[]` — required when regulation is enabled; carries closure-invocation, quota-binding, vessel-exit events.
- `validationLinks[]` — populated only for back-cast runs; lists model→empirical pairings and the score.

See `examples/output.json` for a complete pilot manifest.

## Examples

### Run output manifest for the north-of-Gotland pilot
#### json
```json
{
  "runId": "poseidon-pilot-2026-05-17-001",
  "runConfigRef": "https://stac.marine.copernicus.eu/collections/poseidon-config-north-gotland/items/run-001-config",
  "stacCollection": "https://stac.marine.copernicus.eu/collections/poseidon-output-north-gotland",
  "runMetadata": {
    "startedAt": "2026-05-17T08:14:00Z",
    "finishedAt": "2026-05-17T09:47:12Z",
    "simulatedFromYear": 2010,
    "simulatedToYear": 2025,
    "timeStepUnit": "day",
    "seed": 42,
    "modelVersion": "POSEIDON 2.3.1",
    "hostEnvironment": "edito-modellab-jh"
  },
  "timeSeries": [
    {
      "name": "Species 0 Biomass",
      "asset": "s3://edito-pilot/north-gotland/output/run-001/biomass.parquet",
      "mediaType": "application/vnd.apache.parquet",
      "cadence": "yearly",
      "unit": "kg",
      "dimension": "per-species",
      "stacItem": "https://stac.marine.copernicus.eu/collections/poseidon-output-north-gotland/items/run-001-biomass"
    },
    {
      "name": "Species 0 Landings",
      "asset": "s3://edito-pilot/north-gotland/output/run-001/landings.parquet",
      "mediaType": "application/vnd.apache.parquet",
      "cadence": "yearly",
      "unit": "kg",
      "dimension": "per-species"
    },
    {
      "name": "Average Cash-Flow",
      "asset": "s3://edito-pilot/north-gotland/output/run-001/cashflow.parquet",
      "mediaType": "application/vnd.apache.parquet",
      "cadence": "yearly",
      "unit": "EUR",
      "dimension": "per-segment"
    }
  ],
  "agentLogs": [
    {
      "name": "Fisher Trips",
      "asset": "s3://edito-pilot/north-gotland/output/run-001/trips.parquet",
      "mediaType": "application/vnd.apache.parquet",
      "agentType": "fisher",
      "spatialGeometry": "linestring"
    }
  ],
  "gridded": [
    {
      "name": "Fishing Effort Heatmap",
      "asset": "s3://edito-pilot/north-gotland/output/run-001/effort.zarr",
      "mediaType": "application/vnd.zarr",
      "variable": "fishing_hours",
      "unit": "h/km2/year",
      "gridRef": "https://stac.marine.copernicus.eu/collections/poseidon-map-north-gotland/items/grid-1nm",
      "cadence": "yearly"
    }
  ],
  "events": [
    {
      "name": "Closure Invocations",
      "asset": "s3://edito-pilot/north-gotland/output/run-001/closures.parquet"
    }
  ],
  "validationLinks": [
    {
      "modelProductRef": "Species 0 Biomass",
      "empiricalRef": "https://stac.marine.copernicus.eu/collections/poseidon-bio-north-gotland/items/sag-her-27-2532-ssb",
      "metric": "Pearson_r",
      "value": 0.86
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-output/context.jsonld",
  "runId": "poseidon-pilot-2026-05-17-001",
  "runConfigRef": "https://stac.marine.copernicus.eu/collections/poseidon-config-north-gotland/items/run-001-config",
  "stacCollection": "https://stac.marine.copernicus.eu/collections/poseidon-output-north-gotland",
  "runMetadata": {
    "startedAt": "2026-05-17T08:14:00Z",
    "finishedAt": "2026-05-17T09:47:12Z",
    "simulatedFromYear": 2010,
    "simulatedToYear": 2025,
    "timeStepUnit": "day",
    "seed": 42,
    "modelVersion": "POSEIDON 2.3.1",
    "hostEnvironment": "edito-modellab-jh"
  },
  "timeSeries": [
    {
      "name": "Species 0 Biomass",
      "asset": "s3://edito-pilot/north-gotland/output/run-001/biomass.parquet",
      "mediaType": "application/vnd.apache.parquet",
      "cadence": "yearly",
      "unit": "kg",
      "dimension": "per-species",
      "stacItem": "https://stac.marine.copernicus.eu/collections/poseidon-output-north-gotland/items/run-001-biomass"
    },
    {
      "name": "Species 0 Landings",
      "asset": "s3://edito-pilot/north-gotland/output/run-001/landings.parquet",
      "mediaType": "application/vnd.apache.parquet",
      "cadence": "yearly",
      "unit": "kg",
      "dimension": "per-species"
    },
    {
      "name": "Average Cash-Flow",
      "asset": "s3://edito-pilot/north-gotland/output/run-001/cashflow.parquet",
      "mediaType": "application/vnd.apache.parquet",
      "cadence": "yearly",
      "unit": "EUR",
      "dimension": "per-segment"
    }
  ],
  "agentLogs": [
    {
      "name": "Fisher Trips",
      "asset": "s3://edito-pilot/north-gotland/output/run-001/trips.parquet",
      "mediaType": "application/vnd.apache.parquet",
      "agentType": "fisher",
      "spatialGeometry": "linestring"
    }
  ],
  "gridded": [
    {
      "name": "Fishing Effort Heatmap",
      "asset": "s3://edito-pilot/north-gotland/output/run-001/effort.zarr",
      "mediaType": "application/vnd.zarr",
      "variable": "fishing_hours",
      "unit": "h/km2/year",
      "gridRef": "https://stac.marine.copernicus.eu/collections/poseidon-map-north-gotland/items/grid-1nm",
      "cadence": "yearly"
    }
  ],
  "events": [
    {
      "name": "Closure Invocations",
      "asset": "s3://edito-pilot/north-gotland/output/run-001/closures.parquet"
    }
  ],
  "validationLinks": [
    {
      "modelProductRef": "Species 0 Biomass",
      "empiricalRef": "https://stac.marine.copernicus.eu/collections/poseidon-bio-north-gotland/items/sag-her-27-2532-ssb",
      "metric": "Pearson_r",
      "value": 0.86
    }
  ]
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/iliad/seadots/poseidon/output#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix stac: <https://w3id.org/ogc/stac/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] schema:hasPart ( [ :asset "s3://edito-pilot/north-gotland/output/run-001/biomass.parquet" ;
                :cadence "yearly" ;
                :dimension "per-species" ;
                :mediaType "application/vnd.apache.parquet" ;
                :name "Species 0 Biomass" ;
                :unit "kg" ;
                stac:Item "https://stac.marine.copernicus.eu/collections/poseidon-output-north-gotland/items/run-001-biomass" ] [ :asset "s3://edito-pilot/north-gotland/output/run-001/landings.parquet" ;
                :cadence "yearly" ;
                :dimension "per-species" ;
                :mediaType "application/vnd.apache.parquet" ;
                :name "Species 0 Landings" ;
                :unit "kg" ] [ :asset "s3://edito-pilot/north-gotland/output/run-001/cashflow.parquet" ;
                :cadence "yearly" ;
                :dimension "per-segment" ;
                :mediaType "application/vnd.apache.parquet" ;
                :name "Average Cash-Flow" ;
                :unit "EUR" ] ),
        ( [ :asset "s3://edito-pilot/north-gotland/output/run-001/closures.parquet" ;
                :name "Closure Invocations" ] ),
        ( [ :asset "s3://edito-pilot/north-gotland/output/run-001/effort.zarr" ;
                :cadence "yearly" ;
                :gridRef "https://stac.marine.copernicus.eu/collections/poseidon-map-north-gotland/items/grid-1nm" ;
                :mediaType "application/vnd.zarr" ;
                :name "Fishing Effort Heatmap" ;
                :unit "h/km2/year" ;
                :variable "fishing_hours" ] ),
        ( [ :agentType "fisher" ;
                :asset "s3://edito-pilot/north-gotland/output/run-001/trips.parquet" ;
                :mediaType "application/vnd.apache.parquet" ;
                :name "Fisher Trips" ;
                :spatialGeometry "linestring" ] ) ;
    schema:identifier "poseidon-pilot-2026-05-17-001" ;
    schema:isBasedOn "https://stac.marine.copernicus.eu/collections/poseidon-config-north-gotland/items/run-001-config" ;
    schema:subjectOf ( [ :empiricalRef "https://stac.marine.copernicus.eu/collections/poseidon-bio-north-gotland/items/sag-her-27-2532-ssb" ;
                :metric "Pearson_r" ;
                :modelProductRef "Species 0 Biomass" ;
                :value 8.6e-01 ] ) ;
    :runMetadata [ :finishedAt "2026-05-17T09:47:12Z" ;
            :hostEnvironment "edito-modellab-jh" ;
            :modelVersion "POSEIDON 2.3.1" ;
            :seed 42 ;
            :simulatedFromYear 2010 ;
            :simulatedToYear 2025 ;
            :startedAt "2026-05-17T08:14:00Z" ;
            :timeStepUnit "day" ] ;
    stac:Collection "https://stac.marine.copernicus.eu/collections/poseidon-output-north-gotland" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: POSEIDON Output (EDITO target)
description: Target schema for POSEIDON run outputs published in EDITO-compliant form.
  Tabular and per-agent products are encoded as GeoParquet 1.1 (CRS EPSG:4326, WKB
  geometry where spatial). Gridded products are encoded as GeoZarr (Zarr v3, CF coords,
  `spatial_ref` aux coord). All products are indexed by a STAC Collection one-to-one
  with a POSEIDON run.
type: object
required:
- runId
- stacCollection
- timeSeries
properties:
  runId:
    type: string
    description: Unique identifier of the POSEIDON run (UUID recommended).
    x-jsonld-id: https://schema.org/identifier
  runConfigRef:
    type: string
    format: uri
    description: URI of the bundled poseidon-input-* configuration used for this run
      (typically a STAC Item that aggregates the input bblocks).
    x-jsonld-id: https://schema.org/isBasedOn
  stacCollection:
    oneOf:
    - type: string
      format: uri
    - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
    description: STAC Collection grouping all output Items for this run.
    x-jsonld-id: https://w3id.org/ogc/stac/Collection
  runMetadata:
    type: object
    properties:
      startedAt:
        type: string
        format: date-time
      finishedAt:
        type: string
        format: date-time
      simulatedFromYear:
        type: integer
      simulatedToYear:
        type: integer
      timeStepUnit:
        type: string
        enum:
        - day
        - week
        - month
        - year
      seed:
        type: integer
      modelVersion:
        type: string
      hostEnvironment:
        type: string
    additionalProperties: true
  timeSeries:
    type: array
    minItems: 1
    description: Non-spatial or aggregate time-series products as GeoParquet.
    items:
      type: object
      required:
      - name
      - asset
      - cadence
      - mediaType
      properties:
        name:
          type: string
          description: Indicator name (matches a column from poseidon-input-observation-output).
        asset:
          type: string
          format: uri
          description: S3 URI or HTTPS URI of the GeoParquet file.
        mediaType:
          type: string
          const: application/vnd.apache.parquet
        cadence:
          type: string
          enum:
          - daily
          - weekly
          - monthly
          - yearly
          - end-of-run
          - event
        unit:
          type: string
        dimension:
          type: string
          enum:
          - global
          - per-species
          - per-fisher
          - per-port
          - per-segment
        stacItem:
          oneOf:
          - type: string
            format: uri
          - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
          x-jsonld-id: https://w3id.org/ogc/stac/Item
      additionalProperties: true
    x-jsonld-id: https://schema.org/hasPart
    x-jsonld-container: '@list'
  agentLogs:
    type: array
    description: Per-agent (fisher / vessel / port) logs as GeoParquet.
    items:
      type: object
      required:
      - name
      - asset
      - mediaType
      properties:
        name:
          type: string
        asset:
          type: string
          format: uri
        mediaType:
          type: string
          const: application/vnd.apache.parquet
        agentType:
          type: string
          enum:
          - fisher
          - vessel
          - port
          - regulator
          - market
        spatialGeometry:
          type: string
          enum:
          - point
          - linestring
          - polygon
          - none
        stacItem:
          oneOf:
          - type: string
            format: uri
          - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
          x-jsonld-id: https://w3id.org/ogc/stac/Item
      additionalProperties: true
    x-jsonld-id: https://schema.org/hasPart
    x-jsonld-container: '@list'
  gridded:
    type: array
    description: Gridded model outputs as GeoZarr (Zarr v3 stores).
    items:
      type: object
      required:
      - name
      - asset
      - mediaType
      properties:
        name:
          type: string
        asset:
          type: string
          format: uri
        mediaType:
          type: string
          enum:
          - application/vnd.zarr+zip
          - application/vnd.zarr
        variable:
          type: string
          description: Name of the primary variable in the Zarr store.
        unit:
          type: string
        gridRef:
          type: string
          format: uri
          description: STAC Item URI of the canonical grid this product is aligned
            to (typically the grid declared in poseidon-input-map).
        cadence:
          type: string
          enum:
          - daily
          - weekly
          - monthly
          - yearly
          - end-of-run
          - event
        stacItem:
          oneOf:
          - type: string
            format: uri
          - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
          x-jsonld-id: https://w3id.org/ogc/stac/Item
      additionalProperties: true
    x-jsonld-id: https://schema.org/hasPart
    x-jsonld-container: '@list'
  events:
    type: array
    description: Discrete event logs (regulation invocations, closures triggered,
      vessel exits, etc.).
    items:
      type: object
      required:
      - name
      - asset
      properties:
        name:
          type: string
        asset:
          type: string
          format: uri
        mediaType:
          type: string
          const: application/vnd.apache.parquet
        stacItem:
          oneOf:
          - type: string
            format: uri
          - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
          x-jsonld-id: https://w3id.org/ogc/stac/Item
      additionalProperties: true
    x-jsonld-id: https://schema.org/hasPart
    x-jsonld-container: '@list'
  validationLinks:
    type: array
    description: References to the empirical series used for back-cast validation.
    items:
      type: object
      properties:
        modelProductRef:
          type: string
          description: Name of a timeSeries / agentLog / gridded entry above.
        empiricalRef:
          type: string
          format: uri
          description: STAC Item URI of the empirical product compared against.
        metric:
          type: string
          enum:
          - RMSE
          - MAPE
          - Pearson_r
          - Spearman_r
          - KS
          - IoU
        value:
          type: number
      additionalProperties: true
    x-jsonld-id: https://schema.org/subjectOf
    x-jsonld-container: '@list'
additionalProperties: true
x-jsonld-vocab: https://w3id.org/iliad/seadots/poseidon/output#
x-jsonld-prefixes:
  schema: https://schema.org/
  stac: https://w3id.org/ogc/stac/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-output/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-output/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/iliad/seadots/poseidon/output#",
    "runId": "schema:identifier",
    "runConfigRef": "schema:isBasedOn",
    "stacCollection": {
      "@context": {
        "stac_extensions": "stac:core/hasExtension",
        "id": "@id",
        "extent": "dct:extent",
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
      "@id": "stac:Collection"
    },
    "timeSeries": {
      "@context": {
        "stacItem": {
          "@context": {
            "id": "@id",
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
            "title": {
              "@id": "dct:title",
              "@container": "@set"
            },
            "description": {
              "@id": "dct:description",
              "@container": "@set"
            },
            "keywords": {
              "@id": "dcat:keyword",
              "@container": "@set"
            },
            "license": "dcat:license",
            "created": "dct:created",
            "updated": "dct:modified",
            "language": "rec:language",
            "languages": {
              "@container": "@set",
              "@id": "rec:languages"
            },
            "resourceLanguages": {
              "@container": "@set",
              "@id": "rec:resourceLanguages"
            },
            "externalIds": {
              "@context": {
                "scheme": "rec:scheme",
                "value": "rec:id"
              },
              "@container": "@set",
              "@id": "rec:scopedIdentifier"
            },
            "themes": {
              "@context": {
                "concepts": {
                  "@context": {
                    "id": "stac:themes/id",
                    "url": "@id"
                  },
                  "@id": "stac:themes/concepts",
                  "@container": "@set"
                },
                "scheme": "stac:themes/scheme"
              },
              "@container": "@set",
              "@id": "rec:themes"
            },
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
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                }
              },
              "@container": "@set",
              "@id": "dcat:contactPoint",
              "@type": "@id"
            },
            "rights": "dcat:rights"
          },
          "@id": "stac:Item"
        }
      },
      "@id": "schema:hasPart",
      "@container": "@list"
    },
    "agentLogs": {
      "@context": {
        "stacItem": {
          "@context": {
            "id": "@id",
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
            "title": {
              "@id": "dct:title",
              "@container": "@set"
            },
            "description": {
              "@id": "dct:description",
              "@container": "@set"
            },
            "keywords": {
              "@id": "dcat:keyword",
              "@container": "@set"
            },
            "license": "dcat:license",
            "created": "dct:created",
            "updated": "dct:modified",
            "language": "rec:language",
            "languages": {
              "@container": "@set",
              "@id": "rec:languages"
            },
            "resourceLanguages": {
              "@container": "@set",
              "@id": "rec:resourceLanguages"
            },
            "externalIds": {
              "@context": {
                "scheme": "rec:scheme",
                "value": "rec:id"
              },
              "@container": "@set",
              "@id": "rec:scopedIdentifier"
            },
            "themes": {
              "@context": {
                "concepts": {
                  "@context": {
                    "id": "stac:themes/id",
                    "url": "@id"
                  },
                  "@id": "stac:themes/concepts",
                  "@container": "@set"
                },
                "scheme": "stac:themes/scheme"
              },
              "@container": "@set",
              "@id": "rec:themes"
            },
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
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                }
              },
              "@container": "@set",
              "@id": "dcat:contactPoint",
              "@type": "@id"
            },
            "rights": "dcat:rights"
          },
          "@id": "stac:Item"
        }
      },
      "@id": "schema:hasPart",
      "@container": "@list"
    },
    "gridded": {
      "@context": {
        "stacItem": {
          "@context": {
            "id": "@id",
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
            "title": {
              "@id": "dct:title",
              "@container": "@set"
            },
            "description": {
              "@id": "dct:description",
              "@container": "@set"
            },
            "keywords": {
              "@id": "dcat:keyword",
              "@container": "@set"
            },
            "license": "dcat:license",
            "created": "dct:created",
            "updated": "dct:modified",
            "language": "rec:language",
            "languages": {
              "@container": "@set",
              "@id": "rec:languages"
            },
            "resourceLanguages": {
              "@container": "@set",
              "@id": "rec:resourceLanguages"
            },
            "externalIds": {
              "@context": {
                "scheme": "rec:scheme",
                "value": "rec:id"
              },
              "@container": "@set",
              "@id": "rec:scopedIdentifier"
            },
            "themes": {
              "@context": {
                "concepts": {
                  "@context": {
                    "id": "stac:themes/id",
                    "url": "@id"
                  },
                  "@id": "stac:themes/concepts",
                  "@container": "@set"
                },
                "scheme": "stac:themes/scheme"
              },
              "@container": "@set",
              "@id": "rec:themes"
            },
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
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                }
              },
              "@container": "@set",
              "@id": "dcat:contactPoint",
              "@type": "@id"
            },
            "rights": "dcat:rights"
          },
          "@id": "stac:Item"
        }
      },
      "@id": "schema:hasPart",
      "@container": "@list"
    },
    "events": {
      "@context": {
        "stacItem": {
          "@context": {
            "id": "@id",
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
            "title": {
              "@id": "dct:title",
              "@container": "@set"
            },
            "description": {
              "@id": "dct:description",
              "@container": "@set"
            },
            "keywords": {
              "@id": "dcat:keyword",
              "@container": "@set"
            },
            "license": "dcat:license",
            "created": "dct:created",
            "updated": "dct:modified",
            "language": "rec:language",
            "languages": {
              "@container": "@set",
              "@id": "rec:languages"
            },
            "resourceLanguages": {
              "@container": "@set",
              "@id": "rec:resourceLanguages"
            },
            "externalIds": {
              "@context": {
                "scheme": "rec:scheme",
                "value": "rec:id"
              },
              "@container": "@set",
              "@id": "rec:scopedIdentifier"
            },
            "themes": {
              "@context": {
                "concepts": {
                  "@context": {
                    "id": "stac:themes/id",
                    "url": "@id"
                  },
                  "@id": "stac:themes/concepts",
                  "@container": "@set"
                },
                "scheme": "stac:themes/scheme"
              },
              "@container": "@set",
              "@id": "rec:themes"
            },
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
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                }
              },
              "@container": "@set",
              "@id": "dcat:contactPoint",
              "@type": "@id"
            },
            "rights": "dcat:rights"
          },
          "@id": "stac:Item"
        }
      },
      "@id": "schema:hasPart",
      "@container": "@list"
    },
    "validationLinks": {
      "@id": "schema:subjectOf",
      "@container": "@list"
    },
    "stac_version": "stac:core/version",
    "keywords": "dct:subject",
    "license": "dct:license",
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
    "type": "@type",
    "title": "dct:title",
    "description": "dct:description",
    "schema": "https://schema.org/",
    "stac": "https://w3id.org/ogc/stac/",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "geojson": "https://purl.org/geojson/vocab#",
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
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-output/context.jsonld)

## Sources

* [POSEIDON implementation repository](https://github.com/poseidon-fisheries/POSEIDON)
* [EDITO-Infra Data Lake](https://edito-infra.eu/news/what-is-a-data-lake/)
* [GeoParquet 1.1 specification](https://geoparquet.org/releases/v1.1.0/)
* [OGC GeoZarr SWG](https://www.ogc.org/announcement/ogc-forms-new-geozarr-standards-working-group-to-establish-a-zarr-encoding-for-geospatial-data/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/_stage/poseidon-output`

