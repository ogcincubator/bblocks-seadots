// Central runtime configuration for the SeaDOTs concept editor.
//
// The defaults point at the live SeaDOTs Fuseki instance and named graph
// declared in bblocks-config.yaml. Override at build/run time with Vite env
// vars (VITE_SPARQL_QUERY, VITE_SPARQL_UPDATE, VITE_GRAPH).

const env = import.meta.env;

// Runtime config injected by the backend at /config.js (see server/index.mjs).
// This lets a single pre-built image be deployed with different endpoints via
// Helm/env without rebuilding. Falls back to Vite build-time env, then defaults.
interface RuntimeConfig {
  queryEndpoint?: string;
  updateEndpoint?: string;
  graph?: string;
  apiBase?: string;
}
const rt: RuntimeConfig =
  (typeof window !== 'undefined' && (window as { __APP_CONFIG__?: RuntimeConfig }).__APP_CONFIG__) || {};

export const config = {
  /** SPARQL 1.1 Query endpoint (read). */
  queryEndpoint:
    rt.queryEndpoint ?? env.VITE_SPARQL_QUERY ?? 'http://defs-hosted.opengis.net/fuseki-hosted/query',

  /** SPARQL 1.1 Update endpoint (write). May require credentials. */
  updateEndpoint:
    rt.updateEndpoint ?? env.VITE_SPARQL_UPDATE ?? 'http://defs-hosted.opengis.net/fuseki-hosted/update',

  /** Named graph the SeaDOTs concepts live in. */
  graph: rt.graph ?? env.VITE_GRAPH ?? 'https://w3id.org/ogc/hosted/seadots',

  /**
   * Base URL of the backend API (git-commit endpoint). Empty string = same
   * origin (production: app and API are served by the same Node server). In dev
   * the Vite proxy forwards /api to the backend, so empty also works.
   */
  apiBase: rt.apiBase ?? env.VITE_API_BASE ?? '',
};
