/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_SPARQL_QUERY?: string;
  readonly VITE_SPARQL_UPDATE?: string;
  readonly VITE_GRAPH?: string;
  readonly VITE_API_BASE?: string;
  readonly VITE_PUBLISH_ENABLED?: string;
  readonly VITE_COMMIT_ENABLED?: string;
  readonly VITE_IMPORTED_NAMESPACES?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
