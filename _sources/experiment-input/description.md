# Computational Experiment Input

OGC API Records profile for one input artefact that can be consumed by one or more computational experiments.

The record is **experiment-agnostic**: it describes the artefact (what it is, where it lives, what concept it represents) but does not commit to any specific equation symbol, CWL input port, or experiment URI. Those bindings live on the consuming `experiment` record so that the same input can be referenced from multiple experiments without edit.

Captured fields:

1. **Role** — generic role of the artefact: `AOI`, `feature-of-interest geometry`, `primary baseline`, `fallback baseline`, `coefficient (per taxon)`, `coefficient (scalar)`, `scenario parameter`.
2. **Source and format** — access URI plus media type for the canonical / full dataset. For sources that resolve to another bblock record, the URI MUST resolve and `format` SHOULD be `application/ld+json`.
3. **Vocabulary term** — authoritative concept URI for the underlying quantity.
4. **Inline data values** — every example MUST embed representative sample values inside the `data` object so a reader can see what shape the input actually has. For per-taxon inputs (densities, AF_i), use a `perTaxon` array keyed by `scientificName`. For scalar / sigmoid inputs, include the parameters and an evaluated lookup table. Pure geographic inputs (AOI) MAY rely on the top-level `geometry` field and omit `data`. Treat `source` as the canonical / full dataset URI; treat `data` as the representative sample a reader needs without leaving the record.
5. **`data.provenance` — required when `data` is present** — every `data` block MUST carry a `provenance` sibling that documents where the values came from. Mandatory `values` field: `retrieved` (cite the precise API call URL and verification date), `illustrative` (clearly label the values as not measurements, and link the closest real source under `nearestAuthoritativeSource` for orientation), or `mixed` (per-row sources called out in-line). Plausible-looking numbers without provenance read as real measurements and corrupt downstream pipelines — this is non-negotiable.

The consuming `experiment` record's `inputs[]` carries the wiring: each entry references an `experiment-input` URI and adds `equationBinding` (e.g. `A_{sub}`, `D_{pre,i}`, `AF_i`, `C_t`, or omitted) plus `cwlInput` (the workflow port the artefact is fed into).

## Vocabulary priority

For `vocabularyTerm`: NERC > CF > Darwin Core > OBIS > ICES > EMODnet > schema.org.
