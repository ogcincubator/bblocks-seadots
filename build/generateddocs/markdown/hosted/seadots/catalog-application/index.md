
# SeaDOTs Catalog Application (Schema)

`ogc.hosted.seadots.catalog-application` *v0.1*

Generic OGC API Records profile for a discoverable SeaDOTs Application: a digital twin application, workflow, transformer, model, or processing service.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# SeaDOTs Catalog Application

A reusable application record is the discovery entry point for a SeaDOTs digital twin application, model, workflow, transformer, or processing service. The record is an OGC API Records Feature and may link to an APKG/CWL application package and a PROV-O workflow plan.

## Role in the Catalog Metadata Model

This generic building block supports the SeaDOTs catalog model described in
`data_framework/INTEROPERABILITY.md` under `Catalog Metadata Model` and
`2.2 Provenance model (Open Science)`.

## Source-property coverage gaps

This block is a generic catalog template and is not derived from a raw source
dataset. No source properties are intentionally dropped.

## Examples

### SeaDOTs Catalog Application
#### json
```json
{
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/application/reef-effect",
  "type": "Feature",
  "itemType": "record",
  "conformsTo": [
    "https://docs.ogc.org/is/20-004/20-004.html"
  ],
  "geometry": null,
  "bbox": [

  ],
  "properties": {
    "title": "Utsira reef-effect biomass application",
    "description": "Reusable application record for estimating reef-associated biomass around floating wind infrastructure.",
    "type": "Application",
    "applicationCategory": "DigitalTwinApplication",
    "softwareVersion": "0.1.0",
    "programmingLanguage": "Python",
    "applicationPackage": "https://w3id.org/ogc/hosted/seadots/catalog/application-package/reef-effect",
    "workflow": "https://w3id.org/ogc/hosted/seadots/catalog/workflow/reef-effect",
    "inputs": [
      {
        "profileId": "ogc.hosted.seadots.catalog-input",
        "required": true,
        "role": "catalog-input",
        "description": "Generic STAC input item accepted by this application."
      },
      {
        "profileId": "ogc.hosted.seadots.area-of-interest",
        "required": true,
        "role": "area-of-interest",
        "description": "GeoJSON Feature defining the spatial area for the calculation."
      },
      {
        "profileId": "ogc.hosted.seadots.benthic-biomass-density-mareano",
        "required": false,
        "role": "benthic-biomass-density",
        "description": "Optional baseline benthic biomass-density input profile."
      }
    ],
    "outputs": [
      {
        "profileId": "ogc.hosted.seadots.catalog-output",
        "required": true,
        "role": "catalog-output",
        "description": "Generic STAC output item produced by this application."
      },
      {
        "profileId": "ogc.hosted.seadots.reef-effect-output",
        "required": true,
        "role": "reef-biomass-result",
        "description": "Structured reef-effect biomass output record."
      }
    ],
    "keywords": [
      "open-science",
      "digital-twin",
      "offshore-wind"
    ],
    "license": "https://creativecommons.org/licenses/by/4.0/"
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-application",
      "type": "application/schema+json"
    },
    {
      "rel": "application-package",
      "href": "https://w3id.org/ogc/hosted/seadots/catalog/application-package/reef-effect",
      "type": "application/json"
    },
    {
      "rel": "workflow",
      "href": "https://w3id.org/ogc/hosted/seadots/catalog/workflow/reef-effect",
      "type": "application/json"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-application/context.jsonld",
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/application/reef-effect",
  "type": "Feature",
  "itemType": "record",
  "conformsTo": [
    "https://docs.ogc.org/is/20-004/20-004.html"
  ],
  "geometry": null,
  "bbox": [],
  "properties": {
    "title": "Utsira reef-effect biomass application",
    "description": "Reusable application record for estimating reef-associated biomass around floating wind infrastructure.",
    "type": "Application",
    "applicationCategory": "DigitalTwinApplication",
    "softwareVersion": "0.1.0",
    "programmingLanguage": "Python",
    "applicationPackage": "https://w3id.org/ogc/hosted/seadots/catalog/application-package/reef-effect",
    "workflow": "https://w3id.org/ogc/hosted/seadots/catalog/workflow/reef-effect",
    "inputs": [
      {
        "profileId": "ogc.hosted.seadots.catalog-input",
        "required": true,
        "role": "catalog-input",
        "description": "Generic STAC input item accepted by this application."
      },
      {
        "profileId": "ogc.hosted.seadots.area-of-interest",
        "required": true,
        "role": "area-of-interest",
        "description": "GeoJSON Feature defining the spatial area for the calculation."
      },
      {
        "profileId": "ogc.hosted.seadots.benthic-biomass-density-mareano",
        "required": false,
        "role": "benthic-biomass-density",
        "description": "Optional baseline benthic biomass-density input profile."
      }
    ],
    "outputs": [
      {
        "profileId": "ogc.hosted.seadots.catalog-output",
        "required": true,
        "role": "catalog-output",
        "description": "Generic STAC output item produced by this application."
      },
      {
        "profileId": "ogc.hosted.seadots.reef-effect-output",
        "required": true,
        "role": "reef-biomass-result",
        "description": "Structured reef-effect biomass output record."
      }
    ],
    "keywords": [
      "open-science",
      "digital-twin",
      "offshore-wind"
    ],
    "license": "https://creativecommons.org/licenses/by/4.0/"
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-application",
      "type": "application/schema+json"
    },
    {
      "rel": "application-package",
      "href": "https://w3id.org/ogc/hosted/seadots/catalog/application-package/reef-effect",
      "type": "application/json"
    },
    {
      "rel": "workflow",
      "href": "https://w3id.org/ogc/hosted/seadots/catalog/workflow/reef-effect",
      "type": "application/json"
    }
  ]
}
```

