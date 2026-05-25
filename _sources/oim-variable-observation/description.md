# OIM Variable Observation

This building block profiles OIM/SOSA observations for SEADOTS variables and
indicators. It follows the generic OIM/SOSA observation pattern and adds a small
numeric result object for variable values.

The observed variable is carried by `observedProperty`. For reef-effect
demonstrators, a reef aggregation index value is represented by setting:

```json
"observedProperty": "indp:reef-aggregation-index"
```

The example in this block is a compact observation for a dimensionless reef
aggregation index at Utsira Nord. The numeric value is illustrative because no
source data payload was provided with the generation request.
