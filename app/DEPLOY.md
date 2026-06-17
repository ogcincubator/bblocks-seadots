# Deploying the SeaDOTs Concept Editor

The app ships as a single container: a Node server that serves the built SPA and
exposes the git-commit API. SPARQL traffic goes browser → triplestore directly.

## 1. Build & publish the image

```bash
cd app

# Build locally (tags :<git-sha> and :latest)
./build-image.sh

# Build and push to a registry
IMAGE=ghcr.io/ogcincubator/seadots-concept-editor TAG=0.1.0 ./build-image.sh --push
```

The Dockerfile is multi-stage: stage 1 runs `npm run build` (Vite), stage 2 runs
the Node server with production deps and `git` installed for the commit/push
endpoint.

Optional: bake SPARQL defaults into the bundle at build time with
`--build-arg VITE_SPARQL_QUERY=...`. Otherwise endpoints are supplied at
**runtime** via env (preferred — one image, many environments).

## 2. Run with Docker (quick test)

```bash
docker run --rm -p 8080:8080 \
  -e SPARQL_QUERY=http://defs-hosted.opengis.net/fuseki-hosted/query \
  -e SPARQL_UPDATE=http://defs-hosted.opengis.net/fuseki-hosted/update \
  -e SPARQL_GRAPH=https://w3id.org/ogc/hosted/seadots \
  -e GIT_REMOTE_URL=https://github.com/ogcincubator/bblocks-seadots.git \
  -e GIT_TOKEN=ghp_xxx \
  ghcr.io/ogcincubator/seadots-concept-editor:latest
# open http://localhost:8080
```

## 3. Deploy with Helm

```bash
helm upgrade --install concept-editor app/helm/seadots-concept-editor \
  --set image.tag=0.1.0 \
  --set sparql.query=http://defs-hosted.opengis.net/fuseki-hosted/query \
  --set sparql.update=http://defs-hosted.opengis.net/fuseki-hosted/update \
  --set sparql.graph=https://w3id.org/ogc/hosted/seadots \
  --set git.remoteUrl=https://github.com/ogcincubator/bblocks-seadots.git \
  --set git.branch=concept-edits \
  --set git.existingSecret=concept-editor-git \
  --set ingress.enabled=true \
  --set ingress.hosts[0].host=concept-editor.example.org \
  --set ingress.hosts[0].paths[0].path=/ \
  --set ingress.hosts[0].paths[0].pathType=Prefix
```

Create the git token secret beforehand (recommended over inline `git.token`):

```bash
kubectl create secret generic concept-editor-git --from-literal=token=ghp_xxx
```

### Key values

| Value | Purpose | Default |
|-------|---------|---------|
| `image.repository` / `image.tag` | container image | `ghcr.io/.../seadots-concept-editor` / chart appVersion |
| `sparql.query` / `sparql.update` / `sparql.graph` | endpoints injected into the SPA at runtime (`/config.js`) | live Fuseki |
| `git.enabled` | expose the commit-to-git button | `true` |
| `git.remoteUrl` / `git.branch` / `git.editsPath` | where edits are committed | repo / `concept-edits` / `_sources/oim-variables/edits` |
| `git.push` | push after commit (vs. local-only) | `true` |
| `git.token` / `git.existingSecret` | auth for clone + push | — |
| `persistence.enabled` | keep the cloned repo across restarts | `false` |
| `ingress.*` | expose externally | disabled |

Full list: [`helm/seadots-concept-editor/values.yaml`](helm/seadots-concept-editor/values.yaml).

## How config reaches the browser

Vite inlines env vars at build time, so to keep **one** image reusable the
server serves `GET /config.js` which sets `window.__APP_CONFIG__` from the
container's `SPARQL_*` env. `src/config.ts` reads that global first, then
build-time env, then compiled defaults. Changing endpoints = change Helm values
+ restart, no rebuild.

## Security notes

- The git token grants push access — store it in a Secret, never inline in a
  committed values file. Use a fine-grained/deploy token scoped to this repo.
- Edits are committed to a **separate branch** (`concept-edits`) for review via
  PR, not straight to `master`.
- The SPARQL **update** endpoint write path depends on the triplestore's own
  auth; if it rejects anonymous writes, prefer the git-commit flow.
- Consider protecting the app itself (ingress auth / SSO) since it can write to
  both the triplestore and the repo.
