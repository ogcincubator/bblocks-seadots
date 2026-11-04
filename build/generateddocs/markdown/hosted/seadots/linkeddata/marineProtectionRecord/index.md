
# Marine Protection Dataset Record (Schema)

`ogc.hosted.seadots.linkeddata.marineProtectionRecord` *v0.1*

Profile of the GeoDCAT binding of OGC API Records for describing a dataset of marine protections and how to access it, requiring its descriptive metadata, temporal extent, creator and a link to its features.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Marine Protection Dataset Record

A profile of [OGC API Records](https://github.com/opengeospatial/ogcapi-records), through its GeoDCAT binding, for
describing a dataset of [marine protection features](../marineProtectionFeature).

The profile adds these constraints:

- `type` must be `dataset`.
- `title`, `description`, `keywords`, `contacts`, `license`, `created`, `updated` and `time` are required.
- At least one contact must have the role `creator`.
- At least one link must have `rel: items` and `type: application/geo+json`, giving access to the features.

It also adds `isAccessibleForFree` and `citation`, which have no equivalent in OGC API Records, mapped to `schema.org`
terms from the OGC Cross Domain Model. Other properties inherit their mappings to DCAT and DCTERMS.

### Additions to the inherited context

The context of OGC API Records, inherited through the GeoDCAT binding, does not carry some of the values required here
into RDF. This profile therefore maps these terms, none of which the inherited context defines:

| Term | Maps to | Otherwise |
|------|---------|-----------|
| `dataset` (value of `type`) | `dcat:Dataset` | resolves to a meaningless IRI relative to the base URI |
| `interval` | `time:hasTime`, as an ordered list | the temporal extent is an empty node |
| `organization`, `roles`, `emails` | `vcard:organization-name`, `vcard:role`, `vcard:hasEmail` | contacts retain only their links |

vCard is not part of the OGC Cross Domain Model, but is the range DCAT specifies for `dcat:contactPoint`.

### Mapping from the source catalog entry

The Ocean Data Platform publishes this dataset's [catalog entry](https://api.hubocean.earth/api/public/catalog/v2/jsonld/datasets/a608f54b-75c7-4df9-a3a8-cedbfa391873)
as a `schema:Dataset` in JSON-LD, which is **not** itself an OGC API Records response. The example is a manual mapping
of that entry into a Record, as retrieved on 2026-11-03:

| schema.org | Record |
|------------|--------|
| `@id` | `id` (final path segment), and a `rel: alternate` link |
| `name`, `description`, `keywords` | `properties.title`, `.description`, `.keywords` |
| `dateCreated`, `dateModified` | `properties.created`, `.updated` |
| `license` | `properties.license` as an SPDX identifier, and a `rel: license` link |
| `creator`, `provider`, `maintainer` | `properties.contacts`, using the source property name as the role |
| `temporalCoverage` | `time.interval` |
| `geosparql:hasGeometry` | `geometry`, converted from WKT |
| `distribution` | `properties.formats`, and a `rel: items` link to the items of `contentUrl` |
| `isPartOf` | a `rel: collection` link |
| `url` | a `rel: about` link |
| `isAccessibleForFree`, `citation` | `properties.isAccessibleForFree`, `.citation` |

`spatialCoverage` is not mapped, since it duplicates the extent given by `geosparql:hasGeometry`.

## Examples

### ProtectedSeas Navigator dataset
The [catalog entry](https://api.hubocean.earth/api/public/catalog/v2/jsonld/datasets/a608f54b-75c7-4df9-a3a8-cedbfa391873)
for the ProtectedSeas Navigator dataset, mapped to this profile. The mapping is described above.
#### json
```json
{
  "id": "a608f54b-75c7-4df9-a3a8-cedbfa391873",
  "type": "Feature",
  "conformsTo": [
    "http://www.opengis.net/spec/ogcapi-records-1/1.0/req/record-core"
  ],
  "time": {
    "interval": [
      "2018-12-31T23:00:00Z",
      "2025-12-29T23:00:00Z"
    ]
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -180.0,
          85.0
        ],
        [
          180.0,
          85.0
        ],
        [
          180.0,
          -85.0
        ],
        [
          -180.0,
          -85.0
        ],
        [
          -180.0,
          85.0
        ]
      ]
    ]
  },
  "properties": {
    "type": "dataset",
    "title": "ProtectedSeas Navigator V2 — Focused: Area-Based Protections",
    "description": "Navigator is the most comprehensive global map of marine life protections, with regulatory information for marine protected areas (MPAs) and marine managed areas (MMAs) worldwide. It catalogs boundary and regulation information for maritime areas that manage the extraction of natural living resources. Navigator enables comparisons through standardized ratings of fishing protection for each area, providing actionable insights into the state of conservation of the global ocean.\n\nThis version refines the dataset by excluding large-scale jurisdictional and fishery management zones (category_type = \"Jurisdictional Authority Area\", \"Fisheries Management Area\") as well as entries classified under country = \"Global\", \"High Seas / International\". The result is a more focused and performant view of localized marine protections. The complete database, which includes all area categories, is linked below.",
    "keywords": [
      "restrictions",
      "conservation",
      "marine protected areas",
      "management",
      "fishing protection",
      "MPA",
      "MPAs"
    ],
    "created": "2025-10-16T12:02:50Z",
    "updated": "2026-11-02T13:55:50Z",
    "license": "CC-BY-4.0",
    "formats": [
      {
        "mediaType": "application/geo+json"
      }
    ],
    "contacts": [
      {
        "organization": "ProtectedSeas",
        "roles": [
          "creator",
          "provider"
        ],
        "links": [
          {
            "rel": "about",
            "type": "text/html",
            "href": "https://protectedseas.net/"
          }
        ]
      },
      {
        "organization": "HUB Ocean",
        "roles": [
          "maintainer"
        ],
        "emails": [
          {
            "value": "info@oceandata.earth"
          }
        ],
        "links": [
          {
            "rel": "about",
            "type": "text/html",
            "href": "https://www.hubocean.earth/"
          }
        ]
      }
    ],
    "isAccessibleForFree": true,
    "citation": [
      "Navigator Data Download, ProtectedSeas®. Accessed [date] from Ocean Data Platform: https://app.hubocean.earth/catalog/dataset/a608f54b-75c7-4df9-a3a8-cedbfa391873/protectedseas-navigator-v2-focused-area-based-protections"
    ]
  },
  "links": [
    {
      "rel": "items",
      "type": "application/geo+json",
      "href": "https://api.hubocean.earth/api/features/collections/a608f54b-75c7-4df9-a3a8-cedbfa391873/items",
      "title": "Features of this dataset"
    },
    {
      "rel": "alternate",
      "type": "application/ld+json",
      "href": "https://api.hubocean.earth/api/public/catalog/v2/jsonld/datasets/a608f54b-75c7-4df9-a3a8-cedbfa391873",
      "title": "This entry as schema.org JSON-LD"
    },
    {
      "rel": "about",
      "type": "text/html",
      "href": "https://app.hubocean.earth/catalog/dataset/a608f54b-75c7-4df9-a3a8-cedbfa391873",
      "title": "Catalog page"
    },
    {
      "rel": "license",
      "type": "text/html",
      "href": "https://creativecommons.org/licenses/by/4.0/",
      "title": "CC BY 4.0"
    },
    {
      "rel": "collection",
      "type": "application/ld+json",
      "href": "https://api.hubocean.earth/api/public/catalog/v2/jsonld/data-collections/a8228453-d089-433b-90e1-92fe9c2aa7e1",
      "title": "ProtectedSeas Navigator - Global Marine Life Protections"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/linkeddata/marineProtectionRecord/context.jsonld",
  "id": "a608f54b-75c7-4df9-a3a8-cedbfa391873",
  "type": "Feature",
  "conformsTo": [
    "http://www.opengis.net/spec/ogcapi-records-1/1.0/req/record-core"
  ],
  "time": {
    "interval": [
      "2018-12-31T23:00:00Z",
      "2025-12-29T23:00:00Z"
    ]
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -180.0,
          85.0
        ],
        [
          180.0,
          85.0
        ],
        [
          180.0,
          -85.0
        ],
        [
          -180.0,
          -85.0
        ],
        [
          -180.0,
          85.0
        ]
      ]
    ]
  },
  "properties": {
    "type": "dataset",
    "title": "ProtectedSeas Navigator V2 \u2014 Focused: Area-Based Protections",
    "description": "Navigator is the most comprehensive global map of marine life protections, with regulatory information for marine protected areas (MPAs) and marine managed areas (MMAs) worldwide. It catalogs boundary and regulation information for maritime areas that manage the extraction of natural living resources. Navigator enables comparisons through standardized ratings of fishing protection for each area, providing actionable insights into the state of conservation of the global ocean.\n\nThis version refines the dataset by excluding large-scale jurisdictional and fishery management zones (category_type = \"Jurisdictional Authority Area\", \"Fisheries Management Area\") as well as entries classified under country = \"Global\", \"High Seas / International\". The result is a more focused and performant view of localized marine protections. The complete database, which includes all area categories, is linked below.",
    "keywords": [
      "restrictions",
      "conservation",
      "marine protected areas",
      "management",
      "fishing protection",
      "MPA",
      "MPAs"
    ],
    "created": "2025-10-16T12:02:50Z",
    "updated": "2026-11-02T13:55:50Z",
    "license": "CC-BY-4.0",
    "formats": [
      {
        "mediaType": "application/geo+json"
      }
    ],
    "contacts": [
      {
        "organization": "ProtectedSeas",
        "roles": [
          "creator",
          "provider"
        ],
        "links": [
          {
            "rel": "about",
            "type": "text/html",
            "href": "https://protectedseas.net/"
          }
        ]
      },
      {
        "organization": "HUB Ocean",
        "roles": [
          "maintainer"
        ],
        "emails": [
          {
            "value": "info@oceandata.earth"
          }
        ],
        "links": [
          {
            "rel": "about",
            "type": "text/html",
            "href": "https://www.hubocean.earth/"
          }
        ]
      }
    ],
    "isAccessibleForFree": true,
    "citation": [
      "Navigator Data Download, ProtectedSeas\u00ae. Accessed [date] from Ocean Data Platform: https://app.hubocean.earth/catalog/dataset/a608f54b-75c7-4df9-a3a8-cedbfa391873/protectedseas-navigator-v2-focused-area-based-protections"
    ]
  },
  "links": [
    {
      "rel": "items",
      "type": "application/geo+json",
      "href": "https://api.hubocean.earth/api/features/collections/a608f54b-75c7-4df9-a3a8-cedbfa391873/items",
      "title": "Features of this dataset"
    },
    {
      "rel": "alternate",
      "type": "application/ld+json",
      "href": "https://api.hubocean.earth/api/public/catalog/v2/jsonld/datasets/a608f54b-75c7-4df9-a3a8-cedbfa391873",
      "title": "This entry as schema.org JSON-LD"
    },
    {
      "rel": "about",
      "type": "text/html",
      "href": "https://app.hubocean.earth/catalog/dataset/a608f54b-75c7-4df9-a3a8-cedbfa391873",
      "title": "Catalog page"
    },
    {
      "rel": "license",
      "type": "text/html",
      "href": "https://creativecommons.org/licenses/by/4.0/",
      "title": "CC BY 4.0"
    },
    {
      "rel": "collection",
      "type": "application/ld+json",
      "href": "https://api.hubocean.earth/api/public/catalog/v2/jsonld/data-collections/a8228453-d089-433b-90e1-92fe9c2aa7e1",
      "title": "ProtectedSeas Navigator - Global Marine Life Protections"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix schema1: <http://schema.org/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://api.hubocean.earth/api/public/catalog/v2/jsonld/datasets/a608f54b-75c7-4df9-a3a8-cedbfa391873> a dcat:Dataset,
        geojson:Feature ;
    dcterms:conformsTo <http://www.opengis.net/spec/ogcapi-records-1/1.0/req/record-core> ;
    dcterms:created "2025-10-16T12:02:50Z" ;
    dcterms:description """Navigator is the most comprehensive global map of marine life protections, with regulatory information for marine protected areas (MPAs) and marine managed areas (MMAs) worldwide. It catalogs boundary and regulation information for maritime areas that manage the extraction of natural living resources. Navigator enables comparisons through standardized ratings of fishing protection for each area, providing actionable insights into the state of conservation of the global ocean.

This version refines the dataset by excluding large-scale jurisdictional and fishery management zones (category_type = "Jurisdictional Authority Area", "Fisheries Management Area") as well as entries classified under country = "Global", "High Seas / International". The result is a more focused and performant view of localized marine protections. The complete database, which includes all area categories, is linked below.""" ;
    dcterms:modified "2026-11-02T13:55:50Z" ;
    dcterms:temporal [ time:hasTime ( "2018-12-31T23:00:00Z" "2025-12-29T23:00:00Z" ) ] ;
    dcterms:title "ProtectedSeas Navigator V2 — Focused: Area-Based Protections" ;
    schema1:citation "Navigator Data Download, ProtectedSeas®. Accessed [date] from Ocean Data Platform: https://app.hubocean.earth/catalog/dataset/a608f54b-75c7-4df9-a3a8-cedbfa391873/protectedseas-navigator-v2-focused-area-based-protections" ;
    schema1:isAccessibleForFree true ;
    rdfs:seeAlso [ rdfs:label "This entry as schema.org JSON-LD" ;
            dcterms:format "application/ld+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/alternate> ;
            oa:hasTarget <https://api.hubocean.earth/api/public/catalog/v2/jsonld/datasets/a608f54b-75c7-4df9-a3a8-cedbfa391873> ],
        [ rdfs:label "CC BY 4.0" ;
            dcterms:format "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/license> ;
            oa:hasTarget <https://creativecommons.org/licenses/by/4.0/> ],
        [ rdfs:label "Catalog page" ;
            dcterms:format "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/about> ;
            oa:hasTarget <https://app.hubocean.earth/catalog/dataset/a608f54b-75c7-4df9-a3a8-cedbfa391873> ],
        [ rdfs:label "Features of this dataset" ;
            dcterms:format "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/items> ;
            oa:hasTarget <https://api.hubocean.earth/api/features/collections/a608f54b-75c7-4df9-a3a8-cedbfa391873/items> ],
        [ rdfs:label "ProtectedSeas Navigator - Global Marine Life Protections" ;
            dcterms:format "application/ld+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://api.hubocean.earth/api/public/catalog/v2/jsonld/data-collections/a8228453-d089-433b-90e1-92fe9c2aa7e1> ] ;
    dcat:contactPoint [ rdfs:seeAlso [ dcterms:format "text/html" ;
                    ns1:relation <http://www.iana.org/assignments/relation/about> ;
                    oa:hasTarget <https://www.hubocean.earth/> ] ;
            vcard:hasEmail "info@oceandata.earth" ;
            vcard:organization-name "HUB Ocean" ;
            vcard:role "maintainer" ],
        [ rdfs:seeAlso [ dcterms:format "text/html" ;
                    ns1:relation <http://www.iana.org/assignments/relation/about> ;
                    oa:hasTarget <https://protectedseas.net/> ] ;
            vcard:organization-name "ProtectedSeas" ;
            vcard:role "creator",
                "provider" ] ;
    dcat:keyword "MPA",
        "MPAs",
        "conservation",
        "fishing protection",
        "management",
        "marine protected areas",
        "restrictions" ;
    dcat:license "CC-BY-4.0" ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -1.8e+02 8.5e+01 ) ( 1.8e+02 8.5e+01 ) ( 1.8e+02 -8.5e+01 ) ( -1.8e+02 -8.5e+01 ) ( -1.8e+02 8.5e+01 ) ) ) ] ;
    rec:format [ rec:mediaType "application/geo+json" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Record describing a dataset of marine protections
allOf:
- $ref: https://ogcincubator.github.io/geodcat-ogcapi-records/build/annotated/geo/geodcat/geodcat-records/schema.yaml
- type: object
  required:
  - time
  properties:
    properties:
      type: object
      required:
      - type
      - title
      - description
      - keywords
      - contacts
      - license
      - created
      - updated
      properties:
        type:
          const: dataset
        keywords:
          minItems: 1
        contacts:
          description: At least one contact must identify the creator of the dataset.
          contains:
            type: object
            required:
            - roles
            properties:
              roles:
                contains:
                  const: creator
        isAccessibleForFree:
          type: boolean
          description: A flag to signal that the dataset is accessible for free.
          x-jsonld-id: http://schema.org/isAccessibleForFree
          x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
        citation:
          type: array
          description: The recommended citations for the dataset.
          items:
            type: string
          x-jsonld-id: http://schema.org/citation
          x-jsonld-container: '@set'
    links:
      description: At least one link must give access to the features of the dataset.
      contains:
        type: object
        required:
        - rel
        - type
        properties:
          rel:
            const: items
          type:
            const: application/geo+json
x-jsonld-extra-terms:
  dataset: http://www.w3.org/ns/dcat#Dataset
  interval:
    x-jsonld-id: http://www.w3.org/2006/time#hasTime
    x-jsonld-container: '@list'
  organization: http://www.w3.org/2006/vcard/ns#organization-name
  roles:
    x-jsonld-id: http://www.w3.org/2006/vcard/ns#role
    x-jsonld-container: '@set'
  emails:
    x-jsonld-id: http://www.w3.org/2006/vcard/ns#hasEmail
    x-jsonld-container: '@set'
    x-jsonld-context:
      value: '@value'
x-jsonld-prefixes:
  vcard: http://www.w3.org/2006/vcard/ns#
  schema: http://schema.org/
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.linkeddata.marineProtectionRecord
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-04'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/linkeddata/marineProtectionRecord/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/linkeddata/marineProtectionRecord/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
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
    "properties": "@nest",
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
        },
        "scheme": "thns:scheme"
      }
    },
    "formats": {
      "@id": "rec:format",
      "@context": {
        "name": "rec:name",
        "mediaType": "rec:mediaType"
      },
      "@container": "@set",
      "@type": "@id"
    },
    "contacts": {
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "license": "dcat:license",
    "accessrights": "dct:accessRights",
    "variables": {
      "@container": "@id",
      "@id": "rec:hasVariable",
      "@context": {
        "@base": "http://example.com/variables/",
        "@vocab": "https://www.opengis.net/def/ogc-api/records/"
      }
    },
    "isAccessibleForFree": {
      "@id": "schema:isAccessibleForFree",
      "@type": "xsd:boolean"
    },
    "citation": {
      "@id": "schema:citation",
      "@container": "@set"
    },
    "dataset": "dcat:Dataset",
    "interval": {
      "@id": "w3ctime:hasTime",
      "@container": "@list"
    },
    "organization": "vcard:organization-name",
    "roles": {
      "@id": "vcard:role",
      "@container": "@set"
    },
    "emails": {
      "@id": "vcard:hasEmail",
      "@container": "@set",
      "@context": {
        "value": "@value"
      }
    },
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
    "schema": "http://schema.org/",
    "rights": "dcat:rights",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/linkeddata/marineProtectionRecord/context.jsonld)

## Sources

* [OGC API - Records](https://github.com/opengeospatial/ogcapi-records)
* [Ocean Data Platform catalog entry (schema.org JSON-LD)](https://api.hubocean.earth/api/public/catalog/v2/jsonld/datasets/a608f54b-75c7-4df9-a3a8-cedbfa391873)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/linkeddata/marineProtectionRecord`

