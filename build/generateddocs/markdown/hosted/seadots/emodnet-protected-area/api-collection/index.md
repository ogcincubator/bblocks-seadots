
# EMODnet-view collection description (Schema)

`ogc.hosted.seadots.emodnet-protected-area.api-collection` *v0.1*

Profile of the OGC API - Features collection description for collections that serve an EMODnet-compliant view of a national or regional source. Requires links to the EMODnet profile (rel=profile), the item schema (describedby), queryables, the source collection it is derived from, the corresponding EMODnet Human Activities layer and the source licence.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# EMODnet-view collection description

Profile of the OGC API - Features collection description (`/collections/{collectionId}`) for a
collection that serves an **EMODnet-compliant view** of a national or regional source, next to the
unchanged source collection on the same API.

A client must be able to find out from the collection description alone which EMODnet profile the
items follow, where they came from and how they were derived. The profile therefore requires these
links in addition to the standard members:

| `rel` | Target | Why |
|---|---|---|
| `profile` | the EMODnet target building block (`nationally-designated-area` or `rsc-mpa`) | RFC 6906: the items conform to it |
| `describedby` (`application/schema+json`) | the annotated item schema of that block | OGC API - Features Part 5 style schema |
| `http://www.opengis.net/def/rel/ogc/1.0/queryables` | the collection's queryables | filters use EMODnet attribute names, so `designatio=NO05` works on both services |
| `derived-from` | the source collection on the same API | provenance of every item |
| `related` | the corresponding EMODnet Human Activities layer | where the same sites are published by EMODnet |
| `license` | the source licence | the view inherits the source's terms |

The collection id must start with `emodnet-view-`, `itemType` is `feature` and CRS84 must be offered.
A link to the transform report (`seadotsTransformReport`, see `protected-area.transform-report`) is
recommended, so clients can see which sites were excluded, routed or differ from EMODnet.

pygeoapi provides all of these through the per-resource `links:` setting.

The examples are **illustrative target designs**: the two views are specified but not yet deployed.

## Examples

### Collection description for the Norwegian EMODnet view (target design)
**Illustrative target design, not a live response.** The collection `emodnet-view-no-nationallydesignatedareas` is specified here but not yet deployed on the Seadots pygeoapi instance. The document shows the collection description it must serve: profile, schema, queryables, source collection, corresponding EMODnet layer, source metadata, licence and the transform report, all reachable as links. Link targets to EMODnet, Geonorge and the licence are real; the Seadots API URLs point at a local pygeoapi instance (localhost:5000).

