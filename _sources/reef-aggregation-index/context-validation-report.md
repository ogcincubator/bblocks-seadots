# Context validation report — `reef-aggregation-index`

Date: 2026-05-19 · `context.jsonld` covers every property used in `schema.yaml` and `examples/degraer2020_bindings.json`.

## Resolved to authoritative vocabularies

| Term | Resolved to |
|---|---|
| `title`, `name`, `description`, `created`, `updated`, `language`, `license`, `format`, `citation`, `validityScope` (`coverage`) | DC Terms |
| `keywords`, `themes`, `formats`, `source`, `url` | DCAT |
| `concepts`, `scheme`, `label`, `vocabularyTerm`, `note` | SKOS |
| `scientificName`, `aphiaID` | Darwin Core |
| `AF_i` | `indo:reef-aggregation-index` (SeaDOTs indicator namespace) |
| `units` | QUDT |
| `evidence` | PROV-O `wasInfluencedBy` |
| `provenance`, `primarySource` | PROV-O / DC Terms |

## Missing authoritative URIs (local `seadots:` namespace)

| Term | Status | Action |
|---|---|---|
| `reefAggregationIndex` | local-permanent | Container term |
| `role` | needs-vocabulary | DCAT-Prov |
| `doi` | needs-vocabulary | `bibo:doi`; or DC Terms `identifier` with `@type` DOI |
| `supportingFigure` | needs-vocabulary | `bibo` figure-reference term, or `schema:citation` |
| `provenanceValues`, `nearestAuthoritativeSource`, `verificationGap` | local-permanent / mixed | Shared family pattern |

## Outstanding

- The `indo:reef-aggregation-index` concept is unique to the SeaDOTs indicator namespace. There is no community vocabulary for a per-m² reef-effect aggregation coefficient — flagged for a future literature/registry survey.
- AF_i numeric values are illustrative (Degraer 2020 reports only a turbine-footprint figure for Mytilus). When real values become available, attach evidence URIs per-row via the existing `evidence` term.
