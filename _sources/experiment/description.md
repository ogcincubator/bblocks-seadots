# Computational Experiment

OGC API Records profile for describing one computational experiment that realises a documented model.

A computational experiment is the executable counterpart of an ODD Protocol description: it commits to specific software, specific inputs and a specific output target. This bblock provides the scaffold so a CWL-aware engine can load the record and run the experiment without further hand-wiring.

## What an experiment record carries

```
experiment:
  kind                — computational | observational | mesocosm | in-situ
  purpose             — research question being addressed
  applicationPackage  — link to a CWL Application Package
  modelledBy          — link to the ODD record realised by this experiment
  evidenceEquation    — link to the equation-property-relationship record
  parameters[]        — parameter definitions with bindings to CWL inputs
  inputs[]            — link[] to experiment-input records (NOT inlined)
  outputs[]           — link[] to experiment-output records (NOT inlined)
  execution           — engine list, container digest, scheduling, reproducibility flags
  successCriteria[]   — assertions the run must satisfy to be considered successful
```

## Composition pattern

The experiment record references inputs and outputs **by URI** rather than embedding them. This matches the cross-bblock composition already used by `odd-protocol` (which references `equation-property-relationship` records by URI) and keeps the experiment record stable when the input set is revised.

- Each input is a standalone instance of [`experiment-input`](../experiment-input/).
- Each output is a standalone instance of [`experiment-output`](../experiment-output/).
- The equation is a standalone instance of [`equation-property-relationship`](../equation-property-relationship/).
- The model documentation is a standalone instance of [`odd-protocol`](../odd-protocol/).

## Reproducibility

`execution.container` and `execution.containerDigest` MUST identify the runtime container. `execution.reproducibility.seedPolicy` SHOULD state whether the experiment is deterministic or how randomness is controlled. A PROV-O record (referenced as one of the `outputs`) closes the loop back to the inputs and the modelled equation.
