
# SeaDOTs Catalog Data Tabular Survey (Schema)

`ogc.hosted.seadots.catalog-data-tabular-survey` *v0.1*

Tabular survey-data profile for the saltmarsh perceptions questionnaire, designed to carry ELSST thesaurus mappings, CESSDA controlled-vocabulary references, and DDI-style descriptive metadata for questionnaire variables and response categories.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# SeaDOTs Catalog Data Tabular Survey

This profile is intended for survey-style tabular datasets such as the Norwegian saltmarsh perceptions workbook. It extends the SeaDOTs tabular catalog profile with survey-specific metadata for questionnaire variables, controlled-vocabulary links, and DDI-style variable descriptions.

## Why this is tabular rather than generic

The source is a rectangular questionnaire export with repeated response columns and coded categories. That makes it a good fit for the tabular catalog profile, because the data asset is still a table with rows and columns, even though the metadata is richer than a generic data record. The richer semantics are captured here without forcing the entire dataset into a generic catalog record.

## Semantic hooks

- ELSST: use the `survey:conceptUri` and `survey:controlledVocabulary` fields to reference thesaurus concepts for environmental and social-science terms.
- CESSDA: use `survey:controlledVocabulary` with a `scheme` and `uri` to point at controlled vocabularies used by survey instruments.
- DDI: use `survey:variableMetadata[].ddi:variableDescription` and `survey:studyDescription` to preserve questionnaire and variable-level documentation.

## Recommended usage

Use this block when the data asset is an Excel/CSV/Parquet survey export and you need to describe questionnaire variables and their controlled-vocabulary mappings in the catalog record.

## Examples

