
# POSEIDON Biology Input (Schema)

`ogc.hosted.seadots.poseidon-input-biology` *v0.1*

Schema for biological inputs consumed by POSEIDON, including biomass, abundance, recruitment, growth, mortality, diffusion, carrying capacity, OSMOSE configuration, and species-specific parameter files.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# POSEIDON Biology Input

Biology inputs initialize fish populations and ecological dynamics in POSEIDON. The implementation includes biomass, abundance, school, and OSMOSE-linked biology options. Common consumed parameters include species names, carrying capacity, initial biomass or abundance, recruitment, growth, natural mortality, meristics, diffusion, and external files such as OSMOSE parameter CSVs or species parameter tables.

## Pilot area: Swedish Baltic, north of Gotland Island

The reference pilot area covers ICES Subdivisions 27 (West of Gotland) and 29 (Archipelago Sea / Northern Baltic Proper), with the Bothnian Sea fringe (SD 30). Key stocks: Central Baltic herring (*Clupea harengus membras*), Baltic sprat (*Sprattus sprattus*), Eastern Baltic cod (*Gadus morhua*), European flounder (*Platichthys flesus*), Atlantic salmon (*Salmo salar*) Main-Basin stock, and coastal perch (*Perca fluviatilis*) and pike (*Esox lucius*).

## Source availability for the pilot area

Role classification:
- **R** = *Required* on the chosen initializer path — model cannot start without it.
- **S** = *Substitutable* — pick one source per role; do not stack alternatives.
- **V** = *Validation-only* — compared against model output after a run; not needed to start.

| Source | Role | Coverage of SD 27 / 29 | Provides | Feeds POSEIDON field(s) | Related bblock(s) | Format at origin | Licence |
|---|---|---|---|---|---|---|---|
| FishBase REST API / `rfishbase` | **R** | All species, global | von Bertalanffy `Linf,K,t0`; length-weight `a,b`; M (Pauly/Hoenig); maturity ogive | `species[].growth`, `.meristics`, `.mortality` | [properties], [property-relationship], [equation-property-relationship] | Tabular JSON/CSV | CC-BY-NC |
| SeaLifeBase | **R** (invertebrates only) | Invertebrates (e.g. *Saduria entomon*, *Crangon*) | Same as FishBase | Same as FishBase | [properties] | Tabular JSON/CSV | CC-BY-NC |
| ICES WGBFAS SAG | **R / S** (preferred for Baltic) | Central Baltic herring (25–27, 28.2, 29, 32), sprat (22–32), Eastern Baltic cod (24–32) | SSB, recruitment, F, reference points (B0, MSY) | `species[].carryingCapacity`, `.initialBiomass`, `.recruitment` | [poseidon-input-run-control] (start year), [poseidon-input-observation-output] | XML/CSV (SAG) | ICES Data Policy (open) |
| RAM Legacy v4.x | **S** (fallback when SAG absent) | Central Baltic herring, Baltic sprat, Eastern + Western Baltic cod | `bioparams` (K, r, B0, MSY); `timeseries` (SSB, R, F) | `species[].carryingCapacity`, `.virginBiomass`, `schaeferParamsFile` | [poseidon-input-run-control] | SQLite / Excel | CC-BY |
| ICES DATRAS — BITS Q1 & Q4 | **R** for `Abundance` initializer / **V** for `Biomass` initializer | Yes, stratified by SD incl. 27, 28, 29 | Haul-level CPUE, length frequency, age-length keys | `binsFilePath`, `species[].modelType: abundance` | [poseidon-input-map] (grid), [poseidon-input-observation-output] | CSV via web service / Exchange format | ICES Data Policy (open) |
| Copernicus Marine BAL physics `BALTICSEA_MULTIYEAR_PHY_003_011` | **S** (only if spatial diffusion enabled) | Whole Baltic, 1 nm res, 56 z-levels, 1993–present | SST, SSS, currents (driver of diffusion / spawning) | `species[].diffusion` (calibration); referenced via `stacItems[]` | [poseidon-input-map], [poseidon-input-scenario] | NetCDF + ARCO Zarr | Copernicus Licence |
| Copernicus Marine BAL BGC `BALTICSEA_MULTIYEAR_BGC_003_012` | **S** (only if env-recruitment enabled) | Same domain | Chl-a, NPP, O₂, nutrients | `species[].recruitment` (env-driver) | [poseidon-input-scenario], [equation-property-relationship] | NetCDF + ARCO Zarr | Copernicus Licence |
| SLU Aqua KUL database | **R / S** for coastal perch & pike | Swedish coast incl. SD 27/29 reference areas (Asköfjärden, Lagnö, Kvädöfjärden) | Coastal gillnet/fyke catch-at-length | `species[].initialBiomass` (coastal), `binsFilePath` | [poseidon-input-map], [poseidon-input-observation-output] | CSV / GBIF DwC-A | CC-BY 4.0 |
| HELCOM core indicators | **V** + **S** (spawning-area mask) | Whole Baltic incl. SD 27/29 | Coastal-fish indicators; cod/sprat/herring spawning-area maps; salmon abundance | spatial mask for `species[].diffusion`; validation thresholds | [poseidon-input-map], [poseidon-input-observation-output], [poseidon-input-regulation-policy] (MSFD GES bands) | CSV + WMS/WFS | CC-BY |
| EMODnet Biology | **V** | Baltic, by station and grid | Aggregated abundance per species / grid | validation only | [poseidon-input-observation-output] | NetCDF + WFS + DwC-A | CC-BY |
| OBIS / GBIF | **V** | Baltic, by occurrence | Occurrence points for diffusion calibration | validation only | [poseidon-input-observation-output] | DwC-A | CC0 / CC-BY |
| OSMOSE generated config (`osmose-web-api`) | **R** *only* for `Osmose Biology` initializer | No published Baltic config; generated from FishBase + pilot polygon | Full ecosystem-model parameter set | `osmoseConfigurationFile`, `species[].modelType: osmose` (replaces all per-species fields) | [poseidon-model], [odd-protocol] | YAML + CSV | LGPL / CC-BY-SA |

