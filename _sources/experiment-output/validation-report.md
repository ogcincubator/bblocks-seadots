# Validation report — `experiment-output`

Date: 2026-05-19 · Scope: schema, context.jsonld, three example records under `examples/`.

## 1. OGC Feature compliance

| Record | type=Feature | geometry | properties | id | Status |
|---|:-:|:-:|:-:|:-:|:-:|
| `reef_biomass_result.json` | ✓ | Polygon | ✓ | ✓ | **PASS** |
| `stac_catalog.json` | ✓ | `null` | ✓ | ✓ | **PASS** |
| `prov_record.json` | ✓ | `null` | ✓ | ✓ | **PASS** |

## 2. OIM-OBS / SOSA compliance

`reef_biomass_result.json` is the only record in this bblock that represents a measurement/calculation outcome. It now declares conformance to `http://www.w3.org/ns/sosa/Observation` and `https://w3id.org/ogc/hosted/iliad/oim-obs`, and carries the SOSA-aligned fields under `properties.experimentOutput`:

| SOSA term | Value in `reef_biomass_result.json` |
|---|---|
| `sosa:observedProperty` | `indo:floating-wind-reef-biomass` |
| `sosa:hasSimpleResult` | `741237` |
| `qudt:unit` (`hasSimpleResultUnit`) | `kg` |
| `sosa:resultTime` | `2028-05-13T00:00:00Z` |
| `sosa:phenomenonTime` | `{ start: 2026-05-13, end: 2028-05-13 }` |
| `sosa:hasFeatureOfInterest` | URI of `aoi_utsira_surroundings` input record |

These are siblings of the `experimentOutput.data` block (where the structured result lives) and do not replace it. A consumer that only reads SOSA fields gets the headline scalar and the feature/time; a consumer that reads the full `data` block additionally gets the per-taxon decomposition, time series, and uncertainty attribution.

`stac_catalog.json` and `prov_record.json` are **catalog** and **provenance** records and are NOT observations — they intentionally carry no SOSA fields.

### Gap vs OIM-OBS

OIM-OBS extends SOSA with a multilingual `label` and a controlled-vocabulary `observedProperty`. Status:
- `observedProperty` ✓ URI-shaped (resolves under `id3.seadots.eu/indicator/`)
- `label` ✗ not yet provided in multilingual form (English `title` is present, which is single-language)

This is a **known gap**: action item below.

## 3. Schema-vs-example diff

For all three records: `experimentOutput` (required) is present with `name`, `role`, `format` (all required) ✓. `data.provenance` (required when `data` is present) ✓.

No schema violations detected.

## 4. Context coverage

Every key appearing in any of the three example records now has a `@context` term mapping. Including the SOSA-aligned additions, the diff resolved 0 missing terms.

## 5. Terms with authoritative URIs (resolved)

| Term | Resolved to |
|---|---|
| `title`, `description`, `created`, `updated`, `language`, `license`, `format`, `methodology` | DC Terms |
| `keywords`, `themes`, `concepts`, `formats`, `conformsTo` | DCAT / SKOS |
| `observedProperty`, `hasSimpleResult`, `resultTime`, `phenomenonTime`, `hasFeatureOfInterest` | SOSA |
| `start`, `end` | OWL-Time (`hasBeginning` / `hasEnd`) |
| `scientificName`, `aphiaID` | Darwin Core |
| `units`, `hasSimpleResultUnit`, `value`, `valueUnits` | QUDT |
| `sigma_kg`, `sigma_tonnes`, `totalSigma_kg`, `totalSigma_tonnes`, `sigma` | `qudt:standardUncertainty` |
| `CV`, `totalCV` | `qudt:coefficientOfVariation` |
| `B_reef_kg`, `B_reef_tonnes`, `B_kg` | `indo:floating-wind-reef-biomass` |
| `A_sub_m2` | `indo:submerged-infrastructure-area` |
| `D_pre_kg_m2` | `indo:benthic-biomass-density` |
| `AF_i` | `indo:reef-aggregation-index` |
| `C_t` | `indo:colonisation-time-factor` |
| `derivedFrom`, `provenance` | PROV-O |
| `equationRecord` | `prov:hadPlan` |
| `computedOn` | `dcterms:date` |
| `vocabularyTerm` | `skos:exactMatch` |
| `caveats`, `note`, `timeSeriesNote`, `computeCodeNote`, `methodDetail` | `skos:note` / `skos:definition` |

