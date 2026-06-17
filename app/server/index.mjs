// Production server for the SeaDOTs Concept Editor.
//
// Responsibilities:
//   1. Serve the built single-page app (dist/) as static files.
//   2. Expose a small JSON API to commit/push editor changes to git.
// SPARQL traffic goes browser -> triplestore directly (CORS is open), so it is
// not proxied here.

import express from 'express';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { commitTurtle, gitConfig } from './git.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const distDir = path.resolve(__dirname, '..', 'dist');
const port = Number(process.env.PORT || 8080);

const app = express();
app.use(express.json({ limit: '4mb' }));

// Runtime configuration injected into the SPA. Lets one image be deployed with
// different SPARQL endpoints/graph via env vars (no rebuild needed).
app.get('/config.js', (_req, res) => {
  const cfg = {
    queryEndpoint: process.env.SPARQL_QUERY || process.env.VITE_SPARQL_QUERY || '',
    updateEndpoint: process.env.SPARQL_UPDATE || process.env.VITE_SPARQL_UPDATE || '',
    graph: process.env.SPARQL_GRAPH || process.env.VITE_GRAPH || '',
    apiBase: process.env.API_BASE || '',
  };
  // Drop empty values so the app's compiled-in defaults win.
  const filtered = Object.fromEntries(Object.entries(cfg).filter(([, v]) => v));
  res.type('application/javascript');
  res.send(`window.__APP_CONFIG__ = ${JSON.stringify(filtered)};`);
});

app.get('/api/health', (_req, res) => {
  res.json({
    ok: true,
    git: { branch: gitConfig.branch, editsPath: gitConfig.editsPath, push: gitConfig.push },
  });
});

// Report whether the git-commit feature is wired up, so the UI can hide the
// button when running as a pure static deployment.
app.get('/api/git/status', (_req, res) => {
  res.json({
    enabled: true,
    branch: gitConfig.branch,
    remote: gitConfig.remote,
    push: gitConfig.push,
  });
});

app.post('/api/git/commit', async (req, res) => {
  try {
    const { turtle, message, filename } = req.body ?? {};
    const result = await commitTurtle({ turtle, message, filename });
    res.json({ ok: true, ...result });
  } catch (e) {
    console.error('git commit failed:', e);
    res.status(500).json({ ok: false, error: String(e.message || e) });
  }
});

// Static SPA with history-API fallback.
app.use(express.static(distDir));
app.get('*', (_req, res) => {
  res.sendFile(path.join(distDir, 'index.html'));
});

app.listen(port, () => {
  console.log(`SeaDOTs Concept Editor listening on :${port}`);
  console.log(`  git branch: ${gitConfig.branch} (push=${gitConfig.push})`);
});
