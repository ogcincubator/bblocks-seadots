# FCM solution

What iterating a fuzzy cognitive map to convergence produces. The solver runs many trials
from random starting states, clusters the endpoints that land within tolerance of each
other, and reports one representative point per cluster:

- `centroids` — one state vector per distinct equilibrium found;
- `maxdists` — for each, the componentwise spread `max − min` across the cluster it
  represents, as a rudimentary error bound;
- `b_success` — whether the map settled on finitely many discrete stable points.

Source-faithful to `DeterministicFCMSolution` in
[FuzzyCognitiveMapTools.jl](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl)
v0.1.0 (`src/fcm/proc_trials.jl`). A solution is a digital-twin **output**: it is
catalogued as a `catalog-data` record with `role: output` and `derivedFrom` pointing at
the map it came from.

## A solution does not stand on its own

This is the fact that governs everything else in this block. The document carries **no
node identities**. Element *i* of every centroid is the value of the *i*-th vertex of the
map that was solved, and nothing in the solution says which map that was or what its
vertex order is.

The worked example here is recognisably the solution of the ten-concept
researcher-proposal map carried by `ogc.hosted.seadots.fcm` only because both have ten
components. That is not identification, it is a coincidence of arity.

Two consequences:

- **Always publish a solution with a reference to its map.** In a catalog record that is
  `derivedFrom`; inside a sequence it is the index alignment of `fcm_series` and
  `solution_series`. A solution published alone is uninterpretable, not merely
  inconvenient.
- **The RDF projection stops at `b_success`.** See below.

## Constraints this schema does not carry

`centroids` and `maxdists` must have the same outer length, and correspondingly-indexed
inner vectors must have the same length as each other and as the vertex count of the map.
All three are relations *between* values — two siblings, or a sibling and an external
document — and none is expressible in JSON Schema. They need a block test.

What the schema does carry is the part that is local:

- inner vectors have `minItems: 2`, from the upstream rule that a map has at least two
  vertices;
- `maxdists` components have `minimum: 0`, **derived** from their construction as
  `maximum(Xmat; dims=2) .- minimum(Xmat; dims=2)`, not declared upstream;
- a conditional: when `b_success` is true, `centroids` and `maxdists` must be non-empty.
  A successful solve that found nothing is incoherent.

## `b_success` is never false

Worth knowing before trusting it. The flag is documented upstream as the signal that a
solution must be ignored, but **no code path in v0.1.0 sets it to `false`**: both
`DeterministicFCMSolution` constructors end in `DeterministicFCMSolution(centroids,
maxdists, true)`.

It is not a dead flag either, because the situation it warns about does arise:
`run_trials` pushes **every** trial endpoint into the clustering regardless of
`trial.b_converged`, so a trial that exhausted `maxitr` with a large residual contributes
to a centroid and inflates the corresponding `maxdists` entry, silently. A large
`maxdists` value relative to its centroid is the only evidence a consumer currently has
that this happened.

Read `b_success: true` as "not yet contradicted", and treat `maxdists` as the real quality
signal. Reported upstream.

## JSON-LD projection

Only `b_success` projects, to `fcm:hasFiniteEquilibria`. `centroids` and `maxdists` are
**not mapped**, for a reason stronger than the usual JSON-LD addressing limits: the
ontology models an equilibrium as `fcm:Equilibrium` with one `fcm:NodeState` per node,
each naming its node through `fcm:ofNode`, precisely to replace the positional coupling
this document relies on. Producing those nodes needs the node identities, which are in the
map, not here.

So the lift is a **join**, not a projection: given the map and the solution, element *i*
becomes `fcm:NodeState` of vertex *i* with `fcm:stateValue` and `fcm:maxDistance`. That
transform belongs in the sequence block or in a publication pipeline that has both
documents in hand. Mapping the arrays to an RDF list of doubles instead would be
well-formed and useless — it would assert a list of numbers where the ontology asks for
named node states — so the gap is left open and recorded here rather than papered over.

This is the same discipline applied to `matrix.weights` and `activation_spec.*.params` in
`ogc.hosted.seadots.fcm`: project what can be projected honestly, record the rest.

## Relationship to other blocks

| | |
| --- | --- |
| `fcm-ontology` | `fcm:Solution`, `fcm:Equilibrium`, `fcm:NodeState` and the join target |
| `fcm` | the map this is the solution *of*; index alignment is against its vertex order |
| `fcm-sequence` | embeds solutions index-aligned with their maps and time specs |
| `catalog-data` | the record that publishes a solution, with `role: output` and `derivedFrom` |
| `catalog-data-tabular` | the right profile for a solution exported as a table |

## Source-property coverage

Every field of `DeterministicFCMSolution` is present: `centroids`, `maxdists`,
`b_success`. Nothing is dropped, nothing is renamed.

The execution parameters that produced the solution — `num_trials`, `x0_range`,
`x0_clamp_range`, `maxitr`, `tol_convergence`, and the clustering `tol` — are **not** in
this document and are not serialised anywhere upstream. They belong on an execution
record. Without them a solution is not reproducible, which is the main argument for
writing the deferred `fcm-execution` block once a real run exists.
