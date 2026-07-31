# Harvest time series scenario Scen M3 — Data Usability Assessment and Check-in

**Piotr Zaborowski**

*Generated with data-usability-checkin-agent (Sonnet 4.6) : 2026-07-28*
*Building blocks generated from the supplied local GeoJSON export `harvest_timeseries_scenario_Scen_M3[539974].geojson`*
*Reviewed by human: pending*

---

## 1. Source Dataset

| Field | Value |
|---|---|
| Name | Harvest time series scenario Scen M3 |
| Programme / owner | Not supplied |
| IDs / DOI | Not supplied |
| Format | GeoJSON FeatureCollection |
| Record count | 19,920 Point features; 83 repeated feature IDs × 240 timestamps |
| Spatial coverage | 7.6425708566666666–7.7134926933333334 E, 54.37364839–54.40949512 N |
| Temporal coverage | 2020-04-30 00:00:00–2020-12-25 00:00:00 (240 distinct, timezone-unspecified timestamps) |
| Theme | Harvest scenario time series (inferred solely from filename) |
| Fields | `id` (integer), Point geometry, `properties.bwmus` (number), `properties.time` (string) |
| Licence | Not supplied |
| Sample / provenance | Local attachment `/Users/piotr/harvest_timeseries_scenario_Scen_M3[539974].geojson`; SHA-256 `be2abe4e83f239888eb9540d7aa1b9bf5c85516546ffec18067147a3f454a554` |

No endpoint or dataset definition accompanied the file. The reproducible sample-extraction script is BB1 `transforms/extract-representative-sample.jq`.

## 2. Usability Assessment

| Criterion | Score | Rationale | Confidence | Evidence | Gap |
|---|---:|---|---|---|---|
| Relevance | Conditional | A spatial time series can support DT analysis, but the semantic meaning of `bwmus` and scenario purpose are unknown. | Low | Filename, Point/time/value structure | Variable definition and intended use |
| Representativeness | Pass | Six raw features are selected from first/final timestamps and three spatial-series IDs, without altering values. | High | SHA-256-pinned source; extraction jq script | No public source endpoint |
| Reliability | Blocked | No producer, methodology, QA, model version or authoritative source was supplied. | High | Attachment contains only features | Owner, lineage, uncertainty and scenario documentation |
| Temporal validity | Conditional | The file spans 240 timestamps in 2020; currentness and timezone are unknown. | High | Field scan | Timezone/calendar and update cadence |
| Ingestability | Pass | Valid GeoJSON FeatureCollection with a stable two-property schema and Point geometries. | High | 19,920 records; no property-type variation | Formal CRS declaration unavailable |
| Reusability in DT framework | Conditional | A SeaDOTs source profile, reproducible transform and OIM Observation target are checked in; semantics remain provisional. | Medium | BB1→BB2 mapping | Units, observed-property URI, licence |
| Initial assessment of data quality | Conditional | Structurally usable for staging and transformation, but not publishable or scientifically interpretable until required provenance and variable semantics are supplied. | High | All above | Blocking metadata gaps below |

### 2.1 Overall assessment

The attachment is machine-ingestible and its geometry/time/value pattern is clear. It is not yet a trustworthy scientific or distributable dataset: `bwmus`, its units, ownership, license, model/scenario lineage, timezone and data-quality information are all absent.

## 3. Field Provenance Classification

### Source fields

| Field | Type | Semantic mapping | Source |
|---|---|---|---|
| `id` | integer | `dct:identifier` | Raw GeoJSON feature ID |
| `geometry` / `coordinates` | GeoJSON Point / number[] | GeoJSON vocabulary | Raw GeoJSON |
| `time` | string | `dct:temporal`; transformed to `sosa:phenomenonTime` | Raw GeoJSON |
| `bwmus` | number | provisional `https://w3id.org/iliad/property/bwmus`; transformed to `sosa:hasSimpleResult` | Raw GeoJSON |

### Derived/resolved fields

`observedProperty`, `phenomenonTime`, and `hasSimpleResult` are transform outputs. They add OIM/SOSA structure but do not change the raw numeric value or timestamp string.

### Synthetic enrichment fields

None. The provisional `bwmus` IRI is a local placeholder, not semantic enrichment; it must be replaced after authoritative documentation is supplied.

## 4. Building Block Selection

Catalog pre-check used local `_sources/` plus the imports declared in `bblocks-config.yaml`. The configured `ogcapi-sosa`, `geodcat-ogcapi-records`, and `bblocks-stac` registers resolved successfully at their `/build/register.json` endpoints on 2026-07-28.

