# POSEIDON Regulation and Policy Input

Regulation and policy inputs describe management actions consumed by POSEIDON, including closures, protected areas, quotas, gear restrictions, conditional rules, action-specific regulations, and exogenous shocks or interventions. These inputs may be embedded in a scenario or supplied as an additional policy file for a run or optimization experiment.

## Pilot area: Swedish Baltic, north of Gotland Island

Regulatory landscape applicable to SD 27/29:

- **EU TACs**: annual Council Regulation for Baltic stocks (latest at time of writing: Reg (EU) 2024/257 for fishing year 2025; 2025-yr regulation for 2026). TAC for Central Baltic herring, Baltic sprat, Eastern Baltic cod (zero catch advice), salmon Main Basin.
- **Multiannual plan**: Reg (EU) 2016/1139 (Baltic MAP) — F-ranges and escapement strategies.
- **Technical measures**: Reg (EU) 2019/1241 — gear restrictions, minimum sizes, area technical specs.
- **National Swedish rules**: HaV regulations FIFS 2004:36 (and amendments) — coastal closures, gear permits, recreational rules.
- **Spatial closures**: HELCOM MPAs + Natura 2000 sites + Sweden national fishing-free zones (e.g. Gotska Sandön no-take), all from [poseidon-input-map].
- **Recent shocks**: Eastern Baltic cod targeted-fishery moratorium (2019→ongoing), Bothnian-Sea herring TAC cuts (2023→).

## Source availability for the pilot area

| Source | Role | Coverage of SD 27 / 29 | Provides | Feeds POSEIDON field(s) | Related bblock(s) | Format at origin | Licence |
|---|---|---|---|---|---|---|---|
| EU Council Baltic TAC Regulation (annual, EUR-Lex) | **R** | Whole Baltic, by stock × Member State | Annual TAC tonnes, quota share | `regulations[]` of `type: "Quota"`; `actions: {tac_tonnes, ms_share}` | [poseidon-input-biology] (species names) | OJ HTML/PDF + Cellar JSON | EC Open |
| EU MAP Reg (EU) 2016/1139 (Baltic multiannual plan) | **R** | Whole Baltic | F-ranges, escapement, harvest-control rule | `conditions` on Quota regulation (HCR formula) | – | Consolidated text + Cellar | EC Open |
| EU Technical Measures Reg (EU) 2019/1241 | **R** | EU waters incl. Baltic | Mesh sizes, gear bans, minimum landing sizes | `regulations[]` of `type: "Gear Restriction"`; `actions: {min_mesh_mm, allowed_gears[]}` | [poseidon-input-fleet] (gear taxonomy) | Consolidated text | EC Open |
| Swedish HaV regulations (FIFS 2004:36 etc.) | **R / S** for SE-only rules | Swedish EEZ | National coastal closures, recreational rules, area-specific permits | `regulations[]` of `type: "Seasonal Closure"` / `"Protected Area"` | [poseidon-input-map] (closure polygons) | PDF / Swedish regulation portal | Swedish PSI Open |
| HELCOM MPA management plans | **R** for HELCOM closures | Whole Baltic incl. SE MPAs | Management category, allowed activities per MPA | `actions` payload of `Protected Area` regulations (which gears/seasons) | [poseidon-input-map] | PDF + WFS metadata | CC-BY 4.0 |
| Natura 2000 site management plans (Sweden) | **R** for SCI/SPA-driven restrictions | Swedish Natura 2000 marine sites | Conservation measures per site | Same as above for SCI/SPA polygons | [poseidon-input-map] | PDF + EEA Article 17 reporting | CC-BY 4.0 / national open |
| Sweden Naturvårdsverket MPA decisions | **S** | Swedish marine reserves | National designation rules | Augment HELCOM/Natura rules | [poseidon-input-map] | PDF / GeoPackage | Swedish PSI Open |
| ICES advice (annual stock-by-stock) | **R / S** if MAP HCR is run | Baltic stocks | F_msy ranges, ICES-advised TAC | Feeds Quota `actions.advised_tac` and HCR closure of the loop | [poseidon-input-biology] | PDF + SAG JSON | ICES Data Policy (open) |
| STECF EWG closure-impact reports | **V** | Baltic stocks | Ex-post impact of closures | Validation of regulation effect | [poseidon-input-observation-output] | PDF | EC Open |
| HELCOM BSAP 2021 (Baltic Sea Action Plan) | **S** for scenario regulation overlays | Whole Baltic | Long-horizon environmental targets | Used by [poseidon-input-scenario] as a regulation-scenario overlay | [poseidon-input-scenario] | PDF + Indicator API | CC-BY 4.0 |
| EU CFP reform proposals (in legislative pipeline) | **S** for forecast scenarios | EU-wide | Proposed rule changes | Forward-looking `shocks[]` | [poseidon-input-scenario] | EUR-Lex Cellar | EC Open |
| EU fisheries inspections (control reports) | **V** | EU-wide | Historical compliance, infringement counts | Compliance-rate calibration | [poseidon-input-fleet] | PDF | EC Open |

