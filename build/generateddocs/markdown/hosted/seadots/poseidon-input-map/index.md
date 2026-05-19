
# POSEIDON Map Input (Schema)

`ogc.hosted.seadots.poseidon-input-map` *v0.1*

Schema for spatial map inputs consumed by POSEIDON, including generated grids, file-backed maps, bounds, cell size, bathymetry/depth values, coastline/land flags, and STAC references.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# POSEIDON Map Input

POSEIDON map inputs define the spatial domain consumed by the model. The implementation supports generated maps such as `Simple Map` and `Two Sided Map`, file-backed maps such as `From File Map`, OSMOSE-related maps, spatial bounds, grid/cell sizes, latitude-longitude flags, bathymetry/depth values, and optional depth overrides.

This block also allows STAC item or collection references so spatial domain inputs can be cataloged and reused.

## Pilot area: Swedish Baltic, north of Gotland Island

Spatial extent for the pilot: bounding box `[16.0, 56.5, 21.5, 60.0]` (EPSG:4326), covering ICES Subdivisions 27 and 29 plus the Bothnian Sea fringe. Maximum modelled depth ~250 m (Landsort Deep), median ~70 m. Coastline is heavily indented through the Stockholm and Åland archipelagos — cell size has to be small enough that island chains are not collapsed into solid land. Recommended pilot grid: **1 nm (~1.85 km)** to align with the Copernicus BAL MFC reanalysis grid referenced from [poseidon-input-biology] and [poseidon-input-scenario]; SSCF coastal sub-runs may use a nested **500 m** grid.

## Source availability for the pilot area

Role classification (same convention as [poseidon-input-biology] and [poseidon-input-fleet]):
- **R** = *Required* — model cannot start without it.
- **S** = *Substitutable* — pick one per role; do not stack alternatives.
- **V** = *Validation-only* — compared against map-derived outputs after a run.

