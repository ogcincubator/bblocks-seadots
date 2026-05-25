# Context validation report — `reef-effect-output`

Date: 2026-05-20 · `context.jsonld` covers every property used in `schema.yaml` and in all three example records under `examples/` (0 missing terms).

## Resolved to authoritative vocabularies

| Term | Resolved to |
|---|---|
| `title`, `name`, `description`, `created`, `updated`, `language`, `license`, `format`, `conformsTo`, `methodology` (`method`) | DC Terms |
| `keywords`, `themes`, `formats` | DCAT |
| `concepts`, `scheme`, `label`, `vocabularyTerm` | SKOS |
| `observedProperty`, `hasSimpleResult`, `resultTime`, `phenomenonTime`, `hasFeatureOfInterest` | SOSA |
| `start`, `end` | OWL-Time `hasBeginning` / `hasEnd` |
| `scientificName`, `aphiaID` | Darwin Core |
| `units`, `hasSimpleResultUnit`, `value`, `valueUnits` | QUDT |
| `sigma_kg`, `sigma_tonnes`, `totalSigma_kg`, `totalSigma_tonnes`, `sigma` | `qudt:standardUncertainty` |
| `CV`, `totalCV` | `qudt:coefficientOfVariation` |
| `B_reef_kg`, `B_reef_tonnes`, `B_kg` | `indo:floating-wind-reef-biomass` |
| `A_sub_m2` | `indp:submerged-infrastructure-area` |
| `D_pre_kg_m2` | `indo:benthic-biomass-density` |
| `AF_i` | `indp:reef-aggregation-index` |
| `C_t` | `indp:colonisation-time-factor` |
| `derivedFrom`, `provenance` | PROV-O |
| `equationRecord` | `prov:hadPlan` |
| `computedOn` | DC Terms `date` |
| `caveats`, `note`, `timeSeriesNote`, `computeCodeNote`, `methodDetail` | SKOS `note` / `definition` |
| `term` (variance attribution rows) | `skos:notation` |
| `reef-effect` | `seadots:experiment` (URI to experiment record) |

## Missing authoritative URIs (mapped under local `seadots:` namespace)

### Result structure

| Term | Current @id | Suggested vocabulary | Status |
|---|---|---|---|
| `experimentOutput` | `seadots:output` | Container term | local-permanent |
| `role` | `seadots:role` | DCAT-Prov `Role`; PROV `Role` | needs-vocabulary |
| `headline` | `seadots:headline` | Local convenience container; the scalar inside is reachable via `sosa:hasSimpleResult` | local-permanent |
| `ci95_kg`, `ci95_tonnes` | `seadots:ci95_*` | uncertml `ConfidenceInterval`; not a single QUDT term | needs-vocabulary |
| `asOf_months` | `seadots:asOf_months` | sosa:resultTime variant; OWL-Time months | needs-discussion |
| `scenarioInterval` | `dcterms:temporal` | resolved | ✓ |
| `perTaxonAtT24` | `seadots:perTaxonAtT24` | Local container; the `@t24` suffix is example-specific | local-permanent |
| `shareOfTotal` | `seadots:shareOfTotal` | Local | local-permanent |
| `aggregation` | `seadots:aggregation` | DCAT-Prov; `prop-rel:Aggregation` | needs-vocabulary |
| `equation` | `seadots:equation` | `qudt:hasFormula` (close fit) | needs-vocabulary |

### Uncertainty propagation

| Term | Current @id | Suggested vocabulary | Status |
|---|---|---|---|
| `uncertainty`, `uncertaintyMethod` | `seadots:uncertainty`, `seadots:uncertaintyMethod` | uncertml ontology; JCGM/BIPM GUM vocab | needs-vocabulary |
| `inputs` (under uncertainty) | `seadots:uncertaintyInput` | Could lift to `prov:used` if each row is a `prov:Entity` | needs-discussion |
| `variable`, `value`, `sigma`, `valueUnits` | qudt:value / standardUncertainty / unit | resolved | ✓ |
| `valueSource`, `sigmaSource` | `dcterms:source` | resolved | ✓ |
| `valueKind`, `sigmaKind` | `seadots:valueKind`, `seadots:sigmaKind` | Local enum (`assumed` / `illustrative-proxy` / `computed`) | local-permanent |
| `perTaxonVariance`, `D_times_AF`, `var_D_times_AF`, `shareWithinS` | `seadots:*` | Internals of the propagation step; no external | local-permanent |
| `S_value_kg_m2`, `S_sigma_kg_m2`, `S_CV` | `seadots:S_*` | Intermediate quantity; no external | local-permanent |
| `varianceAttribution`, `CV_squared`, `dominantUncertainty` | `seadots:*` | Local | local-permanent |

### Provenance sub-block

| Term | Current @id | Suggested vocabulary | Status |
|---|---|---|---|
| `values` (`computed` / `retrieved` / `illustrative` / `mixed`) | `seadots:provenanceValues` | Shared with all input bblocks; promote to a `seadots-provenance` bblock | local-permanent |
| `computeCode` | `seadots:computeCode` | codemeta `SoftwareSourceCode`; `prov:wasGeneratedBy` plan | needs-vocabulary |
| `computeCodeNote` | `skos:note` | resolved | ✓ |

## Outstanding actions

- [ ] Add multilingual `label` to `reef_biomass_result.json → properties.experimentOutput` to close the OIM-OBS multilingual-label gap.
- [ ] Evaluate **uncertml** as the canonical container for `uncertainty`, `uncertaintyMethod`, `CV_squared`, `dominantUncertainty` — and possibly `ci95_*` (replace with `{lower, upper, confidenceLevel}`).
- [ ] Promote the shared local enums `provenanceValues`, `valueKind`, `sigmaKind` to a `seadots-provenance` bblock so they are defined once across all record types.
- [ ] Decide whether the JSON-LD context could lift `headline` directly into `sosa:hasSimpleResult` and drop the `headline` container.
