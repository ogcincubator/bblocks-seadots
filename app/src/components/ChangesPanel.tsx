import { useEffect, useState } from 'react';
import { config } from '../config';
import { useStore } from '../store/useStore';
import { toTurtle, toSparqlUpdate, termToString } from '../rdf/serialize';
import { toCurie, predicateLabel } from '../rdf/terms';
import type { Triple } from '../rdf/model';

function line(t: Triple) {
  return `${toCurie(t.subject)}  ${predicateLabel(t.predicate)}  ${termToString(t.object)}`;
}

/**
 * Floating panel summarising pending edits. Lets the editor review the diff and
 * either download a Turtle file (to commit via the bblocks repo) or push a
 * SPARQL UPDATE straight to the triplestore.
 */
export default function ChangesPanel() {
  const added = useStore((s) => s.added);
  const removed = useStore((s) => s.removed);
  const discard = useStore((s) => s.discardChanges);
  const push = useStore((s) => s.pushToSparql);
  const commitToGit = useStore((s) => s.commitToGit);

  const [open, setOpen] = useState(false);
  const [showTtl, setShowTtl] = useState(false);
  const [pushing, setPushing] = useState(false);
  const [committing, setCommitting] = useState(false);
  const [gitEnabled, setGitEnabled] = useState(false);
  const [gitBranch, setGitBranch] = useState('');
  const [commitMsg, setCommitMsg] = useState('');
  const [msg, setMsg] = useState<string | null>(null);

  // Detect whether a git-capable backend is present (hidden for static deploys).
  useEffect(() => {
    fetch(`${config.apiBase}/api/git/status`)
      .then((r) => (r.ok ? r.json() : null))
      .then((j) => {
        if (j?.enabled) {
          setGitEnabled(true);
          setGitBranch(j.branch);
        }
      })
      .catch(() => setGitEnabled(false));
  }, []);

  const total = added.length + removed.length;
  if (total === 0) return null;

  function download() {
    const ttl = toTurtle(added);
    const blob = new Blob([ttl], { type: 'text/turtle' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'seadots-additions.ttl';
    a.click();
    URL.revokeObjectURL(url);
  }

  async function doPush() {
    setPushing(true);
    setMsg(null);
    try {
      await push();
      setMsg('✓ Pushed to the triplestore.');
      setOpen(false);
    } catch (e) {
      setMsg('⚠ ' + (e as Error).message);
    } finally {
      setPushing(false);
    }
  }

  async function doCommit() {
    setCommitting(true);
    setMsg(null);
    try {
      const r = await commitToGit(commitMsg || 'Concept edits via SeaDOTs editor');
      setMsg(
        `✓ Committed ${r.commit.slice(0, 8)} to ${r.branch}${r.pushed ? ' (pushed)' : ' (local)'} — ${r.file}`,
      );
      setCommitMsg('');
    } catch (e) {
      setMsg('⚠ ' + (e as Error).message);
    } finally {
      setCommitting(false);
    }
  }

  return (
    <div className={open ? 'changes-panel open' : 'changes-panel'}>
      <button className="changes-toggle" onClick={() => setOpen((o) => !o)}>
        {open ? '▾' : '▴'} Pending changes <span className="badge">{total}</span>
      </button>
      {open && (
        <div className="changes-body">
          {removed.length > 0 && (
            <>
              <h4 className="diff-h del">Removing ({removed.length})</h4>
              <ul className="diff">
                {removed.map((t, i) => (
                  <li key={i} className="del">− {line(t)}</li>
                ))}
              </ul>
            </>
          )}
          {added.length > 0 && (
            <>
              <h4 className="diff-h ins">Adding ({added.length})</h4>
              <ul className="diff">
                {added.map((t, i) => (
                  <li key={i} className="ins">+ {line(t)}</li>
                ))}
              </ul>
            </>
          )}

          <div className="changes-actions">
            <button className="secondary" onClick={download}>
              ⬇ Download Turtle
            </button>
            <button className="primary" onClick={doPush} disabled={pushing}>
              {pushing ? 'Pushing…' : '↥ Push to triplestore'}
            </button>
            <button className="link-btn" onClick={() => setShowTtl((v) => !v)}>
              {showTtl ? 'hide' : 'view'} SPARQL
            </button>
            <button className="link-btn danger" onClick={discard}>
              discard all
            </button>
          </div>

          {gitEnabled && (
            <div className="git-commit">
              <input
                className="commit-msg"
                value={commitMsg}
                placeholder={`Commit message (branch: ${gitBranch})`}
                onChange={(e) => setCommitMsg(e.target.value)}
              />
              <button className="secondary" onClick={doCommit} disabled={committing || added.length === 0}>
                {committing ? 'Committing…' : ' Commit to Git'}
              </button>
            </div>
          )}
          {msg && <p className={msg.startsWith('✓') ? 'ok' : 'error'}>{msg}</p>}
          {showTtl && <pre className="ttl-preview">{toSparqlUpdate(added, removed)}</pre>}
        </div>
      )}
    </div>
  );
}
