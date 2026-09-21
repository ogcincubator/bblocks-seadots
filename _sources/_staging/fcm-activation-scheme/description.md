## FCM activation and inference scheme

Two SKOS concept schemes used by `ogc.hosted.seadots.fcm-ontology`:

- **`fcmact:ActivationFunctionScheme`** — the transfer function applied componentwise to
  the state vector after each propagation step: `logistic`, `gaussian`,
  `logistic-of-square`, `offset`, `hyperbolic-tangent`, `bivalent`, `trivalent`.
- **`fcmact:InferenceRuleScheme`** — how the state is propagated through the weight matrix
  before activation: `kosko`, `modified-kosko`, `rescaled`.

### Why a concept scheme and not a string enumeration

Every FCM implementation names these functions differently, and two tools can apply
materially different mathematics under the same label. A map exchanged as
`{"label": "sigmoid"}` carries no guarantee about what will be computed at the other end.
Each concept here therefore carries a `schema:mathExpression` and its expected parameter
names, so the function is identified by what it computes rather than by what it is called.

Concepts not implemented by FuzzyCognitiveMapTools.jl v0.1.0 (`hyperbolic-tangent`,
`bivalent`, `trivalent`, and the non-Kosko inference rules) are declared anyway and marked
with a `skos:scopeNote`; they exist so that incoming maps from other tools can be described
rather than silently coerced.

### Two discrepancies recorded rather than normalised

1. **`gaussian`.** `ProcGaussianActivationFunction` in
   `src/fcm/activation_functions.jl` computes `a / (1 + exp(-lambda * (x - b)^2))` — a
   logistic of the squared deviation, monotone in `|x - b|` and bounded in `[a/2, a)`. A
   Gaussian activation is `a * exp(-lambda * (x - b)^2)`, a bell curve. The scheme declares
   both: `fcmact:gaussian` for the canonical meaning and `fcmact:logistic-of-square` for
   what the code does, with the upstream label `"gaussian"` bound to the latter. **This
   needs confirming with the package author**; if the bell was intended, the binding moves
   and this note goes away.
2. **Inference rule.** `single_fcm_trial` hard-codes `f(Wᵀx)` — classic Kosko — with no way
   to select another rule. A map exchanged with a tool defaulting to modified Kosko will
   not reproduce the same equilibria, which is why the rule is named explicitly in the model
   rather than left implicit.

---

## Future work

### B1. `skos:exactMatch` to tool-specific function names

`fcmact:logistic` and FCMpy's `sigmoid` are the same function, `a/(1+e^(−λ(x−b)))`; the
`tanh`, `bivalent` and `trivalent` concepts likewise mirror FCMpy's four transfer
functions, and the three inference rules mirror its Kosko / modified Kosko / rescaled
options. FCMpy exposes no IRIs, so an alignment file would have to mint IRIs on its behalf
or map to literal tool-and-version-qualified strings. Deferred until the exchange direction
is actually needed; the `skos:altLabel` values carry the tool names in the meantime.

### B2. Parameter-name mapping

`fcmact:hasParameterName` records `a`, `b`, `lambda` as FuzzyCognitiveMapTools.jl names
them. Other tools parameterise the same curves differently (slope-and-offset, or a single
steepness). A future alignment should map parameter *roles*, not names, otherwise a
round trip silently rescales the curve.

### B3. Linguistic terms

FCMpy builds weights from expert ratings expressed as triangular membership functions,
`[lower, center, upper]` per linguistic term (`'-vh': [-1, -1, -0.75]`). SeaDOTs
participatory elicitation will need the same. That belongs in a separate
`fcm-elicitation` block, not here: it describes how a weight was *derived*, not how the map
is *iterated*.

### B4. SBML `qual` transition terms

SBML `qual` expresses its update logic as `FunctionTerm`s with MathML rather than as named
transfer functions. Mapping the two is possible only for the threshold concepts
(`bivalent`, `trivalent`); the continuous ones have no `qual` counterpart. See section A3 of
the `fcm-ontology` description.
