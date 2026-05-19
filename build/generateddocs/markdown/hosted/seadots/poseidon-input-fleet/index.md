
# POSEIDON Fleet and Fisher Input (Schema)

`ogc.hosted.seadots.poseidon-input-fleet` *v0.1*

Schema for fleet, fisher, vessel, gear, behavioural strategy, social-network, logbook, and adaptation inputs consumed by POSEIDON.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# POSEIDON Fleet and Fisher Input

Fleet inputs configure the fishing-agent side of POSEIDON. They include fisher counts, home ports, vessels, gear, destination/departure/fishing/gear strategies, discarding, logbook initialization, adaptation probabilities, and social-network structures used by imitation and learning behaviour.

## Pilot area: Swedish Baltic, north of Gotland Island

ICES Subdivisions 27 and 29 (and the Bothnian Sea fringe, SD 30). The Swedish Baltic fleet operating there is dominated by:

- **Pelagic trawlers** (TM/OTM, ≥ 24 m LOA) targeting Central Baltic herring and sprat — concentrated in Simrishamn, Västervik, Karlskrona; some Storebro / Slite landings.
- **Small-scale coastal vessels** (PG, FPN, GNS, 0–8 m and 8–12 m segments) targeting perch, pike, whitefish, salmon and herring in the archipelago — Stockholm archipelago, Öregrund, Hudiksvall, Slite.
- **Demersal trawl / gillnet** activity on Eastern Baltic cod is effectively at zero quota; included for back-cast / validation runs only.

## Source availability for the pilot area

Role classification (same convention as [poseidon-input-biology]):
- **R** = *Required* — model cannot start without it.
- **S** = *Substitutable* — pick one per role; do not stack alternatives.
- **V** = *Validation-only* — compared against fleet outputs after a run.

| Source | Role | Coverage of SD 27 / 29 | Provides | Feeds POSEIDON field(s) | Related bblock(s) | Format at origin | Licence |
|---|---|---|---|---|---|---|---|
| EU Fleet Register (CFR) | **R** | Per-vessel, Sweden flag | LOA, GT, kW, mainGear, hull material, registration port, MMSI link | `fishers[].vessel`, `.gear.type`, `.homePort`, `.count` (after grouping) | [poseidon-input-port-market], [poseidon-input-map] | CSV / XML (Fleet-Europa portal) | EC Open |
| STECF AER (Annual Economic Report) | **R / S** for segment averages | EU + Sweden, by fleet segment (LOA × gear) including Baltic SSCF 0-8/8-12 m | Days-at-sea, fuel use, GVA, crew cost, capital, fuel intensity | `fishers[].vessel.fuelCapacity`, `.holdCapacity`, `.crewSize`; per-segment `count`; `adaptation` priors | [poseidon-input-port-market], [poseidon-input-optimization] | Excel / CSV | EC Open |
| ICES VMS & Logbook DB (WGSFD) | **R** for spatial-effort init / **S** vs AIS sources | C-square (0.05°≈ 3 km), métier-resolved, 2009–present; HELCOM 2016–2021 product published | Fishing hours by métier per C-square per year | `fishers[].destinationStrategy` prior heatmap; `.logbook` initial state | [poseidon-input-map], [poseidon-input-regulation-policy] (closure overlay) | CSV via web service | ICES Data Policy (open, aggregated) |
| EMODnet Human Activities — Vessel Density Maps (Fishing) | **S** alternative to VMS | 1 km grid, monthly, EU waters incl. Baltic | AIS-derived ship-hours per cell, ship type 1 = Fishing | Same as VMS but coarser métier | [poseidon-input-map] | GeoTIFF | CC-BY |
| Global Fishing Watch (GFW) Apparent Fishing Effort | **S** alternative to VMS | 0.01° daily, gear-class taxonomy, 2012–2024 public | Fishing hours by flag × gear-class × cell × day | Same as VMS — finer time resolution, coarser métier | [poseidon-input-map], [poseidon-input-scenario] | CSV / Parquet / R+Python SDK | CC-BY-NC 4.0 (research) |
| HELCOM Map & Data Service — fishing intensity 2016-2021 | **V** | Whole Baltic incl. SD 27/29 | Aggregated VMS intensity (re-publication of ICES product) | Validation of modelled spatial effort | [poseidon-input-observation-output] | GeoPackage / WMS / WFS | CC-BY |
| Swedish HaV national fleet & landings | **R** for Swedish coastal segments (0-8 / 8-12 m) | Swedish flag, by port and fleet segment | Vessel-level catch and trip records (aggregated); landings declarations | `fishers[].logbook`, `.count` for SSCF | [poseidon-input-port-market] | CSV / API | Swedish PSI Open |
| SLU Aqua catch & effort statistics | **S** for SSCF where HaV is not granular enough | Swedish coast incl. SD 27/29 | Coastal catch & effort by gear and reference area | `fishers[].logbook` priors; coastal `count` | [poseidon-input-biology] (coastal stocks) | CSV / API | CC-BY 4.0 |
| EU Data Collection Framework (DCF) métier-by-segment | **S** for métier classification | EU + Sweden | DCF Level-6 métier codes per segment | Crosswalk that defines `gear.type` taxonomy used across the model | [poseidon-input-regulation-policy] | CSV (RDB-FIS) | EC Open |
| AIS raw feeds (Spire, Orbcomm) | **V** + alternative source | Whole Baltic | Per-MMSI positions, speed, heading | Validation of `.destinationStrategy` traces | [poseidon-input-observation-output] | NMEA / Parquet | Commercial |
| EUMOFA price observatory | **R** for adaptation revenue calc | EU + Sweden | First-sale price per species per port per month | `fishers[].adaptation` revenue priors (link only — actual prices live in [poseidon-input-port-market]) | [poseidon-input-port-market] | CSV / API | EC Open |

