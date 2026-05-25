# Colonisation Time Factor (C_t)

OGC Feature + OIM Variable profile for the dimensionless time factor `C_t` in the reef-biomass equation `B_reef = sum_i (A_sub · D_pre,i · AF_i · C_t)`.

`C_t` is a scalar that varies with time since installation, typically rising from near zero immediately after deployment to a saturation value (≈1) once the biofouling community has stabilised. This bblock encodes the curve as:

- `formula` — the closed-form expression (e.g. `C(t) = L / (1 + exp(-k * (t - t0)))`)
- `parameters` — values of the formula parameters (e.g. `L`, `k`, `t0_months`)
- `lookup` — an evaluated table at discrete `t_months` so a consumer can read pre-computed `C_t` values without re-evaluating the formula

## Dependency

Extends `ogc.hosted.seadots.api.features.oim-variables` — `C_t` is an OIM indicator.

## Required fields for script consumption

`_sources/reef-effect/scripts/utsira_reef_biomass.py` reads `data.parameters.L`, `data.parameters.k`, `data.parameters.t0_months` to evaluate the formula analytically, and the `data.lookup[]` array to populate the time series. All four are marked `required` in the schema.

## Authoritative source

There is no published closed-form sigmoid parameterisation of reef colonisation per taxon as of writing. Degraer 2020 discusses temporal dynamics qualitatively but gives no numeric parameters. The realistic calibration route is fitting a sigmoid to a published time series (WindFloat Atlantic monitoring etc.) — flagged in `context-validation-report.md`.