[properties]: ../properties/
[property-relationship]: ../property-relationship/
[equation-property-relationship]: ../equation-property-relationship/
[poseidon-input-run-control]: ../poseidon-input-run-control/
[poseidon-input-map]: ../poseidon-input-map/
[poseidon-input-observation-output]: ../poseidon-input-observation-output/
[poseidon-input-scenario]: ../poseidon-input-scenario/
[poseidon-input-regulation-policy]: ../poseidon-input-regulation-policy/
[poseidon-model]: ../poseidon-model/
[odd-protocol]: ../odd-protocol/

## What you must acquire vs what is optional

Selecting sources is **not** "take all of the above". Each source falls in exactly one of three roles for a given run; the role depends on which `initializerType` and which optional drivers you turn on.

### Required path — what you must have to start a run

The `initializerType` chosen in this bblock controls the minimum required set. For the north-of-Gotland pilot:

| Chosen `initializerType` | Minimum required sources | Optional drivers |
|---|---|---|
| `Single Species Biomass` (Schaefer / logistic) | FishBase (R) + one of {WGBFAS SAG, RAM Legacy} (R) | Copernicus PHY for diffusion; BGC for env-recruitment |
| `Single Species Abundance` / `Multiple Species Abundance` | FishBase (R) + WGBFAS SAG (R) for recruitment + DATRAS BITS (R) for length bins | Copernicus PHY; SLU KUL adds coastal species |
| `Osmose Biology` | OSMOSE generated config (R) — replaces all per-species inputs | Copernicus PHY+BGC drives OSMOSE forcings |

If a source is marked **S** in the table, exactly one of the substitutable alternatives is required; the rest are *not* added.

### Substitutable — pick the highest authority for your stocks

Stacking alternatives produces conflicts and silently breaks reproducibility. For each role below, choose one:

- **Stock-level dynamics**: WGBFAS SAG (preferred for ICES Baltic stocks) **xor** RAM Legacy (fallback).
- **Coastal species initial state**: SLU Aqua KUL (preferred) **xor** OBIS/GBIF occurrence kernel.
- **Environmental forcing**: Copernicus BAL reanalysis (`MULTIYEAR_PHY_003_011`) **xor** Copernicus BAL forecast (`ANALYSISFORECAST_PHY_003_006`) — reanalysis for hindcast/validation, forecast for prospective scenarios. Selection lives in [poseidon-input-scenario], not here.

