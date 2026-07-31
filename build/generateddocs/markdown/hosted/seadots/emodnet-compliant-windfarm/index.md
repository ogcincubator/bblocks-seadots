
# EMODnet-compliant windfarm (Schema)

`ogc.hosted.seadots.emodnet-compliant-windfarm` *v0.1*

GeoJSON Feature profile aligned to the official EMODnet Human Activities windfarms XSD. It preserves the service's published field names and primitive types for country, turbine count, power output, status, installation type, year fields, distance to coast, and notes.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# EMODnet-compliant windfarm

This block is a GeoJSON Feature profile aligned with the official EMODnet Human
Activities windfarms XSD. It uses the same published attribute names as the
service schema and maps the official `the_geom` concept to the GeoJSON
`geometry` object.

The profile is intentionally flat and service-aligned with the following
properties. The `country` value is represented as the source country name,
not as an ISO code, and is not restricted to a fixed enumeration — the
underlying EMODnet field is a free-text `xsd:string` (see
`examples/emodnet-windfarms.xsd`) and can hold any country name the service
publishes. `context.jsonld` and `ontology.ttl` bind the country names
currently observed in the live service (queried via WFS
`GetPropertyValue`: Belgium, Denmark, Estonia, Finland, France, Germany,
Greece, Ireland, Italy, Latvia, Lithuania, Malta, Netherlands, Norway,
Poland, Portugal, Romania, Spain, Sweden, United Kingdom) to the
[EU Publications Office Country authority table](http://publications.europa.eu/resource/authority/country/)
(e.g. Belgium -> `http://publications.europa.eu/resource/authority/country/BEL`),
whose ISO 3166-1 alpha-3 codes cover all countries, not just EU/EEA member
states. Any new country name appearing in the source data should be added
to both files following the same pattern.

- `country`
- `n_turbines`
- `power_mw`
- `status`
- `type_inst`
- `updateyear`
- `year`
- `dist_coast`
- `notes`

It is intended for direct publication as a GeoJSON Feature or WFS feature and
can be used as a minimal interchange layer before any downstream semantic
enrichment.

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
title: EMODnet-compliant windfarm
description: 'GeoJSON Feature profile aligned to the official EMODnet Human Activities
  windfarms XSD. It preserves the service''s published field names and primitive types
  for country, turbine count, power output, status, installation type, year fields,
  distance to coast, and notes.

  '
required:
- id
- type
- geometry
- properties
properties:
  id:
    type: string
    format: uri
    x-jsonld-id: '@id'
  type:
    const: Feature
    x-jsonld-id: '@type'
  geometry:
    type: object
    required:
    - type
    - coordinates
    properties:
      type:
        enum:
        - Point
        - Polygon
        - MultiPolygon
        x-jsonld-id: '@type'
      coordinates:
        type: array
        x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
  properties:
    type: object
    required:
    - country
    - n_turbines
    - power_mw
    - status
    - type_inst
    - updateyear
    - year
    - dist_coast
    - notes
    properties:
      country:
        type: string
        description: "Country name of the responsible/coastal country as represented
          in the source data (not restricted to a fixed enumeration \u2014 any country
          name published by the EMODnet Human Activities windfarms service is valid).
          In RDF/JSON-LD, the context binds the country names currently observed in
          the live service to EU Publications Office Country authority table URIs
          (http://publications.europa.eu/resource/authority/country/), e.g. \"Belgium\"
          -> http://publications.europa.eu/resource/authority/country/BEL. Names not
          yet covered by the context fall back to a plain string and should be added
          to the context/ontology as the source data grows."
        x-jsonld-id: https://schema.org/addressCountry
        x-jsonld-type: '@vocab'
      n_turbines:
        type: number
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#nTurbines
      power_mw:
        type: number
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#powerMW
      status:
        type: string
        description: 'Status of the windfarm, as represented in the source data. The
          EMODnet service uses a controlled vocabulary of five values: Planned, Production,
          Dismantled, Approved, Construction.'
        enum:
        - Planned
        - Production
        - Dismantled
        - Approved
        - Construction
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet/
        x-jsonld-type: '@vocab'
      type_inst:
        oneOf:
        - type: string
          enum:
          - Grounded
          - Floating
        - type: 'null'
        x-jsonld-id: https://schema.org/additionalType
      updateyear:
        type: string
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#updateYear
      year:
        type: string
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#year
      dist_coast:
        type: number
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#distanceToCoast
      notes:
        type:
        - string
        - 'null'
        x-jsonld-id: http://purl.org/dc/terms/description
    x-jsonld-id: https://purl.org/geojson/vocab#properties
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

