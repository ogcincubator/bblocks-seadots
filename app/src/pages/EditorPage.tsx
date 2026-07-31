import { useEffect, useMemo, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { useStore } from '../store/useStore';
import type { RdfValue, Triple } from '../rdf/model';
import { tripleKey } from '../rdf/model';
import {
  PREDICATES,
  PREFIXES,
  MERGED_LABEL,
  MERGED_LABEL_EXPANDS_TO,
  SKOS_PREF_LABEL,
  RDFS_LABEL,
  RDF_TYPE,
  SKOS_CONCEPT,
  typeFilterFor,
  sourceFilterFor,
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

/**
 * Collapse the redundant skos:prefLabel / rdfs:label triples into a single
 * MERGED_LABEL row (prefLabel primary). Other triples pass through unchanged.
 */
function collapseLabels(triples: Triple[]): Row[] {
  const rows: Row[] = [];
  const seenLabel = new Set<string>(); // value|lang already emitted as merged
  const prefByKey = new Map<string, RdfValue>();
  for (const t of triples) {
    if (t.predicate === SKOS_PREF_LABEL) prefByKey.set(`${t.object.value}|${t.object.lang ?? ''}`, t.object);
  }
  for (const t of triples) {
    if (t.predicate === SKOS_PREF_LABEL || t.predicate === RDFS_LABEL) {
      const key = `${t.object.value}|${t.object.lang ?? ''}`;
      // Prefer the prefLabel instance; emit each distinct label value once.
      const primary = prefByKey.get(key) ?? t.object;
      if (seenLabel.has(key)) continue;
      seenLabel.add(key);
      rows.push({ id: newId(), predicate: MERGED_LABEL, value: primary });
      continue;
    }
    rows.push({ id: newId(), predicate: t.predicate, value: t.object });
  }
  return rows;
}

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
  const dbPredicates = useStore((s) => s.predicates);

  // DB predicates not already covered by the curated palette.
  const extraDbPredicates = useMemo(() => {
    const known = new Set(PREDICATES.map((p) => p.iri));
    return dbPredicates.filter((p) => !known.has(p)).sort((a, b) => toCurie(a).localeCompare(toCurie(b)));
  }, [dbPredicates]);

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
        { id: newId(), predicate: MERGED_LABEL, value: { kind: 'literal', value: '', lang: 'en' } },
      ]);
      return;
    }
    void loadConcept(iri!).then((c) => {
      setOriginal(c.triples);
      setRows(collapseLabels(c.triples));
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
    const out: Triple[] = [];
    for (const r of rows) {
      // Drop empty literal/iri rows (blank nodes have no scalar value).
      if (r.value.kind !== 'bnode' && r.value.value.trim() === '') continue;
      if (r.predicate === MERGED_LABEL) {
        // Expand to both prefLabel and rdfs:label (mirrored), prefLabel primary.
        for (const p of MERGED_LABEL_EXPANDS_TO) {
          out.push({ subject: subj, predicate: p, object: r.value });
        }
      } else {
        out.push({ subject: subj, predicate: r.predicate, object: r.value });
      }
    }
    return out;
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
                <span className="field-curie">
                  {predicate === MERGED_LABEL ? 'skos:prefLabel + rdfs:label' : toCurie(predicate)}
                </span>
                <span className="field-hint">{def.hint}</span>
              </div>
              <div className="field-values">
                {predRows.map((r) => (
                  <div className="field-value-row" key={r.id}>
                    <ValueEditor
                      value={r.value}
                      kind={def.valueKind}
                      typeFilter={typeFilterFor(predicate)}
                      sourceFilter={sourceFilterFor(predicate)}
                      exclude={sourceFilterFor(predicate) === 'db' ? computedSubject : undefined}
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
              <optgroup label="Common properties">
                {PREDICATES.map((p) => (
                  <option key={p.iri} value={p.iri}>
                    {p.label} ({toCurie(p.iri)})
                  </option>
                ))}
              </optgroup>
              {extraDbPredicates.length > 0 && (
                <optgroup label="Other properties used in this database">
                  {extraDbPredicates.map((p) => (
                    <option key={p} value={p}>
                      {toCurie(p)}
                    </option>
                  ))}
                </optgroup>
              )}
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
