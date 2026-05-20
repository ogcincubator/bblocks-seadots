
# MAREANO Benthic Biomass Density Observation (Schema)

`ogc.hosted.seadots.benthic-biomass-density-mareano` *v0.1*

OGC Feature + SOSA observation profile for per-taxon benthic biomass density (kg m-2) derived from the MAREANO programme. Each record is a SOSA Observation of `benthic-biomass-density` over a polygon footprint and a sampling period, with the per-taxon values carried inline by `data.perTaxon[]` and mandatory provenance describing whether the values are retrieved or illustrative.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# MAREANO Benthic Biomass Density Observation

OGC Feature + SOSA Observation profile for per-taxon benthic biomass density (kg m⁻²) sourced from the MAREANO programme.

Each record is a SOSA Observation:
- `sosa:observedProperty` → `indo:benthic-biomass-density-mareano`
- `sosa:hasFeatureOfInterest` → the AOI polygon URI (or inline polygon)
- `sosa:phenomenonTime` → the sampling period
- `sosa:hasResult` → the structured `data.perTaxon[]` array

`data.perTaxon[]` rows carry `scientificName`, `aphiaID` (WoRMS), `density_kg_m2`, `habitat`, `depthBand_m`, `nSamples`. `data.aggregateDensity_kg_m2` is the sum-over-taxa convenience scalar.

## Dependency

Extends `ogc.hosted.iliad.api.features.oim-obs` (SOSA observation profile in iliad-apis-features).

## Required fields for script consumption

The calculator `_sources/experiment/scripts/utsira_reef_biomass.py` reads `data.perTaxon[].scientificName` and `data.perTaxon[].density_kg_m2` to populate `D_pre,i`. Both are marked `required` in the schema.

## Retrieval

MAREANO does not expose a single REST endpoint that returns per-taxon biomass density aggregated over an arbitrary AOI. The realistic retrieval path is the OBIS occurrence API (per-record observations, aggregated off-line) — recorded under `data.provenance.nearestAuthoritativeSource`.

## Examples

