# Proposal: align bblock contexts to `oim-variables/examples/indicators.ttl`

## Executive summary

**What:** Migrate the indicator-concept URIs in our 7 affected JSON-LD contexts (and 6 `vocabularyTerm` strings in examples) from the `https://w3id.org/indicators/marine/` placeholder namespace to the canonical `https://w3id.org/indicators/marine/` namespace declared by `iliad-apis-features/_sources/oim-variables/examples/indicators.ttl`.

**Three substantive corrections, not just a prefix swap:**
1. **B_reef sits in `ind:`, not `indo:`** — the top-level composite indicator `floating-wind-reef-biomass` is in `https://w3id.org/indicators/marine/`, while every input concept (`submerged-infrastructure-area`, `baseline-benthic-biomass-density`, `reef-aggregation-index`, `colonisation-time-factor`) is in `https://w3id.org/indicators/marine/obs/`. We currently put all of them under `indo:`.
2. **`D_pre` canonical name is `baseline-benthic-biomass-density`** — we use `benthic-biomass-density`. The TTL distinguishes the abstract baseline from the `-mareano` / `-imr-baseline` source-specific narrower bindings.
3. **`-aggregate` does not exist in the TTL** — our `indo:benthic-biomass-density-aggregate` synthetic concept should fold back to the parent `indo:baseline-benthic-biomass-density`.

**Three additions worth adopting now:**
- Add `ind:`, `inda:`, `prop-rel:` prefix declarations to the `reef-effect` context.
- Use the SKOS narrower terms in source-specific bblocks (`indo:benthic-biomass-density-mareano` in the MAREANO bblock, `-imr-baseline` in IMR, `-utsira-design` in floating-wind aggregate).
- **Lift `equationBinding` to `prop-rel:toProperty`** — single most powerful change: per-input bindings become SKOS-traversable property relationships rather than private strings.

**Scope and risk if accepted:**

| Item | Count |
|---|---:|
| `context.jsonld` files to edit | 6 |
| `vocabularyTerm` strings in example records to migrate | 6 |
| Schema changes required | **0** |
| Python script changes required | **0** |
| Tests affected | none (contexts are pure JSON-LD term tables) |
| Re-validation needed afterwards | context-coverage diff (must remain 0 missing per bblock) |

**Recommendation:** apply in a single coordinated pass; re-verify with the existing coverage checker. The full per-term mapping table with TTL line references is below.

---

Source of truth: `/Users/piotr/repos/Iliad/iliad-apis-features/_sources/oim-variables/examples/indicators.ttl` (the now-parseable indicator + property-relationship vocabulary).

The TTL is the canonical place where concept URIs for the reef-biomass equation are *declared* (with `skos:prefLabel`, `skos:definition`, `qudt:hasQuantityKind`, and `skos:broader`/`narrower` hierarchies). The contexts in our bblocks should resolve to those URIs so that a triple-store consumer can navigate from a value (e.g. a `density_kg_m2` cell) back to the concept that defines it.

## Namespace prefix table

| Prefix | Current value in our contexts | Proposed value (matches the TTL) | Action |
|---|---|---|---|
| `indo:` | `https://w3id.org/indicators/marine/` | `https://w3id.org/indicators/marine/obs/` | **change** (used in 7 contexts) |
| `ind:` | — (not currently declared) | `https://w3id.org/indicators/marine/` | **add** to `reef-effect-output` (carries `indo:floating-wind-reef-biomass-effect`) |
| `inda:` | — | `https://w3id.org/indicators/marine/activity/` | **add** to `reef-effect` (for `inda:cdi-computation`-style activities, when used) |
| `indrel:` | — | `https://w3id.org/indicators/marine/relationship/` | optional — only needed if we surface property-relationship edges in examples |
| `prop-rel:` | — | `https://w3id.org/ogc/hosted/seadots/prop-rel/` | **add** to `reef-effect` (so `equationBinding` can later be expressed as `prop-rel:fromProperty`) |
| `sosa:` | already declared in some | `http://www.w3.org/ns/sosa/` | unchanged |
| `qudt:`, `quantitykind:` | already declared | unchanged | unchanged (the TTL uses `quantitykind:Area`, `Mass`, `Dimensionless`, `SurfaceDensity` — same URIs) |

## Term-by-term realignment