[poseidon-input-biology]: ../poseidon-input-biology/
[poseidon-input-map]: ../poseidon-input-map/
[poseidon-input-port-market]: ../poseidon-input-port-market/
[poseidon-input-regulation-policy]: ../poseidon-input-regulation-policy/
[poseidon-input-observation-output]: ../poseidon-input-observation-output/
[poseidon-input-optimization]: ../poseidon-input-optimization/
[poseidon-input-scenario]: ../poseidon-input-scenario/

## Two-stage transformation pipeline

Stage A normalises each source to **EDITO Data Lake** form (GeoParquet 1.1 vector / GeoZarr v3 grid, STAC-indexed under collection `poseidon-fleet-north-gotland`, persisted under `s3://edito-pilot/north-gotland/fleet/`). Stage B projects EDITO artefacts to the POSEIDON `fishers[]` / `socialNetwork` schema.

### Stage A — Source → EDITO

| Source | EDITO artefact | Transformation |
|---|---|---|
| EU Fleet Register | `fleet/cfr_vessels.parquet` (GeoParquet, registration-port POINT) | Pull CSV from Fleet-Europa filtered by country = SE; geocode `registration_port_name` against the EU port code list (UN/LOCODE) to attach POINT; columns `cfr, mmsi, vessel_name, loa_m, gt, kw, main_gear_lvl4, registration_port_locode, geometry`. |
| STECF AER | `fleet/aer_segment_econ.parquet` (non-spatial Parquet) | Pull AER Excel; pivot to long format `country, supra_region=Baltic Sea, segment_id, year, indicator, value`; segment IDs follow DCF Level-3 (e.g. `BSA_DTS_VL1218`). |
| ICES VMS & Logbook | `fleet/vms_effort.parquet` (GeoParquet, C-square polygon) | Use `icesVMS` R package or ICES web service to pull C-square aggregates filtered by `ICES_area ∈ {27, 28, 29, 30}`; build cell polygons from C-square code; columns `csquare, geometry, year, metier_lvl6, fishing_hours, kw_hours, total_weight_kg`. |
| EMODnet HA Vessel Density (Fishing) | `fleet/emodnet_vd_fishing.zarr` (GeoZarr) | Stack monthly GeoTIFFs for ship type 1 (Fishing); rechunk to `time=12, lat=512, lon=512`; clip to pilot bbox `[16.0, 56.5, 21.5, 60.0]`; preserve unit `h/km²/month`. |
| Global Fishing Watch | `fleet/gfw_effort.parquet` partitioned by `year` | Pull via `gfwr` R SDK or download portal; columns `cell_ll, year, month, flag, gear_class, fishing_hours`; clip cell centroids to pilot bbox. |
| HELCOM fishing-intensity product | Reference-only STAC Item pointing at HELCOM WFS | No copy; expose as `application/vnd.ogc.wfs`. |
| Swedish HaV landings & effort | `fleet/se_hav_landings.parquet` (GeoParquet, port POINT) | Pull HaV open-data CSVs; harmonise with CFR via `cfr` join key; columns `cfr, trip_id, departure_locode, return_locode, gear, species_aphia_id, weight_kg, value_sek, geometry`. |
| SLU Aqua coastal catch | `fleet/slu_coastal_catch.parquet` | Same shape as KUL in [poseidon-input-biology] but with `effort_h` and `gear` fields preserved. |
| DCF Level-6 métier list | `fleet/dcf_metier_lookup.parquet` (lookup table) | Read DCF appendix; columns `metier_lvl6, gear, target_assemblage, mesh_range, selectivity_device`. |
| EUMOFA prices | `fleet/eumofa_prices.parquet` | Pull monthly first-sale price table; columns `species_aphia_id, locode, year, month, eur_per_kg`. |

