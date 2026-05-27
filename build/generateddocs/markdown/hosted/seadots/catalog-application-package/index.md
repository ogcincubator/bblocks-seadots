
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
  "id": "reef-effect",
  "type": "ApplicationPackage",
  "title": "Reef-effect CWL application package",
  "description": "Minimal APKG/CWL package contract for the reef-effect biomass calculation.",
  "cwlVersion": "v1.2",
  "class": "CommandLineTool",
  "baseCommand": "reef-effect",
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
  "id": "reef-effect",
  "type": "ApplicationPackage",
  "title": "Reef-effect CWL application package",
  "description": "Minimal APKG/CWL package contract for the reef-effect biomass calculation.",
  "cwlVersion": "v1.2",
  "class": "CommandLineTool",
  "baseCommand": "reef-effect",
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

<file:///github/workspace/reef-effect> a apkg:ApplicationPackage ;
    dcterms:description "Minimal APKG/CWL package contract for the reef-effect biomass calculation." ;
    dcterms:title "Reef-effect CWL application package" ;
    schema:programmingLanguage "Python" ;
    schema:softwareVersion "0.1.0" ;
    apkg:inputs <file:///github/workspace/areaOfInterest>,
        <file:///github/workspace/benthicBiomassDensity> ;
    apkg:outputs <file:///github/workspace/reefBiomassOutput> ;
    cwl:class "CommandLineTool" ;
    cwl:requirements [ cwl:class "DockerRequirement" ;
            seadots:dockerPull "ghcr.io/seadots/reef-effect:0.1.0" ] ;
    seadots:baseCommand "reef-effect" ;
    seadots:cwlVersion "v1.2" .

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
allOf:
- $ref: https://ogcincubator.github.io/bblocks-openscience/build/annotated/osc/application-package/schema.yaml
type: object
properties:
  type:
    const: ApplicationPackage
    x-jsonld-id: '@type'
  softwareVersion:
    type: string
    x-jsonld-id: https://schema.org/softwareVersion
  programmingLanguage:
    type: string
    x-jsonld-id: https://schema.org/programmingLanguage
additionalProperties: true
x-jsonld-extra-terms:
  id: '@id'
  ApplicationPackage: https://w3id.org/apkg/terms/ApplicationPackage
  title: http://purl.org/dc/terms/title
  description: http://purl.org/dc/terms/description
  class: https://w3id.org/cwl/cwl#class
  inputs:
    x-jsonld-id: https://w3id.org/apkg/terms/inputs
    x-jsonld-container: '@set'
  outputs:
    x-jsonld-id: https://w3id.org/apkg/terms/outputs
    x-jsonld-container: '@set'
  requirements:
    x-jsonld-id: https://w3id.org/cwl/cwl#requirements
    x-jsonld-container: '@set'
  dockerPull: https://w3id.org/ogc/hosted/seadots/catalog#dockerPull
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/catalog#
x-jsonld-prefixes:
  apkg: https://w3id.org/apkg/terms/
  dcterms: http://purl.org/dc/terms/
  cwl: https://w3id.org/cwl/cwl#
  schema: https://schema.org/
  seadots: https://w3id.org/ogc/hosted/seadots/catalog#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-application-package/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-application-package/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/catalog#",
    "id": "@id",
    "ApplicationPackage": "apkg:ApplicationPackage",
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
    "dockerPull": "seadots:dockerPull",
    "type": "@type",
    "softwareVersion": "schema:softwareVersion",
    "programmingLanguage": "schema:programmingLanguage",
    "apkg": "https://w3id.org/apkg/terms/",
    "dcterms": "http://purl.org/dc/terms/",
    "cwl": "https://w3id.org/cwl/cwl#",
    "schema": "https://schema.org/",
    "seadots": "https://w3id.org/ogc/hosted/seadots/catalog#",
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

