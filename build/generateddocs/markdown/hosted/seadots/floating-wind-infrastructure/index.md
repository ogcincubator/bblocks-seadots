
# Floating-Wind Submerged Infrastructure (Schema)

`ogc.hosted.seadots.floating-wind-infrastructure` *v0.1*

OGC Feature profile describing per-unit submerged geometry (wetted hull + mooring + anchor surfaces) of a floating-wind farm layout. Used as the feature-of-interest geometry input to reef-effect biomass equations (drives the A_sub aggregate). Inline `data` block carries per-unit areas, count, design label, aggregate submerged area, and sample unit coordinates; geometry travels in the top-level GeoJSON Polygon.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Floating-Wind Submerged Infrastructure

OGC API Records / OGC Feature profile describing the submerged geometry of a floating-wind farm layout.

The record carries:
- a top-level GeoJSON Polygon delimiting the farm's licence footprint;
- a `floatingWindInfrastructure.data` block carrying per-unit surface areas (hull, mooring, anchor), the unit count, an aggregate submerged area, and a small sample of per-unit coordinates with submerged area;
- mandatory `data.provenance` distinguishing the values that come from a real engineering source (e.g. NVE assessment for `nUnits` and `unitDesign`) from illustrative values for per-unit areas.

The aggregate `submerged_area_total_m2` is the variable consumed as `A_sub` in the reef-biomass equation `B_reef = sum_i (A_sub · D_pre,i · AF_i · C_t)`.

## Dependency

Inherits the OIM feature shape from `ogc.hosted.iliad.api.features.oim`.

## Required fields for script consumption

The accompanying calculator script (`_sources/experiment/scripts/utsira_reef_biomass.py`) reads `data.aggregate.submerged_area_total_m2`. That field is marked `required` in the schema.

## Examples

