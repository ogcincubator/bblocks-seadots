import { useEffect, useMemo, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { useStore } from '../store/useStore';
import type { RdfValue, Triple } from '../rdf/model';
import { tripleKey } from '../rdf/model';
import {
  PREDICATES,
  PREFIXES,
  expandCurie,
  predicateLabel,
  toCurie,
  type PredicateDef,
} from '../rdf/terms';
import ValueEditor from '../components/ValueEditor';

interface Row {
  id: string;
  predicate: string;
  value: RdfValue;
}

const RDF_TYPE = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type';
const SKOS_CONCEPT = 'http://www.w3.org/2004/02/skos/core#Concept';
const CONCEPT_SCHEME = 'http://www.w3.org/2004/02/skos/core#ConceptScheme';

function predicateDef(iri: string): PredicateDef {
  return (
    PREDICATES.find((p) => p.iri === iri) ?? {
      iri,
      label: toCurie(iri),
      hint: 'Custom property',
      valueKind: 'either',
    }
  );
}

/** Object suggestions are narrowed for a couple of well-known predicates. */
function typeFilterFor(predicate: string): string[] | undefined {
  if (predicate === 'http://www.w3.org/2004/02/skos/core#inScheme') return [CONCEPT_SCHEME];
  return undefined;
}

let rowSeq = 0;
const newId = () => `r${rowSeq++}`;

export default function EditorPage() {
  const { iri: rawIri } = useParams();
  const iri = rawIri ? decodeURIComponent(rawIri) : undefined;
  const isNew = !iri;
  const navigate = useNavigate();

  const loadConcept = useStore((s) => s.loadConcept);
  const addTriple = useStore((s) => s.addTriple);
  const removeTriple = useStore((s) => s.removeTriple);

  const [subject, setSubject] = useState<string>(iri ?? '');
  const [newPrefix, setNewPrefix] = useState('indo');
  const [newLocal, setNewLocal] = useState('');
  const [rows, setRows] = useState<Row[]>([]);
  const [original, setOriginal] = useState<Triple[]>([]);
  const [addingField, setAddingField] = useState(false);
  const [customPred, setCustomPred] = useState('');
  const [saved, setSaved] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Load existing concept into editable rows.
  useEffect(() => {
    if (isNew) {
      setRows([
        { id: newId(), predicate: RDF_TYPE, value: { kind: 'iri', value: SKOS_CONCEPT } },
        { id: newId(), predicate: 'http://www.w3.org/2004/02/skos/core#prefLabel', value: { kind: 'literal', value: '', lang: 'en' } },
      ]);
      return;
    }
    void loadConcept(iri!).then((c) => {
      setOriginal(c.triples);
      setRows(c.triples.map((t) => ({ id: newId(), predicate: t.predicate, value: t.object })));
    });
  }, [iri, isNew, loadConcept]);

  const computedSubject = useMemo(() => {
    if (!isNew) return subject;
    const base = PREFIXES.find((p) => p.prefix === newPrefix)?.iri ?? '';
    return newLocal ? base + newLocal.trim() : '';
  }, [isNew, subject, newPrefix, newLocal]);

  function updateRow(id: string, value: RdfValue) {
    setRows((rs) => rs.map((r) => (r.id === id ? { ...r, value } : r)));
    setSaved(false);
  }

  function deleteRow(id: string) {
    setRows((rs) => rs.filter((r) => r.id !== id));
    setSaved(false);
  }

  function addField(predicate: string) {
    const def = predicateDef(predicate);
    const value: RdfValue =
      def.valueKind === 'iri'
        ? { kind: 'iri', value: '' }
        : { kind: 'literal', value: '', lang: def.langText ? 'en' : undefined };
    setRows((rs) => [...rs, { id: newId(), predicate, value }]);
    setAddingField(false);
    setCustomPred('');
    setSaved(false);
  }

  function rowsToTriples(): Triple[] {
    const subj = computedSubject;
    return rows
      .filter((r) => r.value.value.trim() !== '')
      .map((r) => ({ subject: subj, predicate: r.predicate, object: r.value }));
  }

  function save() {
    setError(null);
    const subj = computedSubject;
    if (!subj) {
      setError('Please give the concept an identifier first.');
      return;
    }
    const next = rowsToTriples();
    // For a renamed/new subject, the original triples (old subject) are removed.
    const origKeys = new Map(original.map((t) => [tripleKey(t), t]));
    const nextKeys = new Map(next.map((t) => [tripleKey(t), t]));

    // Removed = in original, not in next.
    for (const [k, t] of origKeys) {
      if (!nextKeys.has(k)) removeTriple(t);
    }
    // Added = in next, not in original.
    for (const [k, t] of nextKeys) {
      if (!origKeys.has(k)) addTriple(t);
    }
    setSaved(true);
    if (isNew) {
      // Treat the saved triples as the new baseline so further edits diff cleanly.
      setOriginal(next);
      setSubject(subj);
    }
  }

  // Group rows by predicate for display.
  const grouped = useMemo(() => {
    const map = new Map<string, Row[]>();
    for (const r of rows) {
      const arr = map.get(r.predicate) ?? [];
      arr.push(r);
      map.set(r.predicate, arr);
    }
    return [...map.entries()];
  }, [rows]);

  return (
    <div className="editor">
      <div className="editor-head">
        <h1>{isNew ? 'New concept' : 'Edit concept'}</h1>
        {isNew ? (
          <div className="iri-builder">
            <label>Identifier</label>
            <select value={newPrefix} onChange={(e) => setNewPrefix(e.target.value)}>
              {['indo', 'indp', 'indr', 'ind'].map((p) => (
                <option key={p} value={p}>
                  {p}:
                </option>
              ))}
            </select>
            <input
              className="local-input"
              value={newLocal}
              placeholder="local-name e.g. fish-stock-biomass"
              onChange={(e) => setNewLocal(e.target.value.replace(/\s+/g, '-'))}
            />
            <code className="iri-preview">{computedSubject || '—'}</code>
          </div>
        ) : (
          <code className="iri-preview big">{toCurie(subject)}</code>
        )}
      </div>

      <div className="fields">
        {grouped.map(([predicate, predRows]) => {
          const def = predicateDef(predicate);
          return (
            <div className="field-group" key={predicate}>
              <div className="field-label" title={predicate}>
                {predicateLabel(predicate)}
                <span className="field-curie">{toCurie(predicate)}</span>
                <span className="field-hint">{def.hint}</span>
              </div>
              <div className="field-values">
                {predRows.map((r) => (
                  <div className="field-value-row" key={r.id}>
                    <ValueEditor
                      value={r.value}
                      kind={def.valueKind}
                      typeFilter={typeFilterFor(predicate)}
                      onChange={(v) => updateRow(r.id, v)}
                    />
                    <button type="button" className="icon-btn" title="Remove value" onClick={() => deleteRow(r.id)}>
                      🗑
                    </button>
                  </div>
                ))}
                <button type="button" className="link-btn" onClick={() => addField(predicate)}>
                  + add another value
                </button>
              </div>
            </div>
          );
        })}
      </div>

      <div className="add-field">
        {addingField ? (
          <div className="add-field-pick">
            <select
              defaultValue=""
              onChange={(e) => {
                if (e.target.value) addField(e.target.value);
              }}
            >
              <option value="" disabled>
                Choose a property to add…
              </option>
              {PREDICATES.map((p) => (
                <option key={p.iri} value={p.iri}>
                  {p.label} ({toCurie(p.iri)})
                </option>
              ))}
            </select>
            <span className="or">or</span>
            <input
              placeholder="custom property IRI / CURIE"
              value={customPred}
              onChange={(e) => setCustomPred(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === 'Enter' && customPred.trim()) addField(expandCurie(customPred.trim()));
              }}
            />
            <button type="button" className="link-btn" onClick={() => setAddingField(false)}>
              cancel
            </button>
          </div>
        ) : (
          <button type="button" className="secondary" onClick={() => setAddingField(true)}>
            + Add field
          </button>
        )}
      </div>

      {error && <p className="error">⚠ {error}</p>}

      <div className="editor-actions">
        <button type="button" className="primary" onClick={save}>
          Save to draft
        </button>
        {saved && <span className="ok">✓ Added to your pending changes (review bottom-right)</span>}
        <button type="button" className="secondary" onClick={() => navigate('/')}>
          Back to browse
        </button>
      </div>
    </div>
  );
}
