# Fuzzy Cognitive Map

A fuzzy cognitive map is a signed, weighted digraph of concepts: each node is a variable
or indicator of the modelled system, each edge asserts that a change in one concept drives
a change in another, with a magnitude. In SeaDOTs the weights carry participatory
knowledge elicited from stakeholders.

This block is the **source-faithful** profile of the map as serialised by
[FuzzyCognitiveMapTools.jl](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl)
v0.1.0. Field names, nesting and types are exactly the upstream ones; nothing is renamed
or restructured.

## Why the map is a digital-twin *input*

The activation specification is a field of the map object, not a parameter of the run that
consumes it, so a map arrives at the solver self-contained. The dividing line used across
the FCM blocks is therefore mechanical:

- **in the JSON → input data**: `graph`, `metadata`, `activation_spec` (mode, function
  label, and the numeric parameters `a`, `b`, `lambda`)
- **only a Julia keyword argument → execution parameter**: `x0_range`, `x0_clamp_range`,
  `maxitr`, `tol_convergence`, trial count. None of these are serialised anywhere, and
  they belong on the execution record.

A map is catalogued as a `catalog-data` record with `role: input`; solutions and sequences
are catalogued with `role: output` and `derivedFrom` pointing back at it.

## Two representations, one map

Exactly one of `graph` or `matrix` must be present.

`graph` is the upstream edge list. `matrix` is the n×n adjacency form that FCMpy, Mental
Modeler and FCMapper speak. The conversion is lossless — the worked example round-trips 14
edges into exactly 14 non-zero cells of a 10×10 matrix — but only because two things are
stated rather than assumed:

- `nodes` declares the ordering that both axes follow, so the matrix does not depend on the
  order of an external vertex list;
- `orientation` is a **required constant** `source-major`, declaring that `weights[i][j]` is
  the influence of `nodes[i]` on `nodes[j]`. The opposite convention is equally common and
  silently transposes the whole model, which is a failure no validator would catch. The
  solver applies the transpose itself at iteration time, computing `f(W'x)`.

## Constraints this schema does not carry

`minItems` gives the upstream "at least 2 vertices, at least 1 edge" rule, but two of the
four invariants enforced by `_check_core_fcm_graph_validity` are relations *between*
sibling arrays and are not expressible in JSON Schema:

- every `src`/`dst` must resolve to a vertex of the same map;
- no vertex may be left unconnected.

Both are carried as SHACL constraints by `ogc.hosted.seadots.fcm-ontology`, together with
node-key uniqueness and activation-mode coherence. **Schema validation alone is not
sufficient for this block.**

The matrix form has the mirror-image gap: that `weights` is square against `nodes` relates
the lengths of two sibling values, so it is not expressible in JSON Schema, and not
checkable in RDF either since the cells are not there. It needs a block test. What SHACL
does check on the header is that at least two nodes are indexed and that an orientation is
declared.

The `[-1, 1]` weight convention is documented upstream but enforced nowhere — not in the
Julia validator and not here. Adding a range shape is a one-line change once the modelling
team confirms the convention is binding.

## JSON-LD projection

`context.jsonld` was tested by lifting each example to RDF and running the ontology's SHACL
rules over the result. Four things are worth knowing before relying on it.

**Vertex keys become node IRIs.** `id` maps to `@id`, so `"C1"` resolves against the
document base and edges' `src`/`dst` (both `@type: @id`) point at the same IRIs. Graph
structure therefore survives the lift intact — 10 `fcm:hasNode`, 14 `fcm:hasEdge`, 14
resolved endpoints for the worked example. The consequence is that `fcm:nodeKey` is *not*
separately materialised: in this projection the key is the final segment of the node IRI.
Directly-authored RDF should assert `fcm:nodeKey` as usual.

**Edge keys stay literals.** `id` on an edge maps to `fcm:edgeKey`, not `@id`, because the
conventional edge key `"C5->C3"` contains `>` and is not a legal IRI. Edges are blank
nodes; they have no need for stable identity.

**Upstream activation labels are corrected on the way in.** `label` is `@type: @vocab`, so
`"logistic"` → `fcmact:logistic` and `"other"` → `fcmact:offset`. Critically,
`"gaussian"` → `fcmact:logistic-of-square`, which is what the implementation actually
computes; see the `fcm-activation-scheme` block. The correction happens in the context, so
no consumer has to know about it.

**The matrix form projects at header level, not per cell.** This is the same arrangement
as any array or datacube description: the ILIAD `zarr_array_metadata` block maps `shape`,
`chunks`, `dtype` and `order` to RDF while the array values never enter it. `matrix.nodes`
maps to `fcm:matrixNodes` as an **RDF list**, because it is the coordinate list of both
axes and its order is semantic; `matrix.orientation` maps to `fcm:matrixOrientation`,
resolving `source-major` to `fcm:SourceMajor` — the direct analogue of Zarr's `order`.
`matrix.weights` stays out of RDF, exactly as array cells do.

The first attempt mapped `matrix.nodes` onto `fcm:hasNode` and produced a *graph* with
nodes and no edges, which correctly failed the dangling-node and minimum-edge constraints.
That failure was the signal that a matrix is not a graph projection but an array-header
one, which is why `fcm:WeightMatrix` is a class of its own rather than a second way of
writing `fcm:ConceptGraph`.

### Known context gaps

Two free-keyed objects are **not mapped**, for the same reason: JSON-LD cannot address
arbitrary keys. `matrix.nodeLabels` (`{"C1": "..."}`) is one; where labels matter, use the
edge-list form, whose vertex metadata maps to `skos:prefLabel` properly.

`activation_spec.*.params` is the other. It is **not mapped**. It is a free-keyed object (`{"a": 1, "b": 0,
"lambda": 1}`) and JSON-LD cannot address arbitrary keys, while the ontology models
parameters as `fcm:Parameter` nodes with `fcm:parameterName` / `fcm:parameterValue`. Faking
a mapping would mint properties that do not exist, so the keys are left unmapped and the
gap is recorded here. Closing it needs a transform, `{"a": 1}` → `[{"parameterName": "a",
"parameterValue": 1}]`, which would be the right shape for a future version of the upstream
serialiser.

## Relationship to other blocks

| | |
| --- | --- |
| `fcm-ontology` | the semantics, and the SHACL constraints this schema cannot express |
| `fcm-activation-scheme` | the vocabulary `label` resolves into |
| `fcm-timespec` | when a map applies; the element type of a sequence's `timespec_series` |
| `fcm-solution` | the equilibria computed from a map; index-aligned with *this* block's vertex order |
| `fcm-sequence` | maps and solutions over successive elicitation rounds |
| `catalog-data` | the record that makes a map discoverable, with `role: input` |
| `catalog-data-multidim` | the right catalog profile for a map published in `matrix` form — array-oriented data with a declared coordinate list is exactly what that profile describes |
| `catalog-data-tabular-survey` | the elicitation the weights came from; a map's `derivedFrom` should point at it |
| `catalog-workflow` | declares which activation concepts the solver actually supports — `logistic`, `logistic-of-square` and `offset` only |

## Source-property coverage

Every field of the upstream `SimpleDeterministicFCM`, `SimpleDeterministicFCMGraph`,
`SimpleDeterministicFCMVertex`, `SimpleDeterministicFCMEdge`, `ActivationSpec` and
`ActivationFunctionSpec` is present. Nothing is dropped.

The stochastic variant is **out of scope**: `SimpleStochasticFCMEdge` carries
`Tuple{Float64, Distribution}`, which has no serialisation in v0.1.0 and is flagged
upstream as certain to change.