### Utsira Nord 60 × 15 MW — submerged infrastructure layout
#### json
```json
{
  "id": "https://example.org/norwegian-ses/floating-wind-infrastructure/utsira-nord-60x15mw",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [4.40, 59.20],
      [5.10, 59.20],
      [5.10, 59.55],
      [4.40, 59.55],
      [4.40, 59.20]
    ]]
  },
  "properties": {
    "type": "Dataset",
    "title": "Submerged infrastructure layout — Utsira Nord 60 × 15 MW",
    "description": "Per-unit submerged geometry (wetted hull + mooring + anchor surfaces) for the 60 × 15 MW floating-wind units of the Utsira Nord engineering design. Drives the A_sub calculation in the reef-biomass equation.",
    "created": "2026-05-18",
    "updated": "2026-05-19",
    "language": { "code": "en" },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "themes": [{ "concepts": [{ "id": "floating-wind", "label": "Floating wind infrastructure" }], "scheme": "https://id3.seadots.eu/themes" }],
    "keywords": ["infrastructure", "floating-wind", "Utsira Nord", "submerged area"],
    "formats": [{ "mediaType": "application/geo+json" }],
    "floatingWindInfrastructure": {
      "name": "Submerged infrastructure layout — Utsira Nord 60 × 15 MW",
      "description": "Per-unit submerged geometry for the floating-wind units intersecting the AOI.",
      "role": "feature-of-interest geometry",
      "source": "infrastructure/utsira_nord_60x15mw.geojson",
      "format": "application/geo+json",
      "vocabularyTerm": "https://id3.seadots.eu/indicator/submerged-infrastructure-area-utsira-design",
      "data": {
        "unitDesign": "15 MW semi-submersible (3-column hull, 3-point catenary mooring, drag-embedment anchors)",
        "nUnits": 60,
        "perUnit": {
          "hull_area_m2": 1450,
          "mooring_area_m2": 280,
          "anchor_area_m2": 95,
          "submerged_area_total_m2": 1825,
          "depth_range_m": [200, 280]
        },
        "aggregate": {
          "submerged_area_total_m2": 109500,
          "submerged_area_total_km2": 0.1095
        },
        "sampleUnits": [
          { "unit_id": "U01", "lon": 4.5520, "lat": 59.3812, "submerged_area_m2": 1825 },
          { "unit_id": "U02", "lon": 4.5780, "lat": 59.3812, "submerged_area_m2": 1825 },
          { "unit_id": "U03", "lon": 4.6040, "lat": 59.3812, "submerged_area_m2": 1825 }
        ],
        "units": "m2",
        "provenance": {
          "values": "mixed",
          "note": "`unitDesign=15 MW semi-submersible` and `nUnits=60` match the publicly stated Utsira Nord engineering envelope (NVE strategic assessment). Per-unit surface areas (1450 / 280 / 95 m²), depth range, sample unit coordinates and the 109,500 m² aggregate are ILLUSTRATIVE — actual wetted areas depend on platform-supplier engineering drawings that are not in the public domain.",
          "primarySource": {
            "url": "https://veiledere.nve.no/havvind/strategisk-konsekvensutredning-av-vindkraft-til-havs/",
            "title": "NVE Strategisk konsekvensutredning av vindkraft til havs (covers `nUnits` and `unitDesign` only)"
          },
          "nearestAuthoritativeSource": {
            "url": "https://www.equinor.com/energy/hywind-tampen",
            "note": "Hywind Tampen 11×8.6 MW spar-buoy is the closest deployed Norwegian floating-wind asset with public-domain geometry; the Utsira Nord 15 MW semi-submersible has different surface areas. Use only for orientation."
          }
        }
      }
    }
  },
  "links": [
    { "rel": "describedby", "href": "bblocks://ogc.hosted.seadots.floating-wind-infrastructure", "type": "application/schema+json", "title": "Floating-Wind Submerged Infrastructure bblock" },
    { "rel": "profile", "href": "bblocks://ogc.hosted.iliad.api.features.oim", "type": "application/schema+json", "title": "OIM feature profile" },
    { "rel": "cite-as", "href": "https://veiledere.nve.no/havvind/strategisk-konsekvensutredning-av-vindkraft-til-havs/", "title": "NVE strategic assessment — Utsira Nord design source" }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/floating-wind-infrastructure/context.jsonld",
  "id": "https://example.org/norwegian-ses/floating-wind-infrastructure/utsira-nord-60x15mw",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          4.4,
          59.2
        ],
        [
          5.1,
          59.2
        ],
        [
          5.1,
          59.55
        ],
        [
          4.4,
          59.55
        ],
        [
          4.4,
          59.2
        ]
      ]
    ]
  },
  "properties": {
    "type": "Dataset",
    "title": "Submerged infrastructure layout \u2014 Utsira Nord 60 \u00d7 15 MW",
    "description": "Per-unit submerged geometry (wetted hull + mooring + anchor surfaces) for the 60 \u00d7 15 MW floating-wind units of the Utsira Nord engineering design. Drives the A_sub calculation in the reef-biomass equation.",
    "created": "2026-05-18",
    "updated": "2026-05-19",
    "language": {
      "code": "en"
    },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "themes": [
      {
        "concepts": [
          {
            "id": "floating-wind",
            "label": "Floating wind infrastructure"
          }
        ],
        "scheme": "https://id3.seadots.eu/themes"
      }
    ],
    "keywords": [
      "infrastructure",
      "floating-wind",
      "Utsira Nord",
      "submerged area"
    ],
    "formats": [
      {
        "mediaType": "application/geo+json"
      }
    ],
    "floatingWindInfrastructure": {
      "name": "Submerged infrastructure layout \u2014 Utsira Nord 60 \u00d7 15 MW",
      "description": "Per-unit submerged geometry for the floating-wind units intersecting the AOI.",
      "role": "feature-of-interest geometry",
      "source": "infrastructure/utsira_nord_60x15mw.geojson",
      "format": "application/geo+json",
      "vocabularyTerm": "https://id3.seadots.eu/indicator/submerged-infrastructure-area-utsira-design",
      "data": {
        "unitDesign": "15 MW semi-submersible (3-column hull, 3-point catenary mooring, drag-embedment anchors)",
        "nUnits": 60,
        "perUnit": {
          "hull_area_m2": 1450,
          "mooring_area_m2": 280,
          "anchor_area_m2": 95,
          "submerged_area_total_m2": 1825,
          "depth_range_m": [
            200,
            280
          ]
        },
        "aggregate": {
          "submerged_area_total_m2": 109500,
          "submerged_area_total_km2": 0.1095
        },
        "sampleUnits": [
          {
            "unit_id": "U01",
            "lon": 4.552,
            "lat": 59.3812,
            "submerged_area_m2": 1825
          },
          {
            "unit_id": "U02",
            "lon": 4.578,
            "lat": 59.3812,
            "submerged_area_m2": 1825
          },
          {
            "unit_id": "U03",
            "lon": 4.604,
            "lat": 59.3812,
            "submerged_area_m2": 1825
          }
        ],
        "units": "m2",
        "provenance": {
          "values": "mixed",
          "note": "`unitDesign=15 MW semi-submersible` and `nUnits=60` match the publicly stated Utsira Nord engineering envelope (NVE strategic assessment). Per-unit surface areas (1450 / 280 / 95 m\u00b2), depth range, sample unit coordinates and the 109,500 m\u00b2 aggregate are ILLUSTRATIVE \u2014 actual wetted areas depend on platform-supplier engineering drawings that are not in the public domain.",
          "primarySource": {
            "url": "https://veiledere.nve.no/havvind/strategisk-konsekvensutredning-av-vindkraft-til-havs/",
            "title": "NVE Strategisk konsekvensutredning av vindkraft til havs (covers `nUnits` and `unitDesign` only)"
          },
          "nearestAuthoritativeSource": {
            "url": "https://www.equinor.com/energy/hywind-tampen",
            "note": "Hywind Tampen 11\u00d78.6 MW spar-buoy is the closest deployed Norwegian floating-wind asset with public-domain geometry; the Utsira Nord 15 MW semi-submersible has different surface areas. Use only for orientation."
          }
        }
      }
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.floating-wind-infrastructure",
      "type": "application/schema+json",
      "title": "Floating-Wind Submerged Infrastructure bblock"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.iliad.api.features.oim",
      "type": "application/schema+json",
      "title": "OIM feature profile"
    },
    {
      "rel": "cite-as",
      "href": "https://veiledere.nve.no/havvind/strategisk-konsekvensutredning-av-vindkraft-til-havs/",
      "title": "NVE strategic assessment \u2014 Utsira Nord design source"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix indo: <https://id3.seadots.eu/indicator/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/norwegian-ses/floating-wind-infrastructure/utsira-nord-60x15mw> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Floating-Wind Submerged Infrastructure bblock" ;
            dcterms:format "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.floating-wind-infrastructure> ],
        [ rdfs:label "NVE strategic assessment — Utsira Nord design source" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://veiledere.nve.no/havvind/strategisk-konsekvensutredning-av-vindkraft-til-havs/> ],
        [ rdfs:label "OIM feature profile" ;
            dcterms:format "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/profile> ;
            oa:hasTarget <bblocks://ogc.hosted.iliad.api.features.oim> ] ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 4.4e+00 5.92e+01 ) ( 5.1e+00 5.92e+01 ) ( 5.1e+00 5.955e+01 ) ( 4.4e+00 5.955e+01 ) ( 4.4e+00 5.92e+01 ) ) ) ] ;
    geojson:properties [ a seadots:Dataset ;
            dcterms:created "2026-05-18" ;
            dcterms:description "Per-unit submerged geometry (wetted hull + mooring + anchor surfaces) for the 60 × 15 MW floating-wind units of the Utsira Nord engineering design. Drives the A_sub calculation in the reef-biomass equation." ;
            dcterms:license "https://creativecommons.org/licenses/by/4.0/" ;
            dcterms:modified "2026-05-19" ;
            dcterms:title "Submerged infrastructure layout — Utsira Nord 60 × 15 MW" ;
            dcat:keyword "Utsira Nord",
                "floating-wind",
                "infrastructure",
                "submerged area" ;
            seadots:floatingWindInfrastructure [ dcterms:description "Per-unit submerged geometry for the floating-wind units intersecting the AOI." ;
                    dcterms:format "application/geo+json" ;
                    dcterms:title "Submerged infrastructure layout — Utsira Nord 60 × 15 MW" ;
                    skos:exactMatch indo:submerged-infrastructure-area-utsira-design ;
                    dcat:accessURL <file:///github/workspace/infrastructure/utsira_nord_60x15mw.geojson> ;
                    seadots:data [ qudt:unit "m2" ;
                            prov:wasDerivedFrom [ dcterms:source [ dcterms:title "NVE Strategisk konsekvensutredning av vindkraft til havs (covers `nUnits` and `unitDesign` only)" ;
                                            dcat:accessURL <https://veiledere.nve.no/havvind/strategisk-konsekvensutredning-av-vindkraft-til-havs/> ] ;
                                    skos:note "`unitDesign=15 MW semi-submersible` and `nUnits=60` match the publicly stated Utsira Nord engineering envelope (NVE strategic assessment). Per-unit surface areas (1450 / 280 / 95 m²), depth range, sample unit coordinates and the 109,500 m² aggregate are ILLUSTRATIVE — actual wetted areas depend on platform-supplier engineering drawings that are not in the public domain." ;
                                    seadots:nearestAuthoritativeSource [ skos:note "Hywind Tampen 11×8.6 MW spar-buoy is the closest deployed Norwegian floating-wind asset with public-domain geometry; the Utsira Nord 15 MW semi-submersible has different surface areas. Use only for orientation." ;
                                            dcat:accessURL <https://www.equinor.com/energy/hywind-tampen> ] ;
                                    seadots:provenanceValues "mixed" ] ;
                            seadots:aggregate [ indo:submerged-infrastructure-area "109500"^^qudt:QuantityValue ;
                                    seadots:submergedAreaTotal_km2 "0.1095"^^qudt:QuantityValue ] ;
                            seadots:nUnits 60 ;
                            seadots:perUnit [ indo:submerged-infrastructure-area "1825"^^qudt:QuantityValue ;
                                    seadots:anchorArea_m2 "95"^^qudt:QuantityValue ;
                                    seadots:depthRange_m 200,
                                        280 ;
                                    seadots:hullArea_m2 "1450"^^qudt:QuantityValue ;
                                    seadots:mooringArea_m2 "280"^^qudt:QuantityValue ] ;
                            seadots:sampleUnit [ dcterms:identifier "U01" ;
                                    geojson:latitude 5.93812e+01 ;
                                    geojson:longitude 4.552e+00 ;
                                    seadots:submergedArea_m2 "1825"^^qudt:QuantityValue ],
                                [ dcterms:identifier "U03" ;
                                    geojson:latitude 5.93812e+01 ;
                                    geojson:longitude 4.604e+00 ;
                                    seadots:submergedArea_m2 "1825"^^qudt:QuantityValue ],
                                [ dcterms:identifier "U02" ;
                                    geojson:latitude 5.93812e+01 ;
                                    geojson:longitude 4.578e+00 ;
                                    seadots:submergedArea_m2 "1825"^^qudt:QuantityValue ] ;
                            seadots:unitDesign "15 MW semi-submersible (3-column hull, 3-point catenary mooring, drag-embedment anchors)" ] ;
                    seadots:role "feature-of-interest geometry" ] ;
            rec:format [ dcterms:format "application/geo+json" ] ;
            rec:language [ rec:languageCode "en" ] ;
            rec:themes [ rec:concept [ skos:prefLabel "Floating wind infrastructure" ;
                            rec:conceptID "floating-wind"^^xsd:string ] ;
                    rec:scheme "https://id3.seadots.eu/themes" ] ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Floating-Wind Submerged Infrastructure
description: 'Per-unit submerged geometry of a floating-wind farm layout, plus aggregate
  submerged area (`A_sub`) used as feature-of-interest input to the reef-biomass equation.

  '
allOf:
- $ref: https://ogcincubator.github.io/geodcat-ogcapi-records/build/annotated/geo/geodcat/geodcat-records/schema.yaml
properties:
  properties:
    type: object
    required:
    - floatingWindInfrastructure
    properties:
      floatingWindInfrastructure:
        type: object
        required:
        - name
        - source
        - format
        - data
        properties:
          name:
            type: string
            x-jsonld-id: http://purl.org/dc/terms/title
          description:
            type: string
            x-jsonld-id: http://purl.org/dc/terms/description
          role:
            type: string
            description: Usually `feature-of-interest geometry`.
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#role
          source:
            type: string
            x-jsonld-id: http://www.w3.org/ns/dcat#accessURL
            x-jsonld-type: '@id'
          format:
            type: string
            x-jsonld-id: http://purl.org/dc/terms/format
          vocabularyTerm:
            type: string
            format: uri
            x-jsonld-id: http://www.w3.org/2004/02/skos/core#exactMatch
            x-jsonld-type: '@id'
          data:
            type: object
            required:
            - nUnits
            - perUnit
            - aggregate
            - provenance
            properties:
              unitDesign:
                type: string
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#unitDesign
              nUnits:
                type: integer
                minimum: 1
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#nUnits
              perUnit:
                type: object
                required:
                - submerged_area_total_m2
                properties:
                  hull_area_m2:
                    type: number
                    minimum: 0
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#hullArea_m2
                    x-jsonld-type: http://qudt.org/schema/qudt/QuantityValue
                  mooring_area_m2:
                    type: number
                    minimum: 0
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#mooringArea_m2
                    x-jsonld-type: http://qudt.org/schema/qudt/QuantityValue
                  anchor_area_m2:
                    type: number
                    minimum: 0
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#anchorArea_m2
                    x-jsonld-type: http://qudt.org/schema/qudt/QuantityValue
                  submerged_area_total_m2:
                    type: number
                    minimum: 0
                    x-jsonld-id: https://id3.seadots.eu/indicator/submerged-infrastructure-area
                    x-jsonld-type: http://qudt.org/schema/qudt/QuantityValue
                  depth_range_m:
                    type: array
                    items:
                      type: number
                    minItems: 2
                    maxItems: 2
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#depthRange_m
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#perUnit
              aggregate:
                type: object
                required:
                - submerged_area_total_m2
                properties:
                  submerged_area_total_m2:
                    type: number
                    minimum: 0
                    description: Consumed as `A_sub` by the reef-biomass equation.
                    x-jsonld-id: https://id3.seadots.eu/indicator/submerged-infrastructure-area
                    x-jsonld-type: http://qudt.org/schema/qudt/QuantityValue
                  submerged_area_total_km2:
                    type: number
                    minimum: 0
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#submergedAreaTotal_km2
                    x-jsonld-type: http://qudt.org/schema/qudt/QuantityValue
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#aggregate
              sampleUnits:
                type: array
                items:
                  type: object
                  required:
                  - unit_id
                  properties:
                    unit_id:
                      type: string
                      x-jsonld-id: http://purl.org/dc/terms/identifier
                    lon:
                      type: number
                      x-jsonld-id: https://purl.org/geojson/vocab#longitude
                    lat:
                      type: number
                      x-jsonld-id: https://purl.org/geojson/vocab#latitude
                    submerged_area_m2:
                      type: number
                      minimum: 0
                      x-jsonld-id: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#submergedArea_m2
                      x-jsonld-type: http://qudt.org/schema/qudt/QuantityValue
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#sampleUnit
                x-jsonld-container: '@set'
              units:
                type: string
                description: Default units of the area quantities, e.g. m2.
                x-jsonld-id: http://qudt.org/schema/qudt/unit
              provenance:
                type: object
                required:
                - values
                properties:
                  values:
                    type: string
                    enum:
                    - retrieved
                    - illustrative
                    - mixed
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#provenanceValues
                  note:
                    type: string
                    x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
                  primarySource:
                    type: object
                    properties:
                      url:
                        type: string
                        format: uri
                        x-jsonld-id: http://www.w3.org/ns/dcat#accessURL
                        x-jsonld-type: '@id'
                      title:
                        type: string
                        x-jsonld-id: http://purl.org/dc/terms/title
                      citation:
                        type: string
                      doi:
                        type: string
                      supportingFigure:
                        type: string
                    x-jsonld-id: http://purl.org/dc/terms/source
                  nearestAuthoritativeSource:
                    type: object
                    properties:
                      url:
                        type: string
                        format: uri
                        x-jsonld-id: http://www.w3.org/ns/dcat#accessURL
                        x-jsonld-type: '@id'
                      note:
                        type: string
                        x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#nearestAuthoritativeSource
                  retrievalApiCall:
                    type: string
                  verifiedOn:
                    type: string
                    format: date
                  verificationGap:
                    type: string
                x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#data
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#floatingWindInfrastructure
    x-jsonld-id: https://purl.org/geojson/vocab#properties
x-jsonld-extra-terms:
  id: '@id'
  type: '@type'
  geometry: https://purl.org/geojson/vocab#geometry
  coordinates: https://purl.org/geojson/vocab#coordinates
  Feature: https://purl.org/geojson/vocab#Feature
  Polygon: https://purl.org/geojson/vocab#Polygon
  links:
    x-jsonld-id: http://www.w3.org/ns/iana/link-relations/relation
    x-jsonld-container: '@set'
  href: '@id'
  rel: https://purl.org/geojson/vocab#rel
  created: http://purl.org/dc/terms/created
  updated: http://purl.org/dc/terms/modified
  language: http://purl.org/dc/terms/language
  license: http://purl.org/dc/terms/license
  keywords:
    x-jsonld-id: http://www.w3.org/ns/dcat#keyword
    x-jsonld-container: '@set'
  themes:
    x-jsonld-id: http://www.w3.org/ns/dcat#theme
    x-jsonld-container: '@set'
  concepts:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#Concept
    x-jsonld-container: '@set'
  scheme: http://www.w3.org/2004/02/skos/core#inScheme
  label: http://www.w3.org/2004/02/skos/core#prefLabel
  formats:
    x-jsonld-id: http://purl.org/dc/terms/format
    x-jsonld-container: '@set'
  mediaType: http://purl.org/dc/terms/format
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#
x-jsonld-prefixes:
  dcterms: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#
  skos: http://www.w3.org/2004/02/skos/core#
  seadots: https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#
  qudt: http://qudt.org/schema/qudt/
  indo: https://id3.seadots.eu/indicator/
  prov: http://www.w3.org/ns/prov#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/floating-wind-infrastructure/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/floating-wind-infrastructure/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#",
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
        "floatingWindInfrastructure": {
          "@context": {
            "name": "dct:title",
            "role": "seadots:role",
            "source": {
              "@id": "dcat:accessURL",
              "@type": "@id"
            },
            "format": "dct:format",
            "vocabularyTerm": {
              "@id": "skos:exactMatch",
              "@type": "@id"
            },
            "data": {
              "@context": {
                "unitDesign": "seadots:unitDesign",
                "nUnits": "seadots:nUnits",
                "perUnit": {
                  "@context": {
                    "hull_area_m2": {
                      "@id": "seadots:hullArea_m2",
                      "@type": "qudt:QuantityValue"
                    },
                    "mooring_area_m2": {
                      "@id": "seadots:mooringArea_m2",
                      "@type": "qudt:QuantityValue"
                    },
                    "anchor_area_m2": {
                      "@id": "seadots:anchorArea_m2",
                      "@type": "qudt:QuantityValue"
                    },
                    "submerged_area_total_m2": {
                      "@id": "indo:submerged-infrastructure-area",
                      "@type": "qudt:QuantityValue"
                    },
                    "depth_range_m": "seadots:depthRange_m"
                  },
                  "@id": "seadots:perUnit"
                },
                "aggregate": {
                  "@context": {
                    "submerged_area_total_m2": {
                      "@id": "indo:submerged-infrastructure-area",
                      "@type": "qudt:QuantityValue"
                    },
                    "submerged_area_total_km2": {
                      "@id": "seadots:submergedAreaTotal_km2",
                      "@type": "qudt:QuantityValue"
                    }
                  },
                  "@id": "seadots:aggregate"
                },
                "sampleUnits": {
                  "@context": {
                    "unit_id": "dct:identifier",
                    "lon": "geojson:longitude",
                    "lat": "geojson:latitude",
                    "submerged_area_m2": {
                      "@id": "seadots:submergedArea_m2",
                      "@type": "qudt:QuantityValue"
                    }
                  },
                  "@id": "seadots:sampleUnit",
                  "@container": "@set"
                },
                "units": "qudt:unit",
                "provenance": {
                  "@context": {
                    "values": "seadots:provenanceValues",
                    "note": "skos:note",
                    "primarySource": {
                      "@context": {
                        "url": {
                          "@id": "dcat:accessURL",
                          "@type": "@id"
                        }
                      },
                      "@id": "dct:source"
                    },
                    "nearestAuthoritativeSource": {
                      "@context": {
                        "url": {
                          "@id": "dcat:accessURL",
                          "@type": "@id"
                        }
                      },
                      "@id": "seadots:nearestAuthoritativeSource"
                    }
                  },
                  "@id": "prov:wasDerivedFrom"
                }
              },
              "@id": "seadots:data"
            }
          },
          "@id": "seadots:floatingWindInfrastructure"
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
    "href": "@id",
    "rel": "geojson:rel",
    "concepts": {
      "@id": "skos:Concept",
      "@container": "@set"
    },
    "scheme": "skos:inScheme",
    "label": "skos:prefLabel",
    "mediaType": "dct:format",
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
    "seadots": "https://w3id.org/ogc/hosted/seadots/floating-wind-infrastructure#",
    "qudt": "http://qudt.org/schema/qudt/",
    "indo": "https://id3.seadots.eu/indicator/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/floating-wind-infrastructure/context.jsonld)

## Sources

* [NVE strategisk konsekvensutredning av vindkraft til havs](https://veiledere.nve.no/havvind/strategisk-konsekvensutredning-av-vindkraft-til-havs/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/floating-wind-infrastructure`