### Stage B — EDITO → POSEIDON

| EDITO artefact | POSEIDON field(s) | Transformation |
|---|---|---|
| `cfr_vessels.parquet` | `fishers[]` grouped by `(main_gear_lvl4, loa_band, registration_port_locode)`; each group becomes one `fishers[]` element with `count`, `homePort`, `vessel{loa, gt, kw}`, `gear.type` | Bin LOA into model bands (e.g. <8, 8–12, 12–24, ≥24); set `count` = number of vessels in the group; `homePort` = LOCODE (must also appear in [poseidon-input-port-market]). |
| `aer_segment_econ.parquet` | `fishers[].vessel.fuelCapacity`, `.crewSize`, `.holdCapacity`; `fishers[].adaptation.explorationProbability` (prior) | Pick year matching `poseidon-input-run-control.startYear`; join on `segment_id` derived from `(gear, loa_band)`; fuel intensity → fuel capacity given typical trip length. |
| `vms_effort.parquet` | `fishers[].destinationStrategy = {type: "WeightedHeatmap", weights: <csquare → hours>}`; `fishers[].logbook = {historicEffort: ...}` | Aggregate hours by `(metier_lvl6, csquare)` for the start year (or 3-year mean); normalise to a probability surface; CSV is referenced as `dataFiles[]` and the path embedded in `destinationStrategy.weightsFile`. |
| `emodnet_vd_fishing.zarr` *(if VMS not used)* | Same `destinationStrategy.weightsFile` | Average over chosen years → 1 km raster → convert to C-squares or model cells, then identical normalisation. |
| `gfw_effort.parquet` *(if VMS not used)* | Same `destinationStrategy.weightsFile` | Filter to `flag = SWE` (or the modelled fleet's flag set); aggregate by `(gear_class, cell)`; convert GFW `gear_class` to model `gear.type` via the DCF lookup. |
| `se_hav_landings.parquet` | `fishers[].logbook = {priorTrips: ...}`; `fishers[].discardingStrategy` if discard columns present | Aggregate trips by fisher group; convert to per-fisher mean trip catch composition; reference `dataFiles[]`. |
| `slu_coastal_catch.parquet` | `fishers[]` for coastal perch/pike segments — `count`, `gear`, `homePort` | One `fishers[]` element per reference area × gear; `count` from active-gear-day proxies. |
| `dcf_metier_lookup.parquet` | Drives mapping CFR `main_gear_lvl4` ↔ `gear.type` enum | Lookup at Stage B; output canonical model `gear.type` strings (e.g. `OTM_SPF` for pelagic midwater trawl targeting small pelagics). |
| `eumofa_prices.parquet` | Pointer only — actual fields live in [poseidon-input-port-market]; this bblock records the FK | Add an entry to `fishers[].adaptation.priceTableRef` referencing the port-market STAC Item. |
| (derived) port co-membership graph | `socialNetwork = {type: "Directed Graph", edgesFile: ...}` | Build edges between fishers sharing `homePort`; weight by gear similarity (Jaccard on métier set) and LOA proximity; export GraphML / Parquet edges. |

### Required vs substitutable vs validation-only

#### Required path — minimum to start a run

| Behavioural complexity chosen | Required sources | Optional drivers |
|---|---|---|
| Static fleet (no learning) — fixed gear, no adaptation | CFR (R) + STECF AER (R) | DCF métier lookup (recommended) |
| Adaptive fleet with spatial-effort prior | CFR (R) + STECF AER (R) + **one of** {ICES VMS, EMODnet HA, GFW} (R/S) + DCF métier lookup (R) | EUMOFA prices via port-market bblock |
| Adaptive fleet + full logbook initialization | All of the above + Swedish HaV landings (R) | SLU Aqua coastal catch for SSCF |

#### Substitutable — XOR rules

- **Spatial-effort prior**: ICES VMS (preferred — métier-resolved, regulator-grade) **xor** EMODnet HA Vessel Density **xor** Global Fishing Watch. Choosing more than one and averaging produces non-reproducible heatmaps.
- **Per-vessel attributes**: CFR (preferred, per-vessel) **xor** STECF AER segment averages (only when individual-vessel resolution is not required).
- **Métier taxonomy**: DCF Level-6 (preferred) **xor** GFW gear-class taxonomy (only if GFW is the sole spatial source).

#### Validation-only

- HELCOM 2016-2021 fishing intensity product (republished VMS) — sanity check on the modelled effort distribution.
- Raw AIS feeds — per-MMSI track validation of `destinationStrategy` if licences allow.
- Held-out years of VMS / GFW effort.

The validation harness is wired through [poseidon-input-observation-output] — that bblock declares which fleet variables are observed; this bblock declares which empirical series they are compared against.

### Minimal viable bundle for the pilot

1. **EU Fleet Register (CFR)** filtered to Swedish flag, ports in SD 27/29 catchment — defines vessel agents.
2. **STECF AER** Baltic segments for the chosen start year — fills vessel economics and behavioural priors.
3. **ICES VMS & Logbook** (or GFW if a VMS data-call licence is not in place) — defines the destination-strategy prior.
4. **DCF Level-6 métier lookup** — closes the gear taxonomy gap.

Everything else either substitutes for one of the four above, refines small-scale-coastal segments, or sits in the validation harness.

### Cross-bblock contract

- `fishers[].homePort` values MUST resolve to ports declared in [poseidon-input-port-market].
- `fishers[].gear.type` values MUST conform to the gear taxonomy referenced in [poseidon-input-regulation-policy] (which carries gear-specific closures and quotas).
- Spatial-effort priors materialised here MUST use the same C-square / model-cell grid as declared in [poseidon-input-map].
- Adaptive-fleet behavioural priors are calibrated against historical logbooks; the target metrics live in [poseidon-input-optimization].
- The "future" vs "past" axis (forecast vs reanalysis Copernicus, near-real-time vs back-cast VMS) is selected in [poseidon-input-scenario] — this bblock does not switch on time-axis itself.

## Examples

### Simple adaptive fleet input
#### json
```json
{
  "fishers": [
    {
      "name": "small-vessel-fleet",
      "count": 50,
      "homePort": "Main Port",
      "gear": {
        "type": "Random Catchability",
        "catchability": 0.001
      },
      "destinationStrategy": {
        "type": "Bandit Destination"
      },
      "adaptation": {
        "explorationProbability": 0.1,
        "imitationProbability": 0.2
      }
    }
  ],
  "socialNetwork": {
    "type": "Directed Graph"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-fleet/context.jsonld",
  "fishers": [
    {
      "name": "small-vessel-fleet",
      "count": 50,
      "homePort": "Main Port",
      "gear": {
        "type": "Random Catchability",
        "catchability": 0.001
      },
      "destinationStrategy": {
        "type": "Bandit Destination"
      },
      "adaptation": {
        "explorationProbability": 0.1,
        "imitationProbability": 0.2
      }
    }
  ],
  "socialNetwork": {
    "type": "Directed Graph"
  }
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/iliad/seadots/poseidon/input#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] schema:agent ( [ schema:homeLocation "Main Port" ;
                schema:name "small-vessel-fleet" ;
                :adaptation [ :explorationProbability 1e-01 ;
                        :imitationProbability 2e-01 ] ;
                :count 50 ;
                :destinationStrategy [ :type "Bandit Destination" ] ;
                :gear [ :catchability 1e-03 ;
                        :type "Random Catchability" ] ] ) ;
    :socialNetwork [ :type "Directed Graph" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: POSEIDON Fleet and Fisher Input
description: Fleet and fisher-agent configuration consumed by POSEIDON.
type: object
properties:
  fishers:
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
        count:
          type: integer
          minimum: 1
        homePort:
          type: string
          x-jsonld-id: https://schema.org/homeLocation
        vessel:
          type: object
          additionalProperties: true
        gear:
          type: object
          required:
          - type
          properties:
            type:
              type: string
          additionalProperties: true
        departingStrategy:
          type: object
          additionalProperties: true
        destinationStrategy:
          type: object
          additionalProperties: true
        fishingStrategy:
          type: object
          additionalProperties: true
        gearStrategy:
          type: object
          additionalProperties: true
        discardingStrategy:
          type: object
          additionalProperties: true
        adaptation:
          type: object
          additionalProperties: true
        logbook:
          type: object
          additionalProperties: true
    x-jsonld-id: https://schema.org/agent
    x-jsonld-container: '@list'
  socialNetwork:
    type: object
    additionalProperties: true
additionalProperties: true
x-jsonld-vocab: https://w3id.org/iliad/seadots/poseidon/input#
x-jsonld-prefixes:
  schema: https://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-fleet/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-fleet/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/iliad/seadots/poseidon/input#",
    "fishers": {
      "@context": {
        "name": "schema:name",
        "homePort": "schema:homeLocation"
      },
      "@id": "schema:agent",
      "@container": "@list"
    },
    "schema": "https://schema.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/poseidon-input-fleet/context.jsonld)

## Sources

* [POSEIDON YAML component samples](https://github.com/poseidon-fisheries/POSEIDON/tree/main/POSEIDON/inputs/YAML%20Samples/components)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/_stage/poseidon-input-fleet`

