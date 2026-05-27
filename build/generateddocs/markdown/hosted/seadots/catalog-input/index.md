
# SeaDOTs Catalog Input (Schema)

`ogc.hosted.seadots.catalog-input` *v0.1*

Generic STAC Item profile for a concrete dataset, parameter file, or configuration consumed by an execution.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# SeaDOTs Catalog Input

An input is a concrete STAC Item consumed by an execution. It may represent an observation collection, AOI, forcing dataset, parameter object, model configuration, or other resource used by a SeaDOTs application.

## Role in the Catalog Metadata Model

This generic building block supports the SeaDOTs catalog model described in
`data_framework/INTEROPERABILITY.md` under `Catalog Metadata Model` and
`2.2 Provenance model (Open Science)`.

## Source-property coverage gaps

This block is a generic catalog template and is not derived from a raw source
dataset. No source properties are intentionally dropped.

## Examples

### SeaDOTs Catalog Input
#### json
```json
{
  "id": "aoi-utsira",
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json"
  ],
  "collection": "seadots-inputs",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          4.7,
          59.1
        ],
        [
          5.0,
          59.1
        ],
        [
          5.0,
          59.4
        ],
        [
          4.7,
          59.4
        ],
        [
          4.7,
          59.1
        ]
      ]
    ]
  },
  "bbox": [
    4.7,
    59.1,
    5.0,
    59.4
  ],
  "properties": {
    "title": "Utsira area of interest",
    "description": "Example area-of-interest input for a SeaDOTs execution.",
    "datetime": "2026-05-26T00:00:00Z",
    "role": "input",
    "convention": "CF-1.10",
    "cf:parameter": [
      {
        "name": "area",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "m2",
        "description": "Optional CF-style parameter declaration for spatial input extent."
      }
    ]
  },
  "assets": {
    "data": {
      "href": "../../area-of-interest/examples/utsira_surroundings_aoi.json",
      "type": "application/geo+json",
      "title": "Utsira surroundings AOI",
      "cf:parameter": [
        {
          "name": "area",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "m2",
          "description": "Optional CF-style parameter declaration for spatial input extent."
        }
      ],
      "roles": [
        "data",
        "input"
      ]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "https://w3id.org/ogc/hosted/seadots/catalog/collections/seadots-inputs",
      "type": "application/json",
      "title": "SeaDOTs inputs"
    },
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-input",
      "type": "application/schema+json"
    },
    {
      "rel": "item",
      "href": "bblocks://ogc.hosted.seadots.area-of-interest/examples/utsira_surroundings_aoi.json",
      "type": "application/geo+json",
      "title": "Utsira surroundings AOI"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-input/context.jsonld",
  "id": "aoi-utsira",
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json"
  ],
  "collection": "seadots-inputs",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          4.7,
          59.1
        ],
        [
          5.0,
          59.1
        ],
        [
          5.0,
          59.4
        ],
        [
          4.7,
          59.4
        ],
        [
          4.7,
          59.1
        ]
      ]
    ]
  },
  "bbox": [
    4.7,
    59.1,
    5.0,
    59.4
  ],
  "properties": {
    "title": "Utsira area of interest",
    "description": "Example area-of-interest input for a SeaDOTs execution.",
    "datetime": "2026-05-26T00:00:00Z",
    "role": "input",
    "convention": "CF-1.10",
    "cf:parameter": [
      {
        "name": "area",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "m2",
        "description": "Optional CF-style parameter declaration for spatial input extent."
      }
    ]
  },
  "assets": {
    "data": {
      "href": "../../area-of-interest/examples/utsira_surroundings_aoi.json",
      "type": "application/geo+json",
      "title": "Utsira surroundings AOI",
      "cf:parameter": [
        {
          "name": "area",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "m2",
          "description": "Optional CF-style parameter declaration for spatial input extent."
        }
      ],
      "roles": [
        "data",
        "input"
      ]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "https://w3id.org/ogc/hosted/seadots/catalog/collections/seadots-inputs",
      "type": "application/json",
      "title": "SeaDOTs inputs"
    },
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-input",
      "type": "application/schema+json"
    },
    {
      "rel": "item",
      "href": "bblocks://ogc.hosted.seadots.area-of-interest/examples/utsira_surroundings_aoi.json",
      "type": "application/geo+json",
      "title": "Utsira surroundings AOI"
    }
  ]
}
```

