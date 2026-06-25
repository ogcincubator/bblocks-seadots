import { config } from '../config';

/**
 * Wrap a pattern in `GRAPH <g> { … }` when a named graph is configured.
 * Some stores (e.g. the Prez backend) keep everything in the default graph, in
 * which case `config.graph` is empty and we query without a GRAPH block.
 */
function g(body: string): string {
  return config.graph ? `GRAPH <${config.graph}> {\n${body}\n}` : body;
}

/** All concepts with a resolved label, their types and schemes. */
export const LIST_CONCEPTS = `
SELECT ?iri ?label ?type ?scheme WHERE {
${g(`    ?iri a ?type .
    VALUES ?conceptType {
      <http://www.w3.org/2004/02/skos/core#Concept>
      <http://www.w3.org/ns/sosa/ObservableProperty>
      <http://www.w3.org/ns/ssn/Property>
    }
    ?iri a ?conceptType .
    OPTIONAL { ?iri <http://www.w3.org/2004/02/skos/core#prefLabel> ?pl }
    OPTIONAL { ?iri <http://www.w3.org/2000/01/rdf-schema#label> ?rl }
    BIND(COALESCE(?pl, ?rl, STR(?iri)) AS ?label)
    OPTIONAL { ?iri <http://www.w3.org/2004/02/skos/core#inScheme> ?scheme }`)}
}
ORDER BY ?label`;

/**
 * Every triple about one concept, plus one level of blank-node children so we
 * can inline anonymous nodes (e.g. `hasWeight [ qudt:numericValue 0.5 ]`).
 * ?bp/?bo are bound only when ?o is itself a blank node.
 */
export function describeConcept(iri: string): string {
  return `
SELECT ?p ?o ?oKind ?lang ?dt ?bp ?bo ?boKind ?bLang ?bDt WHERE {
${g(`    <${iri}> ?p ?o .
    BIND(IF(isIRI(?o), "iri", IF(isBlank(?o), "bnode", "literal")) AS ?oKind)
    BIND(LANG(?o) AS ?lang)
    BIND(DATATYPE(?o) AS ?dt)
    OPTIONAL {
      FILTER(isBlank(?o))
      ?o ?bp ?bo .
      BIND(IF(isIRI(?bo), "iri", IF(isBlank(?bo), "bnode", "literal")) AS ?boKind)
      BIND(LANG(?bo) AS ?bLang)
      BIND(DATATYPE(?bo) AS ?bDt)
    }`)}
}`;
}

/** Concept schemes available for the inScheme picker / browse. */
export const LIST_SCHEMES = `
SELECT ?iri ?label WHERE {
${g(`    ?iri a <http://www.w3.org/2004/02/skos/core#ConceptScheme> .
    OPTIONAL { ?iri <http://www.w3.org/2004/02/skos/core#prefLabel> ?pl }
    OPTIONAL { ?iri <http://www.w3.org/2000/01/rdf-schema#label> ?rl }
    BIND(COALESCE(?pl, ?rl, STR(?iri)) AS ?label)`)}
}`;

/** Distinct predicates actually used in the database, for the field picker. */
export const LIST_PREDICATES = `
SELECT DISTINCT ?p WHERE {
${g(`    ?s ?p ?o .`)}
}`;

/**
 * The term index used for object-value autocomplete: every IRI in the graph
 * that carries a label, regardless of type. This includes concepts from this
 * vocabulary AND any imported vocabulary terms that have been materialised in
 * the graph (quantity kinds, external sameAs targets that got labelled, etc.).
 */
export const TERM_INDEX = `
SELECT DISTINCT ?iri ?label ?type WHERE {
${g(`    ?iri ?labelProp ?label .
    VALUES ?labelProp {
      <http://www.w3.org/2004/02/skos/core#prefLabel>
      <http://www.w3.org/2000/01/rdf-schema#label>
    }
    FILTER(isIRI(?iri))
    OPTIONAL { ?iri a ?type }`)}
}`;
