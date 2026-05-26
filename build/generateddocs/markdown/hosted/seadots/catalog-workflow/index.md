
# SeaDOTs Catalog Workflow (Schema)

`ogc.hosted.seadots.catalog-workflow` *v0.1*

Generic PROV-O Plan profile for the workflow or method described by a SeaDOTs application.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# SeaDOTs Catalog Workflow

A workflow is the reusable PROV-O Plan behind an application. It describes the intended method, model chain, processing order, version, expected inputs, expected outputs, and the planned Activity pattern that is repeated by every execution.

## Role in the Catalog Metadata Model

This generic building block supports the SeaDOTs catalog model described in
`data_framework/INTEROPERABILITY.md` under `Catalog Metadata Model` and
`2.2 Provenance model (Open Science)`.

## Source-property coverage gaps

This block is a generic catalog template and is not derived from a raw source
dataset. No source properties are intentionally dropped.

## Examples

### SeaDOTs Catalog Workflow
#### json
```json
{
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/workflow/reef-effect",
  "type": "Workflow",
  "title": "Reef-effect biomass workflow",
  "description": "Plan for deriving reef-associated biomass from infrastructure area, baseline biomass density, aggregation factors, and colonisation time.",
  "version": "0.1.0",
  "method": "Evaluate a deterministic biomass equation over the AOI and taxon-specific parameters.",
  "activity": "https://w3id.org/ogc/hosted/seadots/catalog/activity/reef-effect-calculation",
  "inputs": [
    "areaOfInterest",
    "floatingWindInfrastructure",
    "benthicBiomassDensity",
    "reefAggregationIndex",
    "colonisationTimeFactor"
  ],
  "outputs": [
    "reefBiomassOutput"
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-workflow/context.jsonld",
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/workflow/reef-effect",
  "type": "Workflow",
  "title": "Reef-effect biomass workflow",
  "description": "Plan for deriving reef-associated biomass from infrastructure area, baseline biomass density, aggregation factors, and colonisation time.",
  "version": "0.1.0",
  "method": "Evaluate a deterministic biomass equation over the AOI and taxon-specific parameters.",
  "activity": "https://w3id.org/ogc/hosted/seadots/catalog/activity/reef-effect-calculation",
  "inputs": [
    "areaOfInterest",
    "floatingWindInfrastructure",
    "benthicBiomassDensity",
    "reefAggregationIndex",
    "colonisationTimeFactor"
  ],
  "outputs": [
    "reefBiomassOutput"
  ]
}
```

