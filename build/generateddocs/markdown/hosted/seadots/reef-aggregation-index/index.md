
# Reef Aggregation Index (AF_i) (Schema)

`ogc.hosted.seadots.reef-aggregation-index` *v0.1*

OGC Feature profile carrying per-taxon dimensionless reef aggregation index AF_i used by the reef-biomass equation. Treated as an OIM variable / indicator binding — one record per evidence basis (e.g. Degraer 2020 prior). Per-taxon rows carry scientificName, AphiaID, AF_i value, validityScope, and evidence URI.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Reef Aggregation Index (AF_i)

OGC Feature + OIM Variable profile for per-taxon dimensionless reef aggregation index `AF_i` consumed by the reef-biomass equation `B_reef = sum_i (A_sub · D_pre,i · AF_i · C_t)`.

Each record collects a set of `AF_i` bindings sharing one evidence basis (e.g. Degraer 2020 synthesis). Per-taxon rows carry `scientificName`, WoRMS `aphiaID`, the dimensionless `AF_i` value, a `validityScope` annotation (e.g. depth band, substrate type), and an `evidence` URI.

## Dependency

Extends `ogc.hosted.iliad.api.features.oim-variables` — `AF_i` is an indicator/variable in the OIM sense.

## Required fields for script consumption

`_sources/experiment/scripts/utsira_reef_biomass.py` reads `data.perTaxon[].scientificName` and `data.perTaxon[].AF_i`. Both are marked `required` in the schema.

## Vocabulary

The indicator concept `indo:reef-aggregation-index` is local to the SeaDOTs indicator namespace. No external community vocabulary defines a per-m² reef-effect aggregation coefficient at the time of writing — flagged in `context-validation-report.md`.

## Examples

