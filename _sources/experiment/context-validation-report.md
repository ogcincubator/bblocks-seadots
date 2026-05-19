# Context validation report — `experiment`

Date: 2026-05-20 · `context.jsonld` covers every property used in `schema.yaml` and in `examples/utsira_surroundings_experiment.json` (0 missing terms).

## Resolved to authoritative vocabularies

| Term | Resolved to |
|---|---|
| `title`, `name`, `description`, `created`, `updated`, `language`, `license`, `format`, `purpose` | DC Terms |
| `keywords`, `themes`, `formats`, `conformsTo`, `contacts` | DCAT / DC Terms |
| `concepts`, `scheme`, `label`, `vocabularyTerm` | SKOS |
| `geometry`, `coordinates`, `Feature`, `Polygon`, `properties`, `bbox`, `rel` | GeoJSON vocab |
| `links`, `href` | IANA link relations / `@id` |
| `roles`, `organization` | DCAT / schema.org |
| `time`, `interval`, `resolution` | DC Terms `temporal` / DCAT `temporalResolution` |
| `provenance` | PROV-O `wasGeneratedBy` |

## Missing authoritative URIs (mapped under local `seadots:` namespace)

### High priority — application + execution

| Term | Current @id | Suggested vocabulary | Status |
|---|---|---|---|
| `experiment` | `seadots:experiment` | Container term | local-permanent |
| `kind` | `seadots:kind` | schema.org `additionalType`; promote to SKOS scheme | needs-vocabulary |
| `application` | `seadots:application` | codemeta `SoftwareSourceCode`; schema.org `SoftwareApplication` | needs-vocabulary |
| `modelledBy` | `seadots:modelledBy` | `prov:wasInformedBy`; `sosa:isResultOf` (close fit) | needs-discussion |
| `evidenceEquation` | `seadots:evidenceEquation` | `prov:hadPlan`; `qudt:hasFormula` | needs-vocabulary |
| `parameters` / `parameterSchema` | `seadots:parameter` | codemeta `softwareInput`; no exact JSON-Schema-fragment term | needs-vocabulary |
| `equationBinding` | `seadots:equationBinding` | No external candidate — bridge to `equation-property-relationship` symbol table | local-permanent |
| `execution` | `seadots:execution` | codemeta `runtimePlatform`; ro-crate workflow run pattern | needs-vocabulary |
| `language` | `dcterms:language` | resolved | ✓ |
| `languageVersion` | `seadots:languageVersion` | codemeta `runtimePlatform`; schema.org `softwareVersion` | needs-vocabulary |
| `dependencies` | `seadots:dependency` | codemeta `softwareRequirements` | needs-vocabulary |
| `entrypoint` | `seadots:entrypoint` | codemeta or schema.org `potentialAction` | needs-vocabulary |
| `scheduling` | `seadots:scheduling` | Local; no obvious external term | local-permanent |
| `reproducibility` / `seedPolicy` | `seadots:reproducibility` / `seedPolicy` | RO-Crate workflow-run profile | needs-vocabulary |
| `successCriteria` | `seadots:successCriterion` | schema.org `Criterion` (loose fit) | needs-discussion |
| `inputs`, `outputs` | `seadots:input`, `seadots:output` | Could lift to `prov:used` / `prov:wasGeneratedBy` | needs-discussion |

## Outstanding actions

- [ ] Align `application` + `execution` with the **codemeta** vocabulary (https://codemeta.github.io/) once the experiment runs against a non-Python target — current single-link shape will need a Software object then.
- [ ] Decide whether `kind` should be a SKOS scheme so other registers can extend it.
- [ ] `equationBinding` should remain local but document its mapping to the `equation-property-relationship` symbol table (currently informal — equation symbols appear as plain strings like `A_{sub}`).
