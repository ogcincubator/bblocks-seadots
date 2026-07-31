# SeaDOTs Concept Editor

A small front end that lets **non-RDF experts** browse and edit the SeaDOTs OIM
concepts (indicators, observable properties, model parameters and their
relationships) that live in the SeaDOTs triplestore — without ever writing
Turtle or SPARQL by hand.

It reads directly from the live Fuseki SPARQL endpoint declared in configuration but it can be different from the one in the `../bblocks-config.yaml` (graph `https://w3id.org/ogc/hosted/seadots`).

# Specification

Requirements for the applciation are collected in the [docs/requirements.md](docs/requirements.md)

## Architecture & deployment

- **Data exchange sequence diagrams:** [`docs/data-exchange.md`](docs/data-exchange.md)
  — every triplestore and git interaction as Mermaid sequence diagrams.
- **Build & deploy (Docker + Helm):** [`DEPLOY.md`](DEPLOY.md).

In production a single Node server (`server/`) serves the built SPA and the
git-commit API (`POST /api/git/commit`). SPARQL reads/writes go from the browser
straight to the triplestore. Run the backend in dev with:

```bash
npm run build        # produce dist/
GIT_REMOTE_URL=... GIT_TOKEN=... npm start   # serves SPA + git API on :8080
# or, with the Vite dev server proxying /api to it:
npm run dev:server   # terminal 1 (backend on :8080)
npm run dev          # terminal 2 (Vite on :5173, proxies /api + /sparql)
```

## Run

```bash
cd app
npm install
npm run dev        # http://localhost:5173
npm run build      # type-check + production build into dist/
```

### tmux

To run both development servers in one tmux session, after `npm install` use:

```bash
npm run dev:tmux
```

This creates (or reattaches to) the `seadots-concept-editor` session with the
API server on the left and Vite on the right. Detach with `Ctrl-b d`; stop both
servers with `tmux kill-session -t seadots-concept-editor`.

## Configuration

Defaults target the live SeaDOTs Fuseki instance. Override with Vite env vars
(e.g. an `.env.local`):

| Variable              | Default                                                        |
|-----------------------|----------------------------------------------------------------|
| `VITE_SPARQL_QUERY`   | `http://defs-hosted.opengis.net/fuseki-hosted/query`           |
| `VITE_SPARQL_UPDATE`  | `http://defs-hosted.opengis.net/fuseki-hosted/update`          |
| `VITE_GRAPH`          | `https://w3id.org/ogc/hosted/seadots`                          |

The endpoint already returns permissive CORS headers, so the browser talks to
it directly. If you hit a CORS wall in another environment, `vite.config.ts`
also exposes a `/sparql` dev proxy you can point the config at.

## Structure

```
src/
  config.ts              endpoint + graph configuration
  rdf/
    terms.ts             prefixes, predicate palette, CURIE helpers
    model.ts             Triple / Concept / Term types + diff keys
    serialize.ts         Turtle + SPARQL UPDATE serialization
  sparql/
    queries.ts           SPARQL query strings
    client.ts            fetch wrappers (select / update)
  store/useStore.ts      Zustand store: catalog cache + pending-edit diff
  components/
    TermAutocomplete.tsx vocabulary typeahead
    ValueEditor.tsx      literal-vs-term value input
    ChangesPanel.tsx     diff review + download/push
  pages/
    BrowserPage.tsx      page 1 — browse/search
    EditorPage.tsx       page 2 — concept editor
```
