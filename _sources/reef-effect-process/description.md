# Reef Effect Process

OGC API Processes Part 1 process description for the reef-effect biomass calculation, aligned with the OSPD profile (`ogc.osc.api-profiles.processes.ospd`).

The block wraps the deterministic reproducibility script `_sources/reef-effect/scripts/utsira_reef_biomass.py` as an executable Process. Its inputs and outputs are typed by per-class SeaDOTs building blocks rather than primitive JSON Schemas, so the process is declaratively wired to the same records that the `reef-effect` experiment record links by URI.

## Why a separate block

The `reef-effect` block is an OGC API Records profile that describes the experiment as a discoverable resource (purpose, ODD, equation, success criteria, inputs/outputs by URI). It is the descriptive record.

`reef-effect-process` is the executable counterpart: a process description that an OGC API Processes endpoint can serve at `GET /processes/utsira-reef-biomass` and that clients can invoke at `POST /processes/utsira-reef-biomass/execution`. The two blocks complement each other and the experiment Record SHOULD reference the process by URI once both are deployed.

## Composition

The schema is composed using upstream OGC API Processes building blocks (register `bblocks-ogcapi-processes`):

| Aspect | Source |
|---|---|
| Process summary (id, version, title, description, keywords, jobControlOptions, outputTransmission, links) | `bblocks://ogc.api.processes.v1.schemas.processSummary` |
| Each input description (title, description, minOccurs, maxOccurs, schema) | `bblocks://ogc.api.processes.v1.schemas.inputDescription` |
| Each output description (title, description, schema) | `bblocks://ogc.api.processes.v1.schemas.outputDescription` |

Following the OSPD `buffer-geometry` pattern, every input/output `schema` is a `bblocks://` reference to the JSON Schema of the corresponding per-class record:

| Input id | Equation symbol | Bound to bblock |
|---|---|---|
| `aoi` | — | `ogc.hosted.seadots.area-of-interest` |
| `infrastructure` | A_sub | `ogc.hosted.seadots.floating-wind-infrastructure` |
| `benthicBiomassPrimary` | D_pre,i | `ogc.hosted.seadots.benthic-biomass-density-mareano` |
| `benthicBiomassFallback` | D_pre,i (fallback) | `ogc.hosted.seadots.benthic-biomass-density-imr` |
| `reefAggregationIndex` | AF_i | `ogc.hosted.seadots.reef-aggregation-index` |
| `colonisationTimeFactor` | C_t | `ogc.hosted.seadots.colonisation-time-factor` |
| `asOfMonths` | t | inline scalar (integer, default 24) |

| Output id | Bound to bblock |
|---|---|
| `reefBiomassResult` | `ogc.hosted.seadots.reef-effect-output` |
| `provenance` | inline `application/ld+json` PROV-O record |

## Execution unit

The `executionUnit` link in the process description points at the script:

```
_sources/reef-effect/scripts/utsira_reef_biomass.py
```

with `type: text/x-python`. The example process description declares `language: python`, `languageVersion: ">=3.9"`, and the exact `entrypoint` command. The script is deterministic (closed-form equation), so `reproducibility.seedPolicy: deterministic`.

## What the process emits

Successful execution produces a `reef-effect-output` record carrying:

- `headline.B_reef_kg`, `sigma_kg`, `CV`, 95% CI;
- `perTaxonAtT24` — per-taxon contributions;
- `timeSeries` — B_reef at the C(t) lookup points;
- `uncertainty.varianceAttribution` — share of CV² across A_sub, C_t, S=Σ(D·AF).

The `provenance` output is a PROV-O record linking the run to the six per-class input records, the equation record, and the ODD record by URI.

## Examples

- `examples/utsira_reef_biomass_process.json` — the **process description** document (validated against this bblock's schema).
- `examples/utsira_reef_biomass_execute.json` — a **matching Execute request body** for `POST /processes/utsira-reef-biomass/execution`. It conforms to OGC API Processes `execute.yaml`, not to this bblock's schema, so it is shipped as documentation only and is not validated here. A future companion bblock (mirroring `ogc.osc.api-profiles.processes.ipt.execute`) can wrap it as a schema.
