
# Marine Area of Interest (Schema)

`ogc.hosted.seadots.area-of-interest` *v0.1*

Simple GeoJSON Feature profile for a polygon delimiting a marine area of interest (AOI) used by experiments, monitoring programmes, or impact assessments. The polygon is carried only in the top-level GeoJSON `geometry`; `properties` carries a human-readable `title` and `description`.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Marine Area of Interest

Simple GeoJSON Feature profile for a polygon delimiting a marine area of
interest.

The AOI polygon is carried only by the top-level GeoJSON `geometry` member.
The `properties` object carries only a human-readable `title` and
`description`. Derived values such as bbox, centroid, area, CRS, and provenance
are intentionally omitted to avoid duplicating information that can be computed
from the geometry or managed by a separate metadata record.

## Examples

### AOI — surroundings of Utsira island
#### json
```json
{
  "id": "https://example.org/norwegian-ses/area-of-interest/utsira-surroundings",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [4.20, 59.10],
      [5.30, 59.10],
      [5.30, 59.70],
      [4.20, 59.70],
      [4.20, 59.10]
    ]]
  },
  "properties": {
    "title": "AOI — surroundings of Utsira island",
    "description": "Polygon delimiting the broader study area around Utsira island. Extends the Utsira Nord licence polygon outward to cover the surroundings, while preserving the western and southern boundaries used by the original demonstrator."
  },
  "links": [
    { "rel": "describedby", "href": "bblocks://ogc.hosted.seadots.area-of-interest", "type": "application/schema+json", "title": "Marine Area of Interest bblock" }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/area-of-interest/context.jsonld",
  "id": "https://example.org/norwegian-ses/area-of-interest/utsira-surroundings",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          4.2,
          59.1
        ],
        [
          5.3,
          59.1
        ],
        [
          5.3,
          59.7
        ],
        [
          4.2,
          59.7
        ],
        [
          4.2,
          59.1
        ]
      ]
    ]
  },
  "properties": {
    "title": "AOI \u2014 surroundings of Utsira island",
    "description": "Polygon delimiting the broader study area around Utsira island. Extends the Utsira Nord licence polygon outward to cover the surroundings, while preserving the western and southern boundaries used by the original demonstrator."
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.area-of-interest",
      "type": "application/schema+json",
      "title": "Marine Area of Interest bblock"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <https://purl.org/geojson/vocab#> .
@prefix ns2: <http://www.w3.org/ns/iana/link-relations/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/norwegian-ses/area-of-interest/utsira-surroundings> a ns1:Feature ;
    ns2:relation <bblocks://ogc.hosted.seadots.area-of-interest> ;
    ns1:geometry [ a ns1:Polygon ;
            ns1:coordinates ( ( ( 4.2e+00 5.91e+01 ) ( 5.3e+00 5.91e+01 ) ( 5.3e+00 5.97e+01 ) ( 4.2e+00 5.97e+01 ) ( 4.2e+00 5.91e+01 ) ) ) ] ;
    ns1:properties [ dcterms:description "Polygon delimiting the broader study area around Utsira island. Extends the Utsira Nord licence polygon outward to cover the surroundings, while preserving the western and southern boundaries used by the original demonstrator." ;
            dcterms:title "AOI — surroundings of Utsira island" ] .

<bblocks://ogc.hosted.seadots.area-of-interest> a <file:///github/workspace/application/schema+json> ;
    ns1:rel "describedby" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Marine Area of Interest
description: 'Simple GeoJSON Feature profile for a polygon-delimited marine area of
  interest. The AOI geometry is represented only by the top-level GeoJSON geometry
  member. The feature properties carry only a title and description.

  '
type: object
required:
- type
- geometry
- properties
properties:
  type:
    const: Feature
    x-jsonld-id: '@type'
  geometry:
    description: GeoJSON Polygon delimiting the AOI.
    type: object
    required:
    - type
    - coordinates
    properties:
      type:
        const: Polygon
        x-jsonld-id: '@type'
      coordinates:
        type: array
        x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
  properties:
    type: object
    required:
    - title
    - description
    properties:
      title:
        type: string
        x-jsonld-id: http://purl.org/dc/terms/title
      description:
        type: string
        x-jsonld-id: http://purl.org/dc/terms/description
    x-jsonld-id: https://purl.org/geojson/vocab#properties
x-jsonld-extra-terms:
  id: '@id'
  Feature: https://purl.org/geojson/vocab#Feature
  Polygon: https://purl.org/geojson/vocab#Polygon
  links:
    x-jsonld-id: http://www.w3.org/ns/iana/link-relations/relation
    x-jsonld-container: '@set'
  href: '@id'
  rel: https://purl.org/geojson/vocab#rel
x-jsonld-prefixes:
  dcterms: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/area-of-interest/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/area-of-interest/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "id": "@id",
    "Feature": "https://purl.org/geojson/vocab#Feature",
    "Polygon": "https://purl.org/geojson/vocab#Polygon",
    "links": {
      "@id": "http://www.w3.org/ns/iana/link-relations/relation",
      "@container": "@set"
    },
    "href": "@id",
    "rel": "https://purl.org/geojson/vocab#rel",
    "type": "@type",
    "geometry": {
      "@context": {
        "coordinates": {
          "@id": "https://purl.org/geojson/vocab#coordinates",
          "@container": "@list"
        }
      },
      "@id": "https://purl.org/geojson/vocab#geometry"
    },
    "properties": {
      "@context": {
        "title": "dcterms:title",
        "description": "dcterms:description"
      },
      "@id": "https://purl.org/geojson/vocab#properties"
    },
    "dcterms": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/area-of-interest/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/area-of-interest`