| Role | Catalog / relevance result | Decision |
|---|---|---|
| BB1 source data | Local vector candidates: `macroobservation`, `nina-seapop-source`; neither fits a source-faithful generic scenario time series. | Stage new source profile. |
| BB2 target model | `ogc.hosted.seadots.oim-variable-observation` is the local schema/data match for generic numeric SOSA/OIM observations. | Reuse `ogc.hosted.seadots.oim-variable-observation`; do not mint a duplicate BB2. |
| BB3 metadata | `ogc.hosted.seadots.catalog-data` is the reusable local SeaDOTs Records/DCAT/STAC profile. The dataset-specific Collection record links to it. | Reuse `catalog-data` and keep a narrow dataset-specific catalog record. |

Ranking dimensions that could be computed from the attachment were type and property/model similarity. Vocabulary, semantic-theme and embedding scores are intentionally not decisive because no documentation or vocabulary was supplied.

## 5. Generated Building Blocks

### BB1 — source data

- Path: `_sources/harvest-timeseries-scen-m3-source/`
- ID: `ogc.hosted.seadots.harvest-timeseries-scen-m3-source`
- Purpose: source-faithful Point FeatureCollection profile with all raw properties mapped in `context.jsonld`.
- Added properties: none beyond the raw feature structure.

### BB2 — target model (reused)

- Path: `_sources/oim-variable-observation/`
- ID: `ogc.hosted.seadots.oim-variable-observation`
- Purpose: generic OIM/SOSA observations target. It is reused, not modified.
- Source-property coverage gaps: `bwmus` has no authoritative semantic identifier or unit; the transform uses a provisional project IRI and carries the numeric value as `sosa:hasResult.value`.

### BB3 — metadata/catalog

- Path: `_sources/harvest-timeseries-scen-m3-catalog/`
- ID: `ogc.hosted.seadots.harvest-timeseries-scen-m3-catalog`
- Purpose: STAC Collection / OGC API Records discovery metadata that relates BB1 and BB2.

| Added property | Type | Semantic mapping | Source |
|---|---|---|---|
| `extent` | object | `dct:spatial` | Derived from raw Point coordinates and `time` values |
| `links` | array | `dcat:distribution` | Check-in relationship metadata |
| `keywords` | array | `dcat:keyword` | Filename and format |

## 5a. Transform: BB1 → BB2

The transform is jq because the input and output are GeoJSON JSON structures. It is at `_sources/harvest-timeseries-scen-m3-source/transforms/geojson-to-oim-observation.jq`.

| Source field | Target field | Notes |
|---|---|---|
| `id` | `id` | Retained as a string to avoid conflating repeated spatial IDs with globally unique observation identifiers. |
| `geometry` | `geometry` | Retained unchanged. |
| `time` | `properties.phenomenonTime` | Space is normalised to `T` and `Z` is appended solely to meet the target's `date-time` format; this is provisional pending timezone confirmation. |
| `bwmus` | `properties.hasResult.value` | Numeric value retained unchanged. |
| — | `properties.observedProperty` | Provisional local IRI; not a claim of a formal variable mapping. |

`excluded: {}`: all source properties are represented. The local assertion script is `tests/test-transform.sh`; status: **PASS** (jq transform and source-property assertion).

## 6. Property-Coverage Contract Check

| Rule | BB1 status | BB2 status | BB3 status | Transform status |
|---|---|---|---|---|
| Every source property represented | PASS | PASS with provisional `bwmus` semantics | Links to source/target and gap | PASS |
| Source properties mapped in context | PASS | N/A (reused context) | N/A | N/A |
| Unmappable fields documented | PASS | PASS | PASS | PASS: no excluded fields |
| Real, provenance-recorded examples | PASS | Reused model | Source path + SHA-256 recorded | PASS |

Validation status: JSON syntax, both source/catalog example schemas, and the full-source transform-contract assertion **PASS**. Docker-based `bblocks-postprocess` validation is **not run** because the local Docker daemon is unavailable.

## 7. Identified Metadata Gaps

| Gap | Severity | Resolution |
|---|---|---|
| Variable definition, quantity kind and unit for `bwmus` | Blocking for semantic publication and scientific use | Obtain authoritative model/data dictionary and map to NERC/CF or a documented project vocabulary. |
| Owner, publisher, contact, licence and usage rights | Blocking for distribution | Obtain a dataset landing page or owner-supplied metadata. |
| Scenario/model version, inputs, method and uncertainty | Blocking for quality claims | Supply scenario documentation and QA/validation evidence. |
| Source endpoint / stable distribution URL | Blocking for reproducible public check-in | Supply an accessible endpoint or archival identifier. |
| Timezone/calendar | Medium | Confirm and serialise timestamps as ISO 8601 with offset/calendar. |
| CRS declaration | Medium | Confirm the export CRS; GeoJSON coordinates are treated as WGS 84 only by format convention. |

## 8. References

- Supplied local GeoJSON attachment (checksum above).
- Repository `bblocks-config.yaml` imports: OGC API SOSA, GeoDCAT OGC API Records, and OGC Building Blocks STAC registers.
- `_sources/oim-variable-observation/` — SeaDOTs OIM Variable Observation profile.
