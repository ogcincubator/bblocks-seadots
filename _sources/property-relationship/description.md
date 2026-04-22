A `PropertyRelationship` links two observable properties (`fromProperty` → `toProperty`) with a numeric weight
expressing the strength of their relationship, as produced by a specific model and experiment.

The `model` identifies the algorithm or system that generated the relationship, while `experiment` captures the
activity that ran it, including optional start and end timestamps. Both map to PROV-O concepts
(`prov:wasAttributedTo` and `prov:wasGeneratedBy` respectively).