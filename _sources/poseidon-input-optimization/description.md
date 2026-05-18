# POSEIDON Optimization Input

POSEIDON optimization inputs define a base scenario, tunable parameters or adaptors, an objective or fitness metric, run budget, seeds, and replicate strategy. They are used for policy and parameter search, including the Bayesian optimization workflow described in the POSEIDON paper and represented in the repository's EVA examples.

## Pilot use cases (north of Gotland)

Two canonical optimization tasks for the pilot:

1. **Model calibration (back-cast)**: tune unobservable parameters (gear catchability, exploration probability, social-network density, diffusion coefficients) so that POSEIDON outputs reproduce 2010–2023 observed series — SAG SSB, BITS length frequencies, VMS effort distribution, HaV landings, EUMOFA revenue.
2. **Policy search (forecast)**: hold the calibrated parameters fixed; search over policy parameters (TAC tonnes per stock, closure dates, gear-mesh size) to maximise an objective such as multi-stock GES achievement under a fleet-profit floor.

Both reduce to the same schema; only `baseScenario`, `parameters[]`, and `objective` differ.

## Source availability for the pilot area

Role classification:
- **R** = *Required* — optimization run cannot start without it.
- **S** = *Substitutable* — pick one per role; do not stack.
- **V** = *Validation-only* — used for post-hoc verification of the optimizer's selection, not for the objective.

| Source | Role | Coverage of SD 27 / 29 | Provides | Feeds POSEIDON field(s) | Related bblock(s) | Format at origin | Licence |
|---|---|---|---|---|---|---|---|
| ICES WGBFAS SAG SSB time series | **R** for calibration objective | Central Baltic herring, sprat, E. Baltic cod | Annual SSB, recruitment, F | `objective.expression` target series | [poseidon-input-biology] | XML/CSV (SAG) | ICES Data Policy (open) |
| DATRAS BITS length frequencies | **R** for length-structure calibration | SD 27/28/29 | Length-frequency by year × stratum | `objective.expression` target distribution | [poseidon-input-biology] | CSV | ICES Data Policy (open) |
| ICES VMS / GFW spatial effort | **R** for spatial calibration | Whole Baltic | Effort heatmap by year | `objective.expression` target raster (IoU / Spearman) | [poseidon-input-fleet] | CSV / Parquet | ICES / CC-BY-NC |
| HaV landings & first-sale | **R** for revenue/landings calibration | Sweden | Per-trip catch and value | Revenue and landings target series | [poseidon-input-fleet], [poseidon-input-port-market] | CSV | Swedish PSI Open |
| EUMOFA prices | **S** for revenue calibration | EU + Sweden | Monthly first-sale price | Revenue calibration target (alternative to HaV) | [poseidon-input-port-market] | CSV | EC Open |
| FishBase / RAM Legacy CI on biological parameters | **R** for parameter bounds | Target species | Confidence intervals on `Linf, K, M, h` | `parameters[].lowerBound`, `.upperBound` | [poseidon-input-biology] | CSV / SQLite | CC-BY-NC / CC-BY |
| STECF AER segment variance | **R** for fleet-parameter bounds | EU + Sweden | Segment-level fuel intensity, GVA variance | Bounds on fleet adaptation parameters | [poseidon-input-fleet] | Excel | EC Open |
| HELCOM BSAP indicators (GES thresholds) | **S** for policy objective | Whole Baltic | GES threshold values | `objective.expression` for policy search | [poseidon-input-regulation-policy] | CSV / API | CC-BY 4.0 |
| EU MAP F_msy ranges | **S** for policy objective | Baltic stocks | F target ranges | Constraint in policy-search objective | [poseidon-input-regulation-policy] | EUR-Lex | EC Open |
| BoTorch / Ax library defaults | **R** for BO algorithm | – | Acquisition functions, GP priors | `algorithm` selection, kernel choice | – | Python package | MIT |
| OpenMDAO / pymoo (multi-objective) | **S** for multi-objective policy search | – | NSGA-II, MOEA/D | `algorithm` selection | – | Python | Apache-2 |
| Held-out years of SAG / BITS / VMS | **V** | Same as above | Out-of-sample target | Cross-validation of calibration result | [poseidon-input-observation-output] | CSV / Parquet | ICES Data Policy (open) |

[poseidon-input-biology]: ../poseidon-input-biology/
[poseidon-input-fleet]: ../poseidon-input-fleet/
[poseidon-input-map]: ../poseidon-input-map/
[poseidon-input-port-market]: ../poseidon-input-port-market/
[poseidon-input-regulation-policy]: ../poseidon-input-regulation-policy/
[poseidon-input-scenario]: ../poseidon-input-scenario/
[poseidon-input-observation-output]: ../poseidon-input-observation-output/

## Two-stage transformation pipeline