#### ttl
```ttl
@prefix cf: <https://stac-extensions.github.io/cf/v0.2.0/schema.json#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <https://w3id.org/ogc/stac/cf/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/aoi-utsira> a geojson:Feature ;
    dcterms:date "2026-05-26T00:00:00+00:00"^^xsd:dateTime ;
    dcterms:description "Example area-of-interest input for a SeaDOTs execution." ;
    dcterms:title "Utsira area of interest" ;
    rdfs:seeAlso [ dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-input> ],
        [ rdfs:label "Utsira surroundings AOI" ;
            dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.area-of-interest/examples/utsira_surroundings_aoi.json> ],
        [ rdfs:label "SeaDOTs inputs" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://w3id.org/ogc/hosted/seadots/catalog/collections/seadots-inputs> ] ;
    geojson:bbox ( 4.7e+00 5.91e+01 5e+00 5.94e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 4.7e+00 5.91e+01 ) ( 5e+00 5.91e+01 ) ( 5e+00 5.94e+01 ) ( 4.7e+00 5.94e+01 ) ( 4.7e+00 5.91e+01 ) ) ) ] ;
    cf:parameter [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "Optional CF-style parameter declaration for spatial input extent." ;
            qudt:hasUnit "m2" ;
            ns2:name "area" ] ;
    seadots:collection "seadots-inputs" ;
    seadots:metadataConvention "CF-1.10" ;
    seadots:role "input" ;
    stac:hasAsset [ seadots:data [ dcterms:format "application/geo+json" ;
                    dcterms:title "Utsira surroundings AOI" ;
                    oa:hasTarget <file:///area-of-interest/examples/utsira_surroundings_aoi.json> ;
                    cf:parameter [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
                            dcterms:description "Optional CF-style parameter declaration for spatial input extent." ;
                            qudt:hasUnit "m2" ;
                            ns2:name "area" ] ;
                    stac:roles "data",
                        "input" ] ] ;
    stac:hasExtension "https://stac-extensions.github.io/cf/v0.2.0/schema.json" ;
    stac:version "1.0.0" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SeaDOTs Catalog Input
description: 'STAC Item profile for a concrete input consumed by a SeaDOTs execution.

  '
allOf:
- $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
- $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/cf/schema.yaml
type: object
properties:
  type:
    const: Feature
    x-jsonld-id: '@type'
  properties:
    type: object
    properties:
      role:
        type: string
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#role
      convention:
        type: string
        description: Optional metadata convention declaration, e.g. CF-1.10.
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#metadataConvention
    additionalProperties: true
    x-jsonld-id: '@nest'
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
  FeatureCollection: https://purl.org/geojson/vocab#FeatureCollection
  GeometryCollection: https://purl.org/geojson/vocab#GeometryCollection
  LineString: https://purl.org/geojson/vocab#LineString
  MultiLineString: https://purl.org/geojson/vocab#MultiLineString
  MultiPoint: https://purl.org/geojson/vocab#MultiPoint
  MultiPolygon: https://purl.org/geojson/vocab#MultiPolygon
  Point: https://purl.org/geojson/vocab#Point
  Polygon: https://purl.org/geojson/vocab#Polygon
  features:
    x-jsonld-container: '@set'
    x-jsonld-id: https://purl.org/geojson/vocab#features
  id: '@id'
  geometry:
    x-jsonld-context:
      coordinates:
        '@container': '@list'
        '@id': https://purl.org/geojson/vocab#coordinates
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
  bbox:
    x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#bbox
  links:
    x-jsonld-context:
      rel:
        '@context':
          '@base': http://www.iana.org/assignments/relation/
        '@id': http://www.iana.org/assignments/relation
        '@type': '@id'
      type: http://purl.org/dc/terms/type
      hreflang: http://purl.org/dc/terms/language
      title: http://www.w3.org/2000/01/rdf-schema#label
      length: http://purl.org/dc/terms/extent
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
  conformsTo:
    x-jsonld-container: '@set'
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
  time: http://purl.org/dc/terms/temporal
  linkTemplates:
    x-jsonld-context:
      rel:
        '@context':
          '@base': http://www.iana.org/assignments/relation/
        '@id': http://www.iana.org/assignments/relation
        '@type': '@id'
      type: http://purl.org/dc/terms/format
      hreflang: http://purl.org/dc/terms/language
      title: http://www.w3.org/2000/01/rdf-schema#label
      length: http://purl.org/dc/terms/extent
      uriTemplate:
        '@type': http://www.w3.org/2001/XMLSchema#string
        '@id': https://www.opengis.net/def/ogc-api/records/uriTemplate
      varBase: https://www.opengis.net/def/ogc-api/records/varBase
      variables:
        '@id': https://www.opengis.net/def/ogc-api/records/hasVariable
        '@container': '@index'
        '@index': http://purl.org/dc/terms/identifier
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/hasLinkTemplate
  stac_extensions: https://w3id.org/ogc/stac/core/hasExtension
  assets:
    x-jsonld-context:
      type: http://purl.org/dc/terms/format
      roles:
        '@id': https://w3id.org/ogc/stac/core/roles
        '@container': '@set'
    x-jsonld-id: https://w3id.org/ogc/stac/core/hasAsset
    x-jsonld-container: '@set'
  stac_version: https://w3id.org/ogc/stac/core/version
  title:
    x-jsonld-id: http://purl.org/dc/terms/title
    x-jsonld-container: '@set'
  description:
    x-jsonld-id: http://purl.org/dc/terms/description
    x-jsonld-container: '@set'
  keywords:
    x-jsonld-id: http://www.w3.org/ns/dcat#keyword
    x-jsonld-container: '@set'
  license: http://www.w3.org/ns/dcat#license
  start_datetime:
    x-jsonld-id: https://w3id.org/ogc/stac/core/start_datetime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  end_datetime:
    x-jsonld-id: https://w3id.org/ogc/stac/core/end_datetime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  providers: https://w3id.org/ogc/stac/core/hasProvider
  media_type: http://purl.org/dc/terms/format
  href:
    x-jsonld-type: '@id'
    x-jsonld-id: http://www.w3.org/ns/oa#hasTarget
  created: http://purl.org/dc/terms/created
  updated: http://purl.org/dc/terms/modified
  language: https://www.opengis.net/def/ogc-api/records/language
  languages:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/languages
  resourceLanguages:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/resourceLanguages
  externalIds:
    x-jsonld-context:
      scheme: https://www.opengis.net/def/ogc-api/records/scheme
      value: https://www.opengis.net/def/ogc-api/records/id
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/scopedIdentifier
  themes:
    x-jsonld-context:
      concepts:
        '@context':
          id: https://w3id.org/ogc/stac/themes/id
          url: '@id'
        '@id': https://w3id.org/ogc/stac/themes/concepts
        '@container': '@set'
      scheme: https://w3id.org/ogc/stac/themes/scheme
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/themes
  formats:
    x-jsonld-context:
      name: https://www.opengis.net/def/ogc-api/records/name
      mediaType: https://www.opengis.net/def/ogc-api/records/mediaType
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/format
    x-jsonld-type: '@id'
  contacts:
    x-jsonld-container: '@set'
    x-jsonld-id: http://www.w3.org/ns/dcat#contactPoint
    x-jsonld-type: '@id'
  rights: http://www.w3.org/ns/dcat#rights
  datetime:
    x-jsonld-id: http://purl.org/dc/terms/date
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  extent: http://purl.org/dc/terms/extent
  name: https://w3id.org/ogc/stac/cf/name
  unit:
    x-jsonld-id: http://qudt.org/schema/qudt/hasUnit
    x-jsonld-context:
      '@base': http://qudt.org/vocab/unit/
  cf:parameter:
    x-jsonld-id: https://stac-extensions.github.io/cf/v0.2.0/schema.json#parameter
    x-jsonld-container: '@set'
  schema:
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/catalog#
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  dct: http://purl.org/dc/terms/
  rec: https://www.opengis.net/def/ogc-api/records/
  xsd: http://www.w3.org/2001/XMLSchema#
  stac: https://w3id.org/ogc/stac/core/
  dcat: http://www.w3.org/ns/dcat#
  oa: http://www.w3.org/ns/oa#
  thns: https://w3id.org/ogc/stac/themes/
  cf: https://stac-extensions.github.io/cf/v0.2.0/schema.json#
  qudt: http://qudt.org/schema/qudt/
  seadots: https://w3id.org/ogc/hosted/seadots/catalog#
  dcterms: http://purl.org/dc/terms/
  skos: http://www.w3.org/2004/02/skos/core#
  owl: http://www.w3.org/2002/07/owl#
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  w3ctime: http://www.w3.org/2006/time#
  dctype: http://purl.org/dc/dcmitype/
  vcard: http://www.w3.org/2006/vcard/ns#
  prov: http://www.w3.org/ns/prov#
  foaf: http://xmlns.com/foaf/0.1/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-input/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-input/schema.yaml)


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
        "type": "dct:type",
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
    "stac_extensions": "stac:hasExtension",
    "assets": {
      "@context": {
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
    "title": "dct:title",
    "description": "dct:description",
    "keywords": "dct:subject",
    "license": "dct:license",
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
    "datetime": {
      "@id": "dct:date",
      "@type": "xsd:dateTime"
    },
    "name": "https://w3id.org/ogc/stac/cf/name",
    "unit": {
      "@id": "qudt:hasUnit",
      "@context": {
        "@base": "http://qudt.org/vocab/unit/"
      }
    },
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "created": "dct:created",
    "updated": "dct:modified",
    "language": "rec:language",
    "languages": {
      "@container": "@set",
      "@id": "rec:languages"
    },
    "resourceLanguages": {
      "@container": "@set",
      "@id": "rec:resourceLanguages"
    },
    "externalIds": {
      "@context": {
        "scheme": "rec:scheme",
        "value": "rec:id"
      },
      "@container": "@set",
      "@id": "rec:scopedIdentifier"
    },
    "themes": {
      "@context": {
        "concepts": {
          "@context": {
            "id": "thns:id",
            "url": "@id"
          },
          "@id": "thns:concepts",
          "@container": "@set"
        },
        "scheme": "thns:scheme"
      },
      "@container": "@set",
      "@id": "rec:themes"
    },
    "formats": {
      "@context": {
        "name": "rec:name",
        "mediaType": "rec:mediaType"
      },
      "@container": "@set",
      "@id": "rec:format",
      "@type": "@id"
    },
    "contacts": {
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
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
    "qudt": "http://qudt.org/schema/qudt/",
    "seadots": "https://w3id.org/ogc/hosted/seadots/catalog#",
    "dcterms": "http://purl.org/dc/terms/",
    "role": "seadots:role",
    "convention": "seadots:metadataConvention",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-input/context.jsonld)

## Sources

* [SeaDOTs Interoperability Framework - Catalog Metadata Model](https://github.com/ogcincubator/bblocks-seadots)
* [OGC API - Records](https://docs.ogc.org/is/20-004/20-004.html)
* [OGC bblocks-openscience](https://github.com/ogcincubator/bblocks-openscience)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/catalog-input`

