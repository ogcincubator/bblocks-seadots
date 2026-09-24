# FCM sequence

A time-indexed series of fuzzy cognitive maps and the solutions computed from them: how
the causal structure a stakeholder group describes, and the equilibria that structure
implies, change over successive elicitation rounds.

Source-faithful to `DeterministicFCMSequence` in
[FuzzyCognitiveMapTools.jl](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl)
v0.1.0 (`src/fcm/fcm_sequence.jl`).

## Three parallel arrays, not a list of steps

```json
{ "timespec_series": [...], "fcm_series": [...], "solution_series": [...] }
```

Whatever sits at index *k* of each array is one (time, map, solution) triple. The upstream
author states the reason plainly: three separate vectors make plotting easier. The
consequence is that **position is the only thing binding a step together**, and the three
arrays must be the same length or the document means nothing.

The ontology models the materialised form instead — `fcm:SequenceStep` with `fcm:atTime`,
`fcm:usesMap` and `fcm:hasSolutionAtStep` — so that a step is a resource rather than an
index. Both forms are in the ontology, and going from the serialised one to the
materialised one is an index join, not an entailment; a consumer that wants steps has to
perform it.

## The one place RDF is stricter than the schema

Everywhere else in this block family the JSON Schema carries what it can and SHACL picks
up the cross-field invariants. Here something better happens.

`timespec_series`, `fcm_series` and `solution_series` project to **RDF lists**, because
their order is the whole point. A list can be counted. So the equal-length invariant —
which JSON Schema cannot state, since it relates the lengths of three siblings — is
enforced for real by `fcm:SequenceSeriesShape` in `ogc.hosted.seadots.fcm-ontology`.

This is the one invariant in the FCM blocks where the RDF projection is not a lossy
convenience but the *only* mechanical check available. Validating a sequence against the
schema alone will accept a document with five solutions for six maps. **Run the SHACL.**

## Constraints still not carried anywhere

**Time specs must be pairwise non-overlapping.** Upstream `Base.isless` on two
`AbstractTimeSpec`s does not return a fallback for overlapping intervals — it
`throw`s `ArgumentError("cannot order overlapping time intervals")`. A sequence whose
`timespec_series` contains two overlapping specs therefore cannot be sorted at all. This
needs a block test: checking it means computing `bounds` for the week and month forms,
which is arithmetic, not a constraint language. See `ogc.hosted.seadots.fcm-timespec` for
why those bounds are not the ISO ones.

**A solution must match its own map's vertex count.** Each step's centroid vectors are
positionally aligned with that step's `fcm_series[k].graph.vertices`, not with any other
step's. Three-way and cross-array, so neither JSON Schema nor SHACL reaches it. Block
test.

## A sequence is an output that embeds its own inputs

The upstream constructor takes the timespecs and the maps and computes the solutions, so
the sequence as a whole is a digital-twin **output**: `catalog-data` with `role: output`
and `derivedFrom` pointing at the maps it consumed. That it also contains those maps
verbatim does not make it an input record; it makes it self-contained.

## Publication note: the maps repeat

The worked example is 54 kB for six steps of a ten-concept map, and nearly all of it is
the same map written six times — exactly one weight differs between consecutive steps.
This is fine as an exchange serialisation and poor as a publication format. For anything
larger than a workshop toy, publish the maps once as `catalog-data` records and the
sequence as a table of (time, map reference, equilibrium), for which
`catalog-data-tabular` is the right profile.

## JSON-LD projection

The context composes the three sibling contexts, each inlined under the scope of its
series property, so a map inside `fcm_series` lifts exactly as a standalone `fcm`
document does — the same vertex-key-to-IRI treatment, the same `"gaussian"` →
`fcmact:logistic-of-square` correction — and a timespec inside `timespec_series` carries
its own `type` discriminator and so types itself honestly.

Every context gap of the sibling blocks is inherited and none is added:
`activation_spec.*.params`, `matrix.weights`, `matrix.nodeLabels`, and `centroids` /
`maxdists`. The last is the one that bites here, because a sequence is the one document
that *does* have both halves of the join — the map's vertex order and the solution's
positional vector sit side by side at the same index. Materialising `fcm:NodeState` nodes
from a sequence is therefore possible, and is the obvious next transform to write; it is
not possible from a solution document alone. Recorded rather than done, because it is a
transform, not a context.

## Relationship to other blocks

| | |
| --- | --- |
| `fcm-ontology` | `fcm:Sequence`, `fcm:SequenceStep`, the three series properties, and the equal-length shape |
| `fcm` | the element type of `fcm_series` |
| `fcm-timespec` | the element type of `timespec_series`, and the non-overlap rule |
| `fcm-solution` | the element type of `solution_series` |
| `catalog-data` | publishes the sequence, with `role: output` and `derivedFrom` |
| `catalog-data-tabular` | the better profile once the maps are published separately |
| `catalog-data-tabular-survey` | the elicitation rounds the successive maps came from |

## Source-property coverage

Every field of `DeterministicFCMSequence` is present: `timespec_series`, `fcm_series`,
`solution_series`. Nothing is dropped, nothing is renamed.