### MAREANO benthic biomass density — Norwegian shelf
#### json
```json
{
  "id": "https://example.org/norwegian-ses/benthic-biomass-density-mareano/norwegian-shelf",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-5.0, 56.0],
      [33.0, 56.0],
      [33.0, 82.0],
      [-5.0, 82.0],
      [-5.0, 56.0]
    ]]
  },
  "properties": {
    "type": "Dataset",
    "title": "MAREANO benthic biomass density — primary baseline (D_{pre,i})",
    "description": "MAREANO programme baseline benthic biomass density rasters, queried per AOI cell and scattered over taxon groups by index i. Provides the primary D_{pre,i} binding for the reef-biomass equation. Coverage: Norwegian shelf.",
    "created": "2026-05-18",
    "updated": "2026-05-19",
    "language": { "code": "en" },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "themes": [{ "concepts": [{ "id": "benthic-biomass", "label": "Benthic biomass density" }], "scheme": "https://id3.seadots.eu/themes" }],
    "keywords": ["MAREANO", "benthic biomass", "Norwegian shelf", "baseline"],
    "formats": [{ "mediaType": "application/x-netcdf" }],
    "conformsTo": [
      "http://www.w3.org/ns/sosa/Observation",
      "https://ogcincubator.github.io/geodcat-ogcapi-records/"
    ],
    "benthicBiomassDensity": {
      "name": "MAREANO benthic biomass density",
      "description": "Primary baseline benthic biomass density before installation. Scattered over taxon index i.",
      "role": "primary baseline",
      "source": "https://mareano.no/api/benthic-biomass-density",
      "format": "application/x-netcdf",
      "vocabularyTerm": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano",
      "observedProperty": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano",
      "phenomenonTime": "2018-01-01/2024-12-31",
      "data": {
        "units": "kg m-2",
        "samplePeriod": "2018-2024",
        "samplingProgramme": "MAREANO",
        "perTaxon": [
          { "scientificName": "Mytilus edulis",   "aphiaID": 140480, "density_kg_m2": 0.42, "habitat": "rocky-subtidal", "depthBand_m": "0-30",  "nSamples": 178 },
          { "scientificName": "Buccinum undatum", "aphiaID": 138878, "density_kg_m2": 0.11, "habitat": "soft-sediment",  "depthBand_m": "30-100","nSamples": 64  },
          { "scientificName": "Asterias rubens",  "aphiaID": 123776, "density_kg_m2": 0.28, "habitat": "mixed",          "depthBand_m": "0-100", "nSamples": 122 }
        ],
        "aggregateDensity_kg_m2": 0.81,
        "provenance": {
          "values": "illustrative",
          "note": "Density values (kg/m²), aggregate density, sample counts, depth bands and habitat tags above are ILLUSTRATIVE placeholders. NOT MAREANO measurements. AphiaIDs are real (WoRMS) and scientificName is correct, but the per-taxon density numbers have no MAREANO provenance.",
          "nearestAuthoritativeSource": {
            "url": "https://api.obis.org/v3/occurrence?scientificname=Mytilus%20edulis&geometry=POLYGON((4.20%2059.10,5.30%2059.10,5.30%2059.70,4.20%2059.70,4.20%2059.10))&size=500",
            "note": "OBIS occurrence API returns per-record observations inside the AOI polygon. Repeat per taxon (Mytilus 140480, Buccinum 138878, Asterias 123776) and aggregate to obtain a real per-taxon density estimate."
          },
          "verificationGap": "OBIS endpoint shape verified; aggregation pipeline from per-occurrence records to kg/m² density NOT verified to match what MAREANO publishes internally."
        }
      }
    }
  },
  "links": [
    { "rel": "describedby", "href": "bblocks://ogc.hosted.seadots.benthic-biomass-density-mareano", "type": "application/schema+json", "title": "MAREANO Benthic Biomass Density Observation bblock" },
    { "rel": "profile", "href": "bblocks://ogc.hosted.iliad.api.features.oim-obs", "type": "application/schema+json", "title": "OIM Observations profile" },
    { "rel": "cite-as", "href": "https://mareano.no/", "title": "MAREANO programme" }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/benthic-biomass-density-mareano/context.jsonld",
  "id": "https://example.org/norwegian-ses/benthic-biomass-density-mareano/norwegian-shelf",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -5.0,
          56.0
        ],
        [
          33.0,
          56.0
        ],
        [
          33.0,
          82.0
        ],
        [
          -5.0,
          82.0
        ],
        [
          -5.0,
          56.0
        ]
      ]
    ]
  },
  "properties": {
    "type": "Dataset",
    "title": "MAREANO benthic biomass density \u2014 primary baseline (D_{pre,i})",
    "description": "MAREANO programme baseline benthic biomass density rasters, queried per AOI cell and scattered over taxon groups by index i. Provides the primary D_{pre,i} binding for the reef-biomass equation. Coverage: Norwegian shelf.",
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
            "id": "benthic-biomass",
            "label": "Benthic biomass density"
          }
        ],
        "scheme": "https://id3.seadots.eu/themes"
      }
    ],
    "keywords": [
      "MAREANO",
      "benthic biomass",
      "Norwegian shelf",
      "baseline"
    ],
    "formats": [
      {
        "mediaType": "application/x-netcdf"
      }
    ],
    "conformsTo": [
      "http://www.w3.org/ns/sosa/Observation",
      "https://ogcincubator.github.io/geodcat-ogcapi-records/"
    ],
    "benthicBiomassDensity": {
      "name": "MAREANO benthic biomass density",
      "description": "Primary baseline benthic biomass density before installation. Scattered over taxon index i.",
      "role": "primary baseline",
      "source": "https://mareano.no/api/benthic-biomass-density",
      "format": "application/x-netcdf",
      "vocabularyTerm": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano",
      "observedProperty": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano",
      "phenomenonTime": "2018-01-01/2024-12-31",
      "data": {
        "units": "kg m-2",
        "samplePeriod": "2018-2024",
        "samplingProgramme": "MAREANO",
        "perTaxon": [
          {
            "scientificName": "Mytilus edulis",
            "aphiaID": 140480,
            "density_kg_m2": 0.42,
            "habitat": "rocky-subtidal",
            "depthBand_m": "0-30",
            "nSamples": 178
          },
          {
            "scientificName": "Buccinum undatum",
            "aphiaID": 138878,
            "density_kg_m2": 0.11,
            "habitat": "soft-sediment",
            "depthBand_m": "30-100",
            "nSamples": 64
          },
          {
            "scientificName": "Asterias rubens",
            "aphiaID": 123776,
            "density_kg_m2": 0.28,
            "habitat": "mixed",
            "depthBand_m": "0-100",
            "nSamples": 122
          }
        ],
        "aggregateDensity_kg_m2": 0.81,
        "provenance": {
          "values": "illustrative",
          "note": "Density values (kg/m\u00b2), aggregate density, sample counts, depth bands and habitat tags above are ILLUSTRATIVE placeholders. NOT MAREANO measurements. AphiaIDs are real (WoRMS) and scientificName is correct, but the per-taxon density numbers have no MAREANO provenance.",
          "nearestAuthoritativeSource": {
            "url": "https://api.obis.org/v3/occurrence?scientificname=Mytilus%20edulis&geometry=POLYGON((4.20%2059.10,5.30%2059.10,5.30%2059.70,4.20%2059.70,4.20%2059.10))&size=500",
            "note": "OBIS occurrence API returns per-record observations inside the AOI polygon. Repeat per taxon (Mytilus 140480, Buccinum 138878, Asterias 123776) and aggregate to obtain a real per-taxon density estimate."
          },
          "verificationGap": "OBIS endpoint shape verified; aggregation pipeline from per-occurrence records to kg/m\u00b2 density NOT verified to match what MAREANO publishes internally."
        }
      }
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.benthic-biomass-density-mareano",
      "type": "application/schema+json",
      "title": "MAREANO Benthic Biomass Density Observation bblock"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.iliad.api.features.oim-obs",
      "type": "application/schema+json",
      "title": "OIM Observations profile"
    },
    {
      "rel": "cite-as",
      "href": "https://mareano.no/",
      "title": "MAREANO programme"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix dwc: <http://rs.tdwg.org/dwc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix indo: <https://w3id.org/indicators/marine/obs/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/norwegian-ses/benthic-biomass-density-mareano/norwegian-shelf> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "MAREANO programme" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://mareano.no/> ],
        [ rdfs:label "MAREANO Benthic Biomass Density Observation bblock" ;
            dcterms:format "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.benthic-biomass-density-mareano> ],
        [ rdfs:label "OIM Observations profile" ;
            dcterms:format "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/profile> ;
            oa:hasTarget <bblocks://ogc.hosted.iliad.api.features.oim-obs> ] ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -5e+00 5.6e+01 ) ( 3.3e+01 5.6e+01 ) ( 3.3e+01 8.2e+01 ) ( -5e+00 8.2e+01 ) ( -5e+00 5.6e+01 ) ) ) ] ;
    geojson:properties [ a seadots:Dataset ;
            dcterms:conformsTo sosa:Observation,
                <https://ogcincubator.github.io/geodcat-ogcapi-records/> ;
            dcterms:created "2026-05-18" ;
            dcterms:description "MAREANO programme baseline benthic biomass density rasters, queried per AOI cell and scattered over taxon groups by index i. Provides the primary D_{pre,i} binding for the reef-biomass equation. Coverage: Norwegian shelf." ;
            dcterms:license "https://creativecommons.org/licenses/by/4.0/" ;
            dcterms:modified "2026-05-19" ;
            dcterms:title "MAREANO benthic biomass density — primary baseline (D_{pre,i})" ;
            dcat:keyword "MAREANO",
                "Norwegian shelf",
                "baseline",
                "benthic biomass" ;
            seadots:benthicBiomassDensity [ dcterms:description "Primary baseline benthic biomass density before installation. Scattered over taxon index i." ;
                    dcterms:format "application/x-netcdf" ;
                    dcterms:title "MAREANO benthic biomass density" ;
                    skos:exactMatch indo:benthic-biomass-density-mareano ;
                    dcat:accessURL <https://mareano.no/api/benthic-biomass-density> ;
                    sosa:observedProperty indo:benthic-biomass-density-mareano ;
                    sosa:phenomenonTime "2018-01-01/2024-12-31" ;
                    seadots:data [ dcterms:temporal "2018-2024" ;
                            qudt:unit "kg m-2" ;
                            prov:wasAttributedTo "MAREANO" ;
                            prov:wasDerivedFrom [ skos:note "Density values (kg/m²), aggregate density, sample counts, depth bands and habitat tags above are ILLUSTRATIVE placeholders. NOT MAREANO measurements. AphiaIDs are real (WoRMS) and scientificName is correct, but the per-taxon density numbers have no MAREANO provenance." ;
                                    seadots:nearestAuthoritativeSource [ skos:note "OBIS occurrence API returns per-record observations inside the AOI polygon. Repeat per taxon (Mytilus 140480, Buccinum 138878, Asterias 123776) and aggregate to obtain a real per-taxon density estimate." ;
                                            dcat:accessURL <https://api.obis.org/v3/occurrence?scientificname=Mytilus%20edulis&geometry=POLYGON((4.20%2059.10,5.30%2059.10,5.30%2059.70,4.20%2059.70,4.20%2059.10))&size=500> ] ;
                                    seadots:provenanceValues "illustrative" ;
                                    seadots:verificationGap "OBIS endpoint shape verified; aggregation pipeline from per-occurrence records to kg/m² density NOT verified to match what MAREANO publishes internally." ] ;
                            indo:baseline-benthic-biomass-density "0.81"^^qudt:QuantityValue ;
                            seadots:perTaxon [ dwc:habitat "rocky-subtidal" ;
                                    dwc:sampleSizeValue 178 ;
                                    dwc:scientificName "Mytilus edulis" ;
                                    dwc:taxonID 140480 ;
                                    indo:benthic-biomass-density-mareano "0.42"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "0-30" ],
                                [ dwc:habitat "soft-sediment" ;
                                    dwc:sampleSizeValue 64 ;
                                    dwc:scientificName "Buccinum undatum" ;
                                    dwc:taxonID 138878 ;
                                    indo:benthic-biomass-density-mareano "0.11"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "30-100" ],
                                [ dwc:habitat "mixed" ;
                                    dwc:sampleSizeValue 122 ;
                                    dwc:scientificName "Asterias rubens" ;
                                    dwc:taxonID 123776 ;
                                    indo:benthic-biomass-density-mareano "0.28"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "0-100" ] ] ;
                    seadots:role "primary baseline" ] ;
            rec:format [ dcterms:format "application/x-netcdf" ] ;
            rec:language [ rec:languageCode "en" ] ;
            rec:themes [ rec:concept [ skos:prefLabel "Benthic biomass density" ;
                            rec:conceptID "benthic-biomass"^^xsd:string ] ;
                    rec:scheme "https://id3.seadots.eu/themes" ] ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: MAREANO Benthic Biomass Density Observation
description: 'Per-taxon benthic biomass density observation sourced from the MAREANO
  programme. Treated as a SOSA Observation: feature-of-interest is the observed footprint,
  observed property is `indo:benthic-biomass-density-mareano`, and the result is the
  `data.perTaxon[]` array.

  '
allOf:
- $ref: https://ogcincubator.github.io/geodcat-ogcapi-records/build/annotated/geo/geodcat/geodcat-records/schema.yaml
properties:
  properties:
    type: object
    required:
    - benthicBiomassDensity
    properties:
      benthicBiomassDensity:
        type: object
        required:
        - name
        - source
        - format
        - observedProperty
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
            description: Usually `primary baseline`.
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#role
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
          observedProperty:
            type: string
            format: uri
            description: SOSA observed-property URI (`indo:benthic-biomass-density-mareano`).
            x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
            x-jsonld-type: '@id'
          phenomenonTime:
            description: "SOSA phenomenon time \u2014 typically the sampling period."
            oneOf:
            - type: string
            - type: object
            x-jsonld-id: http://www.w3.org/ns/sosa/phenomenonTime
          data:
            type: object
            required:
            - perTaxon
            - provenance
            properties:
              units:
                type: string
                description: Units of density (kg m-2).
                x-jsonld-id: http://qudt.org/schema/qudt/unit
              samplePeriod:
                type: string
                x-jsonld-id: http://purl.org/dc/terms/temporal
              samplingProgramme:
                type: string
                x-jsonld-id: http://www.w3.org/ns/prov#wasAttributedTo
              perTaxon:
                type: array
                items:
                  type: object
                  required:
                  - scientificName
                  - density_kg_m2
                  properties:
                    scientificName:
                      type: string
                      x-jsonld-id: http://rs.tdwg.org/dwc/terms/scientificName
                    aphiaID:
                      type: integer
                      description: WoRMS AphiaID.
                      x-jsonld-id: http://rs.tdwg.org/dwc/terms/taxonID
                    density_kg_m2:
                      type: number
                      minimum: 0
                      description: Per-taxon density consumed as `D_pre,i`.
                      x-jsonld-id: https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano
                      x-jsonld-type: http://qudt.org/schema/qudt/QuantityValue
                    habitat:
                      type: string
                      x-jsonld-id: http://rs.tdwg.org/dwc/terms/habitat
                    depthBand_m:
                      type: string
                      x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#depthBand_m
                    nSamples:
                      type: integer
                      minimum: 0
                      x-jsonld-id: http://rs.tdwg.org/dwc/terms/sampleSizeValue
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#perTaxon
                x-jsonld-container: '@set'
              aggregateDensity_kg_m2:
                type: number
                minimum: 0
                x-jsonld-id: https://w3id.org/indicators/marine/obs/baseline-benthic-biomass-density
                x-jsonld-type: http://qudt.org/schema/qudt/QuantityValue
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
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#provenanceValues
                  retrievalApiCall:
                    type: string
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#retrievalApiCall
                    x-jsonld-type: '@id'
                  verifiedOn:
                    type: string
                    format: date
                    x-jsonld-id: http://purl.org/dc/terms/date
                  primarySource:
                    type: object
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
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#nearestAuthoritativeSource
                  verificationGap:
                    type: string
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#verificationGap
                  note:
                    type: string
                    x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
                x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#data
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#benthicBiomassDensity
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
  title: http://purl.org/dc/terms/title
  created: http://purl.org/dc/terms/created
  updated: http://purl.org/dc/terms/modified
  language: http://purl.org/dc/terms/language
  code: http://purl.org/dc/terms/identifier
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
  conformsTo:
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
    x-jsonld-container: '@set'
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#
x-jsonld-prefixes:
  dcterms: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#
  skos: http://www.w3.org/2004/02/skos/core#
  seadots: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#
  sosa: http://www.w3.org/ns/sosa/
  qudt: http://qudt.org/schema/qudt/
  prov: http://www.w3.org/ns/prov#
  dwc: http://rs.tdwg.org/dwc/terms/
  indo: https://w3id.org/indicators/marine/obs/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/benthic-biomass-density-mareano/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/benthic-biomass-density-mareano/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#",
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
        "benthicBiomassDensity": {
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
            "observedProperty": {
              "@id": "sosa:observedProperty",
              "@type": "@id"
            },
            "phenomenonTime": "sosa:phenomenonTime",
            "data": {
              "@context": {
                "units": "qudt:unit",
                "samplePeriod": "dct:temporal",
                "samplingProgramme": "prov:wasAttributedTo",
                "perTaxon": {
                  "@context": {
                    "scientificName": "dwc:scientificName",
                    "aphiaID": "dwc:taxonID",
                    "density_kg_m2": {
                      "@id": "indo:benthic-biomass-density-mareano",
                      "@type": "qudt:QuantityValue"
                    },
                    "habitat": "dwc:habitat",
                    "depthBand_m": "seadots:depthBand_m",
                    "nSamples": "dwc:sampleSizeValue"
                  },
                  "@id": "seadots:perTaxon",
                  "@container": "@set"
                },
                "aggregateDensity_kg_m2": {
                  "@id": "indo:baseline-benthic-biomass-density",
                  "@type": "qudt:QuantityValue"
                },
                "provenance": {
                  "@context": {
                    "values": "seadots:provenanceValues",
                    "retrievalApiCall": {
                      "@id": "seadots:retrievalApiCall",
                      "@type": "@id"
                    },
                    "verifiedOn": "dct:date",
                    "primarySource": "dct:source",
                    "nearestAuthoritativeSource": {
                      "@context": {
                        "url": {
                          "@id": "dcat:accessURL",
                          "@type": "@id"
                        }
                      },
                      "@id": "seadots:nearestAuthoritativeSource"
                    },
                    "verificationGap": "seadots:verificationGap",
                    "note": "skos:note"
                  },
                  "@id": "prov:wasDerivedFrom"
                }
              },
              "@id": "seadots:data"
            }
          },
          "@id": "seadots:benthicBiomassDensity"
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
    "code": "dct:identifier",
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
    "seadots": "https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#",
    "sosa": "http://www.w3.org/ns/sosa/",
    "qudt": "http://qudt.org/schema/qudt/",
    "dwc": "http://rs.tdwg.org/dwc/terms/",
    "indo": "https://w3id.org/indicators/marine/obs/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/benthic-biomass-density-mareano/context.jsonld)

## Sources

* [MAREANO programme](https://mareano.no/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/benthic-biomass-density-mareano`