| Source | Role | Coverage of SD 27 / 29 | Provides | Feeds POSEIDON field(s) | Related bblock(s) | Format at origin | Licence |
|---|---|---|---|---|---|---|---|
| EMODnet Bathymetry DTM 2024 | **R** | All European seas incl. Baltic, 1/16 arc-min (~115 m) | Bathymetric surface, type-of-source mask, source-data identifier per cell | `mapFile` (depth column), `minInitialDepth`, `maxInitialDepth`, cell bathymetry | [poseidon-input-biology] (diffusion grid), [poseidon-input-fleet] (effort heatmap) | NetCDF / GeoTIFF / OGC WCS+WMS | CC-BY 4.0 |
| EMODnet High-Resolution Seabed Mapping (national surveys) | **S** | Patchy — Swedish national surveys via Sjöfartsverket cover parts of SD 27/29 | Sub-100 m bathymetry where available | Refines `mapFile` in patches | [poseidon-input-fleet] | GeoTIFF | Mostly open; some restricted (charts) |
| GEBCO 2024 Grid | **S** fallback | Global, 15 arc-sec | Coarser bathymetry | Same as EMODnet DTM | [poseidon-input-scenario] | NetCDF / GeoTIFF | CC0 |
| EMODnet Coastline (HR composite) | **R** | Full European coastline incl. Baltic archipelagos | Shoreline polygon | Land mask used by `From File Map` / `Simple Map` | [poseidon-input-port-market] | Shapefile / GeoPackage | CC-BY 4.0 |
| OpenStreetMap coastline (GSHHG) | **S** | Global | Alternative coastline | Same as EMODnet Coastline | – | Shapefile / PBF | ODbL |
| Copernicus Marine BAL native grid (`BALTICSEA_MULTIYEAR_PHY_003_011`) | **R / S** (when cross-bblock grid alignment is required) | Whole Baltic, 1 nm res, 56 z-levels | Reference model grid + bathymetry-on-grid | Grid extent (`upLeftEasting/Northing`, `lowRightEasting/Northing`), `cellSizeInKilometers`, `gridWidthInCell` | [poseidon-input-biology], [poseidon-input-scenario] | NetCDF + ARCO Zarr | Copernicus Licence |
| HELCOM MPA database (mpas.helcom.fi) | **R** for Baltic closures | All HELCOM Baltic MPAs incl. SE | MPA polygons, designation type, management status | `depthOverrides` (closure mask), spatial closures handed to [poseidon-input-regulation-policy] | [poseidon-input-regulation-policy] | Shapefile / GeoPackage / WMS / WFS / ArcGIS REST | CC-BY 4.0 |
| EEA Natura 2000 spatial data (SCI + SPA) | **R** for EU-directive sites | EU-wide incl. Swedish marine sites | SCI + SPA polygons, habitat codes, species codes | Closure / soft-protection mask | [poseidon-input-regulation-policy], [poseidon-input-biology] | GeoPackage / Shapefile / INSPIRE | CC-BY 4.0 |
| EU CDDA (Nationally Designated Areas) | **S** | EU-wide | Nationally designated reserves | Closure mask (broader than Natura 2000) | [poseidon-input-regulation-policy] | GeoPackage / Shapefile | CC-BY 4.0 |
| WDPA (UNEP-WCMC) | **S** fallback | Global | Global MPA layer | Same as HELCOM/Natura | – | Shapefile / GeoPackage | Custom open |
| EMODnet Human Activities — Main Ports | **R** | EU + Baltic, harmonised with Eurostat | Port locations, UN/LOCODE, traffic class | `farOffPorts[]`, port catalog feeding [poseidon-input-port-market] | [poseidon-input-port-market], [poseidon-input-fleet] | Shapefile / WFS | CC-BY 4.0 |
| UN/LOCODE | **R** | Global | Port code authority | Key used to link ports across bblocks | [poseidon-input-port-market], [poseidon-input-fleet] | CSV | UN open |
| OpenStreetMap (small ports & harbours) | **S** complement | Sweden incl. archipelago | Small fishing harbours not in EMODnet | Adds SSCF home ports to `farOffPorts[]` | [poseidon-input-port-market] | PBF / Overpass API | ODbL |
| EMODnet HA — Offshore wind farms, cables, pipelines | **S** | Baltic | Marine industrial exclusion polygons | Optional closure mask | [poseidon-input-regulation-policy], [poseidon-input-scenario] | Shapefile / WFS | CC-BY 4.0 |
| EMODnet Geology — Seabed Substrate | **S** | Baltic, ~250 m | Folk-7 substrate class per cell | Trawl-feasibility mask used to refine `depthOverrides` and gear-cell-eligibility | [poseidon-input-fleet] (gear–substrate match) | GeoTIFF / Shapefile | CC-BY 4.0 |
| HELCOM MSP data portal | **V / S** | Baltic | Designated MSP zones (shipping lanes, energy, defence) | Validation of closure overlay; alternative closure source | [poseidon-input-regulation-policy], [poseidon-input-scenario] | WMS / WFS | CC-BY 4.0 |
| Swedish Sjöfartsverket nautical chart depth | **V** | Swedish EEZ | In-situ soundings | Bathymetry validation | – | S-57 / S-100 | Restricted (use rights only) |

[poseidon-input-biology]: ../poseidon-input-biology/
[poseidon-input-fleet]: ../poseidon-input-fleet/
[poseidon-input-port-market]: ../poseidon-input-port-market/
[poseidon-input-regulation-policy]: ../poseidon-input-regulation-policy/
[poseidon-input-scenario]: ../poseidon-input-scenario/
[poseidon-input-observation-output]: ../poseidon-input-observation-output/

## Two-stage transformation pipeline

Stage A normalises each source to **EDITO Data Lake** form (GeoParquet 1.1 vector / GeoZarr v3 grid, STAC-indexed under collection `poseidon-map-north-gotland`, persisted under `s3://edito-pilot/north-gotland/map/`). Stage B projects EDITO artefacts to the POSEIDON map-input schema.

### Stage A — Source → EDITO