#### json
```json
{
  "id": "emodnet-view-no-nationallydesignatedareas",
  "title": "Norwegian marine protected sites - EMODnet nationally designated areas view",
  "description": "Miljødirektoratet Naturvernområder (marine subset) transformed to the EMODnet Human Activities nationallydesignatedareas schema. Values come from the national source, so they can differ from EMODnet where the EEA reporting chain differs (e.g. Møysalen). Sites decided after the last EEA reporting have natdaid null and id NO-<naturvernId>. Data: Miljødirektoratet, NLOD 2.0.",
  "keywords": ["protected sites", "marine protected areas", "Norway", "EMODnet", "INSPIRE"],
  "itemType": "feature",
  "crs": ["http://www.opengis.net/def/crs/OGC/1.3/CRS84"],
  "storageCrs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84",
  "extent": {
    "spatial": { "bbox": [[-10.0, 57.5, 35.0, 81.5]], "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84" },
    "temporal": { "interval": [[null, null]] }
  },
  "links": [
    { "rel": "self", "type": "application/json", "href": "http://localhost:5000/collections/emodnet-view-no-nationallydesignatedareas?f=json" },
    { "rel": "items", "type": "application/geo+json", "href": "http://localhost:5000/collections/emodnet-view-no-nationallydesignatedareas/items?f=json" },
    { "rel": "profile", "href": "https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.emodnet-protected-area.nationally-designated-area", "title": "EMODnet-compliant nationally designated area (OGC Building Block)" },
    { "rel": "describedby", "type": "application/schema+json", "href": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/nationally-designated-area/schema.json" },
    { "rel": "http://www.opengis.net/def/rel/ogc/1.0/queryables", "type": "application/schema+json", "href": "http://localhost:5000/collections/emodnet-view-no-nationallydesignatedareas/queryables?f=json" },
    { "rel": "derived-from", "type": "application/json", "href": "http://localhost:5000/collections/no-snapshot-naturvern-omrade-marine?f=json", "title": "Source: Naturvernområder, marine subset (snapshot)" },
    { "rel": "related", "href": "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=DescribeFeatureType&typeNames=emodnet:nationallydesignatedareas", "title": "EMODnet Human Activities: nationallydesignatedareas" },
    { "rel": "describedby", "type": "text/html", "href": "https://kartkatalog.geonorge.no/metadata/5857ec0a-8d2c-4cd8-baa2-0dc54ae213b4", "title": "Source dataset metadata (Geonorge)" },
    { "rel": "license", "type": "text/html", "href": "https://data.norge.no/nlod/en/2.0", "title": "NLOD 2.0 - attribution: Miljødirektoratet" },
    { "rel": "related", "type": "application/json", "href": "http://localhost:5000/collections/emodnet-view-no-nationallydesignatedareas/transform-report.json", "title": "Transform report: excluded sites, sites not yet reported to the EEA, differences from EMODnet" }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/api-collection/context.jsonld",
  "id": "emodnet-view-no-nationallydesignatedareas",
  "title": "Norwegian marine protected sites - EMODnet nationally designated areas view",
  "description": "Milj\u00f8direktoratet Naturvernomr\u00e5der (marine subset) transformed to the EMODnet Human Activities nationallydesignatedareas schema. Values come from the national source, so they can differ from EMODnet where the EEA reporting chain differs (e.g. M\u00f8ysalen). Sites decided after the last EEA reporting have natdaid null and id NO-<naturvernId>. Data: Milj\u00f8direktoratet, NLOD 2.0.",
  "keywords": [
    "protected sites",
    "marine protected areas",
    "Norway",
    "EMODnet",
    "INSPIRE"
  ],
  "itemType": "feature",
  "crs": [
    "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
  ],
  "storageCrs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84",
  "extent": {
    "spatial": {
      "bbox": [
        [
          -10.0,
          57.5,
          35.0,
          81.5
        ]
      ],
      "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
    },
    "temporal": {
      "interval": [
        [
          null,
          null
        ]
      ]
    }
  },
  "links": [
    {
      "rel": "self",
      "type": "application/json",
      "href": "http://localhost:5000/collections/emodnet-view-no-nationallydesignatedareas?f=json"
    },
    {
      "rel": "items",
      "type": "application/geo+json",
      "href": "http://localhost:5000/collections/emodnet-view-no-nationallydesignatedareas/items?f=json"
    },
    {
      "rel": "profile",
      "href": "https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.emodnet-protected-area.nationally-designated-area",
      "title": "EMODnet-compliant nationally designated area (OGC Building Block)"
    },
    {
      "rel": "describedby",
      "type": "application/schema+json",
      "href": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/nationally-designated-area/schema.json"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/queryables",
      "type": "application/schema+json",
      "href": "http://localhost:5000/collections/emodnet-view-no-nationallydesignatedareas/queryables?f=json"
    },
    {
      "rel": "derived-from",
      "type": "application/json",
      "href": "http://localhost:5000/collections/no-snapshot-naturvern-omrade-marine?f=json",
      "title": "Source: Naturvernomr\u00e5der, marine subset (snapshot)"
    },
    {
      "rel": "related",
      "href": "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=DescribeFeatureType&typeNames=emodnet:nationallydesignatedareas",
      "title": "EMODnet Human Activities: nationallydesignatedareas"
    },
    {
      "rel": "describedby",
      "type": "text/html",
      "href": "https://kartkatalog.geonorge.no/metadata/5857ec0a-8d2c-4cd8-baa2-0dc54ae213b4",
      "title": "Source dataset metadata (Geonorge)"
    },
    {
      "rel": "license",
      "type": "text/html",
      "href": "https://data.norge.no/nlod/en/2.0",
      "title": "NLOD 2.0 - attribution: Milj\u00f8direktoratet"
    },
    {
      "rel": "related",
      "type": "application/json",
      "href": "http://localhost:5000/collections/emodnet-view-no-nationallydesignatedareas/transform-report.json",
      "title": "Transform report: excluded sites, sites not yet reported to the EEA, differences from EMODnet"
    }
  ]
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

[] rdfs:seeAlso [ dct:type "application/schema+json" ;
            ns1:relation <http://www.opengis.net/def/rel/ogc/1.0/queryables> ;
            oa:hasTarget <http://localhost:5000/collections/emodnet-view-no-nationallydesignatedareas/queryables?f=json> ],
        [ dct:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/items> ;
            oa:hasTarget <http://localhost:5000/collections/emodnet-view-no-nationallydesignatedareas/items?f=json> ],
        [ rdfs:label "Transform report: excluded sites, sites not yet reported to the EEA, differences from EMODnet" ;
            dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <http://localhost:5000/collections/emodnet-view-no-nationallydesignatedareas/transform-report.json> ],
        [ rdfs:label "NLOD 2.0 - attribution: Miljødirektoratet" ;
            dct:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/license> ;
            oa:hasTarget <https://data.norge.no/nlod/en/2.0> ],
        [ rdfs:label "EMODnet Human Activities: nationallydesignatedareas" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=DescribeFeatureType&typeNames=emodnet:nationallydesignatedareas> ],
        [ rdfs:label "Source dataset metadata (Geonorge)" ;
            dct:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <https://kartkatalog.geonorge.no/metadata/5857ec0a-8d2c-4cd8-baa2-0dc54ae213b4> ],
        [ rdfs:label "EMODnet-compliant nationally designated area (OGC Building Block)" ;
            ns1:relation <http://www.iana.org/assignments/relation/profile> ;
            oa:hasTarget <https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.emodnet-protected-area.nationally-designated-area> ],
        [ rdfs:label "Source: Naturvernområder, marine subset (snapshot)" ;
            dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/derived-from> ;
            oa:hasTarget <http://localhost:5000/collections/no-snapshot-naturvern-omrade-marine?f=json> ],
        [ dct:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/nationally-designated-area/schema.json> ],
        [ dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <http://localhost:5000/collections/emodnet-view-no-nationallydesignatedareas?f=json> ] .


```


