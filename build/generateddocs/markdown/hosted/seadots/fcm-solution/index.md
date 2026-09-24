
# FCM solution (Schema)

`ogc.hosted.seadots.fcm-solution` *v0.1*

Result of iterating a fuzzy cognitive map to convergence: the equilibrium states found, their componentwise numerical spread, and whether the search succeeded. Source-faithful to the DeterministicFCMSolution struct of FuzzyCognitiveMapTools.jl.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### Single equilibrium of the researcher proposal map
#### json
```json
{
    "centroids": [
        [
            0.5,
            0.610639233949222,
            0.45667766616805705,
            0.5792448906757616,
            0.43431236020829006,
            0.4431620318453285,
            0.4682872146731508,
            0.5647806862111074,
            0.5975690903315223,
            0.6397024421278741
        ]
    ],
    "maxdists": [
        [
            0,
            0,
            1.3654966046772188e-11,
            1.0264566974171885e-11,
            2.4121760144879545e-11,
            7.42356176530734e-12,
            1.0557110741160614e-11,
            2.0290991109561674e-11,
            1.5049961277213697e-11,
            2.853928204871181e-11
        ]
    ],
    "b_success": true
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-solution/context.jsonld",
  "centroids": [
    [
      0.5,
      0.610639233949222,
      0.45667766616805705,
      0.5792448906757616,
      0.43431236020829006,
      0.4431620318453285,
      0.4682872146731508,
      0.5647806862111074,
      0.5975690903315223,
      0.6397024421278741
    ]
  ],
  "maxdists": [
    [
      0,
      0,
      1.3654966046772188e-11,
      1.0264566974171885e-11,
      2.4121760144879545e-11,
      7.42356176530734e-12,
      1.0557110741160614e-11,
      2.0290991109561674e-11,
      1.5049961277213697e-11,
      2.853928204871181e-11
    ]
  ],
  "b_success": true
}
```

#### ttl
```ttl
@prefix fcm: <https://w3id.org/ogc/hosted/seadots/fcm/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] fcm:hasFiniteEquilibria true .


```


### Two equilibria (synthetic)
#### json
```json
{
    "centroids": [
        [
            0.2,
            0.8
        ],
        [
            0.9,
            0.1
        ]
    ],
    "maxdists": [
        [
            0.0,
            1.0e-11
        ],
        [
            2.0e-11,
            0.0
        ]
    ],
    "b_success": true
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-solution/context.jsonld",
  "centroids": [
    [
      0.2,
      0.8
    ],
    [
      0.9,
      0.1
    ]
  ],
  "maxdists": [
    [
      0.0,
      1e-11
    ],
    [
      2e-11,
      0.0
    ]
  ],
  "b_success": true
}
```

#### ttl
```ttl
@prefix fcm: <https://w3id.org/ogc/hosted/seadots/fcm/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] fcm:hasFiniteEquilibria true .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: FCM solution
description: 'What iterating a fuzzy cognitive map to convergence produces. The solver
  runs many trials from random starting states, clusters the endpoints that land within
  tolerance of each other, and reports one representative point per cluster. `centroids`
  holds those representatives -- one per distinct equilibrium -- and `maxdists` the
  componentwise spread of the cluster each one stands for, as a rudimentary error
  bound.

  A solution is a digital-twin OUTPUT. It is index-aligned with the map that produced
  it: element i of every centroid is the value of the i-th vertex of that map, and
  the solution document itself carries no node identities. It is therefore not interpretable
  on its own; see description.md.

  '
type: object
required:
- centroids
- maxdists
- b_success
properties:
  centroids:
    type: array
    description: 'One entry per distinct equilibrium found. Each entry is a state
      vector: one value per concept node, in the vertex order of the map that was
      solved. Typically there is exactly one entry, but a map with several basins
      of attraction yields several.

      '
    items:
      $ref: '#/$defs/StateVector'
  maxdists:
    type: array
    description: 'Componentwise error bound for the correspondingly-indexed centroid:
      for each component, the spread (max - min) across the cluster of trial endpoints
      that centroid represents. Index-aligned with `centroids` element by element
      AND component by component.

      '
    items:
      $ref: '#/$defs/SpreadVector'
  b_success:
    type: boolean
    description: 'True when the map settles on finitely many discrete stable points.
      When false the solution carries no usable information and must be ignored.

      Note that no code path in upstream v0.1.0 ever sets this to false -- both constructors
      hardcode `true`. Treat a `true` here as "not yet contradicted" rather than as
      a positive assertion of convergence. See description.md.

      '
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/hasFiniteEquilibria
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
additionalProperties: false
allOf:
- if:
    properties:
      b_success:
        const: true
    required:
    - b_success
  then:
    properties:
      centroids:
        minItems: 1
      maxdists:
        minItems: 1
$defs:
  StateVector:
    type: array
    description: 'One value per concept node, positionally aligned with the vertex
      order of the map that was solved. `minItems: 2` follows from the upstream graph
      validator, which requires a map to have at least two vertices.

      '
    minItems: 2
    items:
      type: number
  SpreadVector:
    type: array
    description: 'Componentwise spread, positionally aligned with a state vector.
      Values are non-negative because each is computed as `maximum(...) - minimum(...)`
      over the cluster; the `minimum: 0` bound is derived from that construction rather
      than declared upstream.

      '
    minItems: 2
    items:
      type: number
      minimum: 0
x-jsonld-extra-terms:
  id: '@id'
  type: '@type'
x-jsonld-prefixes:
  fcm: https://w3id.org/ogc/hosted/seadots/fcm/
  xsd: http://www.w3.org/2001/XMLSchema#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-solution/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-solution/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "id": "@id",
    "type": "@type",
    "b_success": {
      "@id": "fcm:hasFiniteEquilibria",
      "@type": "xsd:boolean"
    },
    "fcm": "https://w3id.org/ogc/hosted/seadots/fcm/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-solution/context.jsonld)

## Sources

* [FuzzyCognitiveMapTools.jl v0.1.0](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl)
* [FCM data specifications (dataspecs/fcm_dataspecs__20260630.md)](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl/-/blob/main/dataspecs/fcm_dataspecs__20260630.md)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/_staging/fcm-solution`

