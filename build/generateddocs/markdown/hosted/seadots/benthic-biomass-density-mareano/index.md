
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

The calculator `_sources/reef-effect/scripts/utsira_reef_biomass.py` reads `data.perTaxon[].scientificName` and `data.perTaxon[].density_kg_m2` to populate `D_pre,i`. Both are marked `required` in the schema.

## Retrieval

MAREANO does not expose a single REST endpoint that returns per-taxon biomass density aggregated over an arbitrary AOI. The realistic retrieval path is the OBIS occurrence API (per-record observations, aggregated off-line) — recorded under `data.provenance.nearestAuthoritativeSource`.

## Examples

### MAREANO benthic biomass density — Norwegian shelf
#### json
```json
{
  "id": "https://example.org/norwegian-ses/benthic-biomass-density-mareano/from-imr-observations",
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
    "title": "MAREANO benthic biomass density derived from IMR/Marbunn observations",
    "description": "Per-taxon benthic biomass density estimate derived from raw IMR / MAREANO Marbunn catch-sample observations by converting catch weights to point densities and extrapolating over the AOI with IDW.",
    "created": "2026-05-26",
    "updated": "2026-05-26",
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
      "Marbunn",
      "IMR",
      "benthic biomass",
      "density",
      "transform"
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
      "name": "MAREANO benthic biomass density from IMR observations",
      "description": "Aggregate per-taxon density estimate transformed from raw Marbunn observation points using IDW interpolation over the AOI.",
      "role": "primary baseline",
      "source": "https://example.org/norwegian-ses/benthic-biomass-observations-imr/all-species-cruises-features",
      "format": "application/json",
      "vocabularyTerm": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano",
      "observedProperty": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano",
      "phenomenonTime": "2006612/2026007006",
      "data": {
        "units": "kg m-2",
        "samplePeriod": "2006612/2026007006",
        "samplingProgramme": "MAREANO / IMR Marbunn",
        "perTaxon": [
          {
            "scientificName": "Umbellula",
            "density_kg_m2": 83.16352182,
            "habitat": "unclassified",
            "depthBand_m": "706-1532",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.51640898
          },
          {
            "scientificName": "Aplysilla",
            "density_kg_m2": 50.0,
            "habitat": "unclassified",
            "depthBand_m": "180-355",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 50.0
          },
          {
            "scientificName": "Asperarca nodulosa",
            "density_kg_m2": 29.19124244,
            "habitat": "unclassified",
            "depthBand_m": "168-412",
            "nSamples": 47,
            "observedMeanDensity_kg_m2": 0.14779681
          },
          {
            "scientificName": "Lophius piscatorius",
            "density_kg_m2": 14.08,
            "habitat": "unclassified",
            "depthBand_m": "272-308",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 14.08
          },
          {
            "scientificName": "Amblyraja hyperborea",
            "density_kg_m2": 9.16,
            "habitat": "unclassified",
            "depthBand_m": "734-1859",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 9.16
          },
          {
            "scientificName": "Macandrevia cranium",
            "density_kg_m2": 6.96685457,
            "habitat": "unclassified",
            "depthBand_m": "91-1598",
            "nSamples": 363,
            "observedMeanDensity_kg_m2": 9.43791785
          },
          {
            "scientificName": "Spatangus purpureus",
            "density_kg_m2": 5.20866008,
            "habitat": "unclassified",
            "depthBand_m": "105-432",
            "nSamples": 21,
            "observedMeanDensity_kg_m2": 2.3918418
          },
          {
            "scientificName": "Lycodes esmarkii",
            "density_kg_m2": 5.10934492,
            "habitat": "unclassified",
            "depthBand_m": "252-814",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 5.10175
          },
          {
            "scientificName": "Amblyraja radiata",
            "density_kg_m2": 4.14758019,
            "habitat": "unclassified",
            "depthBand_m": "45-569",
            "nSamples": 17,
            "observedMeanDensity_kg_m2": 4.13
          },
          {
            "scientificName": "Leptoclinides faeroensis",
            "density_kg_m2": 4.09242115,
            "habitat": "unclassified",
            "depthBand_m": "147-765",
            "nSamples": 17,
            "observedMeanDensity_kg_m2": 0.01241667
          },
          {
            "scientificName": "Tunicata",
            "density_kg_m2": 4.01442644,
            "habitat": "unclassified",
            "depthBand_m": "156-900",
            "nSamples": 27,
            "observedMeanDensity_kg_m2": 0.09495126
          },
          {
            "scientificName": "Urasterias lincki",
            "density_kg_m2": 3.38123,
            "habitat": "unclassified",
            "depthBand_m": "93-458",
            "nSamples": 26,
            "observedMeanDensity_kg_m2": 3.38123
          },
          {
            "scientificName": "Kophobelemnon stelliferum",
            "density_kg_m2": 2.27578482,
            "habitat": "unclassified",
            "depthBand_m": "172-775",
            "nSamples": 72,
            "observedMeanDensity_kg_m2": 0.50907983
          },
          {
            "scientificName": "Acanthochitona fascicularis",
            "density_kg_m2": 2.26,
            "habitat": "unclassified",
            "depthBand_m": "241-241",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 2.26
          },
          {
            "scientificName": "Tethya citrina",
            "density_kg_m2": 1.78787879,
            "habitat": "unclassified",
            "depthBand_m": "95-610",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 1.78787879
          },
          {
            "scientificName": "Thyasira sarsii",
            "density_kg_m2": 1.35288628,
            "habitat": "unclassified",
            "depthBand_m": "58-854",
            "nSamples": 21,
            "observedMeanDensity_kg_m2": 1.25146154
          },
          {
            "scientificName": "Anthozoa",
            "density_kg_m2": 1.18274286,
            "habitat": "unclassified",
            "depthBand_m": "48-2535",
            "nSamples": 184,
            "observedMeanDensity_kg_m2": 2.12369074
          },
          {
            "scientificName": "Lipobranchius jeffreysii",
            "density_kg_m2": 1.15259556,
            "habitat": "unclassified",
            "depthBand_m": "100-413",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.02358267
          },
          {
            "scientificName": "Anarhichas lupus",
            "density_kg_m2": 1.11,
            "habitat": "unclassified",
            "depthBand_m": "199-234",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 1.11
          },
          {
            "scientificName": "Margarites groenlandicus",
            "density_kg_m2": 1.02290148,
            "habitat": "unclassified",
            "depthBand_m": "58-449",
            "nSamples": 31,
            "observedMeanDensity_kg_m2": 0.93866667
          },
          {
            "scientificName": "Lycodes squamiventer",
            "density_kg_m2": 1.02053081,
            "habitat": "unclassified",
            "depthBand_m": "641-1859",
            "nSamples": 16,
            "observedMeanDensity_kg_m2": 1.09949091
          },
          {
            "scientificName": "Abra longicallus",
            "density_kg_m2": 0.83725143,
            "habitat": "unclassified",
            "depthBand_m": "140-687",
            "nSamples": 435,
            "observedMeanDensity_kg_m2": 0.04974464
          },
          {
            "scientificName": "Actiniaria",
            "density_kg_m2": 0.83569994,
            "habitat": "unclassified",
            "depthBand_m": "42-2746",
            "nSamples": 476,
            "observedMeanDensity_kg_m2": 0.59617652
          },
          {
            "scientificName": "Zoantharia",
            "density_kg_m2": 0.66059785,
            "habitat": "unclassified",
            "depthBand_m": "142-2241",
            "nSamples": 118,
            "observedMeanDensity_kg_m2": 0.09397432
          },
          {
            "scientificName": "Typhlomangelia nivalis",
            "density_kg_m2": 0.65109873,
            "habitat": "unclassified",
            "depthBand_m": "178-562",
            "nSamples": 26,
            "observedMeanDensity_kg_m2": 0.00486142
          },
          {
            "scientificName": "Arctica islandica",
            "density_kg_m2": 0.6365,
            "habitat": "unclassified",
            "depthBand_m": "103-339",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.6365
          },
          {
            "scientificName": "Actinopterygii",
            "density_kg_m2": 0.542986,
            "habitat": "unclassified",
            "depthBand_m": "232-232",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.542986
          },
          {
            "scientificName": "Metavermilia arctica",
            "density_kg_m2": 0.54,
            "habitat": "unclassified",
            "depthBand_m": "241-608",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.54
          },
          {
            "scientificName": "Yoldiella philippiana",
            "density_kg_m2": 0.50303439,
            "habitat": "unclassified",
            "depthBand_m": "140-1591",
            "nSamples": 87,
            "observedMeanDensity_kg_m2": 0.01088026
          },
          {
            "scientificName": "Lycodes frigidus",
            "density_kg_m2": 0.497549,
            "habitat": "unclassified",
            "depthBand_m": "810-2908",
            "nSamples": 19,
            "observedMeanDensity_kg_m2": 0.495
          },
          {
            "scientificName": "Leptochiton asellus",
            "density_kg_m2": 0.47146936,
            "habitat": "unclassified",
            "depthBand_m": "158-479",
            "nSamples": 18,
            "observedMeanDensity_kg_m2": 0.00158092
          },
          {
            "scientificName": "Laetmonice producta",
            "density_kg_m2": 0.44360065,
            "habitat": "unclassified",
            "depthBand_m": "160-765",
            "nSamples": 14,
            "observedMeanDensity_kg_m2": 0.47024604
          },
          {
            "scientificName": "Laonice norgensis",
            "density_kg_m2": 0.37404602,
            "habitat": "unclassified",
            "depthBand_m": "153-1999",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.24461538
          },
          {
            "scientificName": "Volutopsius norwegicus",
            "density_kg_m2": 0.33152646,
            "habitat": "unclassified",
            "depthBand_m": "128-755",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.32535072
          },
          {
            "scientificName": "Anarhichas minor",
            "density_kg_m2": 0.32603025,
            "habitat": "unclassified",
            "depthBand_m": "187-262",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.325965
          },
          {
            "scientificName": "Typhlonereis gracilis",
            "density_kg_m2": 0.31457584,
            "habitat": "unclassified",
            "depthBand_m": "768-1072",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.29011765
          },
          {
            "scientificName": "Lumbrineridae",
            "density_kg_m2": 0.29347981,
            "habitat": "unclassified",
            "depthBand_m": "42-2221",
            "nSamples": 141,
            "observedMeanDensity_kg_m2": 0.00752765
          },
          {
            "scientificName": "Antalis entalis",
            "density_kg_m2": 0.2849181,
            "habitat": "unclassified",
            "depthBand_m": "91-650",
            "nSamples": 164,
            "observedMeanDensity_kg_m2": 0.00916108
          },
          {
            "scientificName": "Lithodes maja",
            "density_kg_m2": 0.28102582,
            "habitat": "unclassified",
            "depthBand_m": "95-355",
            "nSamples": 17,
            "observedMeanDensity_kg_m2": 0.28073
          },
          {
            "scientificName": "Spatangus",
            "density_kg_m2": 0.2570747,
            "habitat": "unclassified",
            "depthBand_m": "124-419",
            "nSamples": 18,
            "observedMeanDensity_kg_m2": 0.25725333
          },
          {
            "scientificName": "Limneria undata",
            "density_kg_m2": 0.25611325,
            "habitat": "unclassified",
            "depthBand_m": "67-875",
            "nSamples": 56,
            "observedMeanDensity_kg_m2": 0.00075924
          },
          {
            "scientificName": "Abra nitida",
            "density_kg_m2": 0.24662104,
            "habitat": "unclassified",
            "depthBand_m": "145-493",
            "nSamples": 94,
            "observedMeanDensity_kg_m2": 0.01167398
          },
          {
            "scientificName": "Mohnia mohni",
            "density_kg_m2": 0.19901538,
            "habitat": "unclassified",
            "depthBand_m": "188-2672",
            "nSamples": 26,
            "observedMeanDensity_kg_m2": 0.20263042
          },
          {
            "scientificName": "Melanogrammus aeglefinus",
            "density_kg_m2": 0.19758,
            "habitat": "unclassified",
            "depthBand_m": "167-268",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.19758
          },
          {
            "scientificName": "Amphictene auricoma",
            "density_kg_m2": 0.19662993,
            "habitat": "unclassified",
            "depthBand_m": "103-493",
            "nSamples": 155,
            "observedMeanDensity_kg_m2": 0.00289875
          },
          {
            "scientificName": "Lumbriclymene",
            "density_kg_m2": 0.1947048,
            "habitat": "unclassified",
            "depthBand_m": "82-736",
            "nSamples": 95,
            "observedMeanDensity_kg_m2": 0.198
          },
          {
            "scientificName": "Admete viridula",
            "density_kg_m2": 0.1903075,
            "habitat": "unclassified",
            "depthBand_m": "68-2048",
            "nSamples": 79,
            "observedMeanDensity_kg_m2": 0.00244561
          },
          {
            "scientificName": "Limopsis angusta",
            "density_kg_m2": 0.1888151,
            "habitat": "unclassified",
            "depthBand_m": "168-636",
            "nSamples": 93,
            "observedMeanDensity_kg_m2": 0.01306575
          },
          {
            "scientificName": "Limatula gwyni",
            "density_kg_m2": 0.17524959,
            "habitat": "unclassified",
            "depthBand_m": "92-1591",
            "nSamples": 86,
            "observedMeanDensity_kg_m2": 0.00349163
          },
          {
            "scientificName": "Laetmonice hystrix",
            "density_kg_m2": 0.1725,
            "habitat": "unclassified",
            "depthBand_m": "281-281",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.1725
          },
          {
            "scientificName": "Acanthicolepis asperrima",
            "density_kg_m2": 0.16560611,
            "habitat": "unclassified",
            "depthBand_m": "63-412",
            "nSamples": 42,
            "observedMeanDensity_kg_m2": 0.00082494
          },
          {
            "scientificName": "Lycodes eudipleurostictus",
            "density_kg_m2": 0.163,
            "habitat": "unclassified",
            "depthBand_m": "328-997",
            "nSamples": 17,
            "observedMeanDensity_kg_m2": 0.163
          },
          {
            "scientificName": "Lasaeidae",
            "density_kg_m2": 0.16,
            "habitat": "unclassified",
            "depthBand_m": "241-241",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.16
          },
          {
            "scientificName": "Anatoma",
            "density_kg_m2": 0.15,
            "habitat": "unclassified",
            "depthBand_m": "230-705",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.15
          },
          {
            "scientificName": "Lumbrineris aniara",
            "density_kg_m2": 0.14804359,
            "habitat": "unclassified",
            "depthBand_m": "178-629",
            "nSamples": 153,
            "observedMeanDensity_kg_m2": 0.08534783
          },
          {
            "scientificName": "Yoldiella propinqua",
            "density_kg_m2": 0.1480185,
            "habitat": "unclassified",
            "depthBand_m": "140-1315",
            "nSamples": 184,
            "observedMeanDensity_kg_m2": 0.00193792
          },
          {
            "scientificName": "Ampelisca odontoplax",
            "density_kg_m2": 0.14788454,
            "habitat": "unclassified",
            "depthBand_m": "159-729",
            "nSamples": 32,
            "observedMeanDensity_kg_m2": 0.00257232
          },
          {
            "scientificName": "Turbellaria",
            "density_kg_m2": 0.1377483,
            "habitat": "unclassified",
            "depthBand_m": "101-1581",
            "nSamples": 27,
            "observedMeanDensity_kg_m2": 0.0085004
          },
          {
            "scientificName": "Aglaophamus malmgreni",
            "density_kg_m2": 0.13647198,
            "habitat": "unclassified",
            "depthBand_m": "68-1409",
            "nSamples": 255,
            "observedMeanDensity_kg_m2": 0.00640697
          },
          {
            "scientificName": "Virgularia mirabilis",
            "density_kg_m2": 0.13598664,
            "habitat": "unclassified",
            "depthBand_m": "130-855",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.00185516
          },
          {
            "scientificName": "Malmgrenia mcintoshi",
            "density_kg_m2": 0.13452074,
            "habitat": "unclassified",
            "depthBand_m": "91-548",
            "nSamples": 16,
            "observedMeanDensity_kg_m2": 0.00050336
          },
          {
            "scientificName": "Solaster endeca",
            "density_kg_m2": 0.12986293,
            "habitat": "unclassified",
            "depthBand_m": "75-503",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.14073333
          },
          {
            "scientificName": "Hymenaster pellucidus",
            "density_kg_m2": 0.12797029,
            "habitat": "unclassified",
            "depthBand_m": "124-2597",
            "nSamples": 50,
            "observedMeanDensity_kg_m2": 0.14515477
          },
          {
            "scientificName": "Lumbriclymene minor",
            "density_kg_m2": 0.1276076,
            "habitat": "unclassified",
            "depthBand_m": "128-629",
            "nSamples": 89,
            "observedMeanDensity_kg_m2": 0.00425802
          },
          {
            "scientificName": "Yoldiella nana",
            "density_kg_m2": 0.12707133,
            "habitat": "unclassified",
            "depthBand_m": "42-2000",
            "nSamples": 611,
            "observedMeanDensity_kg_m2": 0.13063571
          },
          {
            "scientificName": "Antalis occidentalis",
            "density_kg_m2": 0.12562503,
            "habitat": "unclassified",
            "depthBand_m": "91-687",
            "nSamples": 421,
            "observedMeanDensity_kg_m2": 0.00410464
          },
          {
            "scientificName": "Anomioidea",
            "density_kg_m2": 0.12265962,
            "habitat": "unclassified",
            "depthBand_m": "202-479",
            "nSamples": 15,
            "observedMeanDensity_kg_m2": 0.1024
          },
          {
            "scientificName": "Antalis",
            "density_kg_m2": 0.11885475,
            "habitat": "unclassified",
            "depthBand_m": "214-547",
            "nSamples": 18,
            "observedMeanDensity_kg_m2": 0.11875
          },
          {
            "scientificName": "Ampelisca diadema",
            "density_kg_m2": 0.11801297,
            "habitat": "unclassified",
            "depthBand_m": "168-367",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.00053818
          },
          {
            "scientificName": "Abra prismatica",
            "density_kg_m2": 0.1164666,
            "habitat": "unclassified",
            "depthBand_m": "92-362",
            "nSamples": 17,
            "observedMeanDensity_kg_m2": 0.10881818
          },
          {
            "scientificName": "Laonice sarsi",
            "density_kg_m2": 0.11579036,
            "habitat": "unclassified",
            "depthBand_m": "118-1966",
            "nSamples": 229,
            "observedMeanDensity_kg_m2": 0.00177215
          },
          {
            "scientificName": "Thyasira gouldii",
            "density_kg_m2": 0.1144877,
            "habitat": "unclassified",
            "depthBand_m": "58-1037",
            "nSamples": 29,
            "observedMeanDensity_kg_m2": 0.1147
          },
          {
            "scientificName": "Asterias rubens",
            "density_kg_m2": 0.1123949,
            "habitat": "unclassified",
            "depthBand_m": "50-290",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.11081333
          },
          {
            "scientificName": "Thyasira succisa",
            "density_kg_m2": 0.11147183,
            "habitat": "unclassified",
            "depthBand_m": "172-446",
            "nSamples": 32,
            "observedMeanDensity_kg_m2": 0.12133333
          },
          {
            "scientificName": "Lycodes paamiuti",
            "density_kg_m2": 0.11054798,
            "habitat": "unclassified",
            "depthBand_m": "997-1221",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.11
          },
          {
            "scientificName": "Malacoceros",
            "density_kg_m2": 0.10250476,
            "habitat": "unclassified",
            "depthBand_m": "187-228",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0992
          },
          {
            "scientificName": "Yoldiella lucida",
            "density_kg_m2": 0.09801362,
            "habitat": "unclassified",
            "depthBand_m": "119-1935",
            "nSamples": 450,
            "observedMeanDensity_kg_m2": 0.0088625
          },
          {
            "scientificName": "Amphiura otteri",
            "density_kg_m2": 0.09574208,
            "habitat": "unclassified",
            "depthBand_m": "237-765",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 0.00222228
          },
          {
            "scientificName": "Lysilla loveni",
            "density_kg_m2": 0.09462131,
            "habitat": "unclassified",
            "depthBand_m": "82-778",
            "nSamples": 24,
            "observedMeanDensity_kg_m2": 0.08826667
          },
          {
            "scientificName": "Antho (Antho) dichotoma",
            "density_kg_m2": 0.09072837,
            "habitat": "unclassified",
            "depthBand_m": "139-730",
            "nSamples": 26,
            "observedMeanDensity_kg_m2": 0.09
          },
          {
            "scientificName": "Kellia suborbicularis",
            "density_kg_m2": 0.09,
            "habitat": "unclassified",
            "depthBand_m": "241-241",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.09
          },
          {
            "scientificName": "Acanthotrochus mirabilis",
            "density_kg_m2": 0.08938029,
            "habitat": "unclassified",
            "depthBand_m": "198-2714",
            "nSamples": 44,
            "observedMeanDensity_kg_m2": 0.00586143
          },
          {
            "scientificName": "Turrisipho moebii",
            "density_kg_m2": 0.08785849,
            "habitat": "unclassified",
            "depthBand_m": "207-2241",
            "nSamples": 20,
            "observedMeanDensity_kg_m2": 0.0880686
          },
          {
            "scientificName": "Lycodes pallidus",
            "density_kg_m2": 0.08416038,
            "habitat": "unclassified",
            "depthBand_m": "124-1330",
            "nSamples": 19,
            "observedMeanDensity_kg_m2": 0.08958769
          },
          {
            "scientificName": "Lycodonus flagellicauda",
            "density_kg_m2": 0.07960703,
            "habitat": "unclassified",
            "depthBand_m": "658-1532",
            "nSamples": 18,
            "observedMeanDensity_kg_m2": 0.08256667
          },
          {
            "scientificName": "Lumbriclymene cylindricauda",
            "density_kg_m2": 0.07927132,
            "habitat": "unclassified",
            "depthBand_m": "124-1072",
            "nSamples": 192,
            "observedMeanDensity_kg_m2": 0.00323861
          },
          {
            "scientificName": "Virgularia",
            "density_kg_m2": 0.07,
            "habitat": "unclassified",
            "depthBand_m": "604-1314",
            "nSamples": 19,
            "observedMeanDensity_kg_m2": 0.07
          },
          {
            "scientificName": "Limatula",
            "density_kg_m2": 0.06977147,
            "habitat": "unclassified",
            "depthBand_m": "78-283",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 0.07
          },
          {
            "scientificName": "Melinna cristata",
            "density_kg_m2": 0.06972489,
            "habitat": "unclassified",
            "depthBand_m": "82-500",
            "nSamples": 116,
            "observedMeanDensity_kg_m2": 0.00068939
          },
          {
            "scientificName": "Artediellus atlanticus",
            "density_kg_m2": 0.06883333,
            "habitat": "unclassified",
            "depthBand_m": "105-458",
            "nSamples": 59,
            "observedMeanDensity_kg_m2": 0.07005421
          },
          {
            "scientificName": "Abyssoninoe scopa",
            "density_kg_m2": 0.06522369,
            "habitat": "unclassified",
            "depthBand_m": "90-1292",
            "nSamples": 305,
            "observedMeanDensity_kg_m2": 0.00485925
          },
          {
            "scientificName": "Leitoscoloplos acutus",
            "density_kg_m2": 0.06515098,
            "habitat": "unclassified",
            "depthBand_m": "249-854",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.05618182
          },
          {
            "scientificName": "Ampelisca macrocephala",
            "density_kg_m2": 0.06283671,
            "habitat": "unclassified",
            "depthBand_m": "91-875",
            "nSamples": 89,
            "observedMeanDensity_kg_m2": 0.00116855
          },
          {
            "scientificName": "Leptychaster arcticus",
            "density_kg_m2": 0.06270622,
            "habitat": "unclassified",
            "depthBand_m": "118-503",
            "nSamples": 56,
            "observedMeanDensity_kg_m2": 0.06480154
          },
          {
            "scientificName": "Amphilepis norvegica",
            "density_kg_m2": 0.06131319,
            "habitat": "unclassified",
            "depthBand_m": "169-490",
            "nSamples": 183,
            "observedMeanDensity_kg_m2": 0.00069721
          },
          {
            "scientificName": "Amathillopsis spinigera",
            "density_kg_m2": 0.06026569,
            "habitat": "unclassified",
            "depthBand_m": "722-1859",
            "nSamples": 43,
            "observedMeanDensity_kg_m2": 0.061336
          },
          {
            "scientificName": "Sphaerodoridae",
            "density_kg_m2": 0.06001681,
            "habitat": "unclassified",
            "depthBand_m": "67-1591",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.06
          },
          {
            "scientificName": "Amphiura filiformis",
            "density_kg_m2": 0.05885298,
            "habitat": "unclassified",
            "depthBand_m": "134-765",
            "nSamples": 22,
            "observedMeanDensity_kg_m2": 0.00143117
          },
          {
            "scientificName": "Maldane arctica",
            "density_kg_m2": 0.05563303,
            "habitat": "unclassified",
            "depthBand_m": "87-1408",
            "nSamples": 233,
            "observedMeanDensity_kg_m2": 0.0005318
          },
          {
            "scientificName": "Kelliola symmetros",
            "density_kg_m2": 0.05481747,
            "habitat": "unclassified",
            "depthBand_m": "663-1591",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.00025749
          },
          {
            "scientificName": "Melinna albicincta",
            "density_kg_m2": 0.05468458,
            "habitat": "unclassified",
            "depthBand_m": "183-431",
            "nSamples": 45,
            "observedMeanDensity_kg_m2": 0.05333333
          },
          {
            "scientificName": "Leptochiton",
            "density_kg_m2": 0.05139382,
            "habitat": "unclassified",
            "depthBand_m": "215-640",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.00556288
          },
          {
            "scientificName": "Alvania cimicoides",
            "density_kg_m2": 0.04993987,
            "habitat": "unclassified",
            "depthBand_m": "212-392",
            "nSamples": 15,
            "observedMeanDensity_kg_m2": 0.04
          },
          {
            "scientificName": "Amaeana trilobata",
            "density_kg_m2": 0.04923131,
            "habitat": "unclassified",
            "depthBand_m": "128-767",
            "nSamples": 121,
            "observedMeanDensity_kg_m2": 0.00151478
          },
          {
            "scientificName": "Luidia sarsii",
            "density_kg_m2": 0.04867947,
            "habitat": "unclassified",
            "depthBand_m": "50-493",
            "nSamples": 74,
            "observedMeanDensity_kg_m2": 0.01169479
          },
          {
            "scientificName": "Turrisipho voeringi",
            "density_kg_m2": 0.04849503,
            "habitat": "unclassified",
            "depthBand_m": "314-1034",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.048614
          },
          {
            "scientificName": "Melanella monterosatoi",
            "density_kg_m2": 0.04709732,
            "habitat": "unclassified",
            "depthBand_m": "201-478",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.03714286
          },
          {
            "scientificName": "Amphicteis gunneri",
            "density_kg_m2": 0.04700574,
            "habitat": "unclassified",
            "depthBand_m": "68-2241",
            "nSamples": 251,
            "observedMeanDensity_kg_m2": 0.0009483
          },
          {
            "scientificName": "Labidoplax",
            "density_kg_m2": 0.04678331,
            "habitat": "unclassified",
            "depthBand_m": "193-636",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.04666667
          },
          {
            "scientificName": "Anonyx nugax",
            "density_kg_m2": 0.04538642,
            "habitat": "unclassified",
            "depthBand_m": "43-1899",
            "nSamples": 68,
            "observedMeanDensity_kg_m2": 0.03913871
          },
          {
            "scientificName": "Amphiura",
            "density_kg_m2": 0.04484703,
            "habitat": "unclassified",
            "depthBand_m": "124-780",
            "nSamples": 68,
            "observedMeanDensity_kg_m2": 0.00125031
          },
          {
            "scientificName": "Turrisipho lachesis",
            "density_kg_m2": 0.04212682,
            "habitat": "unclassified",
            "depthBand_m": "208-1114",
            "nSamples": 42,
            "observedMeanDensity_kg_m2": 0.0417155
          },
          {
            "scientificName": "Laonice cirrata",
            "density_kg_m2": 0.03821955,
            "habitat": "unclassified",
            "depthBand_m": "68-1314",
            "nSamples": 179,
            "observedMeanDensity_kg_m2": 0.00051443
          },
          {
            "scientificName": "Melinna elisabethae",
            "density_kg_m2": 0.03767963,
            "habitat": "unclassified",
            "depthBand_m": "68-809",
            "nSamples": 154,
            "observedMeanDensity_kg_m2": 0.00134153
          },
          {
            "scientificName": "Anonyx lilljeborgi",
            "density_kg_m2": 0.03482355,
            "habitat": "unclassified",
            "depthBand_m": "76-737",
            "nSamples": 35,
            "observedMeanDensity_kg_m2": 0.00170611
          },
          {
            "scientificName": "Yoldiella",
            "density_kg_m2": 0.0341753,
            "habitat": "unclassified",
            "depthBand_m": "187-1591",
            "nSamples": 24,
            "observedMeanDensity_kg_m2": 0.00065541
          },
          {
            "scientificName": "Lacydonia",
            "density_kg_m2": 0.03274105,
            "habitat": "unclassified",
            "depthBand_m": "295-637",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.03555556
          },
          {
            "scientificName": "Limea crassa",
            "density_kg_m2": 0.03231958,
            "habitat": "unclassified",
            "depthBand_m": "100-687",
            "nSamples": 104,
            "observedMeanDensity_kg_m2": 0.00069233
          },
          {
            "scientificName": "Asellota",
            "density_kg_m2": 0.03221926,
            "habitat": "unclassified",
            "depthBand_m": "100-1309",
            "nSamples": 20,
            "observedMeanDensity_kg_m2": 0.00043259
          },
          {
            "scientificName": "Lycodes gracilis",
            "density_kg_m2": 0.03207625,
            "habitat": "unclassified",
            "depthBand_m": "227-486",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.0325
          },
          {
            "scientificName": "Alvania",
            "density_kg_m2": 0.0312,
            "habitat": "unclassified",
            "depthBand_m": "100-2221",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0312
          },
          {
            "scientificName": "Laphania boecki",
            "density_kg_m2": 0.0311916,
            "habitat": "unclassified",
            "depthBand_m": "47-750",
            "nSamples": 95,
            "observedMeanDensity_kg_m2": 0.0375
          },
          {
            "scientificName": "Aonides paucibranchiata",
            "density_kg_m2": 0.02915214,
            "habitat": "unclassified",
            "depthBand_m": "58-362",
            "nSamples": 71,
            "observedMeanDensity_kg_m2": 0.02155251
          },
          {
            "scientificName": "Aglaophamus pulcher",
            "density_kg_m2": 0.02910457,
            "habitat": "unclassified",
            "depthBand_m": "157-808",
            "nSamples": 41,
            "observedMeanDensity_kg_m2": 0.00012581
          },
          {
            "scientificName": "Leucon (Leucon) nathorsti",
            "density_kg_m2": 0.02867644,
            "habitat": "unclassified",
            "depthBand_m": "124-836",
            "nSamples": 167,
            "observedMeanDensity_kg_m2": 0.0200688
          },
          {
            "scientificName": "Anatoma crispata",
            "density_kg_m2": 0.028,
            "habitat": "unclassified",
            "depthBand_m": "63-689",
            "nSamples": 35,
            "observedMeanDensity_kg_m2": 0.028
          },
          {
            "scientificName": "Apomatus globifer",
            "density_kg_m2": 0.02722194,
            "habitat": "unclassified",
            "depthBand_m": "100-1018",
            "nSamples": 19,
            "observedMeanDensity_kg_m2": 0.0034521
          },
          {
            "scientificName": "Malacoceros jirkovi",
            "density_kg_m2": 0.02704552,
            "habitat": "unclassified",
            "depthBand_m": "92-362",
            "nSamples": 39,
            "observedMeanDensity_kg_m2": 0.01272059
          },
          {
            "scientificName": "Lumpenus lampretaeformis",
            "density_kg_m2": 0.02675,
            "habitat": "unclassified",
            "depthBand_m": "77-283",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.02675
          },
          {
            "scientificName": "Maldanidae",
            "density_kg_m2": 0.02665835,
            "habitat": "unclassified",
            "depthBand_m": "82-2009",
            "nSamples": 323,
            "observedMeanDensity_kg_m2": 0.00276652
          },
          {
            "scientificName": "Lysianassidae",
            "density_kg_m2": 0.02648691,
            "habitat": "unclassified",
            "depthBand_m": "50-2189",
            "nSamples": 295,
            "observedMeanDensity_kg_m2": 0.00459948
          },
          {
            "scientificName": "Amphipholis squamata",
            "density_kg_m2": 0.02612387,
            "habitat": "unclassified",
            "depthBand_m": "68-1221",
            "nSamples": 307,
            "observedMeanDensity_kg_m2": 0.00080819
          },
          {
            "scientificName": "Sphaerodorum",
            "density_kg_m2": 0.02597073,
            "habitat": "unclassified",
            "depthBand_m": "124-900",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.026
          },
          {
            "scientificName": "Metopa boeckii",
            "density_kg_m2": 0.02588968,
            "habitat": "unclassified",
            "depthBand_m": "253-429",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.00027861
          },
          {
            "scientificName": "Aphelochaeta marioni",
            "density_kg_m2": 0.02566778,
            "habitat": "unclassified",
            "depthBand_m": "239-300",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.026
          },
          {
            "scientificName": "Lycodes",
            "density_kg_m2": 0.02541761,
            "habitat": "unclassified",
            "depthBand_m": "178-2049",
            "nSamples": 19,
            "observedMeanDensity_kg_m2": 0.02546
          },
          {
            "scientificName": "Aplacophora",
            "density_kg_m2": 0.025,
            "habitat": "unclassified",
            "depthBand_m": "67-2354",
            "nSamples": 67,
            "observedMeanDensity_kg_m2": 0.025
          },
          {
            "scientificName": "Malacoceros fuliginosus",
            "density_kg_m2": 0.025,
            "habitat": "unclassified",
            "depthBand_m": "86-221",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.025
          },
          {
            "scientificName": "Aricidea nolani",
            "density_kg_m2": 0.024,
            "habitat": "unclassified",
            "depthBand_m": "297-386",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.024
          },
          {
            "scientificName": "Amage auricula",
            "density_kg_m2": 0.02350977,
            "habitat": "unclassified",
            "depthBand_m": "91-1678",
            "nSamples": 453,
            "observedMeanDensity_kg_m2": 0.00188305
          },
          {
            "scientificName": "Lyonsiella abyssicola",
            "density_kg_m2": 0.02306205,
            "habitat": "unclassified",
            "depthBand_m": "158-1232",
            "nSamples": 181,
            "observedMeanDensity_kg_m2": 0.00365938
          },
          {
            "scientificName": "Ampharete finmarchica",
            "density_kg_m2": 0.02241351,
            "habitat": "unclassified",
            "depthBand_m": "67-2009",
            "nSamples": 103,
            "observedMeanDensity_kg_m2": 0.00062771
          },
          {
            "scientificName": "Themisto abyssorum",
            "density_kg_m2": 0.02220358,
            "habitat": "unclassified",
            "depthBand_m": "124-2009",
            "nSamples": 40,
            "observedMeanDensity_kg_m2": 0.00954749
          },
          {
            "scientificName": "Laonice blakei",
            "density_kg_m2": 0.02202586,
            "habitat": "unclassified",
            "depthBand_m": "729-2354",
            "nSamples": 16,
            "observedMeanDensity_kg_m2": 0.00060515
          },
          {
            "scientificName": "Leptychaster",
            "density_kg_m2": 0.0214,
            "habitat": "unclassified",
            "depthBand_m": "321-321",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0214
          },
          {
            "scientificName": "Tryphosites longipes",
            "density_kg_m2": 0.02099812,
            "habitat": "unclassified",
            "depthBand_m": "50-900",
            "nSamples": 92,
            "observedMeanDensity_kg_m2": 0.00066675
          },
          {
            "scientificName": "Aricidea",
            "density_kg_m2": 0.02083247,
            "habitat": "unclassified",
            "depthBand_m": "58-1878",
            "nSamples": 115,
            "observedMeanDensity_kg_m2": 0.00227543
          },
          {
            "scientificName": "Asclerocheilus intermedius",
            "density_kg_m2": 0.0207906,
            "habitat": "unclassified",
            "depthBand_m": "100-1072",
            "nSamples": 26,
            "observedMeanDensity_kg_m2": 0.00044668
          },
          {
            "scientificName": "Spatangidae",
            "density_kg_m2": 0.02,
            "habitat": "unclassified",
            "depthBand_m": "142-298",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.02
          },
          {
            "scientificName": "Thracia",
            "density_kg_m2": 0.02,
            "habitat": "unclassified",
            "depthBand_m": "230-402",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.02
          },
          {
            "scientificName": "Aegiochus ventrosa",
            "density_kg_m2": 0.01967735,
            "habitat": "unclassified",
            "depthBand_m": "204-553",
            "nSamples": 22,
            "observedMeanDensity_kg_m2": 0.020475
          },
          {
            "scientificName": "Arcturidae",
            "density_kg_m2": 0.01940691,
            "habitat": "unclassified",
            "depthBand_m": "155-875",
            "nSamples": 18,
            "observedMeanDensity_kg_m2": 7.685e-05
          },
          {
            "scientificName": "Anonyx",
            "density_kg_m2": 0.01934451,
            "habitat": "unclassified",
            "depthBand_m": "44-1803",
            "nSamples": 23,
            "observedMeanDensity_kg_m2": 0.019359
          },
          {
            "scientificName": "Ampelisca",
            "density_kg_m2": 0.01887355,
            "habitat": "unclassified",
            "depthBand_m": "56-1022",
            "nSamples": 399,
            "observedMeanDensity_kg_m2": 0.00032265
          },
          {
            "scientificName": "Lebbeus polaris",
            "density_kg_m2": 0.01851917,
            "habitat": "unclassified",
            "depthBand_m": "43-1229",
            "nSamples": 155,
            "observedMeanDensity_kg_m2": 0.02155659
          },
          {
            "scientificName": "Lycenchelys muraena",
            "density_kg_m2": 0.01835283,
            "habitat": "unclassified",
            "depthBand_m": "266-2048",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.01895429
          },
          {
            "scientificName": "Laonome kroyeri",
            "density_kg_m2": 0.01804838,
            "habitat": "unclassified",
            "depthBand_m": "118-689",
            "nSamples": 25,
            "observedMeanDensity_kg_m2": 8.047e-05
          },
          {
            "scientificName": "Uschakovia gorbunovi",
            "density_kg_m2": 0.01772244,
            "habitat": "unclassified",
            "depthBand_m": "239-284",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.018
          },
          {
            "scientificName": "Ampelisca tenuicornis",
            "density_kg_m2": 0.01756601,
            "habitat": "unclassified",
            "depthBand_m": "165-324",
            "nSamples": 16,
            "observedMeanDensity_kg_m2": 0.00010995
          },
          {
            "scientificName": "Sosane sulcata",
            "density_kg_m2": 0.0172242,
            "habitat": "unclassified",
            "depthBand_m": "167-333",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.01538462
          },
          {
            "scientificName": "Leptasterias",
            "density_kg_m2": 0.0170553,
            "habitat": "unclassified",
            "depthBand_m": "75-432",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.01689485
          },
          {
            "scientificName": "Laeocochlis sinistrata",
            "density_kg_m2": 0.01703357,
            "habitat": "unclassified",
            "depthBand_m": "168-626",
            "nSamples": 26,
            "observedMeanDensity_kg_m2": 0.0174625
          },
          {
            "scientificName": "Laetmonice",
            "density_kg_m2": 0.01702179,
            "habitat": "unclassified",
            "depthBand_m": "135-485",
            "nSamples": 20,
            "observedMeanDensity_kg_m2": 0.01705667
          },
          {
            "scientificName": "Asclerocheilus",
            "density_kg_m2": 0.01650109,
            "habitat": "unclassified",
            "depthBand_m": "68-768",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.01644444
          },
          {
            "scientificName": "Anapagurus laevis",
            "density_kg_m2": 0.01610604,
            "habitat": "unclassified",
            "depthBand_m": "78-384",
            "nSamples": 34,
            "observedMeanDensity_kg_m2": 0.01692086
          },
          {
            "scientificName": "Aricidea (Acmira) laubieri",
            "density_kg_m2": 0.015,
            "habitat": "unclassified",
            "depthBand_m": "351-370",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.015
          },
          {
            "scientificName": "Ampelisca aequicornis",
            "density_kg_m2": 0.0146839,
            "habitat": "unclassified",
            "depthBand_m": "156-425",
            "nSamples": 66,
            "observedMeanDensity_kg_m2": 0.00031486
          },
          {
            "scientificName": "Amythasides macroglossus",
            "density_kg_m2": 0.01440017,
            "habitat": "unclassified",
            "depthBand_m": "68-993",
            "nSamples": 431,
            "observedMeanDensity_kg_m2": 0.00044259
          },
          {
            "scientificName": "Munida rugosa",
            "density_kg_m2": 0.0142885,
            "habitat": "unclassified",
            "depthBand_m": "307-357",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.014348
          },
          {
            "scientificName": "Mesogastropoda",
            "density_kg_m2": 0.01397208,
            "habitat": "unclassified",
            "depthBand_m": "1878-1937",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.014
          },
          {
            "scientificName": "Liomesus",
            "density_kg_m2": 0.01388,
            "habitat": "unclassified",
            "depthBand_m": "211-211",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.01388
          },
          {
            "scientificName": "Turrisipho fenestratus",
            "density_kg_m2": 0.01371599,
            "habitat": "unclassified",
            "depthBand_m": "187-636",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 0.0139675
          },
          {
            "scientificName": "Microclymene tricirrata",
            "density_kg_m2": 0.01355755,
            "habitat": "unclassified",
            "depthBand_m": "172-377",
            "nSamples": 14,
            "observedMeanDensity_kg_m2": 0.01227273
          },
          {
            "scientificName": "Liomesus ovum",
            "density_kg_m2": 0.01344,
            "habitat": "unclassified",
            "depthBand_m": "233-390",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.01344
          },
          {
            "scientificName": "Lycenchelys sarsii",
            "density_kg_m2": 0.01317691,
            "habitat": "unclassified",
            "depthBand_m": "177-486",
            "nSamples": 19,
            "observedMeanDensity_kg_m2": 0.01318
          },
          {
            "scientificName": "Aphrodita aculeata",
            "density_kg_m2": 0.01306807,
            "habitat": "unclassified",
            "depthBand_m": "157-503",
            "nSamples": 36,
            "observedMeanDensity_kg_m2": 0.01286012
          },
          {
            "scientificName": "Lumbrineris",
            "density_kg_m2": 0.01299899,
            "habitat": "unclassified",
            "depthBand_m": "60-1113",
            "nSamples": 110,
            "observedMeanDensity_kg_m2": 0.01482222
          },
          {
            "scientificName": "Korethraster hispidus",
            "density_kg_m2": 0.01257072,
            "habitat": "unclassified",
            "depthBand_m": "218-1532",
            "nSamples": 22,
            "observedMeanDensity_kg_m2": 0.01301182
          },
          {
            "scientificName": "Ilyarachninae",
            "density_kg_m2": 0.0125,
            "habitat": "unclassified",
            "depthBand_m": "172-295",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0125
          },
          {
            "scientificName": "Limatula subauriculata",
            "density_kg_m2": 0.012,
            "habitat": "unclassified",
            "depthBand_m": "100-363",
            "nSamples": 13,
            "observedMeanDensity_kg_m2": 0.012
          },
          {
            "scientificName": "Yoldiella annenkovae",
            "density_kg_m2": 0.012,
            "habitat": "unclassified",
            "depthBand_m": "306-2167",
            "nSamples": 20,
            "observedMeanDensity_kg_m2": 0.012
          },
          {
            "scientificName": "Icelus bicornis",
            "density_kg_m2": 0.01181947,
            "habitat": "unclassified",
            "depthBand_m": "105-295",
            "nSamples": 21,
            "observedMeanDensity_kg_m2": 0.01255076
          },
          {
            "scientificName": "Leaena ebranchiata",
            "density_kg_m2": 0.01106142,
            "habitat": "unclassified",
            "depthBand_m": "82-936",
            "nSamples": 80,
            "observedMeanDensity_kg_m2": 0.00030743
          },
          {
            "scientificName": "Lycenchelys",
            "density_kg_m2": 0.01082371,
            "habitat": "unclassified",
            "depthBand_m": "211-380",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.01075
          },
          {
            "scientificName": "Apseudes spinosus",
            "density_kg_m2": 0.01067753,
            "habitat": "unclassified",
            "depthBand_m": "165-824",
            "nSamples": 21,
            "observedMeanDensity_kg_m2": 0.00014034
          },
          {
            "scientificName": "Aega psora",
            "density_kg_m2": 0.01063134,
            "habitat": "unclassified",
            "depthBand_m": "177-390",
            "nSamples": 37,
            "observedMeanDensity_kg_m2": 0.01192349
          },
          {
            "scientificName": "Liljeborgia (Lilljeborgiella) fissicornis",
            "density_kg_m2": 0.01003968,
            "habitat": "unclassified",
            "depthBand_m": "87-2744",
            "nSamples": 272,
            "observedMeanDensity_kg_m2": 0.00460589
          },
          {
            "scientificName": "Aricidea (Strelzovia) roberti",
            "density_kg_m2": 0.0100197,
            "habitat": "unclassified",
            "depthBand_m": "221-779",
            "nSamples": 17,
            "observedMeanDensity_kg_m2": 0.01
          },
          {
            "scientificName": "Aphelochaeta filiformis",
            "density_kg_m2": 0.01,
            "habitat": "unclassified",
            "depthBand_m": "229-229",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.01
          },
          {
            "scientificName": "Margarites",
            "density_kg_m2": 0.01,
            "habitat": "unclassified",
            "depthBand_m": "276-2354",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.01
          },
          {
            "scientificName": "Amphilochoides boeckii",
            "density_kg_m2": 0.00993597,
            "habitat": "unclassified",
            "depthBand_m": "118-407",
            "nSamples": 32,
            "observedMeanDensity_kg_m2": 0.01021325
          },
          {
            "scientificName": "Macroclymene",
            "density_kg_m2": 0.00959944,
            "habitat": "unclassified",
            "depthBand_m": "765-1591",
            "nSamples": 17,
            "observedMeanDensity_kg_m2": 0.00970588
          },
          {
            "scientificName": "Lafoea dumosa",
            "density_kg_m2": 0.00950148,
            "habitat": "unclassified",
            "depthBand_m": "118-807",
            "nSamples": 15,
            "observedMeanDensity_kg_m2": 0.0020065
          },
          {
            "scientificName": "Ascorhynchus abyssi",
            "density_kg_m2": 0.00916983,
            "habitat": "unclassified",
            "depthBand_m": "490-2597",
            "nSamples": 13,
            "observedMeanDensity_kg_m2": 0.00539051
          },
          {
            "scientificName": "Margarites costalis",
            "density_kg_m2": 0.0089711,
            "habitat": "unclassified",
            "depthBand_m": "68-560",
            "nSamples": 13,
            "observedMeanDensity_kg_m2": 0.00158005
          },
          {
            "scientificName": "Limacina retroversa",
            "density_kg_m2": 0.00852582,
            "habitat": "unclassified",
            "depthBand_m": "105-1863",
            "nSamples": 32,
            "observedMeanDensity_kg_m2": 0.00828571
          },
          {
            "scientificName": "Microclymene acirrata",
            "density_kg_m2": 0.00829536,
            "habitat": "unclassified",
            "depthBand_m": "82-500",
            "nSamples": 25,
            "observedMeanDensity_kg_m2": 0.00833333
          },
          {
            "scientificName": "Mesothuria intestinalis",
            "density_kg_m2": 0.00802614,
            "habitat": "unclassified",
            "depthBand_m": "91-484",
            "nSamples": 31,
            "observedMeanDensity_kg_m2": 0.007955
          },
          {
            "scientificName": "Kelliopsis jozinae",
            "density_kg_m2": 0.008,
            "habitat": "unclassified",
            "depthBand_m": "2714-2714",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.008
          },
          {
            "scientificName": "Kirchenpaueria pinnata",
            "density_kg_m2": 0.008,
            "habitat": "unclassified",
            "depthBand_m": "119-363",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.008
          },
          {
            "scientificName": "Melinnopsis arctica",
            "density_kg_m2": 0.008,
            "habitat": "unclassified",
            "depthBand_m": "222-867",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.008
          },
          {
            "scientificName": "Anomiidae",
            "density_kg_m2": 0.00756085,
            "habitat": "unclassified",
            "depthBand_m": "205-503",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.00018152
          },
          {
            "scientificName": "Amphiuridae",
            "density_kg_m2": 0.00721969,
            "habitat": "unclassified",
            "depthBand_m": "134-881",
            "nSamples": 23,
            "observedMeanDensity_kg_m2": 0.0067835
          },
          {
            "scientificName": "Aricidea (Acmira) cerrutii",
            "density_kg_m2": 0.00709928,
            "habitat": "unclassified",
            "depthBand_m": "78-913",
            "nSamples": 21,
            "observedMeanDensity_kg_m2": 0.00476667
          },
          {
            "scientificName": "Leptoclinus maculatus",
            "density_kg_m2": 0.00703,
            "habitat": "unclassified",
            "depthBand_m": "68-1229",
            "nSamples": 19,
            "observedMeanDensity_kg_m2": 0.00703
          },
          {
            "scientificName": "Hymenodora glacialis",
            "density_kg_m2": 0.00688918,
            "habitat": "unclassified",
            "depthBand_m": "611-2241",
            "nSamples": 24,
            "observedMeanDensity_kg_m2": 0.00648193
          },
          {
            "scientificName": "Tryphosella spitzbergensis",
            "density_kg_m2": 0.00686097,
            "habitat": "unclassified",
            "depthBand_m": "305-329",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.00682
          },
          {
            "scientificName": "Sphaerodoropsis",
            "density_kg_m2": 0.00668053,
            "habitat": "unclassified",
            "depthBand_m": "198-1305",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 3.968e-05
          },
          {
            "scientificName": "Amphiura borealis",
            "density_kg_m2": 0.00659775,
            "habitat": "unclassified",
            "depthBand_m": "100-707",
            "nSamples": 58,
            "observedMeanDensity_kg_m2": 0.00094881
          },
          {
            "scientificName": "Anobothrus gracilis",
            "density_kg_m2": 0.00655449,
            "habitat": "unclassified",
            "depthBand_m": "58-963",
            "nSamples": 108,
            "observedMeanDensity_kg_m2": 9.158e-05
          },
          {
            "scientificName": "Jasmineira caudata",
            "density_kg_m2": 0.00611306,
            "habitat": "unclassified",
            "depthBand_m": "92-749",
            "nSamples": 65,
            "observedMeanDensity_kg_m2": 0.00348406
          },
          {
            "scientificName": "Metzgeria alba",
            "density_kg_m2": 0.00608,
            "habitat": "unclassified",
            "depthBand_m": "164-435",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.006142
          },
          {
            "scientificName": "Adontorhina similis",
            "density_kg_m2": 0.006,
            "habitat": "unclassified",
            "depthBand_m": "147-1582",
            "nSamples": 73,
            "observedMeanDensity_kg_m2": 0.006
          },
          {
            "scientificName": "Leucothoe spinicarpa",
            "density_kg_m2": 0.005963,
            "habitat": "unclassified",
            "depthBand_m": "169-662",
            "nSamples": 55,
            "observedMeanDensity_kg_m2": 0.00030838
          },
          {
            "scientificName": "Ampharete octocirrata",
            "density_kg_m2": 0.00566202,
            "habitat": "unclassified",
            "depthBand_m": "68-808",
            "nSamples": 294,
            "observedMeanDensity_kg_m2": 7.73e-05
          },
          {
            "scientificName": "Alvania jeffreysi",
            "density_kg_m2": 0.0056,
            "habitat": "unclassified",
            "depthBand_m": "240-485",
            "nSamples": 28,
            "observedMeanDensity_kg_m2": 0.0056
          },
          {
            "scientificName": "Apistobranchus tullbergi",
            "density_kg_m2": 0.00548849,
            "habitat": "unclassified",
            "depthBand_m": "82-808",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.0056
          },
          {
            "scientificName": "Ampelisca gibba",
            "density_kg_m2": 0.00528186,
            "habitat": "unclassified",
            "depthBand_m": "118-397",
            "nSamples": 44,
            "observedMeanDensity_kg_m2": 0.00050692
          },
          {
            "scientificName": "Acidostoma",
            "density_kg_m2": 0.00523445,
            "habitat": "unclassified",
            "depthBand_m": "217-543",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 1.996e-05
          },
          {
            "scientificName": "Jorunna tomentosa",
            "density_kg_m2": 0.00517,
            "habitat": "unclassified",
            "depthBand_m": "164-164",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.00517
          },
          {
            "scientificName": "Macrochaeta",
            "density_kg_m2": 0.00507937,
            "habitat": "unclassified",
            "depthBand_m": "105-1591",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 8.858e-05
          },
          {
            "scientificName": "Ampharete acutifrons",
            "density_kg_m2": 0.005,
            "habitat": "unclassified",
            "depthBand_m": "807-807",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.005
          },
          {
            "scientificName": "Laomedea",
            "density_kg_m2": 0.005,
            "habitat": "unclassified",
            "depthBand_m": "231-231",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.005
          },
          {
            "scientificName": "Lycodes adolfi",
            "density_kg_m2": 0.005,
            "habitat": "unclassified",
            "depthBand_m": "1032-1229",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.005
          },
          {
            "scientificName": "Lophaster furcifer",
            "density_kg_m2": 0.00488971,
            "habitat": "unclassified",
            "depthBand_m": "91-810",
            "nSamples": 21,
            "observedMeanDensity_kg_m2": 0.0038695
          },
          {
            "scientificName": "Mohnia",
            "density_kg_m2": 0.00488,
            "habitat": "unclassified",
            "depthBand_m": "222-2136",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.00488
          },
          {
            "scientificName": "Aeginella spinosa",
            "density_kg_m2": 0.00486264,
            "habitat": "unclassified",
            "depthBand_m": "95-881",
            "nSamples": 24,
            "observedMeanDensity_kg_m2": 0.00026371
          },
          {
            "scientificName": "Zatsepinia rittichae",
            "density_kg_m2": 0.00483483,
            "habitat": "unclassified",
            "depthBand_m": "91-1221",
            "nSamples": 270,
            "observedMeanDensity_kg_m2": 0.00036503
          },
          {
            "scientificName": "Aricidea (Strelzovia) quadrilobata",
            "density_kg_m2": 0.00457349,
            "habitat": "unclassified",
            "depthBand_m": "162-1408",
            "nSamples": 63,
            "observedMeanDensity_kg_m2": 0.00021892
          },
          {
            "scientificName": "Sphaerosyllis",
            "density_kg_m2": 0.00455075,
            "habitat": "unclassified",
            "depthBand_m": "244-621",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.00333333
          },
          {
            "scientificName": "Levinsenia gracilis",
            "density_kg_m2": 0.00444986,
            "habitat": "unclassified",
            "depthBand_m": "68-1966",
            "nSamples": 216,
            "observedMeanDensity_kg_m2": 0.00029823
          },
          {
            "scientificName": "Urothoe",
            "density_kg_m2": 0.0043857,
            "habitat": "unclassified",
            "depthBand_m": "242-705",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0001771
          },
          {
            "scientificName": "Montacuta substriata",
            "density_kg_m2": 0.00437364,
            "habitat": "unclassified",
            "depthBand_m": "105-610",
            "nSamples": 13,
            "observedMeanDensity_kg_m2": 3.744e-05
          },
          {
            "scientificName": "Lepechinella arctica",
            "density_kg_m2": 0.00427685,
            "habitat": "unclassified",
            "depthBand_m": "236-881",
            "nSamples": 37,
            "observedMeanDensity_kg_m2": 0.000503
          },
          {
            "scientificName": "Aricidea hartmani",
            "density_kg_m2": 0.00423933,
            "habitat": "unclassified",
            "depthBand_m": "134-1477",
            "nSamples": 98,
            "observedMeanDensity_kg_m2": 0.0029
          },
          {
            "scientificName": "Lumbrineris cingulata",
            "density_kg_m2": 0.004174,
            "habitat": "unclassified",
            "depthBand_m": "118-1678",
            "nSamples": 49,
            "observedMeanDensity_kg_m2": 0.00010079
          },
          {
            "scientificName": "Ampharetinae",
            "density_kg_m2": 0.00406153,
            "habitat": "unclassified",
            "depthBand_m": "241-1221",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0003192
          },
          {
            "scientificName": "Liparidae",
            "density_kg_m2": 0.00392857,
            "habitat": "unclassified",
            "depthBand_m": "755-755",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.00392857
          },
          {
            "scientificName": "Ampharete lindstroemi",
            "density_kg_m2": 0.00385042,
            "habitat": "unclassified",
            "depthBand_m": "147-1037",
            "nSamples": 56,
            "observedMeanDensity_kg_m2": 0.0002395
          },
          {
            "scientificName": "Zoarcidae",
            "density_kg_m2": 0.00374,
            "habitat": "unclassified",
            "depthBand_m": "247-281",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.00374
          },
          {
            "scientificName": "Lumbrineris mixochaeta",
            "density_kg_m2": 0.00351282,
            "habitat": "unclassified",
            "depthBand_m": "82-1477",
            "nSamples": 209,
            "observedMeanDensity_kg_m2": 0.00206897
          },
          {
            "scientificName": "Ampharete falcata",
            "density_kg_m2": 0.00347128,
            "habitat": "unclassified",
            "depthBand_m": "157-386",
            "nSamples": 20,
            "observedMeanDensity_kg_m2": 3.914e-05
          },
          {
            "scientificName": "Micronephthys minuta",
            "density_kg_m2": 0.00338962,
            "habitat": "unclassified",
            "depthBand_m": "243-379",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.00358621
          },
          {
            "scientificName": "Meganyctiphanes norvegica",
            "density_kg_m2": 0.00338232,
            "habitat": "unclassified",
            "depthBand_m": "112-2020",
            "nSamples": 18,
            "observedMeanDensity_kg_m2": 0.00411651
          },
          {
            "scientificName": "Tharyx killariensis",
            "density_kg_m2": 0.00337501,
            "habitat": "unclassified",
            "depthBand_m": "68-1036",
            "nSamples": 33,
            "observedMeanDensity_kg_m2": 3.009e-05
          },
          {
            "scientificName": "Lysianassa costae",
            "density_kg_m2": 0.00337243,
            "habitat": "unclassified",
            "depthBand_m": "172-420",
            "nSamples": 43,
            "observedMeanDensity_kg_m2": 0.00232579
          },
          {
            "scientificName": "Melitidae",
            "density_kg_m2": 0.00336902,
            "habitat": "unclassified",
            "depthBand_m": "121-1999",
            "nSamples": 28,
            "observedMeanDensity_kg_m2": 3.098e-05
          },
          {
            "scientificName": "Mediomastus fragilis",
            "density_kg_m2": 0.00329459,
            "habitat": "unclassified",
            "depthBand_m": "90-533",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 0.00181818
          },
          {
            "scientificName": "Solaster",
            "density_kg_m2": 0.00327,
            "habitat": "unclassified",
            "depthBand_m": "57-662",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.00327
          },
          {
            "scientificName": "Macrocypria sarsi",
            "density_kg_m2": 0.00320181,
            "habitat": "unclassified",
            "depthBand_m": "173-429",
            "nSamples": 14,
            "observedMeanDensity_kg_m2": 0.00354564
          },
          {
            "scientificName": "Monoculodes packardi",
            "density_kg_m2": 0.0031827,
            "habitat": "unclassified",
            "depthBand_m": "80-2354",
            "nSamples": 28,
            "observedMeanDensity_kg_m2": 0.00372627
          },
          {
            "scientificName": "Unciola",
            "density_kg_m2": 0.00315622,
            "habitat": "unclassified",
            "depthBand_m": "91-1314",
            "nSamples": 59,
            "observedMeanDensity_kg_m2": 0.00021651
          },
          {
            "scientificName": "Actaedrilus polyonyx",
            "density_kg_m2": 0.00298389,
            "habitat": "unclassified",
            "depthBand_m": "181-1335",
            "nSamples": 64,
            "observedMeanDensity_kg_m2": 0.00011555
          },
          {
            "scientificName": "Aglajidae",
            "density_kg_m2": 0.00292272,
            "habitat": "unclassified",
            "depthBand_m": "210-351",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.00133533
          },
          {
            "scientificName": "Asteriidae",
            "density_kg_m2": 0.00291,
            "habitat": "unclassified",
            "depthBand_m": "75-864",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.00291
          },
          {
            "scientificName": "Apomatus similis",
            "density_kg_m2": 0.00281689,
            "habitat": "unclassified",
            "depthBand_m": "202-659",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.00053467
          },
          {
            "scientificName": "Macrocypris minna",
            "density_kg_m2": 0.00280546,
            "habitat": "unclassified",
            "depthBand_m": "168-429",
            "nSamples": 30,
            "observedMeanDensity_kg_m2": 0.0023644
          },
          {
            "scientificName": "Antalis agilis",
            "density_kg_m2": 0.00275,
            "habitat": "unclassified",
            "depthBand_m": "229-231",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.00275
          },
          {
            "scientificName": "Thuiaria",
            "density_kg_m2": 0.00265651,
            "habitat": "unclassified",
            "depthBand_m": "45-1409",
            "nSamples": 13,
            "observedMeanDensity_kg_m2": 0.00032934
          },
          {
            "scientificName": "Tryphosella umbonata",
            "density_kg_m2": 0.00247766,
            "habitat": "unclassified",
            "depthBand_m": "199-707",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.00260371
          },
          {
            "scientificName": "Macrochaeta bansei",
            "density_kg_m2": 0.00237389,
            "habitat": "unclassified",
            "depthBand_m": "204-372",
            "nSamples": 15,
            "observedMeanDensity_kg_m2": 2.611e-05
          },
          {
            "scientificName": "Andaniexis lupus",
            "density_kg_m2": 0.0023106,
            "habitat": "unclassified",
            "depthBand_m": "225-367",
            "nSamples": 15,
            "observedMeanDensity_kg_m2": 0.00236747
          },
          {
            "scientificName": "Lumbriclymeninae",
            "density_kg_m2": 0.00230579,
            "habitat": "unclassified",
            "depthBand_m": "188-1277",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 7.97e-06
          },
          {
            "scientificName": "Aoridae",
            "density_kg_m2": 0.00225506,
            "habitat": "unclassified",
            "depthBand_m": "93-850",
            "nSamples": 135,
            "observedMeanDensity_kg_m2": 0.00080583
          },
          {
            "scientificName": "Ilyarachna dubia",
            "density_kg_m2": 0.00224183,
            "habitat": "unclassified",
            "depthBand_m": "258-2561",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.00181333
          },
          {
            "scientificName": "Ampharetidae",
            "density_kg_m2": 0.00215621,
            "habitat": "unclassified",
            "depthBand_m": "142-1833",
            "nSamples": 74,
            "observedMeanDensity_kg_m2": 0.00086034
          },
          {
            "scientificName": "Ampelisca spinipes",
            "density_kg_m2": 0.0020791,
            "habitat": "unclassified",
            "depthBand_m": "169-314",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 9.912e-05
          },
          {
            "scientificName": "Microstomus kitt",
            "density_kg_m2": 0.002,
            "habitat": "unclassified",
            "depthBand_m": "61-560",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.002
          },
          {
            "scientificName": "Lagis koreni",
            "density_kg_m2": 0.00197877,
            "habitat": "unclassified",
            "depthBand_m": "103-374",
            "nSamples": 13,
            "observedMeanDensity_kg_m2": 0.00121212
          },
          {
            "scientificName": "Lysianassa plumosa",
            "density_kg_m2": 0.00195264,
            "habitat": "unclassified",
            "depthBand_m": "118-369",
            "nSamples": 24,
            "observedMeanDensity_kg_m2": 0.00035805
          },
          {
            "scientificName": "Amphithopsis",
            "density_kg_m2": 0.001944,
            "habitat": "unclassified",
            "depthBand_m": "618-618",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.001944
          },
          {
            "scientificName": "Aphrodita perarmata",
            "density_kg_m2": 0.0018284,
            "habitat": "unclassified",
            "depthBand_m": "170-659",
            "nSamples": 16,
            "observedMeanDensity_kg_m2": 1.045e-05
          },
          {
            "scientificName": "Tharyx",
            "density_kg_m2": 0.00172282,
            "habitat": "unclassified",
            "depthBand_m": "103-1037",
            "nSamples": 33,
            "observedMeanDensity_kg_m2": 5.842e-05
          },
          {
            "scientificName": "Astropecten irregularis",
            "density_kg_m2": 0.00171,
            "habitat": "unclassified",
            "depthBand_m": "50-363",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.00171
          },
          {
            "scientificName": "Aora",
            "density_kg_m2": 0.00168,
            "habitat": "unclassified",
            "depthBand_m": "189-189",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.00168
          },
          {
            "scientificName": "Apherusa",
            "density_kg_m2": 0.00157226,
            "habitat": "unclassified",
            "depthBand_m": "128-1189",
            "nSamples": 15,
            "observedMeanDensity_kg_m2": 0.0012725
          },
          {
            "scientificName": "Admete contabulata",
            "density_kg_m2": 0.00157039,
            "habitat": "unclassified",
            "depthBand_m": "1041-2241",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.001555
          },
          {
            "scientificName": "Micronephthys",
            "density_kg_m2": 0.00154549,
            "habitat": "unclassified",
            "depthBand_m": "204-913",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.00130435
          },
          {
            "scientificName": "Liljeborgia (Liljeborgia) macronyx",
            "density_kg_m2": 0.00146619,
            "habitat": "unclassified",
            "depthBand_m": "147-608",
            "nSamples": 23,
            "observedMeanDensity_kg_m2": 3.964e-05
          },
          {
            "scientificName": "Monoculodes latimanus",
            "density_kg_m2": 0.00144,
            "habitat": "unclassified",
            "depthBand_m": "58-627",
            "nSamples": 18,
            "observedMeanDensity_kg_m2": 0.00144
          },
          {
            "scientificName": "Megamoera",
            "density_kg_m2": 0.00136,
            "habitat": "unclassified",
            "depthBand_m": "286-286",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.00136
          },
          {
            "scientificName": "Thuiaria thuja",
            "density_kg_m2": 0.00134587,
            "habitat": "unclassified",
            "depthBand_m": "112-503",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0013575
          },
          {
            "scientificName": "Antedonidae",
            "density_kg_m2": 0.00129707,
            "habitat": "unclassified",
            "depthBand_m": "77-2049",
            "nSamples": 70,
            "observedMeanDensity_kg_m2": 0.00171
          },
          {
            "scientificName": "Liljeborgia (Liljeborgia) brevicornis",
            "density_kg_m2": 0.00129306,
            "habitat": "unclassified",
            "depthBand_m": "207-380",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0013
          },
          {
            "scientificName": "Aricidea (Aricidea) wassi",
            "density_kg_m2": 0.00121033,
            "habitat": "unclassified",
            "depthBand_m": "172-863",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.00083333
          },
          {
            "scientificName": "Ampharete",
            "density_kg_m2": 0.00119128,
            "habitat": "unclassified",
            "depthBand_m": "165-1833",
            "nSamples": 66,
            "observedMeanDensity_kg_m2": 0.00114558
          },
          {
            "scientificName": "Aora gracilis",
            "density_kg_m2": 0.00116523,
            "habitat": "unclassified",
            "depthBand_m": "220-367",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0012
          },
          {
            "scientificName": "Monoculopsis longicornis",
            "density_kg_m2": 0.00111939,
            "habitat": "unclassified",
            "depthBand_m": "207-660",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0011
          },
          {
            "scientificName": "Amphilochus manudens",
            "density_kg_m2": 0.00107989,
            "habitat": "unclassified",
            "depthBand_m": "67-2189",
            "nSamples": 235,
            "observedMeanDensity_kg_m2": 0.00089199
          },
          {
            "scientificName": "Lycodes rossi",
            "density_kg_m2": 0.001,
            "habitat": "unclassified",
            "depthBand_m": "114-499",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.001
          },
          {
            "scientificName": "Apherusa bispinosa",
            "density_kg_m2": 0.00090895,
            "habitat": "unclassified",
            "depthBand_m": "56-627",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.000912
          },
          {
            "scientificName": "Astropectinidae",
            "density_kg_m2": 0.00090379,
            "habitat": "unclassified",
            "depthBand_m": "264-1024",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.0009025
          },
          {
            "scientificName": "Ampelisca pusilla",
            "density_kg_m2": 0.00087773,
            "habitat": "unclassified",
            "depthBand_m": "173-425",
            "nSamples": 35,
            "observedMeanDensity_kg_m2": 6.229e-05
          },
          {
            "scientificName": "Leucon (Leucon) acutirostris",
            "density_kg_m2": 0.0008521,
            "habitat": "unclassified",
            "depthBand_m": "118-836",
            "nSamples": 60,
            "observedMeanDensity_kg_m2": 5.908e-05
          },
          {
            "scientificName": "Aphia minuta",
            "density_kg_m2": 0.00081979,
            "habitat": "unclassified",
            "depthBand_m": "169-205",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.000825
          },
          {
            "scientificName": "Velutina plicatilis",
            "density_kg_m2": 0.00081,
            "habitat": "unclassified",
            "depthBand_m": "191-279",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.00081
          },
          {
            "scientificName": "Lafoea",
            "density_kg_m2": 0.00080168,
            "habitat": "unclassified",
            "depthBand_m": "57-1221",
            "nSamples": 36,
            "observedMeanDensity_kg_m2": 0.00079
          },
          {
            "scientificName": "Amigdoscalpellum hispidum",
            "density_kg_m2": 0.00078611,
            "habitat": "unclassified",
            "depthBand_m": "168-637",
            "nSamples": 59,
            "observedMeanDensity_kg_m2": 0.00079482
          },
          {
            "scientificName": "Sphaerodoropsis philippi",
            "density_kg_m2": 0.00076,
            "habitat": "unclassified",
            "depthBand_m": "198-808",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.00076
          },
          {
            "scientificName": "Amphithopsis longicaudata",
            "density_kg_m2": 0.0007138,
            "habitat": "unclassified",
            "depthBand_m": "121-917",
            "nSamples": 60,
            "observedMeanDensity_kg_m2": 0.00055867
          },
          {
            "scientificName": "Melphidippa borealis",
            "density_kg_m2": 0.0007027,
            "habitat": "unclassified",
            "depthBand_m": "61-917",
            "nSamples": 210,
            "observedMeanDensity_kg_m2": 0.00068666
          },
          {
            "scientificName": "Liljeborgia",
            "density_kg_m2": 0.00069371,
            "habitat": "unclassified",
            "depthBand_m": "63-2744",
            "nSamples": 61,
            "observedMeanDensity_kg_m2": 0.00053589
          },
          {
            "scientificName": "Melphidippidae",
            "density_kg_m2": 0.00068192,
            "habitat": "unclassified",
            "depthBand_m": "98-782",
            "nSamples": 29,
            "observedMeanDensity_kg_m2": 0.00064874
          },
          {
            "scientificName": "Turrisipho",
            "density_kg_m2": 0.00065451,
            "habitat": "unclassified",
            "depthBand_m": "252-901",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.000655
          },
          {
            "scientificName": "Leptostylis",
            "density_kg_m2": 0.00061537,
            "habitat": "unclassified",
            "depthBand_m": "124-2590",
            "nSamples": 69,
            "observedMeanDensity_kg_m2": 0.00015457
          },
          {
            "scientificName": "Amblyops abbreviatus",
            "density_kg_m2": 0.00061166,
            "habitat": "unclassified",
            "depthBand_m": "154-821",
            "nSamples": 160,
            "observedMeanDensity_kg_m2": 0.0006115
          },
          {
            "scientificName": "Leucothoe",
            "density_kg_m2": 0.00060975,
            "habitat": "unclassified",
            "depthBand_m": "236-332",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.000671
          },
          {
            "scientificName": "Malacostraca",
            "density_kg_m2": 0.00059502,
            "habitat": "unclassified",
            "depthBand_m": "218-503",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.00059
          },
          {
            "scientificName": "Aricidea (Acmira) catherinae",
            "density_kg_m2": 0.00059249,
            "habitat": "unclassified",
            "depthBand_m": "60-1233",
            "nSamples": 70,
            "observedMeanDensity_kg_m2": 0.00046429
          },
          {
            "scientificName": "Astacilla intermedia",
            "density_kg_m2": 0.00058616,
            "habitat": "unclassified",
            "depthBand_m": "155-2744",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.0008325
          },
          {
            "scientificName": "Ampelisca typica",
            "density_kg_m2": 0.00058613,
            "habitat": "unclassified",
            "depthBand_m": "147-900",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.0006555
          },
          {
            "scientificName": "Leucon (Alytoleucon) pallidus",
            "density_kg_m2": 0.00058507,
            "habitat": "unclassified",
            "depthBand_m": "43-1118",
            "nSamples": 37,
            "observedMeanDensity_kg_m2": 0.00064005
          },
          {
            "scientificName": "Hyperiopsis voringi",
            "density_kg_m2": 0.00057788,
            "habitat": "unclassified",
            "depthBand_m": "332-2347",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 0.0005896
          },
          {
            "scientificName": "Velutina",
            "density_kg_m2": 0.000569,
            "habitat": "unclassified",
            "depthBand_m": "114-340",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.000569
          },
          {
            "scientificName": "Lembos",
            "density_kg_m2": 0.00056,
            "habitat": "unclassified",
            "depthBand_m": "154-706",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.00056
          },
          {
            "scientificName": "Aricidea (Strelzovia) suecica",
            "density_kg_m2": 0.00055531,
            "habitat": "unclassified",
            "depthBand_m": "147-750",
            "nSamples": 34,
            "observedMeanDensity_kg_m2": 0.00033333
          },
          {
            "scientificName": "Amphilochidae",
            "density_kg_m2": 0.00053471,
            "habitat": "unclassified",
            "depthBand_m": "52-2744",
            "nSamples": 126,
            "observedMeanDensity_kg_m2": 0.00035469
          },
          {
            "scientificName": "Leptostylis longimana",
            "density_kg_m2": 0.00051893,
            "habitat": "unclassified",
            "depthBand_m": "143-1826",
            "nSamples": 117,
            "observedMeanDensity_kg_m2": 0.00038365
          },
          {
            "scientificName": "Amphilepis",
            "density_kg_m2": 0.0005,
            "habitat": "unclassified",
            "depthBand_m": "295-493",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0005
          },
          {
            "scientificName": "Abra",
            "density_kg_m2": 0.00049,
            "habitat": "unclassified",
            "depthBand_m": "128-379",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.00049
          },
          {
            "scientificName": "Laothoes",
            "density_kg_m2": 0.0004734,
            "habitat": "unclassified",
            "depthBand_m": "250-627",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.000371
          },
          {
            "scientificName": "Meterythrops robustus",
            "density_kg_m2": 0.00046714,
            "habitat": "unclassified",
            "depthBand_m": "124-483",
            "nSamples": 31,
            "observedMeanDensity_kg_m2": 0.0004625
          },
          {
            "scientificName": "Tytthocope megalura",
            "density_kg_m2": 0.000424,
            "habitat": "unclassified",
            "depthBand_m": "172-1236",
            "nSamples": 23,
            "observedMeanDensity_kg_m2": 0.000424
          },
          {
            "scientificName": "Meterythrops",
            "density_kg_m2": 0.000402,
            "habitat": "unclassified",
            "depthBand_m": "307-307",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.000402
          },
          {
            "scientificName": "Kroyera carinata",
            "density_kg_m2": 0.00039329,
            "habitat": "unclassified",
            "depthBand_m": "77-367",
            "nSamples": 19,
            "observedMeanDensity_kg_m2": 0.00038871
          },
          {
            "scientificName": "Acanthonotozoma serratum",
            "density_kg_m2": 0.00039314,
            "habitat": "unclassified",
            "depthBand_m": "47-569",
            "nSamples": 32,
            "observedMeanDensity_kg_m2": 0.00038286
          },
          {
            "scientificName": "Aora typica",
            "density_kg_m2": 0.00038485,
            "habitat": "unclassified",
            "depthBand_m": "77-225",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.000383
          },
          {
            "scientificName": "Ampelisca eschrichtii",
            "density_kg_m2": 0.0003836,
            "habitat": "unclassified",
            "depthBand_m": "124-782",
            "nSamples": 134,
            "observedMeanDensity_kg_m2": 0.00101246
          },
          {
            "scientificName": "Leucon",
            "density_kg_m2": 0.00033317,
            "habitat": "unclassified",
            "depthBand_m": "67-1598",
            "nSamples": 52,
            "observedMeanDensity_kg_m2": 0.00036182
          },
          {
            "scientificName": "Lepechinella",
            "density_kg_m2": 0.00031932,
            "habitat": "unclassified",
            "depthBand_m": "98-773",
            "nSamples": 31,
            "observedMeanDensity_kg_m2": 0.00036252
          },
          {
            "scientificName": "Ampeliscidae",
            "density_kg_m2": 0.00031517,
            "habitat": "unclassified",
            "depthBand_m": "93-2020",
            "nSamples": 209,
            "observedMeanDensity_kg_m2": 0.00010922
          },
          {
            "scientificName": "Apseudes talpa",
            "density_kg_m2": 0.000308,
            "habitat": "unclassified",
            "depthBand_m": "226-226",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.000308
          },
          {
            "scientificName": "Maera loveni",
            "density_kg_m2": 0.00029089,
            "habitat": "unclassified",
            "depthBand_m": "114-881",
            "nSamples": 24,
            "observedMeanDensity_kg_m2": 0.00054032
          },
          {
            "scientificName": "Amblyopsoides ohlinii",
            "density_kg_m2": 0.000284,
            "habitat": "unclassified",
            "depthBand_m": "1826-1826",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.000284
          },
          {
            "scientificName": "Leucon (Leucon) serratus",
            "density_kg_m2": 0.00027315,
            "habitat": "unclassified",
            "depthBand_m": "43-1236",
            "nSamples": 120,
            "observedMeanDensity_kg_m2": 0.00017863
          },
          {
            "scientificName": "Leucon (Leucon) fulvus",
            "density_kg_m2": 0.00026641,
            "habitat": "unclassified",
            "depthBand_m": "98-656",
            "nSamples": 30,
            "observedMeanDensity_kg_m2": 0.00028
          },
          {
            "scientificName": "Idotea emarginata",
            "density_kg_m2": 0.00026417,
            "habitat": "unclassified",
            "depthBand_m": "183-824",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.0002525
          },
          {
            "scientificName": "Leucon (Macrauloleucon) siphonatus",
            "density_kg_m2": 0.00026267,
            "habitat": "unclassified",
            "depthBand_m": "1046-1330",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 2.191e-05
          },
          {
            "scientificName": "Megamphopus cornutus",
            "density_kg_m2": 0.000262,
            "habitat": "unclassified",
            "depthBand_m": "50-272",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.000262
          },
          {
            "scientificName": "Laothoes meinerti",
            "density_kg_m2": 0.00024888,
            "habitat": "unclassified",
            "depthBand_m": "155-1899",
            "nSamples": 27,
            "observedMeanDensity_kg_m2": 0.00026575
          },
          {
            "scientificName": "Tryphosella horingi",
            "density_kg_m2": 0.00024486,
            "habitat": "unclassified",
            "depthBand_m": "188-627",
            "nSamples": 28,
            "observedMeanDensity_kg_m2": 0.00027564
          },
          {
            "scientificName": "Leucon (Leucon) nasica",
            "density_kg_m2": 0.0002436,
            "habitat": "unclassified",
            "depthBand_m": "215-279",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0002436
          },
          {
            "scientificName": "Macrocypris",
            "density_kg_m2": 0.00024,
            "habitat": "unclassified",
            "depthBand_m": "229-229",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.00024
          },
          {
            "scientificName": "Melphidippa macrura",
            "density_kg_m2": 0.00023335,
            "habitat": "unclassified",
            "depthBand_m": "118-707",
            "nSamples": 50,
            "observedMeanDensity_kg_m2": 0.00023179
          },
          {
            "scientificName": "Leptamphopus sarsi",
            "density_kg_m2": 0.00023309,
            "habitat": "unclassified",
            "depthBand_m": "173-1598",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 0.000224
          },
          {
            "scientificName": "Themisto",
            "density_kg_m2": 0.000228,
            "habitat": "unclassified",
            "depthBand_m": "48-1018",
            "nSamples": 15,
            "observedMeanDensity_kg_m2": 0.000228
          },
          {
            "scientificName": "Andaniopsis nordlandica",
            "density_kg_m2": 0.00022456,
            "habitat": "unclassified",
            "depthBand_m": "87-618",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 0.00024
          },
          {
            "scientificName": "Tryphosella nanoides",
            "density_kg_m2": 0.0002083,
            "habitat": "unclassified",
            "depthBand_m": "147-610",
            "nSamples": 21,
            "observedMeanDensity_kg_m2": 0.00022169
          },
          {
            "scientificName": "Idunella",
            "density_kg_m2": 0.000192,
            "habitat": "unclassified",
            "depthBand_m": "355-808",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.000192
          },
          {
            "scientificName": "Krithe praetexta",
            "density_kg_m2": 0.00018,
            "habitat": "unclassified",
            "depthBand_m": "300-300",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.00018
          },
          {
            "scientificName": "Thyasiridae",
            "density_kg_m2": 0.00018,
            "habitat": "unclassified",
            "depthBand_m": "68-1018",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.00018
          },
          {
            "scientificName": "Mollusca",
            "density_kg_m2": 0.00017904,
            "habitat": "unclassified",
            "depthBand_m": "92-366",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 0.00088867
          },
          {
            "scientificName": "Leptostylis ampullacea",
            "density_kg_m2": 0.00016835,
            "habitat": "unclassified",
            "depthBand_m": "98-402",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.00017653
          },
          {
            "scientificName": "Andaniexis",
            "density_kg_m2": 0.00016647,
            "habitat": "unclassified",
            "depthBand_m": "207-1118",
            "nSamples": 13,
            "observedMeanDensity_kg_m2": 0.000174
          },
          {
            "scientificName": "Andaniexis abyssi",
            "density_kg_m2": 0.00016095,
            "habitat": "unclassified",
            "depthBand_m": "80-1022",
            "nSamples": 73,
            "observedMeanDensity_kg_m2": 0.000165
          },
          {
            "scientificName": "Leptophoxus falcatus",
            "density_kg_m2": 0.00015008,
            "habitat": "unclassified",
            "depthBand_m": "98-656",
            "nSamples": 124,
            "observedMeanDensity_kg_m2": 0.00013668
          },
          {
            "scientificName": "Andaniopsis pectinata",
            "density_kg_m2": 0.00014975,
            "habitat": "unclassified",
            "depthBand_m": "127-358",
            "nSamples": 16,
            "observedMeanDensity_kg_m2": 0.00014
          },
          {
            "scientificName": "Amathillopsis",
            "density_kg_m2": 0.000148,
            "habitat": "unclassified",
            "depthBand_m": "1189-1189",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.000148
          },
          {
            "scientificName": "Leptostylis macrura",
            "density_kg_m2": 0.00013124,
            "habitat": "unclassified",
            "depthBand_m": "118-2004",
            "nSamples": 92,
            "observedMeanDensity_kg_m2": 0.00013533
          },
          {
            "scientificName": "Aristias tumidus",
            "density_kg_m2": 0.00011996,
            "habitat": "unclassified",
            "depthBand_m": "164-410",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.00012
          },
          {
            "scientificName": "Aristias neglectus",
            "density_kg_m2": 0.00011285,
            "habitat": "unclassified",
            "depthBand_m": "119-555",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.00011578
          },
          {
            "scientificName": "Amphilochus tenuimanus",
            "density_kg_m2": 0.000109,
            "habitat": "unclassified",
            "depthBand_m": "82-937",
            "nSamples": 73,
            "observedMeanDensity_kg_m2": 0.00011767
          },
          {
            "scientificName": "Aspidarachna clypeata",
            "density_kg_m2": 0.00010878,
            "habitat": "unclassified",
            "depthBand_m": "180-864",
            "nSamples": 37,
            "observedMeanDensity_kg_m2": 0.000108
          },
          {
            "scientificName": "Medicorophium affine",
            "density_kg_m2": 0.00010164,
            "habitat": "unclassified",
            "depthBand_m": "103-387",
            "nSamples": 30,
            "observedMeanDensity_kg_m2": 0.000102
          },
          {
            "scientificName": "Lichenoporidae",
            "density_kg_m2": 0.0001,
            "habitat": "unclassified",
            "depthBand_m": "205-328",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0001
          },
          {
            "scientificName": "Leptostraca",
            "density_kg_m2": 9.796e-05,
            "habitat": "unclassified",
            "depthBand_m": "115-604",
            "nSamples": 45,
            "observedMeanDensity_kg_m2": 9.314e-05
          },
          {
            "scientificName": "Liljeborgia (Liljeborgia) pallida",
            "density_kg_m2": 9.795e-05,
            "habitat": "unclassified",
            "depthBand_m": "91-1071",
            "nSamples": 51,
            "observedMeanDensity_kg_m2": 0.00010727
          },
          {
            "scientificName": "Westwoodilla brevicalcar",
            "density_kg_m2": 9.787e-05,
            "habitat": "unclassified",
            "depthBand_m": "61-300",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.00010133
          },
          {
            "scientificName": "Lepidepecreum umbo",
            "density_kg_m2": 9.762e-05,
            "habitat": "unclassified",
            "depthBand_m": "68-901",
            "nSamples": 100,
            "observedMeanDensity_kg_m2": 0.0001065
          },
          {
            "scientificName": "Astacilla pusilla",
            "density_kg_m2": 9.4e-05,
            "habitat": "unclassified",
            "depthBand_m": "227-659",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 9.4e-05
          },
          {
            "scientificName": "Tryphosella",
            "density_kg_m2": 9.392e-05,
            "habitat": "unclassified",
            "depthBand_m": "188-900",
            "nSamples": 17,
            "observedMeanDensity_kg_m2": 0.00010029
          },
          {
            "scientificName": "Anomura",
            "density_kg_m2": 8e-05,
            "habitat": "unclassified",
            "depthBand_m": "128-350",
            "nSamples": 19,
            "observedMeanDensity_kg_m2": 8e-05
          },
          {
            "scientificName": "Lembos websteri",
            "density_kg_m2": 8e-05,
            "habitat": "unclassified",
            "depthBand_m": "881-881",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 8e-05
          },
          {
            "scientificName": "Tryphosella angulata",
            "density_kg_m2": 8e-05,
            "habitat": "unclassified",
            "depthBand_m": "188-490",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 8e-05
          },
          {
            "scientificName": "Arcidae",
            "density_kg_m2": 7.2e-05,
            "habitat": "unclassified",
            "depthBand_m": "881-881",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 7.2e-05
          },
          {
            "scientificName": "Liljeborgia (Liljeborgia) kinahani",
            "density_kg_m2": 7.172e-05,
            "habitat": "unclassified",
            "depthBand_m": "202-875",
            "nSamples": 18,
            "observedMeanDensity_kg_m2": 7.6e-05
          },
          {
            "scientificName": "Melphidippa",
            "density_kg_m2": 7.033e-05,
            "habitat": "unclassified",
            "depthBand_m": "171-815",
            "nSamples": 27,
            "observedMeanDensity_kg_m2": 7.569e-05
          },
          {
            "scientificName": "Abietinaria",
            "density_kg_m2": 7e-05,
            "habitat": "unclassified",
            "depthBand_m": "351-351",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 7e-05
          },
          {
            "scientificName": "Lysianella petalocera",
            "density_kg_m2": 6.692e-05,
            "habitat": "unclassified",
            "depthBand_m": "220-329",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 7.6e-05
          },
          {
            "scientificName": "Leptostylis villosa",
            "density_kg_m2": 6.505e-05,
            "habitat": "unclassified",
            "depthBand_m": "43-1751",
            "nSamples": 80,
            "observedMeanDensity_kg_m2": 6.448e-05
          },
          {
            "scientificName": "Acidostoma obesum",
            "density_kg_m2": 6.329e-05,
            "habitat": "unclassified",
            "depthBand_m": "183-831",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 6.55e-05
          },
          {
            "scientificName": "Liljeborgiidae",
            "density_kg_m2": 6.306e-05,
            "habitat": "unclassified",
            "depthBand_m": "118-2744",
            "nSamples": 34,
            "observedMeanDensity_kg_m2": 8.554e-05
          },
          {
            "scientificName": "Tmetonyx albidus",
            "density_kg_m2": 6.101e-05,
            "habitat": "unclassified",
            "depthBand_m": "189-627",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 6e-05
          },
          {
            "scientificName": "Tryphosella sarsi",
            "density_kg_m2": 5.07e-05,
            "habitat": "unclassified",
            "depthBand_m": "189-432",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 5.2e-05
          },
          {
            "scientificName": "Maldane",
            "density_kg_m2": 5e-05,
            "habitat": "unclassified",
            "depthBand_m": "188-1020",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 5e-05
          },
          {
            "scientificName": "Metopa borealis",
            "density_kg_m2": 4.652e-05,
            "habitat": "unclassified",
            "depthBand_m": "207-621",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 4.733e-05
          },
          {
            "scientificName": "Lampropidae",
            "density_kg_m2": 4.595e-05,
            "habitat": "unclassified",
            "depthBand_m": "183-854",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 4.354e-05
          },
          {
            "scientificName": "Iphimedia",
            "density_kg_m2": 4.042e-05,
            "habitat": "unclassified",
            "depthBand_m": "50-1022",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 5.4e-05
          },
          {
            "scientificName": "Aspidarachna",
            "density_kg_m2": 4e-05,
            "habitat": "unclassified",
            "depthBand_m": "296-316",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 4e-05
          },
          {
            "scientificName": "Amphilochoides",
            "density_kg_m2": 3.8e-05,
            "habitat": "unclassified",
            "depthBand_m": "50-398",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 3.8e-05
          },
          {
            "scientificName": "Ampelisca amblyops",
            "density_kg_m2": 3.625e-05,
            "habitat": "unclassified",
            "depthBand_m": "224-425",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 3.64e-05
          },
          {
            "scientificName": "Lamprops",
            "density_kg_m2": 3.375e-05,
            "habitat": "unclassified",
            "depthBand_m": "146-300",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 3.333e-05
          },
          {
            "scientificName": "Ambasia atlantica",
            "density_kg_m2": 3.2e-05,
            "habitat": "unclassified",
            "depthBand_m": "211-267",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 3.2e-05
          },
          {
            "scientificName": "Melphidippa goesi",
            "density_kg_m2": 3.144e-05,
            "habitat": "unclassified",
            "depthBand_m": "76-623",
            "nSamples": 27,
            "observedMeanDensity_kg_m2": 3.125e-05
          },
          {
            "scientificName": "Anoplodactylus petiolatus",
            "density_kg_m2": 2.996e-05,
            "habitat": "unclassified",
            "depthBand_m": "128-238",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 3e-05
          },
          {
            "scientificName": "Janiridae",
            "density_kg_m2": 2.846e-05,
            "habitat": "unclassified",
            "depthBand_m": "187-2347",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 3e-05
          },
          {
            "scientificName": "Leucon (Crymoleucon) tener",
            "density_kg_m2": 2.36e-05,
            "habitat": "unclassified",
            "depthBand_m": "226-400",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 2.36e-05
          },
          {
            "scientificName": "Metopa",
            "density_kg_m2": 2.165e-05,
            "habitat": "unclassified",
            "depthBand_m": "63-543",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 2.36e-05
          },
          {
            "scientificName": "Amphilochoides serratipes",
            "density_kg_m2": 2e-05,
            "habitat": "unclassified",
            "depthBand_m": "147-207",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 2e-05
          },
          {
            "scientificName": "Unciolidae",
            "density_kg_m2": 2e-05,
            "habitat": "unclassified",
            "depthBand_m": "357-824",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 2e-05
          },
          {
            "scientificName": "Amphilochus",
            "density_kg_m2": 1.904e-05,
            "habitat": "unclassified",
            "depthBand_m": "77-363",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 1.9e-05
          },
          {
            "scientificName": "Laetmatophilus armatus",
            "density_kg_m2": 1.771e-05,
            "habitat": "unclassified",
            "depthBand_m": "77-425",
            "nSamples": 40,
            "observedMeanDensity_kg_m2": 1.91e-05
          },
          {
            "scientificName": "Leucon (Macrauloleucon) spinulosus",
            "density_kg_m2": 1.523e-05,
            "habitat": "unclassified",
            "depthBand_m": "448-2347",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 1.527e-05
          },
          {
            "scientificName": "Leptanthura tenuis",
            "density_kg_m2": 1.3e-05,
            "habitat": "unclassified",
            "depthBand_m": "168-431",
            "nSamples": 21,
            "observedMeanDensity_kg_m2": 1.3e-05
          },
          {
            "scientificName": "Amblyops",
            "density_kg_m2": 1.169e-05,
            "habitat": "unclassified",
            "depthBand_m": "265-636",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 9.5e-06
          },
          {
            "scientificName": "Westwoodilla",
            "density_kg_m2": 1.081e-05,
            "habitat": "unclassified",
            "depthBand_m": "124-1236",
            "nSamples": 16,
            "observedMeanDensity_kg_m2": 1e-05
          },
          {
            "scientificName": "Leucon (Leucon) nasicoides",
            "density_kg_m2": 6.4e-06,
            "habitat": "unclassified",
            "depthBand_m": "47-824",
            "nSamples": 32,
            "observedMeanDensity_kg_m2": 6.4e-06
          },
          {
            "scientificName": "Lamprops fuscatus",
            "density_kg_m2": 4e-06,
            "habitat": "unclassified",
            "depthBand_m": "47-307",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 4e-06
          },
          {
            "scientificName": "Leuconidae",
            "density_kg_m2": 3.77e-06,
            "habitat": "unclassified",
            "depthBand_m": "52-1118",
            "nSamples": 14,
            "observedMeanDensity_kg_m2": 3.8e-06
          },
          {
            "scientificName": "Argulus",
            "density_kg_m2": 3.6e-06,
            "habitat": "unclassified",
            "depthBand_m": "824-824",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 3.6e-06
          },
          {
            "scientificName": "Acari",
            "density_kg_m2": 2e-06,
            "habitat": "unclassified",
            "depthBand_m": "77-2590",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 2e-06
          },
          {
            "scientificName": "Macrostylis spinifera",
            "density_kg_m2": 1.24e-06,
            "habitat": "unclassified",
            "depthBand_m": "219-854",
            "nSamples": 14,
            "observedMeanDensity_kg_m2": 1.5e-06
          },
          {
            "scientificName": "Liriopsis pygmaea",
            "density_kg_m2": 1e-07,
            "habitat": "unclassified",
            "depthBand_m": "227-227",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 1e-07
          },
          {
            "scientificName": "Abietinaria abietina",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "44-304",
            "nSamples": 45,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Abietinaria pulchra",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "190-875",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Abyssoninoe",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "162-1581",
            "nSamples": 85,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Abyssoninoe abyssorum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "87-1477",
            "nSamples": 24,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Abyssoninoe hibernica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "161-1045",
            "nSamples": 70,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Acanthancora aenigma",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "392-392",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Acanthella erecta",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "553-679",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Acantheurypon spinispinosum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "239-239",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Acanthicolepis zibrowii",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "412-412",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Acanthocardia echinata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "134-134",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Acanthodoris pilosa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "183-183",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Acanthonotozoma",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "103-412",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Acanthonotozoma cristatum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "141-679",
            "nSamples": 22,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Acanthonotozoma inflatum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "82-444",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Acanthonotozoma rusanovae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "333-333",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Acanthonotozoma sinuatum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "80-487",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Acanthonotozomatidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "401-401",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Acanthostepheia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "184-184",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Acanthostepheia incarinata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "141-298",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Acanthostepheia malmgreni",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "114-501",
            "nSamples": 30,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aceroides (Aceroides) latipes",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "132-500",
            "nSamples": 59,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aclis sarsi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "373-400",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aclis walleri",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "178-410",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Admete",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "134-148",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aechmalotus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "636-636",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aega",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "380-380",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aega bicarinata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "184-413",
            "nSamples": 32,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aega crenulata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "187-187",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aega monophthalma",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "350-658",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aegidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "320-320",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aeginina",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "467-467",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aeginina longicornis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "603-860",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aegiochus arctica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "380-542",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aegiochus gracilipes",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "239-239",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aglaophamus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "77-431",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Alcyonidiidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "547-950",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Alcyonidium",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "75-610",
            "nSamples": 54,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Alcyonidium diaphanum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "42-42",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Alcyonidium gelatinosum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "45-124",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Alcyonidium mamillatum erectum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "171-171",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Alcyonium",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "950-950",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aldisa zetlandica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "298-318",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Alentia gelatinosa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "119-281",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Allantactis parasitica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "61-499",
            "nSamples": 14,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Altenaeum dawsoni",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "42-74",
            "nSamples": 14,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Alvania moerchii",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "162-547",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Alvania punctura",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "245-425",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Alvania scrobiculata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "392-448",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Alvania subsoluta",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "105-274",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Alvania testae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "246-457",
            "nSamples": 24,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Alvania verrilli",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "240-240",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Alvania zetlandica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "290-291",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amathillopsidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "961-961",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amathillopsis affinis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "203-203",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amauropsis islandica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "42-67",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amblyopsoides crozetii",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "2241-2241",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amblyosyllis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "82-82",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amblyosyllis finmarchica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "105-105",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ammodytes marinus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "87-87",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ammotheidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "1071-1071",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ampelisca anomala",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "224-380",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ampelisca brevicornis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "48-380",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ampharete baltica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "197-826",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ampharete borealis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "68-422",
            "nSamples": 50,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ampharete goesi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "60-103",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ampharete undecima",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "304-965",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphianthus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "222-864",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphiblestrum solidum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "58-171",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphicteis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "208-608",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphicteis ninonae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "124-1057",
            "nSamples": 55,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphicteis sundevalli",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "214-214",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphicteis wesenbergae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "1229-2354",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphilochus anoculus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "197-2744",
            "nSamples": 21,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphilochus hamatus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "104-2561",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphinomidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "207-207",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphipholis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "60-67",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphipholis torelli",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "58-171",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphissa acutecostata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "190-485",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphithoides",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "854-854",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphitrite cirrata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "58-750",
            "nSamples": 26,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphitrite figulus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "282-282",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphiura chiajei",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "168-237",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphiura fragilis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "172-172",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphiura griegi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "190-379",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Amphiura sundevalli",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "61-875",
            "nSamples": 31,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ampithoe",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "313-313",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Anapagurus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "91-474",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Anchistioides",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "311-311",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Andaniexinae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "305-305",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Andaniopsinae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "226-297",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Andaniopsis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "313-397",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Anguillosyllis pupa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "372-372",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Anisarchus medius",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "160-160",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Annelida",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "134-809",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Anomalisipho verkruezeni",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "171-765",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Anomia ephippium",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "135-214",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Anonyx debruynii",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "114-875",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Anoplodactylus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "263-263",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Anoplodactylus arnaudae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "234-272",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Anoplodactylus typhlops",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "313-447",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ansphyrapus tudes",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "93-210",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Antedonoidea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "61-500",
            "nSamples": 16,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Antho",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "320-320",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Anthoathecata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "658-659",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Anthomastus grandiflorus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "327-327",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Anthuroidea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "188-625",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aora spinicornis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "273-273",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aphelochaeta mcintoshi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "171-187",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Apherusa cirrus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "128-128",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Apherusa glacialis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "416-416",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Apherusa jurinei",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "184-543",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Apherusa sarsii",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "67-543",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aphrodita",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "190-378",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aphrodita alta",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "224-324",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aphroditidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "188-349",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Apistobranchus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "305-305",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Apistobranchus tenuis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "74-74",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aplidium",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "58-687",
            "nSamples": 39,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aplidium glabrum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "208-608",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aplidium mutabile",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "155-667",
            "nSamples": 15,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aplidium pallidum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "171-547",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aplousobranchia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "44-936",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Apodida",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "183-183",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Apomatus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "307-705",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aponuphis bilineata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "168-548",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aporrhais pespelecani",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "157-448",
            "nSamples": 45,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aporrhais serresiana",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "184-270",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Apseudes",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "270-270",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Apseudidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "689-918",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aquiloniella paenulata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "103-328",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aquiloniella scabra",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "105-328",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Arcopella balaustina",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "187-187",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Arctolembos arcticus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "296-358",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Arctonula arctica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "105-171",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Arctopleustes glabricauda",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "380-659",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Arcturus baffini",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "543-543",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Argentina",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "118-486",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Argentina silus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "167-271",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Argissa hamatipes",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "56-569",
            "nSamples": 31,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ariadnaria borealis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "119-458",
            "nSamples": 30,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aricidea (Acmira) simonae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "92-749",
            "nSamples": 28,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aricidea (Aricidea) albatrossae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "175-828",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aricidea (Aricidea) minuta",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "187-247",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aricidea (Strelzovia) parabelgicae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "348-348",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aricidea abranchiata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "629-1112",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aricidea hartmanae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "270-767",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aristias",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "160-383",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Arrhinopsis longicornis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "80-260",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Artacama proboscidea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "77-451",
            "nSamples": 16,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Artemisina arcigera",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "189-392",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Artemisina lundbecki",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "124-548",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Articulata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "2537-2537",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Asajirus indicus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "659-1704",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Asbestopluma",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "238-1189",
            "nSamples": 16,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Asbestopluma (Asbestopluma)",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "875-875",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Asbestopluma (Asbestopluma) bihamatifera",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "875-875",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Asbestopluma (Asbestopluma) furcata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "853-853",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Asbestopluma (Asbestopluma) pennatula",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "187-875",
            "nSamples": 65,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ascidia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "42-1608",
            "nSamples": 27,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ascidia callosa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "114-412",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ascidia conchilega",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "135-145",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ascidia dijmphniana",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "203-203",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ascidia mentula",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "101-272",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ascidia obliqua",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "112-1057",
            "nSamples": 40,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ascidia prunum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "68-461",
            "nSamples": 29,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ascidia virginea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "118-225",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Asconema",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "160-679",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Asconema foliatum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "188-611",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Asellus (Asellus) aquaticus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "1118-1118",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aspidosiphon (Aspidosiphon) muelleri muelleri",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "153-1477",
            "nSamples": 16,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Aspidosiphonidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "355-355",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Astacilla",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "157-850",
            "nSamples": 21,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Astacilla dilatata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "154-850",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Astacilla granulata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "384-814",
            "nSamples": 16,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Astacilla longispina",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "402-402",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Astarte crebricostata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "153-411",
            "nSamples": 13,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Astarte subaequilatera",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "128-381",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Asteronyx",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "91-214",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Astropecten",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "49-553",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Astrophorina",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "188-378",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Astyra",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "917-917",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hydractinia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "1036-1036",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hydractinia sarsii",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "45-45",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hydrallmania falcata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "44-875",
            "nSamples": 17,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hydroidolina",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "187-937",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymedesmia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "201-658",
            "nSamples": 13,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymedesmia (Hymedesmia) crux",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "349-378",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymedesmia (Hymedesmia) curvichela",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "611-611",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymedesmia (Hymedesmia) filifera",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "199-658",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymedesmia (Hymedesmia) laevistylus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "349-349",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymedesmia (Hymedesmia) longistylus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "256-256",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymedesmia (Hymedesmia) mucronata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "349-349",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymedesmia (Hymedesmia) nummulus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "171-236",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymedesmia (Hymedesmia) occulta",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "611-853",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymedesmia (Hymedesmia) paupertas",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "199-259",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymedesmia (Hymedesmia) procumbens",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "392-392",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymedesmia (Hymedesmia) simillima",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "256-349",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymedesmia (Hymedesmia) trichoma",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "343-343",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymedesmia (Hymedesmia) truncata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "199-611",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymedesmia (Stylopus) mucronella",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "211-349",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymenaster",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "997-2241",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymeniacidon",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "333-658",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymeniacidon assimilis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "208-875",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymenodora",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "808-2746",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymenodora gracilis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "2609-2672",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hymeraphia stellifera",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "188-212",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hypereteone foliosa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "128-330",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hyperia galba",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "44-765",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hyperiidea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "765-765",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hyperiopsis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "918-918",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Hyperoche medusarum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "46-46",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ianiropsis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "283-283",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ianiropsis breviremis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "219-330",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ianthe",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "623-917",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ianthopsis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "706-706",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Icasterias panopla",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "124-458",
            "nSamples": 26,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Icelus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "68-218",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ichnopus spinicornis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "298-298",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Idanthyrsus saxicavus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "252-252",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Idmidronea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "484-484",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Idmonea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "259-259",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Idotea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "128-2744",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Idotea granulosa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "42-42",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Idotea neglecta",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "2590-2744",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ilyarachna bergendahli",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "867-867",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ilyarachna bicornis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "184-410",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ilyarachna frami",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "541-541",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ilyarachna propinqua",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "268-268",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ilyarachna una",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "397-397",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Inachus phalangium",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "412-412",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Inflatella",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "397-397",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Inflatella pellicula",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "256-421",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Infundibulipora lucernaria",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "258-301",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Iolanthe typhlops",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "547-637",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Iophon dubium",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "75-304",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Iophon nigricans",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "333-333",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Iophon piceum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "390-486",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Iothia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "180-180",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Iotroata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "390-390",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Iotroata abyssi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "199-349",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Iotroata oxeata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "242-242",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Iotroata polydentata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "333-333",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Janiralata tricornis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "76-90",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Janiroidea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "115-689",
            "nSamples": 48,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Janulum spinispiculum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "189-390",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Jasmineira",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "124-1863",
            "nSamples": 16,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Jassa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "547-623",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Jassa falcata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "623-623",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Katerythrops oceanae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "252-267",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Katianira bilobata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "300-689",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Kerguelenia borealis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "145-358",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Kinetoskias",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "202-202",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Kirchenpaueria",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "547-547",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Kirchenpaueria bonnevieae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "237-382",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Kirkegaardia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "306-1232",
            "nSamples": 28,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Kirkegaardia dorsobranchialis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "750-750",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Kirkegaardia serrata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "329-410",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Kolga hyalina",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "2049-2872",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Kolga nana",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "278-278",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Kophobelemnon",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "172-399",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Kukenthalia borealis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "155-296",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Kurtiella",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "689-689",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Kurtiella ovata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "128-128",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Kurtiella tumidula",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "235-372",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lacuna crassior",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "312-312",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lacuna vincta",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "63-63",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lacydoniidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "100-100",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Laetmonice uschakovi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "180-298",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lafoea fruticosa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "115-875",
            "nSamples": 18,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lafoea gracillima",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "169-875",
            "nSamples": 23,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lafoea grandis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "208-209",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lafoeina",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "82-82",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lafoeina maxima",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "63-503",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lafoeina tenuis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "382-390",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lamellaria latens",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "189-189",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lanassa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "265-458",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Laomedea angulata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "382-382",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Laomedea flexuosa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "199-199",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Laothoes polylovi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "245-369",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lasaea adansoni",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "368-629",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Latrunculia (Biannulata) triloba",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "259-853",
            "nSamples": 15,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Laubieriopsis cabiochi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "259-259",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Laubieriopsis norvegica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "265-485",
            "nSamples": 28,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leanira hystricis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "966-966",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lebetus scorpioides",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "178-320",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ledella messanensis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "168-687",
            "nSamples": 202,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leieschara",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "57-258",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leieschara coarctata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "58-241",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leieschara subgracilis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "58-82",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leilaster radians",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "291-291",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leiochone",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "303-303",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leiochrides",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "266-266",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leiochrides norvegicus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "190-608",
            "nSamples": 23,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leitoscoloplos",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "306-913",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leitoscoloplos mammosus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "58-968",
            "nSamples": 153,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lepadomorpha",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "187-187",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lepas",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "327-327",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lepechinella chrysotheras",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "448-850",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lepechinella eupraxiella",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "540-663",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lepechinella helgii",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "548-768",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lepechinellidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "259-1060",
            "nSamples": 21,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lepechinelloides karii",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "321-337",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lepeta caeca",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "48-465",
            "nSamples": 63,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lepetidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "209-209",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lepidasthenia brunnea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "431-431",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lepidorhombus boscii",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "211-448",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lepidorhombus whiffiagonis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "162-202",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lepraliella contigua",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "58-90",
            "nSamples": 13,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lepralioides nordlandica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "259-259",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leptagonus decagonus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "128-374",
            "nSamples": 15,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leptanthura",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "293-993",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leptanthuridae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "186-476",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leptasterias (Leptasterias) muelleri",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "115-304",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leptasterias hyperborea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "63-258",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leptochiton cancellatus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "190-190",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leptognathia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "622-622",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leptognathiidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "629-629",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leptomysinae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "93-372",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leptosynapta",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "147-245",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leptosynapta decaria",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "245-245",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leptothecata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "241-241",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leucandra",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "105-236",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leucia nivea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "355-355",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leucia violacea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "273-405",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leuckartiara octona",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "48-277",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leucon (Crymoleucon)",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "338-388",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leucon (Leucon)",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "141-836",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leucon (Leucon) profundus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "184-410",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leucon (Leucon) robustus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "295-313",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leucon afeni",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "161-458",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leucopsila stilifera",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "212-212",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leucosolenia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "105-425",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leucosolenida",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "44-658",
            "nSamples": 120,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leucothoe articulosa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "298-298",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leucothoe lilljeborgi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "147-369",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leucothoidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "93-210",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Leufroyia leufroyi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "119-187",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Levinsenia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "486-486",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Levinsenia flava",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "190-446",
            "nSamples": 29,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Levinsenia oculata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "412-412",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lichenopora",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "67-171",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Liljeborgia (Liljeborgia) inermis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "282-282",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Liljeborgia (Lilljeborgiella) abyssotypica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "251-251",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Liljeborgia (Lilljeborgiella) caliginis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "487-875",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Liljeborgia (Lilljeborgiella) ossiani",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "202-501",
            "nSamples": 17,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Limacina helicina",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "119-119",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Limaria loscombi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "100-214",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Limatula bisecta",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "182-446",
            "nSamples": 18,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Limatula demiradiata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "239-239",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Limatula hyperborea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "355-355",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Limatula subovata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "145-370",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Limneria",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "128-225",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Limopsis aurita",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "176-687",
            "nSamples": 195,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Liocyma fluctuosa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "87-87",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Liparis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "44-2020",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Liparis bathyarcticus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "47-316",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Liparis fabricii",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "45-307",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Liparis liparis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "63-82",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Liponema",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "257-257",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Liponema multicorne",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "257-451",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lissoclinum aureum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "611-611",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lissodendoryx",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "168-553",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lissodendoryx (Ectyodoryx) atlantica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "256-256",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lissodendoryx (Lissodendoryx) complicata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "611-2597",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lissodendoryx (Lissodendoryx) fragilis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "211-306",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lissodendoryx (Lissodendoryx) lundbecki",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "199-199",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lophaster",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "203-553",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lophogaster typicus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "91-384",
            "nSamples": 14,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lucernaria",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "259-259",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lucernaria bathyphila",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "132-2354",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Luidia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "147-163",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Luidia ciliaris",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "112-112",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lumbrineris coccinea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "392-392",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lumbrineris futilis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "358-562",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lumbrineris latreilli",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "159-1040",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lumpeninae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "257-257",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lycenchelys kolthoffi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "218-218",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lycodes reticulatus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "966-966",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lycodes seminudus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "897-1024",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lycopodina",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "188-188",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lycopodina infundibulum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "208-547",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lycopodina lycopodium",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "328-1036",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lycopodina minuta",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "547-547",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lycopodina tendali",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "611-658",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lyonsia norwegica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "91-91",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lyonsiella subquadrata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "236-396",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lysianassa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "182-329",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lysianassoidea incertae sedis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "307-860",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lysilla",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "135-259",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lysippe fragilis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "195-195",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lysippe labiata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "82-431",
            "nSamples": 83,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Lytocarpia myriophyllum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "57-777",
            "nSamples": 27,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Macandrevia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "384-384",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Macellicephala",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "214-214",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Macellicephala violacea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "190-190",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Macoma calcarea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "58-328",
            "nSamples": 40,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Macoma loveni",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "128-128",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Macrochaeta clavicornis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "59-658",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Macrochaeta helgolandica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "182-900",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Macropipus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "148-307",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Macropipus tuberculatus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "214-272",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Macrostylidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "282-282",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Macrostylis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "176-2744",
            "nSamples": 11,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Macrostylis longiremis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "193-2189",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Madrepora oculata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "320-320",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Maera",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "369-369",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Maera tenera",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "760-760",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Maeridae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "204-451",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Majoidea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "177-603",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Malacalcyonacea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "264-2354",
            "nSamples": 15,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Maldane cristata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "87-87",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Malletia johnsoni",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "266-447",
            "nSamples": 13,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Mallotus villosus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "105-167",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Malmgrenia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "258-448",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Malmgrenia andreapolis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "378-378",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Malmgrenia arenicolae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "187-187",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Malmgrenia castanea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "270-270",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Malmgrenia ljungmani",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "124-187",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Malmgrenia lunulata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "335-335",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Mangeliidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "128-814",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Margarites helicinus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "103-103",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Margarites olivaceus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "59-501",
            "nSamples": 33,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Margarites vahlii",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "103-103",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Marsenina glabra",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "155-239",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Maurolicus muelleri",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "82-765",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Megaluropus agilis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "273-273",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Megamoera dentata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "50-260",
            "nSamples": 22,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Melaenis loveni",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "114-216",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Melanella",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "100-100",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Melanella frielei",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "202-202",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Melanella martynjordani",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "190-276",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Melanella polita",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "171-400",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Melinna",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "153-370",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Melita",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "171-171",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Mellonympha",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "320-320",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Mellonympha mortenseni",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "221-405",
            "nSamples": 18,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Melonanchora",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "334-334",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Melonanchora elliptica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "199-553",
            "nSamples": 10,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Melonanchora emphysema",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "259-259",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Melphidippa willemiana",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "188-501",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Melphidippella",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "623-623",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Melphidippella macra",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "124-503",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Membranipora membranacea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "277-277",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Membraniporoidea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "63-63",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Mendicula",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "314-831",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Mendicula pygmaea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "68-1113",
            "nSamples": 98,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Menestho truncatula",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "213-213",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Menigrates obtusifrons",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "171-782",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Merluccius merluccius",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "271-271",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Mesochaetopterus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "539-539",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Metaconchoecia skogsbergi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "591-782",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Metopa alderi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "228-627",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Metopa bruzelii",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "272-623",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Metopa clypeata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "917-917",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Metopa colliei",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "706-706",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Metopa latimana",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "226-226",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Metopa longicornis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "623-767",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Metopa propinqva",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "249-623",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Metopa pusilla",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "621-706",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Metopa quadrangula",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "777-777",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Metopa submajuscula",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "917-917",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Metopella",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "623-623",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Metopella longimana",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "798-900",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Michthyops theeli",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "314-314",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Microclymene",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "297-297",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Microcosmus glacialis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "163-736",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Microdeutopus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "172-296",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Microdeutopus anomalus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "543-543",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Micronephthys hartmannschroederae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "198-198",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Micronephthys neotena",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "372-372",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Microporella",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "63-63",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Microporella arctica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "47-90",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Microporella ciliata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "58-328",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Microporella klugei",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "61-61",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Microprotopus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "296-555",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Millericrinida",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "207-2020",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Mitrocomella polydiademata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "92-382",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Modeeria rotunda",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "222-382",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Moelleria costulata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "58-162",
            "nSamples": 18,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Mohnia dalli",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "266-1229",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Mohnia parva",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "1229-1229",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Mohnia simplex",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "114-608",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Molgula",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "128-1229",
            "nSamples": 41,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Molgula complanata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "44-750",
            "nSamples": 16,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Molgula griffithsii",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "61-244",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Molgula herdmani",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "562-562",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Molgula siphonalis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "67-626",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Molgulidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "67-2354",
            "nSamples": 12,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Molpadia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "303-814",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Molva dypterygia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "211-248",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Monstrillidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "50-225",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Montacuta spitzbergensis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "63-209",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Montacutinae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "105-500",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Munididae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "281-993",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Munidopsidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "501-501",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Munidopsis serricornis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "183-184",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Solariella varicosa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "86-203",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Solasteridae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "155-707",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Spatangoidea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "271-380",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Spectrarcturus hystrix",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "417-779",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Sphaerephesia philippi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "458-458",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Sphaerodoridium balticum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "67-67",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Sphaerosyllis hystrix",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "622-622",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Sphaerosyllis taylori",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "240-240",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Sphaerotylus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "390-390",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Tethya",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "270-281",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Tethya norvegica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "147-380",
            "nSamples": 13,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Tetilla",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "236-412",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Tetractinellida",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "270-270",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Tharyx maryae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "144-809",
            "nSamples": 13,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Tharyx robustus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "796-796",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thelepus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "57-658",
            "nSamples": 29,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thelepus davehalli",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "333-333",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thelepus marthae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "67-814",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Themisto libellula",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "205-1229",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thenea abyssorum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "864-2597",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thenea levis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "199-687",
            "nSamples": 34,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thenea muricata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "180-622",
            "nSamples": 57,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thenea valdiviae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "190-875",
            "nSamples": 26,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thesbia nana",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "68-188",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thoracica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "147-175",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thracia gracilis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "92-136",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thracia myopsis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "58-501",
            "nSamples": 46,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thracia phaseolina",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "136-167",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thrombus abyssi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "239-239",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thuiaria arctica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "61-61",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thuiaria articulata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "105-875",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thuiaria breitfussi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "44-304",
            "nSamples": 32,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thuiaria carica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "82-392",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thuiaria laxa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "208-208",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thuiaria obsoleta",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "59-82",
            "nSamples": 5,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thyasira biplicata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "194-194",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thysanoessa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "476-918",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thysanoessa inermis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "147-147",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Thysanoessa raschii",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "553-1608",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Tiron",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "128-185",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Tmetonyx norbiensis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "323-323",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Tubificinae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "67-67",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Tubificoides",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "603-659",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Tubularia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "353-402",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Tubulariidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "44-75",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Tubulipora",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "82-328",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Turbicellepora",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "171-171",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Turbicellepora avicularis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "158-280",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Turbicellepora nodulosa",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "171-171",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Turridae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "305-650",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Turritellinella tricarinata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "157-157",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Turritellopsis stimpsoni",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "171-171",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Tylobranchion nordgaardi",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "225-490",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Typhlotanais",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "219-1118",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Typhlotanais aequiremis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "240-300",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Typhlotanais tenuicornis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "182-182",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Tytthocope",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "304-304",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ulosa digitata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "189-189",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Umbellula encrinus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "1189-1189",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Umbonula patens",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "61-61",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Umbrina",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "338-338",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Unciola crassipes",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "658-850",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Unciolinae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "297-297",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Urothoidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "176-176",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Urticina",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "46-63",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Ute gladiata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "119-421",
            "nSamples": 25,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Valvatida",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "214-214",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Valvifera",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "993-993",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Varicorbula gibba",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "157-268",
            "nSamples": 6,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Velatida",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "349-814",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Velutinidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "105-419",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Venus casina",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "157-157",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Verruca stroemia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "145-384",
            "nSamples": 7,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Verrucidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "95-118",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Verrucomorpha",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "91-178",
            "nSamples": 2,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Virgularia tuberculata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "277-277",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Virgulariidae",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "105-264",
            "nSamples": 4,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Volutomitra groenlandica",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "380-380",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Weltnerium cornutum",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "419-755",
            "nSamples": 8,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Westwoodilla rectirostris",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "356-356",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Whoia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "1712-1712",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Xylophaga dorsalis",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "209-249",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Yoldia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "439-439",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Yoldia hyperborea",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "77-298",
            "nSamples": 9,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Yoldiella frigida",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "114-392",
            "nSamples": 93,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Yoldiella intermedia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "82-875",
            "nSamples": 212,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Yoldiella lenticula",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "68-500",
            "nSamples": 164,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Zatsepinia",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "259-259",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Zeugopterus norvegicus",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "95-168",
            "nSamples": 3,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Zygophylax brownei",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "875-875",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          },
          {
            "scientificName": "Zygophylax pinnata",
            "density_kg_m2": 0.0,
            "habitat": "unclassified",
            "depthBand_m": "679-679",
            "nSamples": 1,
            "observedMeanDensity_kg_m2": 0.0
          }
        ],
        "aggregateDensity_kg_m2": 250.59523375,
        "provenance": {
          "values": "mixed",
          "retrievalApiCall": "https://marbunn-ekstern.hi.no/apps/marbunn/v1/getmapforcatch?species={value}&cruise={cruise}",
          "verifiedOn": "2026-05-26",
          "primarySource": {
            "name": "MAREANO Marbunn",
            "api": "https://marbunn-ekstern.hi.no/apps/marbunn/v1/",
            "speciesListEndpoint": "https://marbunn-ekstern.hi.no/apps/marbunn/v1/catchspecies",
            "perSpeciesEndpoint": "https://marbunn-ekstern.hi.no/apps/marbunn/v1/getmapforcatch?species={value}&cruise={cruise}",
            "license": "CC BY 4.0 / NLOD"
          },
          "nearestAuthoritativeSource": {
            "url": "https://mareano.no/",
            "note": "Raw observations come from IMR / MAREANO Marbunn catch-sample point features."
          },
          "verificationGap": "Source observations provide catch weight in kg. The target block requires kg m-2. This transform first uses per-gear sampled-area assumptions rather than authoritative cruise-level swept-area metadata, then extrapolates point densities with IDW. Ordinary Kriging or Regression-Kriging would be preferable once variograms, environmental covariates and geostatistical dependencies are available.",
          "note": "Transformed 24881 source features into 1000 per-taxon rows. Ignored 0 malformed or unnamed features. IDW grid=25x25, power=2.0, weighted samples=5396, samples using fallback area=0. Gear-area assumptions m2: {\"Beamtrawl\": 100.0, \"Bioboks\": 0.1, \"Boxcorer\": 0.1, \"Large VV grab\": 0.25, \"RP-sledge\": 50.0, \"Small VV grab\": 0.1, \"VVgrab020\": 0.2, \"Videograb\": 0.1}; fallback=0.1. Source fetched_utc=2026-05-26T11:26:16Z."
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
      "rel": "derivedFrom",
      "href": "bblocks://ogc.hosted.seadots.benthic-biomass-observations-imr",
      "type": "application/schema+json",
      "title": "IMR Benthic Biomass Observations bblock"
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


### MAREANO benthic biomass density proxy — OBIS checklist
#### json
```json
{
  "id": "https://example.org/norwegian-ses/benthic-biomass-density-mareano/obis-checklist-proxy",
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
    "title": "MAREANO benthic biomass density proxy from OBIS checklist",
    "description": "Occurrence-weighted proxy derived from OBIS records for selected MAREANO datasets. OBIS records do not provide biomass, sampled area or station geometry; this output is a schema-compatible proxy, not a physical biomass-density measurement.",
    "created": "2026-05-26",
    "updated": "2026-05-26",
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
      "OBIS",
      "MAREANO",
      "occurrence",
      "benthic biomass",
      "proxy"
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
      "name": "OBIS occurrence proxy for MAREANO benthic biomass density",
      "description": "Per-taxon normalized OBIS occurrence records carried as a density proxy.",
      "role": "primary baseline proxy",
      "source": "https://api.obis.org/v3/checklist?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b",
      "format": "application/json",
      "vocabularyTerm": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano",
      "observedProperty": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano",
      "phenomenonTime": "unknown",
      "data": {
        "units": "dimensionless occurrence share encoded in kg m-2 field",
        "samplePeriod": "unknown",
        "samplingProgramme": "OBIS / MAREANO",
        "perTaxon": [
          {
            "scientificName": "Sipuncula",
            "density_kg_m2": 0.1095726904,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 459,
            "obisRecords": 459,
            "taxonRank": "Order",
            "aphiaID": 1268
          },
          {
            "scientificName": "Amphipoda",
            "density_kg_m2": 0.1079016472,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 452,
            "obisRecords": 452,
            "taxonRank": "Order",
            "aphiaID": 1135
          },
          {
            "scientificName": "Aphelochaeta",
            "density_kg_m2": 0.103127238,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 432,
            "obisRecords": 432,
            "taxonRank": "Genus",
            "aphiaID": 129240
          },
          {
            "scientificName": "Hydrozoa",
            "density_kg_m2": 0.1024110766,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 429,
            "obisRecords": 429,
            "taxonRank": "Class",
            "aphiaID": 1337
          },
          {
            "scientificName": "Oedicerotidae",
            "density_kg_m2": 0.0995464311,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 417,
            "obisRecords": 417,
            "taxonRank": "Family",
            "aphiaID": 101400
          },
          {
            "scientificName": "Notomastus latericeus",
            "density_kg_m2": 0.0985915493,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 413,
            "obisRecords": 413,
            "taxonRank": "Species",
            "aphiaID": 129898
          },
          {
            "scientificName": "Cephalaspidea",
            "density_kg_m2": 0.0978753879,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 410,
            "obisRecords": 410,
            "taxonRank": "Order",
            "aphiaID": 154
          },
          {
            "scientificName": "Harpinia",
            "density_kg_m2": 0.0962043447,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 403,
            "obisRecords": 403,
            "taxonRank": "Genus",
            "aphiaID": 101716
          },
          {
            "scientificName": "Astarte sulcata",
            "density_kg_m2": 0.0926235378,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 388,
            "obisRecords": 388,
            "taxonRank": "Species",
            "aphiaID": 138824
          },
          {
            "scientificName": "Chone",
            "density_kg_m2": 0.0921460969,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 386,
            "obisRecords": 386,
            "taxonRank": "Genus",
            "aphiaID": 129525
          }
        ],
        "aggregateDensity_kg_m2": 0.9999999999,
        "observationOutputs": [],
        "provenance": {
          "values": "mixed",
          "retrievalApiCall": "https://api.obis.org/v3/checklist?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b",
          "verifiedOn": "2026-05-26",
          "primarySource": {
            "name": "OBIS checklist API",
            "url": "https://api.obis.org/v3/checklist?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b"
          },
          "nearestAuthoritativeSource": {
            "url": "https://obis.org/",
            "note": "OBIS occurrence/checklist endpoints for selected MAREANO dataset identifiers."
          },
          "verificationGap": "The source OBIS response contains occurrence records or occurrence record counts. It does not contain biomass, sampled area, station effort or physical density measurements. `density_kg_m2` is therefore a normalized occurrence-count proxy for testing target bblock interoperability.",
          "note": "Transformed 10 OBIS checklist rows from a response with total=3196 into a MAREANO biomass-density proxy example. Proxy density is records / sum(records in this page); aggregate=0.9999999999."
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
      "rel": "derivedFrom",
      "href": "bblocks://ogc.hosted.seadots.obis-mareano-checklist",
      "type": "application/schema+json",
      "title": "OBIS MAREANO Checklist bblock"
    },
    {
      "rel": "cite-as",
      "href": "https://obis.org/",
      "title": "OBIS"
    },
    {
      "rel": "cite-as",
      "href": "https://mareano.no/",
      "title": "MAREANO programme"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/benthic-biomass-density-mareano/context.jsonld",
  "id": "https://example.org/norwegian-ses/benthic-biomass-density-mareano/obis-checklist-proxy",
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
    "title": "MAREANO benthic biomass density proxy from OBIS checklist",
    "description": "Occurrence-weighted proxy derived from OBIS records for selected MAREANO datasets. OBIS records do not provide biomass, sampled area or station geometry; this output is a schema-compatible proxy, not a physical biomass-density measurement.",
    "created": "2026-05-26",
    "updated": "2026-05-26",
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
      "OBIS",
      "MAREANO",
      "occurrence",
      "benthic biomass",
      "proxy"
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
      "name": "OBIS occurrence proxy for MAREANO benthic biomass density",
      "description": "Per-taxon normalized OBIS occurrence records carried as a density proxy.",
      "role": "primary baseline proxy",
      "source": "https://api.obis.org/v3/checklist?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b",
      "format": "application/json",
      "vocabularyTerm": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano",
      "observedProperty": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano",
      "phenomenonTime": "unknown",
      "data": {
        "units": "dimensionless occurrence share encoded in kg m-2 field",
        "samplePeriod": "unknown",
        "samplingProgramme": "OBIS / MAREANO",
        "perTaxon": [
          {
            "scientificName": "Sipuncula",
            "density_kg_m2": 0.1095726904,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 459,
            "obisRecords": 459,
            "taxonRank": "Order",
            "aphiaID": 1268
          },
          {
            "scientificName": "Amphipoda",
            "density_kg_m2": 0.1079016472,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 452,
            "obisRecords": 452,
            "taxonRank": "Order",
            "aphiaID": 1135
          },
          {
            "scientificName": "Aphelochaeta",
            "density_kg_m2": 0.103127238,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 432,
            "obisRecords": 432,
            "taxonRank": "Genus",
            "aphiaID": 129240
          },
          {
            "scientificName": "Hydrozoa",
            "density_kg_m2": 0.1024110766,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 429,
            "obisRecords": 429,
            "taxonRank": "Class",
            "aphiaID": 1337
          },
          {
            "scientificName": "Oedicerotidae",
            "density_kg_m2": 0.0995464311,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 417,
            "obisRecords": 417,
            "taxonRank": "Family",
            "aphiaID": 101400
          },
          {
            "scientificName": "Notomastus latericeus",
            "density_kg_m2": 0.0985915493,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 413,
            "obisRecords": 413,
            "taxonRank": "Species",
            "aphiaID": 129898
          },
          {
            "scientificName": "Cephalaspidea",
            "density_kg_m2": 0.0978753879,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 410,
            "obisRecords": 410,
            "taxonRank": "Order",
            "aphiaID": 154
          },
          {
            "scientificName": "Harpinia",
            "density_kg_m2": 0.0962043447,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 403,
            "obisRecords": 403,
            "taxonRank": "Genus",
            "aphiaID": 101716
          },
          {
            "scientificName": "Astarte sulcata",
            "density_kg_m2": 0.0926235378,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 388,
            "obisRecords": 388,
            "taxonRank": "Species",
            "aphiaID": 138824
          },
          {
            "scientificName": "Chone",
            "density_kg_m2": 0.0921460969,
            "habitat": "marine benthic checklist taxon",
            "depthBand_m": "unknown",
            "nSamples": 386,
            "obisRecords": 386,
            "taxonRank": "Genus",
            "aphiaID": 129525
          }
        ],
        "aggregateDensity_kg_m2": 0.9999999999,
        "observationOutputs": [],
        "provenance": {
          "values": "mixed",
          "retrievalApiCall": "https://api.obis.org/v3/checklist?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b",
          "verifiedOn": "2026-05-26",
          "primarySource": {
            "name": "OBIS checklist API",
            "url": "https://api.obis.org/v3/checklist?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b"
          },
          "nearestAuthoritativeSource": {
            "url": "https://obis.org/",
            "note": "OBIS occurrence/checklist endpoints for selected MAREANO dataset identifiers."
          },
          "verificationGap": "The source OBIS response contains occurrence records or occurrence record counts. It does not contain biomass, sampled area, station effort or physical density measurements. `density_kg_m2` is therefore a normalized occurrence-count proxy for testing target bblock interoperability.",
          "note": "Transformed 10 OBIS checklist rows from a response with total=3196 into a MAREANO biomass-density proxy example. Proxy density is records / sum(records in this page); aggregate=0.9999999999."
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
      "rel": "derivedFrom",
      "href": "bblocks://ogc.hosted.seadots.obis-mareano-checklist",
      "type": "application/schema+json",
      "title": "OBIS MAREANO Checklist bblock"
    },
    {
      "rel": "cite-as",
      "href": "https://obis.org/",
      "title": "OBIS"
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
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/norwegian-ses/benthic-biomass-density-mareano/obis-checklist-proxy> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "OBIS" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://obis.org/> ],
        [ rdfs:label "OBIS MAREANO Checklist bblock" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/derivedFrom> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.obis-mareano-checklist> ],
        [ rdfs:label "MAREANO Benthic Biomass Density Observation bblock" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.benthic-biomass-density-mareano> ],
        [ rdfs:label "MAREANO programme" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://mareano.no/> ] ;
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
            dcterms:title "MAREANO benthic biomass density proxy from OBIS checklist" ;
            dcat:keyword "MAREANO",
                "OBIS",
                "benthic biomass",
                "occurrence",
                "proxy" ;
            dcat:theme [ skos:Concept <file:///github/workspace/benthic-biomass> ;
                    skos:inScheme "https://id3.seadots.eu/themes" ] ;
            seadots:benthicBiomassDensity [ dcterms:description "Per-taxon normalized OBIS occurrence records carried as a density proxy." ;
                    dcterms:format "application/json" ;
                    dcterms:title "OBIS occurrence proxy for MAREANO benthic biomass density" ;
                    skos:exactMatch indo:benthic-biomass-density-mareano ;
                    dcat:accessURL <https://api.obis.org/v3/checklist?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b> ;
                    sosa:observedProperty indo:benthic-biomass-density-mareano ;
                    sosa:phenomenonTime <file:///github/workspace/unknown> ;
                    seadots:data [ dcterms:temporal "unknown" ;
                            qudt:unit "dimensionless occurrence share encoded in kg m-2 field" ;
                            prov:wasAttributedTo "OBIS / MAREANO" ;
                            prov:wasDerivedFrom [ dcterms:date "2026-05-26" ;
                                    dcterms:source [ dcterms:title "OBIS checklist API" ;
                                            seadots:url "https://api.obis.org/v3/checklist?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b" ] ;
                                    skos:note "Transformed 10 OBIS checklist rows from a response with total=3196 into a MAREANO biomass-density proxy example. Proxy density is records / sum(records in this page); aggregate=0.9999999999." ;
                                    seadots:nearestAuthoritativeSource [ skos:note "OBIS occurrence/checklist endpoints for selected MAREANO dataset identifiers." ;
                                            dcat:accessURL <https://obis.org/> ] ;
                                    seadots:provenanceValues "mixed" ;
                                    seadots:retrievalApiCall <https://api.obis.org/v3/checklist?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b> ;
                                    seadots:verificationGap "The source OBIS response contains occurrence records or occurrence record counts. It does not contain biomass, sampled area, station effort or physical density measurements. `density_kg_m2` is therefore a normalized occurrence-count proxy for testing target bblock interoperability." ] ;
                            indo:baseline-benthic-biomass-density "0.9999999999"^^qudt:QuantityValue ;
                            seadots:perTaxon [ dwc:habitat "marine benthic checklist taxon" ;
                                    dwc:sampleSizeValue 417 ;
                                    dwc:scientificName "Oedicerotidae" ;
                                    dwc:taxonID 101400 ;
                                    indo:benthic-biomass-density-mareano "0.0995464311"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "unknown" ;
                                    seadots:obisRecords 417 ;
                                    seadots:taxonRank "Family" ],
                                [ dwc:habitat "marine benthic checklist taxon" ;
                                    dwc:sampleSizeValue 386 ;
                                    dwc:scientificName "Chone" ;
                                    dwc:taxonID 129525 ;
                                    indo:benthic-biomass-density-mareano "0.0921460969"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "unknown" ;
                                    seadots:obisRecords 386 ;
                                    seadots:taxonRank "Genus" ],
                                [ dwc:habitat "marine benthic checklist taxon" ;
                                    dwc:sampleSizeValue 403 ;
                                    dwc:scientificName "Harpinia" ;
                                    dwc:taxonID 101716 ;
                                    indo:benthic-biomass-density-mareano "0.0962043447"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "unknown" ;
                                    seadots:obisRecords 403 ;
                                    seadots:taxonRank "Genus" ],
                                [ dwc:habitat "marine benthic checklist taxon" ;
                                    dwc:sampleSizeValue 413 ;
                                    dwc:scientificName "Notomastus latericeus" ;
                                    dwc:taxonID 129898 ;
                                    indo:benthic-biomass-density-mareano "0.0985915493"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "unknown" ;
                                    seadots:obisRecords 413 ;
                                    seadots:taxonRank "Species" ],
                                [ dwc:habitat "marine benthic checklist taxon" ;
                                    dwc:sampleSizeValue 452 ;
                                    dwc:scientificName "Amphipoda" ;
                                    dwc:taxonID 1135 ;
                                    indo:benthic-biomass-density-mareano "0.1079016472"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "unknown" ;
                                    seadots:obisRecords 452 ;
                                    seadots:taxonRank "Order" ],
                                [ dwc:habitat "marine benthic checklist taxon" ;
                                    dwc:sampleSizeValue 410 ;
                                    dwc:scientificName "Cephalaspidea" ;
                                    dwc:taxonID 154 ;
                                    indo:benthic-biomass-density-mareano "0.0978753879"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "unknown" ;
                                    seadots:obisRecords 410 ;
                                    seadots:taxonRank "Order" ],
                                [ dwc:habitat "marine benthic checklist taxon" ;
                                    dwc:sampleSizeValue 388 ;
                                    dwc:scientificName "Astarte sulcata" ;
                                    dwc:taxonID 138824 ;
                                    indo:benthic-biomass-density-mareano "0.0926235378"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "unknown" ;
                                    seadots:obisRecords 388 ;
                                    seadots:taxonRank "Species" ],
                                [ dwc:habitat "marine benthic checklist taxon" ;
                                    dwc:sampleSizeValue 429 ;
                                    dwc:scientificName "Hydrozoa" ;
                                    dwc:taxonID 1337 ;
                                    indo:benthic-biomass-density-mareano "0.1024110766"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "unknown" ;
                                    seadots:obisRecords 429 ;
                                    seadots:taxonRank "Class" ],
                                [ dwc:habitat "marine benthic checklist taxon" ;
                                    dwc:sampleSizeValue 459 ;
                                    dwc:scientificName "Sipuncula" ;
                                    dwc:taxonID 1268 ;
                                    indo:benthic-biomass-density-mareano "0.1095726904"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "unknown" ;
                                    seadots:obisRecords 459 ;
                                    seadots:taxonRank "Order" ],
                                [ dwc:habitat "marine benthic checklist taxon" ;
                                    dwc:sampleSizeValue 432 ;
                                    dwc:scientificName "Aphelochaeta" ;
                                    dwc:taxonID 129240 ;
                                    indo:benthic-biomass-density-mareano "0.103127238"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "unknown" ;
                                    seadots:obisRecords 432 ;
                                    seadots:taxonRank "Genus" ] ] ;
                    seadots:role "primary baseline proxy" ] ;
            seadots:description "Occurrence-weighted proxy derived from OBIS records for selected MAREANO datasets. OBIS records do not provide biomass, sampled area or station geometry; this output is a schema-compatible proxy, not a physical biomass-density measurement." ] .

<file:///github/workspace/benthic-biomass> rdfs:label "Benthic biomass density" .


```


### MAREANO benthic biomass density proxy — OBIS occurrences
#### json
```json
{
  "id": "https://example.org/norwegian-ses/benthic-biomass-density-mareano/obis-occurrence-proxy",
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
    "title": "MAREANO benthic biomass density proxy from OBIS occurrence data",
    "description": "Occurrence-weighted proxy derived from OBIS records for selected MAREANO datasets. OBIS records do not provide biomass, sampled area or station geometry; this output is a schema-compatible proxy, not a physical biomass-density measurement.",
    "created": "2026-05-26",
    "updated": "2026-05-26",
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
      "OBIS",
      "MAREANO",
      "occurrence",
      "benthic biomass",
      "proxy"
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
      "name": "OBIS occurrence proxy for MAREANO benthic biomass density",
      "description": "Per-taxon normalized OBIS occurrence records carried as a density proxy.",
      "role": "primary baseline proxy",
      "source": "https://api.obis.org/v3/occurrence?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b",
      "format": "application/json",
      "vocabularyTerm": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano",
      "observedProperty": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano",
      "phenomenonTime": "unknown",
      "data": {
        "units": "dimensionless occurrence share encoded in kg m-2 field",
        "samplePeriod": "unknown",
        "samplingProgramme": "OBIS / MAREANO",
        "perTaxon": [
          {
            "scientificName": "Actaedrilus polyonyx",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 1473437
          },
          {
            "scientificName": "Brissopsis lyrifera",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 124373
          },
          {
            "scientificName": "Buccinum finmarkianum",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 160143
          },
          {
            "scientificName": "Chone",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 129525
          },
          {
            "scientificName": "Echinocucumis hispida",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 124593
          },
          {
            "scientificName": "Leucosolenida",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 131591
          },
          {
            "scientificName": "Lysianassoidea",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 176788
          },
          {
            "scientificName": "Munida sarsi",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 107163
          },
          {
            "scientificName": "Ophiuroidea",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 123084
          },
          {
            "scientificName": "Praxillura longissima",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 130327
          }
        ],
        "aggregateDensity_kg_m2": 1.0,
        "observationOutputs": [
          {
            "id": "00014e73-67d6-40ce-919f-0ca40089c1e6",
            "occurrenceID": "143680821001060",
            "scientificName": "Praxillura longissima",
            "density_kg_m2": 0.1,
            "eventDate": "2014-08-30T18:04:00+00:00/2014-08-30T18:17:00+00:00",
            "datasetName": "grab_2006-2022",
            "samplingProtocol": "Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0",
            "aphiaID": 130327,
            "decimalLongitude": 33.378167,
            "decimalLatitude": 73.130833,
            "depth_m": 228.98000000000002
          },
          {
            "id": "0001e2dc-e4c7-4fd0-9214-7c643a7d7c4a",
            "occurrenceID": "078650010010013",
            "scientificName": "Lysianassoidea",
            "density_kg_m2": 0.1,
            "eventDate": "2012-05-05T23:09:00+00:00/2012-05-05T23:24:00+00:00",
            "datasetName": "rp-sledge_2006-2022",
            "samplingProtocol": "RP-sledge,Subsample method: Decanted - Mesh size (mm): 0.5",
            "aphiaID": 176788,
            "decimalLongitude": 9.5926,
            "decimalLatitude": 67.955607,
            "depth_m": 1307.4250000000002
          },
          {
            "id": "0002100b-ad82-4d11-be10-c47f18f30c21",
            "occurrenceID": "081880066019034",
            "scientificName": "Actaedrilus polyonyx",
            "density_kg_m2": 0.1,
            "eventDate": "2012-05-04T23:33:00+00:00",
            "datasetName": "grab_2006-2022",
            "samplingProtocol": "Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0",
            "aphiaID": 1473437,
            "decimalLongitude": 9.307715,
            "decimalLatitude": 67.595283,
            "depth_m": 913.03
          },
          {
            "id": "00029056-f56d-45f4-a1db-f6bbd2350903",
            "occurrenceID": "164910018001034",
            "scientificName": "Leucosolenida",
            "density_kg_m2": 0.1,
            "eventDate": "2016-09-28T00:41:00+00:00/2016-09-28T00:46:00+00:00",
            "datasetName": "beamtrawl_2006-2022",
            "samplingProtocol": "Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0",
            "aphiaID": 131591,
            "decimalLongitude": 25.9995,
            "decimalLatitude": 74.997,
            "depth_m": 208.005
          },
          {
            "id": "0002e38c-8260-4f5d-9bc4-1895860fbcb8",
            "occurrenceID": "171710009001042",
            "scientificName": "Chone",
            "density_kg_m2": 0.1,
            "eventDate": "2017-04-06T03:41:00+00:00/2017-04-06T03:46:00+00:00",
            "datasetName": "beamtrawl_2006-2022",
            "samplingProtocol": "Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0",
            "aphiaID": 129525,
            "decimalLongitude": 23.913167,
            "decimalLatitude": 73.5475,
            "depth_m": 448.975
          },
          {
            "id": "00054ffb-17c9-46eb-9aeb-72252a6b90d8",
            "occurrenceID": "059290417049111",
            "scientificName": "Buccinum finmarkianum",
            "density_kg_m2": 0.1,
            "eventDate": "2010-08-11T00:40:00+00:00",
            "datasetName": "grab_2006-2022",
            "samplingProtocol": "VVgrab020,Subsample method: Sieve content - Mesh size (mm): 1.0",
            "aphiaID": 160143,
            "decimalLongitude": 18.704333,
            "decimalLatitude": 70.411833,
            "depth_m": 100.47
          },
          {
            "id": "0007423f-403a-44d2-9565-281acbe343ce",
            "occurrenceID": "253740119001007",
            "scientificName": "Brissopsis lyrifera",
            "density_kg_m2": 0.1,
            "eventDate": "2021-05-03T12:22:00+00:00",
            "datasetName": "grab_2006-2022",
            "samplingProtocol": "Small VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0",
            "aphiaID": 124373,
            "decimalLongitude": 1.414981,
            "decimalLatitude": 62.060718,
            "depth_m": 369.0
          },
          {
            "id": "0007ec71-87e5-4701-8474-ac409618ed43",
            "occurrenceID": "227940090001039",
            "scientificName": "Echinocucumis hispida",
            "density_kg_m2": 0.1,
            "eventDate": "2020-07-23T20:38:00+00:00",
            "datasetName": "grab_2006-2022",
            "samplingProtocol": "Small VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0",
            "aphiaID": 124593,
            "decimalLongitude": 10.611012,
            "decimalLatitude": 65.629713,
            "depth_m": 376.78
          },
          {
            "id": "00087d31-412d-48ce-bed8-9ade8d5b80f5",
            "occurrenceID": "000810008002016",
            "scientificName": "Munida sarsi",
            "density_kg_m2": 0.1,
            "eventDate": "2006-05-28T02:33:00+00:00/2006-05-28T02:39:00+00:00",
            "datasetName": "beamtrawl_2006-2022",
            "samplingProtocol": "Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0",
            "aphiaID": 107163,
            "decimalLongitude": 22.133255,
            "decimalLatitude": 71.287677,
            "depth_m": 321.15
          },
          {
            "id": "0009bf51-340c-4fa4-ba3d-ce3300291d9c",
            "occurrenceID": "000380058031020",
            "scientificName": "Ophiuroidea",
            "density_kg_m2": 0.1,
            "eventDate": "2006-06-06T00:19:00+00:00",
            "datasetName": "grab_2006-2022",
            "samplingProtocol": "Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0",
            "aphiaID": 123084,
            "decimalLongitude": 22.415298,
            "decimalLatitude": 71.329727,
            "depth_m": 434.62
          }
        ],
        "provenance": {
          "values": "mixed",
          "retrievalApiCall": "https://api.obis.org/v3/occurrence?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b",
          "verifiedOn": "2026-05-26",
          "primarySource": {
            "name": "OBIS checklist API",
            "url": "https://api.obis.org/v3/occurrence?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b"
          },
          "nearestAuthoritativeSource": {
            "url": "https://obis.org/",
            "note": "OBIS occurrence/checklist endpoints for selected MAREANO dataset identifiers."
          },
          "verificationGap": "The source OBIS response contains occurrence records or occurrence record counts. It does not contain biomass, sampled area, station effort or physical density measurements. `density_kg_m2` is therefore a normalized occurrence-count proxy for testing target bblock interoperability.",
          "note": "Transformed 10 OBIS occurrence rows from a response with total=105687 into a MAREANO biomass-density proxy example. Proxy density is occurrence count / number of occurrence rows in this page; aggregate=1.0."
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
      "rel": "derivedFrom",
      "href": "bblocks://ogc.hosted.seadots.obis-mareano-checklist",
      "type": "application/schema+json",
      "title": "OBIS MAREANO Checklist bblock"
    },
    {
      "rel": "cite-as",
      "href": "https://obis.org/",
      "title": "OBIS"
    },
    {
      "rel": "cite-as",
      "href": "https://mareano.no/",
      "title": "MAREANO programme"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/benthic-biomass-density-mareano/context.jsonld",
  "id": "https://example.org/norwegian-ses/benthic-biomass-density-mareano/obis-occurrence-proxy",
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
    "title": "MAREANO benthic biomass density proxy from OBIS occurrence data",
    "description": "Occurrence-weighted proxy derived from OBIS records for selected MAREANO datasets. OBIS records do not provide biomass, sampled area or station geometry; this output is a schema-compatible proxy, not a physical biomass-density measurement.",
    "created": "2026-05-26",
    "updated": "2026-05-26",
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
      "OBIS",
      "MAREANO",
      "occurrence",
      "benthic biomass",
      "proxy"
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
      "name": "OBIS occurrence proxy for MAREANO benthic biomass density",
      "description": "Per-taxon normalized OBIS occurrence records carried as a density proxy.",
      "role": "primary baseline proxy",
      "source": "https://api.obis.org/v3/occurrence?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b",
      "format": "application/json",
      "vocabularyTerm": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano",
      "observedProperty": "https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano",
      "phenomenonTime": "unknown",
      "data": {
        "units": "dimensionless occurrence share encoded in kg m-2 field",
        "samplePeriod": "unknown",
        "samplingProgramme": "OBIS / MAREANO",
        "perTaxon": [
          {
            "scientificName": "Actaedrilus polyonyx",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 1473437
          },
          {
            "scientificName": "Brissopsis lyrifera",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 124373
          },
          {
            "scientificName": "Buccinum finmarkianum",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 160143
          },
          {
            "scientificName": "Chone",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 129525
          },
          {
            "scientificName": "Echinocucumis hispida",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 124593
          },
          {
            "scientificName": "Leucosolenida",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 131591
          },
          {
            "scientificName": "Lysianassoidea",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 176788
          },
          {
            "scientificName": "Munida sarsi",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 107163
          },
          {
            "scientificName": "Ophiuroidea",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 123084
          },
          {
            "scientificName": "Praxillura longissima",
            "density_kg_m2": 0.1,
            "habitat": "marine benthic occurrence taxon",
            "depthBand_m": "occurrence depth varies",
            "nSamples": 1,
            "obisRecords": 1,
            "taxonRank": null,
            "aphiaID": 130327
          }
        ],
        "aggregateDensity_kg_m2": 1.0,
        "observationOutputs": [
          {
            "id": "00014e73-67d6-40ce-919f-0ca40089c1e6",
            "occurrenceID": "143680821001060",
            "scientificName": "Praxillura longissima",
            "density_kg_m2": 0.1,
            "eventDate": "2014-08-30T18:04:00+00:00/2014-08-30T18:17:00+00:00",
            "datasetName": "grab_2006-2022",
            "samplingProtocol": "Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0",
            "aphiaID": 130327,
            "decimalLongitude": 33.378167,
            "decimalLatitude": 73.130833,
            "depth_m": 228.98000000000002
          },
          {
            "id": "0001e2dc-e4c7-4fd0-9214-7c643a7d7c4a",
            "occurrenceID": "078650010010013",
            "scientificName": "Lysianassoidea",
            "density_kg_m2": 0.1,
            "eventDate": "2012-05-05T23:09:00+00:00/2012-05-05T23:24:00+00:00",
            "datasetName": "rp-sledge_2006-2022",
            "samplingProtocol": "RP-sledge,Subsample method: Decanted - Mesh size (mm): 0.5",
            "aphiaID": 176788,
            "decimalLongitude": 9.5926,
            "decimalLatitude": 67.955607,
            "depth_m": 1307.4250000000002
          },
          {
            "id": "0002100b-ad82-4d11-be10-c47f18f30c21",
            "occurrenceID": "081880066019034",
            "scientificName": "Actaedrilus polyonyx",
            "density_kg_m2": 0.1,
            "eventDate": "2012-05-04T23:33:00+00:00",
            "datasetName": "grab_2006-2022",
            "samplingProtocol": "Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0",
            "aphiaID": 1473437,
            "decimalLongitude": 9.307715,
            "decimalLatitude": 67.595283,
            "depth_m": 913.03
          },
          {
            "id": "00029056-f56d-45f4-a1db-f6bbd2350903",
            "occurrenceID": "164910018001034",
            "scientificName": "Leucosolenida",
            "density_kg_m2": 0.1,
            "eventDate": "2016-09-28T00:41:00+00:00/2016-09-28T00:46:00+00:00",
            "datasetName": "beamtrawl_2006-2022",
            "samplingProtocol": "Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0",
            "aphiaID": 131591,
            "decimalLongitude": 25.9995,
            "decimalLatitude": 74.997,
            "depth_m": 208.005
          },
          {
            "id": "0002e38c-8260-4f5d-9bc4-1895860fbcb8",
            "occurrenceID": "171710009001042",
            "scientificName": "Chone",
            "density_kg_m2": 0.1,
            "eventDate": "2017-04-06T03:41:00+00:00/2017-04-06T03:46:00+00:00",
            "datasetName": "beamtrawl_2006-2022",
            "samplingProtocol": "Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0",
            "aphiaID": 129525,
            "decimalLongitude": 23.913167,
            "decimalLatitude": 73.5475,
            "depth_m": 448.975
          },
          {
            "id": "00054ffb-17c9-46eb-9aeb-72252a6b90d8",
            "occurrenceID": "059290417049111",
            "scientificName": "Buccinum finmarkianum",
            "density_kg_m2": 0.1,
            "eventDate": "2010-08-11T00:40:00+00:00",
            "datasetName": "grab_2006-2022",
            "samplingProtocol": "VVgrab020,Subsample method: Sieve content - Mesh size (mm): 1.0",
            "aphiaID": 160143,
            "decimalLongitude": 18.704333,
            "decimalLatitude": 70.411833,
            "depth_m": 100.47
          },
          {
            "id": "0007423f-403a-44d2-9565-281acbe343ce",
            "occurrenceID": "253740119001007",
            "scientificName": "Brissopsis lyrifera",
            "density_kg_m2": 0.1,
            "eventDate": "2021-05-03T12:22:00+00:00",
            "datasetName": "grab_2006-2022",
            "samplingProtocol": "Small VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0",
            "aphiaID": 124373,
            "decimalLongitude": 1.414981,
            "decimalLatitude": 62.060718,
            "depth_m": 369.0
          },
          {
            "id": "0007ec71-87e5-4701-8474-ac409618ed43",
            "occurrenceID": "227940090001039",
            "scientificName": "Echinocucumis hispida",
            "density_kg_m2": 0.1,
            "eventDate": "2020-07-23T20:38:00+00:00",
            "datasetName": "grab_2006-2022",
            "samplingProtocol": "Small VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0",
            "aphiaID": 124593,
            "decimalLongitude": 10.611012,
            "decimalLatitude": 65.629713,
            "depth_m": 376.78
          },
          {
            "id": "00087d31-412d-48ce-bed8-9ade8d5b80f5",
            "occurrenceID": "000810008002016",
            "scientificName": "Munida sarsi",
            "density_kg_m2": 0.1,
            "eventDate": "2006-05-28T02:33:00+00:00/2006-05-28T02:39:00+00:00",
            "datasetName": "beamtrawl_2006-2022",
            "samplingProtocol": "Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0",
            "aphiaID": 107163,
            "decimalLongitude": 22.133255,
            "decimalLatitude": 71.287677,
            "depth_m": 321.15
          },
          {
            "id": "0009bf51-340c-4fa4-ba3d-ce3300291d9c",
            "occurrenceID": "000380058031020",
            "scientificName": "Ophiuroidea",
            "density_kg_m2": 0.1,
            "eventDate": "2006-06-06T00:19:00+00:00",
            "datasetName": "grab_2006-2022",
            "samplingProtocol": "Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0",
            "aphiaID": 123084,
            "decimalLongitude": 22.415298,
            "decimalLatitude": 71.329727,
            "depth_m": 434.62
          }
        ],
        "provenance": {
          "values": "mixed",
          "retrievalApiCall": "https://api.obis.org/v3/occurrence?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b",
          "verifiedOn": "2026-05-26",
          "primarySource": {
            "name": "OBIS checklist API",
            "url": "https://api.obis.org/v3/occurrence?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b"
          },
          "nearestAuthoritativeSource": {
            "url": "https://obis.org/",
            "note": "OBIS occurrence/checklist endpoints for selected MAREANO dataset identifiers."
          },
          "verificationGap": "The source OBIS response contains occurrence records or occurrence record counts. It does not contain biomass, sampled area, station effort or physical density measurements. `density_kg_m2` is therefore a normalized occurrence-count proxy for testing target bblock interoperability.",
          "note": "Transformed 10 OBIS occurrence rows from a response with total=105687 into a MAREANO biomass-density proxy example. Proxy density is occurrence count / number of occurrence rows in this page; aggregate=1.0."
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
      "rel": "derivedFrom",
      "href": "bblocks://ogc.hosted.seadots.obis-mareano-checklist",
      "type": "application/schema+json",
      "title": "OBIS MAREANO Checklist bblock"
    },
    {
      "rel": "cite-as",
      "href": "https://obis.org/",
      "title": "OBIS"
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
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/norwegian-ses/benthic-biomass-density-mareano/obis-occurrence-proxy> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "MAREANO programme" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://mareano.no/> ],
        [ rdfs:label "OBIS" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://obis.org/> ],
        [ rdfs:label "OBIS MAREANO Checklist bblock" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/derivedFrom> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.obis-mareano-checklist> ],
        [ rdfs:label "MAREANO Benthic Biomass Density Observation bblock" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.benthic-biomass-density-mareano> ] ;
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
            dcterms:title "MAREANO benthic biomass density proxy from OBIS occurrence data" ;
            dcat:keyword "MAREANO",
                "OBIS",
                "benthic biomass",
                "occurrence",
                "proxy" ;
            dcat:theme [ skos:Concept <file:///github/workspace/benthic-biomass> ;
                    skos:inScheme "https://id3.seadots.eu/themes" ] ;
            seadots:benthicBiomassDensity [ dcterms:description "Per-taxon normalized OBIS occurrence records carried as a density proxy." ;
                    dcterms:format "application/json" ;
                    dcterms:title "OBIS occurrence proxy for MAREANO benthic biomass density" ;
                    skos:exactMatch indo:benthic-biomass-density-mareano ;
                    dcat:accessURL <https://api.obis.org/v3/occurrence?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b> ;
                    sosa:observedProperty indo:benthic-biomass-density-mareano ;
                    sosa:phenomenonTime <file:///github/workspace/unknown> ;
                    seadots:data [ dcterms:temporal "unknown" ;
                            qudt:unit "dimensionless occurrence share encoded in kg m-2 field" ;
                            prov:wasAttributedTo "OBIS / MAREANO" ;
                            prov:wasDerivedFrom [ dcterms:date "2026-05-26" ;
                                    dcterms:source [ dcterms:title "OBIS checklist API" ;
                                            seadots:url "https://api.obis.org/v3/occurrence?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b" ] ;
                                    skos:note "Transformed 10 OBIS occurrence rows from a response with total=105687 into a MAREANO biomass-density proxy example. Proxy density is occurrence count / number of occurrence rows in this page; aggregate=1.0." ;
                                    seadots:nearestAuthoritativeSource [ skos:note "OBIS occurrence/checklist endpoints for selected MAREANO dataset identifiers." ;
                                            dcat:accessURL <https://obis.org/> ] ;
                                    seadots:provenanceValues "mixed" ;
                                    seadots:retrievalApiCall <https://api.obis.org/v3/occurrence?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b> ;
                                    seadots:verificationGap "The source OBIS response contains occurrence records or occurrence record counts. It does not contain biomass, sampled area, station effort or physical density measurements. `density_kg_m2` is therefore a normalized occurrence-count proxy for testing target bblock interoperability." ] ;
                            indo:baseline-benthic-biomass-density "1.0"^^qudt:QuantityValue ;
                            seadots:observationOutputs <file:///github/workspace/00014e73-67d6-40ce-919f-0ca40089c1e6>,
                                <file:///github/workspace/0001e2dc-e4c7-4fd0-9214-7c643a7d7c4a>,
                                <file:///github/workspace/0002100b-ad82-4d11-be10-c47f18f30c21>,
                                <file:///github/workspace/00029056-f56d-45f4-a1db-f6bbd2350903>,
                                <file:///github/workspace/0002e38c-8260-4f5d-9bc4-1895860fbcb8>,
                                <file:///github/workspace/00054ffb-17c9-46eb-9aeb-72252a6b90d8>,
                                <file:///github/workspace/0007423f-403a-44d2-9565-281acbe343ce>,
                                <file:///github/workspace/0007ec71-87e5-4701-8474-ac409618ed43>,
                                <file:///github/workspace/00087d31-412d-48ce-bed8-9ade8d5b80f5>,
                                <file:///github/workspace/0009bf51-340c-4fa4-ba3d-ce3300291d9c> ;
                            seadots:perTaxon [ dwc:habitat "marine benthic occurrence taxon" ;
                                    dwc:sampleSizeValue 1 ;
                                    dwc:scientificName "Lysianassoidea" ;
                                    dwc:taxonID 176788 ;
                                    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "occurrence depth varies" ;
                                    seadots:obisRecords 1 ],
                                [ dwc:habitat "marine benthic occurrence taxon" ;
                                    dwc:sampleSizeValue 1 ;
                                    dwc:scientificName "Echinocucumis hispida" ;
                                    dwc:taxonID 124593 ;
                                    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "occurrence depth varies" ;
                                    seadots:obisRecords 1 ],
                                [ dwc:habitat "marine benthic occurrence taxon" ;
                                    dwc:sampleSizeValue 1 ;
                                    dwc:scientificName "Ophiuroidea" ;
                                    dwc:taxonID 123084 ;
                                    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "occurrence depth varies" ;
                                    seadots:obisRecords 1 ],
                                [ dwc:habitat "marine benthic occurrence taxon" ;
                                    dwc:sampleSizeValue 1 ;
                                    dwc:scientificName "Chone" ;
                                    dwc:taxonID 129525 ;
                                    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "occurrence depth varies" ;
                                    seadots:obisRecords 1 ],
                                [ dwc:habitat "marine benthic occurrence taxon" ;
                                    dwc:sampleSizeValue 1 ;
                                    dwc:scientificName "Munida sarsi" ;
                                    dwc:taxonID 107163 ;
                                    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "occurrence depth varies" ;
                                    seadots:obisRecords 1 ],
                                [ dwc:habitat "marine benthic occurrence taxon" ;
                                    dwc:sampleSizeValue 1 ;
                                    dwc:scientificName "Praxillura longissima" ;
                                    dwc:taxonID 130327 ;
                                    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "occurrence depth varies" ;
                                    seadots:obisRecords 1 ],
                                [ dwc:habitat "marine benthic occurrence taxon" ;
                                    dwc:sampleSizeValue 1 ;
                                    dwc:scientificName "Leucosolenida" ;
                                    dwc:taxonID 131591 ;
                                    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "occurrence depth varies" ;
                                    seadots:obisRecords 1 ],
                                [ dwc:habitat "marine benthic occurrence taxon" ;
                                    dwc:sampleSizeValue 1 ;
                                    dwc:scientificName "Actaedrilus polyonyx" ;
                                    dwc:taxonID 1473437 ;
                                    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "occurrence depth varies" ;
                                    seadots:obisRecords 1 ],
                                [ dwc:habitat "marine benthic occurrence taxon" ;
                                    dwc:sampleSizeValue 1 ;
                                    dwc:scientificName "Buccinum finmarkianum" ;
                                    dwc:taxonID 160143 ;
                                    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "occurrence depth varies" ;
                                    seadots:obisRecords 1 ],
                                [ dwc:habitat "marine benthic occurrence taxon" ;
                                    dwc:sampleSizeValue 1 ;
                                    dwc:scientificName "Brissopsis lyrifera" ;
                                    dwc:taxonID 124373 ;
                                    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue ;
                                    seadots:depthBand_m "occurrence depth varies" ;
                                    seadots:obisRecords 1 ] ] ;
                    seadots:role "primary baseline proxy" ] ;
            seadots:description "Occurrence-weighted proxy derived from OBIS records for selected MAREANO datasets. OBIS records do not provide biomass, sampled area or station geometry; this output is a schema-compatible proxy, not a physical biomass-density measurement." ] .

<file:///github/workspace/00014e73-67d6-40ce-919f-0ca40089c1e6> dcterms:title "grab_2006-2022" ;
    dwc:decimalLatitude 7.313083e+01 ;
    dwc:decimalLongitude 3.337817e+01 ;
    dwc:eventDate "2014-08-30T18:04:00+00:00/2014-08-30T18:17:00+00:00" ;
    dwc:minimumDepthInMeters 2.2898e+02 ;
    dwc:occurrenceID "143680821001060" ;
    dwc:samplingProtocol "Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0" ;
    dwc:scientificName "Praxillura longissima" ;
    dwc:taxonID 130327 ;
    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue .

<file:///github/workspace/0001e2dc-e4c7-4fd0-9214-7c643a7d7c4a> dcterms:title "rp-sledge_2006-2022" ;
    dwc:decimalLatitude 6.795561e+01 ;
    dwc:decimalLongitude 9.5926e+00 ;
    dwc:eventDate "2012-05-05T23:09:00+00:00/2012-05-05T23:24:00+00:00" ;
    dwc:minimumDepthInMeters 1.307425e+03 ;
    dwc:occurrenceID "078650010010013" ;
    dwc:samplingProtocol "RP-sledge,Subsample method: Decanted - Mesh size (mm): 0.5" ;
    dwc:scientificName "Lysianassoidea" ;
    dwc:taxonID 176788 ;
    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue .

<file:///github/workspace/0002100b-ad82-4d11-be10-c47f18f30c21> dcterms:title "grab_2006-2022" ;
    dwc:decimalLatitude 6.759528e+01 ;
    dwc:decimalLongitude 9.307715e+00 ;
    dwc:eventDate "2012-05-04T23:33:00+00:00" ;
    dwc:minimumDepthInMeters 9.1303e+02 ;
    dwc:occurrenceID "081880066019034" ;
    dwc:samplingProtocol "Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0" ;
    dwc:scientificName "Actaedrilus polyonyx" ;
    dwc:taxonID 1473437 ;
    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue .

<file:///github/workspace/00029056-f56d-45f4-a1db-f6bbd2350903> dcterms:title "beamtrawl_2006-2022" ;
    dwc:decimalLatitude 7.4997e+01 ;
    dwc:decimalLongitude 2.59995e+01 ;
    dwc:eventDate "2016-09-28T00:41:00+00:00/2016-09-28T00:46:00+00:00" ;
    dwc:minimumDepthInMeters 2.08005e+02 ;
    dwc:occurrenceID "164910018001034" ;
    dwc:samplingProtocol "Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0" ;
    dwc:scientificName "Leucosolenida" ;
    dwc:taxonID 131591 ;
    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue .

<file:///github/workspace/0002e38c-8260-4f5d-9bc4-1895860fbcb8> dcterms:title "beamtrawl_2006-2022" ;
    dwc:decimalLatitude 7.35475e+01 ;
    dwc:decimalLongitude 2.391317e+01 ;
    dwc:eventDate "2017-04-06T03:41:00+00:00/2017-04-06T03:46:00+00:00" ;
    dwc:minimumDepthInMeters 4.48975e+02 ;
    dwc:occurrenceID "171710009001042" ;
    dwc:samplingProtocol "Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0" ;
    dwc:scientificName "Chone" ;
    dwc:taxonID 129525 ;
    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue .

<file:///github/workspace/00054ffb-17c9-46eb-9aeb-72252a6b90d8> dcterms:title "grab_2006-2022" ;
    dwc:decimalLatitude 7.041183e+01 ;
    dwc:decimalLongitude 1.870433e+01 ;
    dwc:eventDate "2010-08-11T00:40:00+00:00" ;
    dwc:minimumDepthInMeters 1.0047e+02 ;
    dwc:occurrenceID "059290417049111" ;
    dwc:samplingProtocol "VVgrab020,Subsample method: Sieve content - Mesh size (mm): 1.0" ;
    dwc:scientificName "Buccinum finmarkianum" ;
    dwc:taxonID 160143 ;
    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue .

<file:///github/workspace/0007423f-403a-44d2-9565-281acbe343ce> dcterms:title "grab_2006-2022" ;
    dwc:decimalLatitude 6.206072e+01 ;
    dwc:decimalLongitude 1.414981e+00 ;
    dwc:eventDate "2021-05-03T12:22:00+00:00" ;
    dwc:minimumDepthInMeters 3.69e+02 ;
    dwc:occurrenceID "253740119001007" ;
    dwc:samplingProtocol "Small VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0" ;
    dwc:scientificName "Brissopsis lyrifera" ;
    dwc:taxonID 124373 ;
    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue .

<file:///github/workspace/0007ec71-87e5-4701-8474-ac409618ed43> dcterms:title "grab_2006-2022" ;
    dwc:decimalLatitude 6.562971e+01 ;
    dwc:decimalLongitude 1.061101e+01 ;
    dwc:eventDate "2020-07-23T20:38:00+00:00" ;
    dwc:minimumDepthInMeters 3.7678e+02 ;
    dwc:occurrenceID "227940090001039" ;
    dwc:samplingProtocol "Small VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0" ;
    dwc:scientificName "Echinocucumis hispida" ;
    dwc:taxonID 124593 ;
    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue .

<file:///github/workspace/00087d31-412d-48ce-bed8-9ade8d5b80f5> dcterms:title "beamtrawl_2006-2022" ;
    dwc:decimalLatitude 7.128768e+01 ;
    dwc:decimalLongitude 2.213325e+01 ;
    dwc:eventDate "2006-05-28T02:33:00+00:00/2006-05-28T02:39:00+00:00" ;
    dwc:minimumDepthInMeters 3.2115e+02 ;
    dwc:occurrenceID "000810008002016" ;
    dwc:samplingProtocol "Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0" ;
    dwc:scientificName "Munida sarsi" ;
    dwc:taxonID 107163 ;
    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue .

<file:///github/workspace/0009bf51-340c-4fa4-ba3d-ce3300291d9c> dcterms:title "grab_2006-2022" ;
    dwc:decimalLatitude 7.132973e+01 ;
    dwc:decimalLongitude 2.24153e+01 ;
    dwc:eventDate "2006-06-06T00:19:00+00:00" ;
    dwc:minimumDepthInMeters 4.3462e+02 ;
    dwc:occurrenceID "000380058031020" ;
    dwc:samplingProtocol "Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0" ;
    dwc:scientificName "Ophiuroidea" ;
    dwc:taxonID 123084 ;
    indo:benthic-biomass-density-mareano "0.1"^^qudt:QuantityValue .

<file:///github/workspace/benthic-biomass> rdfs:label "Benthic biomass density" .


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
                    observedMeanDensity_kg_m2:
                      type: number
                      minimum: 0
                      description: Diagnostic mean of point-level weight/assumed-sampled-area
                        before spatial extrapolation.
                      x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#observedMeanDensity_kg_m2
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
              observationOutputs:
                type: array
                description: Per-observation output rows derived from source occurrence
                  records, when available.
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      x-jsonld-id: '@id'
                    occurrenceID:
                      type: string
                      x-jsonld-id: http://rs.tdwg.org/dwc/terms/occurrenceID
                    scientificName:
                      type: string
                      x-jsonld-id: http://rs.tdwg.org/dwc/terms/scientificName
                    aphiaID:
                      type: integer
                      x-jsonld-id: http://rs.tdwg.org/dwc/terms/taxonID
                    decimalLongitude:
                      type: number
                      x-jsonld-id: http://rs.tdwg.org/dwc/terms/decimalLongitude
                    decimalLatitude:
                      type: number
                      x-jsonld-id: http://rs.tdwg.org/dwc/terms/decimalLatitude
                    eventDate:
                      type: string
                      x-jsonld-id: http://rs.tdwg.org/dwc/terms/eventDate
                    depth_m:
                      type: number
                      x-jsonld-id: http://rs.tdwg.org/dwc/terms/minimumDepthInMeters
                    datasetName:
                      type: string
                      x-jsonld-id: http://purl.org/dc/terms/title
                    samplingProtocol:
                      type: string
                      x-jsonld-id: http://rs.tdwg.org/dwc/terms/samplingProtocol
                    density_kg_m2:
                      type: number
                      minimum: 0
                      x-jsonld-id: https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano
                      x-jsonld-type: http://qudt.org/schema/qudt/QuantityValue
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#observationOutputs
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
                    "observedMeanDensity_kg_m2": {
                      "@id": "seadots:observedMeanDensity_kg_m2",
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
                "observationOutputs": {
                  "@context": {
                    "occurrenceID": "dwc:occurrenceID",
                    "scientificName": "dwc:scientificName",
                    "aphiaID": "dwc:taxonID",
                    "decimalLongitude": "dwc:decimalLongitude",
                    "decimalLatitude": "dwc:decimalLatitude",
                    "eventDate": "dwc:eventDate",
                    "depth_m": "dwc:minimumDepthInMeters",
                    "datasetName": "dct:title",
                    "samplingProtocol": "dwc:samplingProtocol",
                    "density_kg_m2": {
                      "@id": "indo:benthic-biomass-density-mareano",
                      "@type": "qudt:QuantityValue"
                    }
                  },
                  "@id": "seadots:observationOutputs",
                  "@container": "@set"
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
                    "verificationGap": "seadots:verificationGap"
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
    "seadots": "https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano#",
    "qudt": "http://qudt.org/schema/qudt/",
    "prov": "http://www.w3.org/ns/prov#",
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

