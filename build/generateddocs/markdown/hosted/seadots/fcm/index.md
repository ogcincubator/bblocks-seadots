
# Fuzzy Cognitive Map (Schema)

`ogc.hosted.seadots.fcm` *v0.1*

Source-faithful profile of a deterministic fuzzy cognitive map as serialised by FuzzyCognitiveMapTools.jl: a signed weighted digraph of concepts plus the activation specification that governs its update. Accepts the upstream edge-list form and the n x n adjacency form used by the wider FCM tool ecosystem.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### Researcher proposal toy map (edge-list form)
#### json
```json
{
    "graph": {
        "vertices": [
            {
                "id": "C1",
                "metadata": {
                    "description": "[C1] Proposal Deadline Nearness"
                }
            },
            {
                "id": "C2",
                "metadata": {
                    "description": "[C2] Stress Level"
                }
            },
            {
                "id": "C3",
                "metadata": {
                    "description": "[C3] Dark Chocolate Consumption"
                }
            },
            {
                "id": "C4",
                "metadata": {
                    "description": "[C4] Temporary Morale Boost"
                }
            },
            {
                "id": "C5",
                "metadata": {
                    "description": "[C5] Proposal Progress"
                }
            },
            {
                "id": "C6",
                "metadata": {
                    "description": "[C6] Sleep Quality"
                }
            },
            {
                "id": "C7",
                "metadata": {
                    "description": "[C7] Overthinking / Scope Creep"
                }
            },
            {
                "id": "C8",
                "metadata": {
                    "description": "[C8] Confidence That 'This Is a Great Idea'"
                }
            },
            {
                "id": "C9",
                "metadata": {
                    "description": "[C9] Likelihood of Creating Yet Another Figure"
                }
            },
            {
                "id": "C10",
                "metadata": {
                    "description": "[C10] Probability of Submitting on Time"
                }
            }
        ],
        "edges": [
            {
                "id": "C5->C3",
                "src": "C5",
                "dst": "C3",
                "weight": -0.4,
                "metadata": {
                    "description": "More progress reduces emergency dark chocolate consumption"
                }
            },
            {
                "id": "C2->C10",
                "src": "C2",
                "dst": "C10",
                "weight": 0.3,
                "metadata": {
                    "description": "Panic can, regrettably, improve on-time submission"
                }
            },
            {
                "id": "C1->C2",
                "src": "C1",
                "dst": "C2",
                "weight": 0.9,
                "metadata": {
                    "description": "Deadline nearness increases stress"
                }
            },
            {
                "id": "C3->C6",
                "src": "C3",
                "dst": "C6",
                "weight": -0.5,
                "metadata": {
                    "description": "Late chocolate reduces sleep quality"
                }
            },
            {
                "id": "C5->C10",
                "src": "C5",
                "dst": "C10",
                "weight": 0.9,
                "metadata": {
                    "description": "More progress increases the chance of submitting on time"
                }
            },
            {
                "id": "C9->C5",
                "src": "C9",
                "dst": "C5",
                "weight": -0.3,
                "metadata": {
                    "description": "Additional figure creation has a questionable net effect on progress"
                }
            },
            {
                "id": "C8->C9",
                "src": "C8",
                "dst": "C9",
                "weight": 0.7,
                "metadata": {
                    "description": "Confidence encourages creation of yet another figure"
                }
            },
            {
                "id": "C5->C8",
                "src": "C5",
                "dst": "C8",
                "weight": 0.6,
                "metadata": {
                    "description": "Progress boosts confidence"
                }
            },
            {
                "id": "C4->C5",
                "src": "C4",
                "dst": "C5",
                "weight": 0.5,
                "metadata": {
                    "description": "Higher morale improves proposal progress"
                }
            },
            {
                "id": "C6->C7",
                "src": "C6",
                "dst": "C7",
                "weight": -0.7,
                "metadata": {
                    "description": "Better sleep reduces overthinking and scope creep"
                }
            },
            {
                "id": "C2->C7",
                "src": "C2",
                "dst": "C7",
                "weight": 0.3,
                "metadata": {
                    "description": "Stress promotes overthinking and scope creep"
                }
            },
            {
                "id": "C7->C5",
                "src": "C7",
                "dst": "C5",
                "weight": -0.8,
                "metadata": {
                    "description": "Scope creep reduces genuine proposal progress"
                }
            },
            {
                "id": "C3->C4",
                "src": "C3",
                "dst": "C4",
                "weight": 0.7,
                "metadata": {
                    "description": "Dark chocolate provides a temporary morale boost"
                }
            },
            {
                "id": "C2->C3",
                "src": "C2",
                "dst": "C3",
                "weight": 0.2,
                "metadata": {
                    "description": "Stress increases dark chocolate consumption"
                }
            }
        ],
        "metadata": {
            "description": "Proposal-time scientist FCM with dark chocolate, stress, progress, and figure proliferation"
        }
    },
    "metadata": {},
    "activation_spec": {
        "mode": "homogeneous",
        "homogeneous": {
            "label": "logistic",
            "params": {
                "b": 0,
                "lambda": 1,
                "a": 1
            }
        }
    }
}
```


