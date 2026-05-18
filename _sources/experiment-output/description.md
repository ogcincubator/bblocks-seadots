# Computational Experiment Output

OGC API Records profile for one output artefact produced by a computational experiment.

Each instance describes a single output — a primary result file, a catalog, or a provenance record. The schema is intentionally narrow so that an `experiment` record can reference many `experiment-output` records by URI and an audit pipeline can resolve each artefact independently.

Captured fields:

1. **Role** — `primary result`, `catalog`, `provenance`, `diagnostic`. Mirrors the `role` field on `experiment-input`.
2. **Format** — media type or URI for the artefact's format profile (e.g. `https://geoparquet.org/`, `application/ld+json`).
3. **Vocabulary term** — concept URI for the produced quantity (e.g. `floating-wind-reef-biomass`).
4. **CWL binding** — `cwlOutput` port name and the consuming experiment URI.
5. **Conformance** — optional list of conformance class URIs (e.g. the SeaDOTs EDITO output conventions, STAC version).

Outputs may be self-contained datasets, references to STAC collections, or PROV-O records that close the loop back to the experiment's inputs and the modelled equation.
