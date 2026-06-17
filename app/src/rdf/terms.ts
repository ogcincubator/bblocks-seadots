// Vocabulary knowledge baked into the UI so non-RDF experts never have to type
// raw IRIs. Prefixes, the predicate palette, and value-type hints all live here.

export interface Prefix {
  prefix: string;
  iri: string;
}

// Namespaces used across the SeaDOTs graph and its imported vocabularies.
export const PREFIXES: Prefix[] = [
  { prefix: 'rdf', iri: 'http://www.w3.org/1999/02/22-rdf-syntax-ns#' },
  { prefix: 'rdfs', iri: 'http://www.w3.org/2000/01/rdf-schema#' },
  { prefix: 'owl', iri: 'http://www.w3.org/2002/07/owl#' },
  { prefix: 'skos', iri: 'http://www.w3.org/2004/02/skos/core#' },
  { prefix: 'sosa', iri: 'http://www.w3.org/ns/sosa/' },
  { prefix: 'ssn', iri: 'http://www.w3.org/ns/ssn/' },
  { prefix: 'prov', iri: 'http://www.w3.org/ns/prov#' },
  { prefix: 'dcterms', iri: 'http://purl.org/dc/terms/' },
  { prefix: 'dcat', iri: 'http://www.w3.org/ns/dcat#' },
  { prefix: 'qudt', iri: 'http://qudt.org/schema/qudt/' },
  { prefix: 'quantitykind', iri: 'http://qudt.org/vocab/quantitykind/' },
  { prefix: 'dwc', iri: 'http://rs.tdwg.org/dwc/terms/' },
  { prefix: 'xsd', iri: 'http://www.w3.org/2001/XMLSchema#' },
  { prefix: 'ind', iri: 'https://w3id.org/indicators/marine/' },
  { prefix: 'indo', iri: 'https://w3id.org/indicators/marine/obs/' },
  { prefix: 'indp', iri: 'https://w3id.org/indicators/marine/parameters/' },
  { prefix: 'indr', iri: 'https://w3id.org/indicators/marine/relationships/' },
  { prefix: 'im', iri: 'https://w3id.org/indicators/marine/indicator-model/' },
  { prefix: 'dapsim', iri: 'https://w3id.org/indicators/marine/dapsim/' },
  { prefix: 'prop-rel', iri: 'https://w3id.org/ogc/hosted/seadots/prop-rel/' },
  { prefix: 'sdn', iri: 'https://vocab.nerc.ac.uk/collection/SDN/current/' },
  { prefix: 'agrovoc', iri: 'http://aims.fao.org/aos/agrovoc/' },
];

/** Whether a property's value is normally a literal (text) or an IRI object. */
export type ValueKind = 'literal' | 'iri' | 'either';

export interface PredicateDef {
  iri: string;
  label: string;
  /** Short human hint shown under the field. */
  hint: string;
  valueKind: ValueKind;
  /** Suggested datatype/lang behaviour for literals. */
  langText?: boolean;
}

// The palette of predicates a user can add to a concept. Curated from the
// patterns actually used in indicators.ttl plus common SKOS annotation props.
export const PREDICATES: PredicateDef[] = [
  { iri: 'http://www.w3.org/2004/02/skos/core#prefLabel', label: 'Preferred label', hint: 'Main human-readable name', valueKind: 'literal', langText: true },
  { iri: 'http://www.w3.org/2004/02/skos/core#altLabel', label: 'Alternative label', hint: 'Synonym or alternate name', valueKind: 'literal', langText: true },
  { iri: 'http://www.w3.org/2000/01/rdf-schema#label', label: 'Label (rdfs)', hint: 'Generic label', valueKind: 'literal', langText: true },
  { iri: 'http://www.w3.org/2004/02/skos/core#definition', label: 'Definition', hint: 'What this concept means', valueKind: 'literal', langText: true },
  { iri: 'http://www.w3.org/2000/01/rdf-schema#comment', label: 'Comment', hint: 'Free-text note', valueKind: 'literal', langText: true },
  { iri: 'http://www.w3.org/2004/02/skos/core#scopeNote', label: 'Scope note', hint: 'Usage / provenance note', valueKind: 'literal', langText: true },
  { iri: 'http://www.w3.org/2004/02/skos/core#inScheme', label: 'In concept scheme', hint: 'Which vocabulary it belongs to', valueKind: 'iri' },
  { iri: 'http://www.w3.org/2004/02/skos/core#broader', label: 'Broader concept', hint: 'More general parent concept', valueKind: 'either' },
  { iri: 'http://www.w3.org/2004/02/skos/core#narrower', label: 'Narrower concept', hint: 'More specific child concept', valueKind: 'iri' },
  { iri: 'http://www.w3.org/2004/02/skos/core#related', label: 'Related concept', hint: 'Associatively linked concept', valueKind: 'either' },
  { iri: 'http://www.w3.org/2002/07/owl#sameAs', label: 'Same as (owl)', hint: 'Equivalent external IRI', valueKind: 'iri' },
  { iri: 'http://www.w3.org/2000/01/rdf-schema#seeAlso', label: 'See also', hint: 'Related external resource', valueKind: 'iri' },
  { iri: 'http://qudt.org/schema/qudt/hasQuantityKind', label: 'Quantity kind', hint: 'Physical quantity (mass, area…)', valueKind: 'iri' },
  { iri: 'http://www.w3.org/ns/prov#wasAttributedTo', label: 'Attributed to', hint: 'Agent/source responsible', valueKind: 'iri' },
  { iri: 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type', label: 'Type (rdf:type)', hint: 'Class membership', valueKind: 'iri' },
];

const sortedPrefixes = [...PREFIXES].sort((a, b) => b.iri.length - a.iri.length);

/** Compress a full IRI to a CURIE when a known prefix matches, else return it. */
export function toCurie(iri: string): string {
  for (const p of sortedPrefixes) {
    if (iri.startsWith(p.iri)) {
      const local = iri.slice(p.iri.length);
      if (local && !local.includes('/') && !local.includes('#')) {
        return `${p.prefix}:${local}`;
      }
    }
  }
  return iri;
}

/** Expand a CURIE (prefix:local) to a full IRI; pass through full IRIs. */
export function expandCurie(value: string): string {
  const m = /^([A-Za-z][\w-]*):(.+)$/.exec(value);
  if (m && !/^https?:/.test(value)) {
    const pre = PREFIXES.find((p) => p.prefix === m[1]);
    if (pre) return pre.iri + m[2];
  }
  return value;
}

export function looksLikeIri(value: string): boolean {
  return /^https?:\/\//.test(value) || /^[A-Za-z][\w-]*:[^\s/]+/.test(value);
}

export function predicateLabel(iri: string): string {
  return PREDICATES.find((p) => p.iri === iri)?.label ?? toCurie(iri);
}

/** Turtle serialization of the prefix header. */
export function prefixHeader(): string {
  return PREFIXES.map((p) => `@prefix ${p.prefix}: <${p.iri}> .`).join('\n');
}