| Source | EDITO artefact | Transformation |
|---|---|---|
| EMODnet Bathymetry DTM 2024 | `map/bathymetry.zarr` (GeoZarr, dims `lat, lon`, var `elevation`) | Pull tile(s) via OGC WCS for pilot bbox; reproject to EPSG:4326 if needed; resample to chosen pilot resolution (1 nm preferred); write Zarr v3 with `spatial_ref` aux coord and `_ARRAY_DIMENSIONS`; preserve `source_type` mask as a second variable. |
| EMODnet HR Seabed Mapping (national) | `map/bathymetry_patches.parquet` (GeoParquet, POLYGON footprints) + `map/bathymetry_patches/*.zarr` | One GeoZarr per high-res patch; footprint polygons indexed in the parquet for cell-level priority join. |
| GEBCO 2024 | `map/bathymetry_gebco.zarr` (only if used as fallback) | Same shape as EMODnet bathymetry; flagged in STAC properties as `priority=2`. |
| EMODnet Coastline (HR composite) | `map/coastline.parquet` (GeoParquet, LINESTRING/POLYGON) | Pull HR coastline; clip to pilot bbox + 5 km buffer; columns `feature_id, geometry, source, year`. |
| Copernicus BAL native grid | Reference STAC Item (no copy) | Register the Copernicus BALTICSEA_MULTIYEAR_PHY_003_011 Zarr as the canonical "model grid" Item; properties carry `grid:cell_size_nm=1`, `grid:nx`, `grid:ny`, `grid:bbox`. |
| HELCOM MPA database | `map/helcom_mpa.parquet` (GeoParquet, POLYGON) | WFS pull from HELCOM MADS; columns `mpa_id, name, designation, designation_year, management_status, geometry`. |
| EEA Natura 2000 | `map/natura2000.parquet` (GeoParquet, POLYGON) | Pull GeoPackage from EEA Data Hub; filter to `marine = true` and country `SE`; columns `site_code, site_name, site_type ∈ {SCI, SPA, SCI/SPA}, designation_year, geometry, species_codes[]`. |
| EU CDDA | `map/cdda.parquet` (GeoParquet, POLYGON) | Filter to SE marine sites. |
| EMODnet HA Main Ports | `map/ports.parquet` (GeoParquet, POINT) | WFS pull; columns `locode, port_name, country, geometry, goods_kt, passengers, vessel_calls`; clip to pilot bbox + 50 km landward. |
| OpenStreetMap small ports | `map/ports_osm.parquet` (GeoParquet, POINT) | Overpass API query `node[harbour=yes][harbour:type~"marina|fishing"]` within bbox; columns `osm_id, name, harbour_type, geometry`. |
| UN/LOCODE | `map/un_locode.parquet` | Read CSV; columns `locode, country, location, geometry` (POINT from CSV coords). |
| EMODnet HA Wind farms / cables | `map/industrial_exclusions.parquet` (GeoParquet, POLYGON / LINESTRING) | WFS pull; aggregate to a single `exclusion_type, geometry` table. |
| EMODnet Geology Seabed Substrate | `map/substrate.zarr` | GeoTIFF → Zarr v3, var `substrate_folk7`; preserve attribute `legend` mapping codes to Folk classes. |
| HELCOM MSP zones | `map/msp_zones.parquet` (GeoParquet, POLYGON) | WFS pull from HELCOM MSP portal; columns `zone_id, zone_type, member_state, status, geometry`. |

Each Stage A artefact is registered as a STAC Item with `properties.processing:lineage` pointing back to upstream identifier and `proj:epsg = 4326`.

### Stage B — EDITO → POSEIDON

