// Central runtime configuration for the SeaDOTs concept editor.
//
// Defaults point at the SeaDOTs Prez (VocPrez) SPARQL backend, whose data lives
// in the default graph (so VITE_GRAPH is empty). Override at build/run time with
// Vite env vars (VITE_SPARQL_QUERY, VITE_SPARQL_UPDATE, VITE_GRAPH) or the
// backend-served /config.js (Helm).

// `import.meta.env` is injected by Vite; guard so the module is also importable
// under plain Node (tests, tooling).
const env = (import.meta as { env?: Record<string, string | undefined> }).env ?? {};

// Runtime config injected by the backend at /config.js (see server/index.mjs).
// This lets a single pre-built image be deployed with different endpoints via
// Helm/env without rebuilding. Falls back to Vite build-time env, then defaults.
interface RuntimeConfig {
  queryEndpoint?: string;
  updateEndpoint?: string;
  graph?: string;
  apiBase?: string;
  publishEnabled?: boolean;
  commitEnabled?: boolean;
  importedNamespaces?: string[];
}
const rt: RuntimeConfig =
  (typeof window !== 'undefined' && (window as { __APP_CONFIG__?: RuntimeConfig }).__APP_CONFIG__) || {};

function envBool(v: string | undefined): boolean | undefined {
  if (v === undefined) return undefined;
  return v === 'true' || v === '1';
}
function envList(v: string | undefined): string[] | undefined {
  if (v === undefined) return undefined;
  return v.split(',').map((s) => s.trim()).filter(Boolean);
}

const PREZ = 'https://project-seadots-definition-server.lab.dive.edito.eu/prez-b';

export const config = {
  /** SPARQL 1.1 Query endpoint (read). */
  queryEndpoint: rt.queryEndpoint ?? env.VITE_SPARQL_QUERY ?? `${PREZ}/sparql`,

  /** SPARQL 1.1 Update endpoint (write). May require credentials. */
  updateEndpoint: rt.updateEndpoint ?? env.VITE_SPARQL_UPDATE ?? `${PREZ}/update`,

  /**
   * Named graph the concepts live in. Empty string = default graph (the Prez
   * backend stores everything there). `??` preserves an explicit empty value.
   */
  graph: rt.graph ?? env.VITE_GRAPH ?? '',

  /**
   * Base URL of the backend API (git-commit endpoint). Empty string = same
   * origin (production: app and API are served by the same Node server). In dev
   * the Vite proxy forwards /api to the backend, so empty also works.
   */
  apiBase: rt.apiBase ?? env.VITE_API_BASE ?? '',

  /**
   * Write-path feature flags. Disabled by default per requirements; the actual
   * button visibility also depends on RBAC role (Phase 5).
   */
  publishEnabled: rt.publishEnabled ?? envBool(env.VITE_PUBLISH_ENABLED) ?? false,
  commitEnabled: rt.commitEnabled ?? envBool(env.VITE_COMMIT_ENABLED) ?? false,

  /**
   * Namespace IRIs treated as *imported* vocabularies. Terms under these
   * prefixes are offered as autocomplete objects but excluded from same-DB-only
   * pickers (broader/narrower/inScheme). Everything else counts as in-DB.
   */
  importedNamespaces:
    rt.importedNamespaces ?? envList(env.VITE_IMPORTED_NAMESPACES) ?? [],
};
