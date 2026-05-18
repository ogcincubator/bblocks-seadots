# Computational Experiment Input

OGC API Records profile for one input artefact that can be consumed by one or more computational experiments.

The record is **experiment-agnostic**: it describes the artefact (what it is, where it lives, what concept it represents) but does not commit to any specific equation symbol, CWL input port, or experiment URI. Those bindings live on the consuming `experiment` record so that the same input can be referenced from multiple experiments without edit.

Captured fields:

1. **Role** — generic role of the artefact: `AOI`, `feature-of-interest geometry`, `primary baseline`, `fallback baseline`, `coefficient (per taxon)`, `coefficient (scalar)`, `scenario parameter`.
2. **Source and format** — access URI plus media type. For sources that resolve to another bblock record, the URI MUST resolve and `format` SHOULD be `application/ld+json`.
3. **Vocabulary term** — authoritative concept URI for the underlying quantity.

The consuming `experiment` record's `inputs[]` carries the wiring: each entry references an `experiment-input` URI and adds `equationBinding` (e.g. `A_{sub}`, `D_{pre,i}`, `AF_i`, `C_t`, or omitted) plus `cwlInput` (the workflow port the artefact is fed into).

## Vocabulary priority

For `vocabularyTerm`: NERC > CF > Darwin Core > OBIS > ICES > EMODnet > schema.org.
