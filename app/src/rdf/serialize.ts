import type { Triple, RdfValue } from './model';
import { config } from '../config';
import { prefixHeader, toCurie } from './terms';

function escapeLiteral(s: string): string {
  return s.replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/\n/g, '\\n');
}

/** Render an object value as a Turtle/SPARQL term. */
export function termToString(v: RdfValue): string {
  if (v.kind === 'iri') {
    const curie = toCurie(v.value);
    return curie === v.value ? `<${v.value}>` : curie;
  }
  const lit = `"${escapeLiteral(v.value)}"`;
  if (v.lang) return `${lit}@${v.lang}`;
  if (v.datatype) return `${lit}^^${toCurie(v.datatype) === v.datatype ? `<${v.datatype}>` : toCurie(v.datatype)}`;
  return lit;
}

function tripleLine(t: Triple): string {
  const s = `<${t.subject}>`;
  const p = toCurie(t.predicate) === t.predicate ? `<${t.predicate}>` : toCurie(t.predicate);
  return `${s} ${p} ${termToString(t.object)} .`;
}

/** Serialize triples to a standalone Turtle document with prefixes. */
export function toTurtle(triples: Triple[]): string {
  const body = triples.map(tripleLine).join('\n');
  return `${prefixHeader()}\n\n${body}\n`;
}

/**
 * Build a single SPARQL UPDATE that applies the pending edits to the named
 * graph: removed triples in DELETE DATA, added triples in INSERT DATA.
 */
export function toSparqlUpdate(added: Triple[], removed: Triple[]): string {
  const g = `<${config.graph}>`;
  const blocks: string[] = [prefixHeader()];
  if (removed.length) {
    blocks.push(`DELETE DATA {\n  GRAPH ${g} {\n${removed.map((t) => '    ' + tripleLine(t)).join('\n')}\n  }\n} ;`);
  }
  if (added.length) {
    blocks.push(`INSERT DATA {\n  GRAPH ${g} {\n${added.map((t) => '    ' + tripleLine(t)).join('\n')}\n  }\n}`);
  }
  return blocks.join('\n\n') + '\n';
}
