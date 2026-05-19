# Validation report — `experiment`

Date: 2026-05-19 · Scope: schema, context.jsonld, every record under `examples/`.

## 1. OGC Feature compliance

| Record | type=Feature | geometry present | properties present | id present | Status |
|---|:-:|:-:|:-:|:-:|:-:|
| `examples/utsira_surroundings_experiment.json` | ✓ | ✓ (Polygon) | ✓ | ✓ | **PASS** |

The record is a valid OGC GeoJSON Feature. `time.interval` is a JSON-FG-style temporal extent (acceptable as an extension; not validated against JSON-FG schema yet).

## 2. OIM-OBS / SOSA compliance

**Not applicable.** This record describes a *process* (a computational experiment), not an *observation* of a phenomenon. SOSA terms (`observedProperty`, `hasSimpleResult`, etc.) are emitted by the `experiment-output` result record, not here. The experiment record links to that output via `properties.experiment.outputs[]`.

## 3. Schema-vs-example diff

- `experiment` (required) ✓ present
- `experiment.kind` ✓ value `"computational"` is in the enum
- `experiment.application` (required) ✓ present, points to `../scripts/utsira_reef_biomass.py`
- `experiment.inputs[]` ✓ 6 entries, each an `InputBinding` with `href`, `equationBinding`
- `experiment.outputs[]` ✓ 3 entries, each a `Link`
- `experiment.execution` ✓ uses the new (post-CWL-removal) `language` / `entrypoint` shape

No schema violations detected.

## 4. Context coverage

Every key appearing in the example record now has a `@context` term mapping. The diff against the example resolved 0 missing terms.

## 5. Terms still needing authoritative vocabulary URIs

The following terms are currently mapped to the local `https://w3id.org/ogc/hosted/seadots/experiment#` namespace (via the `seadots:` prefix or `@vocab` default) and SHOULD be replaced with authoritative URIs when a community vocabulary is identified:

| Term | Current @id | Suggested vocabulary search | Status |
|---|---|---|---|
| `kind` | `seadots:kind` | schema.org `additionalType`, dcat:theme | needs-vocabulary |
| `application` | `seadots:application` | schema.org `SoftwareApplication`, codemeta | needs-vocabulary |
| `modelledBy` | `seadots:modelledBy` | prov:wasInformedBy, sosa:isResultOf | needs-discussion |
| `evidenceEquation` | `seadots:evidenceEquation` | prov:hadPlan, qudt:hasFormula | needs-vocabulary |
| `parameters` / `parameterSchema` | `seadots:parameter` | codemeta:applicationCategory, CWL inputs | needs-vocabulary |
| `equationBinding` | `seadots:equationBinding` | local — no obvious external term | local-permanent |
| `execution` | `seadots:execution` | codemeta:runtimePlatform | needs-vocabulary |
| `languageVersion` | `seadots:languageVersion` | codemeta:runtimePlatform | needs-vocabulary |
| `dependencies` | `seadots:dependency` | codemeta:softwareRequirements | needs-vocabulary |
| `entrypoint` | `seadots:entrypoint` | codemeta:applicationCategory, schema:potentialAction | needs-vocabulary |
| `scheduling` | `seadots:scheduling` | local | local-permanent |
| `reproducibility` / `seedPolicy` | `seadots:reproducibility` / `seadots:seedPolicy` | prov-aq, ro-crate | needs-vocabulary |
| `successCriteria` | `seadots:successCriterion` | schema:Criterion (not exactly aligned) | needs-discussion |

**Resolved with authoritative URIs:** `purpose` → `dcterms:purpose`; `title`, `description`, `created`, `updated`, `language`, `license` → DC Terms; `themes`, `keywords`, `formats`, `conformsTo`, `contacts` → DCAT / DC Terms; `provenance` → `prov:wasGeneratedBy`; `vocabularyTerm` → `skos:exactMatch`.

## 6. Action items

- [ ] Reconcile `application` with the codemeta vocabulary (`https://codemeta.github.io/`) once an experiment runs on a non-Python target — the current single-link shape may need a Software object.
- [ ] Decide whether `kind` enum maps to a SKOS scheme rather than free-text + enum (would let other registers extend it).
- [ ] Confirm that `equationBinding` should remain local — alternative is to coin it under `eqrel:` once the equation-property-relationship bblock publishes a stable URI scheme.
