
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

The raw per-sample Marbunn FeatureCollection and its collector script live in
the companion block [`benthic-biomass-observations-imr`](../benthic-biomass-observations-imr/).
This block keeps only the aggregate per-taxon observation used by downstream
reef-effect calculations.

## Dependency

Extends `ogc.hosted.iliad.api.features.oim-obs`.

## Required fields for script consumption

`_sources/reef-effect/scripts/utsira_reef_biomass.py` reads `data.perTaxon[].scientificName`, `data.perTaxon[].density_kg_m2`, and `data.perTaxon[].uncertainty_kg_m2`. All three are marked `required` in the schema.

## Retrieval

The aggregate example is built from the MAREANO Marbunn API using
`build_example.py`. It groups catch-sample records by species and summarizes
their weights, while the raw block preserves the individual point features.

## Examples

### IMR benthic biomass baseline — ICES IVa fallback
#### json
```json
{
  "id": "https://example.org/norwegian-ses/benthic-biomass-density-imr/mareano-aoi-aggregate",
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
    "title": "MAREANO benthic catch-sample biomass, aggregated per species over a North Sea / Norwegian Sea / Barents Sea AOI",
    "description": "Per-species sum of weighed catch-sample mass from the MAREANO Marbunn database, filtered to the AOI polygon. All numbers are real Marbunn-API responses fetched at file generation time.",
    "created": "2026-05-26",
    "updated": "2026-05-26",
    "language": {
      "code": "en"
    },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "attribution": "Institute of Marine Research (IMR) / MAREANO programme. CC BY 4.0 / NLOD.",
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
      "Marbunn",
      "IMR",
      "benthic biomass",
      "catch samples",
      "Norway"
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
      "name": "MAREANO catch-sample biomass aggregation",
      "description": "Catch weight summed across every weighed Marbunn sample whose station point falls inside the AOI polygon, grouped by species.",
      "role": "real measured baseline (catch-weight; NOT area-normalised density)",
      "source": "https%3A%2F%2Fmarbunn-ekstern.hi.no%2Fapps%2Fmarbunn%2Fv1%2Fgetmapforcatch%3Fspecies%3D%7BscientificName%7D%26cruise%3D",
      "format": "application/geo+json",
      "vocabularyTerm": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-imr-baseline",
      "observedProperty": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-imr-baseline",
      "phenomenonTime": "2006612/2026007006",
      "data": {
        "units": "kg (per-sample catch weight, summed across samples; NOT kg m-2)",
        "method": "For every species in MAREANO's catch-species list, fetched /getmapforcatch as GeoJSON, filtered to the AOI bbox by station coordinate, summed the per-sample Weight property (kg) and counted samples.",
        "samplingGear": [
          "Beamtrawl",
          "Bioboks",
          "Boxcorer",
          "Large VV grab",
          "RP-sledge",
          "Small VV grab",
          "VVgrab020",
          "Videograb"
        ],
        "cruisesContributing": [
          "2006612",
          "2007105",
          "2007111",
          "2024007005",
          "2025001009",
          "2026007006",
              "2009105",
              "2009111",
              "2010110",
              "2010112"
        ],
        "timeBoundaries": null,
        "speciesQueried": 3620,
        "speciesWithRecordsInAOI": 988,
        "speciesWithWeighedSamples": 481,
        "totalRecordsInAOI": 23438,
        "totalWeight_kg": 25405.761,
        "perTaxon": [
          {
            "scientificName": "Aplysilla",
            "totalWeight_kg": 5000.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 10,
            "totalIndividuals": 0,
            "cruises": [
              "2009105",
              "2009111",
              "2010110",
              "2010112"
            ],
            "equipment": [
              "Beamtrawl",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Actiniaria",
            "totalWeight_kg": 4473.589,
            "samplesWithWeight": 95,
            "samplesInAOI": 476,
            "totalIndividuals": 656,
            "cruises": [
              "2007105",
              "2007111",
              "2024007003",
              "2024007005"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          }
        ],
        "provenance": {
          "values": "real",
          "source": {
            "name": "MAREANO Marbunn (IMR catch-samples viewer)",
            "api": "https://marbunn-ekstern.hi.no/apps/marbunn/v1/",
            "speciesListEndpoint": "https://marbunn-ekstern.hi.no/apps/marbunn/v1/catchspecies",
            "perSpeciesEndpoint": "https://marbunn-ekstern.hi.no/apps/marbunn/v1/getmapforcatch?species={name}&cruise=",
            "portal": "https://mareano.no/",
            "license": "CC BY 4.0 / NLOD"
          },
          "fetched_utc": "2026-05-26T11:11:24Z",
          "generator": "build_example.py",
          "timeBoundaryNote": "No explicit --time-boundaries supplied; phenomenonTime falls back to the min/max contributing cruise identifiers.",
          "caveats": [
            "Marbunn returns catch-sample weights in kilograms; the values here are SUMS of those per-sample weights — not areal densities. Converting to kg m-2 would require the swept area of every sample, which Marbunn does not expose.",
            "Many catch records have Weight=null (sample identified but not weighed); they are excluded from totalWeight_kg but counted in samplesInAOI so coverage gaps stay visible.",
            "Cruise IDs are MAREANO/IMR internal cruise codes; the same physical cruise may use multiple gear types.",
            "The AOI polygon is a wide bbox; it overlaps but does not equal any single ICES Division."
          ],
          "rawCollectionBlock": "bblocks://ogc.hosted.seadots.benthic-biomass-observations-imr"
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
      "rel": "derivedFrom",
      "href": "bblocks://ogc.hosted.seadots.benthic-biomass-observations-imr",
      "type": "application/schema+json",
      "title": "IMR benthic biomass observations bblock"
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
    },
    {
      "rel": "cite-as",
      "href": "https://www.hi.no/",
      "title": "Institute of Marine Research"
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/benthic-biomass-density-imr/context.jsonld",
  "id": "https://example.org/norwegian-ses/benthic-biomass-density-imr/mareano-aoi-aggregate",
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
    "title": "MAREANO benthic catch-sample biomass, aggregated per species over a North Sea / Norwegian Sea / Barents Sea AOI",
    "description": "Per-species sum of weighed catch-sample mass from the MAREANO Marbunn database, filtered to the AOI polygon. All numbers are real Marbunn-API responses fetched at file generation time.",
    "created": "2026-05-26",
    "updated": "2026-05-26",
    "language": {
      "code": "en"
    },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "attribution": "Institute of Marine Research (IMR) / MAREANO programme. CC BY 4.0 / NLOD.",
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
      "Marbunn",
      "IMR",
      "benthic biomass",
      "catch samples",
      "Norway"
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
      "name": "MAREANO catch-sample biomass aggregation",
      "description": "Catch weight summed across every weighed Marbunn sample whose station point falls inside the AOI polygon, grouped by species.",
      "role": "real measured baseline (catch-weight; NOT area-normalised density)",
      "source": "https%3A%2F%2Fmarbunn-ekstern.hi.no%2Fapps%2Fmarbunn%2Fv1%2Fgetmapforcatch%3Fspecies%3D%7BscientificName%7D%26cruise%3D",
      "format": "application/geo+json",
      "vocabularyTerm": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-imr-baseline",
      "observedProperty": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-imr-baseline",
      "phenomenonTime": "2006612/2026007006",
      "data": {
        "units": "kg (per-sample catch weight, summed across samples; NOT kg m-2)",
        "method": "For every species in MAREANO's catch-species list, fetched /getmapforcatch as GeoJSON, filtered to the AOI bbox by station coordinate, summed the per-sample Weight property (kg) and counted samples.",
        "samplingGear": [
          "Beamtrawl",
          "Bioboks",
          "Boxcorer",
          "Large VV grab",
          "RP-sledge",
          "Small VV grab",
          "VVgrab020",
          "Videograb"
        ],
        "cruisesContributing": [
          "2006612",
          "2007105",
          "2007111",
          "2024007005",
          "2025001009",
          "2026007006",
          "2009105",
          "2009111",
          "2010110",
          "2010112"
        ],
        "timeBoundaries": null,
        "speciesQueried": 3620,
        "speciesWithRecordsInAOI": 988,
        "speciesWithWeighedSamples": 481,
        "totalRecordsInAOI": 23438,
        "totalWeight_kg": 25405.761,
        "perTaxon": [
          {
            "scientificName": "Aplysilla",
            "totalWeight_kg": 5000.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 10,
            "totalIndividuals": 0,
            "cruises": [
              "2009105",
              "2009111",
              "2010110",
              "2010112"
            ],
            "equipment": [
              "Beamtrawl",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Actiniaria",
            "totalWeight_kg": 4473.589,
            "samplesWithWeight": 95,
            "samplesInAOI": 476,
            "totalIndividuals": 656,
            "cruises": [
              "2007105",
              "2007111",
              "2024007003",
              "2024007005"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          }
        ],
        "provenance": {
          "values": "real",
          "source": {
            "name": "MAREANO Marbunn (IMR catch-samples viewer)",
            "api": "https://marbunn-ekstern.hi.no/apps/marbunn/v1/",
            "speciesListEndpoint": "https://marbunn-ekstern.hi.no/apps/marbunn/v1/catchspecies",
            "perSpeciesEndpoint": "https://marbunn-ekstern.hi.no/apps/marbunn/v1/getmapforcatch?species={name}&cruise=",
            "portal": "https://mareano.no/",
            "license": "CC BY 4.0 / NLOD"
          },
          "fetched_utc": "2026-05-26T11:11:24Z",
          "generator": "build_example.py",
          "timeBoundaryNote": "No explicit --time-boundaries supplied; phenomenonTime falls back to the min/max contributing cruise identifiers.",
          "caveats": [
            "Marbunn returns catch-sample weights in kilograms; the values here are SUMS of those per-sample weights \u2014 not areal densities. Converting to kg m-2 would require the swept area of every sample, which Marbunn does not expose.",
            "Many catch records have Weight=null (sample identified but not weighed); they are excluded from totalWeight_kg but counted in samplesInAOI so coverage gaps stay visible.",
            "Cruise IDs are MAREANO/IMR internal cruise codes; the same physical cruise may use multiple gear types.",
            "The AOI polygon is a wide bbox; it overlaps but does not equal any single ICES Division."
          ],
          "rawCollectionBlock": "bblocks://ogc.hosted.seadots.benthic-biomass-observations-imr"
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
      "rel": "derivedFrom",
      "href": "bblocks://ogc.hosted.seadots.benthic-biomass-observations-imr",
      "type": "application/schema+json",
      "title": "IMR benthic biomass observations bblock"
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
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/norwegian-ses/benthic-biomass-density-imr/mareano-aoi-aggregate> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "MAREANO programme" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://mareano.no/> ],
        [ rdfs:label "IMR Benthic Biomass Density Observation bblock" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.benthic-biomass-density-imr> ],
        [ rdfs:label "Institute of Marine Research" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://www.hi.no/> ],
        [ rdfs:label "OIM Observations profile" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/profile> ;
            oa:hasTarget <bblocks://ogc.hosted.iliad.api.features.oim-obs> ],
        [ rdfs:label "IMR benthic biomass observations bblock" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/derivedFrom> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.benthic-biomass-observations-imr> ] ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( -5e+00 5.6e+01 ) ( 3.3e+01 5.6e+01 ) ( 3.3e+01 8.2e+01 ) ( -5e+00 8.2e+01 ) ( -5e+00 5.6e+01 ) ) ) ] ;
    geojson:properties [ a seadots:Dataset ;
            dcterms:conformsTo sosa:Observation,
                <https://ogcincubator.github.io/geodcat-ogcapi-records/> ;
            dcterms:created "2026-05-26" ;
            dcterms:format [ dcterms:format "application/json" ] ;
            dcterms:language [ dcterms:identifier "en" ] ;
            dcterms:license "https://creativecommons.org/licenses/by/4.0/" ;
            dcterms:modified "2026-05-26" ;
            dcterms:title "MAREANO benthic catch-sample biomass, aggregated per species over a North Sea / Norwegian Sea / Barents Sea AOI" ;
            dcat:keyword "IMR",
                "MAREANO",
                "Marbunn",
                "Norway",
                "benthic biomass",
                "catch samples" ;
            dcat:theme [ skos:Concept <file:///github/workspace/benthic-biomass> ;
                    skos:inScheme "https://id3.seadots.eu/themes" ] ;
            seadots:attribution "Institute of Marine Research (IMR) / MAREANO programme. CC BY 4.0 / NLOD." ;
            seadots:benthicBiomassDensity [ dcterms:description "Catch weight summed across every weighed Marbunn sample whose station point falls inside the AOI polygon, grouped by species." ;
                    dcterms:format "application/geo+json" ;
                    dcterms:title "MAREANO catch-sample biomass aggregation" ;
                    skos:exactMatch indo:benthic-biomass-density-imr-baseline ;
                    dcat:accessURL <file:///github/workspace/https%3A%2F%2Fmarbunn-ekstern.hi.no%2Fapps%2Fmarbunn%2Fv1%2Fgetmapforcatch%3Fspecies%3D%7BscientificName%7D%26cruise%3D> ;
                    sosa:observedProperty indo:benthic-biomass-density-imr-baseline ;
                    sosa:phenomenonTime "2006612/2026007006" ;
                    seadots:data [ dcterms:methodology "For every species in MAREANO's catch-species list, fetched /getmapforcatch as GeoJSON, filtered to the AOI bbox by station coordinate, summed the per-sample Weight property (kg) and counted samples." ;
                            dcterms:temporal () ;
                            qudt:unit "kg (per-sample catch weight, summed across samples; NOT kg m-2)" ;
                            prov:wasDerivedFrom [ skos:note "No explicit --time-boundaries supplied; phenomenonTime falls back to the min/max contributing cruise identifiers." ;
                                    dcat:accessURL [ dcterms:license "CC BY 4.0 / NLOD" ;
                                            dcterms:title "MAREANO Marbunn (IMR catch-samples viewer)" ;
                                            seadots:api "https://marbunn-ekstern.hi.no/apps/marbunn/v1/" ;
                                            seadots:perSpeciesEndpoint "https://marbunn-ekstern.hi.no/apps/marbunn/v1/getmapforcatch?species={name}&cruise=" ;
                                            seadots:portal "https://mareano.no/" ;
                                            seadots:speciesListEndpoint "https://marbunn-ekstern.hi.no/apps/marbunn/v1/catchspecies" ] ;
                                    prov:wasDerivedFrom <bblocks://ogc.hosted.seadots.benthic-biomass-observations-imr> ;
                                    seadots:caveats "Cruise IDs are MAREANO/IMR internal cruise codes; the same physical cruise may use multiple gear types.",
                                        "Many catch records have Weight=null (sample identified but not weighed); they are excluded from totalWeight_kg but counted in samplesInAOI so coverage gaps stay visible.",
                                        "Marbunn returns catch-sample weights in kilograms; the values here are SUMS of those per-sample weights — not areal densities. Converting to kg m-2 would require the swept area of every sample, which Marbunn does not expose.",
                                        "The AOI polygon is a wide bbox; it overlaps but does not equal any single ICES Division." ;
                                    seadots:fetched_utc "2026-05-26T11:11:24Z" ;
                                    seadots:generator "build_example.py" ;
                                    seadots:provenanceValues "real" ] ;
                            seadots:cruisesContributing "2006612",
                                "2007105",
                                "2007111",
                                "2009105",
                                "2009111",
                                "2010110",
                                "2010112",
                                "2024007005",
                                "2025001009",
                                "2026007006" ;
                            seadots:perTaxon [ dwc:scientificName "Actiniaria" ;
                                    seadots:cruises "2007105",
                                        "2007111",
                                        "2024007003",
                                        "2024007005" ;
                                    seadots:equipment "Beamtrawl",
                                        "Large VV grab",
                                        "RP-sledge",
                                        "Small VV grab",
                                        "VVgrab020" ;
                                    seadots:samplesInAOI 476 ;
                                    seadots:samplesWithWeight 95 ;
                                    seadots:totalIndividuals 656 ;
                                    seadots:totalWeight_kg 4.473589e+03 ],
                                [ dwc:scientificName "Aplysilla" ;
                                    seadots:cruises "2009105",
                                        "2009111",
                                        "2010110",
                                        "2010112" ;
                                    seadots:equipment "Beamtrawl",
                                        "VVgrab020" ;
                                    seadots:samplesInAOI 10 ;
                                    seadots:samplesWithWeight 1 ;
                                    seadots:totalIndividuals 0 ;
                                    seadots:totalWeight_kg 5e+03 ] ;
                            seadots:samplingGear "Beamtrawl",
                                "Bioboks",
                                "Boxcorer",
                                "Large VV grab",
                                "RP-sledge",
                                "Small VV grab",
                                "VVgrab020",
                                "Videograb" ;
                            seadots:speciesQueried 3620 ;
                            seadots:speciesWithRecordsInAOI 988 ;
                            seadots:speciesWithWeighedSamples 481 ;
                            seadots:totalRecordsInAOI 23438 ;
                            seadots:totalWeight_kg 2.540576e+04 ] ;
                    seadots:role "real measured baseline (catch-weight; NOT area-normalised density)" ] ;
            seadots:description "Per-species sum of weighed catch-sample mass from the MAREANO Marbunn database, filtered to the AOI polygon. All numbers are real Marbunn-API responses fetched at file generation time." ] .

<file:///github/workspace/benthic-biomass> rdfs:label "Benthic biomass density" .


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
- $ref: https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-obs/schema.yaml
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
              required:
              - start
              - end
              properties:
                start:
                  type: string
                  format: date
                  x-jsonld-id: http://www.w3.org/2006/time#hasBeginning
                  x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
                end:
                  type: string
                  format: date
                  x-jsonld-id: http://www.w3.org/2006/time#hasEnd
                  x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
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
              timeBoundaries:
                type: array
                description: Explicit phenomenon-time boundaries supplied to build_example.py.
                minItems: 2
                maxItems: 2
                items:
                  type: string
                  format: date
                x-jsonld-id: http://purl.org/dc/terms/temporal
                x-jsonld-container: '@list'
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
                  rawCollectionBlock:
                    type: string
                    x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
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
                  timeBoundaryNote:
                    type: string
                    x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
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
  time: http://www.w3.org/2006/time#
  qudt: http://qudt.org/schema/qudt/
  dwc: http://rs.tdwg.org/dwc/terms/
  indo: https://w3id.org/indicators/marine/obs/
  prov: http://www.w3.org/ns/prov#
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.benthic-biomass-density-imr
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-04'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/benthic-biomass-density-imr/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/benthic-biomass-density-imr/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#",
    "id": "@id",
    "properties": {
      "@id": "geojson:properties",
      "@context": {
        "benthicBiomassDensity": {
          "@context": {
            "name": "dct:title",
            "description": "dct:description",
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
            "phenomenonTime": {
              "@context": {
                "start": {
                  "@id": "owlTime:hasBeginning",
                  "@type": "xsd:date"
                },
                "end": {
                  "@id": "owlTime:hasEnd",
                  "@type": "xsd:date"
                }
              },
              "@id": "sosa:phenomenonTime"
            },
            "data": {
              "@context": {
                "units": "qudt:unit",
                "samplePeriod": "dct:temporal",
                "timeBoundaries": {
                  "@id": "dct:temporal",
                  "@container": "@list"
                },
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
                    "rawCollectionBlock": {
                      "@id": "prov:wasDerivedFrom",
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
                    "timeBoundaryNote": "skos:note"
                  },
                  "@id": "prov:wasDerivedFrom"
                }
              },
              "@id": "seadots:data"
            }
          },
          "@id": "seadots:benthicBiomassDensity"
        }
      }
    },
    "featureType": "geojson:collectionFeatureType",
    "ActuatableProperty": {
      "@id": "sosa:ActuatableProperty",
      "@type": "@id"
    },
    "Actuation": {
      "@id": "sosa:Actuation",
      "@type": "@id"
    },
    "ActuationCollection": {
      "@id": "sosa:ActuationCollection",
      "@type": "@id"
    },
    "Actuator": {
      "@id": "sosa:Actuator",
      "@type": "@id"
    },
    "Deployment": {
      "@id": "sosa:Deployment",
      "@type": "@id"
    },
    "Execution": {
      "@id": "sosa:Execution",
      "@type": "@id"
    },
    "FeatureOfInterest": {
      "@id": "sosa:FeatureOfInterest",
      "@type": "@id"
    },
    "ObservableProperty": {
      "@id": "sosa:ObservableProperty",
      "@type": "@id"
    },
    "Observation": {
      "@id": "sosa:Observation",
      "@type": "@id"
    },
    "ObservationCollection": {
      "@id": "sosa:ObservationCollection",
      "@type": "@id"
    },
    "Platform": {
      "@id": "sosa:Platform",
      "@type": "@id"
    },
    "Property": {
      "@id": "sosa:Property",
      "@type": "@id"
    },
    "Procedure ": {
      "@id": "sosa:Procedure",
      "@type": "@id"
    },
    "Sample": {
      "@id": "sosa:Sample",
      "@type": "@id"
    },
    "SampleCollection": {
      "@id": "sosa:SampleCollection",
      "@type": "@id"
    },
    "Sampler": {
      "@id": "sosa:Sampler",
      "@type": "@id"
    },
    "Sampling": {
      "@id": "sosa:Sampling",
      "@type": "@id"
    },
    "Sensor": {
      "@id": "sosa:Sensor",
      "@type": "@id"
    },
    "Stimulus": {
      "@id": "sosa:Stimulus",
      "@type": "@id"
    },
    "System": {
      "@id": "sosa:System",
      "@type": "@id"
    },
    "actsOn": {
      "@id": "sosa:actsOn",
      "@type": "@id"
    },
    "actsOnProperty": {
      "@id": "sosa:actsOnProperty",
      "@type": "@id"
    },
    "deployedAsset": {
      "@id": "sosa:deployedAsset",
      "@type": "@id"
    },
    "deployedOnPlatform": {
      "@id": "sosa:deployedOnPlatform",
      "@type": "@id"
    },
    "deployedSystem": {
      "@id": "sosa:deployedSystem",
      "@type": "@id"
    },
    "detects": {
      "@id": "sosa:detects",
      "@type": "@id"
    },
    "features": {
      "@id": "sosa:hasMember",
      "@type": "@id",
      "@container": "@set",
      "@context": {
        "properties": "@nest",
        "featureType": "@type",
        "Prism": {
          "@id": "geojson:Prism",
          "@context": {
            "base": "geojson:prismBase",
            "lower": "geojson:prismLower",
            "upper": "geojson:prismUpper"
          }
        },
        "MultiPrism": {
          "@id": "geojson:MultiPrism",
          "@context": {
            "prisms": "geojson:prisms"
          }
        }
      }
    },
    "forProperty": {
      "@id": "sosa:forProperty",
      "@type": "@id"
    },
    "hasDeployment": {
      "@id": "sosa:hasDeployment",
      "@type": "@id"
    },
    "hasInput": {
      "@id": "sosa:hasInput",
      "@type": "@id"
    },
    "hasMember": {
      "@id": "sosa:hasMember",
      "@type": "@id"
    },
    "hasOriginalSample": {
      "@id": "sosa:hasOriginalSample",
      "@type": "@id"
    },
    "hasOutput": {
      "@id": "sosa:hasOutput",
      "@type": "@id"
    },
    "hasProperty": {
      "@id": "sosa:hasProperty",
      "@type": "@id"
    },
    "hasResultQuality": {
      "@id": "sosa:hasResultQuality",
      "@type": "@id"
    },
    "hasSample": {
      "@id": "sosa:hasSample",
      "@type": "@id"
    },
    "hasSampledFeature": {
      "@id": "sosa:hasSampledFeature",
      "@type": "@id"
    },
    "hasSubSystem": {
      "@id": "sosa:hasSubSystem",
      "@type": "@id",
      "@container": "@set"
    },
    "hosts": {
      "@id": "sosa:hosts",
      "@type": "@id",
      "@container": "@set"
    },
    "implementedBy": {
      "@id": "sosa:implementedBy",
      "@type": "@id"
    },
    "implements": {
      "@id": "sosa:implements",
      "@type": "@id"
    },
    "inDeployment": {
      "@id": "sosa:inDeployment",
      "@type": "@id"
    },
    "isActedOnBy": {
      "@id": "sosa:isActedOnBy",
      "@type": "@id"
    },
    "isFeatureOfInterestOf": {
      "@id": "sosa:isFeatureOfInterestOf",
      "@type": "@id"
    },
    "isHostedBy": {
      "@id": "sosa:isHostedBy",
      "@type": "@id"
    },
    "isObservedBy": {
      "@id": "sosa:isObservedBy",
      "@type": "@id"
    },
    "isOriginalSampleOf": {
      "@id": "sosa:isOriginalSampleOf",
      "@type": "@id"
    },
    "isPropertyOf": {
      "@id": "sosa:isPropertyOf",
      "@type": "@id"
    },
    "isProxyFor": {
      "@id": "sosa:isProxyFor",
      "@type": "@id"
    },
    "isResultOf": {
      "@id": "sosa:isResultOf",
      "@type": "@id"
    },
    "isResultOfMadeBySampler": {
      "@id": "sosa:isResultOfMadeBySampler",
      "@type": "@id"
    },
    "isResultOfUsedProcedure": {
      "@id": "sosa:isResultOfUsedProcedure",
      "@type": "@id"
    },
    "isSampleOf": {
      "@id": "sosa:isSampleOf",
      "@type": "@id"
    },
    "isSampleOfUltimateFOI": {
      "@id": "sosa:isSampleOfUltimateFOI",
      "@type": "@id"
    },
    "isSubSystemOf": {
      "@id": "sosa:isSubSystemOf",
      "@type": "@id"
    },
    "madeActuation": {
      "@id": "sosa:madeActuation",
      "@type": "@id"
    },
    "madeByActuator": {
      "@id": "sosa:madeByActuator",
      "@type": "@id"
    },
    "madeBySampler": {
      "@id": "sosa:madeBySampler",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "sosa:madeBySensor",
      "@type": "@id"
    },
    "madeBySystem": {
      "@id": "sosa:madeBySystem",
      "@type": "@id"
    },
    "madeExecution": {
      "@id": "sosa:madeExecution",
      "@type": "@id"
    },
    "madeObservation": {
      "@id": "sosa:madeObservation",
      "@type": "@id"
    },
    "madeSampling": {
      "@id": "sosa:madeSampling",
      "@type": "@id"
    },
    "observedProperty": {
      "@id": "sosa:observedProperty",
      "@type": "@id",
      "@context": {
        "@base": "https://w3id.org/iliad/jellyfish/property/"
      }
    },
    "observes": {
      "@id": "sosa:observes",
      "@type": "@id"
    },
    "wasOriginatedBy": {
      "@id": "sosa:wasOriginatedBy",
      "@type": "@id"
    },
    "Accuracy": {
      "@id": "ssn-system:Accuracy",
      "@type": "@id"
    },
    "ActuationRange": {
      "@id": "ssn-system:ActuationRange",
      "@type": "@id"
    },
    "BatteryLifetime": {
      "@id": "ssn-system:BatteryLifetime",
      "@type": "@id"
    },
    "DetectionLimit": {
      "@id": "ssn-system:DetectionLimit",
      "@type": "@id"
    },
    "Drift": {
      "@id": "ssn-system:Drift",
      "@type": "@id"
    },
    "Frequency": {
      "@id": "ssn-system:Frequency",
      "@type": "@id"
    },
    "Latency": {
      "@id": "ssn-system:Latency",
      "@type": "@id"
    },
    "MaintenanceSchedule": {
      "@id": "ssn-system:MaintenanceSchedule",
      "@type": "@id"
    },
    "MeasurementRange": {
      "@id": "ssn-system:MeasurementRange",
      "@type": "@id"
    },
    "OperatingPowerRange": {
      "@id": "ssn-system:OperatingPowerRange",
      "@type": "@id"
    },
    "OperatingProperty": {
      "@id": "ssn-system:OperatingProperty",
      "@type": "@id"
    },
    "OperatingRange": {
      "@id": "ssn-system:OperatingRange",
      "@type": "@id"
    },
    "Precision": {
      "@id": "ssn-system:Precision",
      "@type": "@id"
    },
    "Resolution": {
      "@id": "ssn-system:Resolution",
      "@type": "@id"
    },
    "ResponseTime": {
      "@id": "ssn-system:ResponseTime",
      "@type": "@id"
    },
    "Selectivity": {
      "@id": "ssn-system:Selectivity",
      "@type": "@id"
    },
    "Sensitivity": {
      "@id": "ssn-system:Sensitivity",
      "@type": "@id"
    },
    "SurvivalProperty": {
      "@id": "ssn-system:SurvivalProperty",
      "@type": "@id"
    },
    "SystemLifetime": {
      "@id": "ssn-system:SystemLifetime",
      "@type": "@id"
    },
    "SurvivalRange": {
      "@id": "ssn-system:SurvivalRange",
      "@type": "@id"
    },
    "SystemCapability": {
      "@id": "ssn-system:SystemCapability",
      "@type": "@id"
    },
    "SystemProperty": {
      "@id": "ssn-system:SystemProperty",
      "@type": "@id"
    },
    "hasOperatingProperty": {
      "@id": "ssn-system:hasOperatingProperty",
      "@type": "@id"
    },
    "hasOperatingRange": {
      "@id": "ssn-system:hasOperatingRange",
      "@type": "@id"
    },
    "hasSurvivalProperty": {
      "@id": "ssn-system:hasSurvivalProperty",
      "@type": "@id"
    },
    "hasSystemCapability": {
      "@id": "ssn-system:hasSystemCapability",
      "@type": "@id"
    },
    "hasSystemProperty": {
      "@id": "ssn-system:hasSystemProperty",
      "@type": "@id"
    },
    "hasSurvivalRange": {
      "@id": "ssn-system:hasSurvivalRange",
      "@type": "@id"
    },
    "inCondition": {
      "@id": "ssn-system:inCondition",
      "@type": "@id"
    },
    "qualityOfObservation": {
      "@id": "ssn-system:qualityOfObservation",
      "@type": "@id"
    },
    "resultTime": {
      "@id": "sosa:resultTime",
      "@type": "xsd:dateTime"
    },
    "phenomenonTime": {
      "@context": {
        "inXSDDateTime": {
          "@id": "owlTime:inXSDDateTime",
          "@type": "xsd:dateTime"
        },
        "ProperInterval": "owlTime:ProperInterval",
        "hasDuration": "owlTime:hasDuration",
        "hasXSDDuration": {
          "@id": "owlTime:hasXSDDuration",
          "@type": "xsd:duration"
        },
        "inTimePosition": "owlTime:inTimePosition",
        "inXSDgYear": {
          "@id": "owlTime:inXSDgYear",
          "@type": "xsd:gYear"
        },
        "inXSDgYearMonth": {
          "@id": "owlTime:inXSDgYearMonth",
          "@type": "xsd:gYearMonth"
        },
        "time": "http://www.w3.org/2006/time#"
      },
      "@id": "sosa:phenomenonTime",
      "@type": "xsd:dateTime"
    },
    "hasFeatureOfInterest": {
      "@id": "sosa:hasFeatureOfInterest",
      "@type": "@id"
    },
    "hasUltimateFeatureOfInterest": {
      "@id": "sosa:hasUltimateFeatureOfInterest",
      "@type": "@id"
    },
    "usedProcedure": {
      "@id": "sosa:usedProcedure",
      "@type": "@id"
    },
    "startTime": {
      "@id": "sosa:startTime",
      "@type": "xsd:dateTime"
    },
    "endTime": {
      "@id": "sosa:endTime",
      "@type": "xsd:dateTime"
    },
    "hasResult": {
      "@id": "sosa:hasResult",
      "@type": "@id"
    },
    "hasSimpleResult": "sosa:hasSimpleResult",
    "hasInputValue": {
      "@id": "sosa:hasInputValue",
      "@type": "@id"
    },
    "label": {
      "@id": "rdfs:label",
      "@container": "@language"
    },
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "type": "@type",
    "geometry": "geojson:geometry",
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
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "time": {
      "@context": {
        "date": {
          "@id": "owlTime:hasTime",
          "@type": "xsd:date"
        },
        "timestamp": {
          "@id": "owlTime:hasTime",
          "@type": "xsd:dateTime"
        },
        "interval": {
          "@id": "owlTime:hasTime",
          "@container": "@list"
        }
      },
      "@id": "dct:time"
    },
    "coordRefSys": "http://www.opengis.net/def/glossary/term/CoordinateReferenceSystemCRS",
    "place": "dct:spatial",
    "Polyhedron": "geojson:Polyhedron",
    "MultiPolyhedron": "geojson:MultiPolyhedron",
    "Prism": {
      "@id": "geojson:Prism",
      "@context": {
        "base": "geojson:prismBase",
        "lower": "geojson:prismLower",
        "upper": "geojson:prismUpper"
      }
    },
    "MultiPrism": {
      "@id": "geojson:MultiPrism",
      "@context": {
        "prisms": "geojson:prisms"
      }
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "geometries": {
      "@id": "geojson:geometry",
      "@container": "@list"
    },
    "PhotonFluxDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#PhotonFluxDensity",
    "invalidatedAtTime": {
      "@id": "prov:invalidatedAtTime",
      "@type": "xsd:dateTime"
    },
    "Attachable": "http://purl.org/linked-data/cube#Attachable",
    "QuantityValue": "qudt:QuantityValue",
    "affiliation": "https://schema.org/affiliation",
    "Unit": "qudt:Unit",
    "Line": "http://www.opengis.net/ont/sf#Line",
    "member": {
      "@id": "http://xmlns.com/foaf/0.1/member",
      "@type": "@id"
    },
    "versionInfo": "http://www.w3.org/2002/07/owl#versionInfo",
    "generatedAtTime": {
      "@id": "prov:generatedAtTime",
      "@type": "xsd:dateTime"
    },
    "example": "skos:example",
    "Slice": "http://purl.org/linked-data/cube#Slice",
    "Concentration": "http://purl.oclc.org/NET/ssnx/qu/dim#Concentration",
    "dataSet": {
      "@id": "http://purl.org/linked-data/cube#dataSet",
      "@type": "@id"
    },
    "componentAttachment": {
      "@id": "http://purl.org/linked-data/cube#componentAttachment",
      "@type": "@id"
    },
    "concept": {
      "@id": "http://purl.org/linked-data/cube#concept",
      "@type": "@id"
    },
    "MultiSurface": "http://www.opengis.net/ont/sf#MultiSurface",
    "TemporalDuration": "owlTime:TemporalDuration",
    "Procedure": "sosa:Procedure",
    "DiffusionCoefficient": "http://purl.oclc.org/NET/ssnx/qu/dim#DiffusionCoefficient",
    "asGeoJSON": {
      "@id": "http://www.opengis.net/ont/geosparql#asGeoJSON",
      "@type": "http://www.opengis.net/ont/geosparql#geoJSONLiteral"
    },
    "Organization": "https://schema.org/Organization",
    "Volume": "http://purl.oclc.org/NET/ssnx/qu/dim#Volume",
    "Thing": "http://www.w3.org/2002/07/owl#Thing",
    "GFI_Feature": "http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_Feature",
    "AttributeProperty": "http://purl.org/linked-data/cube#AttributeProperty",
    "quantityValue": {
      "@id": "qudt:quantityValue",
      "@type": "@id"
    },
    "TemporalUnit": "owlTime:TemporalUnit",
    "asWKT": {
      "@id": "http://www.opengis.net/ont/geosparql#asWKT",
      "@type": "http://www.opengis.net/ont/geosparql#wktLiteral"
    },
    "Angle": "http://purl.oclc.org/NET/ssnx/qu/dim#Angle",
    "TemperatureDrift": "http://purl.oclc.org/NET/ssnx/qu/dim#TemperatureDrift",
    "RotationalSpeed": "http://purl.oclc.org/NET/ssnx/qu/dim#RotationalSpeed",
    "ComponentProperty": "http://purl.org/linked-data/cube#ComponentProperty",
    "Class": "rdfs:Class",
    "Geometry": "http://www.opengis.net/ont/geosparql#Geometry",
    "NumberPerArea": "http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerArea",
    "depiction": "http://xmlns.com/foaf/0.1/depiction",
    "Curve": "http://www.opengis.net/ont/sf#Curve",
    "Instant": "owlTime:Instant",
    "maker": "http://xmlns.com/foaf/0.1/maker",
    "sfWithin": {
      "@id": "http://www.opengis.net/ont/geosparql#sfWithin",
      "@type": "@id"
    },
    "hasBoundingBox": {
      "@id": "http://www.opengis.net/ont/geosparql#hasBoundingBox",
      "@type": "@id"
    },
    "ThermalConductivity": "http://purl.oclc.org/NET/ssnx/qu/dim#ThermalConductivity",
    "domainIncludes": "https://schema.org/domainIncludes",
    "long": "http://www.w3.org/2003/01/geo/wgs84_pos#long",
    "numericValue": "qudt:numericValue",
    "Concept": "skos:Concept",
    "component": {
      "@id": "http://purl.org/linked-data/cube#component",
      "@type": "@id"
    },
    "measure": {
      "@id": "http://purl.org/linked-data/cube#measure",
      "@type": "@id"
    },
    "attribute": {
      "@id": "http://purl.org/linked-data/cube#attribute",
      "@type": "@id"
    },
    "structure": {
      "@id": "http://purl.org/linked-data/cube#structure",
      "@type": "@id"
    },
    "SliceKey": "http://purl.org/linked-data/cube#SliceKey",
    "Result": "sosa:Result",
    "Compressibility": "http://purl.oclc.org/NET/ssnx/qu/dim#Compressibility",
    "ComponentSet": "http://purl.org/linked-data/cube#ComponentSet",
    "MassPerTimePerArea": "http://purl.oclc.org/NET/ssnx/qu/dim#MassPerTimePerArea",
    "numericDuration": {
      "@id": "owlTime:numericDuration",
      "@type": "xsd:decimal"
    },
    "ElectricConductivity": "http://purl.oclc.org/NET/ssnx/qu/dim#ElectricConductivity",
    "Temperature": "http://purl.oclc.org/NET/ssnx/qu/dim#Temperature",
    "homepage": "http://xmlns.com/foaf/0.1/homepage",
    "Measure": "http://def.seegrid.csiro.au/isotc211/iso19103/2005/basic#Measure",
    "Person": "http://xmlns.com/foaf/0.1/Person",
    "Triangle": "http://www.opengis.net/ont/sf#Triangle",
    "note": "skos:note",
    "observationGroup": {
      "@id": "http://purl.org/linked-data/cube#observationGroup",
      "@type": "@id"
    },
    "Interval": "owlTime:Interval",
    "EnergyFlux": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyFlux",
    "StressOrPressure": "http://purl.oclc.org/NET/ssnx/qu/dim#StressOrPressure",
    "VolumeDensityRate": "http://purl.oclc.org/NET/ssnx/qu/dim#VolumeDensityRate",
    "Agent": "http://xmlns.com/foaf/0.1/Agent",
    "creator": "dct:creator",
    "Energy": "http://purl.oclc.org/NET/ssnx/qu/dim#Energy",
    "foaf.name": "http://xmlns.com/foaf/0.1/name",
    "Role": "https://schema.org/Role",
    "hasSerialization": {
      "@id": "http://www.opengis.net/ont/geosparql#hasSerialization",
      "@type": "rdfs:Literal"
    },
    "hasTime": {
      "@id": "owlTime:hasTime",
      "@type": "@id"
    },
    "SF_SamplingFeature.sampledFeature": {
      "@id": "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature.sampledFeature",
      "@type": "@id"
    },
    "rangeIncludes": "https://schema.org/rangeIncludes",
    "Mass": "http://purl.oclc.org/NET/ssnx/qu/dim#Mass",
    "location": {
      "@id": "http://www.w3.org/2003/01/geo/wgs84_pos#location",
      "@type": "@id"
    },
    "ComponentSpecification": "http://purl.org/linked-data/cube#ComponentSpecification",
    "Scheme": "skos:Scheme",
    "hasEnd": {
      "@id": "owlTime:hasEnd",
      "@type": "@id"
    },
    "rights": "dct:rights",
    "TemporalEntity": "owlTime:TemporalEntity",
    "hasBeginning": {
      "@id": "owlTime:hasBeginning",
      "@type": "@id"
    },
    "SF_SamplingFeature": "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature",
    "DimensionProperty": "http://purl.org/linked-data/cube#DimensionProperty",
    "alt": "http://www.w3.org/2003/01/geo/wgs84_pos#alt",
    "Acceleration": "http://purl.oclc.org/NET/ssnx/qu/dim#Acceleration",
    "identifier": "dct:identifier",
    "Quantity": "qudt:Quantity",
    "MassFlowRate": "http://purl.oclc.org/NET/ssnx/qu/dim#MassFlowRate",
    "qu.QuantityKind": "http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind",
    "SpatialObjectCollection": "http://www.opengis.net/ont/geosparql#SpatialObjectCollection",
    "Distance": "http://purl.oclc.org/NET/ssnx/qu/dim#Distance",
    "deprecated": "http://www.w3.org/2002/07/owl#deprecated",
    "Radiance": "http://purl.oclc.org/NET/ssnx/qu/dim#Radiance",
    "Duration": "owlTime:Duration",
    "TIN": "http://www.opengis.net/ont/sf#TIN",
    "SurfaceDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#SurfaceDensity",
    "isDefinedBy": "rdfs:isDefinedBy",
    "wgs84.Point": "http://www.w3.org/2003/01/geo/wgs84_pos#Point",
    "definition": "skos:definition",
    "editorialNote": "skos:editorialNote",
    "order": {
      "@id": "http://purl.org/linked-data/cube#order",
      "@type": "xsd:int"
    },
    "hasGeometry": {
      "@id": "http://www.opengis.net/ont/geosparql#hasGeometry",
      "@type": "@id"
    },
    "ssn.Property": "ssn:Property",
    "sfContains": {
      "@id": "http://www.opengis.net/ont/geosparql#sfContains",
      "@type": "@id"
    },
    "title": "dct:title",
    "Density": "http://purl.oclc.org/NET/ssnx/qu/dim#Density",
    "LinearRing": "http://www.opengis.net/ont/sf#LinearRing",
    "Molality": "http://purl.oclc.org/NET/ssnx/qu/dim#Molality",
    "inXSDDateTimeStamp": {
      "@id": "owlTime:inXSDDateTimeStamp",
      "@type": "xsd:dateTimeStamp"
    },
    "MeasureProperty": "http://purl.org/linked-data/cube#MeasureProperty",
    "PropertyKind": "http://purl.oclc.org/NET/ssnx/qu/qu#PropertyKind",
    "SpatialObject": "http://www.opengis.net/ont/geosparql#SpatialObject",
    "sliceStructure": {
      "@id": "http://purl.org/linked-data/cube#sliceStructure",
      "@type": "@id"
    },
    "NumberPerLength": "http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerLength",
    "lat": "http://www.w3.org/2003/01/geo/wgs84_pos#lat",
    "VolumeFlowRate": "http://purl.oclc.org/NET/ssnx/qu/dim#VolumeFlowRate",
    "SpecificEntropy": "http://purl.oclc.org/NET/ssnx/qu/dim#SpecificEntropy",
    "CodedProperty": "http://purl.org/linked-data/cube#CodedProperty",
    "slice": {
      "@id": "http://purl.org/linked-data/cube#slice",
      "@type": "@id"
    },
    "unit": {
      "@id": "qudt:unit",
      "@type": "@id"
    },
    "date": "dct:date",
    "seeAlso": "rdfs:seeAlso",
    "ObservationGroup": "http://purl.org/linked-data/cube#ObservationGroup",
    "DataSet": "http://purl.org/linked-data/cube#DataSet",
    "comment": "rdfs:comment",
    "PolyhedralSurface": "http://www.opengis.net/ont/sf#PolyhedralSurface",
    "contributor": "dct:contributor",
    "unitKind": {
      "@id": "http://purl.oclc.org/NET/ssnx/qu/qu#unitKind",
      "@type": "@id"
    },
    "dimension": {
      "@id": "http://purl.org/linked-data/cube#dimension",
      "@type": "@id"
    },
    "RadianceExposure": "http://purl.oclc.org/NET/ssnx/qu/dim#RadianceExposure",
    "VelocityOrSpeed": "http://purl.oclc.org/NET/ssnx/qu/dim#VelocityOrSpeed",
    "inXSDDate": {
      "@id": "owlTime:inXSDDate",
      "@type": "xsd:date"
    },
    "GFI_DomainFeature": "http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_DomainFeature",
    "observation": {
      "@id": "http://purl.org/linked-data/cube#observation",
      "@type": "@id"
    },
    "Dimensionless": "http://purl.oclc.org/NET/ssnx/qu/dim#Dimensionless",
    "Area": "http://purl.oclc.org/NET/ssnx/qu/dim#Area",
    "Power": "http://purl.oclc.org/NET/ssnx/qu/dim#Power",
    "OM_Observation": "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation",
    "prefLabel": "skos:prefLabel",
    "Surface": "http://www.opengis.net/ont/sf#Surface",
    "sliceKey": {
      "@id": "http://purl.org/linked-data/cube#sliceKey",
      "@type": "@id"
    },
    "inScheme": "skos:inScheme",
    "dct.description": "dct:description",
    "MultiCurve": "http://www.opengis.net/ont/sf#MultiCurve",
    "hasQuantityKind": {
      "@id": "qudt:hasQuantityKind",
      "@type": "@id"
    },
    "DataStructureDefinition": "http://purl.org/linked-data/cube#DataStructureDefinition",
    "qb.Observation": "http://purl.org/linked-data/cube#Observation",
    "EnergyDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyDensity",
    "unitType": {
      "@id": "owlTime:unitType",
      "@type": "@id"
    },
    "componentProperty": {
      "@id": "http://purl.org/linked-data/cube#componentProperty",
      "@type": "@id"
    },
    "sf.Geometry": "http://www.opengis.net/ont/sf#Geometry",
    "schema.Person": "https://schema.org/Person",
    "schema.name": "https://schema.org/name",
    "QuantityKind": "qudt:QuantityKind",
    "href": "@id",
    "rel": "geojson:rel",
    "created": "dct:created",
    "updated": "dct:modified",
    "language": "dct:language",
    "code": "dct:identifier",
    "license": "dct:license",
    "keywords": {
      "@id": "dcat:keyword",
      "@container": "@set"
    },
    "themes": {
      "@id": "dcat:theme",
      "@container": "@set"
    },
    "concepts": {
      "@id": "skos:Concept",
      "@container": "@set"
    },
    "scheme": "skos:inScheme",
    "formats": {
      "@id": "dct:format",
      "@container": "@set"
    },
    "mediaType": "dct:format",
    "conformsTo": {
      "@id": "dct:conformsTo",
      "@type": "@id",
      "@container": "@set"
    },
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn-system": "ssn:systems/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "iliad": "https://w3id.org/iliad/property/",
    "geojson": "https://purl.org/geojson/vocab#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "owlTime": "http://www.w3.org/2006/time#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "seadots": "https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr#",
    "qudt": "http://qudt.org/schema/qudt/",
    "dwc": "http://rs.tdwg.org/dwc/terms/",
    "indo": "https://w3id.org/indicators/marine/obs/",
    "prov": "http://www.w3.org/ns/prov#",
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