[poseidon-input-biology]: ../poseidon-input-biology/
[poseidon-input-fleet]: ../poseidon-input-fleet/
[poseidon-input-map]: ../poseidon-input-map/
[poseidon-input-scenario]: ../poseidon-input-scenario/
[poseidon-input-optimization]: ../poseidon-input-optimization/
[poseidon-input-observation-output]: ../poseidon-input-observation-output/

## Two-stage transformation pipeline

Stage A normalises each source to **EDITO Data Lake** form. Regulations are largely *legal text* — Stage A here is dominated by **structured extraction** from PDFs / EUR-Lex Cellar JSON-LD into Parquet rule tables. STAC Collection: `poseidon-regulation-north-gotland`.

### Stage A — Source → EDITO

| Source | EDITO artefact | Transformation |
|---|---|---|
| EU Council Baltic TAC Regulation | `regulation/tac.parquet` | Pull EUR-Lex Cellar JSON-LD for the annual regulation; extract Annex tables with structured-extraction (LLM-assisted + regex fallback); columns `stock_code, year, member_state, tac_tonnes, special_conditions[]`. |
| EU MAP Reg (EU) 2016/1139 | `regulation/map_hcr.parquet` (one-row reference table) | Encode HCR parameters: `stock_code, f_lower, f_upper, b_lim, b_pa, b_trigger, escapement_target`. |
| EU Technical Measures Reg (EU) 2019/1241 | `regulation/tech_measures.parquet` | Extract Annex VIII (Baltic) tables; columns `gear_lvl4, area_code, min_mesh_mm, min_size_species_aphia, allowed_codend_devices[]`. |
| Swedish HaV regulations (FIFS) | `regulation/se_national.parquet` (GeoParquet where the rule is geographic) | Parse FIFS chapters; for spatial rules, geo-reference the area description against the Swedish coastal polygons; columns `rule_id, rule_type, area_code, start_day, end_day, gear_in_scope[], species_in_scope[], geometry`. |
| HELCOM MPA management plans | `regulation/helcom_mpa_rules.parquet` (joined to `helcom_mpa.parquet` polygon table in [poseidon-input-map]) | Per MPA, extract IUCN category and activity table; columns `mpa_id, gear_in_scope[], species_in_scope[], allowed_periods[]`. |
| Natura 2000 management plans | `regulation/natura_rules.parquet` (joined to `natura2000.parquet`) | Same shape, keyed on `site_code`. |
| ICES advice (SAG + Single Stock Advice docs) | `regulation/ices_advice.parquet` | Pull from icesSAG and ICES advice JSON where available; columns `stock_code, year, advised_tac_tonnes, fmsy, blim, advice_basis`. |
| HELCOM BSAP indicators | `regulation/bsap_targets.parquet` | Pull from HELCOM Indicators API; columns `indicator_id, target_value, threshold_type, target_year`. |
| EU CFP reform proposals | `regulation/cfp_proposals.parquet` | Curated by year; columns `proposal_id, in_force_from, summary, projected_effects[]`. |

All artefacts are vector-free except spatial-rule rows, which carry a `geometry` linking back to the polygon set in [poseidon-input-map].

### Stage B — EDITO → POSEIDON

