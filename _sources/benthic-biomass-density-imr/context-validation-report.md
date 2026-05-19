# Context validation report — `benthic-biomass-density-imr`

Date: 2026-05-19 · `context.jsonld` covers every property used in `schema.yaml` and `examples/imr_ices_iva_fallback.json`.

## Resolved to authoritative vocabularies

| Term | Resolved to |
|---|---|
| `title`, `name`, `description`, `created`, `updated`, `language`, `license`, `format`, `conformsTo`, `method` (`methodology`) | DC Terms |
| `keywords`, `themes`, `formats`, `source`, `url` | DCAT |
| `concepts`, `scheme`, `label`, `vocabularyTerm`, `note` | SKOS |
| `observedProperty`, `phenomenonTime` | SOSA |
| `scientificName`, `aphiaID` | Darwin Core |
| `density_kg_m2` | `indo:benthic-biomass-density` |
| `aggregateDensity_kg_m2` | `indo:benthic-biomass-density-aggregate` |
| `uncertainty_kg_m2` | `qudt:standardUncertainty` |
| `units` | QUDT |
| `samplePeriod` | DC Terms `temporal` |
| `provenance`, `primarySource`, `verifiedOn` | PROV-O / DC Terms |

## Missing authoritative URIs (local `seadots:` namespace)

| Term | Status | Action |
|---|---|---|
| `benthicBiomassDensity` | local-permanent | Container term |
| `role` | needs-vocabulary | DCAT-Prov |
| `icesDivision` | needs-vocabulary | Replace string `"IVa"` with the ICES area URI (`http://vocab.ices.dk/services/icesAreas/IVa`) |
| `provenanceValues`, `nearestAuthoritativeSource`, `verificationGap` | local-permanent / mixed | Shared family pattern |

## Outstanding

- File the ICES vocabulary upgrade so `icesDivision` values resolve to URIs rather than strings.
- The `source` URL (`https://www.hi.no/api/benthic-biomass-baseline`) is a notional endpoint that does not exist — already flagged in `data.provenance.verificationGap`. Replace once a real IMR endpoint or NMD dataset is wired up.