### Researcher proposal toy map (matrix form)
#### json
```json
{
  "matrix": {
    "nodes": [
      "C1",
      "C2",
      "C3",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10"
    ],
    "nodeLabels": {
      "C1": "[C1] Proposal Deadline Nearness",
      "C2": "[C2] Stress Level",
      "C3": "[C3] Dark Chocolate Consumption",
      "C4": "[C4] Temporary Morale Boost",
      "C5": "[C5] Proposal Progress",
      "C6": "[C6] Sleep Quality",
      "C7": "[C7] Overthinking / Scope Creep",
      "C8": "[C8] Confidence That 'This Is a Great Idea'",
      "C9": "[C9] Likelihood of Creating Yet Another Figure",
      "C10": "[C10] Probability of Submitting on Time"
    },
    "orientation": "source-major",
    "weights": [
      [
        0,
        0.9,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      [
        0,
        0,
        0.2,
        0,
        0,
        0,
        0.3,
        0,
        0,
        0.3
      ],
      [
        0,
        0,
        0,
        0.7,
        0,
        -0.5,
        0,
        0,
        0,
        0
      ],
      [
        0,
        0,
        0,
        0,
        0.5,
        0,
        0,
        0,
        0,
        0
      ],
      [
        0,
        0,
        -0.4,
        0,
        0,
        0,
        0,
        0.6,
        0,
        0.9
      ],
      [
        0,
        0,
        0,
        0,
        0,
        0,
        -0.7,
        0,
        0,
        0
      ],
      [
        0,
        0,
        0,
        0,
        -0.8,
        0,
        0,
        0,
        0,
        0
      ],
      [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0.7,
        0
      ],
      [
        0,
        0,
        0,
        0,
        -0.3,
        0,
        0,
        0,
        0,
        0
      ],
      [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ]
    ]
  },
  "activation_spec": {
    "mode": "homogeneous",
    "homogeneous": {
      "label": "logistic",
      "params": {
        "b": 0,
        "lambda": 1,
        "a": 1
      }
    }
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm/context.jsonld",
  "matrix": {
    "nodes": [
      "C1",
      "C2",
      "C3",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10"
    ],
    "nodeLabels": {
      "C1": "[C1] Proposal Deadline Nearness",
      "C2": "[C2] Stress Level",
      "C3": "[C3] Dark Chocolate Consumption",
      "C4": "[C4] Temporary Morale Boost",
      "C5": "[C5] Proposal Progress",
      "C6": "[C6] Sleep Quality",
      "C7": "[C7] Overthinking / Scope Creep",
      "C8": "[C8] Confidence That 'This Is a Great Idea'",
      "C9": "[C9] Likelihood of Creating Yet Another Figure",
      "C10": "[C10] Probability of Submitting on Time"
    },
    "orientation": "source-major",
    "weights": [
      [
        0,
        0.9,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      [
        0,
        0,
        0.2,
        0,
        0,
        0,
        0.3,
        0,
        0,
        0.3
      ],
      [
        0,
        0,
        0,
        0.7,
        0,
        -0.5,
        0,
        0,
        0,
        0
      ],
      [
        0,
        0,
        0,
        0,
        0.5,
        0,
        0,
        0,
        0,
        0
      ],
      [
        0,
        0,
        -0.4,
        0,
        0,
        0,
        0,
        0.6,
        0,
        0.9
      ],
      [
        0,
        0,
        0,
        0,
        0,
        0,
        -0.7,
        0,
        0,
        0
      ],
      [
        0,
        0,
        0,
        0,
        -0.8,
        0,
        0,
        0,
        0,
        0
      ],
      [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0.7,
        0
      ],
      [
        0,
        0,
        0,
        0,
        -0.3,
        0,
        0,
        0,
        0,
        0
      ],
      [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ]
    ]
  },
  "activation_spec": {
    "mode": "homogeneous",
    "homogeneous": {
      "label": "logistic",
      "params": {
        "b": 0,
        "lambda": 1,
        "a": 1
      }
    }
  }
}
```

