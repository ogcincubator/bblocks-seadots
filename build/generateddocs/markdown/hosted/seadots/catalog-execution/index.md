
# SeaDOTs Catalog Execution (Schema)

`ogc.hosted.seadots.catalog-execution` *v0.1*

Generic OGC API Records and PROV-O profile for one concrete execution, experiment run, or digital twin run represented as links to catalog application, workflow, input, and output records.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# SeaDOTs Catalog Execution

An execution is one concrete experiment run: an instance of the same reusable workflow that links to the catalog application, workflow, input records, and output records using OGC API Records and PROV-O relations.

The execution record is intentionally light. It avoids repeating descriptive
metadata that belongs in the linked records, so a run can be represented by its
identifier and relative references that work in local checkouts and published
registers.

## Role in the Catalog Metadata Model

This generic building block supports the SeaDOTs catalog model described in
`data_framework/INTEROPERABILITY.md` under `Catalog Metadata Model` and
`2.2 Provenance model (Open Science)`.

## Source-property coverage gaps

This block is a generic catalog template and is not derived from a raw source
dataset. No source properties are intentionally dropped.

## Examples

### SeaDOTs Catalog Execution
#### json
```json
{
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/execution/reef-effect-run-001",
  "type": "Feature",
  "itemType": "record",
  "conformsTo": [
    "https://docs.ogc.org/is/20-004/20-004.html",
    "http://www.w3.org/TR/prov-o/"
  ],
  "geometry": null,
  "properties": {
    "type": "Execution",
    "application": "../../catalog-application/examples/application-record.json",
    "workflow": "../../catalog-workflow/examples/workflow.json",
    "inputRecords": [
      "../../catalog-input/examples/input-stac-item.json"
    ],
    "outputRecords": [
      "../../catalog-output/examples/output-stac-item.json"
    ]
  },
  "links": [
    {
      "rel": "related",
      "href": "../../catalog-application/examples/application-record.json",
      "type": "application/geo+json"
    },
    {
      "rel": "related",
      "href": "../../catalog-workflow/examples/workflow.json",
      "type": "application/geo+json"
    },
    {
      "rel": "related",
      "href": "../../catalog-input/examples/input-stac-item.json",
      "type": "application/geo+json"
    },
    {
      "rel": "related",
      "href": "../../catalog-output/examples/output-stac-item.json",
      "type": "application/geo+json"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-execution/context.jsonld",
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/execution/reef-effect-run-001",
  "type": "Feature",
  "itemType": "record",
  "conformsTo": [
    "https://docs.ogc.org/is/20-004/20-004.html",
    "http://www.w3.org/TR/prov-o/"
  ],
  "geometry": null,
  "properties": {
    "type": "Execution",
    "application": "../../catalog-application/examples/application-record.json",
    "workflow": "../../catalog-workflow/examples/workflow.json",
    "inputRecords": [
      "../../catalog-input/examples/input-stac-item.json"
    ],
    "outputRecords": [
      "../../catalog-output/examples/output-stac-item.json"
    ]
  },
  "links": [
    {
      "rel": "related",
      "href": "../../catalog-application/examples/application-record.json",
      "type": "application/geo+json"
    },
    {
      "rel": "related",
      "href": "../../catalog-workflow/examples/workflow.json",
      "type": "application/geo+json"
    },
    {
      "rel": "related",
      "href": "../../catalog-input/examples/input-stac-item.json",
      "type": "application/geo+json"
    },
    {
      "rel": "related",
      "href": "../../catalog-output/examples/output-stac-item.json",
      "type": "application/geo+json"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.w3.org/ns/iana/link-relations/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .

<https://w3id.org/ogc/hosted/seadots/catalog/execution/reef-effect-run-001> a geojson:Feature ;
    dcterms:conformsTo <http://www.w3.org/TR/prov-o/>,
        <https://docs.ogc.org/is/20-004/20-004.html> ;
    dcterms:type "record" ;
    ns1:relation <file:///catalog-application/examples/application-record.json>,
        <file:///catalog-input/examples/input-stac-item.json>,
        <file:///catalog-output/examples/output-stac-item.json>,
        <file:///catalog-workflow/examples/workflow.json> ;
    geojson:properties [ a seadots:Execution ;
            prov:generated <file:///catalog-output/examples/output-stac-item.json> ;
            prov:hadPlan <file:///catalog-workflow/examples/workflow.json> ;
            prov:used <file:///catalog-application/examples/application-record.json>,
                <file:///catalog-input/examples/input-stac-item.json> ] .

<file:///catalog-application/examples/application-record.json> a <https://w3id.org/ogc/hosted/seadots/catalog#application/geo+json> ;
    ns1:relation "related" .

<file:///catalog-input/examples/input-stac-item.json> a <https://w3id.org/ogc/hosted/seadots/catalog#application/geo+json> ;
    ns1:relation "related" .

<file:///catalog-output/examples/output-stac-item.json> a <https://w3id.org/ogc/hosted/seadots/catalog#application/geo+json> ;
    ns1:relation "related" .

<file:///catalog-workflow/examples/workflow.json> a <https://w3id.org/ogc/hosted/seadots/catalog#application/geo+json> ;
    ns1:relation "related" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SeaDOTs Catalog Execution
description: 'OGC API Records profile for a concrete workflow execution or experiment
  run that links to reusable catalog records instead of duplicating their metadata.

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
    - type
    - workflow
    - application
    - inputRecords
    - outputRecords
    properties:
      type:
        const: Execution
        x-jsonld-id: '@type'
      application:
        type: string
        format: uri-reference
        description: Relative or absolute reference to the catalog application record.
        x-jsonld-id: http://www.w3.org/ns/prov#used
        x-jsonld-type: '@id'
      workflow:
        type: string
        format: uri-reference
        description: Relative or absolute reference to the workflow plan record instantiated
          by this execution.
        x-jsonld-id: http://www.w3.org/ns/prov#hadPlan
        x-jsonld-type: '@id'
      startTime:
        type: string
        format: date-time
        x-jsonld-id: http://www.w3.org/ns/prov#startedAtTime
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
      endTime:
        type: string
        format: date-time
        x-jsonld-id: http://www.w3.org/ns/prov#endedAtTime
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
      status:
        type: string
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#status
      parameters:
        type: object
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#parameters
      inputRecords:
        type: array
        minItems: 1
        items:
          type: string
          format: uri-reference
        x-jsonld-id: http://www.w3.org/ns/prov#used
        x-jsonld-type: '@id'
        x-jsonld-container: '@set'
      outputRecords:
        type: array
        minItems: 1
        items:
          type: string
          format: uri-reference
        x-jsonld-id: http://www.w3.org/ns/prov#generated
        x-jsonld-type: '@id'
        x-jsonld-container: '@set'
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
          format: uri-reference
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
  description: http://purl.org/dc/terms/description
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
  inputs:
    x-jsonld-id: https://w3id.org/apkg/terms/inputs
    x-jsonld-container: '@set'
  outputs:
    x-jsonld-id: https://w3id.org/apkg/terms/outputs
    x-jsonld-container: '@set'
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
  version: http://purl.org/dc/terms/hasVersion
  method: http://purl.org/dc/terms/method
  timeBoundaryStart:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#timeBoundaryStart
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
  timeBoundaryEnd:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#timeBoundaryEnd
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
  activity:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#activity
    x-jsonld-type: '@id'
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

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-execution/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-execution/schema.yaml)


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
        "application": {
          "@id": "prov:used",
          "@type": "@id"
        },
        "workflow": {
          "@id": "prov:hadPlan",
          "@type": "@id"
        },
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
        "inputRecords": {
          "@id": "prov:used",
          "@type": "@id",
          "@container": "@set"
        },
        "outputRecords": {
          "@id": "prov:generated",
          "@type": "@id",
          "@container": "@set"
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
    "applicationCategory": "schema:applicationCategory",
    "softwareVersion": "schema:softwareVersion",
    "programmingLanguage": "schema:programmingLanguage",
    "applicationPackage": {
      "@id": "seadots:applicationPackage",
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
    "profileId": {
      "@id": "dct:conformsTo",
      "@type": "@id"
    },
    "required": {
      "@id": "seadots:requiredInput",
      "@type": "xsd:boolean"
    },
    "class": "cwl:class",
    "requirements": {
      "@id": "cwl:requirements",
      "@container": "@set"
    },
    "version": "dct:hasVersion",
    "method": "dct:method",
    "timeBoundaryStart": {
      "@id": "seadots:timeBoundaryStart",
      "@type": "xsd:date"
    },
    "timeBoundaryEnd": {
      "@id": "seadots:timeBoundaryEnd",
      "@type": "xsd:date"
    },
    "activity": {
      "@id": "seadots:activity",
      "@type": "@id"
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
    "role": "seadots:role",
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
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-execution/context.jsonld)

## Sources

* [SeaDOTs Interoperability Framework - Catalog Metadata Model](https://github.com/ogcincubator/bblocks-seadots)
* [OGC API - Records](https://docs.ogc.org/is/20-004/20-004.html)
* [OGC bblocks-openscience](https://github.com/ogcincubator/bblocks-openscience)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/catalog-execution`