### Validation-only — not needed to start

These are compared against POSEIDON outputs after a run completes and never appear in the required path:

- OBIS / GBIF occurrences (spatial KDE vs. modelled steady-state distribution)
- HELCOM coastal-fish indicators (GES thresholds; cross-referenced from [poseidon-input-regulation-policy])
- EMODnet Biology gridded abundance
- Held-out years from WGBFAS SAG / RAM Legacy SSB time-series
- BITS CPUE when *Biomass* initializer is chosen (length frequencies are not used as input)

The validation harness is wired through [poseidon-input-observation-output] — that bblock declares which model variables are observed; this bblock declares which empirical series they are compared against.

### Minimal viable bundle for the pilot

The smallest credible set of data to run POSEIDON for Central Baltic herring + sprat + Eastern Baltic cod, north of Gotland, on the `Single Species Biomass` path:

1. **FishBase** — biological traits per species.
2. **ICES WGBFAS SAG** — `K` (carrying capacity) and `initialBiomass` (start-year SSB).
3. *(Optional)* **Copernicus BAL physics reanalysis** — required only if `species[].diffusion` is to be currents-driven; otherwise scalar diffusion suffices.

Everything else in the table either substitutes for one of the three above, refines a coastal-species sub-model, or sits in the validation harness.

## Two-stage transformation pipeline

All sources are normalised to the **EDITO Data Lake** (object-store on S3, indexed by STAC at `stac.marine.copernicus.eu`) before being projected to the POSEIDON biology-input schema. Vector data is encoded as **GeoParquet 1.1** (`geometry` WKB, CRS `EPSG:4326`); gridded data is encoded as **GeoZarr** (Zarr v3 store, CF coords `time, lat, lon`, `_ARRAY_DIMENSIONS`, `spatial_ref` aux coord, time- and geo-chunked variants).

### Stage A — Source → EDITO (GeoParquet for vector / GeoZarr for grid)

| Source | EDITO artefact | Transformation |
|---|---|---|
| FishBase / SeaLifeBase | `bio/species_traits.parquet` (non-spatial GeoParquet with a sentinel POINT(0,0) or pure Parquet sibling) | `rfishbase::popgrowth(), poplw(), maturity()` → harmonise units (cm, g, yr⁻¹) → WoRMS AphiaID join → one row per `species_aphia_id`, columns `Linf, K, t0, a, b, M_pauly, Lmat, h`. |
| ICES DATRAS BITS HH/HL/CA | `bio/bits_hauls.parquet`, `bio/bits_lengths.parquet` (GeoParquet, haul `geometry` = POINT WGS84) | Pull via `icesDatras::getDATRAS("HH"/"HL"/"CA", "BITS", years, quarters)`; filter `AreaCode ∈ {27,28,29}`; join HL/CA on HaulID; convert subfactor-corrected numbers to numbers-per-hour-per-km²; write partitioned by `year, quarter`. |
| ICES WGBFAS SAG | `bio/sag_timeseries.parquet`, `bio/sag_refpoints.parquet` | `icesSAG::getStockDownloadData(assessmentKey)` for stocks `her.27.25-2932`, `spr.27.22-32`, `cod.27.24-32`, `sal.27.22-31`; long-format `stock, year, ssb, recruitment, F, catch`; reference points in companion table. |
| RAM Legacy | `bio/ram_bioparams.parquet`, `bio/ram_timeseries.parquet` | Read SQLite; filter `assessid` LIKE `%-BALTIC-%` and `%-HER-2532%`, `%-SPR-2232%`, `%-COD-2432%`; pivot `bioparams` to wide; keep `timeseries` long with `tsid ∈ {SSB-MT, R-E00, F-1/yr}`. |
| Copernicus Marine BAL physics / BGC | GeoZarr stores reusing the EDITO ARCO endpoints (no copy needed — register STAC Items pointing at existing `s3://mdl-native-XX/native/MUL/BALTICSEA_MULTIYEAR_PHY_003_011/...zarr`) | Subset to bbox `[16.0, 56.5, 21.5, 60.0]` and depth ≤ 100 m using `xarray.open_zarr` lazy slicing; rechunk to `geoChunked` (`time≈138, lat=32, lon=64`) for time-series extraction; persist subset under `s3://edito-pilot/north-gotland/phy.zarr`. |
| SLU Aqua KUL (coastal) | `bio/slu_kul_catch.parquet` (GeoParquet, station POINT) | Download CSV from KUL portal or GBIF DwC-A (dataset UUID `1b7e83a0-…`); harmonise to columns `station_id, geometry, year, gear, species_aphia_id, length_cm, count, effort_h`; clip to SE EEZ ≥ 57.5°N. |
| HELCOM indicators | `bio/helcom_indicator.parquet` (GeoParquet, assessment-unit polygons) + `bio/helcom_spawning.zarr` for raster habitat maps | WFS pull of assessment-unit polygons; join indicator CSV on `assessment_unit_id`; for spawning-area rasters, regrid to common 1 nm Baltic grid and write GeoZarr. |
| EMODnet Biology | `bio/emodnet_abundance.parquet` (gridded points) | WFS request `emodnet:abundance_grid`; reproject to EPSG:4326; column rename to DwC-style. |
| OBIS / GBIF | `bio/occurrence.parquet` (GeoParquet, POINT) | DwC-A → Parquet; deduplicate on `eventID + occurrenceID`; keep `scientificName, eventDate, decimalLat, decimalLon, basisOfRecord`. |

