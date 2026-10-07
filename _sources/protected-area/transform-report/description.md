# Protected-area transform report

Every protected-area transform returns its output FeatureCollection with one extra member,
`seadotsTransformReport`, that says what the transform did **not** carry over unchanged. The view keeps
the national or regional source values, which are authoritative, and publishes where and why the
result departs from the source or from EMODnet instead of hiding it.

| Member | Written by | Meaning |
|---|---|---|
| `excluded` | Norway | source site left out, with the selection rule (not marine; no EEA designation type) |
| `notYetReportedToEEA` | Norway | site published without an EEA id; feature id `<country>-<nationalid>` |
| `needsMarineAreaOverlay` | Norway | `marinearea` not computed from a coastline overlay |
| `inferredDesignation` | Norway | EEA designation type taken from an *inferred* crosswalk row |
| `differsFromEMODnet` | Norway | field-level differences from the EMODnet record of the same site (`source` value kept, `emodnet` value reported) |
| `routedToNatura2000` | HELCOM layer 190 | Natura 2000 code, published by `emodnet:natura2000areas`; not duplicated |
| `routedToNationallyDesignatedAreas` | HELCOM layer 190 | EEA/WDPA site id, published by `emodnet:nationallydesignatedareas`; not duplicated |
| `unresolvedCode` | HELCOM layer 190 | national code matching no known scheme |
| `noStatusInRegister` | HELCOM layer 190 | HELCOM id without a layer-54 record, so no status; reported, not published |
| `mergedParts` | HELCOM | number of source polygons merged into one MultiPolygon per site |

The source blocks list this block in `dependsOn` because their transforms write the report; their
schemas do not refer to it, as the report is a foreign member of the output FeatureCollection.

The examples are the real reports produced by running each transform on its block's examples.
