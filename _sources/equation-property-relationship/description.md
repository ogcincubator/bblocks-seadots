An `EquationPropertyRelationship` is a specialised `PropertyRelationship` that records the
canonical equation calculating a derived indicator (`toProperty`) and the symbols inside it.
It supports two usage modes:

- **Equation-level (recommended for documentation)**: omit top-level `fromProperty`. The
  record describes the equation as a whole; `symbols[]` is the complete symbol table.
  Examples in this block use this mode.

- **Symbol-edge (sensitivity / cross-impact reading)**: include top-level `fromProperty`,
  matching exactly one entry in `symbols[]`. The record is then centred on that input,
  while still carrying the full table.

Use this block when the relationship is mathematical lineage. Use the existing
`property-relationship` block for weighted causal cross-impact edges, such as
`ind:floating-wind-reef-biomass -> indo:floating-wind-fish-abundance`.

Validation intent (partly enforced by `_sources/ontology/rules.shacl`):

- `equation` should be byte-identical to `schema:mathExpression` on the target Rainbow concept.
- every `symbols[].fromProperty` should be listed in `prov:wasDerivedFrom` on `toProperty`.
- each `symbols[].symbol` must occur literally inside `equation`.
- `symbols[].indexed: true` requires `toProperty` to declare an `:Aggregation`.
- when present, top-level `fromProperty` must match exactly one `symbols[].fromProperty`.
- `weight`, if present, represents sensitivity or coefficient value, not causal influence.

The `symbols[]` table is intentionally complete: every equation symbol is declared there,
making each record computationally self-contained.

Recommended symbol fields:

- `symbol` — the LaTeX symbol used in `equation` (e.g. `A_{sub}`, `D_{pre,i}`, `AF_i`, `C_t`).
- `symbolAliases` — ASCII or alternate renderings.
- `variableKind` — semantic role (`featureOfInterest`, `intensiveQuantity`, `adjustmentFactor`,
  `timeCoefficient`, `uncertaintyFactor`, …).
- `dimensionKind` — QUDT QuantityKind URI (unit-abstract).
- `bindings[]` — concrete Rainbow IRIs that realise the abstract `fromProperty`.
