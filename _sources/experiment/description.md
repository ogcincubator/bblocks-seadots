# Computational Experiment

OGC API Records profile for describing one computational experiment that realises a documented model.

A computational experiment is the executable counterpart of an ODD Protocol description: it commits to specific software, specific inputs and a specific output target. The record points at the executable code (Python script, Jupyter notebook, R script, etc.) that runs the experiment, and at standalone per-class input records (e.g. `area-of-interest`, `floating-wind-infrastructure`, `benthic-biomass-density-mareano`, …) and `experiment-output` records by URI so they can be reused across runs.

## What an experiment record carries

```
experiment:
  kind                — computational | observational | mesocosm | in-situ
  purpose             — research question being addressed
  application         — link to the executable (any language / format that exists and runs)
  modelledBy          — link to the ODD record realised by this experiment
  evidenceEquation    — link to the equation-property-relationship record
  parameters[]        — parameter definitions
  inputs[]            — link[] to per-class input records (NOT inlined)
                          each entry MAY carry an equationBinding symbol
  outputs[]           — link[] to experiment-output records (NOT inlined)
  execution           — language, languageVersion, dependencies, entrypoint,
                          scheduling, reproducibility flags
  successCriteria[]   — assertions the run must satisfy to be considered successful
```

## Composition pattern

The experiment record references inputs and outputs **by URI** rather than embedding them. This matches the cross-bblock composition already used by `odd-protocol` (which references `equation-property-relationship` records by URI) and keeps the experiment record stable when the input set is revised.

- Each input is a standalone instance of the matching per-class bblock: [`area-of-interest`](../area-of-interest/), [`floating-wind-infrastructure`](../floating-wind-infrastructure/), [`benthic-biomass-density-mareano`](../benthic-biomass-density-mareano/), [`benthic-biomass-density-imr`](../benthic-biomass-density-imr/), [`reef-aggregation-index`](../reef-aggregation-index/), [`colonisation-time-factor`](../colonisation-time-factor/).
- Each output is a standalone instance of [`experiment-output`](../experiment-output/).
- The equation is a standalone instance of [`equation-property-relationship`](../equation-property-relationship/).
- The model documentation is a standalone instance of [`odd-protocol`](../odd-protocol/).

## Application

The `application` field MUST point to an executable artefact that **exists and runs**. Acceptable forms:

- A Python script committed to the same repository (the case in the worked example).
- A Jupyter notebook with explicit kernel + dependencies.
- An R script or RMarkdown document with explicit `sessionInfo()` capture.
- Any other self-contained executable for which an `entrypoint` command exists.

Do not link to placeholder workflows that reference containers or tools that have not been built and published. The record should reflect what is actually runnable today, not what is intended in the future.

## Reproducibility

`execution.language` and `execution.languageVersion` identify the runtime; `execution.dependencies` lists the packages and versions; `execution.entrypoint` gives the exact command to invoke from the repository root. `execution.reproducibility.seedPolicy` SHOULD state whether the experiment is deterministic or how randomness is controlled. A PROV-O record (referenced as one of the `outputs`) closes the loop back to the inputs and the modelled equation.