Each artefact is published as a **STAC Item** with `properties.processing:lineage` referring back to the upstream identifier (DOI, dataset UUID, or DATRAS query) and `assets[*].type = application/vnd.apache.parquet` or `application/vnd.zarr+zip`.

### Stage B — EDITO → POSEIDON `poseidon-input-biology`

| EDITO artefact | POSEIDON field(s) | Transformation |
|---|---|---|
| `species_traits.parquet` | `species[].growth = {growerType: "von Bertalanffy", Linf, K, t0}`; `species[].meristics = {a, b, Lmat}`; `species[].mortality = {naturalMortality: M}` | Filter rows for target species AphiaIDs; pivot wide; emit one element of `species[]` per row; convert per-year to per-day if `poseidon-input-run-control.stepUnit = day`. |
| `sag_refpoints.parquet` + `ram_bioparams.parquet` | `species[].carryingCapacity`, `species[].virginBiomass` | Prefer SAG `Blim`-derived B0 if present; else RAM `K` (tonnes → kg ×1000); pick latest assessment year. |
| `sag_timeseries.parquet` | `species[].initialBiomass`, validation series held out | `WHERE year = run_control.startYear → initialBiomass` (SSB in tonnes → kg); remaining years kept as `validation.ssbSeries` (out of schema, attached via `dataFiles[]`). |
| `bits_lengths.parquet` | `binsFilePath` + `initializerType: "Single Species Abundance"` + `species[].modelType: abundance` | Aggregate by `species_aphia_id, year, length_cm`; build bin edges (1 cm); pivot to matrix `bin × age`; write CSV `bins/<species>.csv` referenced from `binsFilePath`. |
| `phy.zarr` (SST, currents) | `species[].diffusion = {differentialPercentageToMove, percentageLimitOnDailyMovement}` | Compute climatological surface current magnitude and ∇SST per cell; scale to the diffusion coefficients (calibration loop, not direct copy); cells written into `poseidon-input-map` grid – diffusion params here remain scalars but with **provenance** STAC pointer added to `stacItems[]`. |
| `bgc.zarr` (Chl-a, NPP) | `species[].recruitment = {recruiterType: "EnvironmentalRecruiter", chlProxy: ...}` | Annual mean Chl-a anomaly → multiplicative recruitment driver; emit as YAML-friendly map. |
| `slu_kul_catch.parquet` | `species[]` for coastal perch and pike, `initializerType: "Multiple Species Abundance"` | Compute design-based abundance index (`number / effort_h × area`) by year; provides initial coastal abundance at start year. |
| `helcom_indicator.parquet` + `helcom_spawning.zarr` | `species[].diffusion` (spatial restriction) + validation thresholds | Use spawning-area mask to constrain initial seeding cells in `poseidon-input-map`; indicator thresholds drive validation tolerance. |
| `occurrence.parquet` | Diffusion calibration target (validation, not schema) | KDE of occurrences → expected steady-state distribution; tune diffusion until KS-distance below tolerance. |
| OSMOSE generated config (via `osmose-web-api`) | `initializerType: "Osmose Biology"`, `osmoseConfigurationFile`, `species[].modelType: osmose` | Call config-builder with the FishBase species list and pilot-area shapefile; checksum and upload to `s3://edito-pilot/north-gotland/osmose/`; reference the YAML path. |

