
# Harvest time series scenario Scen M3 — GeoParquet representation (Schema)

`ogc.hosted.seadots.harvest-timeseries-scen-m3-geoparquet` *v0.1*

GeoParquet representation of the source-faithful harvest_timeseries_scenario_Scen_M3 point time series: id, Point geometry, bwmus and time, unchanged from harvest-timeseries-scen-m3-source. geometry_types, bbox and CRS are derived from the actual data, not declared placeholders.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Harvest time series scenario Scen M3 — GeoParquet representation

GeoParquet representation of the same source data as
[harvest-timeseries-scen-m3-source](../harvest-timeseries-scen-m3-source/):
19,920 Point features (83 spatial-series identifiers × 240 timestamps), each
with a numeric `bwmus` value and a `time` string, unchanged from the source.
This block adds no properties and resolves no additional semantics beyond
what `harvest-timeseries-scen-m3-source`'s own `context.jsonld` already
defines — it exists to declare a GeoParquet physical representation of the
same data, built on the shared [GeoParquet Header](../geoparquet-header/)
envelope schema.

## Provenance

The example header (`examples/harvest-timeseries-scen-m3-header.json`) was
generated directly from
`harvest-timeseries-scen-m3-source/examples/harvest-timeseries-scen-m3-sample.geojson`
using the `geojson-to-geoparquet` skill (ogcaibb
`skills/geojson-to-geoparquet/scripts/geojson_to_geoparquet.py`):

```bash
python3 <path-to-ogcaibb>/skills/geojson-to-geoparquet/scripts/geojson_to_geoparquet.py \
  --input ../harvest-timeseries-scen-m3-source/examples/harvest-timeseries-scen-m3-sample.geojson \
  --output harvest-timeseries-scen-m3.geoparquet \
  --write-header examples/harvest-timeseries-scen-m3-header.json \
  --source-href "../harvest-timeseries-scen-m3-source/examples/harvest-timeseries-scen-m3-sample.geojson" \
  --context ../harvest-timeseries-scen-m3-source/context.jsonld
```

`geometry_types` (`["Point"]`), the `bbox`, and the row/column counts in the
header are computed from the real 19,920-feature source, not asserted by
hand. The `crs` is a full PROJJSON `OGC:CRS84` object (the script's built-in
default) — never the hand-typed shorthand that, in an earlier revision of
the sibling `swedish-DT-simulations-output` block, parsed as JSON but broke
real GeoParquet readers at read time; the shared `geoparquet-header` schema
now rejects that shape outright.

`examples/harvest-timeseries-scen-m3.geoparquet` itself is a derived build
artifact and is **not** committed — regenerate it with the command above
(drop `--write-header` if you only need the Parquet file) and sanity-check
it opens before trusting it:

```bash
python3 -c "import geopandas as gpd; print(gpd.read_parquet('harvest-timeseries-scen-m3.geoparquet').shape)"
```

## Known gaps (inherited from the source)

Same as `harvest-timeseries-scen-m3-source`: `bwmus` has no authoritative
scientific definition or unit, and `time` has no declared timezone or
calendar. This block does not resolve either — see that block's description
for details and recommended fallbacks.

## Examples

