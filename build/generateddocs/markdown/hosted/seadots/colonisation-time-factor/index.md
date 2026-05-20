
# Colonisation Time Factor (C_t) (Schema)

`ogc.hosted.seadots.colonisation-time-factor` *v0.1*

OGC Feature + OIM Variable profile for the dimensionless time factor C_t in the reef-biomass equation. Encodes the colonisation curve as a closed-form expression (typically a logistic sigmoid) with its parameters plus an evaluated lookup table at discrete time points. Mandatory provenance flags whether the curve parameters are calibrated or illustrative.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Colonisation Time Factor (C_t)

OGC Feature + OIM Variable profile for the dimensionless time factor `C_t` in the reef-biomass equation `B_reef = sum_i (A_sub · D_pre,i · AF_i · C_t)`.

`C_t` is a scalar that varies with time since installation, typically rising from near zero immediately after deployment to a saturation value (≈1) once the biofouling community has stabilised. This bblock encodes the curve as:

- `formula` — the closed-form expression (e.g. `C(t) = L / (1 + exp(-k * (t - t0)))`)
- `parameters` — values of the formula parameters (e.g. `L`, `k`, `t0_months`)
- `lookup` — an evaluated table at discrete `t_months` so a consumer can read pre-computed `C_t` values without re-evaluating the formula

## Dependency

Extends `ogc.hosted.iliad.api.features.oim-variables` — `C_t` is an OIM indicator.

## Required fields for script consumption

`_sources/experiment/scripts/utsira_reef_biomass.py` reads `data.parameters.L`, `data.parameters.k`, `data.parameters.t0_months` to evaluate the formula analytically, and the `data.lookup[]` array to populate the time series. All four are marked `required` in the schema.

## Authoritative source

There is no published closed-form sigmoid parameterisation of reef colonisation per taxon as of writing. Degraer 2020 discusses temporal dynamics qualitatively but gives no numeric parameters. The realistic calibration route is fitting a sigmoid to a published time series (WindFloat Atlantic monitoring etc.) — flagged in `context-validation-report.md`.

## Examples

