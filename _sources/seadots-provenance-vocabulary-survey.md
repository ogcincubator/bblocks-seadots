# Survey: can `seadots-provenance` reuse terms from the 6 imported registers?

Date: 2026-05-20.

Registers surveyed:
1. `ogcapi-sosa` — https://opengeospatial.github.io/ogcapi-sosa/
2. `geodcat-ogcapi-records` — https://ogcincubator.github.io/geodcat-ogcapi-records/
3. `cross-domain-model` — https://ogcincubator.github.io/cross-domain-model/
4. `bblocks-sta` — https://ogcincubator.github.io/bblocks-sta/
5. `bblocks-stac` — https://ogcincubator.github.io/bblocks-stac/
6. `bblocks-openscience` — https://ogcincubator.github.io/bblocks-openscience/
7. `iliad-apis-features` (local) — https://ogcincubator.github.io/iliad-apis-features/

## Provenance-relevant bblocks discovered

| Register | Bblock | What it offers |
|---|---|---|
| cross-domain-model | `ogc.model.cross-domain.prov` | Model wrapper around the full **W3C PROV-O** ontology (`https://www.w3.org/ns/prov-o`). No seadots-specific extension; gives `prov:Entity`, `prov:Activity`, `prov:Agent` + properties (`wasDerivedFrom`, `hadPrimarySource`, `wasAttributedTo`, `wasInformedBy`, `wasInfluencedBy`, `hadPlan`, `generatedAtTime`, `invalidatedAtTime`, `specializationOf`, …). |
| geodcat-ogcapi-records | `geodcat-records-prov` | Composition: `geodcat-records` ∪ `bblocks://ogc.ogc-utils.prov#/$defs/Entity`. Adds PROV-O Entity properties to a Records feature. No new domain terms. |
| bblocks-stac | `item-prov` | Composition: PROV-O Entity + STAC item + the standalone **STAC PROV extension** (`https://stac-extensions.github.io/prov/v1.0.0/schema.json`). The STAC PROV extension itself adds: `processing:software`, `processing:datetime`, `processing:version`, `processing:lineage`, `processing:level`, `processing:facility`, `processing:expression`. |
| bblocks-openscience | `application-package` | CWL v1.2 wrapper; carries software citation via CWL `s:softwareVersion` etc. Provenance is implicit in CWLProv. |
| ogcapi-sosa | `properties/observation`, `features/observation` | `sosa:resultTime`, `phenomenonTime`, `hasFeatureOfInterest`, `observedProperty`, `madeBySensor`, `usedProcedure`. Provenance is process-step-shaped (a sensor/procedure produced a result), not record-audit-shaped. |
| bblocks-sta | `Observation`, `Datastream`, `Thing`, `Sensor`, `FeatureOfInterest` | Same shape as SOSA (SensorThings is built on it). Same provenance scope: who-sensed-what-when. |
| iliad-apis-features | `oim-obs`, `oim-variables`, `oim`, `macroobservation`, `property-relationship`, `indicator-quality-requirement`, `ses-impact-assessment` | OIM-aligned profiles of SOSA. `macroobservation` carries `dcterms:provenance`, `dcterms:source`, `provenance_urls`. `ses-impact-assessment` uses `prov:wasDerivedFrom` for `sourceInventory`. None define audit-state enums or "nearest authoritative source" patterns. |

## Term-by-term map for `seadots-provenance` candidates

