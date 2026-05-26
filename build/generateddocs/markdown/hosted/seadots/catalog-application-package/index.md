
# SeaDOTs Catalog Application Package (Schema)

`ogc.hosted.seadots.catalog-application-package` *v0.1*

Generic APKG/CWL-aligned profile for the executable package attached to a SeaDOTs application record.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# SeaDOTs Catalog Application Package

An application package is the deployable profile of an application. It records the APKG/CWL computational contract: declared inputs, declared outputs, runtime class, requirements, software version, implementation language, and deployment metadata.

## Role in the Catalog Metadata Model

This generic building block supports the SeaDOTs catalog model described in
`data_framework/INTEROPERABILITY.md` under `Catalog Metadata Model` and
`2.2 Provenance model (Open Science)`.

## Source-property coverage gaps

This block is a generic catalog template and is not derived from a raw source
dataset. No source properties are intentionally dropped.

## Examples

### SeaDOTs Catalog Application Package
#### json
```json
{
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/application-package/reef-effect",
  "type": "ApplicationPackage",
  "title": "Reef-effect CWL application package",
  "description": "Minimal APKG/CWL package contract for the reef-effect biomass calculation.",
  "class": "CommandLineTool",
  "inputs": [
    {
      "id": "areaOfInterest",
      "type": "File",
      "description": "GeoJSON Feature describing the AOI."
    },
    {
      "id": "benthicBiomassDensity",
      "type": "File",
      "description": "Input biomass-density STAC Item or OGC Record."
    }
  ],
  "outputs": [
    {
      "id": "reefBiomassOutput",
      "type": "File",
      "description": "STAC/OGC Records output item."
    }
  ],
  "requirements": [
    {
      "class": "DockerRequirement",
      "dockerPull": "ghcr.io/seadots/reef-effect:0.1.0"
    }
  ],
  "softwareVersion": "0.1.0",
  "programmingLanguage": "Python"
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-application-package/context.jsonld",
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/application-package/reef-effect",
  "type": "ApplicationPackage",
  "title": "Reef-effect CWL application package",
  "description": "Minimal APKG/CWL package contract for the reef-effect biomass calculation.",
  "class": "CommandLineTool",
  "inputs": [
    {
      "id": "areaOfInterest",
      "type": "File",
      "description": "GeoJSON Feature describing the AOI."
    },
    {
      "id": "benthicBiomassDensity",
      "type": "File",
      "description": "Input biomass-density STAC Item or OGC Record."
    }
  ],
  "outputs": [
    {
      "id": "reefBiomassOutput",
      "type": "File",
      "description": "STAC/OGC Records output item."
    }
  ],
  "requirements": [
    {
      "class": "DockerRequirement",
      "dockerPull": "ghcr.io/seadots/reef-effect:0.1.0"
    }
  ],
  "softwareVersion": "0.1.0",
  "programmingLanguage": "Python"
}
```

#### ttl
```ttl
@prefix apkg: <https://w3id.org/apkg/terms/> .
@prefix cwl: <https://w3id.org/cwl/cwl#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema: <https://schema.org/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .

<https://w3id.org/ogc/hosted/seadots/catalog/application-package/reef-effect> a seadots:ApplicationPackage ;
    dcterms:description "Minimal APKG/CWL package contract for the reef-effect biomass calculation." ;
    dcterms:title "Reef-effect CWL application package" ;
    schema:programmingLanguage "Python" ;
    schema:softwareVersion "0.1.0" ;
    apkg:inputs <file:///github/workspace/areaOfInterest>,
        <file:///github/workspace/benthicBiomassDensity> ;
    apkg:outputs <file:///github/workspace/reefBiomassOutput> ;
    cwl:class "CommandLineTool" ;
    cwl:requirements [ cwl:class "DockerRequirement" ;
            seadots:dockerPull "ghcr.io/seadots/reef-effect:0.1.0" ] .

<file:///github/workspace/areaOfInterest> a seadots:File ;
    dcterms:description "GeoJSON Feature describing the AOI." .

<file:///github/workspace/benthicBiomassDensity> a seadots:File ;
    dcterms:description "Input biomass-density STAC Item or OGC Record." .

<file:///github/workspace/reefBiomassOutput> a seadots:File ;
    dcterms:description "STAC/OGC Records output item." .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SeaDOTs Catalog Application Package
description: 'APKG/CWL-aligned computational contract for a reusable SeaDOTs application.

  '
type: object
required:
- id
- type
- title
- description
- class
- inputs
- outputs
properties:
  id:
    type: string
    format: uri
    x-jsonld-id: '@id'
  type:
    const: ApplicationPackage
    x-jsonld-id: '@type'
  title:
    type: string
    x-jsonld-id: http://purl.org/dc/terms/title
  description:
    type: string
    x-jsonld-id: http://purl.org/dc/terms/description
  class:
    type: string
    x-jsonld-id: https://w3id.org/cwl/cwl#class
  inputs:
    type: array
    items:
      type: object
      required:
      - id
      - type
      properties:
        id:
          type: string
          x-jsonld-id: '@id'
        type:
          type: string
          x-jsonld-id: '@type'
        description:
          type: string
          x-jsonld-id: http://purl.org/dc/terms/description
    x-jsonld-id: https://w3id.org/apkg/terms/inputs
    x-jsonld-container: '@set'
  outputs:
    type: array
    items:
      type: object
      required:
      - id
      - type
      properties:
        id:
          type: string
          x-jsonld-id: '@id'
        type:
          type: string
          x-jsonld-id: '@type'
        description:
          type: string
          x-jsonld-id: http://purl.org/dc/terms/description
    x-jsonld-id: https://w3id.org/apkg/terms/outputs
    x-jsonld-container: '@set'
  requirements:
    type: array
    items:
      type: object
    x-jsonld-id: https://w3id.org/cwl/cwl#requirements
    x-jsonld-container: '@set'
  softwareVersion:
    type: string
    x-jsonld-id: https://schema.org/softwareVersion
  programmingLanguage:
    type: string
    x-jsonld-id: https://schema.org/programmingLanguage
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
  version: http://purl.org/dc/terms/hasVersion
  method: http://purl.org/dc/terms/method
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
  activity:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#activity
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

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-application-package/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-application-package/schema.yaml)


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
    "version": "dcterms:hasVersion",
    "method": "dcterms:method",
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
    "activity": {
      "@id": "seadots:activity",
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
    "class": "cwl:class",
    "inputs": {
      "@id": "apkg:inputs",
      "@container": "@set"
    },
    "outputs": {
      "@id": "apkg:outputs",
      "@container": "@set"
    },
    "requirements": {
      "@id": "cwl:requirements",
      "@container": "@set"
    },
    "softwareVersion": "schema:softwareVersion",
    "programmingLanguage": "schema:programmingLanguage",
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
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-application-package/context.jsonld)

## Sources

* [SeaDOTs Interoperability Framework - Catalog Metadata Model](https://github.com/ogcincubator/bblocks-seadots)
* [OGC API - Records](https://docs.ogc.org/is/20-004/20-004.html)
* [OGC bblocks-openscience](https://github.com/ogcincubator/bblocks-openscience)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/catalog-application-package`

