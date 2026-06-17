# Implementation Roadmap

Derived from [`requirements.md`](requirements.md), assessed against the current
build (June 2026). Phased so each chunk is independently reviewable.

## Locked decisions

- **Authentication:** GitHub **App installation**. Commits authored via the app
  installation token; user identity via OAuth; Publish/Commit gated on the
  user's editor/push permission to the configured repo.
- **VocPrez conventions:** **Auto-maintain + validate** — the app adds inverse
  / bidirectional triples, mirrors `prefLabel`⇄`rdfs:label`, derives
  top-concept status and Dataset membership on save, *and* runs a
  convention/SHACL validator that warns (or blocks) before Publish/Commit.
- **Execution order:** Phase 1 first, then check in before continuing.

## Phases

### Phase 1 — RDF model & serialisation correctness ← in progress
- Inline **blank nodes** (e.g. `prop-rel:hasWeight [ qudt:numericValue 0.5 ]`)
  in the data layer so they round-trip and never surface as bnode IDs.
- Rewrite the Turtle serialiser to the **serialisation convention**:
  ConceptSchemes + Dataset first, then Concepts grouped by prefix
  (alphanumeric); per-subject predicate ordering (type → label → definition →
  internal taxonomy rels → external rels → SKOS hierarchy); `;`/`,` aggregation.

### Phase 2 — Browse + Concept editor
- Make **ConceptScheme** a first-class browsable/editable type; type filter
  concept/conceptScheme.
- **Collapse redundant fields** (single label field mirroring
  `prefLabel`/`rdfs:label`); friendly **blank-node editing** (e.g. weight shown
  as a number); type-filter **broader/narrower** to same-DB concepts;
  predicate picker driven by DB predicates + configured prefixes.
- Rename + relocate save actions to **Download All / Publish / Commit** on edit
  pages; gate by feature flags + role.

### Phase 3 — Concept Scheme tabular editor (`/conceptScheme/:iri`)
- Spreadsheet grid: id, label, description, scheme, non-SKOS types,
  broader/narrower; inline-editable cells (free text or DB-filtered dropdowns);
  edits flow into the shared pending-diff store.

### Phase 4 — VocPrez convention enforcement + validators
- Auto-maintain inverse/bidirectional triples, label mirroring, top-concept &
  Dataset membership on save.
- Config-driven validator layer (convention checks + optional SHACL via
  `rules.shacl`) surfacing warnings before Publish/Commit.

### Phase 5 — Auth (GitHub App) + RBAC
- GitHub App + OAuth login; verify editor/push permission on the configured
  repo; expose role to the SPA. Anonymous = edit + export only; editor =
  Publish/Commit enabled.

### Phase 6 — Config & browser persistence
- Unified config object (endpoints, secret refs, validators, feature flags,
  auth) via `/config.js` + Helm values.
- Persist the pending-edit draft to **localStorage** across reloads.

### Deferred
- Multiple schemes/DBs with imported prefixes (`requirements.md` marks this
  `[TODO]`).
