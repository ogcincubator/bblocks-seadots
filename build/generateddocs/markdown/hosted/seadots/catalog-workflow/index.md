
# SeaDOTs Catalog Workflow (Schema)

`ogc.hosted.seadots.catalog-workflow` *v0.1*

Generic OGC API Records and PROV-O profile for a discoverable reusable workflow, model, transformer, or digital-twin application.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# SeaDOTs Catalog Workflow

A workflow is the reusable catalog-facing plan for a digital twin application,
model, transformer, or processing service. It is represented as an OGC API
Records item with PROV-O plan semantics, so it carries both discovery metadata
and the intended method, model chain, version, expected inputs, expected
outputs, and planned Activity pattern repeated by every execution.

Runnable implementation details are linked through `applicationPackage`, which
points to the APKG/CWL-aligned `catalog-application-package` block. This avoids
maintaining a separate `catalog-application` record with duplicate metadata.

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
  "@context": [
    "https://ogcincubator.github.io/geodcat-ogcapi-records/build/annotated/geo/geodcat/geodcat-records/context.jsonld",
    "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-workflow/context.jsonld"
  ],
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/workflow/reef-effect",
  "type": "Feature",
  "itemType": "record",
  "conformsTo": [
    "https://docs.ogc.org/is/20-004/20-004.html",
    "http://www.w3.org/TR/prov-o/"
  ],
  "geometry": null,
  "properties": {
    "title": "Utsira reef-effect biomass workflow",
    "description": "Reusable catalog workflow for estimating reef-associated biomass around floating wind infrastructure.",
    "type": "Workflow",
    "applicationCategory": "DigitalTwinApplication",
    "version": "0.1.0",
    "method": "Evaluate a deterministic biomass equation over the AOI and taxon-specific parameters.",
    "activity": "https://w3id.org/ogc/hosted/seadots/catalog/activity/reef-effect-calculation",
    "softwareVersion": "0.1.0",
    "programmingLanguage": "Python",
    "applicationPackage": "../../catalog-application-package/examples/application-package.json",
    "inputs": [
      {
        "profileId": "ogc.hosted.seadots.catalog-data",
        "required": true,
        "role": "input",
        "description": "Generic STAC catalog data item accepted by this workflow."
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
        "profileId": "ogc.hosted.seadots.catalog-data",
        "required": true,
        "role": "output",
        "description": "Generic STAC catalog data item produced by this workflow."
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
      "href": "bblocks://ogc.hosted.seadots.catalog-workflow",
      "type": "application/schema+json"
    },
    {
      "rel": "related",
      "href": "bblocks://ogc.hosted.seadots.catalog-application-package/examples/application-package.json",
      "type": "application/json",
      "title": "Reef-effect application package"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-workflow/context.jsonld",
    "https://ogcincubator.github.io/geodcat-ogcapi-records/build/annotated/geo/geodcat/geodcat-records/context.jsonld",
    "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-workflow/context.jsonld"
  ],
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/workflow/reef-effect",
  "type": "Feature",
  "itemType": "record",
  "conformsTo": [
    "https://docs.ogc.org/is/20-004/20-004.html",
    "http://www.w3.org/TR/prov-o/"
  ],
  "geometry": null,
  "properties": {
    "title": "Utsira reef-effect biomass workflow",
    "description": "Reusable catalog workflow for estimating reef-associated biomass around floating wind infrastructure.",
    "type": "Workflow",
    "applicationCategory": "DigitalTwinApplication",
    "version": "0.1.0",
    "method": "Evaluate a deterministic biomass equation over the AOI and taxon-specific parameters.",
    "activity": "https://w3id.org/ogc/hosted/seadots/catalog/activity/reef-effect-calculation",
    "softwareVersion": "0.1.0",
    "programmingLanguage": "Python",
    "applicationPackage": "../../catalog-application-package/examples/application-package.json",
    "inputs": [
      {
        "profileId": "ogc.hosted.seadots.catalog-data",
        "required": true,
        "role": "input",
        "description": "Generic STAC catalog data item accepted by this workflow."
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
        "profileId": "ogc.hosted.seadots.catalog-data",
        "required": true,
        "role": "output",
        "description": "Generic STAC catalog data item produced by this workflow."
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
      "href": "bblocks://ogc.hosted.seadots.catalog-workflow",
      "type": "application/schema+json"
    },
    {
      "rel": "related",
      "href": "bblocks://ogc.hosted.seadots.catalog-application-package/examples/application-package.json",
      "type": "application/json",
      "title": "Reef-effect application package"
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
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/ogc/hosted/seadots/catalog/workflow/reef-effect> a prov:Plan,
        geojson:Feature ;
    dcterms:conformsTo <http://www.w3.org/TR/prov-o/>,
        <https://docs.ogc.org/is/20-004/20-004.html> ;
    dcterms:description "Reusable catalog workflow for estimating reef-associated biomass around floating wind infrastructure." ;
    dcterms:hasVersion "0.1.0" ;
    dcterms:license "https://creativecommons.org/licenses/by/4.0/" ;
    dcterms:method "Evaluate a deterministic biomass equation over the AOI and taxon-specific parameters." ;
    dcterms:title "Utsira reef-effect biomass workflow" ;
    rdfs:seeAlso [ dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-workflow> ],
        [ rdfs:label "Reef-effect application package" ;
            dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-application-package/examples/application-package.json> ] ;
    dcat:keyword "digital-twin",
        "offshore-wind",
        "open-science" ;
    prov:activity <https://w3id.org/ogc/hosted/seadots/catalog/activity/reef-effect-calculation> ;
    schema:applicationCategory "DigitalTwinApplication" ;
    schema:programmingLanguage "Python" ;
    schema:softwareVersion "0.1.0" ;
    apkg:inputs [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.catalog-data> ;
            dcterms:description "Generic STAC catalog data item accepted by this workflow." ;
            seadots:required true ;
            seadots:role "input" ],
        [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.benthic-biomass-density-mareano> ;
            dcterms:description "Optional baseline benthic biomass-density input profile." ;
            seadots:required false ;
            seadots:role "benthic-biomass-density" ],
        [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.area-of-interest> ;
            dcterms:description "GeoJSON Feature defining the spatial area for the calculation." ;
            seadots:required true ;
            seadots:role "area-of-interest" ] ;
    apkg:outputs [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.catalog-data> ;
            dcterms:description "Generic STAC catalog data item produced by this workflow." ;
            seadots:required true ;
            seadots:role "output" ],
        [ dcterms:conformsTo <file:///github/workspace/ogc.hosted.seadots.reef-effect-output> ;
            dcterms:description "Structured reef-effect biomass output record." ;
            seadots:required true ;
            seadots:role "reef-biomass-result" ] ;
    seadots:applicationPackage <file:///catalog-application-package/examples/application-package.json> ;
    seadots:itemType "record" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SeaDOTs Catalog Workflow
description: 'OGC API Records profile for a reusable SeaDOTs workflow, model, transformer,
  or digital-twin application. This is the catalog-facing plan and discovery record;
  runnable APKG/CWL details are linked through applicationPackage.

  '
allOf:
- $ref: https://ogcincubator.github.io/geodcat-ogcapi-records/build/annotated/geo/geodcat/geodcat-records/schema.yaml
- $ref: https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov-entity/schema.yaml
type: object
properties:
  '@context':
    oneOf:
    - type: string
      format: uri-reference
    - type: object
    - type: array
      items:
        oneOf:
        - type: string
          format: uri-reference
        - type: object
  type:
    const: Feature
    x-jsonld-id: '@type'
  itemType:
    const: record
  properties:
    type: object
    required:
    - title
    - description
    - type
    - applicationCategory
    - version
    - method
    properties:
      type:
        const: Workflow
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
      version:
        type: string
        x-jsonld-id: http://purl.org/dc/terms/hasVersion
      method:
        type: string
        x-jsonld-id: http://purl.org/dc/terms/method
      activity:
        type: string
        format: uri-reference
        description: URI of the planned PROV-O Activity pattern contained by this
          workflow.
        x-jsonld-id: http://www.w3.org/ns/prov#activity
        x-jsonld-type: '@id'
      softwareVersion:
        type: string
        x-jsonld-id: https://schema.org/softwareVersion
      programmingLanguage:
        type: string
        x-jsonld-id: https://schema.org/programmingLanguage
      applicationPackage:
        type: string
        format: uri-reference
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#applicationPackage
        x-jsonld-type: '@id'
      inputs:
        type: array
        description: Input profiles accepted by this workflow.
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
              description: Whether this input profile is required to execute the workflow.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#required
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
            role:
              type: string
              description: Workflow-specific input role.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#role
            description:
              type: string
              x-jsonld-container: '@set'
              x-jsonld-id: http://purl.org/dc/terms/description
        x-jsonld-id: https://w3id.org/apkg/terms/inputs
        x-jsonld-container: '@set'
      outputs:
        type: array
        description: Output profiles produced by this workflow.
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
              description: Whether this output profile is always produced by the workflow.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#required
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
            role:
              type: string
              description: Workflow-specific output role.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#role
            description:
              type: string
              x-jsonld-container: '@set'
              x-jsonld-id: http://purl.org/dc/terms/description
        x-jsonld-id: https://w3id.org/apkg/terms/outputs
        x-jsonld-container: '@set'
      keywords:
        type: array
        items:
          type: string
        x-jsonld-container: '@set'
        x-jsonld-id: http://www.w3.org/ns/dcat#keyword
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
      href:
        '@type': '@id'
        '@id': http://www.w3.org/ns/oa#hasTarget
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
  created: http://purl.org/dc/terms/created
  updated: http://purl.org/dc/terms/modified
  title:
    x-jsonld-container: '@set'
    x-jsonld-id: http://purl.org/dc/terms/title
  language:
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/language
    x-jsonld-context:
      code: https://www.opengis.net/def/ogc-api/records/languageCode
      name: http://www.w3.org/2004/02/skos/core#prefLabel
  languages:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/languages
    x-jsonld-context:
      code: https://www.opengis.net/def/ogc-api/records/languageCode
      name: http://www.w3.org/2004/02/skos/core#prefLabel
  resourceLanguages:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/resourceLanguages
    x-jsonld-context:
      code: https://www.opengis.net/def/ogc-api/records/languageCode
      name: http://www.w3.org/2004/02/skos/core#prefLabel
  externalIds:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/scopedIdentifier
    x-jsonld-context:
      scheme: https://www.opengis.net/def/ogc-api/records/scheme
      value: https://www.opengis.net/def/ogc-api/records/id
  themes:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/themes
    x-jsonld-context:
      concepts:
        '@id': https://w3id.org/ogc/stac/themes/concepts
        '@context':
          id:
            '@type': http://www.w3.org/2001/XMLSchema#string
            '@id': https://w3id.org/ogc/stac/themes/id
          url:
            '@type': '@id'
            '@id': '@id'
        '@container': '@set'
      scheme: https://w3id.org/ogc/stac/themes/scheme
  formats:
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/format
    x-jsonld-context:
      name: https://www.opengis.net/def/ogc-api/records/name
      mediaType: https://www.opengis.net/def/ogc-api/records/mediaType
    x-jsonld-container: '@set'
    x-jsonld-type: '@id'
  contacts:
    x-jsonld-container: '@set'
    x-jsonld-id: http://www.w3.org/ns/dcat#contactPoint
    x-jsonld-type: '@id'
  license: http://www.w3.org/ns/dcat#license
  accessrights: http://purl.org/dc/terms/accessRights
  variables:
    x-jsonld-container: '@id'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/hasVariable
    x-jsonld-context:
      '@base': http://example.com/variables/
      '@vocab': https://www.opengis.net/def/ogc-api/records/
  href:
    x-jsonld-type: '@id'
    x-jsonld-id: http://www.w3.org/ns/oa#hasTarget
  rights: http://www.w3.org/ns/dcat#rights
  wasInfluencedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasInfluencedBy
    x-jsonld-type: '@id'
  qualifiedInfluence:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInfluence
    x-jsonld-type: '@id'
  hadMember:
    x-jsonld-id: http://www.w3.org/ns/prov#hadMember
    x-jsonld-type: '@id'
  provType: '@type'
  featureType: '@type'
  entityType: '@type'
  has_provenance:
    x-jsonld-id: http://purl.org/dc/terms/provenance
    x-jsonld-type: '@id'
  wasGeneratedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
    x-jsonld-type: '@id'
  wasAttributedTo:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAttributedTo
    x-jsonld-type: '@id'
  wasDerivedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
    x-jsonld-type: '@id'
  alternateOf:
    x-jsonld-id: http://www.w3.org/ns/prov#alternateOf
    x-jsonld-type: '@id'
  hadPrimarySource:
    x-jsonld-id: http://www.w3.org/ns/prov#hadPrimarySource
    x-jsonld-type: '@id'
  specializationOf:
    x-jsonld-id: http://www.w3.org/ns/prov#specializationOf
    x-jsonld-type: '@id'
  wasInvalidatedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasInvalidatedBy
    x-jsonld-type: '@id'
  wasQuotedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasQuotedFrom
    x-jsonld-type: '@id'
  wasRevisionOf:
    x-jsonld-id: http://www.w3.org/ns/prov#wasRevisionOf
    x-jsonld-type: '@id'
  generatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#generatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  invalidatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#invalidatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  value: http://www.w3.org/ns/prov#value
  qualifiedPrimarySource:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedPrimarySource
    x-jsonld-type: '@id'
  qualifiedQuotation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedQuotation
    x-jsonld-type: '@id'
  qualifiedRevision:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedRevision
    x-jsonld-type: '@id'
  atLocation:
    x-jsonld-id: http://www.w3.org/ns/prov#atLocation
    x-jsonld-type: '@id'
  qualifiedGeneration:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedGeneration
    x-jsonld-type: '@id'
  qualifiedInvalidation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInvalidation
    x-jsonld-type: '@id'
  qualifiedDerivation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedDerivation
    x-jsonld-type: '@id'
  qualifiedAttribution:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedAttribution
    x-jsonld-type: '@id'
  activityType: '@type'
  agentType: '@type'
  Activity: http://www.w3.org/ns/prov#Activity
  ActivityInfluence: http://www.w3.org/ns/prov#ActivityInfluence
  Agent: http://www.w3.org/ns/prov#Agent
  AgentInfluence: http://www.w3.org/ns/prov#AgentInfluence
  Association: http://www.w3.org/ns/prov#Association
  Attribution: http://www.w3.org/ns/prov#Attribution
  Bundle: http://www.w3.org/ns/prov#Bundle
  Collection: http://www.w3.org/ns/prov#Collection
  Communication: http://www.w3.org/ns/prov#Communication
  Delegation: http://www.w3.org/ns/prov#Delegation
  Derivation: http://www.w3.org/ns/prov#Derivation
  EmptyCollection: http://www.w3.org/ns/prov#EmptyCollection
  End: http://www.w3.org/ns/prov#End
  Entity: http://www.w3.org/ns/prov#Entity
  EntityInfluence: http://www.w3.org/ns/prov#EntityInfluence
  Generation: http://www.w3.org/ns/prov#Generation
  Influence: http://www.w3.org/ns/prov#Influence
  InstantaneousEvent: http://www.w3.org/ns/prov#InstantaneousEvent
  Invalidation: http://www.w3.org/ns/prov#Invalidation
  Location: http://www.w3.org/ns/prov#Location
  Organization: http://www.w3.org/ns/prov#Organization
  Person: http://www.w3.org/ns/prov#Person
  Plan: http://www.w3.org/ns/prov#Plan
  PrimarySource: http://www.w3.org/ns/prov#PrimarySource
  Quotation: http://www.w3.org/ns/prov#Quotation
  Revision: http://www.w3.org/ns/prov#Revision
  Role: http://www.w3.org/ns/prov#Role
  SoftwareAgent: http://www.w3.org/ns/prov#SoftwareAgent
  Start: http://www.w3.org/ns/prov#Start
  Usage: http://www.w3.org/ns/prov#Usage
  ServiceDescription: http://www.w3.org/ns/prov#ServiceDescription
  DirectQueryService: http://www.w3.org/ns/prov#DirectQueryService
  Accept: http://www.w3.org/ns/prov#Accept
  Contribute: http://www.w3.org/ns/prov#Contribute
  Contributor: http://www.w3.org/ns/prov#Contributor
  Copyright: http://www.w3.org/ns/prov#Copyright
  Create: http://www.w3.org/ns/prov#Create
  Creator: http://www.w3.org/ns/prov#Creator
  Modify: http://www.w3.org/ns/prov#Modify
  Publish: http://www.w3.org/ns/prov#Publish
  Publisher: http://www.w3.org/ns/prov#Publisher
  Replace: http://www.w3.org/ns/prov#Replace
  RightsAssignment: http://www.w3.org/ns/prov#RightsAssignment
  RightsHolder: http://www.w3.org/ns/prov#RightsHolder
  Submit: http://www.w3.org/ns/prov#Submit
  Dictionary: http://www.w3.org/ns/prov#Dictionary
  EmptyDictionary: http://www.w3.org/ns/prov#EmptyDictionary
  KeyEntityPair: http://www.w3.org/ns/prov#KeyEntityPair
  Insertion: http://www.w3.org/ns/prov#Insertion
  Removal: http://www.w3.org/ns/prov#Removal
  atTime:
    x-jsonld-id: http://www.w3.org/ns/prov#atTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  endedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#endedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  startedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#startedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  provenanceUriTemplate: http://www.w3.org/ns/prov#provenanceUriTemplate
  pairKey:
    x-jsonld-id: http://www.w3.org/ns/prov#pairKey
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  removedKey:
    x-jsonld-id: http://www.w3.org/ns/prov#removedKey
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  actedOnBehalfOf:
    x-jsonld-id: http://www.w3.org/ns/prov#actedOnBehalfOf
    x-jsonld-type: '@id'
  agent:
    x-jsonld-id: http://www.w3.org/ns/prov#agent
    x-jsonld-type: '@id'
  entity:
    x-jsonld-id: http://www.w3.org/ns/prov#entity
    x-jsonld-type: '@id'
  generated:
    x-jsonld-id: http://www.w3.org/ns/prov#generated
    x-jsonld-type: '@id'
  hadActivity:
    x-jsonld-id: http://www.w3.org/ns/prov#hadActivity
    x-jsonld-type: '@id'
  hadGeneration:
    x-jsonld-id: http://www.w3.org/ns/prov#hadGeneration
    x-jsonld-type: '@id'
  hadPlan:
    x-jsonld-id: http://www.w3.org/ns/prov#hadPlan
    x-jsonld-type: '@id'
  hadRole:
    x-jsonld-id: http://www.w3.org/ns/prov#hadRole
    x-jsonld-type: '@id'
  hadUsage:
    x-jsonld-id: http://www.w3.org/ns/prov#hadUsage
    x-jsonld-type: '@id'
  influenced:
    x-jsonld-id: http://www.w3.org/ns/prov#influenced
    x-jsonld-type: '@id'
  influencer:
    x-jsonld-id: http://www.w3.org/ns/prov#influencer
    x-jsonld-type: '@id'
  invalidated:
    x-jsonld-id: http://www.w3.org/ns/prov#invalidated
    x-jsonld-type: '@id'
  qualifiedAssociation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedAssociation
    x-jsonld-type: '@id'
  qualifiedCommunication:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedCommunication
    x-jsonld-type: '@id'
  qualifiedDelegation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedDelegation
    x-jsonld-type: '@id'
  qualifiedEnd:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedEnd
    x-jsonld-type: '@id'
  qualifiedStart:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedStart
    x-jsonld-type: '@id'
  qualifiedUsage:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedUsage
    x-jsonld-type: '@id'
  used:
    x-jsonld-id: http://www.w3.org/ns/prov#used
    x-jsonld-type: '@id'
  wasAssociatedWith:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAssociatedWith
    x-jsonld-type: '@id'
  wasEndedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasEndedBy
    x-jsonld-type: '@id'
  wasInformedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasInformedBy
    x-jsonld-type: '@id'
  wasStartedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasStartedBy
    x-jsonld-type: '@id'
  has_anchor:
    x-jsonld-id: http://www.w3.org/ns/prov#has_anchor
    x-jsonld-type: '@id'
  has_query_service:
    x-jsonld-id: http://www.w3.org/ns/prov#has_query_service
    x-jsonld-type: '@id'
  describesService:
    x-jsonld-id: http://www.w3.org/ns/prov#describesService
    x-jsonld-type: '@id'
  pingback:
    x-jsonld-id: http://www.w3.org/ns/prov#pingback
    x-jsonld-type: '@id'
  dictionary:
    x-jsonld-id: http://www.w3.org/ns/prov#dictionary
    x-jsonld-type: '@id'
  derivedByInsertionFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#derivedByInsertionFrom
    x-jsonld-type: '@id'
  derivedByRemovalFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#derivedByRemovalFrom
    x-jsonld-type: '@id'
  insertedKeyEntityPair:
    x-jsonld-id: http://www.w3.org/ns/prov#insertedKeyEntityPair
    x-jsonld-type: '@id'
  hadDictionaryMember:
    x-jsonld-id: http://www.w3.org/ns/prov#hadDictionaryMember
    x-jsonld-type: '@id'
  pairEntity:
    x-jsonld-id: http://www.w3.org/ns/prov#pairEntity
    x-jsonld-type: '@id'
  qualifiedInsertion:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInsertion
    x-jsonld-type: '@id'
  qualifiedRemoval:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedRemoval
    x-jsonld-type: '@id'
  asInBundle:
    x-jsonld-id: http://www.w3.org/ns/prov#asInBundle
    x-jsonld-type: '@id'
  mentionOf:
    x-jsonld-id: http://www.w3.org/ns/prov#mentionOf
    x-jsonld-type: '@id'
  name: http://www.w3.org/2000/01/rdf-schema#label
  Workflow: http://www.w3.org/ns/prov#Plan
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/catalog#
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  dct: http://purl.org/dc/terms/
  rec: https://www.opengis.net/def/ogc-api/records/
  xsd: http://www.w3.org/2001/XMLSchema#
  dcat: http://www.w3.org/ns/dcat#
  skos: http://www.w3.org/2004/02/skos/core#
  thns: https://w3id.org/ogc/stac/themes/
  oa: http://www.w3.org/ns/oa#
  prov: http://www.w3.org/ns/prov#
  schema: https://schema.org/
  dcterms: http://purl.org/dc/terms/
  seadots: https://w3id.org/ogc/hosted/seadots/catalog#
  apkg: https://w3id.org/apkg/terms/
  owl: http://www.w3.org/2002/07/owl#
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  w3ctime: http://www.w3.org/2006/time#
  dctype: http://purl.org/dc/dcmitype/
  vcard: http://www.w3.org/2006/vcard/ns#
  foaf: http://xmlns.com/foaf/0.1/

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
    "wasInfluencedBy": {
      "@id": "prov:wasInfluencedBy",
      "@type": "@id"
    },
    "qualifiedInfluence": {
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
      "@id": "dct:provenance",
      "@type": "@id"
    },
    "wasGeneratedBy": {
      "@id": "prov:wasGeneratedBy",
      "@type": "@id"
    },
    "wasAttributedTo": {
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
      "@id": "prov:qualifiedPrimarySource",
      "@type": "@id"
    },
    "qualifiedQuotation": {
      "@id": "prov:qualifiedQuotation",
      "@type": "@id"
    },
    "qualifiedRevision": {
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
      "@id": "prov:qualifiedDerivation",
      "@type": "@id"
    },
    "qualifiedAttribution": {
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
    "name": "rdfs:label",
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "rights": "dcat:rights",
    "Workflow": "prov:Plan",
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
    "schema": "https://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "seadots": "https://w3id.org/ogc/hosted/seadots/catalog#",
    "apkg": "https://w3id.org/apkg/terms/",
    "applicationCategory": "schema:applicationCategory",
    "version": "dct:hasVersion",
    "method": "dct:method",
    "softwareVersion": "schema:softwareVersion",
    "programmingLanguage": "schema:programmingLanguage",
    "applicationPackage": {
      "@id": "seadots:applicationPackage",
      "@type": "@id"
    },
    "inputs": {
      "@context": {
        "profileId": {
          "@id": "dct:conformsTo",
          "@type": "@id"
        },
        "required": {
          "@id": "seadots:required",
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
          "@id": "seadots:required",
          "@type": "xsd:boolean"
        },
        "role": "seadots:role"
      },
      "@id": "apkg:outputs",
      "@container": "@set"
    },
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

