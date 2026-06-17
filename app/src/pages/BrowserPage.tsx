import { useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import { useStore } from '../store/useStore';
import { toCurie } from '../rdf/terms';

const TYPE_LABELS: Record<string, string> = {
  'https://w3id.org/indicators/marine/Indicator': 'Indicator',
  'http://www.w3.org/ns/sosa/ObservableProperty': 'Observable property',
  'http://www.w3.org/ns/ssn/Property': 'Model parameter',
  'https://w3id.org/ogc/hosted/seadots/prop-rel/PropertyRelationship': 'Relationship',
  'http://www.w3.org/2004/02/skos/core#Concept': 'Concept',
};

function typeName(iri: string): string {
  return TYPE_LABELS[iri] ?? toCurie(iri);
}

export default function BrowserPage() {
  const conceptList = useStore((s) => s.conceptList);
  const schemes = useStore((s) => s.schemes);
  const loading = useStore((s) => s.loading);

  const [q, setQ] = useState('');
  const [scheme, setScheme] = useState('');
  const [type, setType] = useState('');

  const allTypes = useMemo(() => {
    const set = new Set<string>();
    conceptList.forEach((c) => c.types.forEach((t) => set.add(t)));
    return [...set];
  }, [conceptList]);

  const filtered = useMemo(() => {
    const needle = q.trim().toLowerCase();
    return conceptList
      .filter((c) => {
        if (scheme && !c.schemes.includes(scheme)) return false;
        if (type && !c.types.includes(type)) return false;
        if (needle) {
          const hay = (c.label + ' ' + toCurie(c.iri)).toLowerCase();
          if (!hay.includes(needle)) return false;
        }
        return true;
      })
      .sort((a, b) => a.label.localeCompare(b.label));
  }, [conceptList, q, scheme, type]);

  return (
    <div className="browser">
      <div className="filters">
        <input
          className="search"
          value={q}
          placeholder="Search concepts by name…"
          onChange={(e) => setQ(e.target.value)}
        />
        <select value={scheme} onChange={(e) => setScheme(e.target.value)}>
          <option value="">All schemes</option>
          {schemes.map((s) => (
            <option key={s.iri} value={s.iri}>
              {s.label}
            </option>
          ))}
        </select>
        <select value={type} onChange={(e) => setType(e.target.value)}>
          <option value="">All types</option>
          {allTypes.map((t) => (
            <option key={t} value={t}>
              {typeName(t)}
            </option>
          ))}
        </select>
        <span className="count">{filtered.length} concepts</span>
      </div>

      {loading && conceptList.length === 0 ? (
        <p className="muted">Loading concepts from the triplestore…</p>
      ) : (
        <ul className="concept-list">
          {filtered.map((c) => (
            <li key={c.iri}>
              <Link to={`/concept/${encodeURIComponent(c.iri)}`} className="concept-card">
                <div className="concept-main">
                  <span className="concept-label">{c.label}</span>
                  <code className="concept-curie">{toCurie(c.iri)}</code>
                </div>
                <div className="concept-tags">
                  {c.types.filter((t) => TYPE_LABELS[t]).map((t) => (
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