### Colonisation time factor — default sigmoid
#### json
```json
{
  "id": "https://example.org/norwegian-ses/colonisation-time-factor/default-sigmoid",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "type": "Dataset",
    "title": "Colonisation time factor (C_t) — default sigmoid",
    "description": "Default sigmoid colonisation curve saturating at t = 24 months. Provides the scalar C_t coefficient for the reef-biomass equation.",
    "created": "2026-05-18",
    "updated": "2026-05-19",
    "language": { "code": "en" },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "themes": [{ "concepts": [{ "id": "reef-effect", "label": "Floating-wind reef effect" }], "scheme": "https://id3.seadots.eu/themes" }],
    "keywords": ["colonisation", "C_t", "sigmoid", "time factor"],
    "formats": [{ "mediaType": "application/ld+json" }],
    "colonisationTimeFactor": {
      "name": "Colonisation time factor (default sigmoid)",
      "description": "Scalar colonisation factor evaluated at scenario T0 + colonisation_months.",
      "role": "coefficient (scalar)",
      "source": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
      "format": "application/ld+json",
      "vocabularyTerm": "https://id3.seadots.eu/indicator/colonisation-time-factor-default",
      "data": {
        "curveType": "sigmoid",
        "formula": "C(t) = L / (1 + exp(-k * (t - t0)))",
        "parameters": { "L": 1.0, "k": 0.30, "t0_months": 8 },
        "lookup": [
          { "t_months": 0,  "C_t": 0.08 },
          { "t_months": 6,  "C_t": 0.32 },
          { "t_months": 12, "C_t": 0.71 },
          { "t_months": 18, "C_t": 0.93 },
          { "t_months": 24, "C_t": 0.99 }
        ],
        "saturationMonth": 24,
        "units": "dimensionless",
        "provenance": {
          "values": "illustrative",
          "note": "Curve form (logistic sigmoid), the L / k / t0 parameter triple, the lookup table values and the 24-month saturation point are ALL ILLUSTRATIVE. Degraer 2020 discusses temporal colonisation dynamics qualitatively but does NOT publish closed-form sigmoid parameters per taxon. There is no public Web API that returns a colonisation-curve parameter set on demand.",
          "primarySource": {
            "doi": "10.5670/oceanog.2020.405",
            "url": "https://tos.org/oceanography/article/offshore-wind-farm-artificial-reefs-affect-ecosystem-structure-and-functioning-a-synthesis",
            "citation": "Degraer et al. 2020 — qualitative discussion of temporal colonisation, no numeric parameters",
            "supportingFigure": "n/a — no equation given"
          },
          "nearestAuthoritativeSource": {
            "url": "https://www.windfloat-atlantic.com/",
            "note": "WindFloat Atlantic monitoring programmes publish time-series of benthic biofouling on floating-wind hulls; fitting a sigmoid to those time series is the realistic route to per-taxon C_t parameters."
          },
          "verificationGap": "Sigmoid parameter values not calibrated against any published time series."
        }
      }
    }
  },
  "links": [
    { "rel": "describedby", "href": "bblocks://ogc.hosted.seadots.colonisation-time-factor", "type": "application/schema+json", "title": "Colonisation Time Factor bblock" },
    { "rel": "profile", "href": "bblocks://ogc.hosted.iliad.api.features.oim-variables", "type": "application/schema+json", "title": "OIM Variables profile" },
    { "rel": "cite-as", "href": "https://doi.org/10.5670/oceanog.2020.405", "title": "Degraer et al. 2020 — colonisation prior" }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/colonisation-time-factor/context.jsonld",
  "id": "https://example.org/norwegian-ses/colonisation-time-factor/default-sigmoid",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "type": "Dataset",
    "title": "Colonisation time factor (C_t) \u2014 default sigmoid",
    "description": "Default sigmoid colonisation curve saturating at t = 24 months. Provides the scalar C_t coefficient for the reef-biomass equation.",
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
            "id": "reef-effect",
            "label": "Floating-wind reef effect"
          }
        ],
        "scheme": "https://id3.seadots.eu/themes"
      }
    ],
    "keywords": [
      "colonisation",
      "C_t",
      "sigmoid",
      "time factor"
    ],
    "formats": [
      {
        "mediaType": "application/ld+json"
      }
    ],
    "colonisationTimeFactor": {
      "name": "Colonisation time factor (default sigmoid)",
      "description": "Scalar colonisation factor evaluated at scenario T0 + colonisation_months.",
      "role": "coefficient (scalar)",
      "source": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
      "format": "application/ld+json",
      "vocabularyTerm": "https://id3.seadots.eu/indicator/colonisation-time-factor-default",
      "data": {
        "curveType": "sigmoid",
        "formula": "C(t) = L / (1 + exp(-k * (t - t0)))",
        "parameters": {
          "L": 1.0,
          "k": 0.3,
          "t0_months": 8
        },
        "lookup": [
          {
            "t_months": 0,
            "C_t": 0.08
          },
          {
            "t_months": 6,
            "C_t": 0.32
          },
          {
            "t_months": 12,
            "C_t": 0.71
          },
          {
            "t_months": 18,
            "C_t": 0.93
          },
          {
            "t_months": 24,
            "C_t": 0.99
          }
        ],
        "saturationMonth": 24,
        "units": "dimensionless",
        "provenance": {
          "values": "illustrative",
          "note": "Curve form (logistic sigmoid), the L / k / t0 parameter triple, the lookup table values and the 24-month saturation point are ALL ILLUSTRATIVE. Degraer 2020 discusses temporal colonisation dynamics qualitatively but does NOT publish closed-form sigmoid parameters per taxon. There is no public Web API that returns a colonisation-curve parameter set on demand.",
          "primarySource": {
            "doi": "10.5670/oceanog.2020.405",
            "url": "https://tos.org/oceanography/article/offshore-wind-farm-artificial-reefs-affect-ecosystem-structure-and-functioning-a-synthesis",
            "citation": "Degraer et al. 2020 \u2014 qualitative discussion of temporal colonisation, no numeric parameters",
            "supportingFigure": "n/a \u2014 no equation given"
          },
          "nearestAuthoritativeSource": {
            "url": "https://www.windfloat-atlantic.com/",
            "note": "WindFloat Atlantic monitoring programmes publish time-series of benthic biofouling on floating-wind hulls; fitting a sigmoid to those time series is the realistic route to per-taxon C_t parameters."
          },
          "verificationGap": "Sigmoid parameter values not calibrated against any published time series."
        }
      }
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.colonisation-time-factor",
      "type": "application/schema+json",
      "title": "Colonisation Time Factor bblock"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.iliad.api.features.oim-variables",
      "type": "application/schema+json",
      "title": "OIM Variables profile"
    },
    {
      "rel": "cite-as",
      "href": "https://doi.org/10.5670/oceanog.2020.405",
      "title": "Degraer et al. 2020 \u2014 colonisation prior"
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
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/norwegian-ses/colonisation-time-factor/default-sigmoid> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "OIM Variables profile" ;
            dcterms:format "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/profile> ;
            oa:hasTarget <bblocks://ogc.hosted.iliad.api.features.oim-variables> ],
        [ rdfs:label "Colonisation Time Factor bblock" ;
            dcterms:format "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.colonisation-time-factor> ],
        [ rdfs:label "Degraer et al. 2020 — colonisation prior" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://doi.org/10.5670/oceanog.2020.405> ] ;
    geojson:properties [ a seadots:Dataset ;
            dcterms:created "2026-05-18" ;
            dcterms:description "Default sigmoid colonisation curve saturating at t = 24 months. Provides the scalar C_t coefficient for the reef-biomass equation." ;
            dcterms:license "https://creativecommons.org/licenses/by/4.0/" ;
            dcterms:modified "2026-05-19" ;
            dcterms:title "Colonisation time factor (C_t) — default sigmoid" ;
            dcat:keyword "C_t",
                "colonisation",
                "sigmoid",
                "time factor" ;
            seadots:colonisationTimeFactor [ dcterms:description "Scalar colonisation factor evaluated at scenario T0 + colonisation_months." ;
                    dcterms:format "application/ld+json" ;
                    dcterms:title "Colonisation time factor (default sigmoid)" ;
                    skos:exactMatch indo:colonisation-time-factor-default ;
                    dcat:accessURL <https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation> ;
                    seadots:data [ qudt:unit "dimensionless" ;
                            prov:wasDerivedFrom [ dcterms:source [ dcterms:bibliographicCitation "Degraer et al. 2020 — qualitative discussion of temporal colonisation, no numeric parameters" ;
                                            dcat:accessURL <https://tos.org/oceanography/article/offshore-wind-farm-artificial-reefs-affect-ecosystem-structure-and-functioning-a-synthesis> ;
                                            seadots:doi "10.5670/oceanog.2020.405" ;
                                            seadots:supportingFigure "n/a — no equation given" ] ;
                                    skos:note "Curve form (logistic sigmoid), the L / k / t0 parameter triple, the lookup table values and the 24-month saturation point are ALL ILLUSTRATIVE. Degraer 2020 discusses temporal colonisation dynamics qualitatively but does NOT publish closed-form sigmoid parameters per taxon. There is no public Web API that returns a colonisation-curve parameter set on demand." ;
                                    seadots:nearestAuthoritativeSource [ skos:note "WindFloat Atlantic monitoring programmes publish time-series of benthic biofouling on floating-wind hulls; fitting a sigmoid to those time series is the realistic route to per-taxon C_t parameters." ;
                                            dcat:accessURL <https://www.windfloat-atlantic.com/> ] ;
                                    seadots:provenanceValues "illustrative" ;
                                    seadots:verificationGap "Sigmoid parameter values not calibrated against any published time series." ] ;
                            seadots:curveType "sigmoid" ;
                            seadots:formula "C(t) = L / (1 + exp(-k * (t - t0)))" ;
                            seadots:lookup ( [ indo:colonisation-time-factor "0.08"^^qudt:DimensionlessQuantity ;
                                        seadots:t_months 0 ] [ indo:colonisation-time-factor "0.32"^^qudt:DimensionlessQuantity ;
                                        seadots:t_months 6 ] [ indo:colonisation-time-factor "0.71"^^qudt:DimensionlessQuantity ;
                                        seadots:t_months 12 ] [ indo:colonisation-time-factor "0.93"^^qudt:DimensionlessQuantity ;
                                        seadots:t_months 18 ] [ indo:colonisation-time-factor "0.99"^^qudt:DimensionlessQuantity ;
                                        seadots:t_months 24 ] ) ;
                            seadots:parameters [ seadots:sigmoidK 3e-01 ;
                                    seadots:sigmoidL 1e+00 ;
                                    seadots:sigmoidT0_months 8 ] ;
                            seadots:saturationMonth 24 ] ;
                    seadots:role "coefficient (scalar)" ] ;
            rec:format [ dcterms:format "application/ld+json" ] ;
            rec:language [ rec:languageCode "en" ] ;
            rec:themes [ rec:concept [ skos:prefLabel "Floating-wind reef effect" ;
                            rec:conceptID "reef-effect"^^xsd:string ] ;
                    rec:scheme "https://id3.seadots.eu/themes" ] ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Colonisation Time Factor (C_t)
description: 'Dimensionless time factor for reef colonisation. Encoded as a closed-form
  expression with named parameters plus an evaluated lookup table.

  '
allOf:
- $ref: https://ogcincubator.github.io/geodcat-ogcapi-records/build/annotated/geo/geodcat/geodcat-records/schema.yaml
properties:
  properties:
    type: object
    required:
    - colonisationTimeFactor
    properties:
      colonisationTimeFactor:
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
            description: Usually `coefficient (scalar)`.
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#role
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
            - curveType
            - formula
            - parameters
            - lookup
            - provenance
            properties:
              curveType:
                type: string
                description: e.g. `sigmoid`.
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#curveType
              formula:
                type: string
                description: Closed-form expression in plain text.
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#formula
              parameters:
                type: object
                required:
                - L
                - k
                - t0_months
                properties:
                  L:
                    type: number
                    minimum: 0
                    description: Sigmoid saturation level.
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#sigmoidL
                  k:
                    type: number
                    description: Sigmoid growth rate.
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#sigmoidK
                  t0_months:
                    type: number
                    description: Sigmoid midpoint, months since installation.
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#sigmoidT0_months
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#parameters
              lookup:
                type: array
                items:
                  type: object
                  required:
                  - t_months
                  - C_t
                  properties:
                    t_months:
                      type: number
                      minimum: 0
                      x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#t_months
                    C_t:
                      type: number
                      minimum: 0
                      maximum: 1
                      description: Evaluated C_t at t_months.
                      x-jsonld-id: https://id3.seadots.eu/indicator/colonisation-time-factor
                      x-jsonld-type: http://qudt.org/schema/qudt/DimensionlessQuantity
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#lookup
                x-jsonld-container: '@list'
              saturationMonth:
                type: number
                minimum: 0
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#saturationMonth
              units:
                type: string
                description: Always `dimensionless`.
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
                    - calibrated
                    - illustrative
                    - mixed
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#provenanceValues
                  primarySource:
                    type: object
                    properties:
                      doi:
                        type: string
                        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#doi
                      url:
                        type: string
                        format: uri
                        x-jsonld-id: http://www.w3.org/ns/dcat#accessURL
                        x-jsonld-type: '@id'
                      citation:
                        type: string
                        x-jsonld-id: http://purl.org/dc/terms/bibliographicCitation
                      supportingFigure:
                        type: string
                        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#supportingFigure
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
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#nearestAuthoritativeSource
                  verificationGap:
                    type: string
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#verificationGap
                  note:
                    type: string
                    x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
                x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#data
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#colonisationTimeFactor
    x-jsonld-id: https://purl.org/geojson/vocab#properties
x-jsonld-extra-terms:
  id: '@id'
  type: '@type'
  geometry: https://purl.org/geojson/vocab#geometry
  Feature: https://purl.org/geojson/vocab#Feature
  links:
    x-jsonld-id: http://www.w3.org/ns/iana/link-relations/relation
    x-jsonld-container: '@set'
  href: '@id'
  rel: https://purl.org/geojson/vocab#rel
  title: http://purl.org/dc/terms/title
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
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#
x-jsonld-prefixes:
  dcterms: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#
  skos: http://www.w3.org/2004/02/skos/core#
  seadots: https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#
  qudt: http://qudt.org/schema/qudt/
  indo: https://id3.seadots.eu/indicator/
  prov: http://www.w3.org/ns/prov#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/colonisation-time-factor/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/colonisation-time-factor/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#",
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
        "colonisationTimeFactor": {
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
                "curveType": "seadots:curveType",
                "formula": "seadots:formula",
                "parameters": {
                  "@context": {
                    "L": "seadots:sigmoidL",
                    "k": "seadots:sigmoidK",
                    "t0_months": "seadots:sigmoidT0_months"
                  },
                  "@id": "seadots:parameters"
                },
                "lookup": {
                  "@context": {
                    "t_months": "seadots:t_months",
                    "C_t": {
                      "@id": "indo:colonisation-time-factor",
                      "@type": "qudt:DimensionlessQuantity"
                    }
                  },
                  "@id": "seadots:lookup",
                  "@container": "@list"
                },
                "saturationMonth": "seadots:saturationMonth",
                "units": "qudt:unit",
                "provenance": {
                  "@context": {
                    "values": "seadots:provenanceValues",
                    "primarySource": {
                      "@context": {
                        "doi": "seadots:doi",
                        "url": {
                          "@id": "dcat:accessURL",
                          "@type": "@id"
                        },
                        "citation": "dct:bibliographicCitation",
                        "supportingFigure": "seadots:supportingFigure"
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
          "@id": "seadots:colonisationTimeFactor"
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
    "seadots": "https://w3id.org/ogc/hosted/seadots/colonisation-time-factor#",
    "qudt": "http://qudt.org/schema/qudt/",
    "indo": "https://id3.seadots.eu/indicator/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/colonisation-time-factor/context.jsonld)

## Sources

* [Degraer et al. 2020 — reef-effect synthesis](https://doi.org/10.5670/oceanog.2020.405)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/colonisation-time-factor`

