
# GeoParquet Header (Schema)

`ogc.hosted.seadots.geoparquet-header` *v0.1*

Generic, reusable CSVW + GeoParquet 1.1 metadata header envelope shape (fileName, source, parquetSchema, geo). Dataset-specific GeoParquet profiles reference this schema via $ref rather than redefining the envelope inline.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# GeoParquet Header

This building block defines the generic, reusable envelope shape for a CSVW +
GeoParquet 1.1 metadata header: `fileName`, `encoding`, `source`
(`href`/`sourceFormat`/`rowCount`/`columnCount`), `parquetSchema` (per-column
`name`/`type`/`nullable`/`description`/`propertyUrl`), and `geo`
(`version`/`primary_column`/`columns`, including a `crs` block that must be
either omitted, a CRS identifier string, or a full PROJJSON object).

It exists so that dataset-specific GeoParquet profiles — such as
[Swedish DT Simulations Output](../swedish-DT-simulations-output/) and
[Harvest time series scenario Scen M3 — GeoParquet representation](../harvest-timeseries-scen-m3-geoparquet/)
— can `$ref` a single shared envelope definition instead of each redefining
it inline. The envelope was factored out of `swedish-DT-simulations-output`'s
`schema.yaml`, where it was originally defined ad hoc.

## Why `crs` is constrained

A previous dataset-specific header shipped a hand-written CRS shorthand
(`{"type": "GeographicCRS", "name": "WGS 84", "id": {"authority": "EPSG",
"code": 4326}}`) that parses as valid JSON but is not valid PROJJSON — it is
missing the `datum`/`datum_ensemble` (or `base_crs`/`source_crs`) keys a real
CRS definition requires. That header validated fine against a schema with no
`crs` constraint, but `geopandas.read_parquet()` (via `proj`) rejected the
resulting file outright with a `CRSError`. This schema's `crs` property
requires either `null` (the GeoParquet-spec default, meaning OGC:CRS84), a
plain identifier string, or an object that at minimum claims one of the keys
that makes a CRS definition complete — catching that exact mistake at schema
validation time instead of at read time.

## Producing a conformant header

- `csv-to-geoparquet` and `geojson-to-geoparquet` (ogcaibb skills) both emit
  headers that validate against this schema, and both refuse to emit the
  invalid CRS shorthand described above.

## Examples

### Generic stations GeoParquet header
#### json
```json
{
  "@context": {
    "@version": 1.1,
    "csvw": "http://www.w3.org/ns/csvw#",
    "dct": "http://purl.org/dc/terms/",
    "geo": "http://www.opengis.net/ont/geosparql#",
    "ex": "https://example.org/vocab/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "fileName": "dct:identifier",
    "encoding": "dct:format",
    "source": "dct:source",
    "href": {
      "@id": "dct:references",
      "@type": "@id"
    },
    "parquetSchema": {
      "@id": "csvw:tableSchema",
      "@container": "@list"
    },
    "name": "csvw:name",
    "description": "dct:description",
    "propertyUrl": {
      "@id": "csvw:propertyUrl",
      "@type": "@id"
    }
  },
  "fileName": "stations.parquet",
  "encoding": "GeoParquet 1.1.0; Parquet logical types; geometry encoded as WKB",
  "source": {
    "href": "examples/stations.csv",
    "sourceFormat": "text/csv",
    "rowCount": 2,
    "columnCount": 4
  },
  "parquetSchema": [
    {
      "name": "geometry",
      "type": "BYTE_ARRAY/WKB",
      "nullable": true,
      "propertyUrl": "geo:hasGeometry"
    },
    {
      "name": "station_id",
      "type": "BYTE_ARRAY/UTF8",
      "nullable": false,
      "propertyUrl": "ex:stationId"
    },
    {
      "name": "temperature",
      "type": "DOUBLE",
      "nullable": true,
      "propertyUrl": "ex:temperature"
    },
    {
      "name": "salinity",
      "type": "DOUBLE",
      "nullable": true,
      "propertyUrl": "ex:salinity"
    }
  ],
  "geo": {
    "version": "1.1.0",
    "primary_column": "geometry",
    "columns": {
      "geometry": {
        "encoding": "WKB",
        "geometry_types": [
          "Point"
        ],
        "crs": null,
        "bbox": [
          11.9,
          57.7,
          11.9,
          57.7
        ]
      }
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/geoparquet-header/context.jsonld",
    {
      "@version": 1.1,
      "csvw": "http://www.w3.org/ns/csvw#",
      "dct": "http://purl.org/dc/terms/",
      "geo": "http://www.opengis.net/ont/geosparql#",
      "ex": "https://example.org/vocab/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "fileName": "dct:identifier",
      "encoding": "dct:format",
      "source": "dct:source",
      "href": {
        "@id": "dct:references",
        "@type": "@id"
      },
      "parquetSchema": {
        "@id": "csvw:tableSchema",
        "@container": "@list"
      },
      "name": "csvw:name",
      "description": "dct:description",
      "propertyUrl": {
        "@id": "csvw:propertyUrl",
        "@type": "@id"
      }
    }
  ],
  "fileName": "stations.parquet",
  "encoding": "GeoParquet 1.1.0; Parquet logical types; geometry encoded as WKB",
  "source": {
    "href": "examples/stations.csv",
    "sourceFormat": "text/csv",
    "rowCount": 2,
    "columnCount": 4
  },
  "parquetSchema": [
    {
      "name": "geometry",
      "type": "BYTE_ARRAY/WKB",
      "nullable": true,
      "propertyUrl": "geo:hasGeometry"
    },
    {
      "name": "station_id",
      "type": "BYTE_ARRAY/UTF8",
      "nullable": false,
      "propertyUrl": "ex:stationId"
    },
    {
      "name": "temperature",
      "type": "DOUBLE",
      "nullable": true,
      "propertyUrl": "ex:temperature"
    },
    {
      "name": "salinity",
      "type": "DOUBLE",
      "nullable": true,
      "propertyUrl": "ex:salinity"
    }
  ],
  "geo": {
    "version": "1.1.0",
    "primary_column": "geometry",
    "columns": {
      "geometry": {
        "encoding": "WKB",
        "geometry_types": [
          "Point"
        ],
        "crs": null,
        "bbox": [
          11.9,
          57.7,
          11.9,
          57.7
        ]
      }
    }
  }
}
```

