# POSEIDON Port and Market Input

This block describes port and market inputs consumed by POSEIDON: port positions, grid-coordinate or geographic coordinate flags, landing infrastructure, market price configuration by species, price files, and fuel or gas price settings.

## Pilot area: Swedish Baltic, north of Gotland Island

The dominant landing ports for the pilot are **Simrishamn**, **Karlskrona**, **Västervik**, **Slite**, **Stockholm-Frihamnen** and **Hudiksvall**. SSCF segments additionally land at smaller archipelago harbours (Öregrund, Trosa, Mönsterås) that are not in the Eurostat-harmonised port list and have to be supplemented from OpenStreetMap (see [poseidon-input-map]). Target species for the price table: Central Baltic herring, Baltic sprat, perch, pike, salmon (E. Baltic cod priced at zero quota — kept for back-cast only).

## Source availability for the pilot area

Role classification (same convention as [poseidon-input-biology] / [poseidon-input-fleet] / [poseidon-input-map]):
- **R** = *Required* — model cannot start without it.
- **S** = *Substitutable* — pick one per role; do not stack.
- **V** = *Validation-only*.

| Source | Role | Coverage of SD 27 / 29 | Provides | Feeds POSEIDON field(s) | Related bblock(s) | Format at origin | Licence |
|---|---|---|---|---|---|---|---|
| EMODnet Human Activities — Main Ports | **R** | EU + Baltic | Port positions, UN/LOCODE, traffic class | `ports[].name, .longitude, .latitude` | [poseidon-input-map], [poseidon-input-fleet] | Shapefile / WFS | CC-BY 4.0 |
| UN/LOCODE | **R** | Global | Authoritative port code | `ports[].name` carrier (the key linking back to fleet `homePort`) | [poseidon-input-fleet] | CSV | UN open |
| OpenStreetMap — small harbours | **S** complement | Sweden incl. archipelago | Small SSCF landing sites missing from EMODnet | Adds SSCF ports to `ports[]` | [poseidon-input-map] | PBF / Overpass | ODbL |
| EUMOFA monthly first-sale prices | **R** | EU + Sweden by port × species × month | First-sale price EUR/kg | `market.priceBySpecies` (latest year), `market.priceFile` (monthly series) | [poseidon-input-biology] (species name crosswalk) | CSV / API | EC Open |
| Swedish HaV landings & first-sale | **R** for SSCF prices | Swedish ports, all segments incl. coastal | Per-trip first-sale value, by species and gear | Refines `market.priceFile` for archipelago harbours where EUMOFA is too coarse | [poseidon-input-fleet] | CSV / API | Swedish PSI Open |
| EU Weekly Oil Bulletin (DG ENER) | **R / S** for fuel | EU + Sweden, weekly | Diesel pump and excl-tax prices by Member State | `fuel.fuelPrice` (scalar), `fuel.fuelPriceFile` (time-series) | [poseidon-input-scenario] | Excel / CSV | EC Open |
| Eurostat PRC_PEME (Energy prices) | **S** alternative to Oil Bulletin | EU + Sweden, semi-annual / annual | Industrial / commercial energy prices | Same as Oil Bulletin (coarser cadence) | – | CSV / SDMX API | EC Open |
| STECF AER fuel cost share | **S** for fuel-cost-of-segment | EU + Sweden by segment × year | Fuel cost as fraction of revenue per segment | Calibration prior for fuel-elasticity assumptions in fleet adaptation | [poseidon-input-fleet] | Excel | EC Open |
| SCB Fishery statistics (Statistics Sweden) | **V** | Swedish landings, monthly | National landings value vs volume | Validation of price/volume relationship | [poseidon-input-observation-output] | CSV | CC0 |
| Auction-house data (Karlskrona, Simrishamn) | **V** | Specific Swedish ports | Per-auction prices and volumes | Validation of port-level price formation | [poseidon-input-observation-output] | CSV / scraping | Mixed |

[poseidon-input-biology]: ../poseidon-input-biology/
[poseidon-input-fleet]: ../poseidon-input-fleet/
[poseidon-input-map]: ../poseidon-input-map/
[poseidon-input-regulation-policy]: ../poseidon-input-regulation-policy/
[poseidon-input-scenario]: ../poseidon-input-scenario/
[poseidon-input-observation-output]: ../poseidon-input-observation-output/

## Two-stage transformation pipeline

Stage A normalises each source to **EDITO Data Lake** form (GeoParquet 1.1 vector / Parquet for non-spatial / GeoZarr v3 grid). STAC Collection: `poseidon-portmarket-north-gotland` under `s3://edito-pilot/north-gotland/portmarket/`.

### Stage A — Source → EDITO