### Collection description for the HELCOM EMODnet view (target design)
**Illustrative target design, not a live response.** The collection `emodnet-view-helcom-rsc-mpa` (HELCOM MADS layer 54 transformed to EMODnet marineprotectedareas with rsc = HELCOM) is specified here but not yet deployed. Link targets to HELCOM, EMODnet and the licence are real; the Seadots API URLs point at a local pygeoapi instance (localhost:5000).

#### json
```json
{
  "id": "emodnet-view-helcom-rsc-mpa",
  "title": "HELCOM MPAs - EMODnet Regional Sea Convention MPA view",
  "description": "HELCOM MPAs (HELCOM MADS layer 54) transformed to the EMODnet Human Activities marineprotectedareas schema with rsc = HELCOM. Data: HELCOM, free to use with the source cited.",
  "keywords": ["marine protected areas", "Baltic Sea", "HELCOM", "EMODnet"],
  "itemType": "feature",
  "crs": ["http://www.opengis.net/def/crs/OGC/1.3/CRS84"],
  "extent": {
    "spatial": { "bbox": [[9.0, 53.0, 31.0, 66.5]], "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84" },
    "temporal": { "interval": [[null, null]] }
  },
  "links": [
    { "rel": "self", "type": "application/json", "href": "http://localhost:5000/collections/emodnet-view-helcom-rsc-mpa?f=json" },
    { "rel": "items", "type": "application/geo+json", "href": "http://localhost:5000/collections/emodnet-view-helcom-rsc-mpa/items?f=json" },
    { "rel": "profile", "href": "https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.emodnet-protected-area.rsc-mpa" },
    { "rel": "describedby", "type": "application/schema+json", "href": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/rsc-mpa/schema.json" },
    { "rel": "http://www.opengis.net/def/rel/ogc/1.0/queryables", "type": "application/schema+json", "href": "http://localhost:5000/collections/emodnet-view-helcom-rsc-mpa/queryables?f=json" },
    { "rel": "derived-from", "type": "application/json", "href": "http://localhost:5000/collections/helcom-live-mpas?f=json", "title": "Source: HELCOM MPAs (live)" },
    { "rel": "related", "href": "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=DescribeFeatureType&typeNames=emodnet:marineprotectedareas", "title": "EMODnet Human Activities: marineprotectedareas" },
    { "rel": "license", "type": "text/html", "href": "https://helcom.fi/about-us/data-policy/", "title": "HELCOM data policy - cite HELCOM as the source" }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/api-collection/context.jsonld",
  "id": "emodnet-view-helcom-rsc-mpa",
  "title": "HELCOM MPAs - EMODnet Regional Sea Convention MPA view",
  "description": "HELCOM MPAs (HELCOM MADS layer 54) transformed to the EMODnet Human Activities marineprotectedareas schema with rsc = HELCOM. Data: HELCOM, free to use with the source cited.",
  "keywords": [
    "marine protected areas",
    "Baltic Sea",
    "HELCOM",
    "EMODnet"
  ],
  "itemType": "feature",
  "crs": [
    "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
  ],
  "extent": {
    "spatial": {
      "bbox": [
        [
          9.0,
          53.0,
          31.0,
          66.5
        ]
      ],
      "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
    },
    "temporal": {
      "interval": [
        [
          null,
          null
        ]
      ]
    }
  },
  "links": [
    {
      "rel": "self",
      "type": "application/json",
      "href": "http://localhost:5000/collections/emodnet-view-helcom-rsc-mpa?f=json"
    },
    {
      "rel": "items",
      "type": "application/geo+json",
      "href": "http://localhost:5000/collections/emodnet-view-helcom-rsc-mpa/items?f=json"
    },
    {
      "rel": "profile",
      "href": "https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.emodnet-protected-area.rsc-mpa"
    },
    {
      "rel": "describedby",
      "type": "application/schema+json",
      "href": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/rsc-mpa/schema.json"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/queryables",
      "type": "application/schema+json",
      "href": "http://localhost:5000/collections/emodnet-view-helcom-rsc-mpa/queryables?f=json"
    },
    {
      "rel": "derived-from",
      "type": "application/json",
      "href": "http://localhost:5000/collections/helcom-live-mpas?f=json",
      "title": "Source: HELCOM MPAs (live)"
    },
    {
      "rel": "related",
      "href": "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=DescribeFeatureType&typeNames=emodnet:marineprotectedareas",
      "title": "EMODnet Human Activities: marineprotectedareas"
    },
    {
      "rel": "license",
      "type": "text/html",
      "href": "https://helcom.fi/about-us/data-policy/",
      "title": "HELCOM data policy - cite HELCOM as the source"
    }
  ]
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

[] rdfs:seeAlso [ dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/self> ;
            oa:hasTarget <http://localhost:5000/collections/emodnet-view-helcom-rsc-mpa?f=json> ],
        [ rdfs:label "EMODnet Human Activities: marineprotectedareas" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=DescribeFeatureType&typeNames=emodnet:marineprotectedareas> ],
        [ rdfs:label "HELCOM data policy - cite HELCOM as the source" ;
            dct:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/license> ;
            oa:hasTarget <https://helcom.fi/about-us/data-policy/> ],
        [ rdfs:label "Source: HELCOM MPAs (live)" ;
            dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/derived-from> ;
            oa:hasTarget <http://localhost:5000/collections/helcom-live-mpas?f=json> ],
        [ ns1:relation <http://www.iana.org/assignments/relation/profile> ;
            oa:hasTarget <https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.emodnet-protected-area.rsc-mpa> ],
        [ dct:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/rsc-mpa/schema.json> ],
        [ dct:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/items> ;
            oa:hasTarget <http://localhost:5000/collections/emodnet-view-helcom-rsc-mpa/items?f=json> ],
        [ dct:type "application/schema+json" ;
            ns1:relation <http://www.opengis.net/def/rel/ogc/1.0/queryables> ;
            oa:hasTarget <http://localhost:5000/collections/emodnet-view-helcom-rsc-mpa/queryables?f=json> ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EMODnet-view collection description
description: 'Profile of an OGC API - Features collection description (/collections/{collectionId})
  for a collection that serves an EMODnet-compliant view of a national or regional
  source. Besides the standard members it must declare, through links, which EMODnet
  profile the items follow, which source collection they were derived from, which
  EMODnet layer they correspond to, the licence and attribution of the source, and
  where the transform report can be read.

  '
allOf:
- $ref: https://ogcincubator.github.io/bblocks-ogcapi-features/build/annotated/api/features/v1/schemas/collection/schema.yaml
- type: object
  required:
  - id
  - title
  - links
  - extent
  - itemType
  - crs
  properties:
    id:
      type: string
      pattern: ^emodnet-view-[a-z0-9-]+$
    itemType:
      const: feature
    crs:
      type: array
      contains:
        const: http://www.opengis.net/def/crs/OGC/1.3/CRS84
    links:
      type: array
      allOf:
      - contains:
          description: The EMODnet-compliant profile the items conform to (RFC 6906
            profile link to the building block).
          type: object
          required:
          - rel
          - href
          properties:
            rel:
              const: profile
            href:
              enum:
              - https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.emodnet-protected-area.nationally-designated-area
              - https://ogcincubator.github.io/bblocks-seadots/bblock/ogc.hosted.seadots.emodnet-protected-area.rsc-mpa
      - contains:
          description: JSON Schema of the items (OGC API - Features Part 5 style).
          type: object
          required:
          - rel
          - href
          - type
          properties:
            rel:
              const: describedby
            type:
              const: application/schema+json
      - contains:
          description: Queryables using the EMODnet attribute names.
          type: object
          required:
          - rel
          - href
          properties:
            rel:
              const: http://www.opengis.net/def/rel/ogc/1.0/queryables
      - contains:
          description: The source collection on the same API that the view is derived
            from.
          type: object
          required:
          - rel
          - href
          properties:
            rel:
              const: derived-from
      - contains:
          description: The EMODnet Human Activities layer this view corresponds to.
          type: object
          required:
          - rel
          - href
          properties:
            rel:
              const: related
            href:
              type: string
              pattern: ^https://ows\.emodnet-humanactivities\.eu/
      - contains:
          description: Licence of the source data.
          type: object
          required:
          - rel
          - href
          properties:
            rel:
              const: license
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.emodnet-protected-area.api-collection
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-28'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/api-collection/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/api-collection/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "links": {
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
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
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/api-collection/context.jsonld)

## Sources

* [OGC API - Features - Part 1: Core, collection description](https://docs.ogc.org/is/17-069r4/17-069r4.html#_collection_)
* [OGC API - Features - Part 3: Filtering (queryables)](https://docs.ogc.org/is/19-079r2/19-079r2.html)
* [RFC 6906: The 'profile' link relation type](https://datatracker.ietf.org/doc/html/rfc6906)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/emodnet-protected-area/api-collection`

