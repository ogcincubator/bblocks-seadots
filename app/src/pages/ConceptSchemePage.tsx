import { useEffect, useMemo, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { useStore } from '../store/useStore';
import type { Triple } from '../rdf/model';
import {
  PREFIXES,
  SKOS_PREF_LABEL,
  RDFS_LABEL,
  RDF_TYPE,
  SKOS_CONCEPT,
  SKOS_IN_SCHEME,
  SKOS_BROADER,
  SKOS_NARROWER,
  SKOS_DEFINITION,
  MERGED_LABEL_EXPANDS_TO,
  CONCEPT_SCHEME,
  toCurie,
  typeName,
} from '../rdf/terms';
import TermAutocomplete from '../components/TermAutocomplete';

interface Row {
  iri: string;
  label: string;
  labelLang?: string;
  definition: string;
  definitionLang?: string;
  schemeIris: string[];
  typeIris: string[];
  broaderIris: string[];
  narrowerIris: string[];
}

function buildRow(iri: string, triples: Triple[]): Row {
  const pref = triples.find((t) => t.predicate === SKOS_PREF_LABEL && t.object.kind === 'literal');
  const rdfsLbl = triples.find((t) => t.predicate === RDFS_LABEL && t.object.kind === 'literal');
  const labelT = pref ?? rdfsLbl;
  const defT = triples.find((t) => t.predicate === SKOS_DEFINITION && t.object.kind === 'literal');
  const iriValues = (pred: string) =>
    triples.filter((t) => t.predicate === pred && t.object.kind === 'iri').map((t) => t.object.value);
  return {
    iri,
    label: labelT?.object.value ?? '',
    labelLang: labelT?.object.lang,
    definition: defT?.object.value ?? '',
    definitionLang: defT?.object.lang,
    schemeIris: iriValues(SKOS_IN_SCHEME),
    typeIris: iriValues(RDF_TYPE).filter((t) => t !== SKOS_CONCEPT),
    broaderIris: iriValues(SKOS_BROADER),
    narrowerIris: iriValues(SKOS_NARROWER),
  };
}

/** A chip list with an inline typeahead to add one more value. */
function TagCell({
  iris,
  onAdd,
  onRemove,
  typeFilter,
  sourceFilter,
  exclude,
  placeholder,
}: {
  iris: string[];
  onAdd: (iri: string) => void;
  onRemove: (iri: string) => void;
  typeFilter?: string[];
  sourceFilter?: 'db' | 'imported';
  exclude?: string;
  placeholder?: string;
}) {
  const [adding, setAdding] = useState(false);
  return (
    <div className="tag-cell">
      {iris.map((iri) => (
        <span className="chip-tag" key={iri} title={iri}>
          <Link to={`/concept/${encodeURIComponent(iri)}`}>{typeName(iri)}</Link>
          <button type="button" onClick={() => onRemove(iri)} title="Remove">
            ×
          </button>
        </span>
      ))}
      {adding ? (
        <TermAutocomplete
          value=""
          typeFilter={typeFilter}
          sourceFilter={sourceFilter}
          exclude={exclude}
          autoFocus
          placeholder={placeholder}
          onChange={(iri) => {
            if (iri) onAdd(iri);
            setAdding(false);
          }}
        />
      ) : (
        <button type="button" className="chip-add" onClick={() => setAdding(true)}>
          +
        </button>
      )}
    </div>
  );
}

export default function ConceptSchemePage() {
  const { iri: rawIri } = useParams();
  const schemeIri = rawIri ? decodeURIComponent(rawIri) : '';

  const conceptList = useStore((s) => s.conceptList);
  const schemes = useStore((s) => s.schemes);
  const added = useStore((s) => s.added);
  const removed = useStore((s) => s.removed);
  // Subscribed so the grid recomputes once async concept loads land in the cache.
  const conceptCache = useStore((s) => s.conceptCache);
  const loadConcept = useStore((s) => s.loadConcept);
  const effectiveTriples = useStore((s) => s.effectiveTriples);
  const addTriple = useStore((s) => s.addTriple);
  const removeTriple = useStore((s) => s.removeTriple);

  const schemeLabel = schemes.find((s) => s.iri === schemeIri)?.label ?? toCurie(schemeIri);

  // Members = concepts already known to be in this scheme, plus any concept the
  // user has just added to it locally (not yet published).
  const candidateIris = useMemo(() => {
    const set = new Set<string>();
    for (const c of conceptList) if (c.schemes.includes(schemeIri)) set.add(c.iri);
    for (const t of added) {
      if (t.predicate === SKOS_IN_SCHEME && t.object.kind === 'iri' && t.object.value === schemeIri) {
        set.add(t.subject);
      }
    }
    return [...set];
  }, [conceptList, added, schemeIri]);

  useEffect(() => {
    candidateIris.forEach((iri) => void loadConcept(iri));
  }, [candidateIris, loadConcept]);

  const rows = useMemo(() => {
    return candidateIris
      .map((iri) => buildRow(iri, effectiveTriples(iri)))
      // Drop rows whose inScheme link to this scheme has since been removed.
      .filter((r) => r.schemeIris.includes(schemeIri))
      .sort((a, b) => a.label.localeCompare(b.label) || a.iri.localeCompare(b.iri));
    // conceptCache/added/removed aren't read directly here, but effectiveTriples()
    // closes over them — its own reference never changes, so they must be listed
    // explicitly to force a recompute once concept loads/edits land.
  }, [candidateIris, effectiveTriples, schemeIri, conceptCache, added, removed]);

  const stillLoading = rows.length < candidateIris.length;

  function setLabel(iri: string, triples: Triple[], value: string) {
    const olds = triples.filter((t) => t.predicate === SKOS_PREF_LABEL || t.predicate === RDFS_LABEL);
    olds.forEach(removeTriple);
    if (value.trim()) {
      const lang = olds.find((t) => t.object.lang)?.object.lang ?? 'en';
      for (const p of MERGED_LABEL_EXPANDS_TO) {
        addTriple({ subject: iri, predicate: p, object: { kind: 'literal', value, lang } });
      }
    }
  }

  function setDefinition(iri: string, triples: Triple[], value: string) {
    const old = triples.find((t) => t.predicate === SKOS_DEFINITION);
    if (old) removeTriple(old);
    if (value.trim()) {
      addTriple({
        subject: iri,
        predicate: SKOS_DEFINITION,
        object: { kind: 'literal', value, lang: old?.object.lang ?? 'en' },
      });
    }
  }

  function addIriValue(iri: string, predicate: string, object: string) {
    addTriple({ subject: iri, predicate, object: { kind: 'iri', value: object } });
  }

  function removeIriValue(triples: Triple[], predicate: string, object: string) {
    const t = triples.find(
      (x) => x.predicate === predicate && x.object.kind === 'iri' && x.object.value === object,
    );
    if (t) removeTriple(t);
  }

  // --- Add-concept-to-scheme form ------------------------------------------
  const [addingRow, setAddingRow] = useState(false);
  const [newPrefix, setNewPrefix] = useState('indo');
  const [newLocal, setNewLocal] = useState('');

  function submitNewConcept() {
    const base = PREFIXES.find((p) => p.prefix === newPrefix)?.iri ?? '';
    const local = newLocal.trim();
    if (!local) return;
    const iri = base + local;
    addTriple({ subject: iri, predicate: RDF_TYPE, object: { kind: 'iri', value: SKOS_CONCEPT } });
    addTriple({ subject: iri, predicate: SKOS_IN_SCHEME, object: { kind: 'iri', value: schemeIri } });
    setNewLocal('');
  }

  return (
    <div className="concept-scheme">
      <div className="editor-head">
        <h1>{schemeLabel}</h1>
        <code className="iri-preview big">{toCurie(schemeIri)}</code>
        <Link className="link-btn" to={`/concept/${encodeURIComponent(schemeIri)}`}>
          edit scheme metadata ↗
        </Link>
      </div>

      {stillLoading && <p className="muted">Loading members…</p>}

      <div className="scheme-table-wrap">
        <table className="scheme-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Label</th>
              <th>Description</th>
              <th>Concept scheme</th>
              <th>Types (non-SKOS)</th>
              <th>Broader</th>
              <th>Narrower</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {rows.map((r) => {
              const triples = effectiveTriples(r.iri);
              return (
                <tr key={r.iri}>
                  <td className="id-cell">
                    <Link to={`/concept/${encodeURIComponent(r.iri)}`} title={r.iri}>
                      {toCurie(r.iri)}
                    </Link>
                  </td>
                  <td>
                    <input
                      className="cell-input"
                      value={r.label}
                      placeholder="Label…"
                      onChange={(e) => setLabel(r.iri, triples, e.target.value)}
                    />
                  </td>
                  <td>
                    <textarea
                      className="cell-input"
                      rows={1}
                      value={r.definition}
                      placeholder="Definition…"
                      onChange={(e) => setDefinition(r.iri, triples, e.target.value)}
                    />
                  </td>
                  <td>
                    <TagCell
                      iris={r.schemeIris}
                      typeFilter={[CONCEPT_SCHEME]}
                      sourceFilter="db"
                      onAdd={(iri) => addIriValue(r.iri, SKOS_IN_SCHEME, iri)}
                      onRemove={(iri) => removeIriValue(triples, SKOS_IN_SCHEME, iri)}
                    />
                  </td>
                  <td>
                    <TagCell
                      iris={r.typeIris}
                      onAdd={(iri) => addIriValue(r.iri, RDF_TYPE, iri)}
                      onRemove={(iri) => removeIriValue(triples, RDF_TYPE, iri)}
                      placeholder="type CURIE/IRI…"
                    />
                  </td>
                  <td>
                    <TagCell
                      iris={r.broaderIris}
                      typeFilter={[SKOS_CONCEPT]}
                      sourceFilter="db"
                      exclude={r.iri}
                      onAdd={(iri) => addIriValue(r.iri, SKOS_BROADER, iri)}
                      onRemove={(iri) => removeIriValue(triples, SKOS_BROADER, iri)}
                    />
                  </td>
                  <td>
                    <TagCell
                      iris={r.narrowerIris}
                      typeFilter={[SKOS_CONCEPT]}
                      sourceFilter="db"
                      exclude={r.iri}
                      onAdd={(iri) => addIriValue(r.iri, SKOS_NARROWER, iri)}
                      onRemove={(iri) => removeIriValue(triples, SKOS_NARROWER, iri)}
                    />
                  </td>
                  <td>
                    <button
                      type="button"
                      className="icon-btn"
                      title="Remove from this scheme"
                      onClick={() => removeIriValue(triples, SKOS_IN_SCHEME, schemeIri)}
                    >
                      🗑
                    </button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      <div className="add-field">
        {addingRow ? (
          <div className="add-field-pick">
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
              onKeyDown={(e) => {
                if (e.key === 'Enter') submitNewConcept();
              }}
            />
            <button type="button" className="secondary" onClick={submitNewConcept}>
              Add
            </button>
            <button type="button" className="link-btn" onClick={() => setAddingRow(false)}>
              done
            </button>
          </div>
        ) : (
          <button type="button" className="secondary" onClick={() => setAddingRow(true)}>
            + Add concept to this scheme
          </button>
        )}
      </div>
    </div>
  );
}