### AF_i — Degraer 2020 prior (per-taxon)
#### json
```json
{
  "id": "https://example.org/norwegian-ses/reef-aggregation-index/degraer2020-bindings",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "type": "Dataset",
    "title": "Reef aggregation index bindings (AF_i) — Degraer 2020 prior",
    "description": "Per-taxon reef aggregation index for Mytilus edulis, Buccinum undatum, Asterias rubens used as AF_i in the reef-biomass equation. AF values are ILLUSTRATIVE — Degraer 2020 reports only one quantitative value (4000-fold biomass increase for Mytilus at turbine-footprint scale) and no per-m² coefficient.",
    "created": "2026-05-18",
    "updated": "2026-05-19",
    "language": { "code": "en" },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "themes": [{ "concepts": [{ "id": "reef-effect", "label": "Floating-wind reef effect" }], "scheme": "https://id3.seadots.eu/themes" }],
    "keywords": ["reef aggregation index", "AF_i", "Mytilus", "Buccinum", "Asterias"],
    "formats": [{ "mediaType": "application/ld+json" }],
    "reefAggregationIndex": {
      "name": "Reef aggregation index bindings",
      "description": "Per-taxon AF_i (Mytilus edulis, Buccinum undatum, Asterias rubens).",
      "role": "coefficient (per taxon)",
      "source": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
      "format": "application/ld+json",
      "vocabularyTerm": "https://w3id.org/indicators/marine/obs/reef-aggregation-index",
      "data": {
        "units": "dimensionless",
        "perTaxon": [
          { "scientificName": "Mytilus edulis",   "aphiaID": 140480, "AF_i": 12.0, "validityScope": "North Sea, 0-30 m" },
          { "scientificName": "Buccinum undatum", "aphiaID": 138878, "AF_i": 3.5,  "validityScope": "soft-sediment, 30-100 m" },
          { "scientificName": "Asterias rubens",  "aphiaID": 123776, "AF_i": 5.0,  "validityScope": "mixed substrate, 0-100 m" }
        ],
        "provenance": {
          "values": "illustrative",
          "note": "AF_i values 12.0 / 3.5 / 5.0 are ILLUSTRATIVE and NOT taken from any published source. Verified against Degraer et al. 2020: that paper reports only one quantitative figure for blue mussel — `biomass can increase 4000-fold compared to the biomass originally present in the sediments` at turbine-footprint scale (citing Rumes et al. 2013) — and gives NO numeric biomass enhancement for Buccinum or Asterias. The 4000-fold figure is at turbine-footprint scale (areal-integrated) and is not directly the per-m² coefficient AF_i.",
          "primarySource": {
            "doi": "10.5670/oceanog.2020.405",
            "url": "https://tos.org/oceanography/article/offshore-wind-farm-artificial-reefs-affect-ecosystem-structure-and-functioning-a-synthesis",
            "citation": "Degraer, S., D.A. Carey, J.W.P. Coolen, Z.L. Hutchison, F. Kerckhof, B. Rumes, J. Vanaverbeke. 2020. Offshore wind farm artificial reefs affect ecosystem structure and functioning: A synthesis. Oceanography 33(4):48–57.",
            "supportingFigure": "Mytilus edulis biomass increase quoted in body text, citing Rumes et al. 2013."
          },
          "nearestAuthoritativeSource": {
            "url": "https://api.obis.org/v3/occurrence?scientificname=Mytilus%20edulis&geometry=POLYGON_PLACEHOLDER&datasetid=wind-farm-monitoring-dataset",
            "note": "Real AF_i derivation requires paired before/after or inside/outside biomass observations on a real wind farm aggregated against control sites."
          },
          "verificationGap": "Degraer 2020 numeric quote verified. AF_i values in this example NOT calibrated to that source."
        }
      }
    }
  },
  "links": [
    { "rel": "describedby", "href": "bblocks://ogc.hosted.seadots.reef-aggregation-index", "type": "application/schema+json", "title": "Reef Aggregation Index bblock" },
    { "rel": "profile", "href": "bblocks://ogc.hosted.iliad.api.features.oim-variables", "type": "application/schema+json", "title": "OIM Variables profile" },
    { "rel": "cite-as", "href": "https://doi.org/10.5670/oceanog.2020.405", "title": "Degraer et al. 2020 — reef-effect prior" }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/reef-aggregation-index/context.jsonld",
  "id": "https://example.org/norwegian-ses/reef-aggregation-index/degraer2020-bindings",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "type": "Dataset",
    "title": "Reef aggregation index bindings (AF_i) \u2014 Degraer 2020 prior",
    "description": "Per-taxon reef aggregation index for Mytilus edulis, Buccinum undatum, Asterias rubens used as AF_i in the reef-biomass equation. AF values are ILLUSTRATIVE \u2014 Degraer 2020 reports only one quantitative value (4000-fold biomass increase for Mytilus at turbine-footprint scale) and no per-m\u00b2 coefficient.",
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
      "reef aggregation index",
      "AF_i",
      "Mytilus",
      "Buccinum",
      "Asterias"
    ],
    "formats": [
      {
        "mediaType": "application/ld+json"
      }
    ],
    "reefAggregationIndex": {
      "name": "Reef aggregation index bindings",
      "description": "Per-taxon AF_i (Mytilus edulis, Buccinum undatum, Asterias rubens).",
      "role": "coefficient (per taxon)",
      "source": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
      "format": "application/ld+json",
      "vocabularyTerm": "https://w3id.org/indicators/marine/obs/reef-aggregation-index",
      "data": {
        "units": "dimensionless",
        "perTaxon": [
          {
            "scientificName": "Mytilus edulis",
            "aphiaID": 140480,
            "AF_i": 12.0,
            "validityScope": "North Sea, 0-30 m"
          },
          {
            "scientificName": "Buccinum undatum",
            "aphiaID": 138878,
            "AF_i": 3.5,
            "validityScope": "soft-sediment, 30-100 m"
          },
          {
            "scientificName": "Asterias rubens",
            "aphiaID": 123776,
            "AF_i": 5.0,
            "validityScope": "mixed substrate, 0-100 m"
          }
        ],
        "provenance": {
          "values": "illustrative",
          "note": "AF_i values 12.0 / 3.5 / 5.0 are ILLUSTRATIVE and NOT taken from any published source. Verified against Degraer et al. 2020: that paper reports only one quantitative figure for blue mussel \u2014 `biomass can increase 4000-fold compared to the biomass originally present in the sediments` at turbine-footprint scale (citing Rumes et al. 2013) \u2014 and gives NO numeric biomass enhancement for Buccinum or Asterias. The 4000-fold figure is at turbine-footprint scale (areal-integrated) and is not directly the per-m\u00b2 coefficient AF_i.",
          "primarySource": {
            "doi": "10.5670/oceanog.2020.405",
            "url": "https://tos.org/oceanography/article/offshore-wind-farm-artificial-reefs-affect-ecosystem-structure-and-functioning-a-synthesis",
            "citation": "Degraer, S., D.A. Carey, J.W.P. Coolen, Z.L. Hutchison, F. Kerckhof, B. Rumes, J. Vanaverbeke. 2020. Offshore wind farm artificial reefs affect ecosystem structure and functioning: A synthesis. Oceanography 33(4):48\u201357.",
            "supportingFigure": "Mytilus edulis biomass increase quoted in body text, citing Rumes et al. 2013."
          },
          "nearestAuthoritativeSource": {
            "url": "https://api.obis.org/v3/occurrence?scientificname=Mytilus%20edulis&geometry=POLYGON_PLACEHOLDER&datasetid=wind-farm-monitoring-dataset",
            "note": "Real AF_i derivation requires paired before/after or inside/outside biomass observations on a real wind farm aggregated against control sites."
          },
          "verificationGap": "Degraer 2020 numeric quote verified. AF_i values in this example NOT calibrated to that source."
        }
      }
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.reef-aggregation-index",
      "type": "application/schema+json",
      "title": "Reef Aggregation Index bblock"
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
      "title": "Degraer et al. 2020 \u2014 reef-effect prior"
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
@prefix indp: <https://w3id.org/indicators/marine/parameters/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/reef-aggregation-index#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/norwegian-ses/reef-aggregation-index/degraer2020-bindings> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Degraer et al. 2020 — reef-effect prior" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://doi.org/10.5670/oceanog.2020.405> ],
        [ rdfs:label "OIM Variables profile" ;
            dcterms:format "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/profile> ;
            oa:hasTarget <bblocks://ogc.hosted.iliad.api.features.oim-variables> ],
        [ rdfs:label "Reef Aggregation Index bblock" ;
            dcterms:format "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.reef-aggregation-index> ] ;
    geojson:properties [ a seadots:Dataset ;
            dcterms:created "2026-05-18" ;
            dcterms:description "Per-taxon reef aggregation index for Mytilus edulis, Buccinum undatum, Asterias rubens used as AF_i in the reef-biomass equation. AF values are ILLUSTRATIVE — Degraer 2020 reports only one quantitative value (4000-fold biomass increase for Mytilus at turbine-footprint scale) and no per-m² coefficient." ;
            dcterms:license "https://creativecommons.org/licenses/by/4.0/" ;
            dcterms:modified "2026-05-19" ;
            dcterms:title "Reef aggregation index bindings (AF_i) — Degraer 2020 prior" ;
            dcat:keyword "AF_i",
                "Asterias",
                "Buccinum",
                "Mytilus",
                "reef aggregation index" ;
            seadots:reefAggregationIndex [ dcterms:description "Per-taxon AF_i (Mytilus edulis, Buccinum undatum, Asterias rubens)." ;
                    dcterms:format "application/ld+json" ;
                    dcterms:title "Reef aggregation index bindings" ;
                    skos:exactMatch indo:reef-aggregation-index ;
                    dcat:accessURL <https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation> ;
                    seadots:data [ qudt:unit "dimensionless" ;
                            prov:wasDerivedFrom [ dcterms:source [ dcterms:bibliographicCitation "Degraer, S., D.A. Carey, J.W.P. Coolen, Z.L. Hutchison, F. Kerckhof, B. Rumes, J. Vanaverbeke. 2020. Offshore wind farm artificial reefs affect ecosystem structure and functioning: A synthesis. Oceanography 33(4):48–57." ;
                                            dcat:accessURL <https://tos.org/oceanography/article/offshore-wind-farm-artificial-reefs-affect-ecosystem-structure-and-functioning-a-synthesis> ;
                                            seadots:doi "10.5670/oceanog.2020.405" ;
                                            seadots:supportingFigure "Mytilus edulis biomass increase quoted in body text, citing Rumes et al. 2013." ] ;
                                    skos:note "AF_i values 12.0 / 3.5 / 5.0 are ILLUSTRATIVE and NOT taken from any published source. Verified against Degraer et al. 2020: that paper reports only one quantitative figure for blue mussel — `biomass can increase 4000-fold compared to the biomass originally present in the sediments` at turbine-footprint scale (citing Rumes et al. 2013) — and gives NO numeric biomass enhancement for Buccinum or Asterias. The 4000-fold figure is at turbine-footprint scale (areal-integrated) and is not directly the per-m² coefficient AF_i." ;
                                    seadots:nearestAuthoritativeSource [ skos:note "Real AF_i derivation requires paired before/after or inside/outside biomass observations on a real wind farm aggregated against control sites." ;
                                            dcat:accessURL <https://api.obis.org/v3/occurrence?scientificname=Mytilus%20edulis&geometry=POLYGON_PLACEHOLDER&datasetid=wind-farm-monitoring-dataset> ] ;
                                    seadots:provenanceValues "illustrative" ;
                                    seadots:verificationGap "Degraer 2020 numeric quote verified. AF_i values in this example NOT calibrated to that source." ] ;
                            seadots:perTaxon [ dcterms:coverage "soft-sediment, 30-100 m" ;
                                    dwc:scientificName "Buccinum undatum" ;
                                    dwc:taxonID 138878 ;
                                    indp:reef-aggregation-index "3.5"^^qudt:DimensionlessQuantity ],
                                [ dcterms:coverage "North Sea, 0-30 m" ;
                                    dwc:scientificName "Mytilus edulis" ;
                                    dwc:taxonID 140480 ;
                                    indp:reef-aggregation-index "12.0"^^qudt:DimensionlessQuantity ],
                                [ dcterms:coverage "mixed substrate, 0-100 m" ;
                                    dwc:scientificName "Asterias rubens" ;
                                    dwc:taxonID 123776 ;
                                    indp:reef-aggregation-index "5.0"^^qudt:DimensionlessQuantity ] ] ;
                    seadots:role "coefficient (per taxon)" ] ;
            rec:format [ dcterms:format "application/ld+json" ] ;
            rec:language [ rec:languageCode "en" ] ;
            rec:themes [ rec:concept [ skos:prefLabel "Floating-wind reef effect" ;
                            rec:conceptID "reef-effect"^^xsd:string ] ;
                    rec:scheme "https://id3.seadots.eu/themes" ] ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Reef Aggregation Index (AF_i)
description: 'Per-taxon dimensionless reef aggregation index used by the reef-biomass
  equation. Treated as an OIM variable / indicator binding.

  '
allOf:
- $ref: https://ogcincubator.github.io/geodcat-ogcapi-records/build/annotated/geo/geodcat/geodcat-records/schema.yaml
properties:
  properties:
    type: object
    required:
    - reefAggregationIndex
    properties:
      reefAggregationIndex:
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
            description: Usually `coefficient (per taxon)`.
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-aggregation-index#role
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
            - perTaxon
            - provenance
            properties:
              units:
                type: string
                description: Always `dimensionless`.
                x-jsonld-id: http://qudt.org/schema/qudt/unit
              perTaxon:
                type: array
                items:
                  type: object
                  required:
                  - scientificName
                  - AF_i
                  properties:
                    scientificName:
                      type: string
                      x-jsonld-id: http://rs.tdwg.org/dwc/terms/scientificName
                    aphiaID:
                      type: integer
                      x-jsonld-id: http://rs.tdwg.org/dwc/terms/taxonID
                    AF_i:
                      type: number
                      minimum: 0
                      description: Dimensionless aggregation index consumed by the
                        reef-biomass equation.
                      x-jsonld-id: https://w3id.org/indicators/marine/parameters/reef-aggregation-index
                      x-jsonld-type: http://qudt.org/schema/qudt/DimensionlessQuantity
                    validityScope:
                      type: string
                      x-jsonld-id: http://purl.org/dc/terms/coverage
                    evidence:
                      type: string
                      format: uri
                      x-jsonld-id: http://www.w3.org/ns/prov#wasInfluencedBy
                      x-jsonld-type: '@id'
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-aggregation-index#perTaxon
                x-jsonld-container: '@set'
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
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-aggregation-index#provenanceValues
                  primarySource:
                    type: object
                    properties:
                      doi:
                        type: string
                        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-aggregation-index#doi
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
                        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-aggregation-index#supportingFigure
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
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-aggregation-index#nearestAuthoritativeSource
                  verificationGap:
                    type: string
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-aggregation-index#verificationGap
                  note:
                    type: string
                    x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
                x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-aggregation-index#data
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/reef-aggregation-index#reefAggregationIndex
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
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/reef-aggregation-index#
x-jsonld-prefixes:
  dcterms: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#
  skos: http://www.w3.org/2004/02/skos/core#
  seadots: https://w3id.org/ogc/hosted/seadots/reef-aggregation-index#
  qudt: http://qudt.org/schema/qudt/
  dwc: http://rs.tdwg.org/dwc/terms/
  indp: https://w3id.org/indicators/marine/parameters/
  prov: http://www.w3.org/ns/prov#
  indo: https://w3id.org/indicators/marine/obs/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/reef-aggregation-index/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/reef-aggregation-index/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/reef-aggregation-index#",
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
        "reefAggregationIndex": {
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
                "units": "qudt:unit",
                "perTaxon": {
                  "@context": {
                    "scientificName": "dwc:scientificName",
                    "aphiaID": "dwc:taxonID",
                    "AF_i": {
                      "@id": "indp:reef-aggregation-index",
                      "@type": "qudt:DimensionlessQuantity"
                    },
                    "validityScope": "dct:coverage",
                    "evidence": {
                      "@id": "prov:wasInfluencedBy",
                      "@type": "@id"
                    }
                  },
                  "@id": "seadots:perTaxon",
                  "@container": "@set"
                },
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
          "@id": "seadots:reefAggregationIndex"
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
    "seadots": "https://w3id.org/ogc/hosted/seadots/reef-aggregation-index#",
    "qudt": "http://qudt.org/schema/qudt/",
    "dwc": "http://rs.tdwg.org/dwc/terms/",
    "indp": "https://w3id.org/indicators/marine/parameters/",
    "indo": "https://w3id.org/indicators/marine/obs/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/reef-aggregation-index/context.jsonld)

## Sources

* [Degraer et al. 2020 — reef-effect synthesis](https://doi.org/10.5670/oceanog.2020.405)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/reef-aggregation-index`