#### ttl
```ttl
@prefix apkg: <https://w3id.org/apkg/terms/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.w3.org/ns/iana/link-relations/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/ogc/hosted/seadots/catalog/application/reef-effect> a geojson:Feature ;
    dcterms:conformsTo <https://docs.ogc.org/is/20-004/20-004.html> ;
    dcterms:type "record" ;
    ns1:relation <bblocks://ogc.hosted.seadots.catalog-application>,
        <https://w3id.org/ogc/hosted/seadots/catalog/application-package/reef-effect>,
        <https://w3id.org/ogc/hosted/seadots/catalog/workflow/reef-effect> ;
    geojson:bbox () ;
    geojson:properties [ a seadots:Application ;
            dcterms:description "Reusable application record for estimating reef-associated biomass around floating wind infrastructure." ;
            dcterms:license <https://creativecommons.org/licenses/by/4.0/> ;
            dcterms:title "Utsira reef-effect biomass application" ;
            dcat:keyword "digital-twin",
                "offshore-wind",
                "open-science" ;
            prov:hadPlan <https://w3id.org/ogc/hosted/seadots/catalog/workflow/reef-effect> ;
            schema:applicationCategory "DigitalTwinApplication" ;
            schema:programmingLanguage "Python" ;
            schema:softwareVersion "0.1.0" ;
            apkg:inputs [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.catalog-input> ;
                    dcterms:description "Generic STAC input item accepted by this application." ;
                    seadots:requiredInput true ;
                    seadots:role "catalog-input" ],
                [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.area-of-interest> ;
                    dcterms:description "GeoJSON Feature defining the spatial area for the calculation." ;
                    seadots:requiredInput true ;
                    seadots:role "area-of-interest" ],
                [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.benthic-biomass-density-mareano> ;
                    dcterms:description "Optional baseline benthic biomass-density input profile." ;
                    seadots:requiredInput false ;
                    seadots:role "benthic-biomass-density" ] ;
            apkg:outputs [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.reef-effect-output> ;
                    dcterms:description "Structured reef-effect biomass output record." ;
                    seadots:requiredInput true ;
                    seadots:role "reef-biomass-result" ],
                [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.catalog-output> ;
                    dcterms:description "Generic STAC output item produced by this application." ;
                    seadots:requiredInput true ;
                    seadots:role "catalog-output" ] ;
            seadots:applicationPackage <https://w3id.org/ogc/hosted/seadots/catalog/application-package/reef-effect> ] .

<bblocks://ogc.hosted.seadots.catalog-application> a <https://w3id.org/ogc/hosted/seadots/catalog#application/schema+json> ;
    ns1:relation "describedby" .

<https://w3id.org/ogc/hosted/seadots/catalog/application-package/reef-effect> a <https://w3id.org/ogc/hosted/seadots/catalog#application/json> ;
    ns1:relation "application-package" .

<https://w3id.org/ogc/hosted/seadots/catalog/workflow/reef-effect> a <https://w3id.org/ogc/hosted/seadots/catalog#application/json> ;
    ns1:relation "workflow" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SeaDOTs Catalog Application
description: 'OGC API Records profile for a reusable application, workflow, model,
  transformer, or process.

  '
allOf:
- $ref: https://ogcincubator.github.io/geodcat-ogcapi-records/build/annotated/geo/geodcat/geodcat-records/schema.yaml
type: object
required:
- id
- type
- itemType
- properties
properties:
  id:
    type: string
    x-jsonld-id: '@id'
  type:
    const: Feature
    x-jsonld-id: '@type'
  itemType:
    const: record
    x-jsonld-id: http://purl.org/dc/terms/type
  conformsTo:
    type: array
    items:
      type: string
      format: uri
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
    x-jsonld-container: '@set'
  geometry:
    type:
    - object
    - 'null'
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
  bbox:
    type: array
    items:
      type: number
    x-jsonld-id: https://purl.org/geojson/vocab#bbox
  properties:
    type: object
    required:
    - title
    - description
    - type
    - applicationCategory
    properties:
      title:
        type: string
        x-jsonld-id: http://purl.org/dc/terms/title
      description:
        type: string
        x-jsonld-id: http://purl.org/dc/terms/description
      type:
        const: Application
        x-jsonld-id: '@type'
      applicationCategory:
        type: string
        enum:
        - DigitalTwinApplication
        - Workflow
        - Transform
        - Model
        - Service
        x-jsonld-id: https://schema.org/applicationCategory
      softwareVersion:
        type: string
        x-jsonld-id: https://schema.org/softwareVersion
      programmingLanguage:
        type: string
        x-jsonld-id: https://schema.org/programmingLanguage
      applicationPackage:
        type: string
        format: uri
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#applicationPackage
        x-jsonld-type: '@id'
      workflow:
        type: string
        format: uri
        x-jsonld-id: http://www.w3.org/ns/prov#hadPlan
        x-jsonld-type: '@id'
      inputs:
        type: array
        description: Input profiles accepted by this application.
        items:
          type: object
          required:
          - profileId
          - required
          properties:
            profileId:
              type: string
              description: URI or fully qualified building block identifier of the
                accepted input profile.
              x-jsonld-id: http://purl.org/dc/terms/conformsTo
              x-jsonld-type: '@id'
            required:
              type: boolean
              description: Whether this input profile is required to execute the application.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#requiredInput
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
            role:
              type: string
              description: Application-specific input role.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#role
            description:
              type: string
              x-jsonld-id: http://purl.org/dc/terms/description
        x-jsonld-id: https://w3id.org/apkg/terms/inputs
        x-jsonld-container: '@set'
      outputs:
        type: array
        description: Output profiles produced by this application.
        items:
          type: object
          required:
          - profileId
          - required
          properties:
            profileId:
              type: string
              description: URI or fully qualified building block identifier of the
                produced output profile.
              x-jsonld-id: http://purl.org/dc/terms/conformsTo
              x-jsonld-type: '@id'
            required:
              type: boolean
              description: Whether this output profile is always produced by the application.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#requiredInput
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
            role:
              type: string
              description: Application-specific output role.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#role
            description:
              type: string
              x-jsonld-id: http://purl.org/dc/terms/description
        x-jsonld-id: https://w3id.org/apkg/terms/outputs
        x-jsonld-container: '@set'
      keywords:
        type: array
        items:
          type: string
        x-jsonld-id: http://www.w3.org/ns/dcat#keyword
        x-jsonld-container: '@set'
      license:
        type: string
        format: uri
        x-jsonld-id: http://purl.org/dc/terms/license
        x-jsonld-type: '@id'
    additionalProperties: true
    x-jsonld-id: https://purl.org/geojson/vocab#properties
  links:
    type: array
    items:
      type: object
      required:
      - rel
      - href
      properties:
        rel:
          type: string
          x-jsonld-id: http://www.w3.org/ns/iana/link-relations/relation
        href:
          type: string
          x-jsonld-id: '@id'
        type:
          type: string
          x-jsonld-id: '@type'
        title:
          type: string
          x-jsonld-id: http://purl.org/dc/terms/title
    x-jsonld-id: http://www.w3.org/ns/iana/link-relations/relation
    x-jsonld-container: '@set'
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
  coordinates: https://purl.org/geojson/vocab#coordinates
  name: http://purl.org/dc/terms/title
  themes:
    x-jsonld-id: http://www.w3.org/ns/dcat#theme
    x-jsonld-container: '@set'
  created:
    x-jsonld-id: http://purl.org/dc/terms/created
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  updated:
    x-jsonld-id: http://purl.org/dc/terms/modified
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  class: https://w3id.org/cwl/cwl#class
  requirements:
    x-jsonld-id: https://w3id.org/cwl/cwl#requirements
    x-jsonld-container: '@set'
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

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-application/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-application/schema.yaml)


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
    "type": "@type",
    "id": "@id",
    "properties": {
      "@context": {
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
        "inputs": {
          "@context": {
            "profileId": {
              "@id": "dct:conformsTo",
              "@type": "@id"
            },
            "required": {
              "@id": "seadots:requiredInput",
              "@type": "xsd:boolean"
            },
            "role": "seadots:role"
          },
          "@id": "apkg:inputs",
          "@container": "@set"
        },
        "outputs": {
          "@context": {
            "profileId": {
              "@id": "dct:conformsTo",
              "@type": "@id"
            },
            "required": {
              "@id": "seadots:requiredInput",
              "@type": "xsd:boolean"
            },
            "role": "seadots:role"
          },
          "@id": "apkg:outputs",
          "@container": "@set"
        },
        "license": {
          "@id": "dct:license",
          "@type": "@id"
        }
      },
      "@id": "geojson:properties"
    },
    "geometry": {
      "@context": {
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
        "rel": "http://www.w3.org/ns/iana/link-relations/relation",
        "href": "@id"
      },
      "@id": "http://www.w3.org/ns/iana/link-relations/relation",
      "@container": "@set"
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
      "@id": "dcat:keyword"
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
      "@id": "rec:themes",
      "@context": {
        "concepts": {
          "@id": "rec:concept",
          "@context": {
            "id": {
              "@type": "xsd:string",
              "@id": "rec:conceptID"
            },
            "url": {
              "@type": "@id",
              "@id": "dcat:theme"
            }
          }
        },
        "scheme": "rec:scheme"
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
    "coordinates": "geojson:coordinates",
    "name": "dct:title",
    "class": "cwl:class",
    "requirements": {
      "@id": "cwl:requirements",
      "@container": "@set"
    },
    "version": "dct:hasVersion",
    "method": "dct:method",
    "startTime": {
      "@id": "prov:startedAtTime",
      "@type": "xsd:dateTime"
    },
    "endTime": {
      "@id": "prov:endedAtTime",
      "@type": "xsd:dateTime"
    },
    "status": "seadots:status",
    "parameters": "seadots:parameters",
    "timeBoundaryStart": {
      "@id": "seadots:timeBoundaryStart",
      "@type": "xsd:date"
    },
    "timeBoundaryEnd": {
      "@id": "seadots:timeBoundaryEnd",
      "@type": "xsd:date"
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
      "@id": "dct:isPartOf",
      "@type": "@id"
    },
    "datetime": {
      "@id": "dct:date",
      "@type": "xsd:dateTime"
    },
    "convention": "seadots:metadataConvention",
    "cf:parameter": {
      "@id": "cf:parameter",
      "@container": "@set"
    },
    "unit": "dct:format",
    "assets": "stac:assets",
    "data": "stac:data",
    "derivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@type": "@id",
      "@container": "@set"
    },
    "mediaType": "dct:format",
    "dockerPull": "seadots:dockerPull",
    "itemType": "dct:type",
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
    "dcterms": "http://purl.org/dc/terms/",
    "schema": "https://schema.org/",
    "seadots": "https://w3id.org/ogc/hosted/seadots/catalog#",
    "apkg": "https://w3id.org/apkg/terms/",
    "cwl": "https://w3id.org/cwl/cwl#",
    "stac": "https://stacspec.org/vocab#",
    "cf": "https://stac-extensions.github.io/cf/v0.2.0/schema.json#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-application/context.jsonld)

## Sources

* [SeaDOTs Interoperability Framework - Catalog Metadata Model](https://github.com/ogcincubator/bblocks-seadots)
* [OGC API - Records](https://docs.ogc.org/is/20-004/20-004.html)
* [OGC bblocks-openscience](https://github.com/ogcincubator/bblocks-openscience)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/catalog-application`

