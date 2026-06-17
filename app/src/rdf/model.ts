// Core RDF data model used throughout the app. We keep a deliberately small,
// flat representation of a triple so the UI code stays readable for editors who
// do not think in RDF.

export interface RdfValue {
  /**
   * 'iri'     — resource reference
   * 'literal' — text/number value
   * 'bnode'   — an anonymous node, inlined as a set of nested properties so it
   *             never surfaces as a raw blank-node id in the UI or export.
   */
  kind: 'iri' | 'literal' | 'bnode';
  /** Full IRI, or the literal lexical value. Empty for blank nodes. */
  value: string;
  /** Literal language tag, e.g. 'en'. */
  lang?: string;
  /** Literal datatype IRI, e.g. xsd:decimal. */
  datatype?: string;
  /** Nested predicate/object pairs when kind === 'bnode'. */
  properties?: BNodeProp[];
}

export interface BNodeProp {
  predicate: string;
  object: RdfValue;
}

export interface Triple {
  subject: string; // always an IRI in this app
  predicate: string; // IRI
  object: RdfValue;
}

/** A concept as loaded from the store: its IRI plus every triple about it. */
export interface Concept {
  iri: string;
  /** Convenience label resolved from prefLabel/rdfs:label. */
  label: string;
  /** rdf:type IRIs. */
  types: string[];
  /** skos:inScheme IRIs. */
  schemes: string[];
  triples: Triple[];
}

/** Canonical string for an RDF value (blank nodes hashed from their content). */
export function valueKey(v: RdfValue): string {
  if (v.kind === 'iri') return `<${v.value}>`;
  if (v.kind === 'bnode') {
    const inner = (v.properties ?? [])
      .map((p) => `<${p.predicate}> ${valueKey(p.object)}`)
      .sort()
      .join(' ; ');
    return `[ ${inner} ]`;
  }
  return `"${v.value}"${v.lang ? '@' + v.lang : ''}${
    v.datatype ? '^^<' + v.datatype + '>' : ''
  }`;
}

/** Stable identity of a triple, used for diffing pending edits. */
export function tripleKey(t: Triple): string {
  return `<${t.subject}> <${t.predicate}> ${valueKey(t.object)}`;
}

export function sameValue(a: RdfValue, b: RdfValue): boolean {
  return valueKey(a) === valueKey(b);
}

/** A term that can be suggested as an object value in autocomplete. */
export interface Term {
  iri: string;
  label: string;
  /** Where it came from: scheme IRI, vocabulary prefix, or 'external'. */
  source: string;
  types: string[];
}
