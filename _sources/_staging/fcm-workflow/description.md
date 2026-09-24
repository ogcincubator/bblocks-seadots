# FCM solver workflow

SeaDOTs Catalog Workflow profile for the fuzzy-cognitive-map solver of
[FuzzyCognitiveMapTools.jl](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl)
v0.1.0: the record that makes the solver discoverable as the step between a map (input)
and its solutions or sequences (output).

It iterates `x ← f(Wᵀx)` from many random initial states, clusters the endpoints that
agree within tolerance, and reports one representative equilibrium per cluster with its
componentwise spread.

## Why this block exists

A map is self-contained: it carries its own activation specification, so nothing about
the *function being iterated* has to be supplied at run time. That sounds like it makes a
workflow record unnecessary. It does the opposite.

Because the map carries everything it can carry, everything that distinguishes one run
from another lives **only as Julia keyword arguments** and is serialised nowhere — not in
the map, not in the solution, not in the sequence. Take the worked solution of the
researcher-proposal map: it cannot be reproduced from the published artefacts, because
nothing in them records that 1000 trials were run, from states drawn in `[0, 1]` and
clamped to `[0.1, 0.9]`, capped at 100 iterations, converged at `1e-10` and clustered at
`1e-6`.

The `solver` object is where those go. It also declares the two things a consumer cannot
infer from the data model at all: which activation functions are implemented, and which
inference rule is applied.

## What the solver can actually run

The activation scheme names ten concepts, because it names what the *FCM literature and
tool ecosystem* use. This solver implements **three** of them — the three branches of
`to_proc`:

| concept | upstream label | computes |
| --- | --- | --- |
| `fcmact:logistic` | `"logistic"` | `a / (1 + exp(−λ(x − b)))` |
| `fcmact:logistic-of-square` | `"gaussian"` | `a / (1 + exp(−λ(x − b)²))` |
| `fcmact:offset` | `"other"` | `x + a` |

Anything else raises `"Unknown activation function"` at load time. A map naming
`fcmact:hyperbolic-tangent` is perfectly well-formed and simply cannot be run here, which
is exactly the mismatch `supportedActivation` exists to let a catalog detect before
dispatch rather than after.

The label correction is visible in that table: upstream `"gaussian"` appears as
`logistic-of-square` because that is what the code computes — a logistic of the squared
deviation, not a bell curve. See `ogc.hosted.seadots.fcm-activation-scheme`.

`inferenceRule` is `kosko` and nothing else: `single_fcm_trial` hard-codes `mul!(x_next,
W', x)` with no parameter to select another rule. It is declared as an enum rather than a
constant so a record describing a later release can say something different without a
schema change.

## Three things to know before trusting a run

**The execution parameters cannot currently be set.** `run_trials` calls
`single_fcm_trial(fcm)` with no overrides and carries the comment `# TODO parameters to
be passed to single_fcm_trial`. So through the public entry point every run uses the
compiled defaults, and the values in `executionParameters` describe what *did* happen
rather than what was chosen. Recording them is still worth doing — they are what a
reproduction needs — but a record claiming non-default values for v0.1.0 is describing
something the public API cannot produce.

**Trials that never converged are still counted.** `run_trials` pushes every trial's
endpoint into the clustering regardless of `trial.b_converged`, so a trial that exhausted
`maxIterations` with a large residual contributes to a centroid and inflates the matching
`maxdists`. Combined with `b_success` never being set false, this makes `maxdists` the
only real quality signal a consumer has. See `ogc.hosted.seadots.fcm-solution`.

**The sampling range is wider than the clamp range.** `x0Range` is `[0, 1]` and
`x0ClampRange` is `[0.1, 0.9]`, and the clamp is applied after sampling. The extremes of
the sampling range are therefore never explored: any draw below 0.1 or above 0.9 collapses
onto the boundary. Whether that is deliberate — keeping starts off the saturated tails of
the logistic — or an artefact of two defaults chosen independently is worth asking
upstream. Both fields are declared so a record cannot hide the discrepancy.

## Refinement runs under different settings

The optional second pass (`refine_centroid_fcm`) re-solves from each cluster mean to
sharpen the centroid, and it does **not** inherit the trial settings: it uses 3000
iterations, tolerance `1e-13`, and clamp range `[0, 1]` — the full range, not the narrowed
one. If the refined point lands further than `checkTolerance` from the cluster mean the
run `error`s out rather than warning. The `refinement` object records these separately for
that reason; folding them into `executionParameters` would assert a single set of settings
that does not exist.

## JSON-LD projection

`solver` maps to `fcm:solverCapability`, `inferenceRule` and `supportedActivation` to
`fcm:inferenceRule` and `fcm:supportsActivation` (both resolving to scheme IRIs), and
`stochasticMapsSupported` to `fcm:supportsStochasticMaps`. `fcm:SolverCapabilityShape`
checks that a capability names at least one activation function and exactly one inference
rule — the failure mode that would let a map be routed to a solver that cannot run it.

`executionParameters` and `refinement` are **not** mapped. They are numeric run settings
with no ontology terms behind them, and minting a dozen datatype properties to hold
values that the upstream API cannot yet vary would be modelling ahead of the code. They
are schema-validated and left out of RDF, which is the same call made for
`activation_spec.*.params` in `ogc.hosted.seadots.fcm`. Revisit when `fcm-execution` is
written against a real run.

## Relationship to other blocks

| | |
| --- | --- |
| `catalog-workflow` | the generic record profiled here |
| `fcm` | the input this workflow consumes |
| `fcm-solution`, `fcm-sequence` | the outputs it produces |
| `fcm-activation-scheme` | the vocabulary `supportedActivation` and `inferenceRule` draw on |
| `catalog-execution` | where a *particular* run would be recorded — deferred until one exists |

## Deferred

`fcm-execution` (a `catalog-execution` profile) is not written. It should be, once there
is a real run to describe: the execution record is where the parameter values actually
used, the input map's identifier and the resulting solution's identifier belong, and
writing it against a hypothetical run would invent all three. `fcm-process` (an OGC API
Processes description) waits on the solver getting an endpoint; today it is a library, not
a service.
