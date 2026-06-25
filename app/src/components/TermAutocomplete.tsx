import { useMemo, useRef, useState } from 'react';
import { useStore } from '../store/useStore';
import type { Term } from '../rdf/model';
import { toCurie } from '../rdf/terms';

interface Props {
  /** Currently selected IRI value (or empty). */
  value: string;
  onChange: (iri: string, label?: string) => void;
  placeholder?: string;
  /** Restrict suggestions to terms whose type is one of these IRIs. */
  typeFilter?: string[];
  /** Restrict suggestions by origin: 'db' = same database only. */
  sourceFilter?: 'db' | 'imported';
  autoFocus?: boolean;
}

/**
 * Typeahead over the vocabulary term index. As the user types, terms from this
 * vocabulary AND imported/materialised vocabularies are filtered by label or
 * CURIE. The user can also paste a raw IRI for anything not yet in the store.
 */
export default function TermAutocomplete({
  value,
  onChange,
  placeholder,
  typeFilter,
  sourceFilter,
  autoFocus,
}: Props) {
  const terms = useStore((s) => s.terms);
  const [query, setQuery] = useState('');
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState(0);
  const boxRef = useRef<HTMLDivElement>(null);

  const pool = useMemo(() => {
    return terms.filter((t) => {
      if (typeFilter && typeFilter.length && !t.types.some((ty) => typeFilter.includes(ty)))
        return false;
      if (sourceFilter && t.source !== sourceFilter) return false;
      return true;
    });
  }, [terms, typeFilter, sourceFilter]);

  const matches = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return pool.slice(0, 30);
    const scored = pool
      .map((t) => {
        const label = t.label.toLowerCase();
        const curie = toCurie(t.iri).toLowerCase();
        let score = -1;
        if (label.startsWith(q)) score = 0;
        else if (label.includes(q)) score = 1;
        else if (curie.includes(q)) score = 2;
        return { t, score };
      })
      .filter((x) => x.score >= 0)
      .sort((a, b) => a.score - b.score || a.t.label.localeCompare(b.t.label));
    return scored.slice(0, 30).map((x) => x.t);
  }, [pool, query]);

  const selectedLabel =
    terms.find((t) => t.iri === value)?.label ?? (value ? toCurie(value) : '');

  function choose(t: Term) {
    onChange(t.iri, t.label);
    setQuery('');
    setOpen(false);
  }

  function commitRaw() {
    const raw = query.trim();
    if (raw) {
      onChange(raw);
      setQuery('');
      setOpen(false);
    }
  }

  return (
    <div className="autocomplete" ref={boxRef}>
      {value && !open ? (
        <div className="ac-chip" onClick={() => setOpen(true)} title={value}>
          <span className="ac-chip-label">{selectedLabel}</span>
          <code className="ac-chip-curie">{toCurie(value)}</code>
          <button
            type="button"
            className="ac-chip-clear"
            onClick={(e) => {
              e.stopPropagation();
              onChange('');
            }}
          >
            ×
          </button>
        </div>
      ) : (
        <>
          <input
            autoFocus={autoFocus}
            className="ac-input"
            value={query}
            placeholder={placeholder ?? 'Start typing to search terms…'}
            onChange={(e) => {
              setQuery(e.target.value);
              setOpen(true);
              setActive(0);
            }}
            onFocus={() => setOpen(true)}
            onBlur={() => setTimeout(() => setOpen(false), 150)}
            onKeyDown={(e) => {
              if (e.key === 'ArrowDown') {
                e.preventDefault();
                setActive((a) => Math.min(a + 1, matches.length - 1));
              } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                setActive((a) => Math.max(a - 1, 0));
              } else if (e.key === 'Enter') {
                e.preventDefault();
                if (matches[active]) choose(matches[active]);
                else commitRaw();
              } else if (e.key === 'Escape') {
                setOpen(false);
              }
            }}
          />
          {open && (
            <ul className="ac-list">
              {matches.map((t, i) => (
                <li
                  key={t.iri}
                  className={i === active ? 'ac-item active' : 'ac-item'}
                  onMouseDown={(e) => {
                    e.preventDefault();
                    choose(t);
                  }}
                >
                  <span className="ac-item-label">{t.label}</span>
                  <code className="ac-item-curie">{toCurie(t.iri)}</code>
                </li>
              ))}
              {query.trim() && (
                <li className="ac-item ac-raw" onMouseDown={(e) => { e.preventDefault(); commitRaw(); }}>
                  Use “{query.trim()}” as a custom IRI/CURIE
                </li>
              )}
              {matches.length === 0 && !query.trim() && (
                <li className="ac-item muted">Type to search the vocabulary…</li>
              )}
            </ul>
          )}
        </>
      )}
    </div>
  );
}
