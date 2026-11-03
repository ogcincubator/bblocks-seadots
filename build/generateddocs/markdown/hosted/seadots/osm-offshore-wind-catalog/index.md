
# OSM Polish Offshore Wind Catalog Record (Schema)

`ogc.hosted.seadots.osm-offshore-wind-catalog` *v0.1*

Representative catalog record for the 2026-10-27 OpenStreetMap GeoJSON snapshot of offshore wind infrastructure in the Polish Baltic. Profiles the SeaDOTs catalog-data-tabular record envelope while describing the source asset as GeoJSON and linking its source and wind-farm interpretation profiles.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Polish Baltic offshore wind OSM snapshot catalog record
#### json
```json
{
  "id": "osm-polish-offshore-wind-2026-10-27",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [16.74361, 54.953732],
      [17.78045, 54.953732],
      [17.78045, 55.13824],
      [16.74361, 55.13824],
      [16.74361, 54.953732]
    ]]
  },
  "bbox": [16.74361, 54.953732, 17.78045, 55.13824],
  "properties": {
    "title": "OpenStreetMap offshore wind infrastructure, Polish Baltic (2026-10-27 snapshot)",
    "description": "Dated GeoJSON snapshot of offshore wind related OpenStreetMap features in the Polish Baltic. The 292 features comprise 287 Points, 4 Polygons, and 1 feature with null geometry. OSM feature properties retain osm_type, osm_id, and the source tags object; records include generators/turbines, substations and wind-farm areas, so the collection is not exclusively a farm inventory.",
    "datetime": null,
    "start_datetime": "2026-10-27T00:00:00Z",
    "end_datetime": "2026-10-27T23:59:59.999Z",
    "retrieved": "2026-10-27",
    "coverage_note": "Source description says offshore Polish Baltic, latitude greater than 54.85; exact request bounds and feature-selection query are not recorded, so completeness cannot be assessed. start_datetime and end_datetime express the UTC calendar-day bounds for the date-only snapshot, not actual retrieval timestamps.",
    "feature_count": 292,
    "geometry_counts": {
      "Point": 287,
      "Polygon": 4,
      "null": 1
    },
    "extent": [16.74361, 54.953732, 17.78045, 55.13824],
    "license": "ODbL-1.0",
    "attribution": "OpenStreetMap contributors",
    "source": "https://api.openstreetmap.org/api/0.6/map",
    "role": "data"
  },
  "assets": {
    "data": {
      "href": "https://raw.githubusercontent.com/ogcincubator/bblocks-seadots/main/docs/baltic-ses-exercise/data/osm_polish_offshore_wind_2026-10-27.geojson",
      "type": "application/geo+json",
      "title": "Polish Baltic offshore wind OSM snapshot GeoJSON",
      "description": "Source GeoJSON FeatureCollection; each feature preserves the OSM object type and ID and its original tags. Relation members are retained where present.",
      "roles": ["data"]
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.seadots.catalog-data-tabular",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data Tabular shared catalog envelope"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.seadots.osm-offshore-wind-source",
      "type": "application/schema+json",
      "title": "OSM Offshore Wind Source feature model"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.seadots.emodnet-windfarm-osm",
      "type": "application/schema+json",
      "title": "EMODnet Windfarm OSM mapping profile"
    },
    {
      "rel": "license",
      "href": "https://opendatacommons.org/licenses/odbl/1-0/",
      "title": "Open Data Commons Open Database License (ODbL) 1.0"
    },
    {
      "rel": "cite-as",
      "href": "https://www.openstreetmap.org/copyright",
      "title": "© OpenStreetMap contributors"
    },
    {
      "rel": "source",
      "href": "https://api.openstreetmap.org/api/0.6/map",
      "title": "OpenStreetMap API map endpoint used for source extraction"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/osm-offshore-wind-catalog/context.jsonld",
  "id": "osm-polish-offshore-wind-2026-10-27",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          16.74361,
          54.953732
        ],
        [
          17.78045,
          54.953732
        ],
        [
          17.78045,
          55.13824
        ],
        [
          16.74361,
          55.13824
        ],
        [
          16.74361,
          54.953732
        ]
      ]
    ]
  },
  "bbox": [
    16.74361,
    54.953732,
    17.78045,
    55.13824
  ],
  "properties": {
    "title": "OpenStreetMap offshore wind infrastructure, Polish Baltic (2026-10-27 snapshot)",
    "description": "Dated GeoJSON snapshot of offshore wind related OpenStreetMap features in the Polish Baltic. The 292 features comprise 287 Points, 4 Polygons, and 1 feature with null geometry. OSM feature properties retain osm_type, osm_id, and the source tags object; records include generators/turbines, substations and wind-farm areas, so the collection is not exclusively a farm inventory.",
    "datetime": null,
    "start_datetime": "2026-10-27T00:00:00Z",
    "end_datetime": "2026-10-27T23:59:59.999Z",
    "retrieved": "2026-10-27",
    "coverage_note": "Source description says offshore Polish Baltic, latitude greater than 54.85; exact request bounds and feature-selection query are not recorded, so completeness cannot be assessed. start_datetime and end_datetime express the UTC calendar-day bounds for the date-only snapshot, not actual retrieval timestamps.",
    "feature_count": 292,
    "geometry_counts": {
      "Point": 287,
      "Polygon": 4,
      "null": 1
    },
    "extent": [
      16.74361,
      54.953732,
      17.78045,
      55.13824
    ],
    "license": "ODbL-1.0",
    "attribution": "OpenStreetMap contributors",
    "source": "https://api.openstreetmap.org/api/0.6/map",
    "role": "data"
  },
  "assets": {
    "data": {
      "href": "https://raw.githubusercontent.com/ogcincubator/bblocks-seadots/main/docs/baltic-ses-exercise/data/osm_polish_offshore_wind_2026-10-27.geojson",
      "type": "application/geo+json",
      "title": "Polish Baltic offshore wind OSM snapshot GeoJSON",
      "description": "Source GeoJSON FeatureCollection; each feature preserves the OSM object type and ID and its original tags. Relation members are retained where present.",
      "roles": [
        "data"
      ]
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.seadots.catalog-data-tabular",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data Tabular shared catalog envelope"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.seadots.osm-offshore-wind-source",
      "type": "application/schema+json",
      "title": "OSM Offshore Wind Source feature model"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.seadots.emodnet-windfarm-osm",
      "type": "application/schema+json",
      "title": "EMODnet Windfarm OSM mapping profile"
    },
    {
      "rel": "license",
      "href": "https://opendatacommons.org/licenses/odbl/1-0/",
      "title": "Open Data Commons Open Database License (ODbL) 1.0"
    },
    {
      "rel": "cite-as",
      "href": "https://www.openstreetmap.org/copyright",
      "title": "\u00a9 OpenStreetMap contributors"
    },
    {
      "rel": "source",
      "href": "https://api.openstreetmap.org/api/0.6/map",
      "title": "OpenStreetMap API map endpoint used for source extraction"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <https://w3id.org/ogc/stac/assets/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix osm: <https://www.openstreetmap.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/osm-polish-offshore-wind-2026-10-27> dcterms:date "2026-10-27"^^xsd:date ;
    dcterms:description "Dated GeoJSON snapshot of offshore wind related OpenStreetMap features in the Polish Baltic. The 292 features comprise 287 Points, 4 Polygons, and 1 feature with null geometry. OSM feature properties retain osm_type, osm_id, and the source tags object; records include generators/turbines, substations and wind-farm areas, so the collection is not exclusively a farm inventory.",
        "Source description says offshore Polish Baltic, latitude greater than 54.85; exact request bounds and feature-selection query are not recorded, so completeness cannot be assessed. start_datetime and end_datetime express the UTC calendar-day bounds for the date-only snapshot, not actual retrieval timestamps." ;
    dcterms:extent 1.674361e+01,
        1.778045e+01,
        5.495373e+01,
        5.513824e+01 ;
    dcterms:license "ODbL-1.0" ;
    dcterms:rightsHolder "OpenStreetMap contributors" ;
    dcterms:source <https://api.openstreetmap.org/api/0.6/map> ;
    dcterms:title "OpenStreetMap offshore wind infrastructure, Polish Baltic (2026-10-27 snapshot)" ;
    dcterms:type "Feature" ;
    rdfs:seeAlso [ rdfs:label "OpenStreetMap API map endpoint used for source extraction" ;
            ns1:relation <http://www.iana.org/assignments/relation/source> ;
            oa:hasTarget <https://api.openstreetmap.org/api/0.6/map> ],
        [ rdfs:label "© OpenStreetMap contributors" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget osm:copyright ],
        [ rdfs:label "EMODnet Windfarm OSM mapping profile" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/profile> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.emodnet-windfarm-osm> ],
        [ rdfs:label "OSM Offshore Wind Source feature model" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/profile> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.osm-offshore-wind-source> ],
        [ rdfs:label "SeaDOTs Catalog Data Tabular shared catalog envelope" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/profile> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-data-tabular> ],
        [ rdfs:label "Open Data Commons Open Database License (ODbL) 1.0" ;
            ns1:relation <http://www.iana.org/assignments/relation/license> ;
            oa:hasTarget <https://opendatacommons.org/licenses/odbl/1-0/> ],
        [ rdfs:label "SeaDOTs Catalog Data" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-data> ] ;
    geojson:bbox ( 1.674361e+01 5.495373e+01 1.778045e+01 5.513824e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.674361e+01 5.495373e+01 ) ( 1.778045e+01 5.495373e+01 ) ( 1.778045e+01 5.513824e+01 ) ( 1.674361e+01 5.513824e+01 ) ( 1.674361e+01 5.495373e+01 ) ) ) ] ;
    schema:additionalProperty [ geojson:Point 287 ;
            geojson:Polygon 4 ;
            seadots:null 1 ] ;
    schema:numberOfItems 292 ;
    seadots:itemType "record" ;
    seadots:role "data" ;
    stac:end_datetime "2026-10-27T23:59:59.999000+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ns2:data <https://raw.githubusercontent.com/ogcincubator/bblocks-seadots/main/docs/baltic-ses-exercise/data/osm_polish_offshore_wind_2026-10-27.geojson> ] ;
    stac:hasExtension "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
        "https://stac-extensions.github.io/prov/v1.0.0/schema.json" ;
    stac:start_datetime "2026-10-27T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" .

<https://raw.githubusercontent.com/ogcincubator/bblocks-seadots/main/docs/baltic-ses-exercise/data/osm_polish_offshore_wind_2026-10-27.geojson> dcterms:description "Source GeoJSON FeatureCollection; each feature preserves the OSM object type and ID and its original tags. Relation members are retained where present." ;
    dcterms:format "application/geo+json" ;
    dcterms:title "Polish Baltic offshore wind OSM snapshot GeoJSON" ;
    stac:hasAssetroles "data"^^xsd:string .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: OSM Polish Offshore Wind Catalog Record
description: 'Catalog record profile for a dated GeoJSON snapshot of OpenStreetMap
  features. The catalog record envelope reuses SeaDOTs catalog-data-tabular for shared
  catalog metadata; the referenced data asset remains GeoJSON and is not described
  as a CSV, table, or time series. Source-specific feature data are represented as
  GeoJSON features whose properties contain OSM identifiers and the original OSM tag
  map.

  '
allOf:
- $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data-tabular/schema.yaml
type: object
required:
- type
- itemType
- properties
- assets
- links
properties:
  type:
    const: Feature
    x-jsonld-id: http://purl.org/dc/terms/type
  itemType:
    const: record
  properties:
    type: object
    required:
    - title
    - description
    - datetime
    properties:
      datetime:
        type:
        - string
        - 'null'
        description: 'Null when only a date (not a date-time) is evidenced. Snapshot
          date is recorded separately in retrieved; this is not an observation timestamp
          or time series.

          '
        x-jsonld-id: http://purl.org/dc/terms/date
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
      start_datetime:
        type: string
        format: date-time
        description: 'For date-only source provenance, UTC start of the snapshot calendar
          day; this is a calendar-day bound, not an observed retrieval time.

          '
        x-jsonld-id: https://w3id.org/ogc/stac/core/start_datetime
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
      end_datetime:
        type: string
        format: date-time
        description: 'For date-only source provenance, UTC end of the snapshot calendar
          day; this is a calendar-day bound, not an observed retrieval time.

          '
        x-jsonld-id: https://w3id.org/ogc/stac/core/end_datetime
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
      license:
        const: ODbL-1.0
        x-jsonld-id: http://purl.org/dc/terms/license
      attribution:
        const: OpenStreetMap contributors
        x-jsonld-id: http://purl.org/dc/terms/rightsHolder
      source:
        const: https://api.openstreetmap.org/api/0.6/map
        x-jsonld-id: http://purl.org/dc/terms/source
        x-jsonld-type: '@id'
      retrieved:
        type: string
        format: date
        description: Evidenced retrieval date; source does not provide time of day.
        x-jsonld-id: http://purl.org/dc/terms/date
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
      coverage_note:
        type: string
        description: Textual caveat on geographic/selection coverage of the snapshot.
        x-jsonld-id: http://purl.org/dc/terms/description
      feature_count:
        type: integer
        minimum: 0
        x-jsonld-id: https://schema.org/numberOfItems
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
      geometry_counts:
        type: object
        properties:
          Point:
            type: integer
            minimum: 0
            x-jsonld-id: https://purl.org/geojson/vocab#Point
          Polygon:
            type: integer
            minimum: 0
            x-jsonld-id: https://purl.org/geojson/vocab#Polygon
          'null':
            type: integer
            minimum: 0
        x-jsonld-id: https://schema.org/additionalProperty
      extent:
        type: array
        prefixItems:
        - type: number
        - type: number
        - type: number
        - type: number
        minItems: 4
        maxItems: 4
        description: WGS 84 bbox [west, south, east, north] over available geometries.
        x-jsonld-id: http://purl.org/dc/terms/extent
    additionalProperties: true
    x-jsonld-id: '@nest'
  assets:
    type: object
    required:
    - data
    properties:
      data:
        type: object
        required:
        - href
        - type
        properties:
          type:
            const: application/geo+json
            x-jsonld-id: http://purl.org/dc/terms/format
          roles:
            contains:
              const: data
            x-jsonld-id: https://w3id.org/ogc/stac/core/hasAssetroles
            x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
            x-jsonld-container: '@set'
    additionalProperties: true
    x-jsonld-id: https://w3id.org/ogc/stac/core/hasAsset
    x-jsonld-container: '@set'
    x-jsonld-vocab: https://w3id.org/ogc/stac/assets/
    x-jsonld-extra-terms:
      href: '@id'
  links:
    type: array
    allOf:
    - contains:
        type: object
        required:
        - rel
        - href
        properties:
          rel:
            const: profile
          href:
            const: bblocks://ogc.hosted.seadots.catalog-data-tabular
    - contains:
        type: object
        required:
        - rel
        - href
        properties:
          rel:
            const: profile
          href:
            const: bblocks://ogc.hosted.seadots.osm-offshore-wind-source
    - contains:
        type: object
        required:
        - rel
        - href
        properties:
          rel:
            const: profile
          href:
            const: bblocks://ogc.hosted.seadots.emodnet-windfarm-osm
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
    x-jsonld-extra-terms:
      rel:
        x-jsonld-context:
          '@base': http://www.iana.org/assignments/relation/
        x-jsonld-id: http://www.iana.org/assignments/relation
        x-jsonld-type: '@id'
      type: http://purl.org/dc/terms/type
      hreflang: http://purl.org/dc/terms/language
      title: http://www.w3.org/2000/01/rdf-schema#label
      length: http://purl.org/dc/terms/extent
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
  FeatureCollection: https://purl.org/geojson/vocab#FeatureCollection
  GeometryCollection: https://purl.org/geojson/vocab#GeometryCollection
  LineString: https://purl.org/geojson/vocab#LineString
  MultiLineString: https://purl.org/geojson/vocab#MultiLineString
  MultiPoint: https://purl.org/geojson/vocab#MultiPoint
  MultiPolygon: https://purl.org/geojson/vocab#MultiPolygon
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
  description: http://purl.org/dc/terms/description
  keywords:
    x-jsonld-container: '@set'
    x-jsonld-id: http://www.w3.org/ns/dcat#keyword
  language: https://www.opengis.net/def/ogc-api/records/language
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
          id: https://w3id.org/ogc/stac/themes/id
          url: '@id'
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
  accessrights: http://purl.org/dc/terms/accessRights
  variables:
    x-jsonld-container: '@id'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/hasVariable
    x-jsonld-context:
      '@base': http://example.com/variables/
      '@vocab': https://www.opengis.net/def/ogc-api/records/
  stac_extensions: https://w3id.org/ogc/stac/core/hasExtension
  providers: https://w3id.org/ogc/stac/core/hasProvider
  stac_version: https://w3id.org/ogc/stac/core/version
  media_type: http://purl.org/dc/terms/format
  concepts:
    x-jsonld-id: https://w3id.org/ogc/stac/themes/concepts
    x-jsonld-container: '@set'
    x-jsonld-context:
      id: https://w3id.org/ogc/stac/themes/id
      title: https://w3id.org/ogc/stac/themes/name
      description: https://w3id.org/ogc/stac/themes/description
      url: '@id'
  scheme: https://w3id.org/ogc/stac/themes/scheme
  osc:type:
    x-jsonld-id: https://w3id.org/ogc/stac/osc/type
    x-jsonld-type: '@vocab'
    x-jsonld-context:
      project: https://w3id.org/ogc/stac/osc/project-type
      product: https://w3id.org/ogc/stac/osc/product-type
  osc:status:
    x-jsonld-id: https://w3id.org/ogc/stac/osc/status
    x-jsonld-type: '@vocab'
    x-jsonld-context:
      planned: https://w3id.org/ogc/stac/osc/planned
      ongoing: https://w3id.org/ogc/stac/osc/ongoing
      completed: https://w3id.org/ogc/stac/osc/completed
  osc:project:
    x-jsonld-id: https://w3id.org/ogc/stac/osc/project
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  osc:region:
    x-jsonld-id: https://w3id.org/ogc/stac/osc/region
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  osc:variables:
    x-jsonld-id: https://w3id.org/ogc/stac/osc/variables
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
    x-jsonld-container: '@set'
  osc:missions:
    x-jsonld-id: https://w3id.org/ogc/stac/osc/missions
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
    x-jsonld-container: '@set'
  osc:experiment:
    x-jsonld-id: https://w3id.org/ogc/stac/osc/experiment
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  osc:workflows:
    x-jsonld-id: https://w3id.org/ogc/stac/osc/workflows
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
    x-jsonld-container: '@set'
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
  activity:
    x-jsonld-id: http://www.w3.org/ns/prov#activity
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
  name: http://purl.org/dc/terms/title
  unit:
    x-jsonld-id: http://qudt.org/schema/qudt/unit
    x-jsonld-context:
      '@base': http://qudt.org/vocab/unit/
  role: https://w3id.org/ogc/hosted/seadots/catalog#role
  convention: https://w3id.org/ogc/hosted/seadots/catalog#metadataConvention
  cf:parameter:
    x-jsonld-id: https://stac-extensions.github.io/cf/v0.2.0/schema.json#parameter
    x-jsonld-container: '@set'
  derivedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
    x-jsonld-container: '@set'
    x-jsonld-type: '@id'
  table:columns:
    x-jsonld-id: https://stac-extensions.github.io/table/v1.2.0/schema.json#columns
    x-jsonld-container: '@list'
  table:primary_geometry: https://stac-extensions.github.io/table/v1.2.0/schema.json#primary_geometry
  table:row_count:
    x-jsonld-id: https://stac-extensions.github.io/table/v1.2.0/schema.json#row_count
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
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
  stac: https://w3id.org/ogc/stac/core/
  osc: https://w3id.org/ogc/stac/osc/
  oa: http://www.w3.org/ns/oa#
  prov: http://www.w3.org/ns/prov#
  qudt: http://qudt.org/schema/qudt/
  cf: https://stac-extensions.github.io/cf/v0.2.0/schema.json#
  seadots: https://w3id.org/ogc/hosted/seadots/catalog#
  dcterms: http://purl.org/dc/terms/
  table: https://stac-extensions.github.io/table/v1.2.0/schema.json#
  owl: http://www.w3.org/2002/07/owl#
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  w3ctime: http://www.w3.org/2006/time#
  dctype: http://purl.org/dc/dcmitype/
  vcard: http://www.w3.org/2006/vcard/ns#
  foaf: http://xmlns.com/foaf/0.1/
  schema: https://schema.org/
  osm: https://www.openstreetmap.org/
  odrl: http://www.w3.org/ns/odrl/2/
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.osm-offshore-wind-catalog
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-03'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/osm-offshore-wind-catalog/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/osm-offshore-wind-catalog/schema.yaml)


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
        "href": "@id",
        "data": {
          "@context": {
            "type": "dct:format",
            "roles": {
              "@id": "stac:hasAssetroles",
              "@type": "xsd:string",
              "@container": "@set"
            }
          }
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
        "id": "thns:id",
        "title": "thns:name",
        "description": "thns:description",
        "url": "@id"
      }
    },
    "scheme": "thns:scheme",
    "osc:type": {
      "@id": "osc:type",
      "@type": "@vocab",
      "@context": {
        "project": "osc:project-type",
        "product": "osc:product-type"
      }
    },
    "osc:status": {
      "@id": "osc:status",
      "@type": "@vocab",
      "@context": {
        "planned": "osc:planned",
        "ongoing": "osc:ongoing",
        "completed": "osc:completed"
      }
    },
    "osc:project": {
      "@id": "osc:project",
      "@type": "xsd:string"
    },
    "osc:region": {
      "@id": "osc:region",
      "@type": "xsd:string"
    },
    "osc:variables": {
      "@id": "osc:variables",
      "@type": "xsd:string",
      "@container": "@set"
    },
    "osc:missions": {
      "@id": "osc:missions",
      "@type": "xsd:string",
      "@container": "@set"
    },
    "osc:experiment": {
      "@id": "osc:experiment",
      "@type": "xsd:string"
    },
    "osc:workflows": {
      "@id": "osc:workflows",
      "@type": "xsd:string",
      "@container": "@set"
    },
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
    "name": "https://w3id.org/ogc/stac/cf/name",
    "unit": {
      "@id": "qudt:hasUnit",
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
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "table:columns": {
      "@id": "table:columns",
      "@container": "@list"
    },
    "table:primary_geometry": "table:primary_geometry",
    "table:row_count": {
      "@id": "table:row_count",
      "@type": "xsd:integer"
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
    "osc": "https://w3id.org/ogc/stac/osc/",
    "qudt": "http://qudt.org/schema/qudt/",
    "cf": "https://stac-extensions.github.io/cf/v0.2.0/schema.json#",
    "seadots": "https://w3id.org/ogc/hosted/seadots/catalog#",
    "dcterms": "http://purl.org/dc/terms/",
    "table": "https://stac-extensions.github.io/table/v1.2.0/schema.json#",
    "osm": "https://www.openstreetmap.org/",
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "attribution": "dct:rightsHolder",
    "source": {
      "@id": "dct:source",
      "@type": "@id"
    },
    "retrieved": {
      "@id": "dct:date",
      "@type": "xsd:date"
    },
    "coverage_note": "dct:description",
    "feature_count": {
      "@id": "https://schema.org/numberOfItems",
      "@type": "xsd:integer"
    },
    "geometry_counts": "https://schema.org/additionalProperty",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/osm-offshore-wind-catalog/context.jsonld)

## Sources

* [OpenStreetMap contributors](https://www.openstreetmap.org/copyright)
* [OpenStreetMap API map endpoint](https://api.openstreetmap.org/api/0.6/map)
* [Open Data Commons Open Database License (ODbL) 1.0](https://opendatacommons.org/licenses/odbl/1-0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/_staging/osm-offshore-wind-catalog`