| EDITO artefact | POSEIDON field(s) | Transformation |
|---|---|---|
| `bathymetry.zarr` (+ optional `bathymetry_patches/*.zarr`) | `mapFile` (CSV), `minInitialDepth`, `maxInitialDepth`, `cellSizeInKilometers`, `gridWidthInCell`, `width`, `height` | Resample / clip to pilot grid; where HR patches exist, replace cells (priority join); flatten to CSV `lat, lon, depth` (negative below sea level); set `latLong: true`, `header: true`; emit grid metadata as scalar fields. |
| Reference Copernicus BAL grid Item | `cellSizeInKilometers` ≈ 1.85, `upLeftEasting/Northing`, `lowRightEasting/Northing`, `gridWidthInCell` | Pull from STAC Item properties; same grid is consumed by [poseidon-input-biology] for diffusion and [poseidon-input-scenario] for forcing fields. |
| `coastline.parquet` | Land mask cells (filled in `mapFile` depth column with land sentinel) | Rasterise to pilot grid; cells touching coastline polygon get `depth = land_sentinel` per the chosen initializer. |
| `helcom_mpa.parquet` + `natura2000.parquet` + `cdda.parquet` | `depthOverrides[]` (mask-tag strings) **and** spatial closures handed off to [poseidon-input-regulation-policy] | Compute per-cell closure flag (union of MPA polygons); emit closure cell list as CSV `lat, lon, closure_type` referenced from `depthOverrides[]`; the regulation bblock decides whether each closure is hard/soft/seasonal. |
| `industrial_exclusions.parquet` | Same `depthOverrides[]` channel with tag `industrial_exclusion` | Per-cell mask. |
| `substrate.zarr` | `depthOverrides[]` tag `substrate=<folk7>` per cell | Used by fleet gear-cell eligibility (e.g. bottom trawl forbidden over rock); the mapping rule lives in [poseidon-input-fleet]. |
| `ports.parquet` + `ports_osm.parquet` + `un_locode.parquet` | `farOffPorts[]` — list of port objects | Deduplicate on `locode` (or proximity match for OSM ports without LOCODE); emit one element per port with `locode, name, geometry, isOffMap` where `isOffMap = true` if outside the bounding box (a fisher may still land there in POSEIDON). |
| `msp_zones.parquet` | Optional `depthOverrides[]` tags `msp:<zone_type>` | Per-cell; informational for the scenario bblock. |

### STAC cross-links

`stacItem` (single Item) and `stacCollection` (whole pilot set) are the carriers. For the pilot:

- `stacCollection`: `https://stac.marine.copernicus.eu/collections/poseidon-map-north-gotland`
- `stacItem` for a specific run pinpoints the bathymetry build (e.g. `…/items/north-gotland-bathy-2024-1nm`).

This is how a POSEIDON map configuration becomes reproducible: a single STAC pointer resolves bathymetry, closures, ports, and the reference grid.

## Required vs substitutable vs validation-only

### Required path — minimum to start a run

| Chosen `initializerType` | Minimum required sources | Optional drivers |
|---|---|---|
| `Simple Map` / `Two Sided Map` | none beyond the schema scalars (`width`, `height`, `cellSizeInKilometers`, `latLong`) | Useful for synthetic tests only — not a credible pilot configuration. |
| `From File Map` (recommended for the pilot) | EMODnet Bathymetry DTM (R) + EMODnet Coastline (R) + UN/LOCODE (R) + EMODnet HA Main Ports (R) | HELCOM MPA + Natura 2000 once spatial closures are enabled; Copernicus BAL grid as reference grid |
| `OSMOSE Map` | All of the above + the OSMOSE configuration spatial files referenced from [poseidon-input-biology] | – |

### Substitutable — XOR rules

- **Bathymetry**: EMODnet Bathymetry DTM (preferred) **xor** GEBCO (fallback) **xor** national HR surveys (used as patches *over* EMODnet, not as a substitute).
- **Coastline**: EMODnet Coastline (preferred) **xor** OSM/GSHHG.
- **Reference model grid**: Copernicus BAL native grid (preferred for Baltic) **xor** custom POSEIDON synthetic grid (only if not coupling to environmental forcing).
- **MPA layer set**: HELCOM MPA + Natura 2000 (preferred, complementary) **xor** WDPA (fallback if HELCOM unavailable). HELCOM and Natura 2000 are stacked because they cover different designations; WDPA is a substitute for the union, not an addition.
- **Port catalog**: EMODnet HA Main Ports (preferred) augmented (not substituted) with OSM small-ports for SSCF coverage.

### Validation-only

- Swedish Sjöfartsverket nautical chart depth — bathymetry validation against in-situ soundings (use-rights only; cannot redistribute).
- HELCOM MSP zone polygons — sanity check that simulated effort respects designated lanes.
- HELCOM HOLAS pressure indicators — overlay against modelled spatial impact.

Wired through [poseidon-input-observation-output] as the validation harness.

### Minimal viable bundle for the pilot

