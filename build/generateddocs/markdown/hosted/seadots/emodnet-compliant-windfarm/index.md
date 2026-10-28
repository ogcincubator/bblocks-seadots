
# EMODnet windfarm (Schema)

`ogc.hosted.seadots.emodnet-compliant-windfarm` *v0.1*

GeoJSON representation of EMODnet Human Activities windfarms, aligned with the official WFS/XSD field names, optionality, nullability, and value types.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# EMODnet windfarm

This is the single EMODnet windfarm representation in this register. It is a
GeoJSON representation aligned with the official EMODnet Human Activities
windfarms XSD. It uses the service's published attribute names and primitive
types and maps the official `the_geom` concept to GeoJSON `geometry`.

The XSD fields are optional and nillable, and the schema reflects that. The
`country` value is represented as the source country name, not as an ISO code;
the underlying field is a nullable `xsd:string`. `context.jsonld` and
`ontology.ttl` bind country names currently observed in the live service to the
[EU Publications Office Country authority table](http://publications.europa.eu/resource/authority/country/).

The properties are `country`, `n_turbines`, `power_mw`, `status`, `type_inst`,
`updateyear`, `year`, `dist_coast`, and `notes`.

Source-specific extracts, such as the Baltic exercise CSV, are translated into
this representation before being served. Their column mapping is exercise
configuration, not a second EMODnet data model.

The independent [`emodnet-compliant-windfarm-pl`](../emodnet-compliant-windfarm-pl/)
block uses this representation for Polish national-source integration, adding
project names, reporting details, provenance, and location matching. The
independent [`emodnet-compliant-windfarm-no`](../emodnet-compliant-windfarm-no/)
block demonstrates the same base model with Norwegian NVE source details.

This block is intended for publication as a GeoJSON Feature or WFS feature and
as an interchange layer before downstream semantic enrichment.

## Examples

### EMODnet sample windfarm feature
A point-based example that mirrors the official EMODnet windfarms XSD field names and uses the same geometry-to-attribute mapping as the service.

#### json
```json
{
  "id": "https://example.org/windfarms/belgium-belwind-alstom-haliade-demonstration-bligh-bank",
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [2.84, 51.69]
  },
  "properties": {
    "country": "Belgium",
    "n_turbines": 1,
    "power_mw": 6,
    "status": "Production",
    "type_inst": "Grounded",
    "updateyear": "2024",
    "year": "2013",
    "dist_coast": 43900.7770495,
    "notes": null
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-compliant-windfarm/context.jsonld",
  "id": "https://example.org/windfarms/belgium-belwind-alstom-haliade-demonstration-bligh-bank",
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [
      2.84,
      51.69
    ]
  },
  "properties": {
    "country": "Belgium",
    "n_turbines": 1,
    "power_mw": 6,
    "status": "Production",
    "type_inst": "Grounded",
    "updateyear": "2024",
    "year": "2013",
    "dist_coast": 43900.7770495,
    "notes": null
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

<https://example.org/windfarms/belgium-belwind-alstom-haliade-demonstration-bligh-bank> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 2.84e+00 5.169e+01 ) ] ;
    geojson:properties [ schema:additionalType "Grounded" ;
            schema:addressCountry seadots-emodnet:Belgium ;
            seadots:distanceToCoast 4.390078e+04 ;
            seadots:nTurbines 1 ;
            seadots:powerMW 6 ;
            seadots:updateYear "2024" ;
            seadots:year "2013" ;
            seadots-emodnet: seadots-emodnet:Production ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EMODnet windfarm feature
description: 'GeoJSON representation of the EMODnet Human Activities windfarms feature
  type. Property names, optionality, nullability, and value types follow the service''s
  published windfarms XSD.

  '
type: object
required:
- id
- type
- geometry
- properties
properties:
  id:
    type: string
    x-jsonld-id: '@id'
  type:
    const: Feature
    x-jsonld-id: '@type'
  geometry:
    description: EMODnet the_geom represented as GeoJSON geometry; the XSD allows
      it to be nil.
    oneOf:
    - type: 'null'
    - type: object
      required:
      - type
      - coordinates
      properties:
        type:
          enum:
          - Point
          - MultiPoint
          - LineString
          - MultiLineString
          - Polygon
          - MultiPolygon
          - GeometryCollection
          x-jsonld-id: '@type'
        coordinates:
          x-jsonld-id: https://purl.org/geojson/vocab#coordinates
          x-jsonld-container: '@list'
      additionalProperties: true
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
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
    x-jsonld-id: https://purl.org/geojson/vocab#properties
  additionalProperties:
    not: true
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
  Point: https://purl.org/geojson/vocab#Point
  Polygon: https://purl.org/geojson/vocab#Polygon
  MultiPolygon: https://purl.org/geojson/vocab#MultiPolygon
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/emodnet/
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  schema: https://schema.org/
  seadots: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#
  dcterms: http://purl.org/dc/terms/
  seadots-emodnet: https://w3id.org/ogc/hosted/seadots/emodnet/
  inspire-cofv: http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.emodnet-compliant-windfarm
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-07-24'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-compliant-windfarm/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-compliant-windfarm/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/emodnet/",
    "Feature": "geojson:Feature",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "MultiPolygon": "geojson:MultiPolygon",
    "id": "@id",
    "type": "@type",
    "geometry": {
      "@context": {
        "coordinates": {
          "@id": "geojson:coordinates",
          "@container": "@list"
        }
      },
      "@id": "geojson:geometry"
    },
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
        "notes": "dcterms:description"
      },
      "@id": "geojson:properties"
    },
    "geojson": "https://purl.org/geojson/vocab#",
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
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-compliant-windfarm/context.jsonld)

## Sources

* [EMODnet Human Activities — Wind Farms service](https://www.emodnet-humanactivities.eu/)
* [EMODnet windfarms XSD](https://ows.emodnet-humanactivities.eu/wfs?request=DescribeFeatureType&typeName=emodnet:windfarms)
* [EU Publications Office Country authority table](http://publications.europa.eu/resource/authority/country/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/emodnet-compliant-windfarm`