#### ttl
```ttl
@prefix fcm: <https://w3id.org/ogc/hosted/seadots/fcm/> .
@prefix fcmact: <https://w3id.org/ogc/hosted/seadots/fcm/activation/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

[] fcm:hasActivationSpec [ fcm:activationMode fcm:homogeneousActivation ;
            fcm:homogeneousActivation [ fcm:activationFunction fcmact:logistic ] ] ;
    fcm:hasMatrix [ fcm:matrixNodes ( <file:///github/workspace/C1> <file:///github/workspace/C2> <file:///github/workspace/C3> <file:///github/workspace/C4> <file:///github/workspace/C5> <file:///github/workspace/C6> <file:///github/workspace/C7> <file:///github/workspace/C8> <file:///github/workspace/C9> <file:///github/workspace/C10> ) ;
            fcm:matrixOrientation <file:///github/workspace/source-major> ] .


```


### Minimal heterogeneous-activation map (synthetic)
#### json
```json
{
  "graph": {
    "vertices": [
      {
        "id": "A",
        "metadata": {
          "description": "[A] Synthetic driver concept"
        }
      },
      {
        "id": "B",
        "metadata": {
          "description": "[B] Synthetic responding concept"
        }
      }
    ],
    "edges": [
      {
        "id": "A->B",
        "src": "A",
        "dst": "B",
        "weight": 0.5,
        "metadata": {
          "description": "Synthetic edge; the value carries no empirical meaning."
        }
      },
      {
        "id": "B->A",
        "src": "B",
        "dst": "A",
        "weight": -0.25,
        "metadata": {
          "description": "Synthetic feedback edge; the value carries no empirical meaning."
        }
      }
    ],
    "metadata": {
      "description": "Synthetic two-concept map, the smallest graph the upstream validator accepts."
    }
  },
  "metadata": {
    "description": "SYNTHETIC. Constructed to exercise heterogeneous activation; not derived from any survey or observation."
  },
  "activation_spec": {
    "mode": "heterogeneous",
    "heterogeneous": [
      {
        "label": "logistic",
        "params": {
          "b": 0,
          "lambda": 1,
          "a": 1
        }
      },
      {
        "label": "gaussian",
        "params": {
          "b": 0,
          "lambda": 1,
          "a": 1
        }
      }
    ]
  }
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Fuzzy Cognitive Map
description: 'Source-faithful profile of a deterministic fuzzy cognitive map as serialised
  by FuzzyCognitiveMapTools.jl: a signed weighted digraph of concepts together with
  the activation specification that governs its iterative update. The activation specification
  is part of the map, not of the run that consumes it, so a map is a self-contained
  digital-twin input.

  Two interchangeable representations of the same map are accepted, and exactly one
  must be present. `graph` is the upstream edge-list form. `matrix` is the n x n adjacency
  form used by the wider FCM tool ecosystem (FCMpy, Mental Modeler, FCMapper); it
  is lossless against the edge list only because the node ordering is declared explicitly
  rather than implied.

  '
type: object
required:
- activation_spec
oneOf:
- required:
  - graph
  not:
    required:
    - matrix
- required:
  - matrix
  not:
    required:
    - graph
properties:
  graph:
    $ref: '#/$defs/ConceptGraph'
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/hasGraph
  matrix:
    $ref: '#/$defs/WeightMatrix'
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/hasMatrix
  activation_spec:
    $ref: '#/$defs/ActivationSpec'
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/hasActivationSpec
    x-jsonld-extra-terms:
      label:
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/activationFunction
        x-jsonld-type: '@vocab'
      logistic: https://w3id.org/ogc/hosted/seadots/fcm/activation/logistic
      gaussian: https://w3id.org/ogc/hosted/seadots/fcm/activation/logistic-of-square
      other: https://w3id.org/ogc/hosted/seadots/fcm/activation/offset
      tanh: https://w3id.org/ogc/hosted/seadots/fcm/activation/hyperbolic-tangent
      bivalent: https://w3id.org/ogc/hosted/seadots/fcm/activation/bivalent
      trivalent: https://w3id.org/ogc/hosted/seadots/fcm/activation/trivalent
  metadata:
    $ref: '#/$defs/MapMetadata'
    x-jsonld-id: '@nest'
additionalProperties: false
$defs:
  MapMetadata:
    type: object
    description: 'Map-level metadata. A placeholder upstream, where only `description`
      is defined; discovery metadata belongs in the accompanying catalog record, not
      here.

      '
    properties:
      description:
        type: string
        x-jsonld-id: http://purl.org/dc/terms/description
    additionalProperties: true
  VertexMetadata:
    type: object
    description: Vertex-level metadata.
    properties:
      description:
        type: string
        description: 'Human-readable name of the concept, conventionally prefixed
          with the node key in square brackets, e.g. "[C2] Stress Level". Despite
          the field name this is a label rather than a description, and is mapped
          to skos:prefLabel.

          '
        x-jsonld-id: http://purl.org/dc/terms/description
    additionalProperties: true
  EdgeMetadata:
    type: object
    description: Edge-level metadata.
    properties:
      description:
        type: string
        description: Free-text statement of the causal claim the edge encodes.
        x-jsonld-id: http://purl.org/dc/terms/description
      provenance:
        type: string
        description: 'Free-text statement of where the weight came from. Marked as
          temporary upstream; expected to become a structured reference to the elicitation
          record (see description.md).

          '
    additionalProperties: true
  GraphMetadata:
    type: object
    description: Graph-level metadata.
    properties:
      description:
        type: string
        x-jsonld-id: http://purl.org/dc/terms/description
    additionalProperties: true
  Vertex:
    type: object
    description: One concept of the map.
    required:
    - id
    properties:
      id:
        type: string
        minLength: 1
        description: 'Graph-local key of the concept, unique within the map, e.g.
          "C1" or "Nd". Referenced by the `src` and `dst` fields of edges. Not an
          IRI; the concept IRI, when known, belongs in the catalog record or in a
          future `concept` field (see description.md).

          '
        x-jsonld-id: '@id'
      metadata:
        $ref: '#/$defs/VertexMetadata'
        x-jsonld-id: '@nest'
    additionalProperties: false
  Edge:
    type: object
    description: One directed, weighted causal influence between two concepts.
    required:
    - src
    - dst
    - weight
    properties:
      id:
        type: string
        description: Optional graph-local key of the edge, conventionally "SRC->DST".
        x-jsonld-id: '@id'
      src:
        type: string
        minLength: 1
        description: Key of the driving concept. Must equal the `id` of a vertex of
          the same map.
      dst:
        type: string
        minLength: 1
        description: Key of the influenced concept. Must equal the `id` of a vertex
          of the same map.
      weight:
        type: number
        description: 'Signed strength of the influence. Conventionally dimensionless
          in [-1, 1]; the convention is documented but NOT enforced upstream, and
          is not enforced here either. See description.md.

          '
      metadata:
        $ref: '#/$defs/EdgeMetadata'
        x-jsonld-id: '@nest'
    additionalProperties: false
  ConceptGraph:
    type: object
    description: 'Edge-list representation. The upstream validator additionally requires
      that every `src`/`dst` resolves to a vertex of the same graph and that no vertex
      is left unconnected; neither is expressible in JSON Schema across sibling arrays
      and both are carried as SHACL constraints by ogc.hosted.seadots.fcm-ontology.

      '
    required:
    - vertices
    - edges
    properties:
      vertices:
        type: array
        minItems: 2
        items:
          $ref: '#/$defs/Vertex'
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/hasNode
        x-jsonld-container: '@set'
      edges:
        type: array
        minItems: 1
        items:
          $ref: '#/$defs/Edge'
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/hasEdge
        x-jsonld-container: '@set'
      metadata:
        $ref: '#/$defs/GraphMetadata'
        x-jsonld-id: '@nest'
    additionalProperties: false
  WeightMatrix:
    type: object
    description: 'Adjacency representation. `nodes` declares the ordering that both
      axes of `weights` follow, so the matrix is self-describing rather than depending
      on the order of an external vertex list.

      '
    required:
    - nodes
    - weights
    - orientation
    properties:
      nodes:
        type: array
        minItems: 2
        description: Node keys, in the order used by both axes of `weights`.
        items:
          type: string
          minLength: 1
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/matrixNodes
        x-jsonld-type: '@id'
        x-jsonld-container: '@list'
      nodeLabels:
        type: object
        description: Optional map from node key to human-readable label.
        additionalProperties:
          type: string
      orientation:
        const: source-major
        description: 'Declares that weights[i][j] is the influence of nodes[i] ON
          nodes[j]. Stated as a required constant rather than assumed, because the
          opposite convention is equally common and silently transposes the entire
          model. The solver applies the transpose at iteration time, computing f(W''
          x).

          '
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/matrixOrientation
        x-jsonld-type: '@vocab'
      weights:
        type: array
        minItems: 2
        description: Square matrix of signed weights; absent influences are 0.
        items:
          type: array
          minItems: 2
          items:
            type: number
    additionalProperties: false
  ActivationFunctionSpec:
    type: object
    description: 'One activation (transfer) function together with its numeric parameters.
      `label` is the discriminator.

      '
    required:
    - label
    - params
    properties:
      label:
        type: string
        description: 'Function name as serialised upstream. Values are resolved to
          concepts of ogc.hosted.seadots.fcm-activation-scheme by context.jsonld.
          Note that the upstream label "gaussian" resolves to fcmact:logistic-of-square,
          which is what the implementation computes; see that block''s description.

          '
        examples:
        - logistic
        - gaussian
        - other
      params:
        type: object
        description: 'Numeric parameters keyed by name. Which names are meaningful
          depends on `label` and is declared by fcmact:hasParameterName on the corresponding
          concept (`a`, `b`, `lambda` for the implemented functions).

          '
        additionalProperties:
          type: number
    additionalProperties: false
  ActivationSpec:
    type: object
    description: 'Whether one activation function governs the whole map or one per
      concept. In heterogeneous mode the array is positional: element k applies to
      vertex k of `graph.vertices`, or to `matrix.nodes[k]`.

      '
    required:
    - mode
    properties:
      mode:
        enum:
        - homogeneous
        - heterogeneous
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/activationMode
        x-jsonld-type: '@vocab'
      homogeneous:
        $ref: '#/$defs/ActivationFunctionSpec'
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/homogeneousActivation
      heterogeneous:
        type: array
        minItems: 1
        items:
          $ref: '#/$defs/ActivationFunctionSpec'
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/heterogeneousActivation
        x-jsonld-container: '@list'
    additionalProperties: false
    allOf:
    - if:
        properties:
          mode:
            const: homogeneous
        required:
        - mode
      then:
        required:
        - homogeneous
        not:
          required:
          - heterogeneous
    - if:
        properties:
          mode:
            const: heterogeneous
        required:
        - mode
      then:
        required:
        - heterogeneous
        not:
          required:
          - homogeneous
x-jsonld-extra-terms:
  id: '@id'
  type: '@type'
x-jsonld-prefixes:
  fcm: https://w3id.org/ogc/hosted/seadots/fcm/
  skos: http://www.w3.org/2004/02/skos/core#
  qudt: http://qudt.org/schema/qudt/
  xsd: http://www.w3.org/2001/XMLSchema#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  prov: http://www.w3.org/ns/prov#
  dct: http://purl.org/dc/terms/
  fcmact: https://w3id.org/ogc/hosted/seadots/fcm/activation/
  prop-rel: https://w3id.org/ogc/hosted/seadots/prop-rel/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "id": "@id",
    "type": "@type",
    "graph": {
      "@context": {
        "vertices": {
          "@id": "fcm:hasNode",
          "@container": "@set"
        },
        "edges": {
          "@id": "fcm:hasEdge",
          "@container": "@set"
        }
      },
      "@id": "fcm:hasGraph"
    },
    "matrix": {
      "@context": {
        "nodes": {
          "@id": "fcm:matrixNodes",
          "@type": "@id",
          "@container": "@list"
        },
        "orientation": {
          "@id": "fcm:matrixOrientation",
          "@type": "@vocab"
        }
      },
      "@id": "fcm:hasMatrix"
    },
    "activation_spec": {
      "@context": {
        "mode": {
          "@id": "fcm:activationMode",
          "@type": "@vocab"
        },
        "homogeneous": "fcm:homogeneousActivation",
        "heterogeneous": {
          "@id": "fcm:heterogeneousActivation",
          "@container": "@list"
        },
        "label": {
          "@id": "fcm:activationFunction",
          "@type": "@vocab"
        },
        "logistic": "fcm:activation/logistic",
        "gaussian": "fcm:activation/logistic-of-square",
        "other": "fcm:activation/offset",
        "tanh": "fcm:activation/hyperbolic-tangent",
        "bivalent": "fcm:activation/bivalent",
        "trivalent": "fcm:activation/trivalent"
      },
      "@id": "fcm:hasActivationSpec"
    },
    "description": "dct:description",
    "metadata": "@nest",
    "fcm": "https://w3id.org/ogc/hosted/seadots/fcm/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "qudt": "http://qudt.org/schema/qudt/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "prov": "http://www.w3.org/ns/prov#",
    "dct": "http://purl.org/dc/terms/",
    "fcmact": "fcm:activation/",
    "prop-rel": "https://w3id.org/ogc/hosted/seadots/prop-rel/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm/context.jsonld)

## Sources

* [FuzzyCognitiveMapTools.jl v0.1.0](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl)
* [FCM data specifications (dataspecs/fcm_dataspecs__20260630.md)](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl/-/blob/main/dataspecs/fcm_dataspecs__20260630.md)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/_staging/fcm`

