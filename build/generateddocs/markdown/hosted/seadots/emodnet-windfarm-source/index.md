
# EMODnet Human Activities windfarm source snapshot (Schema)

`ogc.hosted.seadots.emodnet-windfarm-source` *v0.1*

The raw Poland-filtered EMODnet windfarm snapshot used by the Baltic data-integration exercise. Its source properties remain unchanged in the raw collection; a separate translation maps them to the canonical windfarm target block.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# EMODnet Human Activities windfarm source snapshot

This source-stage block keeps the EMODnet source property names, including `dist_coast_m`, `updateyear`, `lon`, and `lat`. The exercise snapshot is the Poland-filtered WFS-derived CSV bundled with the Baltic SES exercise; refresh it from the WFS before regenerating if a newer source edition is required.

`translation.json` records how the raw properties map into the canonical target. The raw API collection remains available alongside the harmonized collection so users can inspect what changed.

## Examples

### EMODnet windfarm source point
Raw source properties retained with their original names and point location.
#### json
```json
{"id":"emodnet-001","type":"Feature","geometry":{"type":"Point","coordinates":[17.65,55.05]},"properties":{"name":"Baltic Power","status":"Construction","power_mw":1140,"n_turbines":76,"year":"2026","dist_coast_m":28427,"updateyear":"2026","lon":17.65,"lat":55.05}}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-windfarm-source/context.jsonld",
  "id": "emodnet-001",
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [
      17.65,
      55.05
    ]
  },
  "properties": {
    "name": "Baltic Power",
    "status": "Construction",
    "power_mw": 1140,
    "n_turbines": 76,
    "year": "2026",
    "dist_coast_m": 28427,
    "updateyear": "2026",
    "lon": 17.65,
    "lat": 55.05
  }
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-source#> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/emodnet-001> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.765e+01 5.505e+01 ) ] ;
    geojson:properties [ schema:name "Baltic Power" ;
            ns1:nTurbines 76 ;
            ns1:powerMW 1140 ;
            ns1:updateYear "2026" ;
            ns1:year "2026" ;
            :distanceToCoastMetres 28427 ;
            :latitude 5.505e+01 ;
            :longitude 1.765e+01 ;
            <https://w3id.org/ogc/hosted/seadots/emodnet/> "Construction" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EMODnet windfarm source feature snapshot
description: Raw Poland-filtered EMODnet source fields used in the exercise snapshot.
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
    type: object
    required:
    - type
    - coordinates
    properties:
      type:
        const: Point
        x-jsonld-id: '@type'
      coordinates:
        type: array
        prefixItems:
        - type: number
        - type: number
        minItems: 2
        maxItems: 2
        x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        x-jsonld-container: '@list'
    additionalProperties: false
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
  properties:
    type: object
    required:
    - name
    - status
    - power_mw
    - n_turbines
    - year
    - dist_coast_m
    - updateyear
    - lon
    - lat
    properties:
      name:
        type: string
        x-jsonld-id: https://schema.org/name
      status:
        type: string
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet/
      power_mw:
        type: string
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#powerMW
      n_turbines:
        type: string
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#nTurbines
      year:
        type: string
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#year
      dist_coast_m:
        type: string
        x-jsonld-id: distanceToCoastMetres
      updateyear:
        type: string
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#updateYear
      lon:
        type: string
        x-jsonld-id: longitude
      lat:
        type: string
        x-jsonld-id: latitude
    additionalProperties: false
    x-jsonld-id: https://purl.org/geojson/vocab#properties
additionalProperties: false
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
  Point: https://purl.org/geojson/vocab#Point
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-source#
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  schema: https://schema.org/
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.emodnet-windfarm-source
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-27'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-windfarm-source/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-windfarm-source/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-source#",
    "Feature": "geojson:Feature",
    "Point": "geojson:Point",
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
        "name": "schema:name",
        "status": "https://w3id.org/ogc/hosted/seadots/emodnet/",
        "power_mw": "https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#powerMW",
        "n_turbines": "https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#nTurbines",
        "year": "https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#year",
        "dist_coast_m": "distanceToCoastMetres",
        "updateyear": "https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#updateYear",
        "lon": "longitude",
        "lat": "latitude"
      },
      "@id": "geojson:properties"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "schema": "https://schema.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-windfarm-source/context.jsonld)

## Sources

* [EMODnet Human Activities WFS windfarms layer](https://ows.emodnet-humanactivities.eu/wfs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/emodnet-windfarm-source`