Stage A in this bblock is unusual: the optimization target series are already EDITO-compliant (they were produced as V-role artefacts by other bblocks' Stage A). Stage A here therefore:

1. Registers a new STAC Collection `poseidon-optimization-north-gotland` that *aggregates* the V-role targets via STAC links.
2. Persists the optimizer's Design-of-Experiments (DoE) ledger and per-iteration evaluation results as Parquet.

Stage B compiles the YAML optimization configuration POSEIDON consumes.

### Stage A — Source → EDITO

| Source | EDITO artefact | Transformation |
|---|---|---|
| V-role series from biology / fleet / port-market | `optimization/targets.json` (STAC links) | Build a STAC Collection that *references* the existing Items (no copy); each link tagged with `role=target` and the metric to be computed against. |
| FishBase / RAM Legacy CI for `Linf, K, M, h` | `optimization/parameter_bounds.parquet` | One row per `(species, parameter, lower, upper, prior_mean, prior_sd, source)`; the CI is parsed from FishBase `popgrowth.PopulationsRef` notes and RAM `bioparams` confidence columns. |
| STECF AER segment variance | `optimization/fleet_parameter_bounds.parquet` | Same shape, keyed on `(fleet_segment_id, parameter, lower, upper)`. |
| HELCOM BSAP indicators (GES thresholds) | `optimization/policy_objectives.parquet` | One row per `(indicator_id, threshold, comparison_op, weight)`. |
| Optimizer DoE ledger (output) | `optimization/doe.parquet` (written per iteration during the optimization run) | Columns `iteration, parameters_json, objective_value, replicates_seeds[], wall_clock_s`. |
| Optimizer best-so-far (output) | `optimization/best.parquet` | One row per Pareto-front member (or one row total for single-objective). |

### Stage B — EDITO → POSEIDON

| EDITO artefact | POSEIDON field(s) | Transformation |
|---|---|---|
| `parameter_bounds.parquet` + `fleet_parameter_bounds.parquet` | `parameters[]` with `name, adaptor, lowerBound, upperBound` | One row per parameter; `adaptor` is the POSEIDON parameter-adaptor path (e.g. `species[0].growth.steepness`). |
| `targets.json` + `policy_objectives.parquet` | `objective` (and optional `objective.expression`) | Build a single scalar (or vector for multi-objective) expression: `Σ_i w_i * metric_i(model_output_i, target_i)`. For calibration: weighted sum of NRMSE on SSB + KS on length-freq + IoU on effort heatmap. For policy: BSAP indicator achievement minus profit-floor penalty. |
| `baseScenario` (input) | `baseScenario` reference | Set to the STAC Item URI of the calibrated scenario for policy search; or to a status-quo scenario for calibration. |
| – | `algorithm` | `"Bayesian optimization"` (default, BoTorch/Ax) for single-objective; `"NSGA-II"` for multi-objective policy search. |
| – | `simulationBudget` | Computed from wall-clock target ÷ mean per-run cost (from previous DoE iterations) and capped by user budget. |
| – | `replicatesPerEvaluation` | 3 by default for stochastic POSEIDON; up to 10 for noisy objectives. |

## Required vs substitutable vs validation-only

### Required path

| Optimization task | Minimum required sources |
|---|---|
| Calibration (back-cast) | SAG SSB (R) + BITS length-freq (R) + VMS/GFW effort (R) + HaV landings (R) + FishBase/RAM CI for bounds (R) + STECF AER variance for fleet bounds (R) + BoTorch/Ax (R) |
| Policy search (forecast, single-objective) | A calibrated `baseScenario` (R) + at least one policy parameter bound table (R) + a single-metric `objective.expression` (R) |
| Policy search (multi-objective) | Same + HELCOM BSAP indicators (S) + pymoo / NSGA-II (S) |

### Substitutable

- **Optimization algorithm**: BoTorch/Ax (preferred for single-objective with ≤ ~30 parameters, expensive evaluations) **xor** NSGA-II via pymoo (preferred for multi-objective ≥ 2 metrics) **xor** CMA-ES (fallback for high-dim, less-expensive evaluations).
- **Policy objective**: HELCOM BSAP indicator achievement **xor** EU MAP F_msy compliance — different normative frames; pick one per run.
- **Revenue calibration target**: Swedish HaV (preferred, vessel-level) **xor** EUMOFA (coarser).

### Validation-only

- Held-out years of SAG / BITS / VMS / HaV — used post-optimization to score generalisation.
- ICES retrospective patterns — sanity check that the calibrated model does not over-fit a single assessment year.

### Minimal viable bundle for the pilot

For **calibration**:
1. SAG SSB time series for Central Baltic herring + sprat (2010–2023).
2. BITS Q1 length frequencies (2010–2023).
3. VMS C-square effort for SE flag (2010–2023).
4. FishBase 95% CI on `Linf, K, M` for the two species.
5. STECF AER 2010–2023 segment fuel intensity variance for pelagic-trawl segment.
6. BoTorch/Ax with default acquisition function.

For **policy search**, the calibrated scenario from above + a TAC parameter table + a single GVA-vs-SSB objective.

## Cross-bblock contract

- `baseScenario` MUST resolve to a STAC Item exported by [poseidon-input-scenario] (a scenario Item bundling all input bblocks).
- `parameters[].adaptor` paths MUST exist in the bundled scenario — the runner statically validates each adaptor path before launching.
- `objective.metric` MUST be the **name** of a `timeSeries[]` or `gridded[]` entry declared in [poseidon-input-observation-output] (and therefore present in the [poseidon-output] manifest of each evaluation).
- Calibration replicates' outputs are written to one [poseidon-output] manifest per evaluation under a sub-Collection `poseidon-output-<runId>` — the DoE ledger records the run IDs so the optimizer's best-so-far is reproducible.
- Held-out V-role years are *not* allowed in `objective.expression`; the runner enforces this by checking the year-range of each referenced target Item against [poseidon-input-run-control]'s `yearsToRun`.