#### ttl
```ttl
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/vocab/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

[] dct:format "GeoParquet 1.1.0; Parquet logical types; geometry encoded as WKB" ;
    dct:identifier "stations.parquet" ;
    dct:source [ dct:references <file:///github/workspace/examples/stations.csv> ] ;
    geo: [ ] ;
    csvw:tableSchema ( [ csvw:name "geometry" ;
                csvw:propertyUrl geo:hasGeometry ] [ csvw:name "station_id" ;
                csvw:propertyUrl ex:stationId ] [ csvw:name "temperature" ;
                csvw:propertyUrl ex:temperature ] [ csvw:name "salinity" ;
                csvw:propertyUrl ex:salinity ] ) .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: GeoParquet Header
description: 'Generic CSVW + GeoParquet 1.1 metadata header envelope: describes the
  physical columns of a GeoParquet file (name, Parquet logical type, nullability,
  CSVW propertyUrl annotation) and the GeoParquet `geo` metadata block for the primary
  geometry column. This schema defines only the reusable envelope shape; dataset-specific
  column lists and semantics are defined by profiles that `$ref` this schema (e.g.
  a source-specific building block''s own GeoParquetHeader definition).

  '
type: object
required:
- fileName
- encoding
- source
- parquetSchema
- geo
properties:
  fileName:
    type: string
    pattern: \.(geo)?parquet$
    x-jsonld-id: https://schema.org/contentUrl
  encoding:
    type: string
    description: Free-text encoding statement, e.g. "GeoParquet 1.1.0; Parquet logical
      types; geometry encoded as WKB".
    x-jsonld-id: https://schema.org/encodingFormat
  source:
    type: object
    required:
    - href
    - sourceFormat
    - rowCount
    - columnCount
    properties:
      href:
        type: string
        description: Path or URL to the original source artifact this header was derived
          from.
        x-jsonld-id: http://purl.org/dc/terms/references
        x-jsonld-type: '@id'
      sourceFormat:
        type: string
        description: Media type or free-text description of the source format, e.g.
          "application/geo+json".
        x-jsonld-id: http://purl.org/dc/terms/format
      rowCount:
        type: integer
        minimum: 1
        x-jsonld-id: https://schema.org/numberOfItems
      columnCount:
        type: integer
        minimum: 1
        x-jsonld-id: https://schema.org/numberOfColumns
      note:
        type: string
        x-jsonld-id: https://schema.org/comment
    additionalProperties: true
    x-jsonld-id: http://purl.org/dc/terms/source
  parquetSchema:
    type: array
    items:
      type: object
      required:
      - name
      - type
      properties:
        name:
          type: string
          x-jsonld-id: http://www.w3.org/ns/csvw#name
        type:
          type: string
          description: Parquet logical type, e.g. INT32, INT64, FLOAT, DOUBLE, BOOLEAN,
            BYTE_ARRAY/UTF8, BYTE_ARRAY/WKB.
          x-jsonld-id: http://www.w3.org/ns/csvw#datatype
        nullable:
          type: boolean
          x-jsonld-id: https://geoparquet.org/schema#nullable
        description:
          type: string
          x-jsonld-id: http://purl.org/dc/terms/description
        propertyUrl:
          type: string
          description: CSVW-style compact IRI or full IRI naming this column's semantic
            mapping.
          x-jsonld-id: http://www.w3.org/ns/csvw#propertyUrl
          x-jsonld-type: '@id'
      additionalProperties: true
    x-jsonld-id: https://geoparquet.org/schema
    x-jsonld-container: '@list'
  geo:
    type: object
    required:
    - version
    - primary_column
    - columns
    properties:
      version:
        type: string
        x-jsonld-id: https://schema.org/version
      primary_column:
        type: string
        x-jsonld-id: https://geoparquet.org/metadata#primary_column
      columns:
        type: object
        additionalProperties:
          type: object
          required:
          - encoding
          properties:
            encoding:
              type: string
              x-jsonld-id: https://schema.org/encodingFormat
            geometry_types:
              type: array
              items:
                type: string
                enum:
                - Point
                - LineString
                - Polygon
                - MultiPoint
                - MultiLineString
                - MultiPolygon
                - GeometryCollection
              x-jsonld-id: https://geoparquet.org/metadata#geometry_types
            crs:
              description: "Must be omitted/null (defaults to OGC:CRS84), a CRS identifier
                string (e.g. \"OGC:CRS84\"), or a full PROJJSON object. A shorthand
                object that merely looks like PROJJSON (has a \"type\" but none of
                the keys that make a CRS definition complete) is exactly the authoring
                mistake that breaks real GeoParquet readers (e.g. geopandas, via proj)
                at read time \u2014 this schema rejects that shape rather than silently
                accepting it.\n"
              oneOf:
              - type: 'null'
              - type: string
              - type: object
                required:
                - type
                properties:
                  type:
                    enum:
                    - GeographicCRS
                    - ProjectedCRS
                    - GeodeticCRS
                    - CompoundCRS
                    - VerticalCRS
                    x-jsonld-id: http://www.w3.org/ns/csvw#datatype
                anyOf:
                - required:
                  - datum
                - required:
                  - datum_ensemble
                - required:
                  - base_crs
                - required:
                  - source_crs
              x-jsonld-id: https://geoparquet.org/metadata#crs
            edges:
              type: string
              enum:
              - planar
              - spherical
              x-jsonld-id: https://geoparquet.org/metadata#edges
            orientation:
              type: string
              x-jsonld-id: https://geoparquet.org/metadata#orientation
            bbox:
              type: array
              items:
                type: number
              minItems: 4
              maxItems: 4
              x-jsonld-id: https://geoparquet.org/metadata#bbox
            covering:
              type: object
              x-jsonld-id: https://geoparquet.org/metadata#covering
          additionalProperties: true
        x-jsonld-id: https://geoparquet.org/metadata#columns
    additionalProperties: true
    x-jsonld-id: https://geoparquet.org/metadata
additionalProperties: true
x-jsonld-prefixes:
  schema: https://schema.org/
  dct: http://purl.org/dc/terms/
  csvw: http://www.w3.org/ns/csvw#
  xsd: http://www.w3.org/2001/XMLSchema#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/geoparquet-header/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/geoparquet-header/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "fileName": "schema:contentUrl",
    "encoding": "schema:encodingFormat",
    "source": {
      "@context": {
        "href": {
          "@id": "dct:references",
          "@type": "@id"
        },
        "sourceFormat": "dct:format",
        "rowCount": "schema:numberOfItems",
        "columnCount": "schema:numberOfColumns",
        "note": "schema:comment"
      },
      "@id": "dct:source"
    },
    "parquetSchema": {
      "@context": {
        "name": "csvw:name",
        "type": "csvw:datatype",
        "nullable": "https://geoparquet.org/schema#nullable",
        "description": "dct:description",
        "propertyUrl": {
          "@id": "csvw:propertyUrl",
          "@type": "@id"
        }
      },
      "@id": "https://geoparquet.org/schema",
      "@container": "@list"
    },
    "geo": {
      "@context": {
        "version": "schema:version",
        "primary_column": "https://geoparquet.org/metadata#primary_column",
        "columns": {
          "@context": {
            "geometry_types": "https://geoparquet.org/metadata#geometry_types",
            "crs": {
              "@context": {
                "type": "csvw:datatype"
              },
              "@id": "https://geoparquet.org/metadata#crs"
            },
            "edges": "https://geoparquet.org/metadata#edges",
            "orientation": "https://geoparquet.org/metadata#orientation",
            "bbox": "https://geoparquet.org/metadata#bbox",
            "covering": "https://geoparquet.org/metadata#covering"
          },
          "@id": "https://geoparquet.org/metadata#columns"
        }
      },
      "@id": "https://geoparquet.org/metadata"
    },
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/geoparquet-header/context.jsonld)

## Sources

* [GeoParquet specification](https://geoparquet.org/)
* [PROJJSON schema](https://proj.org/en/stable/schemas/index.html)
* [CSVW (CSV on the Web)](https://www.w3.org/TR/tabular-data-primer/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/geoparquet-header`

