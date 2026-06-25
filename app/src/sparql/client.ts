import { config } from '../config';
import type { Concept, Term, Triple, RdfValue } from '../rdf/model';
import {
  LIST_CONCEPTS,
  LIST_SCHEMES,
  LIST_PREDICATES,
  TERM_INDEX,
  describeConcept,
} from './queries';

interface Binding {
  [k: string]: { type: string; value: string; 'xml:lang'?: string; datatype?: string };
}

interface SparqlJson {
  results: { bindings: Binding[] };
}

async function select(query: string): Promise<Binding[]> {
  const res = await fetch(config.queryEndpoint, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      Accept: 'application/sparql-results+json',
    },
    body: new URLSearchParams({ query }),
  });
  if (!res.ok) {
    throw new Error(`SPARQL query failed (${res.status}): ${await res.text()}`);
  }
  const json = (await res.json()) as SparqlJson;
  return json.results.bindings;
}

/** Run a SPARQL UPDATE (INSERT/DELETE DATA). Throws on non-2xx. */
export async function update(sparql: string): Promise<void> {
  const res = await fetch(config.updateEndpoint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/sparql-update' },
    body: sparql,
  });
  if (!res.ok) {
    throw new Error(`SPARQL update failed (${res.status}): ${await res.text()}`);
  }
}

export interface ConceptListItem {
  iri: string;
  label: string;
  types: string[];
  schemes: string[];
}

export async function fetchConceptList(): Promise<ConceptListItem[]> {
  const rows = await select(LIST_CONCEPTS);
  const byIri = new Map<string, ConceptListItem>();
  for (const r of rows) {
    const iri = r.iri.value;
    let item = byIri.get(iri);
    if (!item) {
      item = { iri, label: r.label?.value ?? iri, types: [], schemes: [] };
      byIri.set(iri, item);
    }
    if (r.type && !item.types.includes(r.type.value)) item.types.push(r.type.value);
    if (r.scheme && !item.schemes.includes(r.scheme.value)) item.schemes.push(r.scheme.value);
  }
  return [...byIri.values()];
}

function literalValue(value: string, lang?: string, datatype?: string): RdfValue {
  return {
    kind: 'literal',
    value,
    lang: lang || undefined,
    datatype: datatype || undefined,
  };
}

export async function fetchConcept(iri: string): Promise<Concept> {
  const rows = await select(describeConcept(iri));
  // Group rows by (predicate, object) so blank nodes accumulate their children.
  const order: string[] = [];
  const byKey = new Map<string, Triple>();
  for (const r of rows) {
    const oKind = r.oKind.value;
    const key = `${r.p.value}|${oKind}|${r.o.value}`;
    let triple = byKey.get(key);
    if (!triple) {
      const object: RdfValue =
        oKind === 'iri'
          ? { kind: 'iri', value: r.o.value }
          : oKind === 'bnode'
            ? { kind: 'bnode', value: '', properties: [] }
            : literalValue(r.o.value, r.lang?.value, r.dt?.value);
      triple = { subject: iri, predicate: r.p.value, object };
      byKey.set(key, triple);
      order.push(key);
    }
    // Attach a blank-node child property if present on this row.
    if (oKind === 'bnode' && r.bp && r.bo) {
      const child: RdfValue =
        r.boKind.value === 'iri'
          ? { kind: 'iri', value: r.bo.value }
          : r.boKind.value === 'bnode'
            ? { kind: 'bnode', value: '', properties: [] }
            : literalValue(r.bo.value, r.bLang?.value, r.bDt?.value);
      triple.object.properties!.push({ predicate: r.bp.value, object: child });
    }
  }
  const triples: Triple[] = order.map((k) => byKey.get(k)!);
  const types = triples
    .filter((t) => t.predicate === 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type')
    .map((t) => t.object.value);
  const schemes = triples
    .filter((t) => t.predicate === 'http://www.w3.org/2004/02/skos/core#inScheme')
    .map((t) => t.object.value);
  const labelTriple =
    triples.find((t) => t.predicate === 'http://www.w3.org/2004/02/skos/core#prefLabel') ??
    triples.find((t) => t.predicate === 'http://www.w3.org/2000/01/rdf-schema#label');
  return {
    iri,
    label: labelTriple?.object.value ?? iri,
    types,
    schemes,
    triples,
  };
}

export interface SchemeItem {
  iri: string;
  label: string;
}

export async function fetchSchemes(): Promise<SchemeItem[]> {
  const rows = await select(LIST_SCHEMES);
  return rows.map((r) => ({ iri: r.iri.value, label: r.label?.value ?? r.iri.value }));
}

export async function fetchTermIndex(): Promise<Term[]> {
  const rows = await select(TERM_INDEX);
  const imported = config.importedNamespaces;
  const byIri = new Map<string, Term>();
  for (const r of rows) {
    const iri = r.iri.value;
    let t = byIri.get(iri);
    if (!t) {
      // Classify by namespace: imported vocabularies vs this database.
      const source = imported.some((ns) => iri.startsWith(ns)) ? 'imported' : 'db';
      t = { iri, label: r.label?.value ?? iri, source, types: [] };
      byIri.set(iri, t);
    }
    if (r.type && !t.types.includes(r.type.value)) t.types.push(r.type.value);
  }
  return [...byIri.values()];
}

/** Distinct predicate IRIs actually used in the database (for the field picker). */
export async function fetchPredicates(): Promise<string[]> {
  const rows = await select(LIST_PREDICATES);
  return rows.map((r) => r.p.value);
}