## 6. Terms still needing authoritative vocabulary URIs

### High priority — result structure

| Term | Current @id | Suggested search | Status |
|---|---|---|---|
| `headline` | `seadots:headline` | local container — no obvious external | local-permanent |
| `ci95_kg`, `ci95_tonnes` | `seadots:ci95_*` | QUDT `confidenceInterval`? not standard | needs-vocabulary |
| `asOf_months` | `seadots:asOf_months` | sosa:resultTime variant; OWL-Time months | needs-discussion |
| `perTaxonAtT24` | `seadots:perTaxonAtT24` | local container; the @t-suffix is example-specific | local-permanent |
| `shareOfTotal` | `seadots:shareOfTotal` | local | local-permanent |
| `aggregation` | `seadots:aggregation` | dcat-prov, prop-rel:Aggregation | needs-vocabulary |

### High priority — uncertainty propagation

| Term | Current @id | Suggested search | Status |
|---|---|---|---|
| `uncertainty`, `uncertaintyMethod` | `seadots:uncertainty`, `seadots:uncertaintyMethod` | uncertml ontology, JCGM/BIPM GUM vocab | needs-vocabulary |
| `methodDetail` | `skos:definition` | resolved | ✓ |
| `inputs[]` (under uncertainty) | `seadots:uncertaintyInput` | could be `prov:used` if each input is a prov:Entity | needs-discussion |
| `variable`, `value`, `sigma`, `valueUnits` | qudt:value, qudt:standardUncertainty, qudt:unit | resolved | ✓ |
| `valueSource`, `sigmaSource` | `dcterms:source` | resolved | ✓ |
| `valueKind`, `sigmaKind` | `seadots:valueKind`, `seadots:sigmaKind` | local enum (`assumed`/`illustrative-proxy`/`computed`); no external | local-permanent |
| `perTaxonVariance`, `D_times_AF`, `var_D_times_AF`, `shareWithinS` | `seadots:*` | local — internals of the propagation step | local-permanent |
| `S_value_kg_m2`, `S_sigma_kg_m2`, `S_CV` | `seadots:S_*` | local intermediate quantity | local-permanent |
| `varianceAttribution`, `CV_squared`, `dominantUncertainty` | `seadots:*` | local | local-permanent |
| `term` | `skos:notation` | resolved | ✓ |

### Computed-output provenance

| Term | Current @id | Suggested search | Status |
|---|---|---|---|
| `values` (`computed`/`retrieved`/`illustrative`/`mixed`) | `seadots:provenanceValues` | local enum; shared with `experiment-input` | local-permanent |
| `computeCode` | `seadots:computeCode` | codemeta, schema:SoftwareSourceCode | needs-vocabulary |
| `computeCodeNote` | `skos:note` | resolved | ✓ |

## 7. Action items

- [ ] Add multilingual `label` to `reef_biomass_result.json → properties.experimentOutput` to close the OIM-OBS gap. Shape: `"label": { "en": "Reef-associated biomass", "no": "Revassosiert biomasse" }`.
- [ ] File a JCGM/BIPM-aligned uncertainty vocabulary search; uncertml is the closest community attempt — evaluate.
- [ ] Decide whether `ci95_*` should be replaced with a per-bound pair `{lower, upper, confidenceLevel}` aligned with uncertml or QUDT.
- [ ] The local enums `values`, `valueKind`, `sigmaKind` SHOULD be promoted to a shared `seadots-provenance` bblock so they are not redefined per record type.
- [ ] `headline` is a local convenience term; consider whether the JSON-LD context could lift the scalar to `sosa:hasSimpleResult` directly and drop the `headline` container.


[TODO]
for examples in the /Users/piotr/repos/seadots/bblocks-seadots/_sources/experiment-input separate them into different building blocks, each schema shall be updated to cover all the properties, each
  context shall cover all the properties in the schema and examples, examples should depend on the best matching block from /Users/piotr/repos/Iliad/iliad-apis-features
[TODO] update /Users/piotr/repos/seadots/bblocks-seadots/_sources/experiment/scripts/utsira_reef_biomass.py with references from the divided example inputs
[TODO] update schemas of the inputs so they cover all the properties and the ones used in the script above shall be required
[TODO] update the context so it cover all the properties in the example input, output and experiment. create context-validation-report.md for each of the blocks with missing context vocabulary definitions