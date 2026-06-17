# Implementation Roadmap

Single source of truth for delivering the SeaDOTs Concept Editor against
[`requirements.md`](requirements.md). Reviewed 2026-06-18 against the current
build. Phased so each chunk is independently reviewable.

## Locked decisions

- **Authentication:** GitHub **App** installation. Commits authored via the app
  installation token; user identity via OAuth. **RBAC is derived from the
  user's GitHub privileges** on the configured repo — only users with editor
  (push) access may **Publish** (to the triplestore) or **Commit** (to git).
- **VocPrez conventions:** **Auto-maintain + validate** — the app adds inverse /
  bidirectional triples, mirrors `prefLabel`⇄`rdfs:label`, derives top-concept
  status and Dataset membership on save, *and* runs a convention/SHACL validator
  that warns (or blocks) before Publish/Commit.
- **Execution order:** phase by phase, check in after each.

## Cross-cutting principles (apply to every phase)

1. **Nothing hardcoded — everything injectable.** All endpoints, graphs, the
   GitHub App config, vocabularies, prefixes, feature flags and secrets are
   supplied via environment → `/config.js` → Helm values. Source literals exist
   only as *documented test defaults*, never as the sole source. *(requirements
   §Configuration: "do not hardcode any of them")*
2. **Browser-first / user-initiated persistence.** Edits live in the browser
   store; nothing reaches the triplestore or git except on explicit user action.
3. **No RDF expertise required.** Blank nodes hidden, CURIEs/labels shown,
   redundant fields collapsed, typeahead over real terms.
4. **Single lightweight container**, deployable by Helm.

## Default configuration (test)

| Setting | Test default | Injectable as |
|---------|-------------|---------------|
| SPARQL query endpoint | `https://project-seadots-definition-server.lab.dive.edito.eu/prez-b/sparql` | `SPARQL_QUERY` / `VITE_SPARQL_QUERY` |
| Graph | *empty* (default graph) | `SPARQL_GRAPH` / `VITE_GRAPH` |
| SPARQL update endpoint | *(unverified — Prez may be read-only)* | `SPARQL_UPDATE` |
| GitHub App (id, key, repo) | — | env / secret |
| Imported vocabularies | — | config list |

## Phases

### Phase 1 — RDF model & serialisation correctness ✅ DONE
- ✅ Blank-node inlining end-to-end (`hasWeight [ qudt:numericValue … ]` round-trips, never shows a bnode id).
- ✅ Human-readable Turtle serialiser per the **serialisation convention**
  (schemes/dataset first, concepts by prefix; per-subject ordering type → label
  → definition → taxonomy rels → external rels → SKOS hierarchy; `;`/`,`
  aggregation; `a` shorthand).
- ✅ Retargeted to the Prez backend: SPARQL endpoint discovery, **default-graph**
  support (conditional `GRAPH` wrapper), config defaults updated. Verified live:
  107 concepts / 3 schemes / 112 terms.

### Phase 2 — Browse + Concept editor
- Make **ConceptScheme** a first-class browsable/editable type; Browse type
  filter concept/conceptScheme (then by scheme/type for concepts).
- **Collapse redundant fields** — one label field mirroring
  `prefLabel`/`rdfs:label` (prefLabel primary); collapse other redundant pairs
  per the content convention.
- Friendly **blank-node editing** (e.g. weight shown/edited as a number,
  re-wrapped as a bnode on export).
- **Same-DB constraints:** broader/narrower restricted to in-DB concepts;
  inScheme restricted to in-DB ConceptSchemes.
- **Configurable object/predicate sources:** object typeahead = in-DB terms +
  **configurable imported vocabularies**; predicate picker = in-DB predicates +
  configured prefixes (reference content or config), not a fixed source literal.
- Rename + relocate save actions to **Download All / Publish / Commit** on each
  edit page; gate by feature flags + role (flags wired now, role in Phase 5).

### Phase 3 — Concept Scheme tabular editor (`/conceptScheme/:iri`)
- Spreadsheet grid: id (read-only), label, description, scheme, non-SKOS types,
  broader/narrower — inline-editable cells (free text or DB-filtered dropdowns
  honouring the same-DB constraints); edits flow into the shared pending-diff
  store; per-page Download All / Publish / Commit.