| Source | EDITO artefact | Transformation |
|---|---|---|
| EMODnet HA Main Ports + UN/LOCODE + OSM small harbours | `portmarket/ports.parquet` (GeoParquet, POINT) | Inherit the table built in [poseidon-input-map]; subset to ports active for fishing landings (Eurostat traffic class includes Fishing or OSM `harbour:type=fishing`). |
| EUMOFA monthly first-sale prices | `portmarket/eumofa_prices.parquet` (already produced in [poseidon-input-fleet] Stage A; re-used here) | Same artefact. Columns `species_aphia_id, locode, year, month, eur_per_kg`. |
| Swedish HaV landings & first-sale | `portmarket/se_hav_prices.parquet` | Aggregate trip-level value/weight to `(locode, species_aphia_id, year, month)`; columns `locode, species_aphia_id, year, month, eur_per_kg, volume_kg`. |
| EU Weekly Oil Bulletin | `portmarket/fuel_prices.parquet` | Pull weekly XLS; long-format `country, week_start, price_excl_tax_eur_per_l, price_incl_tax_eur_per_l`; clip to SE rows. |
| Eurostat PRC_PEME | `portmarket/eurostat_energy.parquet` | SDMX query; only if Oil Bulletin not used. |
| STECF AER fuel cost share | re-uses `fleet/aer_segment_econ.parquet` from [poseidon-input-fleet] | No copy. |
| SCB / auction-house data | `portmarket/validation_prices.parquet` | Standard schema; held for `validationLinks[]`. |

### Stage B — EDITO → POSEIDON

| EDITO artefact | POSEIDON field(s) | Transformation |
|---|---|---|
| `ports.parquet` | `ports[]` with `name, longitude, latitude, usingGridCoordinates: false`; `portInitializerType: "List of Ports"` | One element per fishing-active port; LOCODE carried in `name` to keep cross-bblock joins clean. |
| `eumofa_prices.parquet` (+ `se_hav_prices.parquet` overlay for SSCF) | `market.priceBySpecies` (scalar map for start year) **and** `market.priceFile` (path to monthly CSV) | Pivot `(species_aphia_id, port?)` × month → wide; pick start-year mean for the scalar map; full monthly series → CSV referenced from `market.priceFile`. Where SE HaV and EUMOFA both cover a (port, species), prefer SE HaV (vessel-level basis). |
| `fuel_prices.parquet` | `fuel.fuelPrice` (scalar mean) and `fuel.fuelPriceFile` (path) | Mean weekly SE diesel for start year → scalar; full weekly series → CSV. |
| – | `fuel.gasPriceMaker` | `"Fixed"` if a scalar is used; `"Time-varying File"` if a `fuelPriceFile` is supplied; `"Stochastic"` if drawn from a parameter adaptor in [poseidon-input-optimization]. |

## Required vs substitutable vs validation-only

### Required path

| Market complexity chosen | Minimum required sources |
|---|---|
| Fixed scalar prices | EMODnet HA + UN/LOCODE (ports) + EUMOFA latest-year mean (prices) + EU Oil Bulletin scalar (fuel) |
| Time-varying prices and fuel | Same + EUMOFA monthly series + EU Oil Bulletin weekly series |
| SSCF-resolved prices | Same + Swedish HaV first-sale overlay + OSM small harbours |

### Substitutable

- **Fuel price**: EU Weekly Oil Bulletin (preferred — weekly granularity) **xor** Eurostat PRC_PEME (annual fallback).
- **Port-level SSCF prices**: Swedish HaV first-sale (preferred for archipelago) **xor** SCB Fishery statistics (coarser).

### Validation-only

- SCB Fishery statistics monthly national volumes vs revenues.
- Auction-house transaction data for a subset of ports.

Wired through [poseidon-input-observation-output] manifest's `validationLinks[]`.

### Minimal viable bundle

1. **EMODnet HA Main Ports** + **UN/LOCODE** for the port catalog (Re-used from [poseidon-input-map]).
2. **EUMOFA first-sale prices** for target species; pick start-year mean.
3. **EU Weekly Oil Bulletin** scalar SE diesel price for start year.

## Cross-bblock contract

- `ports[].name` MUST be a UN/LOCODE present in [poseidon-input-map]'s `farOffPorts[]` and used by [poseidon-input-fleet]'s `fishers[].homePort`. Three-way consistency is enforced by the runner.
- `market.priceBySpecies` keys MUST match `species[].name` in [poseidon-input-biology].
- `fuel.fuelPrice` granularity (scalar vs file) is correlated with [poseidon-input-run-control]'s `yearsToRun`: a multi-year run with a scalar fuel price is allowed only as a simplification — the runner emits a warning.
- Stochastic price/fuel adaptors are parameterised in [poseidon-input-optimization] with bounds informed by EUMOFA / Oil Bulletin historical variance.
