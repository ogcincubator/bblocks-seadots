import type { RdfValue } from '../rdf/model';
import type { ValueKind } from '../rdf/terms';
import { looksLikeIri, toCurie } from '../rdf/terms';
import { termToString } from '../rdf/serialize';
import TermAutocomplete from './TermAutocomplete';

interface Props {
  value: RdfValue;
  /** Predicate's preferred value kind, controls which inputs are offered. */
  kind: ValueKind;
  /** Limit object suggestions to these rdf:type IRIs (optional). */
  typeFilter?: string[];
  onChange: (v: RdfValue) => void;
  autoFocus?: boolean;
}

/**
 * Lets a non-RDF user provide either:
 *  - a free-text literal (with optional language tag), or
 *  - an object reference chosen from the vocabulary via typeahead.
 * Which modes are shown depends on the predicate's declared value kind.
 */
export default function ValueEditor({ value, kind, typeFilter, onChange, autoFocus }: Props) {
  const allowLiteral = kind === 'literal' || kind === 'either';
  const allowIri = kind === 'iri' || kind === 'either';
  const isIri = value.kind === 'iri';

  return (
    <div className="value-editor">
      {kind === 'either' && (
        <div className="value-toggle">
          <button
            type="button"
            className={!isIri ? 'seg active' : 'seg'}
            onClick={() => onChange({ kind: 'literal', value: isIri ? '' : value.value, lang: 'en' })}
          >
            Text
          </button>
          <button
            type="button"
            className={isIri ? 'seg active' : 'seg'}
            onClick={() => onChange({ kind: 'iri', value: isIri ? value.value : '' })}
          >
            Vocabulary term
          </button>
        </div>
      )}

      {isIri && allowIri ? (
        <TermAutocomplete
          value={value.value}
          typeFilter={typeFilter}
          autoFocus={autoFocus}
          onChange={(iri) => onChange({ kind: 'iri', value: iri })}
        />
      ) : allowLiteral ? (
        <div className="literal-row">
          <textarea
            className="literal-input"
            autoFocus={autoFocus}
            rows={1}
            value={value.value}
            placeholder="Enter text…"
            onChange={(e) => {
              const v = e.target.value;
              // Convenience: if the user pastes an IRI into an 'either' text box,
              // offer to treat it as a term by flipping kind automatically.
              if (kind === 'either' && looksLikeIri(v)) {
                onChange({ kind: 'iri', value: v });
              } else {
                onChange({ ...value, kind: 'literal', value: v });
              }
            }}
          />
          <input
            className="lang-input"
            value={value.lang ?? ''}
            placeholder="lang"
            title="Language tag, e.g. en"
            onChange={(e) => onChange({ ...value, kind: 'literal', lang: e.target.value || undefined })}
          />
        </div>
      ) : (
        // Predicate wants an IRI but value is currently literal — show picker.
        <TermAutocomplete
          value={value.kind === 'iri' ? value.value : ''}
          typeFilter={typeFilter}
          autoFocus={autoFocus}
          onChange={(iri) => onChange({ kind: 'iri', value: iri })}
        />
      )}
    </div>
  );
}