1. **EMODnet Bathymetry DTM 2024** clipped to bbox `[16.0, 56.5, 21.5, 60.0]`, resampled to 1 nm.
2. **EMODnet Coastline** HR for the land mask.
3. **Copernicus BAL native grid** reference Item — fixes grid alignment with [poseidon-input-biology] and [poseidon-input-scenario].
4. **EMODnet HA Main Ports** + **UN/LOCODE** — port catalog feeding `farOffPorts[]` and [poseidon-input-port-market].
5. *(Required if spatial closures are enabled)* **HELCOM MPA** + **EEA Natura 2000** — closure polygons handed to [poseidon-input-regulation-policy].

Everything else either substitutes for one of the five above, refines SSCF coverage, or sits in the validation harness.

## Cross-bblock contract

- The grid declared here (cell size, extent, EPSG, bbox) is the **canonical spatial frame** for the run. [poseidon-input-biology] `species[].diffusion`, [poseidon-input-fleet] `destinationStrategy.weightsFile`, [poseidon-input-scenario] forcing fields, and [poseidon-input-observation-output] gridded validation targets MUST reuse this grid.
- `farOffPorts[]` LOCODEs MUST be a subset of the port catalog in [poseidon-input-port-market].
- Spatial closures live as cell masks here; their *rules* (seasonal, gear-specific, quota-tied) live in [poseidon-input-regulation-policy]. The two bblocks share the same closure ID space.
- Substrate masks and depth bands serve as inputs to fleet gear-cell eligibility; the mapping rule lives in [poseidon-input-fleet], not here.
- The "future" vs "past" axis (e.g. retrospective bathymetry vs proposed new MPAs) is selected in [poseidon-input-scenario] — this bblock supplies the alternates but does not switch on time-axis itself.

## Examples

