## Fuzzy Cognitive Map ontology

A fuzzy cognitive map (FCM) is a signed, weighted directed graph in which each node is a
variable or indicator of the modelled system and each edge asserts that a change in one
node drives a change in another, with a magnitude. In SeaDOTs, FCMs carry participatory
knowledge: what stakeholders believe causes what, elicited in workshops and iterated over
survey rounds.

This block defines the core model, derived from the data-representation structs of
[FuzzyCognitiveMapTools.jl](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl)
v0.1.0 and its `dataspecs/fcm_dataspecs__20260630.md`.

### Scope

| Source structure | Ontology term |
| --- | --- |
| `SimpleDeterministicFCM` | `fcm:DeterministicFuzzyCognitiveMap` |
| `SimpleDeterministicFCMGraph` | `fcm:ConceptGraph` |
| `SimpleDeterministicFCMVertex` | `fcm:ConceptNode` (+ `fcm:nodeKey`, `fcm:representsConcept`) |
| `SimpleDeterministicFCMEdge` | `fcm:InfluenceEdge` (+ `fcm:sourceNode`, `fcm:targetNode`, `fcm:hasWeight`) |
| `ActivationSpec`, `ActivationFunctionSpec` | `fcm:ActivationSpec`, `fcm:ActivationAssignment`, `fcm:Parameter` |
| `DeterministicFCMSolution` | `fcm:Solution`, `fcm:Equilibrium`, `fcm:NodeState` |
| `DeterministicFCMSequence` | `fcm:Sequence`, `fcm:SequenceStep` |
| `PointTimeSpec` … `RangeTimeSpec` | `fcm:TimeSpec` and its four subclasses |

`fcm:InfluenceEdge` is a subclass of `prop-rel:PropertyRelationship` from
`ogc.hosted.seadots.ontology`, and `fcm:hasWeight` a subproperty of `prop-rel:hasWeight`,
so an FCM edge is a SeaDOTs property relationship and inherits its weight-as-quantity-value
treatment.

### Three places the RDF form deliberately differs from the wire form

1. **Node identity.** Upstream, a vertex is an opaque graph-local string (`"C1"`, `"Nd"`).
   That is kept as `fcm:nodeKey`, but `fcm:representsConcept` carries the IRI of the
   variable, indicator or taxon the node stands for. Without it a map cannot be joined to
   anything else in the SeaDOTs catalog.
2. **No parallel arrays.** `DeterministicFCMSequence` stores three index-aligned vectors;
   `fcm:SequenceStep` materialises each triple as one resource, with `fcm:stepIndex`
   preserving the original position so the round trip stays exact. The same applies to
   heterogeneous activation (`fcm:ActivationAssignment` names its node) and to equilibrium
   vectors (`fcm:NodeState` names its node).
3. **Polarity is derived, not stored.** `fcm:hasPolarity` is produced from the sign of the
   weight by a SHACL rule in `rules.shacl`. Nothing asserts it by hand, so the sign and the
   weight cannot drift apart.

### Constraints

`rules.shacl` carries the graph invariants enforced by `_check_core_fcm_graph_validity`
upstream (at least two nodes, at least one edge, every endpoint resolvable within the same
graph, no unconnected node), plus node-key uniqueness, activation-mode coherence, and
one-node-state-per-node.

Note that the upstream validator enforces **no range on the weight**. The [-1, 1]
convention is documented but not checked, and this block does not check it either; add a
`sh:minInclusive`/`sh:maxInclusive` shape only once the modelling team confirms the
convention is binding.

---

## Future work

Alignments to external vocabularies are recorded here rather than asserted in
`ontology.ttl`, so that the core model can be reviewed and validated on its own before it
inherits anyone else's semantics. Each item below is a candidate for a future alignment
file (`alignments.ttl`), not a commitment.

### A1. Causal relations — OBO Relation Ontology

