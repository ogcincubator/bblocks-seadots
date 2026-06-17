/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_SPARQL_QUERY?: string;
  readonly VITE_SPARQL_UPDATE?: string;
  readonly VITE_GRAPH?: string;
  readonly VITE_API_BASE?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