### File-backed POSEIDON map
#### json
```json
{
  "initializerType": "From File Map",
  "mapFile": "inputs/indonesia/indonesia_latlong.csv",
  "gridWidthInCell": 100,
  "header": true,
  "latLong": true,
  "mapPaddingInDegrees": 0.000001,
  "stacItem": "https://example.org/stac/collections/poseidon-domain/items/indonesia-map"
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-map/context.jsonld",
  "initializerType": "From File Map",
  "mapFile": "inputs/indonesia/indonesia_latlong.csv",
  "gridWidthInCell": 100,
  "header": true,
  "latLong": true,
  "mapPaddingInDegrees": 1e-06,
  "stacItem": "https://example.org/stac/collections/poseidon-domain/items/indonesia-map"
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/iliad/seadots/poseidon/input#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix stac: <https://w3id.org/ogc/stac/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] dct:source "inputs/indonesia/indonesia_latlong.csv" ;
    :gridWidthInCell 100 ;
    :header true ;
    :initializerType "From File Map" ;
    :latLong true ;
    :mapPaddingInDegrees 1e-06 ;
    stac:Item <https://example.org/stac/collections/poseidon-domain/items/indonesia-map> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: POSEIDON Map Input
description: Spatial domain input for POSEIDON map initializers.
type: object
required:
- initializerType
properties:
  initializerType:
    type: string
    examples:
    - Simple Map
    - From File Map
    - OSMOSE Map
    - Two Sided Map
  mapFile:
    type: string
    description: Path or URI to a CSV-like map file when using a file-backed map initializer.
    x-jsonld-id: http://purl.org/dc/terms/source
  stacItem:
    oneOf:
    - type: string
      format: uri
    - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item/schema.yaml
    x-jsonld-id: https://w3id.org/ogc/stac/Item
    x-jsonld-type: '@id'
  stacCollection:
    oneOf:
    - type: string
      format: uri
    - $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/collection/schema.yaml
    x-jsonld-id: https://w3id.org/ogc/stac/Collection
    x-jsonld-type: '@id'
  cellSizeInKilometers:
    type: number
    exclusiveMinimum: 0
  gridWidthInCell:
    type: number
    exclusiveMinimum: 0
  width:
    type: number
  height:
    type: number
  header:
    type: boolean
  latLong:
    type: boolean
  mapPaddingInDegrees:
    type: number
  minInitialDepth:
    type: number
  maxInitialDepth:
    type: number
  lowRightEasting:
    type: number
  lowRightNorthing:
    type: number
  upLeftEasting:
    type: number
  upLeftNorthing:
    type: number
  depthOverrides:
    type: array
    items:
      type: string
  farOffPorts:
    type: array
    items:
      type: object
      additionalProperties: true
additionalProperties: true
x-jsonld-vocab: https://w3id.org/iliad/seadots/poseidon/input#
x-jsonld-prefixes:
  dcterms: http://purl.org/dc/terms/
  stac: https://w3id.org/ogc/stac/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-map/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-map/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/iliad/seadots/poseidon/input#",
    "mapFile": "dcterms:source",
    "stacItem": {
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
            "type": "dcterms:type",
            "hreflang": "dcterms:language",
            "title": "rdfs:label",
            "length": "dcterms:extent"
          },
          "@id": "rdfs:seeAlso"
        },
        "conformsTo": {
          "@container": "@set",
          "@id": "dcterms:conformsTo",
          "@type": "@id"
        },
        "time": "dcterms:temporal",
        "linkTemplates": {
          "@context": {
            "rel": {
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              },
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id"
            },
            "type": "dcterms:format",
            "hreflang": "dcterms:language",
            "title": "rdfs:label",
            "length": "dcterms:extent",
            "uriTemplate": {
              "@type": "xsd:string",
              "@id": "rec:uriTemplate"
            },
            "varBase": "rec:varBase",
            "variables": {
              "@id": "rec:hasVariable",
              "@container": "@index",
              "@index": "dcterms:identifier"
            }
          },
          "@id": "rec:hasLinkTemplate"
        },
        "stac_extensions": "stac:core/hasExtension",
        "assets": {
          "@context": {
            "type": "dcterms:format",
            "roles": {
              "@id": "stac:core/roles",
              "@container": "@set"
            }
          },
          "@id": "stac:core/hasAsset",
          "@container": "@set"
        },
        "title": {
          "@id": "dcterms:title",
          "@container": "@set"
        },
        "description": {
          "@id": "dcterms:description",
          "@container": "@set"
        },
        "keywords": {
          "@id": "dcat:keyword",
          "@container": "@set"
        },
        "license": "dcat:license",
        "created": "dcterms:created",
        "updated": "dcterms:modified",
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
                "type": "dcterms:type",
                "hreflang": "dcterms:language",
                "title": "rdfs:label",
                "length": "dcterms:extent"
              }
            }
          },
          "@container": "@set",
          "@id": "dcat:contactPoint",
          "@type": "@id"
        },
        "rights": "dcat:rights"
      },
      "@id": "stac:Item",
      "@type": "@id"
    },
    "stacCollection": {
      "@context": {
        "stac_extensions": "stac:core/hasExtension",
        "id": "@id",
        "extent": "dcterms:extent",
        "links": {
          "@context": {
            "rel": {
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              },
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id"
            },
            "type": "dcterms:type",
            "hreflang": "dcterms:language",
            "title": "rdfs:label",
            "length": "dcterms:extent"
          },
          "@id": "rdfs:seeAlso"
        },
        "assets": {
          "@context": {
            "type": "dcterms:format",
            "roles": {
              "@id": "stac:core/roles",
              "@container": "@set"
            }
          },
          "@id": "stac:core/hasAsset",
          "@container": "@set"
        }
      },
      "@id": "stac:Collection",
      "@type": "@id"
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
    "title": "dcterms:title",
    "description": "dcterms:description",
    "keywords": "dcterms:subject",
    "license": "dcterms:license",
    "start_datetime": {
      "@id": "stac:core/start_datetime",
      "@type": "xsd:dateTime"
    },
    "end_datetime": {
      "@id": "stac:core/end_datetime",
      "@type": "xsd:dateTime"
    },
    "providers": "stac:core/hasProvider",
    "media_type": "dcterms:format",
    "datetime": {
      "@id": "dcterms:date",
      "@type": "xsd:dateTime"
    },
    "dcterms": "http://purl.org/dc/terms/",
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
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-map/context.jsonld)

## Sources

* [POSEIDON MapInitializer YAML samples](https://github.com/poseidon-fisheries/POSEIDON/blob/main/POSEIDON/inputs/YAML%20Samples/components/MapInitializer.yaml)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/_stage/poseidon-input-map`

