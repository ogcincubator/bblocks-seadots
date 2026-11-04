
# EMODnet windfarm (Schema)

`ogc.hosted.seadots.windfarms.windfarm-designated-area-emodnet` *v0.1*

GeoJSON representation of EMODnet Human Activities windfarms, aligned with the official WFS/XSD field names and actual data cmoing from the service, optionality, nullability, and value types.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# EMODnet windfarm

This is the single EMODnet windfarm designating area representation in this register. It is a
GeoJSON representation aligned with the official EMODnet Human Activities
windfarms XSD. It uses the service's published attribute names and primitive
types and maps the official `the_geom` concept to GeoJSON `geometry`.

The XSD fields are optional and nillable, and the schema reflects that. The
`country` value is represented as the source country name, not as an ISO code;
the underlying field is a nullable `xsd:string`. `context.jsonld` and
`ontology.ttl` bind country names currently observed in the live service to the
[EU Publications Office Country authority table](http://publications.europa.eu/resource/authority/country/).

The properties are `country`, `n_turbines`, `power_mw`, `status`, `type_inst`, `updateyear`, `year`, `dist_coast`, and `notes`.

Source-specific extracts, such as the Baltic exercise CSV, are translated into this representation before being served. Their column mapping is exercise configuration, not a second EMODnet data model.


This block is intended for publication as a GeoJSON Feature or WFS feature and as an interchange layer before downstream semantic enrichment.

## Examples

### EMODnet sample windfarm feature
An example does not mirrors the official EMODnet windfarms XSD field names and uses the same geometry-to-attribute mapping as the service.

#### json
```json
{
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "id": "windfarms.557",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    15.4921,
                    54.3636
                ]
            },
            "geometry_name": "the_geom",
            "properties": {
                "country": "Poland",
                "name": "Energa MFW 1 Offshore wind farm 1",
                "n_turbines": null,
                "power_mw": 900.0,
                "status": "Planned",
                "type_inst": "Grounded",
                "updateyear": "2026",
                "year": null,
                "dist_coast": 20067.2199269,
                "notes": null
            }
        },
        {
            "type": "Feature",
            "id": "windfarms.610",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    16.49,
                    55.05
                ]
            },
            "geometry_name": "the_geom",
            "properties": {
                "country": "Poland",
                "name": "Baltica 9",
                "n_turbines": null,
                "power_mw": 975.0,
                "status": "Planned",
                "type_inst": null,
                "updateyear": "2026",
                "year": null,
                "dist_coast": 33842.6488621,
                "notes": null
            }
        },
        {
            "type": "Feature",
            "id": "windfarms.613",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    17.84,
                    55.05
                ]
            },
            "geometry_name": "the_geom",
            "properties": {
                "country": "Poland",
                "name": "Baltic East",
                "n_turbines": null,
                "power_mw": 966.0,
                "status": "Planned",
                "type_inst": null,
                "updateyear": "2026",
                "year": null,
                "dist_coast": 25390.2169917,
                "notes": null
            }
        }
    ],
    "totalFeatures": 26,
    "numberMatched": 26,
    "numberReturned": 26,
    "timeStamp": "2026-10-29T22:52:51.131Z",
    "crs": {
        "type": "name",
        "properties": {
            "name": "urn:ogc:def:crs:EPSG::4326"
        }
    }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/windfarm-designated-area-emodnet/context.jsonld",
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": "windfarms.557",
      "geometry": {
        "type": "Point",
        "coordinates": [
          15.4921,
          54.3636
        ]
      },
      "geometry_name": "the_geom",
      "properties": {
        "country": "Poland",
        "name": "Energa MFW 1 Offshore wind farm 1",
        "n_turbines": null,
        "power_mw": 900.0,
        "status": "Planned",
        "type_inst": "Grounded",
        "updateyear": "2026",
        "year": null,
        "dist_coast": 20067.2199269,
        "notes": null
      }
    },
    {
      "type": "Feature",
      "id": "windfarms.610",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.49,
          55.05
        ]
      },
      "geometry_name": "the_geom",
      "properties": {
        "country": "Poland",
        "name": "Baltica 9",
        "n_turbines": null,
        "power_mw": 975.0,
        "status": "Planned",
        "type_inst": null,
        "updateyear": "2026",
        "year": null,
        "dist_coast": 33842.6488621,
        "notes": null
      }
    },
    {
      "type": "Feature",
      "id": "windfarms.613",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.84,
          55.05
        ]
      },
      "geometry_name": "the_geom",
      "properties": {
        "country": "Poland",
        "name": "Baltic East",
        "n_turbines": null,
        "power_mw": 966.0,
        "status": "Planned",
        "type_inst": null,
        "updateyear": "2026",
        "year": null,
        "dist_coast": 25390.2169917,
        "notes": null
      }
    }
  ],
  "totalFeatures": 26,
  "numberMatched": 26,
  "numberReturned": 26,
  "timeStamp": "2026-10-29T22:52:51.131Z",
  "crs": {
    "type": "name",
    "properties": {
      "name": "urn:ogc:def:crs:EPSG::4326"
    }
  }
}
```

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#> .
@prefix seadots-emodnet: <https://w3id.org/ogc/hosted/seadots/emodnet/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/windfarms.557> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.54921e+01 5.43636e+01 ) ] ;
    geojson:properties [ schema:additionalType "Grounded" ;
            schema:addressCountry seadots-emodnet:Poland ;
            seadots:distanceToCoast 2.006722e+04 ;
            seadots:powerMW 9e+02 ;
            seadots:updateYear "2026" ;
            seadots-emodnet: seadots-emodnet:Planned ;
            seadots-emodnet:name "Energa MFW 1 Offshore wind farm 1" ] ;
    seadots-emodnet:geometry_name "the_geom" .

<file:///github/workspace/windfarms.610> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.649e+01 5.505e+01 ) ] ;
    geojson:properties [ schema:addressCountry seadots-emodnet:Poland ;
            seadots:distanceToCoast 3.384265e+04 ;
            seadots:powerMW 9.75e+02 ;
            seadots:updateYear "2026" ;
            seadots-emodnet: seadots-emodnet:Planned ;
            seadots-emodnet:name "Baltica 9" ] ;
    seadots-emodnet:geometry_name "the_geom" .

<file:///github/workspace/windfarms.613> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.784e+01 5.505e+01 ) ] ;
    geojson:properties [ schema:addressCountry seadots-emodnet:Poland ;
            seadots:distanceToCoast 2.539022e+04 ;
            seadots:powerMW 9.66e+02 ;
            seadots:updateYear "2026" ;
            seadots-emodnet: seadots-emodnet:Planned ;
            seadots-emodnet:name "Baltic East" ] ;
    seadots-emodnet:geometry_name "the_geom" .

[] a geojson:FeatureCollection ;
    geojson:features <file:///github/workspace/windfarms.557>,
        <file:///github/workspace/windfarms.610>,
        <file:///github/workspace/windfarms.613> ;
    seadots-emodnet:crs [ a seadots-emodnet:name ;
            geojson:properties [ seadots-emodnet:name "urn:ogc:def:crs:EPSG::4326" ] ] ;
    seadots-emodnet:numberMatched 26 ;
    seadots-emodnet:numberReturned 26 ;
    seadots-emodnet:timeStamp "2026-10-29T22:52:51.131Z" ;
    seadots-emodnet:totalFeatures 26 .


```


### Ocean Data Platform sample windfarm feature taken from EMODnet
this is real data from the 

#### json
```json
{
"type": "Feature",
"geometry": {
"type": "Polygon",
    "coordinates": [[
      [4.40, 59.20],
      [5.10, 59.20],
      [5.10, 59.55],
      [4.40, 59.55],
      [4.40, 59.20]
    ]]
},
"properties": {
"country": "United Kingdom",
"name": "Dogger Bank East Met Mast",
"n_turbines": 1,
"power_mw": null,
"status": "Dismantled",
"updateyear": null,
"year": null,
"dist_coast": 210099.226384,
"area_sqkm": 0.19595891411,
"notes": null,
"shape_leng": 0.0196987539439,
"shape_area": 0.0000275744276405
},
"id": 0
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/windfarm-designated-area-emodnet/context.jsonld",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          4.4,
          59.2
        ],
        [
          5.1,
          59.2
        ],
        [
          5.1,
          59.55
        ],
        [
          4.4,
          59.55
        ],
        [
          4.4,
          59.2
        ]
      ]
    ]
  },
  "properties": {
    "country": "United Kingdom",
    "name": "Dogger Bank East Met Mast",
    "n_turbines": 1,
    "power_mw": null,
    "status": "Dismantled",
    "updateyear": null,
    "year": null,
    "dist_coast": 210099.226384,
    "area_sqkm": 0.19595891411,
    "notes": null,
    "shape_leng": 0.0196987539439,
    "shape_area": 2.75744276405e-05
  },
  "id": 0
}
```

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#> .
@prefix seadots-emodnet: <https://w3id.org/ogc/hosted/seadots/emodnet/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/0> a geojson:Feature ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 4.4e+00 5.92e+01 ) ( 5.1e+00 5.92e+01 ) ( 5.1e+00 5.955e+01 ) ( 4.4e+00 5.955e+01 ) ( 4.4e+00 5.92e+01 ) ) ) ] ;
    geojson:properties [ seadots:distanceToCoast 2.100992e+05 ;
            seadots:nTurbines 1 ;
            seadots-emodnet: seadots-emodnet:Dismantled ;
            seadots-emodnet:area_sqkm 1.959589e-01 ;
            seadots-emodnet:name "Dogger Bank East Met Mast" ;
            seadots-emodnet:shape_area 2.757443e-05 ;
            seadots-emodnet:shape_leng 1.969875e-02 ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EMODnet windfarm feature
description: 'GeoJSON representation of the EMODnet Human Activities windfarms feature
  type. Property names, optionality, nullability, and value types follow the service''s
  published windfarms XSD.

  '
allOf:
- $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.yaml
- type: object
  required:
  - properties
  properties:
    properties:
      type: object
      properties:
        country:
          type:
          - string
          - 'null'
          description: Country name as published by EMODnet; the XSD type is nullable
            xsd:string.
          x-jsonld-id: https://schema.org/addressCountry
          x-jsonld-type: '@vocab'
        n_turbines:
          type:
          - number
          - 'null'
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#nTurbines
        power_mw:
          type:
          - number
          - 'null'
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#powerMW
        status:
          type:
          - string
          - 'null'
          description: Status text as published by EMODnet (nullable xsd:string).
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet/
          x-jsonld-type: '@vocab'
        type_inst:
          type:
          - string
          - 'null'
          x-jsonld-id: https://schema.org/additionalType
        updateyear:
          type:
          - string
          - 'null'
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#updateYear
        year:
          type:
          - string
          - 'null'
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#year
        dist_coast:
          type:
          - number
          - 'null'
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#distanceToCoast
        notes:
          type:
          - string
          - 'null'
          x-jsonld-id: http://purl.org/dc/terms/description
        shape_leng:
          type:
          - number
          - 'null'
        shape_area:
          type:
          - number
          - 'null'
        name:
          type:
          - string
          - 'null'
        area_sqkm:
          type:
          - number
          - 'null'
      x-jsonld-id: https://purl.org/geojson/vocab#properties
    additionalProperties: {}
x-jsonld-extra-terms:
  id: '@id'
  type: '@type'
  Feature: https://purl.org/geojson/vocab#Feature
  Point: https://purl.org/geojson/vocab#Point
  Polygon: https://purl.org/geojson/vocab#Polygon
  MultiPolygon: https://purl.org/geojson/vocab#MultiPolygon
  geometry: https://purl.org/geojson/vocab#geometry
  coordinates:
    x-jsonld-id: https://purl.org/geojson/vocab#coordinates
    x-jsonld-container: '@list'
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/emodnet/
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  schema: https://schema.org/
  seadots: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#
  dcterms: http://purl.org/dc/terms/
  seadots-emodnet: https://w3id.org/ogc/hosted/seadots/emodnet/
  inspire-cofv: http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.windfarms.windfarm-designated-area-emodnet
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-07-24'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/windfarm-designated-area-emodnet/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/windfarm-designated-area-emodnet/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/emodnet/",
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
    "type": "@type",
    "id": "@id",
    "properties": {
      "@context": {
        "country": {
          "@id": "schema:addressCountry",
          "@type": "@vocab"
        },
        "n_turbines": "seadots:nTurbines",
        "power_mw": "seadots:powerMW",
        "status": {
          "@id": "https://w3id.org/ogc/hosted/seadots/emodnet/",
          "@type": "@vocab"
        },
        "type_inst": "schema:additionalType",
        "updateyear": "seadots:updateYear",
        "year": "seadots:year",
        "dist_coast": "seadots:distanceToCoast",
        "notes": "dct:description"
      },
      "@id": "geojson:properties"
    },
    "geometry": "geojson:geometry",
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "links": {
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
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
    "coordinates": {
      "@id": "geojson:coordinates",
      "@container": "@list"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "schema": "https://schema.org/",
    "seadots": "https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#",
    "dcterms": "http://purl.org/dc/terms/",
    "seadots-emodnet": "https://w3id.org/ogc/hosted/seadots/emodnet/",
    "inspire-cofv": "http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/windfarm-designated-area-emodnet/context.jsonld)

## Sources

* [EMODnet Human Activities — Wind Farms service](https://www.emodnet-humanactivities.eu/)
* [EMODnet windfarms XSD, NOTE XSD does not match Feature services which contain additional 3 fields: ](https://ows.emodnet-humanactivities.eu/wfs?request=DescribeFeatureType&typeName=emodnet:windfarms)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/windfarms/windfarm-designated-area-emodnet`