### Harvest time series scenario Scen M3 — GeoParquet header
#### json
```json
{
  "fileName": "harvest-timeseries-scen-m3.geoparquet",
  "encoding": "GeoParquet 1.1.0; Parquet logical types; geometry encoded as WKB",
  "source": {
    "href": "../harvest-timeseries-scen-m3-source/examples/harvest-timeseries-scen-m3-sample.geojson",
    "sourceFormat": "application/geo+json",
    "rowCount": 19920,
    "columnCount": 4
  },
  "parquetSchema": [
    {
      "name": "id",
      "type": "INT64",
      "nullable": false,
      "propertyUrl": "http://purl.org/dc/terms/identifier"
    },
    {
      "name": "geometry",
      "type": "BYTE_ARRAY/WKB",
      "nullable": true,
      "propertyUrl": "https://purl.org/geojson/vocab#geometry"
    },
    {
      "name": "bwmus",
      "type": "DOUBLE",
      "nullable": false,
      "propertyUrl": "https://w3id.org/iliad/property/bwmus"
    },
    {
      "name": "time",
      "type": "BYTE_ARRAY/UTF8",
      "nullable": false,
      "propertyUrl": "http://purl.org/dc/terms/temporal"
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
        "crs": {
          "$schema": "https://proj.org/schemas/v0.7/projjson.schema.json",
          "type": "GeographicCRS",
          "name": "WGS 84 (CRS84)",
          "datum_ensemble": {
            "name": "World Geodetic System 1984 ensemble",
            "members": [
              {
                "name": "World Geodetic System 1984 (Transit)"
              },
              {
                "name": "World Geodetic System 1984 (G730)"
              },
              {
                "name": "World Geodetic System 1984 (G873)"
              },
              {
                "name": "World Geodetic System 1984 (G1150)"
              },
              {
                "name": "World Geodetic System 1984 (G1674)"
              },
              {
                "name": "World Geodetic System 1984 (G1762)"
              },
              {
                "name": "World Geodetic System 1984 (G2139)"
              },
              {
                "name": "World Geodetic System 1984 (G2296)"
              }
            ],
            "ellipsoid": {
              "name": "WGS 84",
              "semi_major_axis": 6378137,
              "inverse_flattening": 298.257223563
            },
            "accuracy": "2.0",
            "id": {
              "authority": "EPSG",
              "code": 6326
            }
          },
          "coordinate_system": {
            "subtype": "ellipsoidal",
            "axis": [
              {
                "name": "Geodetic longitude",
                "abbreviation": "Lon",
                "direction": "east",
                "unit": "degree"
              },
              {
                "name": "Geodetic latitude",
                "abbreviation": "Lat",
                "direction": "north",
                "unit": "degree"
              }
            ]
          },
          "scope": "Not known.",
          "area": "World.",
          "bbox": {
            "south_latitude": -90,
            "west_longitude": -180,
            "north_latitude": 90,
            "east_longitude": 180
          },
          "id": {
            "authority": "OGC",
            "code": "CRS84"
          }
        },
        "bbox": [
          7.642570856666667,
          54.37364839,
          7.713492693333333,
          54.40949512
        ]
      }
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/harvest-timeseries-scen-m3-geoparquet/context.jsonld",
  "fileName": "harvest-timeseries-scen-m3.geoparquet",
  "encoding": "GeoParquet 1.1.0; Parquet logical types; geometry encoded as WKB",
  "source": {
    "href": "../harvest-timeseries-scen-m3-source/examples/harvest-timeseries-scen-m3-sample.geojson",
    "sourceFormat": "application/geo+json",
    "rowCount": 19920,
    "columnCount": 4
  },
  "parquetSchema": [
    {
      "name": "id",
      "type": "INT64",
      "nullable": false,
      "propertyUrl": "http://purl.org/dc/terms/identifier"
    },
    {
      "name": "geometry",
      "type": "BYTE_ARRAY/WKB",
      "nullable": true,
      "propertyUrl": "https://purl.org/geojson/vocab#geometry"
    },
    {
      "name": "bwmus",
      "type": "DOUBLE",
      "nullable": false,
      "propertyUrl": "https://w3id.org/iliad/property/bwmus"
    },
    {
      "name": "time",
      "type": "BYTE_ARRAY/UTF8",
      "nullable": false,
      "propertyUrl": "http://purl.org/dc/terms/temporal"
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
        "crs": {
          "$schema": "https://proj.org/schemas/v0.7/projjson.schema.json",
          "type": "GeographicCRS",
          "name": "WGS 84 (CRS84)",
          "datum_ensemble": {
            "name": "World Geodetic System 1984 ensemble",
            "members": [
              {
                "name": "World Geodetic System 1984 (Transit)"
              },
              {
                "name": "World Geodetic System 1984 (G730)"
              },
              {
                "name": "World Geodetic System 1984 (G873)"
              },
              {
                "name": "World Geodetic System 1984 (G1150)"
              },
              {
                "name": "World Geodetic System 1984 (G1674)"
              },
              {
                "name": "World Geodetic System 1984 (G1762)"
              },
              {
                "name": "World Geodetic System 1984 (G2139)"
              },
              {
                "name": "World Geodetic System 1984 (G2296)"
              }
            ],
            "ellipsoid": {
              "name": "WGS 84",
              "semi_major_axis": 6378137,
              "inverse_flattening": 298.257223563
            },
            "accuracy": "2.0",
            "id": {
              "authority": "EPSG",
              "code": 6326
            }
          },
          "coordinate_system": {
            "subtype": "ellipsoidal",
            "axis": [
              {
                "name": "Geodetic longitude",
                "abbreviation": "Lon",
                "direction": "east",
                "unit": "degree"
              },
              {
                "name": "Geodetic latitude",
                "abbreviation": "Lat",
                "direction": "north",
                "unit": "degree"
              }
            ]
          },
          "scope": "Not known.",
          "area": "World.",
          "bbox": {
            "south_latitude": -90,
            "west_longitude": -180,
            "north_latitude": 90,
            "east_longitude": 180
          },
          "id": {
            "authority": "OGC",
            "code": "CRS84"
          }
        },
        "bbox": [
          7.642570856666667,
          54.37364839,
          7.713492693333333,
          54.40949512
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
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <https://geoparquet.org/metadata#> .
@prefix ns2: <https://geoparquet.org/schema#> .
@prefix ns3: <https://geoparquet.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] dct:source [ dct:format "application/geo+json" ;
            dct:references <file:///github/harvest-timeseries-scen-m3-source/examples/harvest-timeseries-scen-m3-sample.geojson> ;
            schema:numberOfColumns 4 ;
            schema:numberOfItems 19920 ] ;
    ns3:metadata [ ns1:columns [ geojson:geometry [ ns1:bbox 7.642571e+00,
                                7.713493e+00,
                                5.437365e+01,
                                5.44095e+01 ;
                            ns1:crs [ dct:identifier [ ] ;
                                    csvw:datatype "GeographicCRS" ;
                                    csvw:name "WGS 84 (CRS84)" ;
                                    ns1:bbox [ ] ] ;
                            ns1:geometry_types "Point" ;
                            schema:encodingFormat "WKB" ] ] ;
            ns1:primary_column "geometry" ;
            schema:version "1.1.0" ] ;
    ns3:schema ( [ csvw:datatype "INT64" ;
                csvw:name "id" ;
                csvw:propertyUrl dct:identifier ;
                ns2:nullable false ] [ csvw:datatype "BYTE_ARRAY/WKB" ;
                csvw:name "geometry" ;
                csvw:propertyUrl geojson:geometry ;
                ns2:nullable true ] [ csvw:datatype "DOUBLE" ;
                csvw:name "bwmus" ;
                csvw:propertyUrl <https://w3id.org/iliad/property/bwmus> ;
                ns2:nullable false ] [ csvw:datatype "BYTE_ARRAY/UTF8" ;
                csvw:name "time" ;
                csvw:propertyUrl dct:temporal ;
                ns2:nullable false ] ) ;
    schema:contentUrl "harvest-timeseries-scen-m3.geoparquet" ;
    schema:encodingFormat "GeoParquet 1.1.0; Parquet logical types; geometry encoded as WKB" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: "Harvest time series scenario Scen M3 \u2014 GeoParquet representation"
description: 'GeoParquet representation header for the source-faithful harvest time
  series scenario Scen M3 point time series (see harvest-timeseries-scen-m3-source).
  Declares the four physical columns (id, geometry, bwmus, time) via the shared GeoParquetHeader
  envelope. propertyUrls are resolved against harvest-timeseries-scen-m3-source''s
  own context.jsonld (dct:identifier, geojson:geometry, the provisional bwmus IRI,
  dct:temporal), not redefined here.

  '
$ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/geoparquet-header/schema.yaml
x-jsonld-extra-terms:
  fileName: https://schema.org/contentUrl
  encoding: https://schema.org/encodingFormat
  source: http://purl.org/dc/terms/source
  href:
    x-jsonld-id: http://purl.org/dc/terms/references
    x-jsonld-type: '@id'
  sourceFormat: http://purl.org/dc/terms/format
  rowCount: https://schema.org/numberOfItems
  columnCount: https://schema.org/numberOfColumns
  parquetSchema:
    x-jsonld-id: https://geoparquet.org/schema
    x-jsonld-container: '@list'
  name: http://www.w3.org/ns/csvw#name
  description: http://purl.org/dc/terms/description
  type: http://www.w3.org/ns/csvw#datatype
  nullable: https://geoparquet.org/schema#nullable
  propertyUrl:
    x-jsonld-id: http://www.w3.org/ns/csvw#propertyUrl
    x-jsonld-type: '@id'
  geo: https://geoparquet.org/metadata
  version: https://schema.org/version
  primary_column: https://geoparquet.org/metadata#primary_column
  columns: https://geoparquet.org/metadata#columns
  geometry_types: https://geoparquet.org/metadata#geometry_types
  crs: https://geoparquet.org/metadata#crs
  bbox: https://geoparquet.org/metadata#bbox
  id:
    x-jsonld-id: http://purl.org/dc/terms/identifier
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
  geometry: https://purl.org/geojson/vocab#geometry
  time: http://purl.org/dc/terms/temporal
  bwmus:
    x-jsonld-id: https://w3id.org/iliad/property/bwmus
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#double
x-jsonld-prefixes:
  schema: https://schema.org/
  dct: http://purl.org/dc/terms/
  csvw: http://www.w3.org/ns/csvw#
  xsd: http://www.w3.org/2001/XMLSchema#
  geojson: https://purl.org/geojson/vocab#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/harvest-timeseries-scen-m3-geoparquet/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/harvest-timeseries-scen-m3-geoparquet/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "fileName": "schema:contentUrl",
    "encoding": "schema:encodingFormat",
    "source": {
      "@context": {
        "note": "schema:comment"
      },
      "@id": "dct:source"
    },
    "parquetSchema": {
      "@id": "https://geoparquet.org/schema",
      "@container": "@list"
    },
    "geo": {
      "@context": {
        "columns": {
          "@context": {
            "edges": "https://geoparquet.org/metadata#edges",
            "orientation": "https://geoparquet.org/metadata#orientation",
            "covering": "https://geoparquet.org/metadata#covering"
          },
          "@id": "https://geoparquet.org/metadata#columns"
        }
      },
      "@id": "https://geoparquet.org/metadata"
    },
    "href": {
      "@id": "dct:references",
      "@type": "@id"
    },
    "sourceFormat": "dct:format",
    "rowCount": "schema:numberOfItems",
    "columnCount": "schema:numberOfColumns",
    "name": "csvw:name",
    "description": "dct:description",
    "type": "csvw:datatype",
    "nullable": "https://geoparquet.org/schema#nullable",
    "propertyUrl": {
      "@id": "csvw:propertyUrl",
      "@type": "@id"
    },
    "version": "schema:version",
    "primary_column": "https://geoparquet.org/metadata#primary_column",
    "columns": "https://geoparquet.org/metadata#columns",
    "geometry_types": "https://geoparquet.org/metadata#geometry_types",
    "crs": "https://geoparquet.org/metadata#crs",
    "bbox": "https://geoparquet.org/metadata#bbox",
    "id": {
      "@id": "dct:identifier",
      "@type": "xsd:integer"
    },
    "geometry": "geojson:geometry",
    "time": "dct:temporal",
    "bwmus": {
      "@id": "https://w3id.org/iliad/property/bwmus",
      "@type": "xsd:double"
    },
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "geojson": "https://purl.org/geojson/vocab#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/harvest-timeseries-scen-m3-geoparquet/context.jsonld)

## Sources

* [Harvest time series scenario Scen M3 — source GeoJSON](bblocks://ogc.hosted.seadots.harvest-timeseries-scen-m3-source)
* [GeoParquet specification](https://geoparquet.org/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/harvest-timeseries-scen-m3-geoparquet`

