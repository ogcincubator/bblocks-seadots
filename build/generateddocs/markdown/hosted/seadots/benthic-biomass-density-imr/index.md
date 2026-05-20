
# IMR Benthic Biomass Density Observation (Schema)

`ogc.hosted.seadots.benthic-biomass-density-imr` *v0.1*

OGC Feature + SOSA observation profile for per-taxon benthic biomass density (kg m-2) sourced from the Institute of Marine Research (IMR / Havforskningsinstituttet) regional baseline series. Acts as the fallback `D_{pre,i}` binding when MAREANO has no taxon coverage at index i. Carries per-taxon density with explicit `uncertainty_kg_m2`, ICES area annotation, and mandatory provenance.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# IMR Benthic Biomass Density Observation

OGC Feature + SOSA Observation profile for per-taxon benthic biomass density (kg m⁻²) sourced from the Institute of Marine Research (IMR / Havforskningsinstituttet) regional baseline series.

Used as the **fallback** `D_{pre,i}` binding when MAREANO has no taxon coverage at index `i`. Compared to the MAREANO bblock, this record carries:
- explicit per-taxon `uncertainty_kg_m2` (MAREANO's row does not);
- an `icesDivision` annotation (e.g. `IVa`);
- a `method` description.

Otherwise the shape mirrors MAREANO so the two are interchangeable downstream.

## Dependency

Extends `ogc.hosted.iliad.api.features.oim-obs`.

## Required fields for script consumption

`_sources/experiment/scripts/utsira_reef_biomass.py` reads `data.perTaxon[].scientificName`, `data.perTaxon[].density_kg_m2`, and `data.perTaxon[].uncertainty_kg_m2`. All three are marked `required` in the schema.

## Retrieval

IMR does not expose a single REST endpoint for "per-taxon baseline density on an AOI". Cruise sample series are distributed via the Norwegian Marine Data Centre (NMD) as discrete datasets. The `data.source` URL in the example is a NOTIONAL endpoint — flagged in `data.provenance.verificationGap`.

## Examples

### IMR benthic biomass baseline — ICES IVa fallback
#### json
```json
{
  "id": "https://example.org/norwegian-ses/benthic-biomass-density-imr/ices-iva-fallback",
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
    "title": "IMR benthic biomass baseline — fallback (D_{pre,i})",
    "description": "Institute of Marine Research regional baseline used when MAREANO has no taxon coverage at index i. Provides the fallback D_{pre,i} binding for the reef-biomass equation, with explicit per-row uncertainty.",
    "created": "2026-05-18",
    "updated": "2026-05-19",
    "language": { "code": "en" },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "themes": [{ "concepts": [{ "id": "benthic-biomass", "label": "Benthic biomass density" }], "scheme": "https://id3.seadots.eu/themes" }],
    "keywords": ["IMR", "benthic biomass", "fallback", "baseline", "ICES IVa"],
    "formats": [{ "mediaType": "application/json" }],
    "conformsTo": [
      "http://www.w3.org/ns/sosa/Observation",
      "https://ogcincubator.github.io/geodcat-ogcapi-records/"
    ],
    "benthicBiomassDensity": {
      "name": "IMR benthic biomass baseline",
      "description": "Fallback baseline benthic biomass density, used when MAREANO has no taxon coverage at i.",
      "role": "fallback baseline",
      "source": "https://www.hi.no/api/benthic-biomass-baseline",
      "format": "application/json",
      "vocabularyTerm": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-imr-baseline",
      "observedProperty": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-imr-baseline",
      "phenomenonTime": "2015-01-01/2020-12-31",
      "data": {
        "units": "kg m-2",
        "samplePeriod": "2015-2020",
        "method": "regional baseline (IMR cruise series, depth-stratified)",
        "icesDivision": "IVa",
        "perTaxon": [
          { "scientificName": "Mytilus edulis",   "aphiaID": 140480, "density_kg_m2": 0.38, "uncertainty_kg_m2": 0.09 },
          { "scientificName": "Buccinum undatum", "aphiaID": 138878, "density_kg_m2": 0.09, "uncertainty_kg_m2": 0.03 },
          { "scientificName": "Asterias rubens",  "aphiaID": 123776, "density_kg_m2": 0.25, "uncertainty_kg_m2": 0.06 }
        ],
        "aggregateDensity_kg_m2": 0.72,
        "provenance": {
          "values": "illustrative",
          "note": "All densities, uncertainties, the sample period and ICES division IVa annotation above are ILLUSTRATIVE placeholders, not IMR measurements. AphiaIDs are real (WoRMS).",
          "nearestAuthoritativeSource": {
            "url": "https://www.imr.no/forskningsdata/",
            "note": "IMR research-data catalogue page; the actual benthic sample series are distributed via the Norwegian Marine Data Centre (NMD) as discrete datasets, not via a per-AOI REST call. The `https://www.hi.no/api/benthic-biomass-baseline` URL in this record's `source` field is a NOTIONAL endpoint — it is NOT a verified IMR public API."
          },
          "verificationGap": "Verified that no public IMR REST API matches the `source` URL pattern as of the date in this record. Real retrieval requires NMD dataset download + offline aggregation."
        }
      }
    }
  },
  "links": [
    { "rel": "describedby", "href": "bblocks://ogc.hosted.seadots.benthic-biomass-density-imr", "type": "application/schema+json", "title": "IMR Benthic Biomass Density Observation bblock" },
    { "rel": "profile", "href": "bblocks://ogc.hosted.iliad.api.features.oim-obs", "type": "application/schema+json", "title": "OIM Observations profile" },
    { "rel": "cite-as", "href": "https://www.hi.no/", "title": "Institute of Marine Research" }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/benthic-biomass-density-imr/context.jsonld",
  "id": "https://example.org/norwegian-ses/benthic-biomass-density-imr/ices-iva-fallback",
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
    "title": "IMR benthic biomass baseline \u2014 fallback (D_{pre,i})",
    "description": "Institute of Marine Research regional baseline used when MAREANO has no taxon coverage at index i. Provides the fallback D_{pre,i} binding for the reef-biomass equation, with explicit per-row uncertainty.",
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
      "IMR",
      "benthic biomass",
      "fallback",
      "baseline",
      "ICES IVa"
    ],
    "formats": [
      {
        "mediaType": "application/json"
      }
    ],
    "conformsTo": [
      "http://www.w3.org/ns/sosa/Observation",
      "https://ogcincubator.github.io/geodcat-ogcapi-records/"
    ],
    "benthicBiomassDensity": {
      "name": "IMR benthic biomass baseline",
      "description": "Fallback baseline benthic biomass density, used when MAREANO has no taxon coverage at i.",
      "role": "fallback baseline",
      "source": "https://www.hi.no/api/benthic-biomass-baseline",
      "format": "application/json",
      "vocabularyTerm": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-imr-baseline",
      "observedProperty": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-imr-baseline",
      "phenomenonTime": "2015-01-01/2020-12-31",
      "data": {
        "units": "kg m-2",
        "samplePeriod": "2015-2020",
        "method": "regional baseline (IMR cruise series, depth-stratified)",
        "icesDivision": "IVa",
        "perTaxon": [
          {
            "scientificName": "Mytilus edulis",
            "aphiaID": 140480,
            "density_kg_m2": 0.38,
            "uncertainty_kg_m2": 0.09
          },
          {
            "scientificName": "Buccinum undatum",
            "aphiaID": 138878,
            "density_kg_m2": 0.09,
            "uncertainty_kg_m2": 0.03
          },
          {
            "scientificName": "Asterias rubens",
            "aphiaID": 123776,
            "density_kg_m2": 0.25,
            "uncertainty_kg_m2": 0.06
          }
        ],
        "aggregateDensity_kg_m2": 0.72,
        "provenance": {
          "values": "illustrative",
          "note": "All densities, uncertainties, the sample period and ICES division IVa annotation above are ILLUSTRATIVE placeholders, not IMR measurements. AphiaIDs are real (WoRMS).",
          "nearestAuthoritativeSource": {
            "url": "https://www.imr.no/forskningsdata/",
            "note": "IMR research-data catalogue page; the actual benthic sample series are distributed via the Norwegian Marine Data Centre (NMD) as discrete datasets, not via a per-AOI REST call. The `https://www.hi.no/api/benthic-biomass-baseline` URL in this record's `source` field is a NOTIONAL endpoint \u2014 it is NOT a verified IMR public API."
          },
          "verificationGap": "Verified that no public IMR REST API matches the `source` URL pattern as of the date in this record. Real retrieval requires NMD dataset download + offline aggregation."
        }
      }
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.benthic-biomass-density-imr",
      "type": "application/schema+json",
      "title": "IMR Benthic Biomass Density Observation bblock"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.iliad.api.features.oim-obs",
      "type": "application/schema+json",
      "title": "OIM Observations profile"
    },
    {
      "rel": "cite-as",
      "href": "https://www.hi.no/",
      "title": "Institute of Marine Research"
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
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/norwegian-ses/benthic-biomass-density-imr/ices-iva-fallback> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Institute of Marine Research" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://www.hi.no/> ],
        [ rdfs:label "IMR Benthic Biomass Density Observation bblock" ;
            dcterms:format "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.benthic-biomass-density-imr> ],
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
            dcterms:description "Institute of Marine Research regional baseline used when MAREANO has no taxon coverage at index i. Provides the fallback D_{pre,i} binding for the reef-biomass equation, with explicit per-row uncertainty." ;
            dcterms:license "https://creativecommons.org/licenses/by/4.0/" ;
            dcterms:modified "2026-05-19" ;
            dcterms:title "IMR benthic biomass baseline — fallback (D_{pre,i})" ;
            dcat:keyword "ICES IVa",
                "IMR",
                "baseline",
                "benthic biomass",
                "fallback" ;
            seadots:benthicBiomassDensity [ dcterms:description "Fallback baseline benthic biomass density, used when MAREANO has no taxon coverage at i." ;
                    dcterms:format "application/json" ;
                    dcterms:title "IMR benthic biomass baseline" ;
                    skos:exactMatch indo:benthic-biomass-density-imr-baseline ;
                    dcat:accessURL <https://www.hi.no/api/benthic-biomass-baseline> ;
                    sosa:observedProperty indo:benthic-biomass-density-imr-baseline ;
                    sosa:phenomenonTime "2015-01-01/2020-12-31" ;
                    seadots:data [ dcterms:methodology "regional baseline (IMR cruise series, depth-stratified)" ;
                            dcterms:temporal "2015-2020" ;
                            qudt:unit "kg m-2" ;
                            prov:wasDerivedFrom [ skos:note "All densities, uncertainties, the sample period and ICES division IVa annotation above are ILLUSTRATIVE placeholders, not IMR measurements. AphiaIDs are real (WoRMS)." ;
                                    seadots:nearestAuthoritativeSource [ skos:note "IMR research-data catalogue page; the actual benthic sample series are distributed via the Norwegian Marine Data Centre (NMD) as discrete datasets, not via a per-AOI REST call. The `https://www.hi.no/api/benthic-biomass-baseline` URL in this record's `source` field is a NOTIONAL endpoint — it is NOT a verified IMR public API." ;
                                            dcat:accessURL <https://www.imr.no/forskningsdata/> ] ;
                                    seadots:provenanceValues "illustrative" ;
                                    seadots:verificationGap "Verified that no public IMR REST API matches the `source` URL pattern as of the date in this record. Real retrieval requires NMD dataset download + offline aggregation." ] ;
                            indo:baseline-benthic-biomass-density "0.72"^^qudt:QuantityValue ;
                            seadots:icesDivision "IVa" ;
                            seadots:perTaxon [ qudt:standardUncertainty 3e-02 ;
                                    dwc:scientificName "Buccinum undatum" ;
                                    dwc:taxonID 138878 ;
                                    indo:benthic-biomass-density-imr-baseline "0.09"^^qudt:QuantityValue ],
                                [ qudt:standardUncertainty 9e-02 ;
                                    dwc:scientificName "Mytilus edulis" ;
                                    dwc:taxonID 140480 ;
                                    indo:benthic-biomass-density-imr-baseline "0.38"^^qudt:QuantityValue ],
                                [ qudt:standardUncertainty 6e-02 ;
                                    dwc:scientificName "Asterias rubens" ;
                                    dwc:taxonID 123776 ;
                                    indo:benthic-biomass-density-imr-baseline "0.25"^^qudt:QuantityValue ] ] ;
                    seadots:role "fallback baseline" ] ;
            rec:format [ dcterms:format "application/json" ] ;
            rec:language [ rec:languageCode "en" ] ;
            rec:themes [ rec:concept [ skos:prefLabel "Benthic biomass density" ;
                            rec:conceptID "benthic-biomass"^^xsd:string ] ;
                    rec:scheme "https://id3.seadots.eu/themes" ] ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: IMR Benthic Biomass Density Observation
description: 'Per-taxon benthic biomass density observation sourced from the Institute
  of Marine Research regional baseline series. Acts as the fallback D_pre,i binding
  when MAREANO has no taxon coverage. Carries explicit per-row uncertainty.

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
            description: Usually `fallback baseline`.
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#role
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
            description: SOSA observed-property URI (`indo:benthic-biomass-density-imr-baseline`).
            x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
            x-jsonld-type: '@id'
          phenomenonTime:
            description: SOSA phenomenon time.
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
                x-jsonld-id: http://qudt.org/schema/qudt/unit
              samplePeriod:
                type: string
                x-jsonld-id: http://purl.org/dc/terms/temporal
              method:
                type: string
                x-jsonld-id: http://purl.org/dc/terms/methodology
              icesDivision:
                type: string
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#icesDivision
              perTaxon:
                type: array
                items:
                  type: object
                  required:
                  - scientificName
                  - density_kg_m2
                  - uncertainty_kg_m2
                  properties:
                    scientificName:
                      type: string
                      x-jsonld-id: http://rs.tdwg.org/dwc/terms/scientificName
                    aphiaID:
                      type: integer
                      x-jsonld-id: http://rs.tdwg.org/dwc/terms/taxonID
                    density_kg_m2:
                      type: number
                      minimum: 0
                      x-jsonld-id: https://w3id.org/indicators/marine/obs/benthic-biomass-density-imr-baseline
                      x-jsonld-type: http://qudt.org/schema/qudt/QuantityValue
                    uncertainty_kg_m2:
                      type: number
                      minimum: 0
                      description: "1\u03C3 standard uncertainty consumed for CV propagation."
                      x-jsonld-id: http://qudt.org/schema/qudt/standardUncertainty
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#perTaxon
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
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#provenanceValues
                  retrievalApiCall:
                    type: string
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#retrievalApiCall
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
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#nearestAuthoritativeSource
                  verificationGap:
                    type: string
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#verificationGap
                  note:
                    type: string
                    x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
                x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#data
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#benthicBiomassDensity
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
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#
x-jsonld-prefixes:
  dcterms: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#
  skos: http://www.w3.org/2004/02/skos/core#
  seadots: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#
  sosa: http://www.w3.org/ns/sosa/
  qudt: http://qudt.org/schema/qudt/
  dwc: http://rs.tdwg.org/dwc/terms/
  indo: https://w3id.org/indicators/marine/obs/
  prov: http://www.w3.org/ns/prov#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/benthic-biomass-density-imr/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/benthic-biomass-density-imr/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#",
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
                "method": "dct:methodology",
                "icesDivision": "seadots:icesDivision",
                "perTaxon": {
                  "@context": {
                    "scientificName": "dwc:scientificName",
                    "aphiaID": "dwc:taxonID",
                    "density_kg_m2": {
                      "@id": "indo:benthic-biomass-density-imr-baseline",
                      "@type": "qudt:QuantityValue"
                    },
                    "uncertainty_kg_m2": "qudt:standardUncertainty"
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
    "seadots": "https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#",
    "sosa": "http://www.w3.org/ns/sosa/",
    "qudt": "http://qudt.org/schema/qudt/",
    "dwc": "http://rs.tdwg.org/dwc/terms/",
    "indo": "https://w3id.org/indicators/marine/obs/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/benthic-biomass-density-imr/context.jsonld)

## Sources

* [Institute of Marine Research (IMR)](https://www.hi.no/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/benthic-biomass-density-imr`