| seadots term | Closest match in surveyed registers | Match quality | Recommendation |
|---|---|---:|---|
| `provenance` (container) | `prov:wasDerivedFrom` / `prov:Entity` | **full** | Keep mapping to `prov:wasDerivedFrom`. |
| `derivedFrom[]` (output → input URIs) | `prov:wasDerivedFrom` | **full** | Resolved. |
| `equationRecord` (URI of equation) | `prov:hadPlan` | **full** | Resolved. |
| `computedOn` (date) | `prov:generatedAtTime` or STAC `processing:datetime` | **full** | Adopt `prov:generatedAtTime`. |
| `computeCode` (URI of script) | STAC `processing:software` (kv); codemeta `SoftwareSourceCode`; `prov:wasGeneratedBy` qualified | **partial** | Adopt STAC `processing:software` shape if STAC item-prov is added as a dependency; otherwise stay local. |
| `primarySource` (DOI/URL/citation block) | `prov:hadPrimarySource` | **full** for the URI; **partial** for the bundled `{doi, url, citation, supportingFigure}` block | Map the URL to `prov:hadPrimarySource`; keep DCAT/DC Terms for inner fields (`dcterms:bibliographicCitation`, `bibo:doi`). No single term covers the whole block. |
| `values` enum (`retrieved` / `illustrative` / `mixed` / `computed`) | — | **no match** | No register defines this audit-state enum. Stays seadots-local. Possible alignment to **DQV** (`http://www.w3.org/ns/dqv#`), which is W3C but not in any of the six imported registers. |
| `valueKind`, `sigmaKind` (per-input audit state) | — | **no match** | Same as `values`. Per-cell rather than per-record granularity. Stays seadots-local. |
| `nearestAuthoritativeSource` (URL pointing at the closest real source when values are illustrative) | `prov:specializationOf` (loose) or `prov:wasInfluencedBy` (looser) | **partial** | Best fit is `prov:wasInfluencedBy` *typed* with a seadots role qualifier — but the "nearest" pattern itself is novel. Keep local. |
| `retrievalApiCall` (exact API call URL that would retrieve the real data) | Composition of `prov:Activity` (with `prov:used` / `prov:wasInformedBy`) + `dcat:accessURL` | **partial** | Constructable from PROV-O + DCAT, but no single term. Stays local as syntactic sugar. |
| `verificationGap` (free text describing what was verified vs what's outstanding) | DQV `dqv:QualityAnnotation` / `dqv:QualityMeasurement`; STAC `processing:lineage` (loose) | **partial** | None match exactly. DQV is the conceptual analogue but not in the imported registers. STAC `processing:lineage` is free-text but oriented at processing history, not "what was checked". Keep local. |
| `verifiedOn` (date) | `dcterms:date` | **full** | Already resolved to `dcterms:date`. |
| `supportingFigure` (figure citation under primarySource) | `bibo:numPages`-style — not in scope of any imported register | **no match** | Stays local; consider linking to BIBO term if BIBO is added later. |
| `role` (generic role on every input record) | DCAT-Prov `Role`; PROV `Role`; STAC `roles` (asset-only) | **partial** | DCAT-Prov is the right home but not exposed as a dedicated bblock here. Stays local but flagged. |
| `equationBinding` (equation symbol the input parameterises) | — | **no match** | This is a SeaDOTs-specific bridge between an `experiment-input` and an `equation-property-relationship` symbol. Stays local-permanent. |

## Verdict

PROV-O (via `cross-domain-model/prov`) and the STAC PROV extension (via `bblocks-stac/item-prov`) cover the **generic, process-shaped provenance bookkeeping**: which entity was derived from which, when it was generated, what software produced it, what was the primary source. Six terms can be resolved against these registers:

- `provenance` → `prov:wasDerivedFrom`
- `derivedFrom` → `prov:wasDerivedFrom`
- `equationRecord` → `prov:hadPlan`
- `computedOn` → `prov:generatedAtTime`
- `primarySource.url` → `prov:hadPrimarySource`
- `verifiedOn` → `dcterms:date`

The **distinctive seadots-provenance pattern** does NOT have equivalents in any of the six registers:

- `values` / `valueKind` / `sigmaKind` enums (record/cell **audit state**: was the value retrieved, computed, or invented?)
- `nearestAuthoritativeSource` (the "closest real source" pointer when values are illustrative)
- `verificationGap` (what was verified vs what wasn't)
- `retrievalApiCall` (the precise API call a consumer would invoke to obtain real data)

These four are **the audit pattern unique to this work** — they exist precisely because most input values in the current demonstrator are illustrative. The closest community vocabulary is W3C's **Data Quality Vocabulary** (DQV, `http://www.w3.org/ns/dqv#`) — but DQV is not in any of the six imported registers, so adopting it would mean either (a) adding DQV as a new dependency or (b) keeping the seadots-local namespace.

## Recommendation

Make `seadots-provenance` a **small shared bblock** that:

1. Depends on `ogc.model.cross-domain.prov` (PROV-O), so the six already-resolvable terms map straight through.
2. Adds the four audit-state terms locally (`values`, `valueKind`, `sigmaKind`, `nearestAuthoritativeSource`, `verificationGap`, `retrievalApiCall`) under `https://w3id.org/ogc/hosted/seadots/provenance#`.
3. Imports the SOSA `phenomenonTime`/`resultTime`/`observedProperty` vocab when used (so observation-shaped records can carry them without redefining).
4. Optionally aligns to DQV by adding a parallel `@id` per audit-state term (would need DQV added to imports).

The total cost is small: 6 terms with PROV-O mappings + 6 terms staying local. Promoting it to its own bblock eliminates the duplication currently present across all eight bblocks in the experiment chain.
