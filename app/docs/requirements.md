
## general requirements

* It is a lightweght web application available as a single container.
* It allows to edit content of the Vocprez content stored in the backend triplestore (Fuseki for now).
* App should allow to manipulate the data without expertise in RDF.
* Data stored in Voceprez is organised as SKOS hierarchy.
* Sample data is in the bblocks-seadots/_sources/oim-variables/examples.
* application shall keep configuration for secrets, credentials, endpoints, additional rdf validators
* front end aplication shall be fast and use browser store for any changes done by the user
* changes in the triplestore and git shall be commited only on the user request
* change commits shall be allowed only for authenticated user

## authentication
* anonymous user can edit terms in the browser space and export all the changes as RDF - see requiremnts for RDF serialisation
* application allow to login with github authentication and RBAC is based on github priviledges
* users with editor role are allowed to commit changes or send to db
* git KEY and fuseki credentials are provided in the configuration


## Functional requirements

* User shall be able to change and add predicate for each concept
* User chall be able to add and change object of the subject+predicate

Application has following pages:
1. **Browse** (`/`) — a searchable, filterable list of every concept or concept scheme in the
   graph. Filter by type: concept/conceptscheme, for concepts also by concept scheme (Indicators / Parameters / Relationships) and by type, or search by name/CURIE. Click a concept to edit it.
2. **Edit concept** (`/concept/:iri`, and `/concept/new`) — edit the fields a
   concept already has and **add new fields**. Each value is either:
   - **free text** (with an optional language tag), or
   - a **vocabulary term** chosen with a typeahead. As you type, matching terms
     from this vocabulary *and* imported/materialised vocabularies are
     suggested (e.g. typing `herr` surfaces herring-related concepts). You can
     also paste any external IRI/CURIE for terms not yet in the store.
  - blank nodes shall not be visible and generated as export/commit file
  - reduntant fields (see content convention) shall be presented only once with potentially several predicated at the same time

   Which input a field offers (text vs. term picker vs. both) is driven by the
   curated predicate palette in `src/rdf/terms.ts`.

3. **Concept Scheme** (`/conceptScheme) editor allow to edit in a bulk all the concepts
 - it is based on the tabular view with selected predicates
 - default view presents id, label, description, ConceptScheme it belongs to, Types other than skos ones, Broader/Narrower relationship
 - each of the values excluding id are editable
 - values can be free text or dropdown combo list with relevant values - see 'General manipulation constraints' reqs
 - 


General manipulation constraints
- for broader and narrower relationships only terms from the same database are available
- for Concept scheme only Concepts chemes from this database are available
- vocabulary based objects selection shall allow to select terms from the same database (regardless of scheme) and imported vocabularies (configurable)
- vocabulary based predicate selection shall allow to select terms from the same database (regardless of scheme) and prefixes used in the database - they can be either based on reference content or configuration
- each edit page shall have download all, Publish and Commit buttons as described in the Save model reqs



## Save model: edit locally, push when ready

Edits never hit the server until you decide. They accumulate in an in-browser
draft shown in the **Pending changes** panel (bottom-right), which renders a
human-readable diff of what will be added/removed. From there you can:

- **Download All** — export your additions as `seadots-additions.ttl` to
  commit through the bblocks repo (the reviewed/governed path), or
- **Publish** — apply the changes immediately as a single SPARQL
  `DELETE DATA` / `INSERT DATA` update against the configured update endpoint.
  *(Pushing may require the endpoint to accept your credentials/CORS.)*

- **Commit to Git** — when the backend server is running, enter a message and
  the additions are written to a Turtle file, committed on the `concept-edits`
  branch, and pushed upstream for review via PR. (Hidden in static-only
  deployments.)

  - Publish and Commit buttons can be disabled and are on default disabled in the configuration
- Publish and Commit buttons access is controled by roles based constraints (RBAC)

Use **view SPARQL** to inspect the exact update before pushing.

## content convention

Database shall follow Vocprez conventions
* renderable concepts must be of skos:Concept type and belong to ConceptScheme
* ConceptScheme shall belong to Dataset as both dcterms:hasPart and dcat:dataset
* every Concept and Concept Scheme has prefLabel and defitnition
* both dcterms:isPartOf and dcterms:hasPart relationships shall be present as bidirectional and complete
* both skos:hasTopConcept and skos:inScheme relationships shall be present as bidirectional and complete
* top concepts shall be skos:hasTopConcept of at least one ConceptScheme
* top concepts are these without skos:broder meaning
* skos:prefLabel and rdfs:label are deundant but both shall be present and shall be the same. skos:prefLabel is primary in case of conflict

## serialisation convention

RDF serialisation shall be human readible:
 - SKOS Concept Schemes and Data Set are first, than SKOS Concepts per each prefix alphanumeriacally sorted
 - for Concepts and Concept Schemes first goes type, than label, description, relationships to other terms in this taxonomy, relationships to external vocabularies, in the end structral internal SKOS hierarchy
 - RDF shall aggregate objects with the same predicate and object (, convention for TTL)
 - RDF shall aggregate 


 ## DB content organisation

 - [TODO] how it shall handle support of multiple schemes/dbs with their imported prefixes

 ## Configuration
 - triplestore endpoint and graphs are in the configuration. test defaut one will be https://project-seadots-definition-server.lab.dive.edito.eu/prez-b/sparql and empty graph
 - github app will be used for authentication and RBAC
 - all the environmental variables, endpoints vocabularies etc shall be injectable for docker/helm configuration, do not hardcode any of them