`fcm:Positive` and `fcm:Negative` correspond to
[`RO:0002304`](http://purl.obolibrary.org/obo/RO_0002304) *causally upstream of, positive
effect* and [`RO:0002305`](http://purl.obolibrary.org/obo/RO_0002305) *causally upstream
of, negative effect* (with `RO:0004047`/`RO:0004046` as the "or within" variants).

**Caveat that blocks a straight equivalence:** RO's definitions are phrased over
occurrents — "the execution of p", "the progression of x" — so they relate *processes*.
FCM nodes here are variables and indicators. Any alignment must therefore be
`skos:closeMatch`, never `owl:equivalentProperty`, unless SeaDOTs first commits to
modelling each node as a process (a change-in-quantity), which would be a much larger
decision.

### A2. Graph structure and generic causality — SIO

[SIO](https://jbiomedsem.biomedcentral.com/articles/10.1186/2041-1480-5-14) offers
`is causally related to` (`SIO_000294`), `is causally related from` (`SIO_000352`),
`is causally related with` (`SIO_000243`), `edge` (`SIO_001334`), `node` (`SIO_001335`),
`arc` (`SIO_001333`) and `has value` (`SIO_000300`).

A generic `fcm:influences rdfs:subPropertyOf sio:SIO_000294` is defensible and cheap.
SIO's `edge`/`node`, however, are diagram/geometry-flavoured ("an edge is a line connecting
two graph vertices"), and SIO has no signed or weighted edge, so it cannot carry the FCM
model on its own.

### A3. Export to qualitative-network standards — SBML `qual` and XMILE

- [SBML Level 3 `qual`](https://sbml.org/specifications/sbml-level-3/version-1/qual/sbml-qual-version-1-release-1.pdf):
  `QualitativeSpecies` ↔ `fcm:ConceptNode`, `Transition` with Input `sign` ∈ {positive,
  negative, dual, unknown} ↔ `fcm:InfluenceEdge` + derived `fcm:hasPolarity`. Lossy: sign
  survives, the weight does not, and `qual` assumes discrete levels.
- [XMILE v1.0](https://docs.oasis-open.org/xmile/xmile/v1.0/xmile-v1.0.html) (OASIS
  Standard, 2015): signed connectors plus `sim_specs`. The nearest standardised sibling of
  "weighted influence model with a run specification"; useful as a precedent for the
  planned `fcm-execution` block. Lossy in both directions — stock-and-flow semantics are
  not FCM equilibrium semantics.

Both are worth having as one-way export profiles once the schema blocks exist. Neither is
a candidate for the canonical model.

### A4. Round trip with the FCM tool ecosystem

The formats stakeholders actually exchange are matrix-shaped: an n×n weight matrix with
named rows and columns, as used by
[FCMpy](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9575875/) (csv/xlsx/json),
[Mental Modeler](https://www.mentalmodeler.com/) and FCMapper. Edge-list ↔ matrix is
lossless given a declared node ordering, so the planned `fcm` **schema** block should
validate both shapes and declare the ordering explicitly.

*Unresolved:* Mental Modeler is web-based and publishes no format specification. Pinning
down its field names needs an actual export file from the Utsira workshops.

### A5. Time specifications — OWL-Time

`fcm:PointTimeSpec` ↔ `time:Instant`; the three interval forms ↔ `time:ProperInterval`
with `time:hasBeginning`/`time:hasEnd`. Mechanical, and the obvious first alignment to
land. Blocked only on the serialisation defect below.

### A6. Node concepts — controlled vocabularies

`fcm:representsConcept` should resolve into the SeaDOTs indicator vocabulary
(`https://w3id.org/indicators/marine/`) and `oim-variables`; for the Utsira draft map also
WoRMS (e.g. *Nephrops norvegicus*,
`urn:lsid:marinespecies.org:taxname:107254`), ENVO for habitat concepts, and CICES for the
ecosystem-service and socio-economic nodes (jobs, tourism, community facilities).

### A7. Quantity values — QUDT lift

`fcm:stateValue` and `fcm:maxDistance` are plain `xsd:double` datatype properties. They
could be lifted to `qudt:QuantityValue` nodes for consistency with `fcm:hasWeight`. Deferred
because it triples the node count of an equilibrium for no gain until a unit other than
"dimensionless" appears.

### A8. Fix needed in `prop-rel` before two alignments can land

`prop-rel:fromProperty` and `prop-rel:toProperty` in `ogc.hosted.seadots.ontology` both
declare `rdfs:range prop-rel:PropertyRelationship`, which looks like a copy-paste error —
the range of "from property" should be a property, not a relationship. Until that is
corrected, `fcm:sourceNode`/`fcm:targetNode` cannot be declared subproperties of them
without entailing that every `fcm:ConceptNode` is a `PropertyRelationship`. They are
therefore standalone, with an editorial note in `ontology.ttl`.

### A9. Not pursued

- **Fuzzy OWL 2** (Bobillo & Straccia) encodes fuzzy degrees as OWL 2 annotation
  properties. It addresses fuzzy *membership*, not causal-map structure; edge weights here
  are ordinary numeric attributes, so this would add machinery for no benefit.
- **Published FCM ontologies.** A review found only academic one-offs (e.g. RB-FCM
  Ontology Agents, 2007) and research-stage frameworks with no resolvable namespace. There
  is nothing to import, which is why this block mints its own terms.

### A10. Stochastic maps

`fcm:StochasticFuzzyCognitiveMap` exists as a discriminator hook and nothing more. The
upstream `SimpleStochasticFCMEdge` carries `Tuple{Float64, Distribution}`, which has no
serialisation in v0.1.0 and is flagged upstream as certain to change. Distribution-valued
weights need a distribution vocabulary (QUDT statistics, STATO, or UncertML) chosen at the
point the upstream type stabilises.