| Bblock | Term in example | Current `@id` | Proposed `@id` | Source line in TTL |
|---|---|---|---|---|
| **`reef-effect-output`** | `B_reef_kg`, `B_reef_tonnes`, `B_kg` | `indo:floating-wind-reef-biomass` | `indo:floating-wind-reef-biomass-effect` | TTL line 117 (this is the top-level `prov:Entity, sosa:observedProperty` — it's in the `ind:` namespace, **not** `indo:`) |
| `reef-effect-output` | `A_sub_m2` | `indp:submerged-infrastructure-area` | `indp:submerged-infrastructure-area` | TTL line 129 ✓ concept matches, prefix base changes |
| `reef-effect-output` | `D_pre_kg_m2` | `indo:benthic-biomass-density` | **`indo:baseline-benthic-biomass-density`** | TTL line 137 — the canonical term is "baseline-benthic-biomass-density", not "benthic-biomass-density" |
| `reef-effect-output` | `AF_i` | `indp:reef-aggregation-index` | `indp:reef-aggregation-index` | TTL line 146 ✓ |
| `reef-effect-output` | `C_t` | `indp:colonisation-time-factor` | `indp:colonisation-time-factor` | TTL line 156 ✓ |
| **`floating-wind-infrastructure`** | `submerged_area_total_m2` (aggregate) | `indp:submerged-infrastructure-area` | `indp:submerged-infrastructure-area-utsira-design` (when the example is Utsira-specific) | TTL line 164 — narrower for the Utsira engineering design |
| `floating-wind-infrastructure` | (other unit-level `*_area_m2`) | `seadots:*Area_m2` | (stay seadots-local — TTL doesn't yet define unit-level sub-concepts) | — |
| **`benthic-biomass-density-mareano`** | `density_kg_m2` | `indo:benthic-biomass-density` | **`indo:benthic-biomass-density-mareano`** | TTL line 173 — this is the MAREANO-specific narrower binding |
| `benthic-biomass-density-mareano` | `aggregateDensity_kg_m2` | `indo:benthic-biomass-density-aggregate` | `indo:baseline-benthic-biomass-density` (the parent concept) | TTL has no "aggregate" variant; map to parent |
| **`benthic-biomass-density-imr`** | `density_kg_m2` | `indo:benthic-biomass-density` | **`indo:benthic-biomass-density-imr-baseline`** | TTL line 182 |
| `benthic-biomass-density-imr` | `aggregateDensity_kg_m2` | `indo:benthic-biomass-density-aggregate` | `indo:baseline-benthic-biomass-density` | as above |
| **`reef-aggregation-index`** | `AF_i` (top of perTaxon array) | `indp:reef-aggregation-index` | `indp:reef-aggregation-index` | TTL line 146 ✓ (the per-taxon narrower terms — `-mytilus`/`-buccinum`/`-asterias` — are *instances*, attached at the row level if we ever bind a row's `scientificName` to a concept) |
| **`colonisation-time-factor`** | `C_t` | `indp:colonisation-time-factor` | `indp:colonisation-time-factor` | TTL line 156 ✓ (the example's "default sigmoid" parameters are an instance of the narrower `-default` term — could be referenced from `data.vocabularyTerm` rather than from the row) |

## Concept renames that affect the `vocabularyTerm` field in examples

Three example records currently set `vocabularyTerm` to a URL that does not resolve in the TTL — these should be updated alongside the context migration:

| File | Current `vocabularyTerm` | Proposed `vocabularyTerm` |
|---|---|---|
| `benthic-biomass-density-mareano/examples/mareano_norwegian_shelf.json` | `https://w3id.org/indicators/marine/benthic-biomass-density-mareano` | `https://w3id.org/indicators/marine/obs/benthic-biomass-density-mareano` |
| `benthic-biomass-density-imr/examples/imr_ices_iva_fallback.json` | `https://w3id.org/indicators/marine/benthic-biomass-density-imr-baseline` | `https://w3id.org/indicators/marine/obs/benthic-biomass-density-imr-baseline` |
| `reef-aggregation-index/examples/degraer2020_bindings.json` | `https://w3id.org/indicators/marine/reef-aggregation-index` | `https://w3id.org/indicators/marine/parameters/reef-aggregation-index` |
| `colonisation-time-factor/examples/default_sigmoid.json` | `https://w3id.org/indicators/marine/colonisation-time-factor-default` | `https://w3id.org/indicators/marine/parameters/colonisation-time-factor-default` |
| `floating-wind-infrastructure/examples/utsira_nord_60x15mw.json` | `https://w3id.org/indicators/marine/submerged-infrastructure-area-utsira-design` | `https://w3id.org/indicators/marine/parameters/submerged-infrastructure-area-utsira-design` |
| `experiment-output/examples/reef_biomass_result.json` (`observedProperty` + `vocabularyTerm`) | `https://w3id.org/indicators/marine/floating-wind-reef-biomass` | `https://w3id.org/indicators/marine/obs/floating-wind-reef-biomass-effect` (note: `ind:` namespace, no `obs/`) |

## What the TTL adds that we have not yet surfaced

- **`indo:fisheries-production`**, `indo:bird-tourism`, `indo:number-of-jobs`, `indo:number-of-turbines`, `indo:area-use-by-wind-park` — defined in the TTL but unused by the experiment chain. Available if a future Utsira economic-impact extension lands.
- **`prop-rel:PropertyRelationship`**, `prop-rel:fromProperty`, `prop-rel:toProperty`, `prop-rel:hasWeight` — defined in the TTL. Our current `equationBinding` field could be lifted to:
  ```jsonld
  "equationBinding": {
    "@id": "https://w3id.org/ogc/hosted/seadots/prop-rel/toProperty",
    "@type": "@id"
  }
  ```
  so that an input record with `equationBinding: "A_{sub}"` becomes a triple linking the experiment to a `PropertyRelationship` whose `toProperty` is the equation symbol's concept URI. This is the most powerful single change — it turns equation-binding from a private string into a real SKOS-traversable relationship.
- **`ind:CompositeIndicatorComputation`** + `inda:` activities — pattern for representing the computation itself as a PROV-O activity. Our `application` + `computeCode` fields could be expressed as `prov:wasGeneratedBy <inda:utsira-reef-biomass-computation>`.

## Sample minimal patch (illustrative, not yet applied)

```diff
--- _sources/reef-effect-output/context.jsonld
+++ _sources/reef-effect-output/context.jsonld
@@
-    "indo": "https://w3id.org/indicators/marine/",
+    "indo": "https://w3id.org/indicators/marine/obs/",
      "indp": "https://w3id.org/indicators/marine/parameters/",
+    "ind":  "https://w3id.org/indicators/marine/",
+    "prop-rel": "https://w3id.org/ogc/hosted/seadots/prop-rel/",
@@
-    "B_reef_kg":     { "@id": "indo:floating-wind-reef-biomass",  "@type": "qudt:QuantityValue" },
-    "B_reef_tonnes": { "@id": "indo:floating-wind-reef-biomass",  "@type": "qudt:QuantityValue" },
-    "B_kg":          { "@id": "indo:floating-wind-reef-biomass",  "@type": "qudt:QuantityValue" },
-    "D_pre_kg_m2":   { "@id": "indo:benthic-biomass-density",     "@type": "qudt:QuantityValue" },
+    "B_reef_kg":     { "@id": "indo:floating-wind-reef-biomass-effect",   "@type": "qudt:QuantityValue" },
+    "B_reef_tonnes": { "@id": "indo:floating-wind-reef-biomass-effect",   "@type": "qudt:QuantityValue" },
+    "B_kg":          { "@id": "indo:floating-wind-reef-biomass-effect",   "@type": "qudt:QuantityValue" },
+    "D_pre_kg_m2":   { "@id": "indo:baseline-benthic-biomass-density", "@type": "qudt:QuantityValue" },
```

## Summary of changes if the proposal is accepted

| Action | Count |
|---|---|
| `@context` files to edit | 6 (experiment-output + 5 input bblocks; experiment itself only needs the new `prop-rel:` / `inda:` namespaces, no term renames) |
| `vocabularyTerm` strings in example JSON to update | 6 |
| Concept-name corrections (canonical TTL spelling vs ours) | 2 (`baseline-benthic-biomass-density` + `floating-wind-reef-biomass` namespace move) |
| Aggregate-density mappings to drop or remap to parent | 2 (mareano, imr) |
| Tests / breakage | none — the contexts are pure JSON-LD term tables; the Python script doesn't read contexts; the schema files are unchanged; example records still validate against their schemas |

Say the word and I'll apply all six context updates + six `vocabularyTerm` edits as a single coordinated change, then re-verify context coverage = 0 missing on every bblock.
