import { useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import { useStore } from '../store/useStore';
import { toCurie, CONCEPT_SCHEME, TYPE_LABELS, typeName } from '../rdf/terms';

interface Entity {
  iri: string;
  label: string;
  kind: 'concept' | 'scheme';
  types: string[];
  schemes: string[];
}

export default function BrowserPage() {
  const conceptList = useStore((s) => s.conceptList);
  const schemeList = useStore((s) => s.schemes);
  const loading = useStore((s) => s.loading);

  const [q, setQ] = useState('');
  const [kind, setKind] = useState<'' | 'concept' | 'scheme'>('');
  const [scheme, setScheme] = useState('');
  const [type, setType] = useState('');

  // Concepts and concept schemes are browsed together as first-class entities.
  const entities = useMemo<Entity[]>(() => {
    const concepts: Entity[] = conceptList.map((c) => ({ ...c, kind: 'concept' }));
    const schemes: Entity[] = schemeList.map((s) => ({
      iri: s.iri,
      label: s.label,
      kind: 'scheme',
      types: [CONCEPT_SCHEME],
      schemes: [],
    }));
    return [...schemes, ...concepts];
  }, [conceptList, schemeList]);

  const allTypes = useMemo(() => {
    const set = new Set<string>();
    conceptList.forEach((c) => c.types.forEach((t) => set.add(t)));
    return [...set];
  }, [conceptList]);

  const filtered = useMemo(() => {
    const needle = q.trim().toLowerCase();
    return entities
      .filter((e) => {
        if (kind && e.kind !== kind) return false;
        if (scheme && !e.schemes.includes(scheme)) return false;
        if (type && !e.types.includes(type)) return false;
        if (needle) {
          const hay = (e.label + ' ' + toCurie(e.iri)).toLowerCase();
          if (!hay.includes(needle)) return false;
        }
        return true;
      })
      .sort((a, b) => a.label.localeCompare(b.label));
  }, [entities, q, kind, scheme, type]);

  return (
    <div className="browser">
      <div className="filters">
        <input
          className="search"
          value={q}
          placeholder="Search by name…"
          onChange={(e) => setQ(e.target.value)}
        />
        <select value={kind} onChange={(e) => setKind(e.target.value as typeof kind)}>
          <option value="">Concepts & schemes</option>
          <option value="concept">Concepts</option>
          <option value="scheme">Concept schemes</option>
        </select>
        <select value={scheme} onChange={(e) => setScheme(e.target.value)} disabled={kind === 'scheme'}>
          <option value="">All schemes</option>
          {schemeList.map((s) => (
            <option key={s.iri} value={s.iri}>
              {s.label}
            </option>
          ))}
        </select>
        <select value={type} onChange={(e) => setType(e.target.value)} disabled={kind === 'scheme'}>
          <option value="">All types</option>
          {allTypes.map((t) => (
            <option key={t} value={t}>
              {typeName(t)}
            </option>
          ))}
        </select>
        <span className="count">{filtered.length} items</span>
      </div>

      {loading && entities.length === 0 ? (
        <p className="muted">Loading from the triplestore…</p>
      ) : (
        <ul className="concept-list">
          {filtered.map((e) => (
            <li key={e.iri}>
              <Link
                to={
                  e.kind === 'scheme'
                    ? `/conceptScheme/${encodeURIComponent(e.iri)}`
                    : `/concept/${encodeURIComponent(e.iri)}`
                }
                className={e.kind === 'scheme' ? 'concept-card scheme' : 'concept-card'}
              >
                <div className="concept-main">
                  <span className="concept-label">{e.label}</span>
                  <code className="concept-curie">{toCurie(e.iri)}</code>
                </div>
                <div className="concept-tags">
                  {e.kind === 'scheme' && <span className="tag scheme-tag">Concept scheme</span>}
                  {e.types
                    .filter((t) => TYPE_LABELS[t] && t !== CONCEPT_SCHEME)
                    .map((t) => (
                      <span className="tag" key={t}>
                        {typeName(t)}
                      </span>
                    ))}
                </div>
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
