import type { Triple, RdfValue } from './model';
import { config } from '../config';
import { prefixHeader, toCurie } from './terms';

// --- term rendering ----------------------------------------------------------

function escapeLiteral(s: string): string {
  return s.replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/\n/g, '\\n');
}

function pterm(iri: string): string {
  const c = toCurie(iri);
  return c === iri ? `<${iri}>` : c;
}

/** Render an object value as a Turtle term (iri, literal, or inline bnode). */
export function termToString(v: RdfValue): string {
  if (v.kind === 'iri') return pterm(v.value);
  if (v.kind === 'bnode') {
    const inner = (v.properties ?? [])
      .map((p) => `${pterm(p.predicate)} ${termToString(p.object)}`)
      .join(' ; ');
    return inner ? `[ ${inner} ]` : '[]';
  }
  const lit = `"${escapeLiteral(v.value)}"`;
  if (v.lang) return `${lit}@${v.lang}`;
  if (v.datatype) return `${lit}^^${pterm(v.datatype)}`;
  return lit;
}

// --- ordering ----------------------------------------------------------------

const RDF = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#';
const RDFS = 'http://www.w3.org/2000/01/rdf-schema#';
const SKOS = 'http://www.w3.org/2004/02/skos/core#';
const DCT = 'http://purl.org/dc/terms/';
const DCAT = 'http://www.w3.org/ns/dcat#';
const OWL = 'http://www.w3.org/2002/07/owl#';
const PROV = 'http://www.w3.org/ns/prov#';
const QUDT = 'http://qudt.org/schema/qudt/';
const PROPREL = 'https://w3id.org/ogc/hosted/seadots/prop-rel/';

// Predicate display order following the serialisation convention:
// type → label → description → internal taxonomy rels → external vocab rels →
// structural SKOS hierarchy. Unknown predicates fall in the middle (rank 50).
const PRED_RANK: Record<string, number> = {
  [`${RDF}type`]: 0,
  [`${SKOS}prefLabel`]: 10,
  [`${RDFS}label`]: 11,
  [`${SKOS}altLabel`]: 12,
  [`${SKOS}definition`]: 20,
  [`${DCT}description`]: 21,
  [`${RDFS}comment`]: 22,
  [`${SKOS}scopeNote`]: 23,
  [`${SKOS}broader`]: 30,
  [`${SKOS}narrower`]: 31,
  [`${SKOS}related`]: 32,
  [`${QUDT}hasQuantityKind`]: 33,
  [`${PROPREL}fromProperty`]: 34,
  [`${PROPREL}toProperty`]: 35,
  [`${PROPREL}hasWeight`]: 36,
  [`${OWL}sameAs`]: 60,
  [`${SKOS}exactMatch`]: 61,
  [`${SKOS}closeMatch`]: 62,
  [`${RDFS}seeAlso`]: 63,
  [`${PROV}wasAttributedTo`]: 64,
  [`${SKOS}inScheme`]: 80,
  [`${SKOS}topConceptOf`]: 81,
  [`${SKOS}hasTopConcept`]: 82,
  [`${DCT}isPartOf`]: 83,
  [`${DCT}hasPart`]: 84,
  [`${DCAT}dataset`]: 85,
};

function predRank(p: string): number {
  return PRED_RANK[p] ?? 50;
}

// Subjects that head the document: catalogs/datasets and concept schemes.
const TOP_TYPES = new Set([
  `${DCAT}Catalog`,
  `${DCAT}Dataset`,
  `${SKOS}ConceptScheme`,
]);

function subjectRank(types: string[]): number {
  return types.some((t) => TOP_TYPES.has(t)) ? 0 : 1;
}

// --- grouping ----------------------------------------------------------------

interface SubjectBlock {
  subject: string;
  types: string[];
  /** predicate -> ordered object terms */
  preds: Map<string, RdfValue[]>;
}

function groupBySubject(triples: Triple[]): SubjectBlock[] {
  const map = new Map<string, SubjectBlock>();
  for (const t of triples) {
    let b = map.get(t.subject);
    if (!b) {
      b = { subject: t.subject, types: [], preds: new Map() };
      map.set(t.subject, b);
    }
    const arr = b.preds.get(t.predicate) ?? [];
    arr.push(t.object);
    b.preds.set(t.predicate, arr);
    if (t.predicate === `${RDF}type` && t.object.kind === 'iri') {
      b.types.push(t.object.value);
    }
  }
  const blocks = [...map.values()];
  blocks.sort((a, b) => {
    const r = subjectRank(a.types) - subjectRank(b.types);
    if (r !== 0) return r;
    // Group concepts by prefix (CURIE), then by full IRI, alphanumerically.
    return toCurie(a.subject).localeCompare(toCurie(b.subject));
  });
  return blocks;
}

/** Render one subject as an indented Turtle block. */
function blockToTurtle(b: SubjectBlock): string {
  const preds = [...b.preds.entries()].sort((x, y) => predRank(x[0]) - predRank(y[0]));
  const lines = preds.map(([p, objs]) => {
    const rendered = objs.map(termToString).join(', ');
    // Turtle shorthand for rdf:type.
    const pred = p === `${RDF}type` ? 'a' : pterm(p);
    return `    ${pred} ${rendered}`;
  });
  return `${pterm(b.subject)}\n${lines.join(' ;\n')} .`;
}

/** Serialize triples to a standalone, human-readable Turtle document. */
export function toTurtle(triples: Triple[]): string {
  const blocks = groupBySubject(triples).map(blockToTurtle).join('\n\n');
  return `${prefixHeader()}\n\n${blocks}\n`;
}

// --- SPARQL UPDATE -----------------------------------------------------------

function hasBnode(t: Triple): boolean {
  return t.object.kind === 'bnode';
}

/** Wrap a body in `GRAPH <g> { … }` only when a named graph is configured. */
function wrapGraph(body: string): string {
  return config.graph
    ? `  GRAPH <${config.graph}> {\n${body}\n  }`
    : body;
}

function dataBlock(verb: string, triples: Triple[]): string {
  const indent = config.graph ? '    ' : '  ';
  const body = groupBySubject(triples)
    .map((b) => blockToTurtle(b).split('\n').map((l) => indent + l).join('\n'))
    .join('\n');
  return `${verb} {\n${wrapGraph(body)}\n}`;
}

/**
 * Build a SPARQL UPDATE applying the pending edits to the configured graph
 * (default graph when none is set). Blank nodes are illegal in DELETE DATA, so
 * bnode removals use DELETE WHERE.
 */
export function toSparqlUpdate(added: Triple[], removed: Triple[]): string {
  const parts: string[] = [prefixHeader()];

  const removedData = removed.filter((t) => !hasBnode(t));
  const removedBnode = removed.filter(hasBnode);

  if (removedData.length) parts.push(dataBlock('DELETE DATA', removedData) + ' ;');
  for (const t of removedBnode) {
    // Delete any blank node hanging off this subject/predicate.
    parts.push(
      `DELETE WHERE {\n${wrapGraph(
        `    ${pterm(t.subject)} ${pterm(t.predicate)} ?b . ?b ?bp ?bo`,
      )}\n} ;`,
    );
  }
  if (added.length) parts.push(dataBlock('INSERT DATA', added));

  // Drop a trailing ' ;' if there were no INSERTs.
  let out = parts.join('\n\n');
  out = out.replace(/ ;\s*$/, '');
  return out + '\n';
}
