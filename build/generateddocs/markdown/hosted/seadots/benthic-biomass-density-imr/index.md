
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
      "source": "https://marbunn-ekstern.hi.no/apps/marbunn/v1/getmapforcatch?species={scientificName}&cruise=",
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
          "2008104",
          "2008114",
          "2009105",
          "2009111",
          "2010110",
          "2010112",
          "2011105",
          "2011110",
          "2011113",
          "2012106",
          "2012110",
          "2013110",
          "2013112",
          "2013205",
          "2014106",
          "2014115",
          "2014208",
          "2015109",
          "2015113",
          "2016113",
          "2017103",
          "2017112",
          "2017115",
          "2018109",
          "2019106",
          "2019115",
          "2020104",
          "2020110",
          "2021103",
          "2021104",
          "2021115",
          "2022118",
          "2022708",
          "2022846",
          "2023001005",
          "2023001009",
          "2023001014",
          "2024001021",
          "2024007003",
          "2024007005",
          "2025001009",
          "2026007006"
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
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022708",
              "2024001021",
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
          },
          {
            "scientificName": "Anthozoa",
            "totalWeight_kg": 3406.718,
            "samplesWithWeight": 37,
            "samplesInAOI": 184,
            "totalIndividuals": 90,
            "cruises": [
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2023001005"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lycodes esmarkii",
            "totalWeight_kg": 2040.7,
            "samplesWithWeight": 4,
            "samplesInAOI": 12,
            "totalIndividuals": 4,
            "cruises": [
              "2009105",
              "2013112",
              "2014208",
              "2017115",
              "2021104",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lophius piscatorius",
            "totalWeight_kg": 1408.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 1,
            "cruises": [
              "2007105",
              "2012110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Sebastes norvegicus",
            "totalWeight_kg": 1405.0,
            "samplesWithWeight": 2,
            "samplesInAOI": 5,
            "totalIndividuals": 2,
            "cruises": [
              "2006612",
              "2007111",
              "2011105",
              "2015113",
              "2016113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Amblyraja hyperborea",
            "totalWeight_kg": 916.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 6,
            "totalIndividuals": 1,
            "cruises": [
              "2009105",
              "2011113",
              "2012106",
              "2014208",
              "2015113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Amblyraja radiata",
            "totalWeight_kg": 826.0,
            "samplesWithWeight": 2,
            "samplesInAOI": 17,
            "totalIndividuals": 4,
            "cruises": [
              "2007105",
              "2010110",
              "2013112",
              "2014106",
              "2014115",
              "2019106",
              "2019115",
              "2021115",
              "2022708",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Sebastes viviparus",
            "totalWeight_kg": 776.99,
            "samplesWithWeight": 3,
            "samplesInAOI": 11,
            "totalIndividuals": 4,
            "cruises": [
              "2007105",
              "2007111",
              "2010112",
              "2011113",
              "2012106",
              "2013112",
              "2014106",
              "2015113",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lycodes squamiventer",
            "totalWeight_kg": 604.72,
            "samplesWithWeight": 6,
            "samplesInAOI": 16,
            "totalIndividuals": 64,
            "cruises": [
              "2008104",
              "2008114",
              "2010110",
              "2010112",
              "2011113",
              "2012106",
              "2013112",
              "2013205",
              "2014208"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Laetmonice producta",
            "totalWeight_kg": 564.295,
            "samplesWithWeight": 12,
            "samplesInAOI": 14,
            "totalIndividuals": 226,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2009105",
              "2013205"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Laetmonice filicornis",
            "totalWeight_kg": 552.63,
            "samplesWithWeight": 61,
            "samplesInAOI": 173,
            "totalIndividuals": 409,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Kophobelemnon stelliferum",
            "totalWeight_kg": 509.818,
            "samplesWithWeight": 16,
            "samplesInAOI": 72,
            "totalIndividuals": 360,
            "cruises": [
              "2007105",
              "2007111",
              "2008114",
              "2009105",
              "2010110",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118",
              "2023001009",
              "2024007003"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Zoantharia",
            "totalWeight_kg": 395.369,
            "samplesWithWeight": 75,
            "samplesInAOI": 118,
            "totalIndividuals": 2436,
            "cruises": [
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2015109",
              "2019115",
              "2021103"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Urasterias lincki",
            "totalWeight_kg": 338.123,
            "samplesWithWeight": 1,
            "samplesInAOI": 26,
            "totalIndividuals": 27,
            "cruises": [
              "2007105",
              "2014115",
              "2016113",
              "2018109",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Lithodes maja",
            "totalWeight_kg": 224.584,
            "samplesWithWeight": 8,
            "samplesInAOI": 17,
            "totalIndividuals": 16,
            "cruises": [
              "2006612",
              "2007105",
              "2009105",
              "2010110",
              "2010112",
              "2011105",
              "2013110",
              "2013205",
              "2014106",
              "2015113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Trisopterus esmarkii",
            "totalWeight_kg": 173.068,
            "samplesWithWeight": 9,
            "samplesInAOI": 22,
            "totalIndividuals": 11,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2010112",
              "2011105",
              "2011113",
              "2012110",
              "2020104",
              "2023001009",
              "2023001014",
              "2024001021"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Artediellus atlanticus",
            "totalWeight_kg": 133.103,
            "samplesWithWeight": 19,
            "samplesInAOI": 59,
            "totalIndividuals": 77,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2012106",
              "2013110",
              "2013112",
              "2014106",
              "2015109",
              "2015113",
              "2016113",
              "2017112",
              "2017115",
              "2019115",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leptychaster arcticus",
            "totalWeight_kg": 126.363,
            "samplesWithWeight": 20,
            "samplesInAOI": 56,
            "totalIndividuals": 154,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2013110",
              "2014106",
              "2014115",
              "2017103",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Anarhichas lupus",
            "totalWeight_kg": 111.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 3,
            "totalIndividuals": 1,
            "cruises": [
              "2007105",
              "2014106",
              "2020104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lycodes frigidus",
            "totalWeight_kg": 99.0,
            "samplesWithWeight": 2,
            "samplesInAOI": 19,
            "totalIndividuals": 5,
            "cruises": [
              "2008104",
              "2008114",
              "2009111",
              "2010112",
              "2012106",
              "2026007006"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lebbeus polaris",
            "totalWeight_kg": 94.849,
            "samplesWithWeight": 49,
            "samplesInAOI": 155,
            "totalIndividuals": 212,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014208",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Anarhichas minor",
            "totalWeight_kg": 65.193,
            "samplesWithWeight": 2,
            "samplesInAOI": 2,
            "totalIndividuals": 3,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Volutopsius norwegicus",
            "totalWeight_kg": 65.07,
            "samplesWithWeight": 2,
            "samplesInAOI": 9,
            "totalIndividuals": 4,
            "cruises": [
              "2008104",
              "2009105",
              "2013112",
              "2013205",
              "2015113",
              "2016113",
              "2019115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Umbellula",
            "totalWeight_kg": 51.77,
            "samplesWithWeight": 2,
            "samplesInAOI": 3,
            "totalIndividuals": 4,
            "cruises": [
              "2008104",
              "2009105",
              "2013205"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Lycodonus flagellicauda",
            "totalWeight_kg": 49.54,
            "samplesWithWeight": 7,
            "samplesInAOI": 18,
            "totalIndividuals": 21,
            "cruises": [
              "2008104",
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2012106",
              "2013112",
              "2014208",
              "2015113",
              "2019115",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Tunicata",
            "totalWeight_kg": 47.732,
            "samplesWithWeight": 18,
            "samplesInAOI": 27,
            "totalIndividuals": 67,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Asteronyx loveni",
            "totalWeight_kg": 46.802,
            "samplesWithWeight": 9,
            "samplesInAOI": 37,
            "totalIndividuals": 15,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2013112",
              "2020104",
              "2021103",
              "2021104",
              "2022118",
              "2023001009",
              "2025001009"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Turrisipho moebii",
            "totalWeight_kg": 44.034,
            "samplesWithWeight": 5,
            "samplesInAOI": 20,
            "totalIndividuals": 16,
            "cruises": [
              "2008104",
              "2009105",
              "2009111",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014208",
              "2015113",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lycodes paamiuti",
            "totalWeight_kg": 44.0,
            "samplesWithWeight": 4,
            "samplesInAOI": 5,
            "totalIndividuals": 8,
            "cruises": [
              "2008104",
              "2009111",
              "2010110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Karnekampia sulcata",
            "totalWeight_kg": 36.109,
            "samplesWithWeight": 23,
            "samplesInAOI": 146,
            "totalIndividuals": 99,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2019106",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Limopsis angusta",
            "totalWeight_kg": 34.054,
            "samplesWithWeight": 52,
            "samplesInAOI": 93,
            "totalIndividuals": 472,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2009105",
              "2009111",
              "2010110",
              "2011113",
              "2012106"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Asterias rubens",
            "totalWeight_kg": 33.244,
            "samplesWithWeight": 3,
            "samplesInAOI": 10,
            "totalIndividuals": 4,
            "cruises": [
              "2006612",
              "2007111",
              "2010112",
              "2011105",
              "2013110",
              "2014106",
              "2023001009",
              "2024001021"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lycodes eudipleurostictus",
            "totalWeight_kg": 32.6,
            "samplesWithWeight": 2,
            "samplesInAOI": 17,
            "totalIndividuals": 4,
            "cruises": [
              "2009111",
              "2012106",
              "2013112",
              "2014208",
              "2015113",
              "2019106",
              "2021104",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Laonice",
            "totalWeight_kg": 27.602,
            "samplesWithWeight": 15,
            "samplesInAOI": 29,
            "totalIndividuals": 225,
            "cruises": [
              "2006612",
              "2007111",
              "2008104",
              "2008114",
              "2010112",
              "2012106",
              "2013112",
              "2013205",
              "2014208",
              "2015113",
              "2018109",
              "2019115",
              "2020104",
              "2020110",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Amathillopsis spinigera",
            "totalWeight_kg": 27.601,
            "samplesWithWeight": 5,
            "samplesInAOI": 43,
            "totalIndividuals": 41,
            "cruises": [
              "2008104",
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2011113",
              "2012106",
              "2013112",
              "2013205",
              "2014208",
              "2015113",
              "2019106",
              "2021104",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Anonyx nugax",
            "totalWeight_kg": 27.397,
            "samplesWithWeight": 11,
            "samplesInAOI": 68,
            "totalIndividuals": 606,
            "cruises": [
              "2006612",
              "2008104",
              "2008114",
              "2010110",
              "2012106",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2021103",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Actinopterygii",
            "totalWeight_kg": 27.149,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2007111"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Antho (Antho) dichotoma",
            "totalWeight_kg": 27.0,
            "samplesWithWeight": 3,
            "samplesInAOI": 26,
            "totalIndividuals": 6,
            "cruises": [
              "2008104",
              "2008114",
              "2010110",
              "2010112",
              "2011113",
              "2012106",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Abra longicallus",
            "totalWeight_kg": 25.051,
            "samplesWithWeight": 22,
            "samplesInAOI": 435,
            "totalIndividuals": 136,
            "cruises": [
              "2007105",
              "2007111",
              "2008114",
              "2009111",
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014208",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Aega psora",
            "totalWeight_kg": 25.039,
            "samplesWithWeight": 22,
            "samplesInAOI": 37,
            "totalIndividuals": 37,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2010110",
              "2010112",
              "2011105",
              "2011113",
              "2012106",
              "2013112",
              "2014106",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Aphrodita aculeata",
            "totalWeight_kg": 23.154,
            "samplesWithWeight": 20,
            "samplesInAOI": 36,
            "totalIndividuals": 55,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2012106",
              "2012110",
              "2013112",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Antalis entalis",
            "totalWeight_kg": 22.965,
            "samplesWithWeight": 60,
            "samplesInAOI": 164,
            "totalIndividuals": 334,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2011105",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Melanogrammus aeglefinus",
            "totalWeight_kg": 19.758,
            "samplesWithWeight": 1,
            "samplesInAOI": 4,
            "totalIndividuals": 1,
            "cruises": [
              "2006612",
              "2014106",
              "2020104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Troschelia berniciensis",
            "totalWeight_kg": 18.346,
            "samplesWithWeight": 2,
            "samplesInAOI": 2,
            "totalIndividuals": 2,
            "cruises": [
              "2006612",
              "2008114"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lycodes pallidus",
            "totalWeight_kg": 17.918,
            "samplesWithWeight": 2,
            "samplesInAOI": 19,
            "totalIndividuals": 4,
            "cruises": [
              "2006612",
              "2008114",
              "2009105",
              "2012106",
              "2013112",
              "2016113",
              "2018109",
              "2019115"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Anapagurus laevis",
            "totalWeight_kg": 17.767,
            "samplesWithWeight": 11,
            "samplesInAOI": 34,
            "totalIndividuals": 151,
            "cruises": [
              "2007111",
              "2008104",
              "2008114",
              "2010112",
              "2012106",
              "2013112",
              "2013205",
              "2014208",
              "2015113",
              "2020104",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Liljeborgia (Lilljeborgiella) fissicornis",
            "totalWeight_kg": 17.281,
            "samplesWithWeight": 75,
            "samplesInAOI": 272,
            "totalIndividuals": 1045,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2022846",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lumbrineridae",
            "totalWeight_kg": 15.131,
            "samplesWithWeight": 68,
            "samplesInAOI": 141,
            "totalIndividuals": 671,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011110",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Asperarca nodulosa",
            "totalWeight_kg": 14.839,
            "samplesWithWeight": 5,
            "samplesInAOI": 47,
            "totalIndividuals": 65,
            "cruises": [
              "2007111",
              "2008104",
              "2010110",
              "2011113",
              "2012106",
              "2013112",
              "2013205",
              "2014106",
              "2014208",
              "2015113",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Icelus bicornis",
            "totalWeight_kg": 13.178,
            "samplesWithWeight": 11,
            "samplesInAOI": 21,
            "totalIndividuals": 14,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2009111",
              "2010110",
              "2011110",
              "2014106",
              "2016113",
              "2018109",
              "2019106",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Unciola leucopis",
            "totalWeight_kg": 11.712,
            "samplesWithWeight": 54,
            "samplesInAOI": 246,
            "totalIndividuals": 5163,
            "cruises": [
              "2006612",
              "2007105",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011113",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2021103",
              "2021104",
              "2021115",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Vargula norvegica",
            "totalWeight_kg": 11.343,
            "samplesWithWeight": 62,
            "samplesInAOI": 116,
            "totalIndividuals": 7369,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111"
            ],
            "equipment": [
              "Beamtrawl",
              "Boxcorer",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Isidella lofotensis",
            "totalWeight_kg": 10.28,
            "samplesWithWeight": 2,
            "samplesInAOI": 10,
            "totalIndividuals": 2,
            "cruises": [
              "2007111",
              "2021103",
              "2024001021"
            ],
            "equipment": [
              "Beamtrawl",
              "Bioboks",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leptoclinides faeroensis",
            "totalWeight_kg": 9.942,
            "samplesWithWeight": 12,
            "samplesInAOI": 17,
            "totalIndividuals": 660,
            "cruises": [
              "2007111",
              "2009105",
              "2009111",
              "2012110",
              "2020104",
              "2021103",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Turrisipho voeringi",
            "totalWeight_kg": 9.723,
            "samplesWithWeight": 2,
            "samplesInAOI": 10,
            "totalIndividuals": 8,
            "cruises": [
              "2008104",
              "2008114",
              "2012106",
              "2013205",
              "2014208",
              "2016113",
              "2019106",
              "2024007005"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Luidia sarsii",
            "totalWeight_kg": 9.357,
            "samplesWithWeight": 9,
            "samplesInAOI": 74,
            "totalIndividuals": 35,
            "cruises": [
              "2007111",
              "2008104",
              "2008114",
              "2010110",
              "2010112",
              "2011110",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014208",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118",
              "2023001009",
              "2024001021"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Amage auricula",
            "totalWeight_kg": 9.086,
            "samplesWithWeight": 157,
            "samplesInAOI": 453,
            "totalIndividuals": 1170,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017115",
              "2018109",
              "2019106",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Turbellaria",
            "totalWeight_kg": 8.508,
            "samplesWithWeight": 14,
            "samplesInAOI": 27,
            "totalIndividuals": 35,
            "cruises": [
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2012106",
              "2013205",
              "2014106"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Aglaophamus malmgreni",
            "totalWeight_kg": 8.348,
            "samplesWithWeight": 26,
            "samplesInAOI": 255,
            "totalIndividuals": 109,
            "cruises": [
              "2006612",
              "2007105",
              "2008104",
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2011105",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2021103",
              "2021104",
              "2021115",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Boxcorer",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Turrisipho lachesis",
            "totalWeight_kg": 8.343,
            "samplesWithWeight": 2,
            "samplesInAOI": 42,
            "totalIndividuals": 10,
            "cruises": [
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014208",
              "2015113",
              "2016113",
              "2017103",
              "2019115",
              "2021103",
              "2021104",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aegiochus ventrosa",
            "totalWeight_kg": 8.19,
            "samplesWithWeight": 4,
            "samplesInAOI": 22,
            "totalIndividuals": 17,
            "cruises": [
              "2007105",
              "2007111",
              "2009105",
              "2010110",
              "2010112",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014115",
              "2015113"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Scyphozoa",
            "totalWeight_kg": 7.274,
            "samplesWithWeight": 5,
            "samplesInAOI": 10,
            "totalIndividuals": 29,
            "cruises": [
              "2008114",
              "2009105",
              "2009111",
              "2012106",
              "2015113",
              "2017112",
              "2019115"
            ],
            "equipment": [
              "Beamtrawl",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Korethraster hispidus",
            "totalWeight_kg": 7.157,
            "samplesWithWeight": 6,
            "samplesInAOI": 22,
            "totalIndividuals": 27,
            "cruises": [
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2012106",
              "2013112",
              "2013205",
              "2014208",
              "2019115",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Laeocochlis sinistrata",
            "totalWeight_kg": 6.985,
            "samplesWithWeight": 4,
            "samplesInAOI": 26,
            "totalIndividuals": 18,
            "cruises": [
              "2006612",
              "2007105",
              "2010112",
              "2011105",
              "2011113",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014208",
              "2015113",
              "2017103",
              "2021103",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Lycenchelys muraena",
            "totalWeight_kg": 6.634,
            "samplesWithWeight": 4,
            "samplesInAOI": 10,
            "totalIndividuals": 5,
            "cruises": [
              "2007111",
              "2008104",
              "2009105",
              "2010110",
              "2010112",
              "2013112",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Lycenchelys sarsii",
            "totalWeight_kg": 6.59,
            "samplesWithWeight": 5,
            "samplesInAOI": 19,
            "totalIndividuals": 11,
            "cruises": [
              "2007111",
              "2008104",
              "2009105",
              "2010110",
              "2011105",
              "2012106",
              "2014106",
              "2015113",
              "2020104",
              "2021104",
              "2023001009",
              "2024001021"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lycodes gracilis",
            "totalWeight_kg": 6.5,
            "samplesWithWeight": 2,
            "samplesInAOI": 9,
            "totalIndividuals": 3,
            "cruises": [
              "2008114",
              "2009105",
              "2010110",
              "2011105",
              "2017103",
              "2021104",
              "2021115",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Meganyctiphanes norvegica",
            "totalWeight_kg": 5.971,
            "samplesWithWeight": 17,
            "samplesInAOI": 18,
            "totalIndividuals": 31,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2011113",
              "2012106",
              "2012110"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Abra nitida",
            "totalWeight_kg": 5.883,
            "samplesWithWeight": 23,
            "samplesInAOI": 94,
            "totalIndividuals": 128,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2010110",
              "2011110",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014208",
              "2020104",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Triglops murrayi",
            "totalWeight_kg": 5.865,
            "samplesWithWeight": 3,
            "samplesInAOI": 25,
            "totalIndividuals": 3,
            "cruises": [
              "2006612",
              "2007111",
              "2010110",
              "2010112",
              "2012110",
              "2016113",
              "2017115",
              "2020104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Lycenchelys",
            "totalWeight_kg": 5.375,
            "samplesWithWeight": 5,
            "samplesInAOI": 6,
            "totalIndividuals": 8,
            "cruises": [
              "2006612",
              "2013112"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Laetmonice",
            "totalWeight_kg": 5.117,
            "samplesWithWeight": 3,
            "samplesInAOI": 20,
            "totalIndividuals": 12,
            "cruises": [
              "2006612",
              "2008104",
              "2008114",
              "2012110",
              "2013112",
              "2013205",
              "2014106",
              "2015113",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lycodes",
            "totalWeight_kg": 5.092,
            "samplesWithWeight": 2,
            "samplesInAOI": 19,
            "totalIndividuals": 2,
            "cruises": [
              "2006612",
              "2010112",
              "2011113",
              "2012106",
              "2013112",
              "2019106",
              "2019115",
              "2022118",
              "2022708",
              "2022846",
              "2024007003"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Leptasterias",
            "totalWeight_kg": 5.068,
            "samplesWithWeight": 3,
            "samplesInAOI": 7,
            "totalIndividuals": 50,
            "cruises": [
              "2006612",
              "2014106",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Amphictene auricoma",
            "totalWeight_kg": 4.693,
            "samplesWithWeight": 102,
            "samplesInAOI": 155,
            "totalIndividuals": 156,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014106",
              "2014208",
              "2015113",
              "2020104",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Amphilochoides boeckii",
            "totalWeight_kg": 4.085,
            "samplesWithWeight": 8,
            "samplesInAOI": 32,
            "totalIndividuals": 167,
            "cruises": [
              "2007105",
              "2007111",
              "2008114",
              "2010110",
              "2012110",
              "2013112",
              "2013205",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Anonyx",
            "totalWeight_kg": 3.872,
            "samplesWithWeight": 2,
            "samplesInAOI": 23,
            "totalIndividuals": 7,
            "cruises": [
              "2008104",
              "2009105",
              "2010112",
              "2015109",
              "2016113",
              "2019115",
              "2021104",
              "2021115",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Acanthotrochus mirabilis",
            "totalWeight_kg": 3.528,
            "samplesWithWeight": 16,
            "samplesInAOI": 44,
            "totalIndividuals": 269,
            "cruises": [
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010112",
              "2011113",
              "2012106",
              "2016113",
              "2019106",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Amphilochus manudens",
            "totalWeight_kg": 3.435,
            "samplesWithWeight": 78,
            "samplesInAOI": 235,
            "totalIndividuals": 8797,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2017103",
              "2017115",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2022846",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Yoldiella philippiana",
            "totalWeight_kg": 3.321,
            "samplesWithWeight": 27,
            "samplesInAOI": 87,
            "totalIndividuals": 577,
            "cruises": [
              "2008104",
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2011105",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014106",
              "2015113",
              "2021104",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leucon (Leucon) nathorsti",
            "totalWeight_kg": 3.01,
            "samplesWithWeight": 3,
            "samplesInAOI": 167,
            "totalIndividuals": 19,
            "cruises": [
              "2010110",
              "2011105",
              "2012106",
              "2013110",
              "2014106",
              "2014115",
              "2015109",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2021115",
              "2022118",
              "2022708",
              "2023001005",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Laonice sarsi",
            "totalWeight_kg": 2.881,
            "samplesWithWeight": 136,
            "samplesInAOI": 229,
            "totalIndividuals": 156,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014115",
              "2014208",
              "2015113",
              "2018109",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Turrisipho fenestratus",
            "totalWeight_kg": 2.793,
            "samplesWithWeight": 2,
            "samplesInAOI": 11,
            "totalIndividuals": 3,
            "cruises": [
              "2007111",
              "2009105",
              "2011105",
              "2011110",
              "2013112",
              "2013205",
              "2015113",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Unciola planipes",
            "totalWeight_kg": 2.683,
            "samplesWithWeight": 33,
            "samplesInAOI": 97,
            "totalIndividuals": 1458,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2019106",
              "2020104",
              "2021103",
              "2021104",
              "2023001005",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lumpenus lampretaeformis",
            "totalWeight_kg": 2.675,
            "samplesWithWeight": 1,
            "samplesInAOI": 7,
            "totalIndividuals": 1,
            "cruises": [
              "2006612",
              "2012106",
              "2017103",
              "2017112",
              "2017115",
              "2019115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lipobranchius jeffreysii",
            "totalWeight_kg": 2.398,
            "samplesWithWeight": 9,
            "samplesInAOI": 12,
            "totalIndividuals": 14,
            "cruises": [
              "2006612",
              "2010110",
              "2010112",
              "2012110",
              "2013205"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lumbriclymene cylindricauda",
            "totalWeight_kg": 2.339,
            "samplesWithWeight": 110,
            "samplesInAOI": 192,
            "totalIndividuals": 302,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Ascorhynchus abyssi",
            "totalWeight_kg": 2.159,
            "samplesWithWeight": 6,
            "samplesInAOI": 13,
            "totalIndividuals": 89,
            "cruises": [
              "2009111",
              "2010112",
              "2012106",
              "2015113"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Leptychaster",
            "totalWeight_kg": 2.14,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lophaster furcifer",
            "totalWeight_kg": 2.129,
            "samplesWithWeight": 8,
            "samplesInAOI": 21,
            "totalIndividuals": 11,
            "cruises": [
              "2006612",
              "2008104",
              "2008114",
              "2010110",
              "2011113",
              "2013112",
              "2013205",
              "2014106",
              "2016113",
              "2018109",
              "2019115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Abyssoninoe scopa",
            "totalWeight_kg": 2.013,
            "samplesWithWeight": 76,
            "samplesInAOI": 305,
            "totalIndividuals": 179,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Boxcorer",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Macrocypris minna",
            "totalWeight_kg": 2.011,
            "samplesWithWeight": 19,
            "samplesInAOI": 30,
            "totalIndividuals": 2299,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2009105",
              "2009111"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Macrocypria sarsi",
            "totalWeight_kg": 1.95,
            "samplesWithWeight": 11,
            "samplesInAOI": 14,
            "totalIndividuals": 4147,
            "cruises": [
              "2006612",
              "2007105",
              "2008114",
              "2009105",
              "2009111"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Andaniexis lupus",
            "totalWeight_kg": 1.776,
            "samplesWithWeight": 15,
            "samplesInAOI": 15,
            "totalIndividuals": 1153,
            "cruises": [
              "2007105",
              "2007111"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Sertularella",
            "totalWeight_kg": 1.675,
            "samplesWithWeight": 5,
            "samplesInAOI": 8,
            "totalIndividuals": 7,
            "cruises": [
              "2007111",
              "2008104",
              "2008114",
              "2012110",
              "2019115",
              "2021103"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Amphicteis gunneri",
            "totalWeight_kg": 1.625,
            "samplesWithWeight": 82,
            "samplesInAOI": 251,
            "totalIndividuals": 108,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Mesothuria intestinalis",
            "totalWeight_kg": 1.591,
            "samplesWithWeight": 2,
            "samplesInAOI": 31,
            "totalIndividuals": 2,
            "cruises": [
              "2006612",
              "2007105",
              "2012110",
              "2013112",
              "2014106",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2020104",
              "2021104",
              "2022118",
              "2022846",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Urothoe elegans",
            "totalWeight_kg": 1.566,
            "samplesWithWeight": 67,
            "samplesInAOI": 240,
            "totalIndividuals": 1755,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2017103",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022846",
              "2023001005",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Trivia arctica",
            "totalWeight_kg": 1.513,
            "samplesWithWeight": 4,
            "samplesInAOI": 13,
            "totalIndividuals": 7,
            "cruises": [
              "2006612",
              "2007111",
              "2012106",
              "2015113",
              "2020104",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lyonsiella abyssicola",
            "totalWeight_kg": 1.473,
            "samplesWithWeight": 15,
            "samplesInAOI": 181,
            "totalIndividuals": 55,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2015113",
              "2016113",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Limatula gwyni",
            "totalWeight_kg": 1.407,
            "samplesWithWeight": 18,
            "samplesInAOI": 86,
            "totalIndividuals": 52,
            "cruises": [
              "2006612",
              "2007105",
              "2008104",
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2015113",
              "2019106",
              "2020110",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Liomesus",
            "totalWeight_kg": 1.388,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2007111"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Amphiuridae",
            "totalWeight_kg": 1.357,
            "samplesWithWeight": 2,
            "samplesInAOI": 23,
            "totalIndividuals": 2,
            "cruises": [
              "2006612",
              "2007111",
              "2010110",
              "2013205",
              "2014106",
              "2014208",
              "2016113",
              "2019106",
              "2019115",
              "2021103",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Liomesus ovum",
            "totalWeight_kg": 1.344,
            "samplesWithWeight": 1,
            "samplesInAOI": 3,
            "totalIndividuals": 1,
            "cruises": [
              "2007111",
              "2011113",
              "2021103"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Amphipholis squamata",
            "totalWeight_kg": 1.339,
            "samplesWithWeight": 48,
            "samplesInAOI": 307,
            "totalIndividuals": 504,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2015113",
              "2016113",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Weltnerium stroemii",
            "totalWeight_kg": 1.326,
            "samplesWithWeight": 18,
            "samplesInAOI": 77,
            "totalIndividuals": 107,
            "cruises": [
              "2006612",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2017103",
              "2019106",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Tryphosites longipes",
            "totalWeight_kg": 1.302,
            "samplesWithWeight": 52,
            "samplesInAOI": 92,
            "totalIndividuals": 258,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2010110",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2014106",
              "2014208",
              "2015113",
              "2020104",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Aoridae",
            "totalWeight_kg": 1.289,
            "samplesWithWeight": 28,
            "samplesInAOI": 135,
            "totalIndividuals": 2007,
            "cruises": [
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118",
              "2022708",
              "2022846",
              "2023001005",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Amphiura filiformis",
            "totalWeight_kg": 1.146,
            "samplesWithWeight": 12,
            "samplesInAOI": 22,
            "totalIndividuals": 33,
            "cruises": [
              "2006612",
              "2007105",
              "2009105",
              "2012106",
              "2012110",
              "2013205",
              "2016113"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Amphiura otteri",
            "totalWeight_kg": 1.113,
            "samplesWithWeight": 8,
            "samplesInAOI": 11,
            "totalIndividuals": 19,
            "cruises": [
              "2006612",
              "2008114",
              "2009105",
              "2013205"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Ampelisca odontoplax",
            "totalWeight_kg": 1.032,
            "samplesWithWeight": 16,
            "samplesInAOI": 32,
            "totalIndividuals": 36,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2011105",
              "2012106",
              "2012110",
              "2013110",
              "2014115",
              "2016113",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Ampharete finmarchica",
            "totalWeight_kg": 0.944,
            "samplesWithWeight": 35,
            "samplesInAOI": 103,
            "totalIndividuals": 273,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2018109",
              "2019106",
              "2019115",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Ampelisca macrocephala",
            "totalWeight_kg": 0.936,
            "samplesWithWeight": 16,
            "samplesInAOI": 89,
            "totalIndividuals": 47,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2012110",
              "2013110",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2019106",
              "2020104",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leucon (Alytoleucon) pallidus",
            "totalWeight_kg": 0.928,
            "samplesWithWeight": 29,
            "samplesInAOI": 37,
            "totalIndividuals": 2516,
            "cruises": [
              "2006612",
              "2007111",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011113",
              "2012106",
              "2017112",
              "2017115",
              "2018109",
              "2020104",
              "2021115",
              "2023001009"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Sigalion mathildae",
            "totalWeight_kg": 0.916,
            "samplesWithWeight": 2,
            "samplesInAOI": 2,
            "totalIndividuals": 2,
            "cruises": [
              "2008104",
              "2008114"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Tryphosella umbonata",
            "totalWeight_kg": 0.911,
            "samplesWithWeight": 4,
            "samplesInAOI": 7,
            "totalIndividuals": 9,
            "cruises": [
              "2007111",
              "2010110",
              "2011113",
              "2012106",
              "2015113",
              "2020104",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ampelisca",
            "totalWeight_kg": 0.889,
            "samplesWithWeight": 76,
            "samplesInAOI": 399,
            "totalIndividuals": 365,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2016113",
              "2017103",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2022846",
              "2023001005",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Weltnerium nymphocola",
            "totalWeight_kg": 0.885,
            "samplesWithWeight": 5,
            "samplesInAOI": 34,
            "totalIndividuals": 61,
            "cruises": [
              "2009105",
              "2009111",
              "2010112",
              "2011105",
              "2011113",
              "2012106",
              "2013112",
              "2013205",
              "2015113",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Leptostylis longimana",
            "totalWeight_kg": 0.883,
            "samplesWithWeight": 48,
            "samplesInAOI": 117,
            "totalIndividuals": 1682,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014208",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118",
              "2022708",
              "2023001005",
              "2023001009",
              "2024001021",
              "2024007003"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lumbriclymene minor",
            "totalWeight_kg": 0.876,
            "samplesWithWeight": 31,
            "samplesInAOI": 89,
            "totalIndividuals": 115,
            "cruises": [
              "2008114",
              "2009111",
              "2010110",
              "2010112",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2015113",
              "2016113",
              "2017103",
              "2017115",
              "2018109",
              "2019115",
              "2020110",
              "2021103",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Ampharete",
            "totalWeight_kg": 0.805,
            "samplesWithWeight": 17,
            "samplesInAOI": 66,
            "totalIndividuals": 75,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2010110",
              "2010112",
              "2011105",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2016113",
              "2017115",
              "2019115",
              "2020110",
              "2021103",
              "2021104",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lafoea dumosa",
            "totalWeight_kg": 0.803,
            "samplesWithWeight": 5,
            "samplesInAOI": 15,
            "totalIndividuals": 4,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2020104",
              "2021103",
              "2022118",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Stylocordyla",
            "totalWeight_kg": 0.798,
            "samplesWithWeight": 1,
            "samplesInAOI": 5,
            "totalIndividuals": 15,
            "cruises": [
              "2007111",
              "2009111",
              "2010110",
              "2010112",
              "2012110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Amigdoscalpellum hispidum",
            "totalWeight_kg": 0.795,
            "samplesWithWeight": 10,
            "samplesInAOI": 59,
            "totalIndividuals": 67,
            "cruises": [
              "2006612",
              "2007105",
              "2008104",
              "2009105",
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2013112",
              "2013205",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Liljeborgia",
            "totalWeight_kg": 0.75,
            "samplesWithWeight": 26,
            "samplesInAOI": 61,
            "totalIndividuals": 186,
            "cruises": [
              "2006612",
              "2007111",
              "2008104",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2015113",
              "2020104",
              "2020110",
              "2021104",
              "2021115",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lanice conchilega",
            "totalWeight_kg": 0.724,
            "samplesWithWeight": 16,
            "samplesInAOI": 25,
            "totalIndividuals": 6,
            "cruises": [
              "2007111",
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2011110",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014208",
              "2017103",
              "2020104",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leptoclinus maculatus",
            "totalWeight_kg": 0.703,
            "samplesWithWeight": 1,
            "samplesInAOI": 19,
            "totalIndividuals": 1,
            "cruises": [
              "2007105",
              "2010110",
              "2010112",
              "2014106",
              "2016113",
              "2017103",
              "2017112",
              "2018109",
              "2019115",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Apomatus globifer",
            "totalWeight_kg": 0.692,
            "samplesWithWeight": 4,
            "samplesInAOI": 19,
            "totalIndividuals": 18,
            "cruises": [
              "2006612",
              "2010110",
              "2010112",
              "2013205",
              "2015113",
              "2019115",
              "2021103",
              "2021104",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Tryphosella spitzbergensis",
            "totalWeight_kg": 0.682,
            "samplesWithWeight": 2,
            "samplesInAOI": 2,
            "totalIndividuals": 584,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Leptochiton asellus",
            "totalWeight_kg": 0.633,
            "samplesWithWeight": 8,
            "samplesInAOI": 18,
            "totalIndividuals": 14,
            "cruises": [
              "2006612",
              "2007111"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Yoldiella propinqua",
            "totalWeight_kg": 0.587,
            "samplesWithWeight": 18,
            "samplesInAOI": 184,
            "totalIndividuals": 49,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2016113",
              "2017103",
              "2017115",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021104",
              "2022708",
              "2022846",
              "2024007005"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Melphidippidae",
            "totalWeight_kg": 0.584,
            "samplesWithWeight": 19,
            "samplesInAOI": 29,
            "totalIndividuals": 802,
            "cruises": [
              "2007111",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2012106",
              "2013205",
              "2014106",
              "2014115"
            ],
            "equipment": [
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leptochiton",
            "totalWeight_kg": 0.559,
            "samplesWithWeight": 5,
            "samplesInAOI": 5,
            "totalIndividuals": 11,
            "cruises": [
              "2007105",
              "2007111",
              "2008104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Amythasides macroglossus",
            "totalWeight_kg": 0.547,
            "samplesWithWeight": 174,
            "samplesInAOI": 431,
            "totalIndividuals": 1977,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Jorunna tomentosa",
            "totalWeight_kg": 0.517,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Antedonidae",
            "totalWeight_kg": 0.513,
            "samplesWithWeight": 4,
            "samplesInAOI": 70,
            "totalIndividuals": 4,
            "cruises": [
              "2008104",
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014208",
              "2015113",
              "2017115",
              "2018109",
              "2019115",
              "2020104",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Ampelisca eschrichtii",
            "totalWeight_kg": 0.508,
            "samplesWithWeight": 14,
            "samplesInAOI": 134,
            "totalIndividuals": 3,
            "cruises": [
              "2006612",
              "2007111",
              "2009105",
              "2009111",
              "2010110",
              "2011105",
              "2011110",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2015109",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2021103",
              "2021104",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Sertulariidae",
            "totalWeight_kg": 0.504,
            "samplesWithWeight": 2,
            "samplesInAOI": 3,
            "totalIndividuals": 0,
            "cruises": [
              "2006612",
              "2007105",
              "2007111"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Lycodes adolfi",
            "totalWeight_kg": 0.5,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 1,
            "cruises": [
              "2009105",
              "2019115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lumbriclymene",
            "totalWeight_kg": 0.495,
            "samplesWithWeight": 12,
            "samplesInAOI": 95,
            "totalIndividuals": 44,
            "cruises": [
              "2007111",
              "2008114",
              "2009105",
              "2010110",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2016113",
              "2018109",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Admete viridula",
            "totalWeight_kg": 0.49,
            "samplesWithWeight": 4,
            "samplesInAOI": 79,
            "totalIndividuals": 5,
            "cruises": [
              "2008104",
              "2008114",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2022846",
              "2024007005"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Amblyops abbreviatus",
            "totalWeight_kg": 0.489,
            "samplesWithWeight": 16,
            "samplesInAOI": 160,
            "totalIndividuals": 87,
            "cruises": [
              "2007105",
              "2007111",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2016113",
              "2017103",
              "2019106",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Typhlomangelia nivalis",
            "totalWeight_kg": 0.488,
            "samplesWithWeight": 3,
            "samplesInAOI": 26,
            "totalIndividuals": 3,
            "cruises": [
              "2007111",
              "2008114",
              "2012110",
              "2013112",
              "2014106",
              "2014208",
              "2015113",
              "2017115",
              "2020104",
              "2020110",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Westwoodilla caecula",
            "totalWeight_kg": 0.485,
            "samplesWithWeight": 47,
            "samplesInAOI": 170,
            "totalIndividuals": 369,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014106",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2018109",
              "2019106",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lepechinella arctica",
            "totalWeight_kg": 0.478,
            "samplesWithWeight": 15,
            "samplesInAOI": 37,
            "totalIndividuals": 136,
            "cruises": [
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2010110",
              "2012106",
              "2013205",
              "2014106",
              "2014115",
              "2015113",
              "2017103",
              "2019106",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Amaeana trilobata",
            "totalWeight_kg": 0.469,
            "samplesWithWeight": 46,
            "samplesInAOI": 121,
            "totalIndividuals": 79,
            "cruises": [
              "2007105",
              "2008114",
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Scopelocheirus hopei",
            "totalWeight_kg": 0.456,
            "samplesWithWeight": 21,
            "samplesInAOI": 40,
            "totalIndividuals": 94,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2011105",
              "2012106",
              "2012110",
              "2014106",
              "2017103",
              "2019115",
              "2020104",
              "2020110",
              "2021104",
              "2022118",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Acanthicolepis asperrima",
            "totalWeight_kg": 0.413,
            "samplesWithWeight": 13,
            "samplesInAOI": 42,
            "totalIndividuals": 10,
            "cruises": [
              "2007111",
              "2010110",
              "2010112",
              "2012110",
              "2013112",
              "2013205",
              "2014106",
              "2015113",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Liparidae",
            "totalWeight_kg": 0.393,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 3,
            "cruises": [
              "2009105"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Zoarcidae",
            "totalWeight_kg": 0.374,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 1,
            "cruises": [
              "2007111",
              "2025001009"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Amphilochidae",
            "totalWeight_kg": 0.373,
            "samplesWithWeight": 21,
            "samplesInAOI": 126,
            "totalIndividuals": 1088,
            "cruises": [
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Astropectinidae",
            "totalWeight_kg": 0.361,
            "samplesWithWeight": 4,
            "samplesInAOI": 10,
            "totalIndividuals": 5,
            "cruises": [
              "2007111",
              "2020104",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Aora gracilis",
            "totalWeight_kg": 0.36,
            "samplesWithWeight": 6,
            "samplesInAOI": 6,
            "totalIndividuals": 526,
            "cruises": [
              "2006612",
              "2007105"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Amphithopsis longicaudata",
            "totalWeight_kg": 0.335,
            "samplesWithWeight": 12,
            "samplesInAOI": 60,
            "totalIndividuals": 273,
            "cruises": [
              "2007111",
              "2008104",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118",
              "2022708",
              "2022846",
              "2023001009"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Melphidippa macrura",
            "totalWeight_kg": 0.325,
            "samplesWithWeight": 25,
            "samplesInAOI": 50,
            "totalIndividuals": 76,
            "cruises": [
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2011110",
              "2012106",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2017103",
              "2019106",
              "2021104",
              "2023001005",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aeginella spinosa",
            "totalWeight_kg": 0.316,
            "samplesWithWeight": 16,
            "samplesInAOI": 24,
            "totalIndividuals": 61,
            "cruises": [
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2011105",
              "2011113",
              "2012106",
              "2019115",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Admete contabulata",
            "totalWeight_kg": 0.311,
            "samplesWithWeight": 2,
            "samplesInAOI": 2,
            "totalIndividuals": 3,
            "cruises": [
              "2009105",
              "2009111"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Asteriidae",
            "totalWeight_kg": 0.291,
            "samplesWithWeight": 1,
            "samplesInAOI": 7,
            "totalIndividuals": 1,
            "cruises": [
              "2009105",
              "2010112",
              "2011105",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ampelisca aequicornis",
            "totalWeight_kg": 0.285,
            "samplesWithWeight": 34,
            "samplesInAOI": 66,
            "totalIndividuals": 144,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2014106",
              "2020104",
              "2020110",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Margarites groenlandicus",
            "totalWeight_kg": 0.282,
            "samplesWithWeight": 2,
            "samplesInAOI": 31,
            "totalIndividuals": 3,
            "cruises": [
              "2007111",
              "2008104",
              "2010110",
              "2014106",
              "2016113",
              "2017103",
              "2018109",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Ampeliscidae",
            "totalWeight_kg": 0.273,
            "samplesWithWeight": 45,
            "samplesInAOI": 209,
            "totalIndividuals": 157,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2016113",
              "2017103",
              "2017115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Kroyera carinata",
            "totalWeight_kg": 0.272,
            "samplesWithWeight": 12,
            "samplesInAOI": 19,
            "totalIndividuals": 111,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2017103",
              "2018109",
              "2019115",
              "2020104",
              "2021104",
              "2021115",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Ilyarachna dubia",
            "totalWeight_kg": 0.272,
            "samplesWithWeight": 2,
            "samplesInAOI": 12,
            "totalIndividuals": 120,
            "cruises": [
              "2010112",
              "2012106",
              "2019106",
              "2019115",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leucothoe",
            "totalWeight_kg": 0.268,
            "samplesWithWeight": 5,
            "samplesInAOI": 7,
            "totalIndividuals": 32,
            "cruises": [
              "2009111",
              "2010110",
              "2010112"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ampharetidae",
            "totalWeight_kg": 0.262,
            "samplesWithWeight": 21,
            "samplesInAOI": 74,
            "totalIndividuals": 43,
            "cruises": [
              "2006612",
              "2007105",
              "2008104",
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2018109",
              "2019106",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Liljeborgia (Liljeborgia) brevicornis",
            "totalWeight_kg": 0.26,
            "samplesWithWeight": 4,
            "samplesInAOI": 5,
            "totalIndividuals": 149,
            "cruises": [
              "2006612",
              "2013205"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ampelisca gibba",
            "totalWeight_kg": 0.255,
            "samplesWithWeight": 19,
            "samplesInAOI": 44,
            "totalIndividuals": 6,
            "cruises": [
              "2007111",
              "2008114",
              "2012106",
              "2012110",
              "2013205",
              "2020104",
              "2020110",
              "2021104",
              "2022118",
              "2023001005",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Apherusa",
            "totalWeight_kg": 0.255,
            "samplesWithWeight": 3,
            "samplesInAOI": 15,
            "totalIndividuals": 37,
            "cruises": [
              "2010110",
              "2012106",
              "2012110",
              "2013110",
              "2013205",
              "2016113",
              "2017103",
              "2021104",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Aricidea",
            "totalWeight_kg": 0.253,
            "samplesWithWeight": 52,
            "samplesInAOI": 115,
            "totalIndividuals": 408,
            "cruises": [
              "2006612",
              "2008104",
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017115",
              "2019115",
              "2020110",
              "2021104",
              "2021115",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Amphiura",
            "totalWeight_kg": 0.252,
            "samplesWithWeight": 9,
            "samplesInAOI": 68,
            "totalIndividuals": 51,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2014106",
              "2015113",
              "2016113",
              "2017103",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Tritia incrassata",
            "totalWeight_kg": 0.25,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 1,
            "cruises": [
              "2008104",
              "2011110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Typhlonereis gracilis",
            "totalWeight_kg": 0.247,
            "samplesWithWeight": 4,
            "samplesInAOI": 4,
            "totalIndividuals": 5,
            "cruises": [
              "2009105",
              "2010110",
              "2010112"
            ],
            "equipment": [
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lafoea",
            "totalWeight_kg": 0.237,
            "samplesWithWeight": 3,
            "samplesInAOI": 36,
            "totalIndividuals": 44,
            "cruises": [
              "2008104",
              "2008114",
              "2011113",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "Videograb"
            ]
          },
          {
            "scientificName": "Lysianassa costae",
            "totalWeight_kg": 0.236,
            "samplesWithWeight": 9,
            "samplesInAOI": 43,
            "totalIndividuals": 52,
            "cruises": [
              "2010110",
              "2010112",
              "2011110",
              "2012106",
              "2014208",
              "2020104",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Aonides paucibranchiata",
            "totalWeight_kg": 0.236,
            "samplesWithWeight": 61,
            "samplesInAOI": 71,
            "totalIndividuals": 196,
            "cruises": [
              "2007111",
              "2008104",
              "2008114",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2014106",
              "2014115",
              "2014208",
              "2020104",
              "2021115"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leptostylis macrura",
            "totalWeight_kg": 0.23,
            "samplesWithWeight": 34,
            "samplesInAOI": 92,
            "totalIndividuals": 374,
            "cruises": [
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2022118",
              "2023001009"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Acanthochitona fascicularis",
            "totalWeight_kg": 0.226,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2007111"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lepechinella",
            "totalWeight_kg": 0.218,
            "samplesWithWeight": 12,
            "samplesInAOI": 31,
            "totalIndividuals": 149,
            "cruises": [
              "2006612",
              "2009105",
              "2010110",
              "2010112",
              "2011105",
              "2012106",
              "2013110",
              "2013112",
              "2014106",
              "2014208",
              "2015113",
              "2021103",
              "2021104",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leucothoe spinicarpa",
            "totalWeight_kg": 0.216,
            "samplesWithWeight": 12,
            "samplesInAOI": 55,
            "totalIndividuals": 39,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2009105",
              "2010110",
              "2010112",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014208",
              "2015113",
              "2020104",
              "2020110",
              "2021104",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lysianassa plumosa",
            "totalWeight_kg": 0.215,
            "samplesWithWeight": 12,
            "samplesInAOI": 24,
            "totalIndividuals": 53,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2011110",
              "2011113",
              "2012106",
              "2013205",
              "2020110",
              "2021103",
              "2021104",
              "2023001005",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Apomatus similis",
            "totalWeight_kg": 0.214,
            "samplesWithWeight": 5,
            "samplesInAOI": 10,
            "totalIndividuals": 4,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2010110",
              "2013112",
              "2013205",
              "2014208",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Harmothoe viridis",
            "totalWeight_kg": 0.213,
            "samplesWithWeight": 5,
            "samplesInAOI": 10,
            "totalIndividuals": 14,
            "cruises": [
              "2007111",
              "2010110",
              "2012106",
              "2013112",
              "2013205",
              "2020104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leptophoxus falcatus",
            "totalWeight_kg": 0.212,
            "samplesWithWeight": 33,
            "samplesInAOI": 124,
            "totalIndividuals": 689,
            "cruises": [
              "2006612",
              "2007105",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2017103",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118",
              "2023001009"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Limea crassa",
            "totalWeight_kg": 0.209,
            "samplesWithWeight": 12,
            "samplesInAOI": 104,
            "totalIndividuals": 36,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2009111",
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Unciola",
            "totalWeight_kg": 0.206,
            "samplesWithWeight": 24,
            "samplesInAOI": 59,
            "totalIndividuals": 395,
            "cruises": [
              "2006612",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014115",
              "2017103",
              "2021115",
              "2022118",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Labidoplax buskii",
            "totalWeight_kg": 0.197,
            "samplesWithWeight": 20,
            "samplesInAOI": 218,
            "totalIndividuals": 30,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008104",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2017103",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118",
              "2022708",
              "2022846",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lumbrineris aniara",
            "totalWeight_kg": 0.196,
            "samplesWithWeight": 11,
            "samplesInAOI": 153,
            "totalIndividuals": 25,
            "cruises": [
              "2007111",
              "2009105",
              "2010110",
              "2010112",
              "2012106",
              "2013112",
              "2013205",
              "2014106",
              "2014208",
              "2015113",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Amphiura borealis",
            "totalWeight_kg": 0.19,
            "samplesWithWeight": 3,
            "samplesInAOI": 58,
            "totalIndividuals": 3,
            "cruises": [
              "2006612",
              "2007111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2015113",
              "2020104",
              "2020110",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Virgularia mirabilis",
            "totalWeight_kg": 0.187,
            "samplesWithWeight": 5,
            "samplesInAOI": 12,
            "totalIndividuals": 5,
            "cruises": [
              "2008114",
              "2009105",
              "2010112",
              "2011113",
              "2012106",
              "2021103",
              "2023001009",
              "2024001021"
            ],
            "equipment": [
              "Beamtrawl",
              "Bioboks",
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Ampharete octocirrata",
            "totalWeight_kg": 0.187,
            "samplesWithWeight": 104,
            "samplesInAOI": 294,
            "totalIndividuals": 59,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2018109",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Isocirrus planiceps",
            "totalWeight_kg": 0.182,
            "samplesWithWeight": 21,
            "samplesInAOI": 32,
            "totalIndividuals": 12,
            "cruises": [
              "2007111",
              "2008114",
              "2010110",
              "2011110",
              "2012106",
              "2012110",
              "2013112",
              "2020104",
              "2021104"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leucon",
            "totalWeight_kg": 0.181,
            "samplesWithWeight": 10,
            "samplesInAOI": 52,
            "totalIndividuals": 667,
            "cruises": [
              "2006612",
              "2007111",
              "2008104",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011113",
              "2012106",
              "2013110",
              "2013112",
              "2014115",
              "2016113",
              "2017103",
              "2018109",
              "2019106",
              "2019115",
              "2020110",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2023001009"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Stylatula elegans",
            "totalWeight_kg": 0.173,
            "samplesWithWeight": 3,
            "samplesInAOI": 5,
            "totalIndividuals": 4,
            "cruises": [
              "2007105",
              "2007111",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Astropecten irregularis",
            "totalWeight_kg": 0.171,
            "samplesWithWeight": 1,
            "samplesInAOI": 7,
            "totalIndividuals": 1,
            "cruises": [
              "2007105",
              "2012106",
              "2023001009",
              "2024001021"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Harmothoe impar",
            "totalWeight_kg": 0.168,
            "samplesWithWeight": 4,
            "samplesInAOI": 4,
            "totalIndividuals": 3,
            "cruises": [
              "2006612",
              "2007111",
              "2012106"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Astacilla intermedia",
            "totalWeight_kg": 0.167,
            "samplesWithWeight": 3,
            "samplesInAOI": 10,
            "totalIndividuals": 15,
            "cruises": [
              "2006612",
              "2007111",
              "2009111",
              "2010112",
              "2013110",
              "2013112",
              "2014106",
              "2015113"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Aphia minuta",
            "totalWeight_kg": 0.165,
            "samplesWithWeight": 2,
            "samplesInAOI": 2,
            "totalIndividuals": 2,
            "cruises": [
              "2007105"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Laonice norgensis",
            "totalWeight_kg": 0.159,
            "samplesWithWeight": 4,
            "samplesInAOI": 6,
            "totalIndividuals": 9,
            "cruises": [
              "2007111",
              "2008114",
              "2012106",
              "2013112"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Margarites costalis",
            "totalWeight_kg": 0.158,
            "samplesWithWeight": 2,
            "samplesInAOI": 13,
            "totalIndividuals": 5,
            "cruises": [
              "2009111",
              "2011110",
              "2014106",
              "2014115",
              "2015109",
              "2016113",
              "2019115",
              "2021115",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Tryphosella horingi",
            "totalWeight_kg": 0.152,
            "samplesWithWeight": 11,
            "samplesInAOI": 28,
            "totalIndividuals": 72,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2011113",
              "2012106",
              "2015113",
              "2017103",
              "2017115",
              "2019115",
              "2020104",
              "2021103",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leptostylis",
            "totalWeight_kg": 0.147,
            "samplesWithWeight": 20,
            "samplesInAOI": 69,
            "totalIndividuals": 268,
            "cruises": [
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2019115",
              "2020104",
              "2020110",
              "2022118",
              "2022708",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Tryphosella nanoides",
            "totalWeight_kg": 0.144,
            "samplesWithWeight": 13,
            "samplesInAOI": 21,
            "totalIndividuals": 110,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2011110",
              "2011113",
              "2012106",
              "2018109",
              "2019115",
              "2021103",
              "2021104",
              "2023001009"
            ],
            "equipment": [
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Amphilepis norvegica",
            "totalWeight_kg": 0.14,
            "samplesWithWeight": 6,
            "samplesInAOI": 183,
            "totalIndividuals": 7,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2013112",
              "2013205",
              "2014106",
              "2014208",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Apherusa bispinosa",
            "totalWeight_kg": 0.137,
            "samplesWithWeight": 3,
            "samplesInAOI": 12,
            "totalIndividuals": 33,
            "cruises": [
              "2007111",
              "2010112",
              "2012110",
              "2013112",
              "2014115",
              "2015113",
              "2021103",
              "2021115",
              "2023001009"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ampelisca diadema",
            "totalWeight_kg": 0.135,
            "samplesWithWeight": 6,
            "samplesInAOI": 9,
            "totalIndividuals": 12,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2021115"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Acanthonotozoma serratum",
            "totalWeight_kg": 0.134,
            "samplesWithWeight": 7,
            "samplesInAOI": 32,
            "totalIndividuals": 41,
            "cruises": [
              "2006612",
              "2010110",
              "2011105",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2016113",
              "2017103",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Aglajidae",
            "totalWeight_kg": 0.134,
            "samplesWithWeight": 2,
            "samplesInAOI": 2,
            "totalIndividuals": 3,
            "cruises": [
              "2008104",
              "2008114"
            ],
            "equipment": [
              "Beamtrawl",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Ampelisca typica",
            "totalWeight_kg": 0.131,
            "samplesWithWeight": 3,
            "samplesInAOI": 10,
            "totalIndividuals": 24,
            "cruises": [
              "2006612",
              "2007111",
              "2009105",
              "2010110",
              "2013110",
              "2014208",
              "2021115",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Turrisipho",
            "totalWeight_kg": 0.131,
            "samplesWithWeight": 2,
            "samplesInAOI": 6,
            "totalIndividuals": 2,
            "cruises": [
              "2009105",
              "2010112",
              "2014208",
              "2015113",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Anomioidea",
            "totalWeight_kg": 0.128,
            "samplesWithWeight": 8,
            "samplesInAOI": 15,
            "totalIndividuals": 22,
            "cruises": [
              "2006612",
              "2007105",
              "2007111"
            ],
            "equipment": [
              "Boxcorer",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Arctica islandica",
            "totalWeight_kg": 0.127,
            "samplesWithWeight": 1,
            "samplesInAOI": 8,
            "totalIndividuals": 1,
            "cruises": [
              "2008104",
              "2013110",
              "2014106"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Malacoceros",
            "totalWeight_kg": 0.124,
            "samplesWithWeight": 6,
            "samplesInAOI": 6,
            "totalIndividuals": 27,
            "cruises": [
              "2008114",
              "2012110"
            ],
            "equipment": [
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Janira",
            "totalWeight_kg": 0.121,
            "samplesWithWeight": 8,
            "samplesInAOI": 10,
            "totalIndividuals": 144,
            "cruises": [
              "2006612",
              "2010110",
              "2012106"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Scoloplos armiger",
            "totalWeight_kg": 0.12,
            "samplesWithWeight": 3,
            "samplesInAOI": 31,
            "totalIndividuals": 5,
            "cruises": [
              "2006612",
              "2008104",
              "2008114",
              "2010110",
              "2013110",
              "2014106",
              "2017103",
              "2017112",
              "2019115",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Boxcorer",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Abra prismatica",
            "totalWeight_kg": 0.12,
            "samplesWithWeight": 6,
            "samplesInAOI": 17,
            "totalIndividuals": 13,
            "cruises": [
              "2007111",
              "2008104",
              "2008114",
              "2010112",
              "2011105",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2020104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Malacostraca",
            "totalWeight_kg": 0.118,
            "samplesWithWeight": 2,
            "samplesInAOI": 2,
            "totalIndividuals": 3,
            "cruises": [
              "2007111"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lanassa venusta",
            "totalWeight_kg": 0.114,
            "samplesWithWeight": 111,
            "samplesInAOI": 260,
            "totalIndividuals": 195,
            "cruises": [
              "2007105",
              "2007111",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Maera loveni",
            "totalWeight_kg": 0.108,
            "samplesWithWeight": 4,
            "samplesInAOI": 24,
            "totalIndividuals": 6,
            "cruises": [
              "2006612",
              "2007111",
              "2011105",
              "2011110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2018109",
              "2019106",
              "2021104",
              "2021115",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Laothoes meinerti",
            "totalWeight_kg": 0.106,
            "samplesWithWeight": 8,
            "samplesInAOI": 27,
            "totalIndividuals": 20,
            "cruises": [
              "2006612",
              "2007111",
              "2008104",
              "2010110",
              "2010112",
              "2011113",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2020104",
              "2020110",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Malmgrenia mcintoshi",
            "totalWeight_kg": 0.101,
            "samplesWithWeight": 7,
            "samplesInAOI": 16,
            "totalIndividuals": 8,
            "cruises": [
              "2007111",
              "2010110",
              "2010112",
              "2012106",
              "2013110",
              "2014106",
              "2020104",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Idotea emarginata",
            "totalWeight_kg": 0.101,
            "samplesWithWeight": 7,
            "samplesInAOI": 7,
            "totalIndividuals": 24,
            "cruises": [
              "2006612",
              "2011113",
              "2012106"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Lycodes rossi",
            "totalWeight_kg": 0.1,
            "samplesWithWeight": 1,
            "samplesInAOI": 4,
            "totalIndividuals": 1,
            "cruises": [
              "2009105",
              "2018109",
              "2019115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Syllis armillaris",
            "totalWeight_kg": 0.099,
            "samplesWithWeight": 17,
            "samplesInAOI": 23,
            "totalIndividuals": 32,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2013110",
              "2014106",
              "2021104",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Amphithopsis",
            "totalWeight_kg": 0.097,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 174,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ampharete lindstroemi",
            "totalWeight_kg": 0.096,
            "samplesWithWeight": 11,
            "samplesInAOI": 56,
            "totalIndividuals": 23,
            "cruises": [
              "2009105",
              "2010110",
              "2010112",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2016113",
              "2019106",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Antalis",
            "totalWeight_kg": 0.095,
            "samplesWithWeight": 8,
            "samplesInAOI": 18,
            "totalIndividuals": 9,
            "cruises": [
              "2007111",
              "2011113",
              "2012110",
              "2013110",
              "2013112",
              "2014115",
              "2014208",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Kelliella miliaris",
            "totalWeight_kg": 0.093,
            "samplesWithWeight": 8,
            "samplesInAOI": 282,
            "totalIndividuals": 61,
            "cruises": [
              "2006612",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014208",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Meterythrops robustus",
            "totalWeight_kg": 0.092,
            "samplesWithWeight": 4,
            "samplesInAOI": 31,
            "totalIndividuals": 30,
            "cruises": [
              "2007111",
              "2009105",
              "2011105",
              "2015109",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2021104",
              "2021115",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Asclerocheilus intermedius",
            "totalWeight_kg": 0.091,
            "samplesWithWeight": 19,
            "samplesInAOI": 26,
            "totalIndividuals": 43,
            "cruises": [
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2013205",
              "2015113",
              "2017115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Malacoceros jirkovi",
            "totalWeight_kg": 0.087,
            "samplesWithWeight": 33,
            "samplesInAOI": 39,
            "totalIndividuals": 23,
            "cruises": [
              "2007111",
              "2010110",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2021104"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Anonyx lilljeborgi",
            "totalWeight_kg": 0.086,
            "samplesWithWeight": 4,
            "samplesInAOI": 35,
            "totalIndividuals": 3,
            "cruises": [
              "2007105",
              "2007111",
              "2011105",
              "2012106",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leucon (Leucon) fulvus",
            "totalWeight_kg": 0.084,
            "samplesWithWeight": 6,
            "samplesInAOI": 30,
            "totalIndividuals": 58,
            "cruises": [
              "2006612",
              "2007105",
              "2010110",
              "2016113",
              "2017103",
              "2017112",
              "2018109",
              "2019106",
              "2019115",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Syllis gracilis",
            "totalWeight_kg": 0.084,
            "samplesWithWeight": 4,
            "samplesInAOI": 4,
            "totalIndividuals": 8,
            "cruises": [
              "2007111",
              "2009105",
              "2010110"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aora",
            "totalWeight_kg": 0.084,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 40,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Velutina plicatilis",
            "totalWeight_kg": 0.081,
            "samplesWithWeight": 1,
            "samplesInAOI": 4,
            "totalIndividuals": 1,
            "cruises": [
              "2006612",
              "2010110",
              "2011105",
              "2013110"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aora typica",
            "totalWeight_kg": 0.077,
            "samplesWithWeight": 4,
            "samplesInAOI": 4,
            "totalIndividuals": 190,
            "cruises": [
              "2007111"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Limneria undata",
            "totalWeight_kg": 0.076,
            "samplesWithWeight": 2,
            "samplesInAOI": 56,
            "totalIndividuals": 3,
            "cruises": [
              "2007105",
              "2007111",
              "2013110",
              "2013112",
              "2014106",
              "2014115",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2018109",
              "2019106",
              "2019115",
              "2021104",
              "2021115",
              "2022708",
              "2024007005"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Laothoes",
            "totalWeight_kg": 0.074,
            "samplesWithWeight": 3,
            "samplesInAOI": 10,
            "totalIndividuals": 17,
            "cruises": [
              "2009111",
              "2010110",
              "2010112",
              "2013205",
              "2015113"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Melinna albicincta",
            "totalWeight_kg": 0.072,
            "samplesWithWeight": 6,
            "samplesInAOI": 45,
            "totalIndividuals": 5,
            "cruises": [
              "2007105",
              "2008114",
              "2010110",
              "2012106",
              "2013112",
              "2013205",
              "2014208",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Laetmonice hystrix",
            "totalWeight_kg": 0.069,
            "samplesWithWeight": 2,
            "samplesInAOI": 2,
            "totalIndividuals": 2,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Megamoera",
            "totalWeight_kg": 0.068,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 2,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Lumbrineris",
            "totalWeight_kg": 0.067,
            "samplesWithWeight": 20,
            "samplesInAOI": 110,
            "totalIndividuals": 26,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2009105",
              "2010110",
              "2010112",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014106",
              "2015113",
              "2017103",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Boxcorer",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lysilla loveni",
            "totalWeight_kg": 0.066,
            "samplesWithWeight": 4,
            "samplesInAOI": 24,
            "totalIndividuals": 2,
            "cruises": [
              "2008104",
              "2010110",
              "2011105",
              "2011110",
              "2014106",
              "2014208",
              "2015109",
              "2017103",
              "2019115",
              "2020104",
              "2020110",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Andaniexis abyssi",
            "totalWeight_kg": 0.066,
            "samplesWithWeight": 7,
            "samplesInAOI": 73,
            "totalIndividuals": 90,
            "cruises": [
              "2006612",
              "2009105",
              "2011105",
              "2012106",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2022846",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Yoldiella",
            "totalWeight_kg": 0.066,
            "samplesWithWeight": 4,
            "samplesInAOI": 24,
            "totalIndividuals": 7,
            "cruises": [
              "2006612",
              "2007105",
              "2008104",
              "2013205",
              "2019106",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Laonome kroyeri",
            "totalWeight_kg": 0.065,
            "samplesWithWeight": 15,
            "samplesInAOI": 25,
            "totalIndividuals": 6,
            "cruises": [
              "2006612",
              "2009105",
              "2010110",
              "2010112",
              "2011105",
              "2012106",
              "2013110",
              "2013112",
              "2014208",
              "2015113",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Levinsenia gracilis",
            "totalWeight_kg": 0.064,
            "samplesWithWeight": 69,
            "samplesInAOI": 216,
            "totalIndividuals": 313,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leaena ebranchiata",
            "totalWeight_kg": 0.063,
            "samplesWithWeight": 28,
            "samplesInAOI": 80,
            "totalIndividuals": 67,
            "cruises": [
              "2007111",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011113",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Aglaophamus pulcher",
            "totalWeight_kg": 0.063,
            "samplesWithWeight": 8,
            "samplesInAOI": 41,
            "totalIndividuals": 3,
            "cruises": [
              "2007105",
              "2007111",
              "2010110",
              "2010112",
              "2012110",
              "2013112",
              "2013205",
              "2014208",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Limatula",
            "totalWeight_kg": 0.063,
            "samplesWithWeight": 9,
            "samplesInAOI": 11,
            "totalIndividuals": 12,
            "cruises": [
              "2007111",
              "2010110",
              "2014115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Laonice blakei",
            "totalWeight_kg": 0.062,
            "samplesWithWeight": 14,
            "samplesInAOI": 16,
            "totalIndividuals": 8,
            "cruises": [
              "2008104",
              "2008114",
              "2009105",
              "2009111",
              "2010112",
              "2012106",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Iphimedia obesa",
            "totalWeight_kg": 0.06,
            "samplesWithWeight": 5,
            "samplesInAOI": 11,
            "totalIndividuals": 7,
            "cruises": [
              "2007111",
              "2008114",
              "2010110",
              "2012106",
              "2012110",
              "2013112",
              "2014106",
              "2020104"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Velutina",
            "totalWeight_kg": 0.057,
            "samplesWithWeight": 1,
            "samplesInAOI": 6,
            "totalIndividuals": 1,
            "cruises": [
              "2009105",
              "2010110",
              "2010112",
              "2011110",
              "2018109"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Liljeborgiidae",
            "totalWeight_kg": 0.056,
            "samplesWithWeight": 10,
            "samplesInAOI": 34,
            "totalIndividuals": 38,
            "cruises": [
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014106",
              "2020104",
              "2022118",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Anomiidae",
            "totalWeight_kg": 0.054,
            "samplesWithWeight": 4,
            "samplesInAOI": 4,
            "totalIndividuals": 7,
            "cruises": [
              "2007105",
              "2007111",
              "2009105"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Metavermilia arctica",
            "totalWeight_kg": 0.054,
            "samplesWithWeight": 1,
            "samplesInAOI": 3,
            "totalIndividuals": 0,
            "cruises": [
              "2007111",
              "2013112",
              "2013205"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lanassa nordenskioldi",
            "totalWeight_kg": 0.054,
            "samplesWithWeight": 22,
            "samplesInAOI": 40,
            "totalIndividuals": 45,
            "cruises": [
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2016113",
              "2020110",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Laonice cirrata",
            "totalWeight_kg": 0.053,
            "samplesWithWeight": 12,
            "samplesInAOI": 179,
            "totalIndividuals": 6,
            "cruises": [
              "2006612",
              "2007111",
              "2008104",
              "2010110",
              "2011105",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2016113",
              "2017103",
              "2018109",
              "2019106",
              "2019115",
              "2021104",
              "2021115",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Aristias neglectus",
            "totalWeight_kg": 0.052,
            "samplesWithWeight": 9,
            "samplesInAOI": 12,
            "totalIndividuals": 47,
            "cruises": [
              "2007105",
              "2007111",
              "2015113",
              "2020104",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Amphilepis",
            "totalWeight_kg": 0.05,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 2,
            "cruises": [
              "2007111",
              "2010112"
            ],
            "equipment": [
              "Beamtrawl",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Melphidippa",
            "totalWeight_kg": 0.049,
            "samplesWithWeight": 13,
            "samplesInAOI": 27,
            "totalIndividuals": 81,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2013205",
              "2015113",
              "2016113",
              "2017103",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Andaniopsis pectinata",
            "totalWeight_kg": 0.049,
            "samplesWithWeight": 7,
            "samplesInAOI": 16,
            "totalIndividuals": 54,
            "cruises": [
              "2006612",
              "2007105",
              "2014106",
              "2014115",
              "2015113",
              "2016113",
              "2017112",
              "2018109",
              "2019115",
              "2020104"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Abra",
            "totalWeight_kg": 0.049,
            "samplesWithWeight": 1,
            "samplesInAOI": 4,
            "totalIndividuals": 1,
            "cruises": [
              "2007111",
              "2014106",
              "2019115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Liljeborgia (Liljeborgia) pallida",
            "totalWeight_kg": 0.048,
            "samplesWithWeight": 9,
            "samplesInAOI": 51,
            "totalIndividuals": 26,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2009105",
              "2009111",
              "2010110",
              "2011105",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2015113",
              "2019115",
              "2020104",
              "2020110",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Andaniopsis nordlandica",
            "totalWeight_kg": 0.048,
            "samplesWithWeight": 4,
            "samplesInAOI": 11,
            "totalIndividuals": 51,
            "cruises": [
              "2006612",
              "2007111",
              "2013205",
              "2014106",
              "2014115",
              "2020110"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Trypanosyllis troll",
            "totalWeight_kg": 0.046,
            "samplesWithWeight": 27,
            "samplesInAOI": 66,
            "totalIndividuals": 19,
            "cruises": [
              "2007105",
              "2007111",
              "2009105",
              "2010110",
              "2010112",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leptamphopus sarsi",
            "totalWeight_kg": 0.045,
            "samplesWithWeight": 4,
            "samplesInAOI": 11,
            "totalIndividuals": 34,
            "cruises": [
              "2007105",
              "2008104",
              "2008114",
              "2009105",
              "2011113",
              "2012106",
              "2013205",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Asellota",
            "totalWeight_kg": 0.044,
            "samplesWithWeight": 10,
            "samplesInAOI": 20,
            "totalIndividuals": 18,
            "cruises": [
              "2007105",
              "2007111",
              "2008104",
              "2008114",
              "2009105",
              "2010110",
              "2014106"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Apseudes spinosus",
            "totalWeight_kg": 0.042,
            "samplesWithWeight": 9,
            "samplesInAOI": 21,
            "totalIndividuals": 8,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2010110",
              "2011113",
              "2012106",
              "2013112",
              "2021103"
            ],
            "equipment": [
              "Beamtrawl",
              "Boxcorer",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Trophonopsis barvicensis",
            "totalWeight_kg": 0.037,
            "samplesWithWeight": 2,
            "samplesInAOI": 30,
            "totalIndividuals": 2,
            "cruises": [
              "2006612",
              "2008104",
              "2013112",
              "2013205",
              "2014106",
              "2014208",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Amphilochus tenuimanus",
            "totalWeight_kg": 0.035,
            "samplesWithWeight": 6,
            "samplesInAOI": 73,
            "totalIndividuals": 59,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2009105",
              "2010110",
              "2010112",
              "2011105",
              "2011113",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2016113",
              "2017103",
              "2017115",
              "2019106",
              "2020104",
              "2021103",
              "2021115",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Tryphosella",
            "totalWeight_kg": 0.035,
            "samplesWithWeight": 7,
            "samplesInAOI": 17,
            "totalIndividuals": 52,
            "cruises": [
              "2006612",
              "2007111",
              "2009105",
              "2011113",
              "2012106",
              "2015113",
              "2017103",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Labidoplax",
            "totalWeight_kg": 0.035,
            "samplesWithWeight": 3,
            "samplesInAOI": 5,
            "totalIndividuals": 6,
            "cruises": [
              "2009105",
              "2010112",
              "2022708"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Andaniexis",
            "totalWeight_kg": 0.035,
            "samplesWithWeight": 4,
            "samplesInAOI": 13,
            "totalIndividuals": 28,
            "cruises": [
              "2006612",
              "2008104",
              "2009105",
              "2009111",
              "2010110",
              "2012106",
              "2013110",
              "2013205"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Iothia fulva",
            "totalWeight_kg": 0.034,
            "samplesWithWeight": 2,
            "samplesInAOI": 25,
            "totalIndividuals": 2,
            "cruises": [
              "2006612",
              "2007111",
              "2010110",
              "2011105",
              "2012106",
              "2013110",
              "2014106",
              "2019115",
              "2020104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Velutina velutina",
            "totalWeight_kg": 0.034,
            "samplesWithWeight": 2,
            "samplesInAOI": 42,
            "totalIndividuals": 2,
            "cruises": [
              "2006612",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2013110",
              "2013112",
              "2014106",
              "2015109",
              "2016113",
              "2017112",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Macroclymene",
            "totalWeight_kg": 0.033,
            "samplesWithWeight": 17,
            "samplesInAOI": 17,
            "totalIndividuals": 47,
            "cruises": [
              "2008104",
              "2008114"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leptostraca",
            "totalWeight_kg": 0.033,
            "samplesWithWeight": 6,
            "samplesInAOI": 45,
            "totalIndividuals": 9,
            "cruises": [
              "2009105",
              "2010110",
              "2010112",
              "2011110",
              "2013205",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Harmothoe globifera",
            "totalWeight_kg": 0.032,
            "samplesWithWeight": 4,
            "samplesInAOI": 19,
            "totalIndividuals": 2,
            "cruises": [
              "2007111",
              "2009105",
              "2010110",
              "2010112",
              "2013110",
              "2013205",
              "2015113",
              "2017103",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Ampharetinae",
            "totalWeight_kg": 0.032,
            "samplesWithWeight": 2,
            "samplesInAOI": 5,
            "totalIndividuals": 3,
            "cruises": [
              "2006612",
              "2007105",
              "2008104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Leitoscoloplos acutus",
            "totalWeight_kg": 0.031,
            "samplesWithWeight": 4,
            "samplesInAOI": 4,
            "totalIndividuals": 6,
            "cruises": [
              "2009111",
              "2010110"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aristias tumidus",
            "totalWeight_kg": 0.03,
            "samplesWithWeight": 5,
            "samplesInAOI": 10,
            "totalIndividuals": 56,
            "cruises": [
              "2006612",
              "2015109",
              "2016113",
              "2017112",
              "2020104"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Anatoma",
            "totalWeight_kg": 0.03,
            "samplesWithWeight": 2,
            "samplesInAOI": 3,
            "totalIndividuals": 4,
            "cruises": [
              "2007111",
              "2010110"
            ],
            "equipment": [
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lembos",
            "totalWeight_kg": 0.028,
            "samplesWithWeight": 1,
            "samplesInAOI": 6,
            "totalIndividuals": 12,
            "cruises": [
              "2006612",
              "2010110",
              "2010112",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Harmothoe fragilis",
            "totalWeight_kg": 0.027,
            "samplesWithWeight": 7,
            "samplesInAOI": 36,
            "totalIndividuals": 5,
            "cruises": [
              "2007111",
              "2010110",
              "2012106",
              "2013110",
              "2013112",
              "2015109",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leucon (Leucon) serratus",
            "totalWeight_kg": 0.027,
            "samplesWithWeight": 4,
            "samplesInAOI": 120,
            "totalIndividuals": 120,
            "cruises": [
              "2008114",
              "2010110",
              "2010112",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014115",
              "2015109",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leucon (Leucon) acutirostris",
            "totalWeight_kg": 0.027,
            "samplesWithWeight": 10,
            "samplesInAOI": 60,
            "totalIndividuals": 113,
            "cruises": [
              "2006612",
              "2007111",
              "2013110",
              "2014115",
              "2015109",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2021115",
              "2022118",
              "2022708",
              "2023001009"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Urothoe",
            "totalWeight_kg": 0.027,
            "samplesWithWeight": 4,
            "samplesInAOI": 4,
            "totalIndividuals": 32,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leptostylis ampullacea",
            "totalWeight_kg": 0.026,
            "samplesWithWeight": 3,
            "samplesInAOI": 6,
            "totalIndividuals": 29,
            "cruises": [
              "2010112",
              "2012106",
              "2019106",
              "2019115",
              "2020104"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Kelliola symmetros",
            "totalWeight_kg": 0.026,
            "samplesWithWeight": 2,
            "samplesInAOI": 5,
            "totalIndividuals": 17,
            "cruises": [
              "2008104",
              "2010112",
              "2013205",
              "2014208"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Ampelisca spinipes",
            "totalWeight_kg": 0.025,
            "samplesWithWeight": 4,
            "samplesInAOI": 11,
            "totalIndividuals": 4,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2010110",
              "2010112",
              "2012110",
              "2013205",
              "2017103",
              "2020104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Actaedrilus polyonyx",
            "totalWeight_kg": 0.024,
            "samplesWithWeight": 36,
            "samplesInAOI": 64,
            "totalIndividuals": 122,
            "cruises": [
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2011110",
              "2012106",
              "2012110",
              "2013205",
              "2014208",
              "2015113",
              "2016113",
              "2019106",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Aricidea (Strelzovia) quadrilobata",
            "totalWeight_kg": 0.023,
            "samplesWithWeight": 20,
            "samplesInAOI": 63,
            "totalIndividuals": 26,
            "cruises": [
              "2008104",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014115",
              "2014208",
              "2015113",
              "2016113",
              "2017103",
              "2018109",
              "2019115",
              "2021104",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Laphania boecki",
            "totalWeight_kg": 0.022,
            "samplesWithWeight": 4,
            "samplesInAOI": 95,
            "totalIndividuals": 6,
            "cruises": [
              "2007111",
              "2008114",
              "2010110",
              "2013110",
              "2013112",
              "2014106",
              "2014115",
              "2015109",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2021104",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Ampelisca tenuicornis",
            "totalWeight_kg": 0.022,
            "samplesWithWeight": 5,
            "samplesInAOI": 16,
            "totalIndividuals": 13,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2010110",
              "2010112",
              "2020104",
              "2021104"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lepidepecreum umbo",
            "totalWeight_kg": 0.021,
            "samplesWithWeight": 3,
            "samplesInAOI": 100,
            "totalIndividuals": 6,
            "cruises": [
              "2006612",
              "2007105",
              "2009105",
              "2010110",
              "2012106",
              "2013110",
              "2013112",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2016113",
              "2017103",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2021103",
              "2021104",
              "2021115",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Tytthocope megalura",
            "totalWeight_kg": 0.021,
            "samplesWithWeight": 1,
            "samplesInAOI": 23,
            "totalIndividuals": 89,
            "cruises": [
              "2007111",
              "2010112",
              "2012110",
              "2013112",
              "2014208",
              "2015113",
              "2019115",
              "2020104",
              "2021103",
              "2021104",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Meterythrops",
            "totalWeight_kg": 0.02,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 2,
            "cruises": [
              "2007111"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Laonice bahusiensis",
            "totalWeight_kg": 0.02,
            "samplesWithWeight": 1,
            "samplesInAOI": 8,
            "totalIndividuals": 1,
            "cruises": [
              "2007111",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Liljeborgia (Liljeborgia) kinahani",
            "totalWeight_kg": 0.019,
            "samplesWithWeight": 5,
            "samplesInAOI": 18,
            "totalIndividuals": 20,
            "cruises": [
              "2007105",
              "2011113",
              "2012106",
              "2013110",
              "2013205",
              "2015113",
              "2019106",
              "2020104",
              "2021104",
              "2021115",
              "2022118",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lysianella petalocera",
            "totalWeight_kg": 0.019,
            "samplesWithWeight": 5,
            "samplesInAOI": 5,
            "totalIndividuals": 33,
            "cruises": [
              "2006612",
              "2011113"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ampelisca pusilla",
            "totalWeight_kg": 0.019,
            "samplesWithWeight": 7,
            "samplesInAOI": 35,
            "totalIndividuals": 16,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2010112",
              "2012106",
              "2013205",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Alvania cimicoides",
            "totalWeight_kg": 0.018,
            "samplesWithWeight": 3,
            "samplesInAOI": 15,
            "totalIndividuals": 3,
            "cruises": [
              "2007111",
              "2009111",
              "2012106",
              "2020104",
              "2020110",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Uschakovia gorbunovi",
            "totalWeight_kg": 0.018,
            "samplesWithWeight": 4,
            "samplesInAOI": 4,
            "totalIndividuals": 2,
            "cruises": [
              "2007105"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Laetmatophilus tuberculatus",
            "totalWeight_kg": 0.016,
            "samplesWithWeight": 20,
            "samplesInAOI": 123,
            "totalIndividuals": 42,
            "cruises": [
              "2007105",
              "2007111",
              "2009105",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118",
              "2022846",
              "2023001005",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Aspidarachna clypeata",
            "totalWeight_kg": 0.016,
            "samplesWithWeight": 3,
            "samplesInAOI": 37,
            "totalIndividuals": 17,
            "cruises": [
              "2007111",
              "2009111",
              "2010112",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014115",
              "2015113",
              "2019106",
              "2021103",
              "2021104",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leptostylis villosa",
            "totalWeight_kg": 0.016,
            "samplesWithWeight": 5,
            "samplesInAOI": 80,
            "totalIndividuals": 34,
            "cruises": [
              "2008104",
              "2010110",
              "2010112",
              "2011105",
              "2011113",
              "2013110",
              "2013112",
              "2014115",
              "2015109",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022708",
              "2023001009"
            ],
            "equipment": [
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lacydonia",
            "totalWeight_kg": 0.016,
            "samplesWithWeight": 2,
            "samplesInAOI": 3,
            "totalIndividuals": 17,
            "cruises": [
              "2009105",
              "2010112",
              "2015113"
            ],
            "equipment": [
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lasaeidae",
            "totalWeight_kg": 0.016,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2007111"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lamispina falcata",
            "totalWeight_kg": 0.016,
            "samplesWithWeight": 36,
            "samplesInAOI": 44,
            "totalIndividuals": 14,
            "cruises": [
              "2007105",
              "2007111",
              "2010110",
              "2010112",
              "2011110",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2020104",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Apseudes talpa",
            "totalWeight_kg": 0.015,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2007111"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Lampropidae",
            "totalWeight_kg": 0.015,
            "samplesWithWeight": 6,
            "samplesInAOI": 9,
            "totalIndividuals": 15,
            "cruises": [
              "2006612",
              "2007105",
              "2009105",
              "2009111",
              "2011110",
              "2012106"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Westwoodilla brevicalcar",
            "totalWeight_kg": 0.015,
            "samplesWithWeight": 3,
            "samplesInAOI": 6,
            "totalIndividuals": 30,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2021115"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Amathillopsis",
            "totalWeight_kg": 0.015,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 8,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Aricidea hartmani",
            "totalWeight_kg": 0.014,
            "samplesWithWeight": 25,
            "samplesInAOI": 98,
            "totalIndividuals": 37,
            "cruises": [
              "2007111",
              "2009105",
              "2010110",
              "2010112",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014115",
              "2014208",
              "2015113",
              "2016113",
              "2017103",
              "2017115",
              "2018109",
              "2019106",
              "2021103",
              "2021104",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Aricidea (Acmira) cerrutii",
            "totalWeight_kg": 0.014,
            "samplesWithWeight": 16,
            "samplesInAOI": 21,
            "totalIndividuals": 13,
            "cruises": [
              "2007111",
              "2010110",
              "2010112",
              "2012106",
              "2012110",
              "2013112",
              "2014115",
              "2018109",
              "2020104"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Amblyopsoides ohlinii",
            "totalWeight_kg": 0.014,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 2,
            "cruises": [
              "2008114"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Virgularia",
            "totalWeight_kg": 0.014,
            "samplesWithWeight": 1,
            "samplesInAOI": 19,
            "totalIndividuals": 2,
            "cruises": [
              "2008114",
              "2010112",
              "2014208",
              "2019106",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Metopa boeckii",
            "totalWeight_kg": 0.014,
            "samplesWithWeight": 2,
            "samplesInAOI": 2,
            "totalIndividuals": 6,
            "cruises": [
              "2006612",
              "2007105"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Megamphopus cornutus",
            "totalWeight_kg": 0.013,
            "samplesWithWeight": 1,
            "samplesInAOI": 8,
            "totalIndividuals": 21,
            "cruises": [
              "2007111",
              "2013110",
              "2022118",
              "2023001005",
              "2023001009"
            ],
            "equipment": [
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Acidostoma obesum",
            "totalWeight_kg": 0.013,
            "samplesWithWeight": 4,
            "samplesInAOI": 9,
            "totalIndividuals": 6,
            "cruises": [
              "2006612",
              "2007111",
              "2016113",
              "2019115",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Melanella monterosatoi",
            "totalWeight_kg": 0.013,
            "samplesWithWeight": 2,
            "samplesInAOI": 6,
            "totalIndividuals": 4,
            "cruises": [
              "2007111",
              "2013112",
              "2015113",
              "2020104",
              "2021104"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Tryphosella sarsi",
            "totalWeight_kg": 0.013,
            "samplesWithWeight": 5,
            "samplesInAOI": 5,
            "totalIndividuals": 17,
            "cruises": [
              "2006612",
              "2007105"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Aphelochaeta marioni",
            "totalWeight_kg": 0.013,
            "samplesWithWeight": 2,
            "samplesInAOI": 4,
            "totalIndividuals": 5,
            "cruises": [
              "2006612",
              "2007105"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Melphidippa goesi",
            "totalWeight_kg": 0.013,
            "samplesWithWeight": 7,
            "samplesInAOI": 27,
            "totalIndividuals": 16,
            "cruises": [
              "2007111",
              "2009105",
              "2010110",
              "2011105",
              "2012106",
              "2012110",
              "2013110",
              "2014106",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017115",
              "2019106",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Leucon (Leucon) nasica",
            "totalWeight_kg": 0.012,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 38,
            "cruises": [
              "2011105",
              "2019115"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Macrocypris",
            "totalWeight_kg": 0.012,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 9,
            "cruises": [
              "2008114"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ischyrocerus",
            "totalWeight_kg": 0.012,
            "samplesWithWeight": 3,
            "samplesInAOI": 25,
            "totalIndividuals": 8,
            "cruises": [
              "2009105",
              "2010112",
              "2011105",
              "2012106",
              "2013110",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2019106",
              "2019115",
              "2020104",
              "2021115",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lumbrineris cingulata",
            "totalWeight_kg": 0.011,
            "samplesWithWeight": 30,
            "samplesInAOI": 49,
            "totalIndividuals": 7,
            "cruises": [
              "2010112",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014208",
              "2021103"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Medicorophium affine",
            "totalWeight_kg": 0.01,
            "samplesWithWeight": 2,
            "samplesInAOI": 30,
            "totalIndividuals": 40,
            "cruises": [
              "2007111",
              "2010112",
              "2011110",
              "2013112",
              "2014106",
              "2014115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118",
              "2023001005",
              "2023001009"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lichenoporidae",
            "totalWeight_kg": 0.01,
            "samplesWithWeight": 1,
            "samplesInAOI": 4,
            "totalIndividuals": 2,
            "cruises": [
              "2007105",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Idunella",
            "totalWeight_kg": 0.01,
            "samplesWithWeight": 1,
            "samplesInAOI": 3,
            "totalIndividuals": 10,
            "cruises": [
              "2009105",
              "2010110",
              "2010112"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Anobothrus gracilis",
            "totalWeight_kg": 0.009,
            "samplesWithWeight": 9,
            "samplesInAOI": 108,
            "totalIndividuals": 9,
            "cruises": [
              "2008114",
              "2010110",
              "2011105",
              "2011110",
              "2013110",
              "2013112",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2016113",
              "2017103",
              "2017112",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Melitidae",
            "totalWeight_kg": 0.009,
            "samplesWithWeight": 7,
            "samplesInAOI": 28,
            "totalIndividuals": 29,
            "cruises": [
              "2008104",
              "2008114",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013205",
              "2014208",
              "2016113",
              "2017103",
              "2018109",
              "2019106",
              "2020104",
              "2020110",
              "2023001009"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Ampelisca amblyops",
            "totalWeight_kg": 0.009,
            "samplesWithWeight": 5,
            "samplesInAOI": 11,
            "totalIndividuals": 9,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2008114",
              "2012106",
              "2020104",
              "2020110",
              "2021103",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Macrochaeta",
            "totalWeight_kg": 0.009,
            "samplesWithWeight": 9,
            "samplesInAOI": 10,
            "totalIndividuals": 30,
            "cruises": [
              "2008104",
              "2008114",
              "2010110",
              "2010112",
              "2013112"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Kellia suborbicularis",
            "totalWeight_kg": 0.009,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 4,
            "cruises": [
              "2007111"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Krithe praetexta",
            "totalWeight_kg": 0.009,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2007105"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Laetmatophilus armatus",
            "totalWeight_kg": 0.009,
            "samplesWithWeight": 10,
            "samplesInAOI": 40,
            "totalIndividuals": 9,
            "cruises": [
              "2007111",
              "2008114",
              "2009105",
              "2011113",
              "2012106",
              "2014115",
              "2014208",
              "2015113",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Iphimedia",
            "totalWeight_kg": 0.008,
            "samplesWithWeight": 2,
            "samplesInAOI": 4,
            "totalIndividuals": 1,
            "cruises": [
              "2010110",
              "2012106",
              "2021104",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lembos websteri",
            "totalWeight_kg": 0.008,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2007111"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Xenodice frauenfeldti",
            "totalWeight_kg": 0.008,
            "samplesWithWeight": 10,
            "samplesInAOI": 83,
            "totalIndividuals": 12,
            "cruises": [
              "2007111",
              "2009105",
              "2010110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118",
              "2023001005",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Macrochaeta bansei",
            "totalWeight_kg": 0.008,
            "samplesWithWeight": 15,
            "samplesInAOI": 15,
            "totalIndividuals": 40,
            "cruises": [
              "2010110",
              "2010112",
              "2011113",
              "2012106"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Alvania",
            "totalWeight_kg": 0.008,
            "samplesWithWeight": 1,
            "samplesInAOI": 4,
            "totalIndividuals": 1,
            "cruises": [
              "2006612",
              "2009111",
              "2010110",
              "2011105"
            ],
            "equipment": [
              "Boxcorer",
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Arcturidae",
            "totalWeight_kg": 0.008,
            "samplesWithWeight": 2,
            "samplesInAOI": 18,
            "totalIndividuals": 1,
            "cruises": [
              "2008114",
              "2010112",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2015113",
              "2019106",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Asclerocheilus",
            "totalWeight_kg": 0.007,
            "samplesWithWeight": 2,
            "samplesInAOI": 8,
            "totalIndividuals": 7,
            "cruises": [
              "2009105",
              "2010112",
              "2013205",
              "2019115",
              "2020110"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Arcidae",
            "totalWeight_kg": 0.007,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2007111"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Metopa borealis",
            "totalWeight_kg": 0.007,
            "samplesWithWeight": 3,
            "samplesInAOI": 6,
            "totalIndividuals": 14,
            "cruises": [
              "2006612",
              "2007111",
              "2009105"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Anatoma crispata",
            "totalWeight_kg": 0.007,
            "samplesWithWeight": 1,
            "samplesInAOI": 35,
            "totalIndividuals": 1,
            "cruises": [
              "2006612",
              "2007105",
              "2010110",
              "2010112",
              "2011105",
              "2011113",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2019115",
              "2020110",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Septibranchia",
            "totalWeight_kg": 0.007,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 2,
            "cruises": [
              "2009105",
              "2022118"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Abietinaria",
            "totalWeight_kg": 0.007,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2008104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lumbrineris mixochaeta",
            "totalWeight_kg": 0.006,
            "samplesWithWeight": 12,
            "samplesInAOI": 209,
            "totalIndividuals": 9,
            "cruises": [
              "2010112",
              "2011110",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2015109",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2020110",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Ischnomesus",
            "totalWeight_kg": 0.006,
            "samplesWithWeight": 2,
            "samplesInAOI": 26,
            "totalIndividuals": 14,
            "cruises": [
              "2006612",
              "2010112",
              "2012106",
              "2013205",
              "2015113",
              "2020104",
              "2021103",
              "2021104",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Aricidea (Strelzovia) roberti",
            "totalWeight_kg": 0.006,
            "samplesWithWeight": 3,
            "samplesInAOI": 17,
            "totalIndividuals": 7,
            "cruises": [
              "2008104",
              "2010110",
              "2021104"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Aricidea nolani",
            "totalWeight_kg": 0.006,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 6,
            "cruises": [
              "2009105",
              "2013110"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Metopa",
            "totalWeight_kg": 0.006,
            "samplesWithWeight": 5,
            "samplesInAOI": 11,
            "totalIndividuals": 10,
            "cruises": [
              "2006612",
              "2007105",
              "2007111",
              "2011105",
              "2012106",
              "2017103",
              "2019106",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Limacina retroversa",
            "totalWeight_kg": 0.006,
            "samplesWithWeight": 3,
            "samplesInAOI": 32,
            "totalIndividuals": 7,
            "cruises": [
              "2008114",
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2011113",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2015113",
              "2016113",
              "2020104",
              "2021103"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Mesogastropoda",
            "totalWeight_kg": 0.006,
            "samplesWithWeight": 2,
            "samplesInAOI": 2,
            "totalIndividuals": 2,
            "cruises": [
              "2008104",
              "2008114"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Aplacophora",
            "totalWeight_kg": 0.005,
            "samplesWithWeight": 1,
            "samplesInAOI": 67,
            "totalIndividuals": 1,
            "cruises": [
              "2006612",
              "2008104",
              "2010110",
              "2010112",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2016113",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Maldane",
            "totalWeight_kg": 0.005,
            "samplesWithWeight": 1,
            "samplesInAOI": 6,
            "totalIndividuals": 1,
            "cruises": [
              "2006612",
              "2016113",
              "2021115",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lamprops",
            "totalWeight_kg": 0.005,
            "samplesWithWeight": 3,
            "samplesInAOI": 3,
            "totalIndividuals": 10,
            "cruises": [
              "2006612",
              "2007111",
              "2012106"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Malacoceros fuliginosus",
            "totalWeight_kg": 0.005,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 1,
            "cruises": [
              "2008104",
              "2017103"
            ],
            "equipment": [
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Scutopus ventrolineatus",
            "totalWeight_kg": 0.005,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 2,
            "cruises": [
              "2007111"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Astacilla pusilla",
            "totalWeight_kg": 0.005,
            "samplesWithWeight": 1,
            "samplesInAOI": 10,
            "totalIndividuals": 1,
            "cruises": [
              "2010110",
              "2012110",
              "2013110",
              "2013112",
              "2015113",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Janiridae",
            "totalWeight_kg": 0.005,
            "samplesWithWeight": 3,
            "samplesInAOI": 6,
            "totalIndividuals": 31,
            "cruises": [
              "2007111",
              "2010110",
              "2010112",
              "2012106"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ampharete falcata",
            "totalWeight_kg": 0.004,
            "samplesWithWeight": 10,
            "samplesInAOI": 20,
            "totalIndividuals": 4,
            "cruises": [
              "2010110",
              "2010112",
              "2012110",
              "2013110",
              "2013112",
              "2021103",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Anomura",
            "totalWeight_kg": 0.004,
            "samplesWithWeight": 1,
            "samplesInAOI": 19,
            "totalIndividuals": 3,
            "cruises": [
              "2008104",
              "2009111",
              "2011105",
              "2011110",
              "2012106",
              "2013112",
              "2013205",
              "2015113",
              "2017103",
              "2019115",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Tryphosella angulata",
            "totalWeight_kg": 0.004,
            "samplesWithWeight": 1,
            "samplesInAOI": 5,
            "totalIndividuals": 4,
            "cruises": [
              "2006612",
              "2015113",
              "2016113",
              "2019115"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Tryphosa nana",
            "totalWeight_kg": 0.004,
            "samplesWithWeight": 1,
            "samplesInAOI": 3,
            "totalIndividuals": 8,
            "cruises": [
              "2007111",
              "2011105",
              "2023001009"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Aricidea (Acmira) catherinae",
            "totalWeight_kg": 0.004,
            "samplesWithWeight": 36,
            "samplesInAOI": 70,
            "totalIndividuals": 17,
            "cruises": [
              "2007105",
              "2010110",
              "2010112",
              "2011105",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2017103",
              "2019115",
              "2021103",
              "2021104",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Serpula vermicularis",
            "totalWeight_kg": 0.004,
            "samplesWithWeight": 3,
            "samplesInAOI": 6,
            "totalIndividuals": 2,
            "cruises": [
              "2008114",
              "2010112",
              "2012106",
              "2013205",
              "2019115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Iphinopsis alba",
            "totalWeight_kg": 0.003,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2009105"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Adontorhina similis",
            "totalWeight_kg": 0.003,
            "samplesWithWeight": 2,
            "samplesInAOI": 73,
            "totalIndividuals": 3,
            "cruises": [
              "2009111",
              "2010110",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2017112",
              "2018109",
              "2019115",
              "2020104",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Yoldiella annenkovae",
            "totalWeight_kg": 0.003,
            "samplesWithWeight": 1,
            "samplesInAOI": 20,
            "totalIndividuals": 1,
            "cruises": [
              "2009111",
              "2010112",
              "2016113",
              "2019106",
              "2021104"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Limatula subauriculata",
            "totalWeight_kg": 0.003,
            "samplesWithWeight": 1,
            "samplesInAOI": 13,
            "totalIndividuals": 1,
            "cruises": [
              "2007105",
              "2010110",
              "2010112",
              "2012110",
              "2013112"
            ],
            "equipment": [
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Anoplodactylus petiolatus",
            "totalWeight_kg": 0.003,
            "samplesWithWeight": 2,
            "samplesInAOI": 10,
            "totalIndividuals": 5,
            "cruises": [
              "2008104",
              "2008114",
              "2012106",
              "2012110",
              "2020104"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aricidea (Acmira) laubieri",
            "totalWeight_kg": 0.003,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 3,
            "cruises": [
              "2008104",
              "2021104"
            ],
            "equipment": [
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Apistobranchus tullbergi",
            "totalWeight_kg": 0.003,
            "samplesWithWeight": 3,
            "samplesInAOI": 10,
            "totalIndividuals": 3,
            "cruises": [
              "2010110",
              "2010112",
              "2013110",
              "2014106",
              "2019106",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Ilyarachninae",
            "totalWeight_kg": 0.003,
            "samplesWithWeight": 1,
            "samplesInAOI": 4,
            "totalIndividuals": 3,
            "cruises": [
              "2010110",
              "2010112",
              "2012110"
            ],
            "equipment": [
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Scopelocheirus",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 2,
            "cruises": [
              "2008104"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Leucon (Macrauloleucon) spinulosus",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 3,
            "samplesInAOI": 6,
            "totalIndividuals": 5,
            "cruises": [
              "2009111",
              "2010112",
              "2022708"
            ],
            "equipment": [
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aphrodita perarmata",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 6,
            "samplesInAOI": 16,
            "totalIndividuals": 1,
            "cruises": [
              "2010110",
              "2011113",
              "2012110",
              "2013112",
              "2021103",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Aricidea (Strelzovia) suecica",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 27,
            "samplesInAOI": 34,
            "totalIndividuals": 12,
            "cruises": [
              "2009105",
              "2010110",
              "2012106",
              "2012110",
              "2013110",
              "2021104"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Liljeborgia (Liljeborgia) macronyx",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 3,
            "samplesInAOI": 23,
            "totalIndividuals": 2,
            "cruises": [
              "2007105",
              "2007111",
              "2010112",
              "2011105",
              "2013110",
              "2013205",
              "2014115",
              "2019115",
              "2020110",
              "2021104",
              "2022118",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lagis koreni",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 7,
            "samplesInAOI": 13,
            "totalIndividuals": 2,
            "cruises": [
              "2008114",
              "2012110",
              "2013110",
              "2014106",
              "2015109",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Melinnopsis arctica",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 1,
            "samplesInAOI": 12,
            "totalIndividuals": 1,
            "cruises": [
              "2007105",
              "2016113",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Mediomastus fragilis",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 6,
            "samplesInAOI": 11,
            "totalIndividuals": 4,
            "cruises": [
              "2007111",
              "2010110",
              "2012110",
              "2013112",
              "2014115",
              "2020110",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Harmothoe glabra",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 3,
            "samplesInAOI": 8,
            "totalIndividuals": 1,
            "cruises": [
              "2007111",
              "2012110",
              "2013112",
              "2015113",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Kirchenpaueria pinnata",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 1,
            "samplesInAOI": 7,
            "totalIndividuals": 1,
            "cruises": [
              "2006612",
              "2007105",
              "2020104",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Aspidarachna",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 1,
            "samplesInAOI": 3,
            "totalIndividuals": 2,
            "cruises": [
              "2006612",
              "2012106",
              "2013112"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Harmothoe fraserthomsoni",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 1,
            "samplesInAOI": 3,
            "totalIndividuals": 1,
            "cruises": [
              "2007111",
              "2013112",
              "2014106"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aphelochaeta filiformis",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 3,
            "cruises": [
              "2008114"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Kelliopsis jozinae",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2009111"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Amblyops",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 4,
            "samplesInAOI": 6,
            "totalIndividuals": 0,
            "cruises": [
              "2009105",
              "2011113",
              "2012106",
              "2012110",
              "2013110"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Amphilochoides",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 1,
            "samplesInAOI": 5,
            "totalIndividuals": 6,
            "cruises": [
              "2009105",
              "2010112",
              "2020110",
              "2023001009"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Amphilochus",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 2,
            "samplesInAOI": 5,
            "totalIndividuals": 5,
            "cruises": [
              "2007111",
              "2010112",
              "2013205",
              "2014106"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ambasia atlantica",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 1,
            "samplesInAOI": 4,
            "totalIndividuals": 1,
            "cruises": [
              "2007111",
              "2014115",
              "2022118"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Astyris rosacea",
            "totalWeight_kg": 0.002,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 1,
            "cruises": [
              "2009105",
              "2019115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Alvania jeffreysi",
            "totalWeight_kg": 0.001,
            "samplesWithWeight": 1,
            "samplesInAOI": 28,
            "totalIndividuals": 1,
            "cruises": [
              "2009111",
              "2010110",
              "2012106",
              "2013112",
              "2013205",
              "2014106",
              "2015113",
              "2020110",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Trochidae",
            "totalWeight_kg": 0.001,
            "samplesWithWeight": 1,
            "samplesInAOI": 3,
            "totalIndividuals": 1,
            "cruises": [
              "2009111",
              "2010112",
              "2014106"
            ],
            "equipment": [
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leptanthura tenuis",
            "totalWeight_kg": 0.001,
            "samplesWithWeight": 1,
            "samplesInAOI": 21,
            "totalIndividuals": 1,
            "cruises": [
              "2006612",
              "2010110",
              "2012106",
              "2013112",
              "2013205",
              "2015113",
              "2021103",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Syllidia",
            "totalWeight_kg": 0.001,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 2,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leucon (Crymoleucon) tener",
            "totalWeight_kg": 0.001,
            "samplesWithWeight": 1,
            "samplesInAOI": 3,
            "totalIndividuals": 2,
            "cruises": [
              "2011105",
              "2013110",
              "2020110"
            ],
            "equipment": [
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leucon (Macrauloleucon) siphonatus",
            "totalWeight_kg": 0.001,
            "samplesWithWeight": 2,
            "samplesInAOI": 3,
            "totalIndividuals": 4,
            "cruises": [
              "2008104",
              "2008114"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Antalis agilis",
            "totalWeight_kg": 0.001,
            "samplesWithWeight": 2,
            "samplesInAOI": 2,
            "totalIndividuals": 3,
            "cruises": [
              "2008114"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Westwoodilla",
            "totalWeight_kg": 0.001,
            "samplesWithWeight": 2,
            "samplesInAOI": 16,
            "totalIndividuals": 2,
            "cruises": [
              "2006612",
              "2010112",
              "2011105",
              "2011113",
              "2013205",
              "2017103",
              "2017112",
              "2019115",
              "2020104",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Unciolidae",
            "totalWeight_kg": 0.001,
            "samplesWithWeight": 1,
            "samplesInAOI": 8,
            "totalIndividuals": 2,
            "cruises": [
              "2007111",
              "2009105",
              "2009111",
              "2010112",
              "2011113",
              "2013112",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Aricidea (Aricidea) wassi",
            "totalWeight_kg": 0.001,
            "samplesWithWeight": 5,
            "samplesInAOI": 7,
            "totalIndividuals": 1,
            "cruises": [
              "2008104",
              "2012106",
              "2012110",
              "2022708"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Margarites",
            "totalWeight_kg": 0.001,
            "samplesWithWeight": 1,
            "samplesInAOI": 5,
            "totalIndividuals": 1,
            "cruises": [
              "2007111",
              "2010110",
              "2010112"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Acidostoma",
            "totalWeight_kg": 0.001,
            "samplesWithWeight": 2,
            "samplesInAOI": 2,
            "totalIndividuals": 1,
            "cruises": [
              "2007111",
              "2012106"
            ],
            "equipment": [
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Amphilochoides serratipes",
            "totalWeight_kg": 0.001,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 3,
            "cruises": [
              "2006612",
              "2023001009"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ampharete acutifrons",
            "totalWeight_kg": 0.001,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2008114"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Laomedea",
            "totalWeight_kg": 0.001,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2008114"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lumbriclymeninae",
            "totalWeight_kg": 0.001,
            "samplesWithWeight": 3,
            "samplesInAOI": 8,
            "totalIndividuals": 1,
            "cruises": [
              "2010110",
              "2012106",
              "2013110",
              "2018109",
              "2019115",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leuconidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 2,
            "samplesInAOI": 14,
            "totalIndividuals": 1,
            "cruises": [
              "2009111",
              "2011113",
              "2012106",
              "2013110",
              "2014106",
              "2018109",
              "2019115",
              "2021115",
              "2022118"
            ],
            "equipment": [
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leucon (Leucon) nasicoides",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 32,
            "totalIndividuals": 1,
            "cruises": [
              "2011113",
              "2016113",
              "2017103",
              "2018109",
              "2019106",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Macrostylis spinifera",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 5,
            "samplesInAOI": 14,
            "totalIndividuals": 5,
            "cruises": [
              "2007111",
              "2010110",
              "2010112",
              "2011105",
              "2011113",
              "2013110",
              "2013205",
              "2015113",
              "2017103"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lamprops fuscatus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 6,
            "totalIndividuals": 1,
            "cruises": [
              "2007111",
              "2017103",
              "2019106",
              "2021115"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Acari",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 2,
            "samplesInAOI": 3,
            "totalIndividuals": 2,
            "cruises": [
              "2007111",
              "2009111"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Argulus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2011113"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Liriopsis pygmaea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2008114"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Ledella messanensis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 202,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2010112",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014208",
              "2020104",
              "2020110",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Limopsis aurita",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 195,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2011110",
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Yoldiella lenticula",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 164,
            "totalIndividuals": null,
            "cruises": [
              "2006612",
              "2011110",
              "2012110",
              "2013110",
              "2013112",
              "2014106",
              "2014115",
              "2015109",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2021115",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Boxcorer",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leitoscoloplos mammosus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 153,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2013112",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2016113",
              "2017103",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2021115",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leucosolenida",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 120,
            "totalIndividuals": null,
            "cruises": [
              "2016113",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Unciola petalocera",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 102,
            "totalIndividuals": null,
            "cruises": [
              "2008114",
              "2009105",
              "2009111",
              "2010110",
              "2010112",
              "2011113",
              "2012106",
              "2013112",
              "2013205",
              "2014115",
              "2014208",
              "2015113",
              "2019106",
              "2019115",
              "2021103",
              "2021104",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Yoldiella frigida",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 93,
            "totalIndividuals": null,
            "cruises": [
              "2015113",
              "2016113",
              "2017103",
              "2018109",
              "2019115",
              "2020104",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2024007005"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Abyssoninoe",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 7,
            "samplesInAOI": 85,
            "totalIndividuals": 0,
            "cruises": [
              "2010112",
              "2011105",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2018109",
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lysippe labiata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 2,
            "samplesInAOI": 83,
            "totalIndividuals": 0,
            "cruises": [
              "2011113",
              "2013110",
              "2013112",
              "2014106",
              "2014115",
              "2015113",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019115",
              "2020110",
              "2021103",
              "2021115",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Abyssoninoe hibernica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 70,
            "totalIndividuals": 0,
            "cruises": [
              "2011105",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Asbestopluma (Asbestopluma) pennatula",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 65,
            "totalIndividuals": null,
            "cruises": [
              "2019106",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lepeta caeca",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 63,
            "totalIndividuals": null,
            "cruises": [
              "2014106",
              "2015109",
              "2016113",
              "2017103",
              "2017112",
              "2018109",
              "2019115",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aceroides (Aceroides) latipes",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 59,
            "totalIndividuals": null,
            "cruises": [
              "2014106",
              "2014115",
              "2014208",
              "2016113",
              "2017103",
              "2017115",
              "2018109",
              "2019115",
              "2021115",
              "2022118",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Amphicteis ninonae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 55,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2015109",
              "2016113",
              "2017103",
              "2018109",
              "2019106",
              "2019115",
              "2021104",
              "2021115",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Alcyonidium",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 54,
            "totalIndividuals": null,
            "cruises": [
              "2016113",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2024007005"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Ilyarachna torleivi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 53,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2013110",
              "2013205",
              "2014115",
              "2016113",
              "2017103",
              "2021103",
              "2021104",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Ampharete borealis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 2,
            "samplesInAOI": 50,
            "totalIndividuals": 0,
            "cruises": [
              "2012106",
              "2014106",
              "2014115",
              "2016113",
              "2017103",
              "2018109",
              "2019115",
              "2021103",
              "2021115",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Abietinaria abietina",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 45,
            "totalIndividuals": null,
            "cruises": [
              "2019106",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Videograb"
            ]
          },
          {
            "scientificName": "Aporrhais pespelecani",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 45,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2012110",
              "2013112",
              "2013205",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Ascidia obliqua",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 40,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2014208",
              "2020104",
              "2020110",
              "2022118",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Harmothoe imbricata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 40,
            "totalIndividuals": null,
            "cruises": [
              "2019106",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Macoma calcarea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 40,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2014106",
              "2016113",
              "2017103",
              "2017112",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aplidium",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 39,
            "totalIndividuals": null,
            "cruises": [
              "2010112",
              "2013110",
              "2013112",
              "2013205",
              "2014106",
              "2014115",
              "2015109",
              "2016113",
              "2019115",
              "2020104",
              "2020110",
              "2021104",
              "2021115",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Suberites spermatozoon",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 36,
            "totalIndividuals": null,
            "cruises": [
              "2019106",
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Margarites olivaceus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 33,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2014106",
              "2015113",
              "2016113",
              "2017112",
              "2017115",
              "2018109",
              "2019106",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aega bicarinata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 32,
            "totalIndividuals": 0,
            "cruises": [
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2015113",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Amphiura sundevalli",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 31,
            "totalIndividuals": null,
            "cruises": [
              "2016113",
              "2019106",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Argissa hamatipes",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 31,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2013112",
              "2014106",
              "2015109",
              "2016113",
              "2017103",
              "2017115",
              "2019106",
              "2019115",
              "2021104",
              "2021115",
              "2022118",
              "2022708",
              "2023001009"
            ],
            "equipment": [
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Acanthostepheia malmgreni",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 30,
            "totalIndividuals": null,
            "cruises": [
              "2015113",
              "2016113",
              "2018109",
              "2019106",
              "2019115",
              "2021115",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ariadnaria borealis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 30,
            "totalIndividuals": null,
            "cruises": [
              "2006612",
              "2011105",
              "2012106",
              "2013110",
              "2013205",
              "2014106",
              "2014115",
              "2015109",
              "2016113",
              "2018109",
              "2019115",
              "2020104",
              "2021104",
              "2021115",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Ascidia prunum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 29,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2010112",
              "2013110",
              "2013112",
              "2014208",
              "2016113",
              "2017103",
              "2019115",
              "2020104",
              "2020110",
              "2021115",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Levinsenia flava",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 29,
            "totalIndividuals": null,
            "cruises": [
              "2020104",
              "2020110",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aricidea (Acmira) simonae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 7,
            "samplesInAOI": 28,
            "totalIndividuals": 0,
            "cruises": [
              "2012106",
              "2012110",
              "2013112",
              "2013205",
              "2014208",
              "2015113",
              "2020104",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Kirkegaardia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 28,
            "totalIndividuals": null,
            "cruises": [
              "2013112",
              "2013205",
              "2019115",
              "2020110",
              "2021103",
              "2021104",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Laubieriopsis norvegica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 28,
            "totalIndividuals": null,
            "cruises": [
              "2013205",
              "2015113",
              "2020110",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Ascidia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 27,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014115",
              "2015113",
              "2017112",
              "2019106",
              "2019115",
              "2020104",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lytocarpia myriophyllum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 27,
            "totalIndividuals": null,
            "cruises": [
              "2012110",
              "2020104",
              "2021103",
              "2021104",
              "2022118",
              "2023001005",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Amphitrite cirrata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 26,
            "totalIndividuals": 0,
            "cruises": [
              "2012106",
              "2016113",
              "2017112",
              "2018109",
              "2019115",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Ute gladiata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 25,
            "totalIndividuals": null,
            "cruises": [
              "2011110",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Abyssoninoe abyssorum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 24,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2017103",
              "2019106",
              "2020110",
              "2021103",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Alvania testae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 24,
            "totalIndividuals": null,
            "cruises": [
              "2006612",
              "2011105",
              "2011113",
              "2012106",
              "2013112",
              "2013205",
              "2020104",
              "2020110",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Styelidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 24,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2019106",
              "2020110",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Syllis fasciata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 24,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2018109",
              "2019115",
              "2020104",
              "2020110",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Lafoea gracillima",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 23,
            "totalIndividuals": null,
            "cruises": [
              "2019106",
              "2019115",
              "2021103",
              "2021104",
              "2022118",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leiochrides norvegicus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 3,
            "samplesInAOI": 23,
            "totalIndividuals": 0,
            "cruises": [
              "2011113",
              "2012110",
              "2013112",
              "2013205",
              "2014208",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Acanthonotozoma cristatum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 22,
            "totalIndividuals": 0,
            "cruises": [
              "2009105",
              "2012106",
              "2013110",
              "2014115",
              "2015113",
              "2016113",
              "2017103",
              "2018109",
              "2019106",
              "2019115",
              "2021103",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ischyrocerus megalops",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 22,
            "totalIndividuals": null,
            "cruises": [
              "2009111",
              "2016113",
              "2017103",
              "2017112",
              "2017115",
              "2018109",
              "2019115",
              "2020110",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Megamoera dentata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 22,
            "totalIndividuals": null,
            "cruises": [
              "2017103",
              "2017112",
              "2019106",
              "2021115",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Amphilochus anoculus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 21,
            "totalIndividuals": null,
            "cruises": [
              "2009111",
              "2010110",
              "2010112",
              "2013110",
              "2014106",
              "2016113",
              "2017103",
              "2017115",
              "2021104",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Astacilla",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 21,
            "totalIndividuals": null,
            "cruises": [
              "2009111",
              "2010112",
              "2013112",
              "2013205",
              "2017103",
              "2019106",
              "2021103",
              "2021104",
              "2022118",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lepechinellidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 21,
            "totalIndividuals": null,
            "cruises": [
              "2008114",
              "2009105",
              "2010110",
              "2010112",
              "2013110",
              "2013112",
              "2014106"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Syllis kas",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 19,
            "totalIndividuals": null,
            "cruises": [
              "2019115",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Tropidomya abbreviata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 19,
            "totalIndividuals": null,
            "cruises": [
              "2011113",
              "2012106",
              "2012110",
              "2013112",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lafoea fruticosa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 18,
            "totalIndividuals": null,
            "cruises": [
              "2019106",
              "2019115",
              "2020104",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Limatula bisecta",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 18,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2012106",
              "2013205",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Mellonympha mortenseni",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 18,
            "totalIndividuals": null,
            "cruises": [
              "2011113",
              "2012106",
              "2015113",
              "2020110",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Liljeborgia (Lilljeborgiella) ossiani",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 17,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2013110",
              "2013205",
              "2019106",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2021115",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Antedonoidea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 16,
            "totalIndividuals": null,
            "cruises": [
              "2021103",
              "2021104",
              "2021115",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Artacama proboscidea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 16,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2016113",
              "2017103",
              "2019115",
              "2021104",
              "2021115",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Asbestopluma",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 16,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2010112",
              "2011113",
              "2019106",
              "2020104",
              "2020110",
              "2021103",
              "2021104",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aspidosiphon (Aspidosiphon) muelleri muelleri",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 16,
            "totalIndividuals": null,
            "cruises": [
              "2012110",
              "2013112",
              "2013205",
              "2015113",
              "2019106",
              "2020104",
              "2020110"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Astacilla granulata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 16,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2013112",
              "2013205",
              "2015113",
              "2021103",
              "2021104",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Sertularella polyzonias",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 16,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Aplidium mutabile",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 15,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2012106",
              "2013110",
              "2016113",
              "2020104",
              "2020110",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Latrunculia (Biannulata) triloba",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 15,
            "totalIndividuals": null,
            "cruises": [
              "2011113",
              "2020110",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leptagonus decagonus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 15,
            "totalIndividuals": null,
            "cruises": [
              "2016113",
              "2017115",
              "2019115",
              "2021115",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Malacalcyonacea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 15,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2010112",
              "2011113"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Allantactis parasitica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 14,
            "totalIndividuals": null,
            "cruises": [
              "2021115",
              "2022708",
              "2024007005"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Altenaeum dawsoni",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 14,
            "totalIndividuals": null,
            "cruises": [
              "2017112",
              "2021115"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Harmothoe fernandi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 8,
            "samplesInAOI": 14,
            "totalIndividuals": 0,
            "cruises": [
              "2010110",
              "2012106",
              "2012110",
              "2013205",
              "2014208",
              "2015113",
              "2017103",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Ischnomesus norvegicus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 14,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2012110",
              "2019106",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lophogaster typicus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 2,
            "samplesInAOI": 14,
            "totalIndividuals": 0,
            "cruises": [
              "2012110",
              "2013112",
              "2013205",
              "2014208"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Astarte crebricostata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 13,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2010112",
              "2013112",
              "2014115",
              "2016113"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Harmothoe mariannae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 5,
            "samplesInAOI": 13,
            "totalIndividuals": 0,
            "cruises": [
              "2011110",
              "2012106",
              "2012110",
              "2013112",
              "2014106",
              "2016113",
              "2020104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lepraliella contigua",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 13,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Malletia johnsoni",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 13,
            "totalIndividuals": null,
            "cruises": [
              "2013205",
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Ampharete baltica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 2,
            "samplesInAOI": 12,
            "totalIndividuals": 0,
            "cruises": [
              "2010110",
              "2012106",
              "2013110",
              "2013112",
              "2013205",
              "2014115",
              "2016113",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Amphipholis torelli",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 12,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Anapagurus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 12,
            "totalIndividuals": null,
            "cruises": [
              "2010112",
              "2011110",
              "2012106",
              "2012110",
              "2014208"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Anoplodactylus typhlops",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 12,
            "totalIndividuals": null,
            "cruises": [
              "2013112",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Harmothoe rarispina",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 12,
            "totalIndividuals": null,
            "cruises": [
              "2015109",
              "2016113",
              "2017103",
              "2017112",
              "2018109",
              "2019106",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lafoeina maxima",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 12,
            "totalIndividuals": null,
            "cruises": [
              "2019106",
              "2019115",
              "2020104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "Videograb"
            ]
          },
          {
            "scientificName": "Lepidorhombus boscii",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 12,
            "totalIndividuals": null,
            "cruises": [
              "2013112",
              "2013205",
              "2015113",
              "2020104",
              "2020110",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Leucothoe lilljeborgi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 2,
            "samplesInAOI": 12,
            "totalIndividuals": 0,
            "cruises": [
              "2012110",
              "2013112",
              "2021104",
              "2022118",
              "2023001009"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lucernaria bathyphila",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 12,
            "totalIndividuals": null,
            "cruises": [
              "2009111",
              "2010110",
              "2010112",
              "2011113",
              "2012106",
              "2016113",
              "2017103",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Suberites montiniger",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 12,
            "totalIndividuals": null,
            "cruises": [
              "2016113",
              "2018109",
              "2019106",
              "2019115",
              "2020110",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Acanthonotozoma sinuatum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 11,
            "totalIndividuals": null,
            "cruises": [
              "2014115",
              "2016113",
              "2017103",
              "2019106",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Alvania punctura",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 11,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2013112",
              "2020110",
              "2021103"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leucon afeni",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 11,
            "totalIndividuals": null,
            "cruises": [
              "2015109",
              "2017103",
              "2017115",
              "2022708"
            ],
            "equipment": [
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Liparis fabricii",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 11,
            "totalIndividuals": null,
            "cruises": [
              "2016113",
              "2018109",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Macrochaeta clavicornis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 4,
            "samplesInAOI": 11,
            "totalIndividuals": 10,
            "cruises": [
              "2010110",
              "2010112",
              "2012106",
              "2020110",
              "2021103",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Macrostylis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 11,
            "totalIndividuals": null,
            "cruises": [
              "2009111",
              "2010110",
              "2012106",
              "2013112",
              "2014106",
              "2022118"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Alcyonidium gelatinosum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 10,
            "totalIndividuals": null,
            "cruises": [
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Amphissa acutecostata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 10,
            "totalIndividuals": null,
            "cruises": [
              "2015113",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Annelida",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 10,
            "totalIndividuals": null,
            "cruises": [
              "2012110",
              "2016113",
              "2019106",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Anthuroidea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 10,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2010112",
              "2013112",
              "2013205",
              "2014115",
              "2014208",
              "2016113"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Inflatella pellicula",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 10,
            "totalIndividuals": null,
            "cruises": [
              "2020110",
              "2021103",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Kukenthalia borealis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 10,
            "totalIndividuals": null,
            "cruises": [
              "2011113",
              "2013110",
              "2015109",
              "2016113",
              "2017103",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leucon (Leucon)",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 10,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2013110",
              "2015109",
              "2016113",
              "2017103",
              "2018109",
              "2021115",
              "2022708"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Lumbrineris latreilli",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 10,
            "totalIndividuals": 0,
            "cruises": [
              "2006612",
              "2009105",
              "2014208"
            ],
            "equipment": [
              "Boxcorer",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Mangeliidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 10,
            "totalIndividuals": null,
            "cruises": [
              "2011113",
              "2014106",
              "2015113",
              "2016113",
              "2019115",
              "2021104",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Melonanchora elliptica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 10,
            "totalIndividuals": null,
            "cruises": [
              "2011113",
              "2012106",
              "2020104",
              "2021103"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Sertularia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 10,
            "totalIndividuals": null,
            "cruises": [
              "2019106",
              "2019115",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Sycettusa glacialis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 10,
            "totalIndividuals": null,
            "cruises": [
              "2018109",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Anomalisipho verkruezeni",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 9,
            "totalIndividuals": null,
            "cruises": [
              "2013112",
              "2016113",
              "2017103",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Aquiloniella scabra",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 9,
            "totalIndividuals": null,
            "cruises": [
              "2006612",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Astacilla dilatata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 9,
            "totalIndividuals": null,
            "cruises": [
              "2010112",
              "2014106",
              "2014115",
              "2017103",
              "2022118"
            ],
            "equipment": [
              "RP-sledge",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Icelus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 9,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2013112",
              "2019115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Ilyarachna bicornis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 9,
            "totalIndividuals": null,
            "cruises": [
              "2015109",
              "2015113",
              "2016113",
              "2017103",
              "2017115"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Iolanthe typhlops",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 9,
            "totalIndividuals": null,
            "cruises": [
              "2013112",
              "2013205",
              "2015113",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Isaeidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 9,
            "totalIndividuals": null,
            "cruises": [
              "2014106",
              "2014115",
              "2015113",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Liponema multicorne",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 9,
            "totalIndividuals": null,
            "cruises": [
              "2017103",
              "2017115",
              "2019106",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Macrostylis longiremis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 9,
            "totalIndividuals": 0,
            "cruises": [
              "2009111",
              "2010110",
              "2010112",
              "2011105",
              "2012110",
              "2013205"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Melinna",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 9,
            "totalIndividuals": 1,
            "cruises": [
              "2010110",
              "2013112",
              "2018109",
              "2020104",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Sebastes mentella",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 9,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2011105",
              "2014106",
              "2017103",
              "2021115",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Triglops nybelini",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 9,
            "totalIndividuals": null,
            "cruises": [
              "2016113",
              "2019115",
              "2021115",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Yoldia hyperborea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 9,
            "totalIndividuals": null,
            "cruises": [
              "2016113",
              "2018109",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Aclis walleri",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 8,
            "totalIndividuals": null,
            "cruises": [
              "2012110",
              "2013112",
              "2013205",
              "2015113",
              "2020110",
              "2021103"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Alvania moerchii",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 8,
            "totalIndividuals": null,
            "cruises": [
              "2017112",
              "2018109",
              "2019115",
              "2020110",
              "2021104"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Ampharete undecima",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 8,
            "totalIndividuals": null,
            "cruises": [
              "2014208",
              "2015113",
              "2017103",
              "2019106",
              "2021115"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aponuphis bilineata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 3,
            "samplesInAOI": 8,
            "totalIndividuals": 0,
            "cruises": [
              "2012110",
              "2013112",
              "2013205",
              "2021104"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Aquiloniella paenulata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 8,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aristias",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 8,
            "totalIndividuals": null,
            "cruises": [
              "2021103",
              "2021104",
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leptanthuridae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 8,
            "totalIndividuals": 0,
            "cruises": [
              "2012106",
              "2014106",
              "2014115",
              "2015109",
              "2016113",
              "2017103"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Sertularia tenera",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 8,
            "totalIndividuals": null,
            "cruises": [
              "2021103",
              "2021115",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Trypanosyllis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 5,
            "samplesInAOI": 8,
            "totalIndividuals": 0,
            "cruises": [
              "2010110",
              "2011113",
              "2012106",
              "2013112",
              "2013205"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Tubulariidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 8,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Weltnerium cornutum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 8,
            "totalIndividuals": null,
            "cruises": [
              "2009105",
              "2013112",
              "2013205",
              "2015113",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Acanthonotozoma",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 7,
            "totalIndividuals": null,
            "cruises": [
              "2009105",
              "2010110",
              "2013110",
              "2017103",
              "2019106",
              "2021115"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ampharete goesi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 7,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Aplousobranchia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 7,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2012106",
              "2016113",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Katianira bilobata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 7,
            "totalIndividuals": null,
            "cruises": [
              "2006612",
              "2012106",
              "2015113",
              "2022708",
              "2022846"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Kurtiella tumidula",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 7,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2013112",
              "2014106",
              "2020110",
              "2021104"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Leptanthura",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 7,
            "totalIndividuals": null,
            "cruises": [
              "2009111"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Lissodendoryx",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 7,
            "totalIndividuals": null,
            "cruises": [
              "2011110",
              "2011113",
              "2012106",
              "2021103"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Sertularia similis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 7,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Syllis variegata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 7,
            "totalIndividuals": null,
            "cruises": [
              "2012110",
              "2013112",
              "2013205"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Tubulipora",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 7,
            "totalIndividuals": null,
            "cruises": [
              "2021115",
              "2023001009",
              "2024007005"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Typhlotanais",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 6,
            "samplesInAOI": 7,
            "totalIndividuals": 0,
            "cruises": [
              "2011113",
              "2012106",
              "2012110"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Verruca stroemia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 7,
            "totalIndividuals": null,
            "cruises": [
              "2011113",
              "2012106",
              "2012110",
              "2013110",
              "2013112",
              "2013205",
              "2020104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Abietinaria pulchra",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 6,
            "totalIndividuals": null,
            "cruises": [
              "2011113",
              "2019106",
              "2019115",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Ampelisca brevicornis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 6,
            "totalIndividuals": 0,
            "cruises": [
              "2012106",
              "2012110",
              "2013110",
              "2013205",
              "2023001005"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Amphiura griegi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 6,
            "totalIndividuals": null,
            "cruises": [
              "2011113",
              "2012106",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Anonyx debruynii",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 6,
            "totalIndividuals": null,
            "cruises": [
              "2018109",
              "2019106",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aricidea (Aricidea) albatrossae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 6,
            "totalIndividuals": 0,
            "cruises": [
              "2012106",
              "2013112",
              "2013205",
              "2015113",
              "2022708"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Ascidia callosa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 6,
            "totalIndividuals": null,
            "cruises": [
              "2014115",
              "2016113",
              "2018109",
              "2019115",
              "2020110",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Astarte subaequilatera",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 6,
            "totalIndividuals": null,
            "cruises": [
              "2013112",
              "2014106",
              "2014208",
              "2016113",
              "2019115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Laonice appelloefi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 6,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leieschara",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 6,
            "totalIndividuals": null,
            "cruises": [
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leieschara coarctata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 6,
            "totalIndividuals": null,
            "cruises": [
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Scrupocellaria",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 6,
            "totalIndividuals": null,
            "cruises": [
              "2006612",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Sertularella gayi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 6,
            "totalIndividuals": null,
            "cruises": [
              "2012110",
              "2020104",
              "2021103",
              "2021104",
              "2022118",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Sertularia argentea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 6,
            "totalIndividuals": null,
            "cruises": [
              "2021115",
              "2023001009",
              "2024007003"
            ],
            "equipment": [
              "Beamtrawl",
              "Bioboks",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Syllides",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 6,
            "totalIndividuals": 0,
            "cruises": [
              "2012110",
              "2013112",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Varicorbula gibba",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 6,
            "totalIndividuals": null,
            "cruises": [
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Westwoodilla megalops",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 6,
            "totalIndividuals": null,
            "cruises": [
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Whoia angusta",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 6,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2010112",
              "2013112",
              "2014115",
              "2014208"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Acanthonotozoma inflatum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2018109",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aeginina longicornis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2010112",
              "2021103"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Aglaophamus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2006612",
              "2015113",
              "2018109",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Alvania zetlandica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2018109"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Amphilochus hamatus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2010112",
              "2012106",
              "2021115"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Apherusa jurinei",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 2,
            "samplesInAOI": 5,
            "totalIndividuals": 0,
            "cruises": [
              "2011105",
              "2012106",
              "2016113",
              "2017103"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Apherusa sarsii",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 5,
            "totalIndividuals": 0,
            "cruises": [
              "2012106",
              "2016113",
              "2017112",
              "2019115"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Aphroditidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2013112",
              "2020104",
              "2020110"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Astrophorina",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2020104",
              "2020110",
              "2021103",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Idotea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2009111",
              "2012106"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Iotroata abyssi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2020104",
              "2020110"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Kirchenpaueria bonnevieae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2021103",
              "2022118",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Kirkegaardia serrata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2021103"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Laona quadrata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2006612",
              "2017112"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Lasaea adansoni",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2013205",
              "2020110",
              "2021103"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leptomysinae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 5,
            "totalIndividuals": 0,
            "cruises": [
              "2011110",
              "2012106",
              "2012110",
              "2013112",
              "2017103"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Leucosolenia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2020110",
              "2021103",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lycopodina infundibulum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2016113",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Sebastes",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2009111",
              "2012106",
              "2019106",
              "2020110",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Sertularia mirabilis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2019106",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Videograb"
            ]
          },
          {
            "scientificName": "Suberites carnosus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2011113",
              "2015113",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Sycon ciliatum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 5,
            "totalIndividuals": null,
            "cruises": [
              "2019106",
              "2019115",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Aegiochus arctica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2013112",
              "2013205",
              "2015113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Amphipholis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Amphiura chiajei",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2006612",
              "2012106",
              "2012110"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Andaniopsinae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2013110"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Aphrodita",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2013112",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aphrodita alta",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2013205",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Aplidium glabrum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2013205",
              "2016113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Aporrhais serresiana",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2021104",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Artemisina arcigera",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2020104",
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Harmothoe oculinarum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 4,
            "samplesInAOI": 4,
            "totalIndividuals": 0,
            "cruises": [
              "2012110"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Harmothoe serrata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2019106",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Harpinia curtipes",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2009111",
              "2013110",
              "2013205"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ischyrocerus latipes",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2010112",
              "2015113",
              "2017103",
              "2021115"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Janulum spinispiculum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2020104",
              "2021103"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Kerguelenia borealis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 4,
            "totalIndividuals": 0,
            "cruises": [
              "2011113",
              "2013110",
              "2015113"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Kirkegaardia dorsobranchialis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Kolga hyalina",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2009111",
              "2010112",
              "2026007006"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Kophobelemnon",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2020110"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lebetus scorpioides",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2015113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lepechinella chrysotheras",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2010112",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Leptasterias (Leptasterias) muelleri",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2011105",
              "2019106",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Leptasterias hyperborea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2019106",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Leptosynapta",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2012110",
              "2013110",
              "2013112"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Leucon (Leucon) profundus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2016113"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Liparis bathyarcticus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2016113",
              "2019115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Lissodendoryx (Lissodendoryx) fragilis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2020104",
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Malmgrenia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2014115",
              "2020110",
              "2021115"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Melaenis loveni",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2018109"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Melanella martynjordani",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2021104"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Mendicula",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2022708"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Menestho truncatula",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2018109"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Metopa alderi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2015113",
              "2019106"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Metopa bruzelii",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2009105",
              "2010110",
              "2013110"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Serripes groenlandicus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2017103"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Sertularella robusta",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2011113",
              "2012106",
              "2012110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Sycandra utriculus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2016113",
              "2019106",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Sycettusa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Tylobranchion nordgaardi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2015113"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Unciola crassipes",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2010112",
              "2013112",
              "2019106",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Velutinidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2021115",
              "2022846"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Virgulariidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 4,
            "totalIndividuals": null,
            "cruises": [
              "2011113",
              "2023001009",
              "2023001014"
            ],
            "equipment": [
              "Beamtrawl",
              "Bioboks",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Acanthostepheia incarinata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2017103",
              "2018109"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Alcyonidiidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Alvania scrobiculata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2020110",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Amauropsis islandica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2017112",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Amphianthus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2022708"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Amphiblestrum solidum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Anoplodactylus arnaudae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2012110",
              "2013112"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ansphyrapus tudes",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2012110"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Anthoathecata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Aphelochaeta mcintoshi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 3,
            "samplesInAOI": 3,
            "totalIndividuals": 0,
            "cruises": [
              "2012106",
              "2012110"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Aplidium pallidum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Argentina",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2021104",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Aricidea abranchiata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 3,
            "totalIndividuals": 0,
            "cruises": [
              "2012106",
              "2013205",
              "2019106"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Arrhinopsis longicornis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2019115",
              "2021115"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ascidia virginea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2010112",
              "2012106"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Asconema",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2022708",
              "2023001014"
            ],
            "equipment": [
              "Beamtrawl",
              "Bioboks",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Astropecten",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Infundibulipora lucernaria",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2017115",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Janiralata tricornis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Laetmonice uschakovi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 3,
            "samplesInAOI": 3,
            "totalIndividuals": 0,
            "cruises": [
              "2010112"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lafoea grandis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2019115"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leitoscoloplos",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 3,
            "totalIndividuals": 0,
            "cruises": [
              "2012106",
              "2013205",
              "2014106"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leucandra",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2011113",
              "2012106",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Leucia violacea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2020110",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Leuckartiara octona",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2022118",
              "2023001005"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leucon (Crymoleucon)",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2009105",
              "2020110"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Lichenopora",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Liljeborgia (Lilljeborgiella) caliginis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2019106"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Limaria loscombi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2012110"
            ],
            "equipment": [
              "Beamtrawl",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Limatula subovata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2012110",
              "2013112"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Lumbrineris futilis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2015113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lycopodina lycopodium",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lysianassa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 2,
            "samplesInAOI": 3,
            "totalIndividuals": 0,
            "cruises": [
              "2012106",
              "2021103"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Lysilla",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 2,
            "samplesInAOI": 3,
            "totalIndividuals": 0,
            "cruises": [
              "2012106",
              "2015113"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Macropipus tuberculatus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2012110",
              "2014208"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Maeridae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2010112",
              "2017103"
            ],
            "equipment": [
              "RP-sledge",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Marsenina glabra",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2013110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Maurolicus muelleri",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2013112",
              "2019115"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Melphidippella macra",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 3,
            "totalIndividuals": 0,
            "cruises": [
              "2012110",
              "2019106",
              "2019115"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Menigrates obtusifrons",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2009105",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Metaconchoecia skogsbergi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2009105"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Metopa pusilla",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2009105"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Securiflustra securifrons",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Sertularella tenella",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2019106",
              "2022118"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Suberitidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2016113",
              "2020104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Sycettusa thompsoni",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Syllis oerstedi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2013112"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Symplectoscyphus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2021115",
              "2022118"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Trochochaeta multisetosa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 3,
            "samplesInAOI": 3,
            "totalIndividuals": 1,
            "cruises": [
              "2010112",
              "2011110",
              "2012110"
            ],
            "equipment": [
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Trochoidea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2010112",
              "2013112"
            ],
            "equipment": [
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Trophonopsis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2010112"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Tubificinae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Tubificoides",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Turridae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2018109"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Urticina",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Wimvadocus torelli",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2018109",
              "2021104"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Xantho pilipes",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2013112",
              "2014208",
              "2021103"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Xylophaga dorsalis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2013112"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Zeugopterus norvegicus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 3,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2012106",
              "2020104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Acanthella erecta",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Aclis sarsi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2020110"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Admete",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2011110",
              "2016113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Aega monophthalma",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2015113",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Aldisa zetlandica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2016113",
              "2017103"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Alentia gelatinosa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 0,
            "cruises": [
              "2010110",
              "2020104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Alvania subsoluta",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2010112",
              "2021104"
            ],
            "equipment": [
              "Small VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Ampelisca anomala",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 0,
            "cruises": [
              "2012106",
              "2013205"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Amphicteis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2013205",
              "2019115"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Amphicteis wesenbergae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 0,
            "cruises": [
              "2010112",
              "2019115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Andaniopsis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2013205"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Anomia ephippium",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Apomatus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 1,
            "cruises": [
              "2010110",
              "2016113"
            ],
            "equipment": [
              "Beamtrawl",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Apseudidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 2,
            "samplesInAOI": 2,
            "totalIndividuals": 0,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Arctolembos arcticus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2015109",
              "2015113"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Arctonula arctica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Arctopleustes glabricauda",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2013112"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Argentina silus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2014106",
              "2014208"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Aricidea (Aricidea) minuta",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 1,
            "cruises": [
              "2006612",
              "2010112"
            ],
            "equipment": [
              "Large VV grab",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Aricidea hartmanae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2013112"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Artemisina lundbecki",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2019115",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Asajirus indicus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2013112"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Asbestopluma (Asbestopluma) bihamatifera",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2019106"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Ascidia conchilega",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012110",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Ascidia mentula",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2012110"
            ],
            "equipment": [
              "Beamtrawl",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Asconema foliatum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2019115",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Asteronyx",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Atelecyclus rotundatus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2014208",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Atergia corticata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2020104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Idotea granulosa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2017112"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Idotea neglecta",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2009111"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Iophon dubium",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Iophon piceum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2021103",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Iphinoe trispinosa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2022118"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Iphinopsis inflata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Isididae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2022118",
              "2023001009"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Jaera",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 2,
            "samplesInAOI": 2,
            "totalIndividuals": 0,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Jassa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2009105",
              "2021104"
            ],
            "equipment": [
              "RP-sledge",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Katerythrops oceanae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2014208"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Lafoeina tenuis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2021103"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lanassa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2022118",
              "2022708"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Laothoes polylovi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2013205"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Leieschara subgracilis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Lepechinella eupraxiella",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2013205"
            ],
            "equipment": [
              "Large VV grab",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Lepechinella helgii",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2021104",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Lepechinelloides karii",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "Beamtrawl",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lepidorhombus whiffiagonis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2012110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Leucon (Leucon) robustus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2013110",
              "2016113"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Leucothoidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012110",
              "2020104"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Leufroyia leufroyi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2020104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Limneria",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2016113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Liparis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Liparis liparis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lissodendoryx (Ectyodoryx) atlantica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lissodendoryx (Lissodendoryx) complicata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lophaster",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2017103"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Luidia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lycodes seminudus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lycopodina tendali",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lyonsiella subquadrata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2013205"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lysianassoidea incertae sedis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2010112",
              "2016113"
            ],
            "equipment": [
              "Beamtrawl",
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Macrochaeta helgolandica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 2,
            "samplesInAOI": 2,
            "totalIndividuals": 0,
            "cruises": [
              "2009105",
              "2012106"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Macropipus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2011110",
              "2013112"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Majoidea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012106",
              "2021103"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Mallotus villosus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2014106",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Malmgrenia ljungmani",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 2,
            "totalIndividuals": 0,
            "cruises": [
              "2012110",
              "2020104"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Melanella polita",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Melphidippa willemiana",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2019106",
              "2019115"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Metopa longicornis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2009105",
              "2009111"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Metopa propinqva",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2009105",
              "2013110"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Scrupocellaria scrupea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Scutopus robustus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Sertularia fabricii",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2021104",
              "2021115"
            ],
            "equipment": [
              "Beamtrawl",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Sertularioidea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2019115"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Suberites",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2021104",
              "2024001021"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Sycettusa kuekenthali",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Syllides longocirratus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2017103",
              "2019115"
            ],
            "equipment": [
              "Large VV grab",
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Synaptidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2022846"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Tubularia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2011105",
              "2014115"
            ],
            "equipment": [
              "Beamtrawl",
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Turbicellepora avicularis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Typhlotanais aequiremis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Velatida",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2020110",
              "2022708"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Verrucidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2010110",
              "2010112"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Verrucomorpha",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 2,
            "totalIndividuals": null,
            "cruises": [
              "2013112",
              "2014106"
            ],
            "equipment": [
              "Beamtrawl",
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Acanthancora aenigma",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Acantheurypon spinispinosum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Acanthicolepis zibrowii",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2014115"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Acanthocardia echinata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2016113"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Acanthodoris pilosa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2016113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Acanthonotozoma rusanovae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2014106"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Acanthonotozomatidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2014106"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Acanthostepheia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2016113"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Aechmalotus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2009105"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Aega",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013112"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Aega crenulata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Aegidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2015113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Aeginina",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2009105"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Aegiochus gracilipes",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Alcyonidium diaphanum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2017112"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Alcyonidium mamillatum erectum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Alcyonium",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Alvania verrilli",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Amathillopsidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2014208"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Amathillopsis affinis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2017103"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Amblyopsoides crozetii",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2009111"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Amblyosyllis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Amblyosyllis finmarchica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Ammodytes marinus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2017103"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Ammotheidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Amphicteis sundevalli",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2018109"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Amphinomidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 0,
            "cruises": [
              "2010112"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Amphithoides",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2009111"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Amphitrite figulus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 0,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Amphiura fragilis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Ampithoe",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013110"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Anchistioides",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013112"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Andaniexinae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013110"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Anguillosyllis pupa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 3,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Anisarchus medius",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2022708"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Anobothrus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2014106"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Anoplodactylus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Antho",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2015113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Anthomastus grandiflorus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Aora spinicornis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2022118"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Apherusa cirrus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Apherusa glacialis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2022846"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Apistobranchus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2014106"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Apistobranchus tenuis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Apodida",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Apseudes",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2022118"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Arcopella balaustina",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013112"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Arcturus baffini",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Aricidea (Strelzovia) parabelgicae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2020110"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Articulata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Asbestopluma (Asbestopluma)",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2019106"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Asbestopluma (Asbestopluma) furcata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2011113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Ascidia dijmphniana",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2017103"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Asellus (Asellus) aquaticus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 0,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Aspidosiphonidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2015113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Astacilla longispina",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Astyra",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Harmothoe extenuata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2017103"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Harmothoe spinifera",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Harpacticoida incertae sedis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Harpinia clivicola",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013110"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Harpinia crenuloides",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2011113"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ichnopus spinicornis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 0,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Idanthyrsus saxicavus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2014208"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Idmidronea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2015113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Idmonea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Ilyarachna bergendahli",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2022708"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Ilyarachna frami",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013205"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Ilyarachna propinqua",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2014115"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ilyarachna una",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013205"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Inachus phalangium",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013205"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Inflatella",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2020110"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Iophon nigricans",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Iothia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2010112"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Iotroata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021103"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Iotroata oxeata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Iotroata polydentata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Iphinopsis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013205"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Ischnomesidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Jassa falcata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2009105"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Kinetoskias",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Kirchenpaueria",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Kolga nana",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2022118"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Kurtiella",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013112"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Kurtiella ovata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2016113"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Lacuna crassior",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2018109"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lacuna vincta",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Lacydoniidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Lafoeina",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Lamellaria latens",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Laomedea angulata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021103"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Laomedea flexuosa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2020104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Laubieriopsis cabiochi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2015113"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Leanira hystricis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2014208"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Leilaster radians",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2017103"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Leiochone",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2019106"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leiochrides",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2022118"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lepadomorpha",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Lepas",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lepetidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013112"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Lepidasthenia brunnea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2015113"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Lepralioides nordlandica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Leptochiton cancellatus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Leptognathia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013205"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Leptognathiidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013205"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Leptosynapta decaria",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013112"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Leptothecata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Leucia nivea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2014115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Leucopsila stilifera",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2020104"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Leucothoe articulosa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 0,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Levinsenia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Levinsenia oculata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2014115"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Liljeborgia (Liljeborgia) inermis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013110"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Liljeborgia (Lilljeborgiella) abyssotypica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2009111"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Limacina helicina",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2020104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Limatula demiradiata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013205"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Limatula hyperborea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Liocyma fluctuosa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2017103"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Liponema",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2017103"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Lissoclinum aureum",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lissodendoryx (Lissodendoryx) lundbecki",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2020104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lucernaria",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Luidia ciliaris",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lumbrineris coccinea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lumpeninae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2017103"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Lycenchelys kolthoffi",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2019115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lycodes reticulatus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2014208"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lycopodina",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2019115"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lycopodina minuta",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Lyonsia norwegica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Lysippe fragilis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 0,
            "cruises": [
              "2012110"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Macandrevia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013205"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Macellicephala",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2010112"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Macellicephala violacea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2019115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Macoma loveni",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2016113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Macrostylidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Madrepora oculata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2015113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Maera",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013205"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Maera tenera",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013112"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Maldane cristata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2017103"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Malmgrenia andreapolis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2020110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Malmgrenia arenicolae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013112"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Malmgrenia castanea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Malmgrenia lunulata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013112"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Margarites helicinus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2014106"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Margarites vahlii",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Megaluropus agilis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2022118"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Melanella",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Melanella frielei",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Melita",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Mellonympha",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2015113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Melonanchora",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Melonanchora emphysema",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Melphidippella",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2009105"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Membranipora membranacea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2022118"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Membraniporoidea",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Merluccius merluccius",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2014208"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Mesochaetopterus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 0,
            "cruises": [
              "2009111"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Metopa clypeata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Metopa colliei",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2009105"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Metopa latimana",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 1,
            "cruises": [
              "2007111"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Metopa quadrangula",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2010112"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Metopa submajuscula",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Securiflustra",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2015113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Semisuberites cribrosa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Sepiida",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2011105"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Sepiola",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021103"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Sepiola atlantica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2020104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Sertularella porcupine",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021103"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Styela theeli",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013205"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Suberites ficus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2018109"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Suberites luetkenii",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Syllides articulocirratus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 0,
            "cruises": [
              "2010112"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Triglops pingelii",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2018109"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Trischizostoma raschii",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2020110"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Trivia monacha",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2011113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Trochochaeta",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013205"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Trochochaeta carica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2015113"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Trophon",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Trophonopsis orpheus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Turbicellepora",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Turbicellepora nodulosa",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Turritellinella tricarinata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2022118"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Turritellopsis stimpsoni",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Typhlotanais tenuicornis",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "Large VV grab"
            ]
          },
          {
            "scientificName": "Tytthocope",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013110"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Ulosa digitata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2020104"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Umbellula encrinus",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Umbonula patens",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2021115"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Umbrina",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2009105"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Unciolinae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2010110"
            ],
            "equipment": [
              "VVgrab020"
            ]
          },
          {
            "scientificName": "Urothoidae",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 1,
            "samplesInAOI": 1,
            "totalIndividuals": 0,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Valvatida",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012110"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Valvifera",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2009111"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Venus casina",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2022118"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Virgularia tuberculata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2022118"
            ],
            "equipment": [
              "Small VV grab"
            ]
          },
          {
            "scientificName": "Volutomitra groenlandica",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2013112"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Westwoodilla rectirostris",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2020104"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Whoia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "RP-sledge"
            ]
          },
          {
            "scientificName": "Yoldia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2006612"
            ],
            "equipment": [
              "Boxcorer"
            ]
          },
          {
            "scientificName": "Zatsepinia",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2015113"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Zygophylax brownei",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2019106"
            ],
            "equipment": [
              "Beamtrawl"
            ]
          },
          {
            "scientificName": "Zygophylax pinnata",
            "totalWeight_kg": 0.0,
            "samplesWithWeight": 0,
            "samplesInAOI": 1,
            "totalIndividuals": null,
            "cruises": [
              "2012106"
            ],
            "equipment": [
              "Beamtrawl"
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
    "actsOnProperty": {
      "@id": "sosa:actsOnProperty",
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
    "hasResult": {
      "@id": "sosa:hasResult",
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
    "hasSimpleResult": {
      "@id": "sosa:hasSimpleResult",
      "@type": "@id"
    },
    "hasSubSystem": {
      "@id": "sosa:hasSubSystem",
      "@type": "@id",
      "@container": "@set"
    },
    "hasUltimateFeatureOfInterest": {
      "@id": "sosa:hasUltimateFeatureOfInterest",
      "@type": "@id"
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
    "madeObservation": {
      "@id": "sosa:madeObservation",
      "@type": "@id"
    },
    "madeSampling": {
      "@id": "sosa:madeSampling",
      "@type": "@id"
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
    "resultTime": "sosa:resultTime",
    "phenomenonTime": {
      "@id": "sosa:phenomenonTime",
      "@type": "@id"
    },
    "hasFeatureOfInterest": {
      "@id": "sosa:hasFeatureOfInterest",
      "@type": "@id"
    },
    "observedProperty": {
      "@context": {
        "@base": "https://w3id.org/iliad/jellyfish/property/"
      },
      "@id": "sosa:observedProperty",
      "@type": "@id"
    },
    "usedProcedure": {
      "@id": "sosa:usedProcedure",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "sosa:madeBySensor",
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

