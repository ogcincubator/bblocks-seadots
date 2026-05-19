# Context validation report — `benthic-biomass-density-mareano`

Date: 2026-05-19 · `context.jsonld` covers every property used in `schema.yaml` and `examples/mareano_norwegian_shelf.json`.

## Resolved to authoritative vocabularies

| Term | Resolved to |
|---|---|
| `title`, `name`, `description`, `created`, `updated`, `language`, `license`, `format`, `conformsTo` | DC Terms |
| `keywords`, `themes`, `formats`, `source`, `url` | DCAT |
| `concepts`, `scheme`, `label`, `vocabularyTerm`, `note` | SKOS |
| `observedProperty`, `phenomenonTime` | SOSA |
| `scientificName`, `aphiaID`, `habitat`, `nSamples` | Darwin Core |
| `density_kg_m2` | `indo:benthic-biomass-density` (SeaDOTs indicator namespace) |
| `aggregateDensity_kg_m2` | `indo:benthic-biomass-density-aggregate` |
| `units` | QUDT |
| `samplePeriod` | DC Terms `temporal` |
| `samplingProgramme` | PROV-O `wasAttributedTo` |
| `provenance`, `primarySource`, `verifiedOn` | PROV-O / DC Terms |

## Missing authoritative URIs (local `seadots:` namespace)

| Term | Status | Action |
|---|---|---|
| `benthicBiomassDensity` | local-permanent | Container term |
| `role` | needs-vocabulary | DCAT-Prov |
| `depthBand_m` | needs-vocabulary | NERC P01 depth-range; CF `depth` |
| `provenanceValues`, `nearestAuthoritativeSource`, `retrievalApiCall`, `verificationGap` | local-permanent / mixed | Shared family pattern |

## Outstanding

- The `indo:benthic-biomass-density` concept resolves only inside the SeaDOTs indicator namespace. File a NERC P01 vocabulary request so the concept gets a community URI.
- Replace `habitat` free-text strings (`rocky-subtidal`, `soft-sediment`, `mixed`) with EUNIS habitat-type URIs when available.