### STAC cross-links

Every Stage A artefact MUST be registered as a STAC Item under a single Collection `poseidon-bio-north-gotland`. The `stacItems[]` field in this schema accepts either the Item URI (`https://stac.marine.copernicus.eu/.../items/...`) or an embedded Item object — this is how a POSEIDON biology configuration becomes self-describing and reproducible.

### Validation strategy

| Validation target | EDITO source | Comparison |
|---|---|---|
| Modelled SSB 1993–latest | `sag_timeseries.parquet` (SAG) and `ram_timeseries.parquet` | Annual time-series, RMSE and Pearson r per stock. |
| Modelled length distribution | `bits_lengths.parquet` aggregated to year + SD | KS-test per year-SD bin. |
| Modelled spatial distribution | `occurrence.parquet` + `helcom_spawning.zarr` | Spearman of cell density vs KDE / spawning-suitability raster. |
| Modelled coastal abundance | `slu_kul_catch.parquet` | Index correlation at gillnet reference areas. |

Stocks marked `under-assessment-only` (e.g. Eastern Baltic cod where survey signal is currently more reliable than the analytical assessment) should be validated against BITS CPUE rather than SAG outputs.

## Examples

### Single-species biomass input
#### json
```json
{
  "initializerType": "Single Species Biomass",
  "species": [
    {
      "name": "Species 0",
      "modelType": "biomass",
      "carryingCapacity": 5000,
      "growth": {
        "growerType": "Independent Logistic Grower",
        "steepness": "uniform 0.6 0.8"
      },
      "diffusion": {
        "differentialPercentageToMove": 0.001,
        "percentageLimitOnDailyMovement": 0.01
      }
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-biology/context.jsonld",
  "initializerType": "Single Species Biomass",
  "species": [
    {
      "name": "Species 0",
      "modelType": "biomass",
      "carryingCapacity": 5000,
      "growth": {
        "growerType": "Independent Logistic Grower",
        "steepness": "uniform 0.6 0.8"
      },
      "diffusion": {
        "differentialPercentageToMove": 0.001,
        "percentageLimitOnDailyMovement": 0.01
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/iliad/seadots/poseidon/input#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] schema:about ( [ schema:name "Species 0" ;
                :carryingCapacity 5000 ;
                :diffusion [ :differentialPercentageToMove 1e-03 ;
                        :percentageLimitOnDailyMovement 1e-02 ] ;
                :growth [ :growerType "Independent Logistic Grower" ;
                        :steepness "uniform 0.6 0.8" ] ;
                :modelType "biomass" ] ) ;
    :initializerType "Single Species Biomass" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: POSEIDON Biology Input
description: Biological initializer and species parameter input for POSEIDON.
type: object
required:
- initializerType
properties:
  initializerType:
    type: string
    examples:
    - Single Species Biomass
    - Multiple Species Biomass
    - Single Species Abundance
    - Osmose Biology
  species:
    type: array
    minItems: 1
    items:
      type: object
      required:
      - name
      properties:
        name:
          type: string
          x-jsonld-id: https://schema.org/name
        modelType:
          type: string
          enum:
          - biomass
          - abundance
          - school
          - osmose
          - other
        carryingCapacity:
          type: number
        initialBiomass:
          type: number
        virginBiomass:
          type: number
        growth:
          type: object
          additionalProperties: true
        recruitment:
          type: object
          additionalProperties: true
        mortality:
          type: object
          additionalProperties: true
        meristics:
          type: object
          additionalProperties: true
        diffusion:
          type: object
          additionalProperties: true
        dataFiles:
          type: array
          items:
            type: string
          x-jsonld-id: https://schema.org/encoding
          x-jsonld-container: '@list'
    x-jsonld-id: https://schema.org/about
    x-jsonld-container: '@list'
  osmoseConfigurationFile:
    type: string
  preInitializedConfigurationDirectory:
    type: string
  schaeferParamsFile:
    type: string
  binsFilePath:
    type:
    - string
    - 'null'
  stacItems:
    type: array
    items:
      oneOf:
      - type: string
        format: uri
      - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
    x-jsonld-id: https://w3id.org/ogc/stac/Item
    x-jsonld-container: '@list'
additionalProperties: true
x-jsonld-vocab: https://w3id.org/iliad/seadots/poseidon/input#
x-jsonld-prefixes:
  schema: https://schema.org/
  stac: https://w3id.org/ogc/stac/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-biology/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-biology/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/iliad/seadots/poseidon/input#",
    "species": {
      "@context": {
        "name": "schema:name",
        "dataFiles": {
          "@id": "schema:encoding",
          "@container": "@list"
        }
      },
      "@id": "schema:about",
      "@container": "@list"
    },
    "stacItems": {
      "@context": {
        "id": "@id",
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
        "stac_extensions": "stac:core/hasExtension",
        "assets": {
          "@context": {
            "type": "dct:format",
            "roles": {
              "@id": "stac:core/roles",
              "@container": "@set"
            }
          },
          "@id": "stac:core/hasAsset",
          "@container": "@set"
        },
        "title": {
          "@id": "dct:title",
          "@container": "@set"
        },
        "description": {
          "@id": "dct:description",
          "@container": "@set"
        },
        "keywords": {
          "@id": "dcat:keyword",
          "@container": "@set"
        },
        "license": "dcat:license",
        "created": "dct:created",
        "updated": "dct:modified",
        "language": "rec:language",
        "languages": {
          "@container": "@set",
          "@id": "rec:languages"
        },
        "resourceLanguages": {
          "@container": "@set",
          "@id": "rec:resourceLanguages"
        },
        "externalIds": {
          "@context": {
            "scheme": "rec:scheme",
            "value": "rec:id"
          },
          "@container": "@set",
          "@id": "rec:scopedIdentifier"
        },
        "themes": {
          "@context": {
            "concepts": {
              "@context": {
                "id": "stac:themes/id",
                "url": "@id"
              },
              "@id": "stac:themes/concepts",
              "@container": "@set"
            },
            "scheme": "stac:themes/scheme"
          },
          "@container": "@set",
          "@id": "rec:themes"
        },
        "formats": {
          "@context": {
            "name": "rec:name",
            "mediaType": "rec:mediaType"
          },
          "@container": "@set",
          "@id": "rec:format",
          "@type": "@id"
        },
        "contacts": {
          "@context": {
            "logo": {
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
              }
            }
          },
          "@container": "@set",
          "@id": "dcat:contactPoint",
          "@type": "@id"
        },
        "rights": "dcat:rights",
        "datetime": {
          "@id": "dct:date",
          "@type": "xsd:dateTime"
        }
      },
      "@id": "stac:Item",
      "@container": "@list"
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
    "features": {
      "@container": "@set",
      "@id": "geojson:features"
    },
    "properties": "@nest",
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "stac_version": "stac:core/version",
    "type": "@type",
    "title": "dct:title",
    "description": "dct:description",
    "keywords": "dct:subject",
    "license": "dct:license",
    "start_datetime": {
      "@id": "stac:core/start_datetime",
      "@type": "xsd:dateTime"
    },
    "end_datetime": {
      "@id": "stac:core/end_datetime",
      "@type": "xsd:dateTime"
    },
    "providers": "stac:core/hasProvider",
    "media_type": "dct:format",
    "schema": "https://schema.org/",
    "stac": "https://w3id.org/ogc/stac/",
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
    "thns": "stac:themes/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-biology/context.jsonld)

## Sources

* [POSEIDON BiologyInitializer YAML samples](https://github.com/poseidon-fisheries/POSEIDON/blob/main/POSEIDON/inputs/YAML%20Samples/components/BiologyInitializer.yaml)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/_stage/poseidon-input-biology`

