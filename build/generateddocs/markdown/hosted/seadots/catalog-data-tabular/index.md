
# SeaDOTs Catalog Data Tabular (Schema)

`ogc.hosted.seadots.catalog-data-tabular` *v0.1*

OGC API Records profile for catalog records that describe tabular data products (CSV/TSV, GeoParquet, Parquet, attribute tables), reusing the shared SeaDOTs catalog-data profile and adding tabular structural metadata (STAC table extension columns and GeoParquet column metadata).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# SeaDOTs Catalog Data Tabular

OGC API Records profile for catalog records that describe tabular data products such as CSV, TSV, Parquet, GeoParquet, or spatial attribute tables.

The profile composes `ogc.hosted.seadots.catalog-data` for shared Records/DCAT/STAC/CF/PROV-O catalog semantics, then adds locally only the tabular structural metadata terms drawn from the STAC `table` extension (https://github.com/stac-extensions/table) and GeoParquet column metadata conventions (https://geoparquet.org/). It intentionally avoids copying inherited properties, schemas, or JSON-LD context. The local schema constraint requires a profile link that advertises this building block's own identifier.

There is no imported ILIAD tabular block to depend on: the ILIAD `geoparquet` folder contains only a GeoParquet column-metadata sample with no `bblock.json` or schema. Therefore, unlike `catalog-data-multidim`, this profile defines the structural column descriptor terms locally and lists no ILIAD dependency.

## Composition

| Concern | Source |
| --- | --- |
| Shared STAC/CF/provenance data record | `bblocks://ogc.hosted.seadots.catalog-data` |
| Tabular column descriptor structure | Local `schema.yaml` — STAC `table` extension terms |
| GeoParquet primary geometry column | Local `schema.yaml` — `table:primary_geometry` |
| Profile advertisement | Local `schema.yaml` profile-link constraint |
| JSON-LD terms | Inherited `catalog-data/context.jsonld` + local `table:` prefix terms |

## Added Properties

All tabular-specific properties live under `properties` of the OGC API Record Feature:

| Property | Type | Description |
| --- | --- | --- |
| `table:columns` | array of column objects | Ordered column list. Each column has `name` (required), `description`, `type`, and `unit` (CF/UDUNITS string). |
| `table:primary_geometry` | string | Name of the primary geometry column (GeoParquet). |
| `table:row_count` | integer | Total number of data rows in the asset. |

The `table:` prefix is mapped to `https://stac-extensions.github.io/table/v1.2.0/schema.json#` in the JSON-LD context. Unit strings follow CF/UDUNITS conventions and are mapped to `qudt:unit`.

## Source-property Coverage Gaps

No upstream tabular bblock schema exists for the ILIAD ecosystem; the GeoParquet encoding details (e.g. `encoding`, `geometry_types`, `crs` per-column keys from the GeoParquet metadata format) are not yet covered by this profile. Consumers who need per-column GeoParquet encoding metadata should extend this block or declare those terms in `additionalProperties`.

## Usage Notes

Use this block when a SeaDOTs catalog record points to a tabular data asset — CSV, TSV, Parquet, GeoParquet, or a spatial attribute table. Supply `table:columns` to document column names, types, and units so downstream consumers can interpret the file without opening it.

For multidimensional gridded or array-oriented assets (NetCDF, Zarr), use `ogc.hosted.seadots.catalog-data-multidim` instead.

## Examples

### SeaDOTs Catalog Data Tabular
#### json
```json
{
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/dataset/north-sea-cod-occurrences",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/table/v1.2.0/schema.json",
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [3.0, 56.0],
        [9.0, 56.0],
        [9.0, 61.0],
        [3.0, 61.0],
        [3.0, 56.0]
      ]
    ]
  },
  "bbox": [3.0, 56.0, 9.0, 61.0],
  "properties": {
    "title": "North Sea cod occurrence table (synthetic)",
    "description": "Synthetic SeaDOTs catalog record for a GeoParquet tabular dataset of Atlantic cod (Gadus morhua) occurrence records in the North Sea. All values are synthetic documentation data; this record does not represent a real dataset.",
    "datetime": "2026-06-11T00:00:00Z",
    "start_datetime": "2024-01-01T00:00:00Z",
    "end_datetime": "2024-12-31T00:00:00Z",
    "keywords": [
      "SeaDOTs",
      "tabular",
      "GeoParquet",
      "occurrence",
      "cod",
      "Gadus morhua",
      "North Sea",
      "ICES"
    ],
    "license": "CC-BY-4.0",
    "role": "data",
    "table:columns": [
      {
        "name": "occurrence_id",
        "description": "Unique identifier for the occurrence record.",
        "type": "string"
      },
      {
        "name": "species",
        "description": "Scientific species name.",
        "type": "string"
      },
      {
        "name": "longitude",
        "description": "Decimal longitude of the observation (WGS84).",
        "type": "float64",
        "unit": "degrees_east"
      },
      {
        "name": "latitude",
        "description": "Decimal latitude of the observation (WGS84).",
        "type": "float64",
        "unit": "degrees_north"
      },
      {
        "name": "depth",
        "description": "Observation depth below sea surface.",
        "type": "float32",
        "unit": "m"
      },
      {
        "name": "sea_water_temperature",
        "description": "In-situ sea water temperature at the observation depth.",
        "type": "float32",
        "unit": "degrees_C"
      },
      {
        "name": "count",
        "description": "Number of individuals recorded in the observation event.",
        "type": "int32",
        "unit": "1"
      },
      {
        "name": "geometry",
        "description": "Point geometry of the observation location (WGS84, GeoParquet encoding).",
        "type": "geometry"
      }
    ],
    "table:primary_geometry": "geometry",
    "table:row_count": 42150
  },
  "assets": {
    "geoparquet": {
      "href": "https://example.org/seadots/north-sea-cod-occurrences.parquet",
      "type": "application/x-parquet",
      "title": "GeoParquet occurrence table",
      "roles": ["data"]
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data-tabular",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data Tabular bblock"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.seadots.catalog-data-tabular",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data Tabular profile"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data-tabular/context.jsonld",
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/dataset/north-sea-cod-occurrences",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/table/v1.2.0/schema.json",
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          3.0,
          56.0
        ],
        [
          9.0,
          56.0
        ],
        [
          9.0,
          61.0
        ],
        [
          3.0,
          61.0
        ],
        [
          3.0,
          56.0
        ]
      ]
    ]
  },
  "bbox": [
    3.0,
    56.0,
    9.0,
    61.0
  ],
  "properties": {
    "title": "North Sea cod occurrence table (synthetic)",
    "description": "Synthetic SeaDOTs catalog record for a GeoParquet tabular dataset of Atlantic cod (Gadus morhua) occurrence records in the North Sea. All values are synthetic documentation data; this record does not represent a real dataset.",
    "datetime": "2026-06-11T00:00:00Z",
    "start_datetime": "2024-01-01T00:00:00Z",
    "end_datetime": "2024-12-31T00:00:00Z",
    "keywords": [
      "SeaDOTs",
      "tabular",
      "GeoParquet",
      "occurrence",
      "cod",
      "Gadus morhua",
      "North Sea",
      "ICES"
    ],
    "license": "CC-BY-4.0",
    "role": "data",
    "table:columns": [
      {
        "name": "occurrence_id",
        "description": "Unique identifier for the occurrence record.",
        "type": "string"
      },
      {
        "name": "species",
        "description": "Scientific species name.",
        "type": "string"
      },
      {
        "name": "longitude",
        "description": "Decimal longitude of the observation (WGS84).",
        "type": "float64",
        "unit": "degrees_east"
      },
      {
        "name": "latitude",
        "description": "Decimal latitude of the observation (WGS84).",
        "type": "float64",
        "unit": "degrees_north"
      },
      {
        "name": "depth",
        "description": "Observation depth below sea surface.",
        "type": "float32",
        "unit": "m"
      },
      {
        "name": "sea_water_temperature",
        "description": "In-situ sea water temperature at the observation depth.",
        "type": "float32",
        "unit": "degrees_C"
      },
      {
        "name": "count",
        "description": "Number of individuals recorded in the observation event.",
        "type": "int32",
        "unit": "1"
      },
      {
        "name": "geometry",
        "description": "Point geometry of the observation location (WGS84, GeoParquet encoding).",
        "type": "geometry"
      }
    ],
    "table:primary_geometry": "geometry",
    "table:row_count": 42150
  },
  "assets": {
    "geoparquet": {
      "href": "https://example.org/seadots/north-sea-cod-occurrences.parquet",
      "type": "application/x-parquet",
      "title": "GeoParquet occurrence table",
      "roles": [
        "data"
      ]
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data-tabular",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data Tabular bblock"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.seadots.catalog-data-tabular",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data Tabular profile"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <https://w3id.org/ogc/stac/assets/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix table: <https://stac-extensions.github.io/table/v1.2.0/schema.json#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/ogc/hosted/seadots/catalog/dataset/north-sea-cod-occurrences> dcterms:date "2026-06-11T00:00:00+00:00"^^xsd:dateTime ;
    dcterms:description "Synthetic SeaDOTs catalog record for a GeoParquet tabular dataset of Atlantic cod (Gadus morhua) occurrence records in the North Sea. All values are synthetic documentation data; this record does not represent a real dataset." ;
    dcterms:license "CC-BY-4.0" ;
    dcterms:subject "Gadus morhua",
        "GeoParquet",
        "ICES",
        "North Sea",
        "SeaDOTs",
        "cod",
        "occurrence",
        "tabular" ;
    dcterms:title "North Sea cod occurrence table (synthetic)" ;
    dcterms:type "Feature" ;
    rdfs:seeAlso [ rdfs:label "SeaDOTs Catalog Data Tabular bblock" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-data-tabular> ],
        [ rdfs:label "SeaDOTs Catalog Data Tabular profile" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/profile> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-data-tabular> ] ;
    geojson:bbox ( 3e+00 5.6e+01 9e+00 6.1e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 3e+00 5.6e+01 ) ( 9e+00 5.6e+01 ) ( 9e+00 6.1e+01 ) ( 3e+00 6.1e+01 ) ( 3e+00 5.6e+01 ) ) ) ] ;
    table:columns ( [ dcterms:description "Unique identifier for the occurrence record." ;
                dcterms:title "occurrence_id" ;
                dcterms:type "string" ] [ dcterms:description "Scientific species name." ;
                dcterms:title "species" ;
                dcterms:type "string" ] [ dcterms:description "Decimal longitude of the observation (WGS84)." ;
                dcterms:title "longitude" ;
                dcterms:type "float64" ;
                qudt:unit "degrees_east" ] [ dcterms:description "Decimal latitude of the observation (WGS84)." ;
                dcterms:title "latitude" ;
                dcterms:type "float64" ;
                qudt:unit "degrees_north" ] [ dcterms:description "Observation depth below sea surface." ;
                dcterms:title "depth" ;
                dcterms:type "float32" ;
                qudt:unit "m" ] [ dcterms:description "In-situ sea water temperature at the observation depth." ;
                dcterms:title "sea_water_temperature" ;
                dcterms:type "float32" ;
                qudt:unit "degrees_C" ] [ dcterms:description "Number of individuals recorded in the observation event." ;
                dcterms:title "count" ;
                dcterms:type "int32" ;
                qudt:unit "1" ] [ dcterms:description "Point geometry of the observation location (WGS84, GeoParquet encoding)." ;
                dcterms:title "geometry" ;
                dcterms:type "geometry" ] ) ;
    table:primary_geometry "geometry" ;
    table:row_count 42150 ;
    seadots:itemType "record" ;
    seadots:role "data" ;
    stac:end_datetime "2024-12-31T00:00:00+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ns2:geoparquet [ dcterms:format "application/x-parquet" ;
                    dcterms:title "GeoParquet occurrence table" ;
                    oa:hasTarget <https://example.org/seadots/north-sea-cod-occurrences.parquet> ;
                    stac:roles "data" ] ] ;
    stac:hasExtension "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
        "https://stac-extensions.github.io/prov/v1.0.0/schema.json",
        "https://stac-extensions.github.io/table/v1.2.0/schema.json" ;
    stac:start_datetime "2024-01-01T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" .


```


### Harvest time-series scenario tabular catalog example
#### json
```json
{
  "id": "harvest-timeseries-scen-m3-tabular",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/table/v1.2.0/schema.json",
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      [7.64260227, 54.39245755],
      [7.6640575066666665, 54.399025196666663],
      [7.6800021166666665, 54.39909727]
    ]
  },
  "bbox": [
    7.64260227,
    54.39245755,
    7.6800021166666665,
    54.39909727
  ],
  "properties": {
    "title": "Harvest time-series scenario Scen M3 tabular catalog record",
    "description": "Tabular catalog record for the SeaDOTs harvest scenario sample, describing the GeoJSON feature table as a tabular asset.",
    "datetime": "2020-04-30T00:00:00Z",
    "role": "data",
    "convention": "CF-1.10",
    "license": "Not supplied",
    "table:columns": [
      {
        "name": "id",
        "type": "integer",
        "description": "Feature identifier from the source GeoJSON"
      },
      {
        "name": "geometry",
        "type": "geometry",
        "description": "Point geometry for each feature"
      },
      {
        "name": "bwmus",
        "type": "number",
        "description": "Scenario value",
        "unit": "1"
      },
      {
        "name": "time",
        "type": "string",
        "description": "Timestamp string from the source GeoJSON"
      }
    ],
    "table:primary_geometry": "geometry",
    "table:row_count": 19920
  },
  "assets": {
    "data": {
      "href": "../../harvest-timeseries-scen-m3-source/examples/harvest-timeseries-scen-m3-sample.geojson",
      "type": "application/geo+json",
      "title": "Harvest time-series sample GeoJSON"
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data-tabular",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data Tabular bblock"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data-tabular/context.jsonld",
  "id": "harvest-timeseries-scen-m3-tabular",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/table/v1.2.0/schema.json",
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      [
        7.64260227,
        54.39245755
      ],
      [
        7.6640575066666665,
        54.39902519666666
      ],
      [
        7.6800021166666665,
        54.39909727
      ]
    ]
  },
  "bbox": [
    7.64260227,
    54.39245755,
    7.6800021166666665,
    54.39909727
  ],
  "properties": {
    "title": "Harvest time-series scenario Scen M3 tabular catalog record",
    "description": "Tabular catalog record for the SeaDOTs harvest scenario sample, describing the GeoJSON feature table as a tabular asset.",
    "datetime": "2020-04-30T00:00:00Z",
    "role": "data",
    "convention": "CF-1.10",
    "license": "Not supplied",
    "table:columns": [
      {
        "name": "id",
        "type": "integer",
        "description": "Feature identifier from the source GeoJSON"
      },
      {
        "name": "geometry",
        "type": "geometry",
        "description": "Point geometry for each feature"
      },
      {
        "name": "bwmus",
        "type": "number",
        "description": "Scenario value",
        "unit": "1"
      },
      {
        "name": "time",
        "type": "string",
        "description": "Timestamp string from the source GeoJSON"
      }
    ],
    "table:primary_geometry": "geometry",
    "table:row_count": 19920
  },
  "assets": {
    "data": {
      "href": "../../harvest-timeseries-scen-m3-source/examples/harvest-timeseries-scen-m3-sample.geojson",
      "type": "application/geo+json",
      "title": "Harvest time-series sample GeoJSON"
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data-tabular",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data Tabular bblock"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <https://w3id.org/ogc/stac/assets/> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix table: <https://stac-extensions.github.io/table/v1.2.0/schema.json#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/harvest-timeseries-scen-m3-tabular> dcterms:date "2020-04-30T00:00:00+00:00"^^xsd:dateTime ;
    dcterms:description "Tabular catalog record for the SeaDOTs harvest scenario sample, describing the GeoJSON feature table as a tabular asset." ;
    dcterms:license "Not supplied" ;
    dcterms:title "Harvest time-series scenario Scen M3 tabular catalog record" ;
    dcterms:type "Feature" ;
    rdfs:seeAlso [ rdfs:label "SeaDOTs Catalog Data Tabular bblock" ;
            dcterms:type "application/schema+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-data-tabular> ] ;
    geojson:bbox ( 7.642602e+00 5.439246e+01 7.680002e+00 5.43991e+01 ) ;
    geojson:geometry [ a geojson:MultiPoint ;
            geojson:coordinates ( ( 7.642602e+00 5.439246e+01 ) ( 7.664058e+00 5.439903e+01 ) ( 7.680002e+00 5.43991e+01 ) ) ] ;
    table:columns ( [ dcterms:description "Feature identifier from the source GeoJSON" ;
                dcterms:title "id" ;
                dcterms:type "integer" ] [ dcterms:description "Point geometry for each feature" ;
                dcterms:title "geometry" ;
                dcterms:type "geometry" ] [ dcterms:description "Scenario value" ;
                dcterms:title "bwmus" ;
                dcterms:type "number" ;
                qudt:unit "1" ] [ dcterms:description "Timestamp string from the source GeoJSON" ;
                dcterms:title "time" ;
                dcterms:type "string" ] ) ;
    table:primary_geometry "geometry" ;
    table:row_count 19920 ;
    seadots:itemType "record" ;
    seadots:metadataConvention "CF-1.10" ;
    seadots:role "data" ;
    stac:hasAsset [ ns1:data [ dcterms:format "application/geo+json" ;
                    dcterms:title "Harvest time-series sample GeoJSON" ;
                    oa:hasTarget <file:///harvest-timeseries-scen-m3-source/examples/harvest-timeseries-scen-m3-sample.geojson> ] ] ;
    stac:hasExtension "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
        "https://stac-extensions.github.io/prov/v1.0.0/schema.json",
        "https://stac-extensions.github.io/table/v1.2.0/schema.json" ;
    stac:version "1.0.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SeaDOTs Catalog Data Tabular
description: 'OGC API Records profile for records describing tabular data assets such
  as CSV, TSV, Parquet, GeoParquet, or attribute tables. The shared SeaDOTs catalog
  data semantics are inherited from ogc.hosted.seadots.catalog-data; this block adds
  only the STAC table extension column descriptors and the profile-link constraint
  that advertises this building block.

  '
allOf:
- $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data/schema.yaml
type: object
required:
- type
- properties
- links
properties:
  type:
    const: Feature
    x-jsonld-id: http://purl.org/dc/terms/type
  properties:
    type: object
    required:
    - title
    - description
    additionalProperties: true
    properties:
      table:columns:
        type: array
        description: 'Ordered list of columns in the tabular data asset. Based on
          the STAC table extension column descriptor.

          '
        items:
          type: object
          required:
          - name
          properties:
            name:
              type: string
              description: Column name as it appears in the data file.
              x-jsonld-id: http://purl.org/dc/terms/title
            description:
              type: string
              description: Human-readable description of the column.
              x-jsonld-id: http://purl.org/dc/terms/description
            type:
              type: string
              description: 'Data type of the column values (e.g. int32, float64, string,
                geometry, datetime). Follows STAC table extension type vocabulary.

                '
              x-jsonld-id: http://purl.org/dc/terms/type
            unit:
              type: string
              description: 'Physical unit of the column values expressed as a CF/UDUNITS
                string (e.g. "m s-1", "degrees_C", "1").

                '
              x-jsonld-id: http://qudt.org/schema/qudt/unit
          additionalProperties: true
        x-jsonld-id: https://stac-extensions.github.io/table/v1.2.0/schema.json#columns
        x-jsonld-container: '@list'
      table:primary_geometry:
        type: string
        description: 'Name of the primary geometry column in the tabular file. Applicable
          only when the asset is a GeoParquet file or other spatially-enabled tabular
          format.

          '
        x-jsonld-id: https://stac-extensions.github.io/table/v1.2.0/schema.json#primaryGeometry
      table:row_count:
        type: integer
        minimum: 0
        description: Total number of data rows in the tabular asset.
        x-jsonld-id: https://stac-extensions.github.io/table/v1.2.0/schema.json#rowCount
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
    x-jsonld-id: '@nest'
  links:
    type: array
    contains:
      type: object
      required:
      - rel
      - href
      properties:
        rel:
          const: profile
          x-jsonld-id: http://www.iana.org/assignments/relation
          x-jsonld-type: '@id'
          x-jsonld-base: http://www.iana.org/assignments/relation/
        href:
          const: bblocks://ogc.hosted.seadots.catalog-data-tabular
          x-jsonld-type: '@id'
          x-jsonld-id: http://www.w3.org/ns/oa#hasTarget
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
    x-jsonld-extra-terms:
      type: http://purl.org/dc/terms/type
      hreflang: http://purl.org/dc/terms/language
      title: http://www.w3.org/2000/01/rdf-schema#label
      length: http://purl.org/dc/terms/extent
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
  FeatureCollection: https://purl.org/geojson/vocab#FeatureCollection
  GeometryCollection: https://purl.org/geojson/vocab#GeometryCollection
  LineString: https://purl.org/geojson/vocab#LineString
  MultiLineString: https://purl.org/geojson/vocab#MultiLineString
  MultiPoint: https://purl.org/geojson/vocab#MultiPoint
  MultiPolygon: https://purl.org/geojson/vocab#MultiPolygon
  Point: https://purl.org/geojson/vocab#Point
  Polygon: https://purl.org/geojson/vocab#Polygon
  features:
    x-jsonld-container: '@set'
    x-jsonld-id: https://purl.org/geojson/vocab#features
  id: '@id'
  geometry:
    x-jsonld-context:
      coordinates:
        '@container': '@list'
        '@id': https://purl.org/geojson/vocab#coordinates
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
  bbox:
    x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#bbox
  conformsTo:
    x-jsonld-container: '@set'
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
  time: http://purl.org/dc/terms/temporal
  linkTemplates:
    x-jsonld-context:
      rel:
        '@context':
          '@base': http://www.iana.org/assignments/relation/
        '@id': http://www.iana.org/assignments/relation
        '@type': '@id'
      type: http://purl.org/dc/terms/format
      hreflang: http://purl.org/dc/terms/language
      title: http://www.w3.org/2000/01/rdf-schema#label
      length: http://purl.org/dc/terms/extent
      uriTemplate:
        '@type': http://www.w3.org/2001/XMLSchema#string
        '@id': https://www.opengis.net/def/ogc-api/records/uriTemplate
      varBase: https://www.opengis.net/def/ogc-api/records/varBase
      variables:
        '@id': https://www.opengis.net/def/ogc-api/records/hasVariable
        '@container': '@index'
        '@index': http://purl.org/dc/terms/identifier
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/hasLinkTemplate
  created: http://purl.org/dc/terms/created
  updated: http://purl.org/dc/terms/modified
  title:
    x-jsonld-container: '@set'
    x-jsonld-id: http://purl.org/dc/terms/title
  keywords:
    x-jsonld-container: '@set'
    x-jsonld-id: http://www.w3.org/ns/dcat#keyword
  language: https://www.opengis.net/def/ogc-api/records/language
  languages:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/languages
    x-jsonld-context:
      code: https://www.opengis.net/def/ogc-api/records/languageCode
      name: http://www.w3.org/2004/02/skos/core#prefLabel
  resourceLanguages:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/resourceLanguages
    x-jsonld-context:
      code: https://www.opengis.net/def/ogc-api/records/languageCode
      name: http://www.w3.org/2004/02/skos/core#prefLabel
  externalIds:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/scopedIdentifier
    x-jsonld-context:
      scheme: https://www.opengis.net/def/ogc-api/records/scheme
      value: https://www.opengis.net/def/ogc-api/records/id
  themes:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/themes
    x-jsonld-context:
      concepts:
        '@id': https://w3id.org/ogc/stac/themes/concepts
        '@context':
          id: https://w3id.org/ogc/stac/themes/id
          url: '@id'
        '@container': '@set'
      scheme: https://w3id.org/ogc/stac/themes/scheme
  formats:
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/format
    x-jsonld-context:
      name: https://www.opengis.net/def/ogc-api/records/name
      mediaType: https://www.opengis.net/def/ogc-api/records/mediaType
    x-jsonld-container: '@set'
    x-jsonld-type: '@id'
  contacts:
    x-jsonld-container: '@set'
    x-jsonld-id: http://www.w3.org/ns/dcat#contactPoint
    x-jsonld-type: '@id'
  license: http://www.w3.org/ns/dcat#license
  accessrights: http://purl.org/dc/terms/accessRights
  variables:
    x-jsonld-container: '@id'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/hasVariable
    x-jsonld-context:
      '@base': http://example.com/variables/
      '@vocab': https://www.opengis.net/def/ogc-api/records/
  stac_extensions: https://w3id.org/ogc/stac/core/hasExtension
  assets:
    x-jsonld-context:
      type: http://purl.org/dc/terms/format
      roles:
        '@id': https://w3id.org/ogc/stac/core/roles
        '@container': '@set'
      '@vocab': https://w3id.org/ogc/stac/assets/
    x-jsonld-id: https://w3id.org/ogc/stac/core/hasAsset
    x-jsonld-container: '@set'
  stac_version: https://w3id.org/ogc/stac/core/version
  start_datetime:
    x-jsonld-id: https://w3id.org/ogc/stac/core/start_datetime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  end_datetime:
    x-jsonld-id: https://w3id.org/ogc/stac/core/end_datetime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  providers: https://w3id.org/ogc/stac/core/hasProvider
  media_type: http://purl.org/dc/terms/format
  extent: http://purl.org/dc/terms/extent
  datetime:
    x-jsonld-id: http://purl.org/dc/terms/date
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  concepts:
    x-jsonld-id: https://w3id.org/ogc/stac/themes/concepts
    x-jsonld-container: '@set'
    x-jsonld-context:
      name: https://w3id.org/ogc/stac/themes/name
      id: https://w3id.org/ogc/stac/themes/id
      url: '@id'
  scheme: https://w3id.org/ogc/stac/themes/scheme
  rights: http://www.w3.org/ns/dcat#rights
  wasInfluencedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasInfluencedBy
    x-jsonld-type: '@id'
  qualifiedInfluence:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInfluence
    x-jsonld-type: '@id'
  hadMember:
    x-jsonld-id: http://www.w3.org/ns/prov#hadMember
    x-jsonld-type: '@id'
  provType: '@type'
  featureType: '@type'
  entityType: '@type'
  has_provenance:
    x-jsonld-id: http://purl.org/dc/terms/provenance
    x-jsonld-type: '@id'
  wasGeneratedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
    x-jsonld-type: '@id'
  wasAttributedTo:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAttributedTo
    x-jsonld-type: '@id'
  wasDerivedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
    x-jsonld-type: '@id'
  alternateOf:
    x-jsonld-id: http://www.w3.org/ns/prov#alternateOf
    x-jsonld-type: '@id'
  hadPrimarySource:
    x-jsonld-id: http://www.w3.org/ns/prov#hadPrimarySource
    x-jsonld-type: '@id'
  specializationOf:
    x-jsonld-id: http://www.w3.org/ns/prov#specializationOf
    x-jsonld-type: '@id'
  wasInvalidatedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasInvalidatedBy
    x-jsonld-type: '@id'
  wasQuotedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasQuotedFrom
    x-jsonld-type: '@id'
  wasRevisionOf:
    x-jsonld-id: http://www.w3.org/ns/prov#wasRevisionOf
    x-jsonld-type: '@id'
  atLocation:
    x-jsonld-id: http://www.w3.org/ns/prov#atLocation
    x-jsonld-type: '@id'
  qualifiedGeneration:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedGeneration
    x-jsonld-type: '@id'
  qualifiedInvalidation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInvalidation
    x-jsonld-type: '@id'
  qualifiedDerivation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedDerivation
    x-jsonld-type: '@id'
  qualifiedAttribution:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedAttribution
    x-jsonld-type: '@id'
  activityType: '@type'
  agentType: '@type'
  Activity: http://www.w3.org/ns/prov#Activity
  ActivityInfluence: http://www.w3.org/ns/prov#ActivityInfluence
  Agent: http://www.w3.org/ns/prov#Agent
  AgentInfluence: http://www.w3.org/ns/prov#AgentInfluence
  Association: http://www.w3.org/ns/prov#Association
  Attribution: http://www.w3.org/ns/prov#Attribution
  Bundle: http://www.w3.org/ns/prov#Bundle
  Collection: http://www.w3.org/ns/prov#Collection
  Communication: http://www.w3.org/ns/prov#Communication
  Delegation: http://www.w3.org/ns/prov#Delegation
  Derivation: http://www.w3.org/ns/prov#Derivation
  EmptyCollection: http://www.w3.org/ns/prov#EmptyCollection
  End: http://www.w3.org/ns/prov#End
  Entity: http://www.w3.org/ns/prov#Entity
  EntityInfluence: http://www.w3.org/ns/prov#EntityInfluence
  Generation: http://www.w3.org/ns/prov#Generation
  Influence: http://www.w3.org/ns/prov#Influence
  InstantaneousEvent: http://www.w3.org/ns/prov#InstantaneousEvent
  Invalidation: http://www.w3.org/ns/prov#Invalidation
  Location: http://www.w3.org/ns/prov#Location
  Organization: http://www.w3.org/ns/prov#Organization
  Person: http://www.w3.org/ns/prov#Person
  Plan: http://www.w3.org/ns/prov#Plan
  PrimarySource: http://www.w3.org/ns/prov#PrimarySource
  Quotation: http://www.w3.org/ns/prov#Quotation
  Revision: http://www.w3.org/ns/prov#Revision
  Role: http://www.w3.org/ns/prov#Role
  SoftwareAgent: http://www.w3.org/ns/prov#SoftwareAgent
  Start: http://www.w3.org/ns/prov#Start
  Usage: http://www.w3.org/ns/prov#Usage
  ServiceDescription: http://www.w3.org/ns/prov#ServiceDescription
  DirectQueryService: http://www.w3.org/ns/prov#DirectQueryService
  Accept: http://www.w3.org/ns/prov#Accept
  Contribute: http://www.w3.org/ns/prov#Contribute
  Contributor: http://www.w3.org/ns/prov#Contributor
  Copyright: http://www.w3.org/ns/prov#Copyright
  Create: http://www.w3.org/ns/prov#Create
  Creator: http://www.w3.org/ns/prov#Creator
  Modify: http://www.w3.org/ns/prov#Modify
  Publish: http://www.w3.org/ns/prov#Publish
  Publisher: http://www.w3.org/ns/prov#Publisher
  Replace: http://www.w3.org/ns/prov#Replace
  RightsAssignment: http://www.w3.org/ns/prov#RightsAssignment
  RightsHolder: http://www.w3.org/ns/prov#RightsHolder
  Submit: http://www.w3.org/ns/prov#Submit
  Dictionary: http://www.w3.org/ns/prov#Dictionary
  EmptyDictionary: http://www.w3.org/ns/prov#EmptyDictionary
  KeyEntityPair: http://www.w3.org/ns/prov#KeyEntityPair
  Insertion: http://www.w3.org/ns/prov#Insertion
  Removal: http://www.w3.org/ns/prov#Removal
  atTime:
    x-jsonld-id: http://www.w3.org/ns/prov#atTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  endedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#endedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  generatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#generatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  invalidatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#invalidatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  startedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#startedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  value: http://www.w3.org/ns/prov#value
  provenanceUriTemplate: http://www.w3.org/ns/prov#provenanceUriTemplate
  pairKey:
    x-jsonld-id: http://www.w3.org/ns/prov#pairKey
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  removedKey:
    x-jsonld-id: http://www.w3.org/ns/prov#removedKey
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  actedOnBehalfOf:
    x-jsonld-id: http://www.w3.org/ns/prov#actedOnBehalfOf
    x-jsonld-type: '@id'
  agent:
    x-jsonld-id: http://www.w3.org/ns/prov#agent
    x-jsonld-type: '@id'
  entity:
    x-jsonld-id: http://www.w3.org/ns/prov#entity
    x-jsonld-type: '@id'
  generated:
    x-jsonld-id: http://www.w3.org/ns/prov#generated
    x-jsonld-type: '@id'
  hadActivity:
    x-jsonld-id: http://www.w3.org/ns/prov#hadActivity
    x-jsonld-type: '@id'
  activity:
    x-jsonld-id: http://www.w3.org/ns/prov#activity
    x-jsonld-type: '@id'
  hadGeneration:
    x-jsonld-id: http://www.w3.org/ns/prov#hadGeneration
    x-jsonld-type: '@id'
  hadPlan:
    x-jsonld-id: http://www.w3.org/ns/prov#hadPlan
    x-jsonld-type: '@id'
  hadRole:
    x-jsonld-id: http://www.w3.org/ns/prov#hadRole
    x-jsonld-type: '@id'
  hadUsage:
    x-jsonld-id: http://www.w3.org/ns/prov#hadUsage
    x-jsonld-type: '@id'
  influenced:
    x-jsonld-id: http://www.w3.org/ns/prov#influenced
    x-jsonld-type: '@id'
  influencer:
    x-jsonld-id: http://www.w3.org/ns/prov#influencer
    x-jsonld-type: '@id'
  invalidated:
    x-jsonld-id: http://www.w3.org/ns/prov#invalidated
    x-jsonld-type: '@id'
  qualifiedAssociation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedAssociation
    x-jsonld-type: '@id'
  qualifiedCommunication:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedCommunication
    x-jsonld-type: '@id'
  qualifiedDelegation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedDelegation
    x-jsonld-type: '@id'
  qualifiedEnd:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedEnd
    x-jsonld-type: '@id'
  qualifiedPrimarySource:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedPrimarySource
    x-jsonld-type: '@id'
  qualifiedQuotation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedQuotation
    x-jsonld-type: '@id'
  qualifiedRevision:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedRevision
    x-jsonld-type: '@id'
  qualifiedStart:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedStart
    x-jsonld-type: '@id'
  qualifiedUsage:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedUsage
    x-jsonld-type: '@id'
  used:
    x-jsonld-id: http://www.w3.org/ns/prov#used
    x-jsonld-type: '@id'
  wasAssociatedWith:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAssociatedWith
    x-jsonld-type: '@id'
  wasEndedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasEndedBy
    x-jsonld-type: '@id'
  wasInformedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasInformedBy
    x-jsonld-type: '@id'
  wasStartedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasStartedBy
    x-jsonld-type: '@id'
  has_anchor:
    x-jsonld-id: http://www.w3.org/ns/prov#has_anchor
    x-jsonld-type: '@id'
  has_query_service:
    x-jsonld-id: http://www.w3.org/ns/prov#has_query_service
    x-jsonld-type: '@id'
  describesService:
    x-jsonld-id: http://www.w3.org/ns/prov#describesService
    x-jsonld-type: '@id'
  pingback:
    x-jsonld-id: http://www.w3.org/ns/prov#pingback
    x-jsonld-type: '@id'
  dictionary:
    x-jsonld-id: http://www.w3.org/ns/prov#dictionary
    x-jsonld-type: '@id'
  derivedByInsertionFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#derivedByInsertionFrom
    x-jsonld-type: '@id'
  derivedByRemovalFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#derivedByRemovalFrom
    x-jsonld-type: '@id'
  insertedKeyEntityPair:
    x-jsonld-id: http://www.w3.org/ns/prov#insertedKeyEntityPair
    x-jsonld-type: '@id'
  hadDictionaryMember:
    x-jsonld-id: http://www.w3.org/ns/prov#hadDictionaryMember
    x-jsonld-type: '@id'
  pairEntity:
    x-jsonld-id: http://www.w3.org/ns/prov#pairEntity
    x-jsonld-type: '@id'
  qualifiedInsertion:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInsertion
    x-jsonld-type: '@id'
  qualifiedRemoval:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedRemoval
    x-jsonld-type: '@id'
  asInBundle:
    x-jsonld-id: http://www.w3.org/ns/prov#asInBundle
    x-jsonld-type: '@id'
  mentionOf:
    x-jsonld-id: http://www.w3.org/ns/prov#mentionOf
    x-jsonld-type: '@id'
  role: https://w3id.org/ogc/hosted/seadots/catalog#role
  convention: https://w3id.org/ogc/hosted/seadots/catalog#metadataConvention
  cf:parameter:
    x-jsonld-id: https://stac-extensions.github.io/cf/v0.2.0/schema.json#parameter
    x-jsonld-container: '@set'
  schema:
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
  derivedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
    x-jsonld-container: '@set'
    x-jsonld-type: '@id'
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/catalog#
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  dct: http://purl.org/dc/terms/
  rec: https://www.opengis.net/def/ogc-api/records/
  xsd: http://www.w3.org/2001/XMLSchema#
  dcat: http://www.w3.org/ns/dcat#
  skos: http://www.w3.org/2004/02/skos/core#
  thns: https://w3id.org/ogc/stac/themes/
  stac: https://w3id.org/ogc/stac/core/
  oa: http://www.w3.org/ns/oa#
  prov: http://www.w3.org/ns/prov#
  cf: https://stac-extensions.github.io/cf/v0.2.0/schema.json#
  seadots: https://w3id.org/ogc/hosted/seadots/catalog#
  dcterms: http://purl.org/dc/terms/
  table: https://stac-extensions.github.io/table/v1.2.0/schema.json#
  qudt: http://qudt.org/schema/qudt/
  owl: http://www.w3.org/2002/07/owl#
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  w3ctime: http://www.w3.org/2006/time#
  dctype: http://purl.org/dc/dcmitype/
  vcard: http://www.w3.org/2006/vcard/ns#
  foaf: http://xmlns.com/foaf/0.1/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data-tabular/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data-tabular/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/catalog#",
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
    "type": "dct:type",
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
      "@id": "dct:subject"
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
      "@id": "thns:schemes",
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
    "stac_extensions": "stac:hasExtension",
    "assets": {
      "@context": {
        "@vocab": "https://w3id.org/ogc/stac/assets/",
        "type": "dct:format",
        "roles": {
          "@id": "stac:roles",
          "@container": "@set"
        }
      },
      "@id": "stac:hasAsset",
      "@container": "@set"
    },
    "stac_version": "stac:version",
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
    "extent": "dct:extent",
    "item_assets": {
      "@context": {
        "type": "@type"
      }
    },
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
    "wasInfluencedBy": {
      "@context": {
        "name": "rdfs:label"
      },
      "@id": "prov:wasInfluencedBy",
      "@type": "@id"
    },
    "qualifiedInfluence": {
      "@context": {
        "influencer": {
          "@context": {
            "name": "rdfs:label"
          },
          "@id": "prov:influencer",
          "@type": "@id"
        },
        "activity": {
          "@context": {
            "name": "rdfs:label"
          },
          "@id": "prov:activity",
          "@type": "@id"
        },
        "agent": {
          "@context": {
            "name": "rdfs:label"
          },
          "@id": "prov:agent",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedInfluence",
      "@type": "@id"
    },
    "hadMember": {
      "@id": "prov:hadMember",
      "@type": "@id"
    },
    "provType": "@type",
    "featureType": "@type",
    "entityType": "@type",
    "has_provenance": {
      "@context": {
        "name": "rdfs:label"
      },
      "@id": "dct:provenance",
      "@type": "@id"
    },
    "wasGeneratedBy": {
      "@context": {
        "name": "rdfs:label"
      },
      "@id": "prov:wasGeneratedBy",
      "@type": "@id"
    },
    "wasAttributedTo": {
      "@context": {
        "name": "rdfs:label"
      },
      "@id": "prov:wasAttributedTo",
      "@type": "@id"
    },
    "wasDerivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@type": "@id"
    },
    "alternateOf": {
      "@id": "prov:alternateOf",
      "@type": "@id"
    },
    "hadPrimarySource": {
      "@id": "prov:hadPrimarySource",
      "@type": "@id"
    },
    "specializationOf": {
      "@id": "prov:specializationOf",
      "@type": "@id"
    },
    "wasInvalidatedBy": {
      "@context": {
        "name": "rdfs:label"
      },
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
    "generatedAtTime": {
      "@id": "prov:generatedAtTime",
      "@type": "xsd:dateTime"
    },
    "invalidatedAtTime": {
      "@id": "prov:invalidatedAtTime",
      "@type": "xsd:dateTime"
    },
    "value": "prov:value",
    "qualifiedPrimarySource": {
      "@context": {
        "hadActivity": {
          "@context": {
            "wasAssociatedWith": {
              "@context": {
                "name": "rdfs:label"
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "name": "rdfs:label"
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedPrimarySource",
      "@type": "@id"
    },
    "qualifiedQuotation": {
      "@context": {
        "hadActivity": {
          "@context": {
            "wasAssociatedWith": {
              "@context": {
                "name": "rdfs:label"
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "name": "rdfs:label"
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedQuotation",
      "@type": "@id"
    },
    "qualifiedRevision": {
      "@context": {
        "hadActivity": {
          "@context": {
            "wasAssociatedWith": {
              "@context": {
                "name": "rdfs:label"
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "name": "rdfs:label"
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedRevision",
      "@type": "@id"
    },
    "atLocation": {
      "@id": "prov:atLocation",
      "@type": "@id"
    },
    "qualifiedGeneration": {
      "@id": "prov:qualifiedGeneration",
      "@type": "@id"
    },
    "qualifiedInvalidation": {
      "@id": "prov:qualifiedInvalidation",
      "@type": "@id"
    },
    "qualifiedDerivation": {
      "@context": {
        "hadActivity": {
          "@context": {
            "wasAssociatedWith": {
              "@context": {
                "name": "rdfs:label"
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "name": "rdfs:label"
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedDerivation",
      "@type": "@id"
    },
    "qualifiedAttribution": {
      "@context": {
        "agent": {
          "@context": {
            "name": "rdfs:label"
          },
          "@id": "prov:agent",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedAttribution",
      "@type": "@id"
    },
    "activityType": "@type",
    "agentType": "@type",
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
    "startedAtTime": {
      "@id": "prov:startedAtTime",
      "@type": "xsd:dateTime"
    },
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
    "hadPlan": {
      "@id": "prov:hadPlan",
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
    "qualifiedCommunication": {
      "@id": "prov:qualifiedCommunication",
      "@type": "@id"
    },
    "qualifiedDelegation": {
      "@id": "prov:qualifiedDelegation",
      "@type": "@id"
    },
    "qualifiedEnd": {
      "@id": "prov:qualifiedEnd",
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
    "used": {
      "@id": "prov:used",
      "@type": "@id"
    },
    "wasAssociatedWith": {
      "@id": "prov:wasAssociatedWith",
      "@type": "@id"
    },
    "wasEndedBy": {
      "@id": "prov:wasEndedBy",
      "@type": "@id"
    },
    "wasInformedBy": {
      "@id": "prov:wasInformedBy",
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
    "name": "dct:title",
    "unit": {
      "@id": "qudt:unit",
      "@context": {
        "@base": "http://qudt.org/vocab/unit/"
      }
    },
    "rights": "dcat:rights",
    "cf:parameter": {
      "@id": "cf:parameter",
      "@container": "@set"
    },
    "schema": {
      "@id": "dct:conformsTo",
      "@type": "@id"
    },
    "role": "seadots:role",
    "convention": "seadots:metadataConvention",
    "derivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@container": "@set",
      "@type": "@id"
    },
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
    "stac": "https://w3id.org/ogc/stac/core/",
    "cf": "https://stac-extensions.github.io/cf/v0.2.0/schema.json#",
    "seadots": "https://w3id.org/ogc/hosted/seadots/catalog#",
    "dcterms": "http://purl.org/dc/terms/",
    "qudt": "http://qudt.org/schema/qudt/",
    "table": "https://stac-extensions.github.io/table/v1.2.0/schema.json#",
    "table:columns": {
      "@container": "@list"
    },
    "table:row_count": {
      "@type": "xsd:integer"
    },
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data-tabular/context.jsonld)

## Sources

* [SeaDOTs Interoperability Framework - Catalog Metadata Model](https://github.com/ogcincubator/bblocks-seadots)
* [STAC table extension](https://github.com/stac-extensions/table)
* [GeoParquet specification](https://geoparquet.org/)
* [OGC API - Records](https://docs.ogc.org/is/20-004/20-004.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/catalog-data-tabular`

