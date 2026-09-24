
# FCM sequence (Schema)

`ogc.hosted.seadots.fcm-sequence` *v0.1*

A time-indexed series of fuzzy cognitive maps and the solutions computed from them: how the causal structure a stakeholder group describes, and the equilibria it implies, change over successive elicitation rounds. Source-faithful to the DeterministicFCMSequence struct of FuzzyCognitiveMapTools.jl.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### Six weeks of the researcher proposal map
#### json
```json
{
    "timespec_series": [
        {
            "type": "weekofyeartimespec",
            "year": 2026,
            "week": 19
        },
        {
            "type": "weekofyeartimespec",
            "year": 2026,
            "week": 20
        },
        {
            "type": "weekofyeartimespec",
            "year": 2026,
            "week": 21
        },
        {
            "type": "weekofyeartimespec",
            "year": 2026,
            "week": 22
        },
        {
            "type": "weekofyeartimespec",
            "year": 2026,
            "week": 23
        },
        {
            "type": "weekofyeartimespec",
            "year": 2026,
            "week": 24
        }
    ],
    "fcm_series": [
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
                        "weight": 0,
                        "metadata": {
                            "description": "Stress increases dark chocolate consumption"
                        }
                    }
                ],
                "metadata": {
                    "description": "Proposal-time scientist FCM with dark chocolate, stress, progress, and figure proliferation"
                }
            },
            "metadata": {
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
        },
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
            "metadata": {
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
        },
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
                        "weight": 0.4,
                        "metadata": {
                            "description": "Stress increases dark chocolate consumption"
                        }
                    }
                ],
                "metadata": {
                    "description": "Proposal-time scientist FCM with dark chocolate, stress, progress, and figure proliferation"
                }
            },
            "metadata": {
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
        },
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
                        "weight": 0.7,
                        "metadata": {
                            "description": "Stress increases dark chocolate consumption"
                        }
                    }
                ],
                "metadata": {
                    "description": "Proposal-time scientist FCM with dark chocolate, stress, progress, and figure proliferation"
                }
            },
            "metadata": {
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
        },
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
                        "weight": 0.8,
                        "metadata": {
                            "description": "Stress increases dark chocolate consumption"
                        }
                    }
                ],
                "metadata": {
                    "description": "Proposal-time scientist FCM with dark chocolate, stress, progress, and figure proliferation"
                }
            },
            "metadata": {
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
        },
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
                        "weight": 0.9,
                        "metadata": {
                            "description": "Stress increases dark chocolate consumption"
                        }
                    }
                ],
                "metadata": {
                    "description": "Proposal-time scientist FCM with dark chocolate, stress, progress, and figure proliferation"
                }
            },
            "metadata": {
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
    ],
    "solution_series": [
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
        },
        {
            "centroids": [
                [
                    0.5,
                    0.610639233949222,
                    0.4870529858088966,
                    0.5844181353422656,
                    0.4348187071396313,
                    0.4394174858584556,
                    0.4689399279790245,
                    0.5648553618382783,
                    0.5975816608780322,
                    0.6398074694671319
                ]
            ],
            "maxdists": [
                [
                    0,
                    0,
                    1.4616363674946342e-11,
                    9.986012017293433e-12,
                    2.6247726214734257e-11,
                    7.234268739608751e-12,
                    1.0328848887297681e-11,
                    2.157030110083724e-11,
                    1.4591439168043507e-11,
                    3.033617801406763e-11
                ]
            ],
            "b_success": true
        },
        {
            "centroids": [
                [
                    0.5,
                    0.610639233949222,
                    0.5175242704106572,
                    0.5895890972538819,
                    0.4353247208507303,
                    0.4356680270919343,
                    0.46959360413050943,
                    0.564929985382611,
                    0.5975942225290533,
                    0.639912414320346
                ]
            ],
            "maxdists": [
                [
                    0,
                    0,
                    1.343658517782842e-11,
                    1.0514034087805157e-11,
                    2.5167146144866592e-11,
                    7.630729381702395e-12,
                    1.0438094832920797e-11,
                    1.9839241360841697e-11,
                    1.5427992217098563e-11,
                    2.789923847501541e-11
                ]
            ],
            "b_success": true
        },
        {
            "centroids": [
                [
                    0.5,
                    0.610639233949222,
                    0.562919090047955,
                    0.5972556765202262,
                    0.4360747117808305,
                    0.43009598553435724,
                    0.47056521926543216,
                    0.5650405836553745,
                    0.5976128397005995,
                    0.6400679342947546
                ]
            ],
            "maxdists": [
                [
                    0,
                    0,
                    1.455802145500229e-11,
                    1.0294209928929376e-11,
                    2.527777986927049e-11,
                    7.492784170892719e-12,
                    1.0007772388576086e-11,
                    2.1813106876322763e-11,
                    1.5419776566716337e-11,
                    3.067091025599211e-11
                ]
            ],
            "b_success": true
        },
        {
            "centroids": [
                [
                    0.5,
                    0.610639233949222,
                    0.5778572179561533,
                    0.5997683643345215,
                    0.4363204491156591,
                    0.4282661815383021,
                    0.47088433720485207,
                    0.5650768201857603,
                    0.5976189393883914,
                    0.6401188846020557
                ]
            ],
            "maxdists": [
                [
                    0,
                    0,
                    1.1699308188894975e-11,
                    1.0131562255821791e-11,
                    2.598132819997545e-11,
                    7.381872890732666e-12,
                    9.783507337601804e-12,
                    1.7680634734063005e-11,
                    1.5338175174406388e-11,
                    2.4859225788986805e-11
                ]
            ],
            "b_success": true
        },
        {
            "centroids": [
                [
                    0.5,
                    0.610639233949222,
                    0.5926545242277057,
                    0.6022522020584374,
                    0.4365633284265874,
                    0.4264555590227452,
                    0.47120013332343164,
                    0.5651126345874508,
                    0.5976249679896642,
                    0.6401692392339768
                ]
            ],
            "maxdists": [
                [
                    0,
                    0,
                    1.3866574555265743e-11,
                    9.784395516021505e-12,
                    2.4658441954983346e-11,
                    7.136180535383119e-12,
                    9.71445146547012e-12,
                    2.1174062503348523e-11,
                    1.4998557951173552e-11,
                    2.97699642715088e-11
                ]
            ],
            "b_success": true
        }
    ]
}
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: FCM sequence
description: 'A time-indexed series of fuzzy cognitive maps together with the solutions
  computed from them: how the causal structure a stakeholder group describes, and
  the equilibria that structure implies, change over successive elicitation rounds.

  The serialisation is three PARALLEL ARRAYS rather than an array of steps. Whatever
  sits at index k of each is one (time, map, solution) triple; the upstream author
  notes this shape was chosen to make plotting easier. Position is therefore the only
  thing binding a step together, and the three arrays must be the same length -- an
  invariant JSON Schema cannot state. See description.md.

  '
type: object
required:
- timespec_series
- fcm_series
- solution_series
properties:
  timespec_series:
    type: array
    minItems: 1
    description: 'When each step applies. Must be pairwise non-overlapping, or the
      sequence cannot be ordered at all -- see description.md.

      '
    items:
      $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-timespec/schema.yaml
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/timeSpecSeries
    x-jsonld-container: '@list'
    x-jsonld-extra-terms:
      pointtimespec: https://w3id.org/ogc/hosted/seadots/fcm/PointTimeSpec
      weekofyeartimespec: https://w3id.org/ogc/hosted/seadots/fcm/WeekOfYearTimeSpec
      monthofyeartimespec: https://w3id.org/ogc/hosted/seadots/fcm/MonthOfYearTimeSpec
      rangetimespec: https://w3id.org/ogc/hosted/seadots/fcm/RangeTimeSpec
      dt:
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/instant
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
      year:
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/year
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
      week:
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/week
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
      month:
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/month
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
      start:
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/intervalStart
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
      stop:
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/intervalStop
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  fcm_series:
    type: array
    minItems: 1
    description: 'The map that held at each step. Repeating a structurally identical
      map at every step is normal; what usually changes between steps is a handful
      of edge weights.

      '
    items:
      $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm/schema.yaml
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/mapSeries
    x-jsonld-container: '@list'
    x-jsonld-extra-terms:
      graph:
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/hasGraph
        x-jsonld-context:
          '@type': https://w3id.org/ogc/hosted/seadots/fcm/ConceptGraph
          vertices:
            '@id': https://w3id.org/ogc/hosted/seadots/fcm/hasNode
            '@container': '@set'
            '@context':
              '@type': https://w3id.org/ogc/hosted/seadots/fcm/ConceptNode
              metadata:
                '@id': '@nest'
                '@context':
                  description: http://www.w3.org/2004/02/skos/core#prefLabel
          edges:
            '@id': https://w3id.org/ogc/hosted/seadots/fcm/hasEdge
            '@container': '@set'
            '@context':
              '@type': https://w3id.org/ogc/hosted/seadots/fcm/InfluenceEdge
              src:
                '@id': https://w3id.org/ogc/hosted/seadots/fcm/sourceNode
                '@type': '@id'
              dst:
                '@id': https://w3id.org/ogc/hosted/seadots/fcm/targetNode
                '@type': '@id'
              weight:
                '@id': http://qudt.org/schema/qudt/numericValue
                '@type': http://www.w3.org/2001/XMLSchema#double
              metadata:
                '@id': '@nest'
                '@context':
                  description: http://www.w3.org/2000/01/rdf-schema#comment
                  provenance: http://www.w3.org/ns/prov#wasDerivedFrom
              id: https://w3id.org/ogc/hosted/seadots/fcm/edgeKey
          metadata:
            '@id': '@nest'
            '@context':
              description: http://purl.org/dc/terms/description
      activation_spec:
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/hasActivationSpec
        x-jsonld-context:
          '@type': https://w3id.org/ogc/hosted/seadots/fcm/ActivationSpec
          mode:
            '@id': https://w3id.org/ogc/hosted/seadots/fcm/activationMode
            '@type': '@vocab'
            '@context':
              homogeneous: https://w3id.org/ogc/hosted/seadots/fcm/Homogeneous
              heterogeneous: https://w3id.org/ogc/hosted/seadots/fcm/Heterogeneous
          homogeneous: https://w3id.org/ogc/hosted/seadots/fcm/homogeneousActivation
          heterogeneous:
            '@id': https://w3id.org/ogc/hosted/seadots/fcm/heterogeneousActivation
            '@container': '@list'
          label:
            '@id': https://w3id.org/ogc/hosted/seadots/fcm/activationFunction
            '@type': '@vocab'
          logistic: https://w3id.org/ogc/hosted/seadots/fcm/activation/logistic
          gaussian: https://w3id.org/ogc/hosted/seadots/fcm/activation/logistic-of-square
          other: https://w3id.org/ogc/hosted/seadots/fcm/activation/offset
          tanh: https://w3id.org/ogc/hosted/seadots/fcm/activation/hyperbolic-tangent
          bivalent: https://w3id.org/ogc/hosted/seadots/fcm/activation/bivalent
          trivalent: https://w3id.org/ogc/hosted/seadots/fcm/activation/trivalent
      metadata:
        x-jsonld-id: '@nest'
        x-jsonld-context:
          description: http://purl.org/dc/terms/description
      matrix:
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/hasMatrix
        x-jsonld-context:
          nodes:
            '@id': https://w3id.org/ogc/hosted/seadots/fcm/matrixNodes
            '@type': '@id'
            '@container': '@list'
          orientation:
            '@id': https://w3id.org/ogc/hosted/seadots/fcm/matrixOrientation
            '@type': '@vocab'
            '@context':
              source-major: https://w3id.org/ogc/hosted/seadots/fcm/SourceMajor
  solution_series:
    type: array
    minItems: 1
    description: 'The solution computed from the map at the same index. A step''s
      solution is index-aligned with its own map''s vertex order, not with any other
      step''s.

      '
    items:
      $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-solution/schema.yaml
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/solutionSeries
    x-jsonld-container: '@list'
    x-jsonld-extra-terms:
      b_success:
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/hasFiniteEquilibria
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
additionalProperties: false
x-jsonld-extra-terms:
  id: '@id'
  type: '@type'
x-jsonld-prefixes:
  fcm: https://w3id.org/ogc/hosted/seadots/fcm/
  xsd: http://www.w3.org/2001/XMLSchema#
  skos: http://www.w3.org/2004/02/skos/core#
  qudt: http://qudt.org/schema/qudt/
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  prov: http://www.w3.org/ns/prov#
  dct: http://purl.org/dc/terms/
  fcmact: https://w3id.org/ogc/hosted/seadots/fcm/activation/
  prop-rel: https://w3id.org/ogc/hosted/seadots/prop-rel/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-sequence/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-sequence/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "id": "@id",
    "type": "@type",
    "timespec_series": {
      "@context": {
        "dt": {
          "@id": "fcm:instant",
          "@type": "xsd:dateTime"
        },
        "year": {
          "@id": "fcm:year",
          "@type": "xsd:integer"
        },
        "week": {
          "@id": "fcm:week",
          "@type": "xsd:integer"
        },
        "month": {
          "@id": "fcm:month",
          "@type": "xsd:integer"
        },
        "start": {
          "@id": "fcm:intervalStart",
          "@type": "xsd:dateTime"
        },
        "stop": {
          "@id": "fcm:intervalStop",
          "@type": "xsd:dateTime"
        }
      },
      "@id": "fcm:timeSpecSeries",
      "@container": "@list"
    },
    "fcm_series": {
      "@context": {
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
        "metadata": "@nest"
      },
      "@id": "fcm:mapSeries",
      "@container": "@list"
    },
    "solution_series": {
      "@context": {
        "b_success": {
          "@id": "fcm:hasFiniteEquilibria",
          "@type": "xsd:boolean"
        }
      },
      "@id": "fcm:solutionSeries",
      "@container": "@list"
    },
    "pointtimespec": "fcm:PointTimeSpec",
    "weekofyeartimespec": "fcm:WeekOfYearTimeSpec",
    "monthofyeartimespec": "fcm:MonthOfYearTimeSpec",
    "rangetimespec": "fcm:RangeTimeSpec",
    "fcm": "https://w3id.org/ogc/hosted/seadots/fcm/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "qudt": "http://qudt.org/schema/qudt/",
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
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-sequence/context.jsonld)

## Sources

* [FuzzyCognitiveMapTools.jl v0.1.0](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl)
* [FCM data specifications (dataspecs/fcm_dataspecs__20260630.md)](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl/-/blob/main/dataspecs/fcm_dataspecs__20260630.md)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/_staging/fcm-sequence`