### SeaDOTs catalog data tabular survey example
#### json
```json
{
  "id": "saltmarsh-perceptions-norway",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/table/v1.2.0/schema.json",
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json"
  ],
  "properties": {
    "title": "Saltmarsh perceptions survey (Norway)",
    "description": "Questionnaire export describing public perceptions of saltmarsh management and coastal ecosystem services.",
    "datetime": "2024-03-01T00:00:00Z",
    "role": "data",
    "license": "CC BY-NC-SA 4.0",
    "table:columns": [
      {
        "name": "caseid",
        "type": "string",
        "description": "Respondent identifier"
      },
      {
        "name": "Country",
        "type": "string",
        "description": "Country of residence"
      },
      {
        "name": "Q1",
        "type": "string",
        "description": "Respondent age group"
      },
      {
        "name": "Q2",
        "type": "string",
        "description": "Respondent gender"
      }
    ],
    "table:primary_geometry": "none",
    "table:row_count": 5046,
    "survey:studyTitle": "Saltmarsh perceptions survey",
    "survey:studyDescription": "Monadic survey on attitudes toward saltmarsh management in Norway.",
    "survey:variableMetadata": [
      {
        "variableName": "Q1",
        "label": "Age group",
        "questionText": "What is your age group?",
        "conceptUri": "https://elsst.uk/terms/age",
        "vocabularyUri": "https://www.cessda.eu/cessda-vocabularies#age",
        "ddi:variableDescription": "Age group of the respondent"
      },
      {
        "variableName": "Q5_1",
        "label": "Environmental concern",
        "questionText": "How important is the protection of the environment to you?",
        "conceptUri": "https://elsst.uk/terms/environmental-concern",
        "vocabularyUri": "https://www.cessda.eu/cessda-vocabularies#environmental-attitudes",
        "ddi:variableDescription": "Likert-style attitude question"
      }
    ],
    "survey:controlledVocabulary": [
      {
        "scheme": "ELSST",
        "uri": "https://elsst.uk/",
        "label": "European Language Social Science Thesaurus"
      },
      {
        "scheme": "CESSDA",
        "uri": "https://www.cessda.eu/",
        "label": "CESSDA controlled vocabularies"
      }
    ]
  },
  "assets": {
    "data": {
      "href": "https://gitlab.sintef.no/Lara.Veylit/saltmarsh_perceptions/-/tree/master/data/processed?ref_type=heads",
      "type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "title": "Norway monadic survey workbook"
    }
  },
  "links": [
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.seadots.catalog-data-tabular-survey",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data Tabular Survey"
    },
    {
      "rel": "describedby",
      "href": "https://www.sciencedirect.com/science/article/pii/S0964569124000942",
      "type": "text/html",
      "title": "Do citizens value climate change mitigation over biodiversity protection? Exploring citizen support for salt marsh management"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data-tabular-survey/context.jsonld",
  "id": "saltmarsh-perceptions-norway",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/table/v1.2.0/schema.json",
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json"
  ],
  "properties": {
    "title": "Saltmarsh perceptions survey (Norway)",
    "description": "Questionnaire export describing public perceptions of saltmarsh management and coastal ecosystem services.",
    "datetime": "2024-03-01T00:00:00Z",
    "role": "data",
    "license": "CC BY-NC-SA 4.0",
    "table:columns": [
      {
        "name": "caseid",
        "type": "string",
        "description": "Respondent identifier"
      },
      {
        "name": "Country",
        "type": "string",
        "description": "Country of residence"
      },
      {
        "name": "Q1",
        "type": "string",
        "description": "Respondent age group"
      },
      {
        "name": "Q2",
        "type": "string",
        "description": "Respondent gender"
      }
    ],
    "table:primary_geometry": "none",
    "table:row_count": 5046,
    "survey:studyTitle": "Saltmarsh perceptions survey",
    "survey:studyDescription": "Monadic survey on attitudes toward saltmarsh management in Norway.",
    "survey:variableMetadata": [
      {
        "variableName": "Q1",
        "label": "Age group",
        "questionText": "What is your age group?",
        "conceptUri": "https://elsst.uk/terms/age",
        "vocabularyUri": "https://www.cessda.eu/cessda-vocabularies#age",
        "ddi:variableDescription": "Age group of the respondent"
      },
      {
        "variableName": "Q5_1",
        "label": "Environmental concern",
        "questionText": "How important is the protection of the environment to you?",
        "conceptUri": "https://elsst.uk/terms/environmental-concern",
        "vocabularyUri": "https://www.cessda.eu/cessda-vocabularies#environmental-attitudes",
        "ddi:variableDescription": "Likert-style attitude question"
      }
    ],
    "survey:controlledVocabulary": [
      {
        "scheme": "ELSST",
        "uri": "https://elsst.uk/",
        "label": "European Language Social Science Thesaurus"
      },
      {
        "scheme": "CESSDA",
        "uri": "https://www.cessda.eu/",
        "label": "CESSDA controlled vocabularies"
      }
    ]
  },
  "assets": {
    "data": {
      "href": "https://gitlab.sintef.no/Lara.Veylit/saltmarsh_perceptions/-/tree/master/data/processed?ref_type=heads",
      "type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "title": "Norway monadic survey workbook"
    }
  },
  "links": [
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.seadots.catalog-data-tabular-survey",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data Tabular Survey"
    },
    {
      "rel": "describedby",
      "href": "https://www.sciencedirect.com/science/article/pii/S0964569124000942",
      "type": "text/html",
      "title": "Do citizens value climate change mitigation over biodiversity protection? Exploring citizen support for salt marsh management"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ddi: <https://ddialliance.org/terms#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <https://w3id.org/ogc/stac/assets/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix survey: <https://example.org/seadots/survey#> .
@prefix table: <https://stac-extensions.github.io/table/v1.2.0/schema.json#> .
@prefix thns: <https://w3id.org/ogc/stac/themes/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/saltmarsh-perceptions-norway> dcterms:date "2024-03-01T00:00:00+00:00"^^xsd:dateTime ;
    dcterms:description "Questionnaire export describing public perceptions of saltmarsh management and coastal ecosystem services." ;
    dcterms:license "CC BY-NC-SA 4.0" ;
    dcterms:title "Saltmarsh perceptions survey (Norway)" ;
    dcterms:type "Feature" ;
    rdfs:seeAlso [ rdfs:label "Do citizens value climate change mitigation over biodiversity protection? Exploring citizen support for salt marsh management" ;
            dcterms:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <https://www.sciencedirect.com/science/article/pii/S0964569124000942> ],
        [ rdfs:label "SeaDOTs Catalog Data Tabular Survey" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/profile> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-data-tabular-survey> ] ;
    survey:controlledVocabulary [ seadots:label "CESSDA controlled vocabularies" ;
            seadots:uri "https://www.cessda.eu/" ;
            thns:scheme "CESSDA" ],
        [ seadots:label "European Language Social Science Thesaurus" ;
            seadots:uri "https://elsst.uk/" ;
            thns:scheme "ELSST" ] ;
    survey:studyDescription "Monadic survey on attitudes toward saltmarsh management in Norway." ;
    survey:studyTitle "Saltmarsh perceptions survey" ;
    survey:variableMetadata [ ddi:variableDescription "Age group of the respondent" ;
            survey:conceptUri "https://elsst.uk/terms/age" ;
            survey:vocabularyUri "https://www.cessda.eu/cessda-vocabularies#age" ;
            seadots:label "Age group" ;
            seadots:questionText "What is your age group?" ;
            seadots:variableName "Q1" ],
        [ ddi:variableDescription "Likert-style attitude question" ;
            survey:conceptUri "https://elsst.uk/terms/environmental-concern" ;
            survey:vocabularyUri "https://www.cessda.eu/cessda-vocabularies#environmental-attitudes" ;
            seadots:label "Environmental concern" ;
            seadots:questionText "How important is the protection of the environment to you?" ;
            seadots:variableName "Q5_1" ] ;
    table:columns ( [ dcterms:description "Respondent identifier" ;
                dcterms:title "caseid" ;
                dcterms:type "string" ] [ dcterms:description "Country of residence" ;
                dcterms:title "Country" ;
                dcterms:type "string" ] [ dcterms:description "Respondent age group" ;
                dcterms:title "Q1" ;
                dcterms:type "string" ] [ dcterms:description "Respondent gender" ;
                dcterms:title "Q2" ;
                dcterms:type "string" ] ) ;
    table:primary_geometry "none" ;
    table:row_count 5046 ;
    seadots:itemType "record" ;
    seadots:role "data" ;
    stac:hasAsset [ ns2:data [ dcterms:format "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" ;
                    dcterms:title "Norway monadic survey workbook" ;
                    oa:hasTarget <https://gitlab.sintef.no/Lara.Veylit/saltmarsh_perceptions/-/tree/master/data/processed?ref_type=heads> ] ] ;
    stac:hasExtension "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
        "https://stac-extensions.github.io/table/v1.2.0/schema.json" ;
    stac:version "1.0.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SeaDOTs Catalog Data Tabular Survey
description: 'Survey-style tabular profile for saltmarsh perceptions data. It extends
  the SeaDOTs tabular catalog record profile with questionnaire-variable metadata,
  ELSST/CESSDA vocabulary links, and DDI-style descriptions.

  '
allOf:
- $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data-tabular/schema.yaml
type: object
required:
- type
- properties
- links
properties:
  type:
    const: Feature
  properties:
    type: object
    additionalProperties: true
    properties:
      survey:studyTitle:
        type: string
        x-jsonld-id: https://example.org/seadots/survey#studyTitle
      survey:studyDescription:
        type: string
        x-jsonld-id: https://example.org/seadots/survey#studyDescription
      survey:variableMetadata:
        type: array
        items:
          type: object
          required:
          - variableName
          properties:
            variableName:
              type: string
            questionText:
              type: string
            label:
              type: string
            conceptUri:
              type: string
              x-jsonld-id: https://example.org/seadots/survey#conceptUri
            vocabularyUri:
              type: string
              x-jsonld-id: https://example.org/seadots/survey#vocabularyUri
            ddi:variableDescription:
              type: string
              x-jsonld-id: https://ddialliance.org/terms#variableDescription
        x-jsonld-id: https://example.org/seadots/survey#variableMetadata
      survey:controlledVocabulary:
        type: array
        items:
          type: object
          properties:
            scheme:
              type: string
            uri:
              type: string
            label:
              type: string
        x-jsonld-id: https://example.org/seadots/survey#controlledVocabulary
  links:
    type: array
    contains:
      type: object
      required:
      - rel
      - href
      properties:
        rel:
          const: profile
        href:
          const: bblocks://ogc.hosted.seadots.catalog-data-tabular-survey
x-jsonld-prefixes:
  survey: https://example.org/seadots/survey#
  ddi: https://ddialliance.org/terms#
  elsst: https://elsst.uk/terms#
  cessda: https://vocabularies.cessda.eu/terms#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data-tabular-survey/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data-tabular-survey/schema.yaml)


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
    "type": "dct:type",
    "id": "@id",
    "properties": "@nest",
    "geometry": {
      "@context": {
        "type": "@type",
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
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
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
      "@id": "dct:subject"
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
      "@id": "thns:schemes",
      "@context": {
        "concepts": {
          "@id": "thns:concepts",
          "@context": {
            "id": {
              "@type": "xsd:string",
              "@id": "thns:id"
            },
            "url": {
              "@type": "@id",
              "@id": "@id"
            }
          },
          "@container": "@set"
        }
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
    "stac_extensions": "stac:hasExtension",
    "assets": {
      "@context": {
        "@vocab": "https://w3id.org/ogc/stac/assets/",
        "type": "dct:format",
        "roles": {
          "@id": "stac:roles",
          "@container": "@set"
        }
      },
      "@id": "stac:hasAsset",
      "@container": "@set"
    },
    "stac_version": "stac:version",
    "start_datetime": {
      "@id": "stac:start_datetime",
      "@type": "xsd:dateTime"
    },
    "end_datetime": {
      "@id": "stac:end_datetime",
      "@type": "xsd:dateTime"
    },
    "providers": "stac:hasProvider",
    "media_type": "dct:format",
    "extent": "dct:extent",
    "item_assets": {
      "@context": {
        "type": "@type"
      }
    },
    "datetime": {
      "@id": "dct:date",
      "@type": "xsd:dateTime"
    },
    "concepts": {
      "@id": "thns:concepts",
      "@container": "@set",
      "@context": {
        "name": "thns:name",
        "id": "thns:id",
        "url": "@id"
      }
    },
    "scheme": "thns:scheme",
    "wasInfluencedBy": {
      "@context": {
        "name": "rdfs:label"
      },
      "@id": "prov:wasInfluencedBy",
      "@type": "@id"
    },
    "qualifiedInfluence": {
      "@context": {
        "influencer": {
          "@context": {
            "name": "rdfs:label"
          },
          "@id": "prov:influencer",
          "@type": "@id"
        },
        "activity": {
          "@context": {
            "name": "rdfs:label"
          },
          "@id": "prov:activity",
          "@type": "@id"
        },
        "agent": {
          "@context": {
            "name": "rdfs:label"
          },
          "@id": "prov:agent",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedInfluence",
      "@type": "@id"
    },
    "hadMember": {
      "@id": "prov:hadMember",
      "@type": "@id"
    },
    "provType": "@type",
    "featureType": "@type",
    "entityType": "@type",
    "has_provenance": {
      "@context": {
        "name": "rdfs:label"
      },
      "@id": "dct:provenance",
      "@type": "@id"
    },
    "wasGeneratedBy": {
      "@context": {
        "name": "rdfs:label"
      },
      "@id": "prov:wasGeneratedBy",
      "@type": "@id"
    },
    "wasAttributedTo": {
      "@context": {
        "name": "rdfs:label"
      },
      "@id": "prov:wasAttributedTo",
      "@type": "@id"
    },
    "wasDerivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@type": "@id"
    },
    "alternateOf": {
      "@id": "prov:alternateOf",
      "@type": "@id"
    },
    "hadPrimarySource": {
      "@id": "prov:hadPrimarySource",
      "@type": "@id"
    },
    "specializationOf": {
      "@id": "prov:specializationOf",
      "@type": "@id"
    },
    "wasInvalidatedBy": {
      "@context": {
        "name": "rdfs:label"
      },
      "@id": "prov:wasInvalidatedBy",
      "@type": "@id"
    },
    "wasQuotedFrom": {
      "@id": "prov:wasQuotedFrom",
      "@type": "@id"
    },
    "wasRevisionOf": {
      "@id": "prov:wasRevisionOf",
      "@type": "@id"
    },
    "generatedAtTime": {
      "@id": "prov:generatedAtTime",
      "@type": "xsd:dateTime"
    },
    "invalidatedAtTime": {
      "@id": "prov:invalidatedAtTime",
      "@type": "xsd:dateTime"
    },
    "value": "prov:value",
    "qualifiedPrimarySource": {
      "@context": {
        "hadActivity": {
          "@context": {
            "wasAssociatedWith": {
              "@context": {
                "name": "rdfs:label"
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "name": "rdfs:label"
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedPrimarySource",
      "@type": "@id"
    },
    "qualifiedQuotation": {
      "@context": {
        "hadActivity": {
          "@context": {
            "wasAssociatedWith": {
              "@context": {
                "name": "rdfs:label"
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "name": "rdfs:label"
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedQuotation",
      "@type": "@id"
    },
    "qualifiedRevision": {
      "@context": {
        "hadActivity": {
          "@context": {
            "wasAssociatedWith": {
              "@context": {
                "name": "rdfs:label"
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "name": "rdfs:label"
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedRevision",
      "@type": "@id"
    },
    "atLocation": {
      "@id": "prov:atLocation",
      "@type": "@id"
    },
    "qualifiedGeneration": {
      "@id": "prov:qualifiedGeneration",
      "@type": "@id"
    },
    "qualifiedInvalidation": {
      "@id": "prov:qualifiedInvalidation",
      "@type": "@id"
    },
    "qualifiedDerivation": {
      "@context": {
        "hadActivity": {
          "@context": {
            "wasAssociatedWith": {
              "@context": {
                "name": "rdfs:label"
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "name": "rdfs:label"
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedDerivation",
      "@type": "@id"
    },
    "qualifiedAttribution": {
      "@context": {
        "agent": {
          "@context": {
            "name": "rdfs:label"
          },
          "@id": "prov:agent",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedAttribution",
      "@type": "@id"
    },
    "activityType": "@type",
    "agentType": "@type",
    "Activity": "prov:Activity",
    "ActivityInfluence": "prov:ActivityInfluence",
    "Agent": "prov:Agent",
    "AgentInfluence": "prov:AgentInfluence",
    "Association": "prov:Association",
    "Attribution": "prov:Attribution",
    "Bundle": "prov:Bundle",
    "Collection": "prov:Collection",
    "Communication": "prov:Communication",
    "Delegation": "prov:Delegation",
    "Derivation": "prov:Derivation",
    "EmptyCollection": "prov:EmptyCollection",
    "End": "prov:End",
    "Entity": "prov:Entity",
    "EntityInfluence": "prov:EntityInfluence",
    "Generation": "prov:Generation",
    "Influence": "prov:Influence",
    "InstantaneousEvent": "prov:InstantaneousEvent",
    "Invalidation": "prov:Invalidation",
    "Location": "prov:Location",
    "Organization": "prov:Organization",
    "Person": "prov:Person",
    "Plan": "prov:Plan",
    "PrimarySource": "prov:PrimarySource",
    "Quotation": "prov:Quotation",
    "Revision": "prov:Revision",
    "Role": "prov:Role",
    "SoftwareAgent": "prov:SoftwareAgent",
    "Start": "prov:Start",
    "Usage": "prov:Usage",
    "ServiceDescription": "prov:ServiceDescription",
    "DirectQueryService": "prov:DirectQueryService",
    "Accept": "prov:Accept",
    "Contribute": "prov:Contribute",
    "Contributor": "prov:Contributor",
    "Copyright": "prov:Copyright",
    "Create": "prov:Create",
    "Creator": "prov:Creator",
    "Modify": "prov:Modify",
    "Publish": "prov:Publish",
    "Publisher": "prov:Publisher",
    "Replace": "prov:Replace",
    "RightsAssignment": "prov:RightsAssignment",
    "RightsHolder": "prov:RightsHolder",
    "Submit": "prov:Submit",
    "Dictionary": "prov:Dictionary",
    "EmptyDictionary": "prov:EmptyDictionary",
    "KeyEntityPair": "prov:KeyEntityPair",
    "Insertion": "prov:Insertion",
    "Removal": "prov:Removal",
    "atTime": {
      "@id": "prov:atTime",
      "@type": "xsd:dateTime"
    },
    "endedAtTime": {
      "@id": "prov:endedAtTime",
      "@type": "xsd:dateTime"
    },
    "startedAtTime": {
      "@id": "prov:startedAtTime",
      "@type": "xsd:dateTime"
    },
    "provenanceUriTemplate": "prov:provenanceUriTemplate",
    "pairKey": {
      "@id": "prov:pairKey",
      "@type": "rdfs:Literal"
    },
    "removedKey": {
      "@id": "prov:removedKey",
      "@type": "rdfs:Literal"
    },
    "actedOnBehalfOf": {
      "@id": "prov:actedOnBehalfOf",
      "@type": "@id"
    },
    "agent": {
      "@id": "prov:agent",
      "@type": "@id"
    },
    "entity": {
      "@id": "prov:entity",
      "@type": "@id"
    },
    "generated": {
      "@id": "prov:generated",
      "@type": "@id"
    },
    "hadActivity": {
      "@id": "prov:hadActivity",
      "@type": "@id"
    },
    "activity": {
      "@id": "prov:activity",
      "@type": "@id"
    },
    "hadGeneration": {
      "@id": "prov:hadGeneration",
      "@type": "@id"
    },
    "hadPlan": {
      "@id": "prov:hadPlan",
      "@type": "@id"
    },
    "hadRole": {
      "@id": "prov:hadRole",
      "@type": "@id"
    },
    "hadUsage": {
      "@id": "prov:hadUsage",
      "@type": "@id"
    },
    "influenced": {
      "@id": "prov:influenced",
      "@type": "@id"
    },
    "influencer": {
      "@id": "prov:influencer",
      "@type": "@id"
    },
    "invalidated": {
      "@id": "prov:invalidated",
      "@type": "@id"
    },
    "qualifiedAssociation": {
      "@id": "prov:qualifiedAssociation",
      "@type": "@id"
    },
    "qualifiedCommunication": {
      "@id": "prov:qualifiedCommunication",
      "@type": "@id"
    },
    "qualifiedDelegation": {
      "@id": "prov:qualifiedDelegation",
      "@type": "@id"
    },
    "qualifiedEnd": {
      "@id": "prov:qualifiedEnd",
      "@type": "@id"
    },
    "qualifiedStart": {
      "@id": "prov:qualifiedStart",
      "@type": "@id"
    },
    "qualifiedUsage": {
      "@id": "prov:qualifiedUsage",
      "@type": "@id"
    },
    "used": {
      "@id": "prov:used",
      "@type": "@id"
    },
    "wasAssociatedWith": {
      "@id": "prov:wasAssociatedWith",
      "@type": "@id"
    },
    "wasEndedBy": {
      "@id": "prov:wasEndedBy",
      "@type": "@id"
    },
    "wasInformedBy": {
      "@id": "prov:wasInformedBy",
      "@type": "@id"
    },
    "wasStartedBy": {
      "@id": "prov:wasStartedBy",
      "@type": "@id"
    },
    "has_anchor": {
      "@id": "prov:has_anchor",
      "@type": "@id"
    },
    "has_query_service": {
      "@id": "prov:has_query_service",
      "@type": "@id"
    },
    "describesService": {
      "@id": "prov:describesService",
      "@type": "@id"
    },
    "pingback": {
      "@id": "prov:pingback",
      "@type": "@id"
    },
    "dictionary": {
      "@id": "prov:dictionary",
      "@type": "@id"
    },
    "derivedByInsertionFrom": {
      "@id": "prov:derivedByInsertionFrom",
      "@type": "@id"
    },
    "derivedByRemovalFrom": {
      "@id": "prov:derivedByRemovalFrom",
      "@type": "@id"
    },
    "insertedKeyEntityPair": {
      "@id": "prov:insertedKeyEntityPair",
      "@type": "@id"
    },
    "hadDictionaryMember": {
      "@id": "prov:hadDictionaryMember",
      "@type": "@id"
    },
    "pairEntity": {
      "@id": "prov:pairEntity",
      "@type": "@id"
    },
    "qualifiedInsertion": {
      "@id": "prov:qualifiedInsertion",
      "@type": "@id"
    },
    "qualifiedRemoval": {
      "@id": "prov:qualifiedRemoval",
      "@type": "@id"
    },
    "asInBundle": {
      "@id": "prov:asInBundle",
      "@type": "@id"
    },
    "mentionOf": {
      "@id": "prov:mentionOf",
      "@type": "@id"
    },
    "name": "dct:title",
    "unit": {
      "@id": "qudt:unit",
      "@context": {
        "@base": "http://qudt.org/vocab/unit/"
      }
    },
    "rights": "dcat:rights",
    "cf:parameter": {
      "@id": "cf:parameter",
      "@container": "@set"
    },
    "schema": {
      "@id": "dct:conformsTo",
      "@type": "@id"
    },
    "role": "seadots:role",
    "convention": "seadots:metadataConvention",
    "derivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@container": "@set",
      "@type": "@id"
    },
    "conceptUri": "survey:conceptUri",
    "vocabularyUri": "survey:vocabularyUri",
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
    "stac": "https://w3id.org/ogc/stac/core/",
    "cf": "https://stac-extensions.github.io/cf/v0.2.0/schema.json#",
    "seadots": "https://w3id.org/ogc/hosted/seadots/catalog#",
    "dcterms": "http://purl.org/dc/terms/",
    "qudt": "http://qudt.org/schema/qudt/",
    "table": "https://stac-extensions.github.io/table/v1.2.0/schema.json#",
    "survey": "https://example.org/seadots/survey#",
    "ddi": "https://ddialliance.org/terms#",
    "elsst": "https://elsst.uk/terms#",
    "cessda": "https://vocabularies.cessda.eu/terms#",
    "table:columns": {
      "@container": "@list"
    },
    "table:row_count": {
      "@type": "xsd:integer"
    },
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data-tabular-survey/context.jsonld)

## Sources

* [Saltmarsh perceptions survey workbook](https://github.com/seadots/saltmarsh_perceptions)
* [ELSST thesaurus](https://elsst.uk/)
* [CESSDA controlled vocabularies](https://www.cessda.eu/)
* [DDI Lifecycle](https://ddialliance.org/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/catalog-data-tabular-survey`

