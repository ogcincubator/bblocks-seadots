# Context validation report — `floating-wind-infrastructure`

Date: 2026-05-19 · `context.jsonld` covers every property used in `schema.yaml` and `examples/utsira_nord_60x15mw.json`.

## Resolved to authoritative vocabularies

| Term | Resolved to |
|---|---|
| `title`, `name`, `description`, `created`, `updated`, `language`, `license`, `format` | DC Terms |
| `keywords`, `themes`, `formats`, `source`, `url` | DCAT |
| `concepts`, `scheme`, `label`, `vocabularyTerm`, `note` | SKOS |
| `submerged_area_total_m2` (aggregate) | `indo:submerged-infrastructure-area` (SeaDOTs indicator namespace; real concept, no NERC URI yet) |
| `unit_id` | DC Terms `identifier` |
| `lat`, `lon` | GeoJSON vocab |
| `units` | QUDT |
| `provenance`, `primarySource` | PROV-O / DC Terms |

## Missing authoritative URIs (local `seadots:` namespace)

| Term | Status | Action |
|---|---|---|
| `floatingWindInfrastructure` | local-permanent | Container term |
| `role` | needs-vocabulary | See `area-of-interest` |
| `unitDesign`, `nUnits` | local-permanent | Domain-specific; no external candidate |
| `perUnit`, `aggregate`, `sampleUnits` | local-permanent | Container terms |
| `hull_area_m2`, `mooring_area_m2`, `anchor_area_m2`, `submerged_area_m2` | needs-vocabulary | File a NERC P01 request for floating-wind wetted-surface area concepts; current local terms are unique to this bblock |
| `submerged_area_total_km2` | needs-vocabulary | Same concept as `submerged_area_total_m2` (`indo:submerged-infrastructure-area`) in different units — currently distinct local term; consider QUDT unit-conversion approach |
| `depthRange_m` | needs-vocabulary | NERC P01 depth-range concept; CF `depth` |
| `provenanceValues`, `nearestAuthoritativeSource` | local-permanent | Shared family pattern |
