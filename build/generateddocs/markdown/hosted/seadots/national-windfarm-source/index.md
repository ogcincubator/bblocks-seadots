
# Polish national offshore windfarm source record (Schema)

`ogc.hosted.seadots.national-windfarm-source` *v0.1*

Raw project records compiled from Polish national reporting. Retains the published input fields and has no source-provided geometry; a separate, explicit crosswalk can associate projects with EMODnet locations for the harmonized view.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Polish national offshore windfarm source

This block describes the source-stage record exactly as delivered in the exercise CSV: `farm`, `developer`, `capacity_mw`, `status_aug2026`, `first_power_or_completion_year`, and `source`. Its source rows do **not** contain coordinates. Their geometry therefore remains null in the national-source collection.

The exercise applies the separate `location-mapping.json` crosswalk when it builds the harmonized service. Crosswalked locations are explicitly marked as derived from the listed EMODnet records; a project without a defensible EMODnet match remains unlocated.

## Examples

### National source record without coordinates
One row as reported by the national compilation; no geometry is invented at this stage.
#### json
```json
{"id":"national-001","type":"Feature","geometry":null,"properties":{"farm":"MFW Baltic Power","developer":"Orlen; Northland Power","capacity_mw":1200,"status_aug2026":"construction (first power 10 Jul 2026)","first_power_or_completion_year":2026,"source":"gramwzielone.pl 26 Aug 2026"}}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/national-windfarm-source/context.jsonld",
  "id": "national-001",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "farm": "MFW Baltic Power",
    "developer": "Orlen; Northland Power",
    "capacity_mw": 1200,
    "status_aug2026": "construction (first power 10 Jul 2026)",
    "first_power_or_completion_year": 2026,
    "source": "gramwzielone.pl 26 Aug 2026"
  }
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/ogc/hosted/seadots/national-windfarm-source#> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <https://purl.org/dc/terms/> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/national-001> a geojson:Feature ;
    geojson:properties [ ns1:source "gramwzielone.pl 26 Aug 2026" ;
            schema:creator "Orlen; Northland Power" ;
            :projectName "MFW Baltic Power" ;
            :reportedCapacityMW 1200 ;
            :reportedFirstPowerOrCompletionYear 2026 ;
            :reportedStatusAugust2026 "construction (first power 10 Jul 2026)" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Polish national offshore windfarm source feature
description: GeoJSON Feature wrapper for the national source row. Source property
  names and values are retained. The source has no coordinates; geometry is null until
  an explicit location crosswalk is applied in the harmonized target view.
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
    type: 'null'
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
  properties:
    type: object
    required:
    - farm
    - developer
    - capacity_mw
    - status_aug2026
    - first_power_or_completion_year
    - source
    properties:
      farm:
        type: string
        x-jsonld-id: projectName
      developer:
        type: string
        x-jsonld-id: https://schema.org/creator
      capacity_mw:
        type: string
        x-jsonld-id: reportedCapacityMW
      status_aug2026:
        type: string
        x-jsonld-id: reportedStatusAugust2026
      first_power_or_completion_year:
        type: string
        x-jsonld-id: reportedFirstPowerOrCompletionYear
      source:
        type: string
        x-jsonld-id: https://purl.org/dc/terms/source
    additionalProperties: false
    x-jsonld-id: https://purl.org/geojson/vocab#properties
additionalProperties: false
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/national-windfarm-source#
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.national-windfarm-source
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-27'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/national-windfarm-source/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/national-windfarm-source/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/national-windfarm-source#",
    "Feature": "geojson:Feature",
    "id": "@id",
    "type": "@type",
    "geometry": "geojson:geometry",
    "properties": {
      "@context": {
        "farm": "projectName",
        "developer": "https://schema.org/creator",
        "capacity_mw": "reportedCapacityMW",
        "status_aug2026": "reportedStatusAugust2026",
        "first_power_or_completion_year": "reportedFirstPowerOrCompletionYear",
        "source": "https://purl.org/dc/terms/source"
      },
      "@id": "geojson:properties"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/national-windfarm-source/context.jsonld)

## Sources

* [Polish offshore wind project compilation](https://www.gramwzielone.pl/?p=20373718)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/national-windfarm-source`