| EDITO artefact | POSEIDON field(s) | Transformation |
|---|---|---|
| `tac.parquet` + `map_hcr.parquet` + `ices_advice.parquet` | `regulations[]` of `type: "Quota"` with `species, startDay: 1, endDay: 365, conditions: {hcr: ...}, actions: {tac_tonnes, ms_share}` | Join TAC × HCR × advice on `stock_code, year`; filter to `member_state = SWE` for Sweden quota share. |
| `tech_measures.parquet` | `regulations[]` of `type: "Gear Restriction"`; `actions: {min_mesh_mm, allowed_gears[], min_size_species[]}` | Filter to Annex VIII Baltic rows; map `gear_lvl4` to model `gear.type` via the DCF lookup from [poseidon-input-fleet]. |
| `helcom_mpa_rules.parquet` + `natura_rules.parquet` + `se_national.parquet` (spatial) | `regulations[]` of `type: "Protected Area"` with `areas: [{closureId: ...}]`, `actions: {forbidden_gears[], forbidden_species[]}` | `closureId` is the same ID present in [poseidon-input-map]'s closure mask; `areas` carries only the ID, not the geometry. |
| `se_national.parquet` (seasonal rules) | `regulations[]` of `type: "Seasonal Closure"`, `startDay`, `endDay`, `species`, `areas` | Convert calendar dates → day-of-year integers; seasonal rules are emitted independently of MPA rules. |
| `cfp_proposals.parquet` + `bsap_targets.parquet` | `shocks[]` entries (timed interventions) | Each row → one `shocks[]` element with `applyAtYear, payload`; the payload references which subsequent regulation rows become active. |

## Required vs substitutable vs validation-only

### Required path

| Regulation complexity | Minimum required sources |
|---|---|
| TAC-only (no spatial closures) | EU Council Baltic TAC Regulation (R) + EU MAP (R) + ICES advice (R) |
| TAC + technical measures | Same + EU Technical Measures Reg 2019/1241 (R) |
| Full management baseline | Same + HELCOM MPA management plans (R) + Natura 2000 plans (R) + HaV FIFS (R) |
| Forecast scenario with proposed rules | All of the above + EU CFP proposals (S) + HELCOM BSAP targets (S) as `shocks[]` |

### Substitutable

- **Source of HCR**: EU MAP (preferred) **xor** ICES advice basis text (used only when MAP HCR is silent for a stock).
- **Spatial-closure rule set**: HELCOM MPA + Natura 2000 (stacked, complementary) **xor** WDPA fallback (only if HELCOM unavailable — never both).
- **Forecast regulation overlay**: EU CFP proposals **xor** HELCOM BSAP indicators — pick one narrative per scenario.

### Validation-only

- STECF closure-impact reports — ex-post calibration of effort displacement assumptions.
- EU fisheries inspection / infringement statistics — compliance-rate priors.

Wired through [poseidon-input-observation-output] manifest `validationLinks[]` and through `events[]` (compliance breaches as discrete events).

### Minimal viable bundle for the pilot

1. **EU Council Baltic TAC Regulation** for the simulated year(s).
2. **EU MAP Reg (EU) 2016/1139** HCR table.
3. **EU Technical Measures Reg (EU) 2019/1241** gear-restriction rows for Annex VIII (Baltic).
4. **HELCOM MPA + Natura 2000 management plans** for the closures co-keyed with [poseidon-input-map].

This is enough to run a status-quo regulation scenario. Forecast scenarios add CFP proposals or BSAP targets via `shocks[]`.

## Cross-bblock contract

- `regulations[].species` MUST match `species[].name` in [poseidon-input-biology].
- `regulations[].areas[].closureId` MUST exist in [poseidon-input-map]'s closure mask.
- `regulations[]` gear references MUST conform to the gear taxonomy used in [poseidon-input-fleet] (DCF Level-4 / Level-6).
- TAC `actions.tac_tonnes` for the simulated start year is the **regulator-side** quantity; the corresponding **fleet-side** behavioural response (effort displacement) is parameterised in [poseidon-input-fleet] `fishers[].adaptation` and may be the search variable in [poseidon-input-optimization].
- The status-quo / proposed switch lives in [poseidon-input-scenario] — this bblock supplies both rule sets; the scenario picks the active one.