### Phase 4 — VocPrez convention enforcement + validators
- Auto-maintain on save: inverse/bidirectional `dcterms:isPartOf`⇄`hasPart` and
  `skos:hasTopConcept`⇄`inScheme`; `prefLabel`⇄`rdfs:label` mirroring;
  top-concept derivation (no `skos:broader` ⇒ `hasTopConcept` of its scheme);
  ConceptScheme↔Dataset membership (`dcterms:hasPart` + `dcat:dataset`).
- **Config-driven validator layer** — convention checks + optional SHACL
  (`rules.shacl`); the configurable "additional RDF validators" from the
  requirements. Surfaces warnings/blocks before Publish/Commit.

### Phase 5 — Auth (GitHub App) + RBAC
- GitHub App + OAuth login flow on the backend; resolve the user's **GitHub
  privileges** on the configured repo. Anonymous = edit + export (Download)
  only; editor role = **Publish** and **Commit** enabled. App-installation token
  authors the commits. All GitHub App params injected via config/secrets.

### Phase 6 — Config injectability & browser persistence
- **Externalise everything** still living as source literals: the Prez endpoint
  default, the prefix table and predicate palette (`src/rdf/terms.ts`), imported
  vocabularies, feature flags (Publish/Commit default **off**), validators, auth
  — all served through `/config.js` and surfaced as Helm values. Closes the
  "nothing hardcoded" requirement.
- Persist the pending-edit draft to **localStorage** so reloads don't lose work.

### Deferred
- Multiple schemes/DBs with imported prefixes (`requirements.md` §DB content
  organisation marks this `[TODO]`).

## Requirements traceability

| Requirement (requirements.md) | Phase | Status |
|---|---|---|
| Lightweight single container | (build) | ✅ |
| Edit VocPrez/Fuseki content, no RDF expertise | 1–3 | ◑ in progress |
| Config for endpoints | 1 / 6 | ✅ endpoint · ◑ full injectability in 6 |
| Config for secrets, credentials, **validators** | 4–6 | ☐ |
| Fast + **browser store** for changes | (build) / 6 | ◑ in-memory · localStorage in 6 |
| Commit only on user request | (build) | ✅ |
| Commit only for **authenticated** user | 5 | ☐ |
| Anonymous edit + export RDF | (build) | ✅ |
| **GitHub login + RBAC on GitHub privileges** | 5 | ☐ |
| Git KEY + Fuseki creds in config | 5–6 | ◑ git token yes · fuseki in 6 |
| Change/add predicate & object | (build) | ✅ |
| Browse concepts **and** schemes, filter by type | 2 | ☐ |
| Edit concept: text / term typeahead / external IRI | (build) | ✅ |
| **Blank nodes hidden, generated on export** | 1 / 2 | ✅ data · ◑ friendly edit in 2 |
| **Redundant fields shown once** | 2 | ☐ |
| **Concept Scheme tabular bulk editor** | 3 | ☐ |
| broader/narrower & inScheme limited to same DB | 2 | ☐ |
| Object typeahead = DB + **configurable imported vocabs** | 2 / 6 | ☐ |
| Predicate picker = DB predicates + configured prefixes | 2 / 6 | ◑ curated palette only |
| Per-edit-page **Download All / Publish / Commit** | 2–3 | ◑ global panel, old labels |
| Publish/Commit **disabled-by-default + RBAC** | 5–6 | ☐ |
| VocPrez content conventions (bidirectional, top-concepts, label mirror, Dataset) | 4 | ☐ |
| **Human-readable TTL serialisation** | 1 | ✅ |
| Default = Prez `prez-b/sparql`, empty graph | 1 | ✅ |
| GitHub App for auth & RBAC | 5 | ☐ |
| **Everything injectable, nothing hardcoded** | 6 (cross-cutting) | ◑ runtime `/config.js` exists; vocab/prefix/defaults pending |
| Multiple schemes/DBs + imported prefixes | deferred | ☐ `[TODO]` upstream |

Legend: ✅ done · ◑ partial · ☐ not started
