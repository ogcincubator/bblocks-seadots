# Context validation report — `colonisation-time-factor`

Date: 2026-05-19 · `context.jsonld` covers every property used in `schema.yaml` and `examples/default_sigmoid.json`.

## Resolved to authoritative vocabularies

| Term | Resolved to |
|---|---|
| `title`, `name`, `description`, `created`, `updated`, `language`, `license`, `format`, `citation` | DC Terms |
| `keywords`, `themes`, `formats`, `source`, `url` | DCAT |
| `concepts`, `scheme`, `label`, `vocabularyTerm`, `note` | SKOS |
| `C_t` | `indp:colonisation-time-factor` (SeaDOTs indicator namespace) |
| `units` | QUDT |
| `provenance`, `primarySource` | PROV-O / DC Terms |

## Missing authoritative URIs (local `seadots:` namespace)

| Term | Status | Action |
|---|---|---|
| `colonisationTimeFactor` | local-permanent | Container term |
| `role` | needs-vocabulary | DCAT-Prov |
| `curveType`, `formula` | needs-vocabulary | `qudt:hasFormula` for `formula`; `curveType` no external standard |
| `parameters`, `L`, `k`, `t0_months` | local-permanent | Sigmoid-specific; document as local |
| `lookup`, `t_months`, `saturationMonth` | local-permanent | Lookup-table internals |
| `doi`, `supportingFigure` | needs-vocabulary | See `reef-aggregation-index` report |
| `provenanceValues`, `nearestAuthoritativeSource`, `verificationGap` | local-permanent / mixed | Shared family pattern |

## Outstanding

- No published closed-form sigmoid parameterisation of reef colonisation per taxon exists. Sigmoid parameters in the example are illustrative. Real calibration requires fitting to a benthic-biofouling time series (WindFloat Atlantic, Belwind monitoring, etc.) — recorded under `nearestAuthoritativeSource`.
- `curveType` is currently an open string. Consider promoting to a SKOS scheme if multiple curve families (sigmoid, exponential, piecewise-linear) become common.