#### ttl
```ttl
@prefix apkg: <https://w3id.org/apkg/terms/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .

<https://w3id.org/ogc/hosted/seadots/catalog/workflow/reef-effect> a seadots:Workflow ;
    dcterms:description "Plan for deriving reef-associated biomass from infrastructure area, baseline biomass density, aggregation factors, and colonisation time." ;
    dcterms:hasVersion "0.1.0" ;
    dcterms:method "Evaluate a deterministic biomass equation over the AOI and taxon-specific parameters." ;
    dcterms:title "Reef-effect biomass workflow" ;
    apkg:inputs "areaOfInterest",
        "benthicBiomassDensity",
        "colonisationTimeFactor",
        "floatingWindInfrastructure",
        "reefAggregationIndex" ;
    apkg:outputs "reefBiomassOutput" ;
    seadots:activity <https://w3id.org/ogc/hosted/seadots/catalog/activity/reef-effect-calculation> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SeaDOTs Catalog Workflow
description: 'PROV-O Plan profile for a reusable SeaDOTs workflow or method.

  '
type: object
required:
- id
- type
- title
- description
- version
- method
properties:
  id:
    type: string
    format: uri
    x-jsonld-id: '@id'
  type:
    const: Workflow
    x-jsonld-id: '@type'
  title:
    type: string
    x-jsonld-id: http://purl.org/dc/terms/title
  description:
    type: string
    x-jsonld-id: http://purl.org/dc/terms/description
  version:
    type: string
    x-jsonld-id: http://purl.org/dc/terms/hasVersion
  method:
    type: string
    x-jsonld-id: http://purl.org/dc/terms/method
  activity:
    type: string
    format: uri
    description: URI of the planned PROV-O Activity pattern contained by this workflow.
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#activity
    x-jsonld-type: '@id'
  inputs:
    type: array
    items:
      type: string
    x-jsonld-id: https://w3id.org/apkg/terms/inputs
    x-jsonld-container: '@set'
  outputs:
    type: array
    items:
      type: string
    x-jsonld-id: https://w3id.org/apkg/terms/outputs
    x-jsonld-container: '@set'
additionalProperties: true
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
  geometry: https://purl.org/geojson/vocab#geometry
  bbox: https://purl.org/geojson/vocab#bbox
  coordinates: https://purl.org/geojson/vocab#coordinates
  properties: https://purl.org/geojson/vocab#properties
  links:
    x-jsonld-id: http://www.w3.org/ns/iana/link-relations/relation
    x-jsonld-container: '@set'
  href: '@id'
  rel: http://www.w3.org/ns/iana/link-relations/relation
  itemType: http://purl.org/dc/terms/type
  conformsTo:
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
    x-jsonld-container: '@set'
  name: http://purl.org/dc/terms/title
  keywords:
    x-jsonld-id: http://www.w3.org/ns/dcat#keyword
    x-jsonld-container: '@set'
  themes:
    x-jsonld-id: http://www.w3.org/ns/dcat#theme
    x-jsonld-container: '@set'
  license:
    x-jsonld-id: http://purl.org/dc/terms/license
    x-jsonld-type: '@id'
  created:
    x-jsonld-id: http://purl.org/dc/terms/created
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  updated:
    x-jsonld-id: http://purl.org/dc/terms/modified
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  applicationCategory: https://schema.org/applicationCategory
  softwareVersion: https://schema.org/softwareVersion
  programmingLanguage: https://schema.org/programmingLanguage
  applicationPackage:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#applicationPackage
    x-jsonld-type: '@id'
  workflow:
    x-jsonld-id: http://www.w3.org/ns/prov#hadPlan
    x-jsonld-type: '@id'
  profileId:
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
  required:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#requiredInput
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
  class: https://w3id.org/cwl/cwl#class
  requirements:
    x-jsonld-id: https://w3id.org/cwl/cwl#requirements
    x-jsonld-container: '@set'
  startTime:
    x-jsonld-id: http://www.w3.org/ns/prov#startedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  endTime:
    x-jsonld-id: http://www.w3.org/ns/prov#endedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  status: https://w3id.org/ogc/hosted/seadots/catalog#status
  parameters: https://w3id.org/ogc/hosted/seadots/catalog#parameters
  timeBoundaryStart:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#timeBoundaryStart
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
  timeBoundaryEnd:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#timeBoundaryEnd
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
  application:
    x-jsonld-id: http://www.w3.org/ns/prov#used
    x-jsonld-type: '@id'
  inputRecords:
    x-jsonld-id: http://www.w3.org/ns/prov#used
    x-jsonld-type: '@id'
    x-jsonld-container: '@set'
  outputRecords:
    x-jsonld-id: http://www.w3.org/ns/prov#generated
    x-jsonld-type: '@id'
    x-jsonld-container: '@set'
  agent:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAssociatedWith
    x-jsonld-type: '@id'
  configuration: https://w3id.org/ogc/hosted/seadots/catalog#configuration
  containerImage: https://w3id.org/ogc/hosted/seadots/catalog#containerImage
  stac_version: https://stacspec.org/vocab#stac_version
  collection:
    x-jsonld-id: http://purl.org/dc/terms/isPartOf
    x-jsonld-type: '@id'
  datetime:
    x-jsonld-id: http://purl.org/dc/terms/date
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  convention: https://w3id.org/ogc/hosted/seadots/catalog#metadataConvention
  cf:parameter:
    x-jsonld-id: https://stac-extensions.github.io/cf/v0.2.0/schema.json#parameter
    x-jsonld-container: '@set'
  unit: http://purl.org/dc/terms/format
  assets: https://stacspec.org/vocab#assets
  data: https://stacspec.org/vocab#data
  derivedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
    x-jsonld-type: '@id'
    x-jsonld-container: '@set'
  role: https://w3id.org/ogc/hosted/seadots/catalog#role
  mediaType: http://purl.org/dc/terms/format
  dockerPull: https://w3id.org/ogc/hosted/seadots/catalog#dockerPull
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/catalog#
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  dcterms: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#
  schema: https://schema.org/
  seadots: https://w3id.org/ogc/hosted/seadots/catalog#
  prov: http://www.w3.org/ns/prov#
  apkg: https://w3id.org/apkg/terms/
  cwl: https://w3id.org/cwl/cwl#
  stac: https://stacspec.org/vocab#
  cf: https://stac-extensions.github.io/cf/v0.2.0/schema.json#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-workflow/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-workflow/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/catalog#",
    "Feature": "geojson:Feature",
    "geometry": "geojson:geometry",
    "bbox": "geojson:bbox",
    "coordinates": "geojson:coordinates",
    "properties": "geojson:properties",
    "links": {
      "@id": "http://www.w3.org/ns/iana/link-relations/relation",
      "@container": "@set"
    },
    "href": "@id",
    "rel": "http://www.w3.org/ns/iana/link-relations/relation",
    "itemType": "dcterms:type",
    "conformsTo": {
      "@id": "dcterms:conformsTo",
      "@type": "@id",
      "@container": "@set"
    },
    "name": "dcterms:title",
    "keywords": {
      "@id": "dcat:keyword",
      "@container": "@set"
    },
    "themes": {
      "@id": "dcat:theme",
      "@container": "@set"
    },
    "license": {
      "@id": "dcterms:license",
      "@type": "@id"
    },
    "created": {
      "@id": "dcterms:created",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "updated": {
      "@id": "dcterms:modified",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "applicationCategory": "schema:applicationCategory",
    "softwareVersion": "schema:softwareVersion",
    "programmingLanguage": "schema:programmingLanguage",
    "applicationPackage": {
      "@id": "seadots:applicationPackage",
      "@type": "@id"
    },
    "workflow": {
      "@id": "prov:hadPlan",
      "@type": "@id"
    },
    "profileId": {
      "@id": "dcterms:conformsTo",
      "@type": "@id"
    },
    "required": {
      "@id": "seadots:requiredInput",
      "@type": "http://www.w3.org/2001/XMLSchema#boolean"
    },
    "class": "cwl:class",
    "requirements": {
      "@id": "cwl:requirements",
      "@container": "@set"
    },
    "startTime": {
      "@id": "prov:startedAtTime",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "endTime": {
      "@id": "prov:endedAtTime",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "status": "seadots:status",
    "parameters": "seadots:parameters",
    "timeBoundaryStart": {
      "@id": "seadots:timeBoundaryStart",
      "@type": "http://www.w3.org/2001/XMLSchema#date"
    },
    "timeBoundaryEnd": {
      "@id": "seadots:timeBoundaryEnd",
      "@type": "http://www.w3.org/2001/XMLSchema#date"
    },
    "application": {
      "@id": "prov:used",
      "@type": "@id"
    },
    "inputRecords": {
      "@id": "prov:used",
      "@type": "@id",
      "@container": "@set"
    },
    "outputRecords": {
      "@id": "prov:generated",
      "@type": "@id",
      "@container": "@set"
    },
    "agent": {
      "@id": "prov:wasAssociatedWith",
      "@type": "@id"
    },
    "configuration": "seadots:configuration",
    "containerImage": "seadots:containerImage",
    "stac_version": "stac:stac_version",
    "collection": {
      "@id": "dcterms:isPartOf",
      "@type": "@id"
    },
    "datetime": {
      "@id": "dcterms:date",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "convention": "seadots:metadataConvention",
    "cf:parameter": {
      "@id": "cf:parameter",
      "@container": "@set"
    },
    "unit": "dcterms:format",
    "assets": "stac:assets",
    "data": "stac:data",
    "derivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@type": "@id",
      "@container": "@set"
    },
    "role": "seadots:role",
    "mediaType": "dcterms:format",
    "dockerPull": "seadots:dockerPull",
    "id": "@id",
    "type": "@type",
    "title": "dcterms:title",
    "description": "dcterms:description",
    "version": "dcterms:hasVersion",
    "method": "dcterms:method",
    "activity": {
      "@id": "seadots:activity",
      "@type": "@id"
    },
    "inputs": {
      "@id": "apkg:inputs",
      "@container": "@set"
    },
    "outputs": {
      "@id": "apkg:outputs",
      "@container": "@set"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "schema": "https://schema.org/",
    "seadots": "https://w3id.org/ogc/hosted/seadots/catalog#",
    "prov": "http://www.w3.org/ns/prov#",
    "apkg": "https://w3id.org/apkg/terms/",
    "cwl": "https://w3id.org/cwl/cwl#",
    "stac": "https://stacspec.org/vocab#",
    "cf": "https://stac-extensions.github.io/cf/v0.2.0/schema.json#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-workflow/context.jsonld)

## Sources

* [SeaDOTs Interoperability Framework - Catalog Metadata Model](https://github.com/ogcincubator/bblocks-seadots)
* [OGC API - Records](https://docs.ogc.org/is/20-004/20-004.html)
* [OGC bblocks-openscience](https://github.com/ogcincubator/bblocks-openscience)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/catalog-workflow`

