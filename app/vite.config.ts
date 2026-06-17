import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// The Fuseki endpoint already returns permissive CORS headers, so the browser
// can talk to it directly. We still expose a dev proxy under /sparql as a
// fallback for environments where CORS is restricted; toggle it via config.ts.
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      // Forward git-commit API calls to the backend during local dev.
      '/api': {
        target: process.env.VITE_API_TARGET || 'http://localhost:8080',
        changeOrigin: true,
      },
      '/sparql': {
        target: 'http://defs-hosted.opengis.net/fuseki-hosted',
        changeOrigin: true,
        rewrite: (p) => p.replace(/^\/sparql/, ''),
      },
    },
  },
});
