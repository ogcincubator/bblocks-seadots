
# Equation property relationship (Schema)

`ogc.hosted.seadots.equation-property-relationship` *v0.1*

Specialised property relationship profile for declaring that a source property is an explicit term in the canonical equation of a derived target property.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

An `EquationPropertyRelationship` is a specialised `PropertyRelationship` that records the
canonical equation calculating a derived indicator (`toProperty`) and the symbols inside it.
It supports two usage modes:

- **Equation-level (recommended for documentation)**: omit top-level `fromProperty`. The
  record describes the equation as a whole; `symbols[]` is the complete symbol table.
  Examples in this block use this mode.

- **Symbol-edge (sensitivity / cross-impact reading)**: include top-level `fromProperty`,
  matching exactly one entry in `symbols[]`. The record is then centred on that input,
  while still carrying the full table.

Use this block when the relationship is mathematical lineage. Use the existing
`property-relationship` block for weighted causal cross-impact edges, such as
`ind:floating-wind-reef-biomass -> indo:floating-wind-fish-abundance`.

Validation intent (partly enforced by `_sources/ontology/rules.shacl`):

- `equation` should be byte-identical to `schema:mathExpression` on the target Rainbow concept.
- every `symbols[].fromProperty` should be listed in `prov:wasDerivedFrom` on `toProperty`.
- each `symbols[].symbol` must occur literally inside `equation`.
- `symbols[].indexed: true` requires `toProperty` to declare an `:Aggregation`.
- when present, top-level `fromProperty` must match exactly one `symbols[].fromProperty`.
- `weight`, if present, represents sensitivity or coefficient value, not causal influence.

The `symbols[]` table is intentionally complete: every equation symbol is declared there,
making each record computationally self-contained.

Recommended symbol fields:

- `symbol` — the LaTeX symbol used in `equation` (e.g. `A_{sub}`, `D_{pre,i}`, `AF_i`, `C_t`).
- `symbolAliases` — ASCII or alternate renderings.
- `variableKind` — semantic role (`featureOfInterest`, `intensiveQuantity`, `adjustmentFactor`,
  `timeCoefficient`, `uncertaintyFactor`, …).
- `dimensionKind` — QUDT QuantityKind URI (unit-abstract).
- `bindings[]` — concrete Rainbow IRIs that realise the abstract `fromProperty`.

## Examples

### Reef-biomass equation (equation-level record)
Equation-level record for `B_{reef} = \sum_i (A_{sub} \cdot D_{pre,i} \cdot AF_i \cdot C_t)`.
`symbols[]` carries the full computable table: A_{sub} (feature of interest, Area),
D_{pre,i} (intensive density per taxon, SurfaceDensity), AF_i (per-taxon adjustment factor,
Dimensionless), C_t (time coefficient, Dimensionless). Top-level `fromProperty` is omitted
because the record describes the equation as a whole, not a single symbol-edge.

#### json
```json
{
  "id": "indo:eqrel/reef-biomass-effect",
  "type": [
    "PropertyRelationship",
    "EquationPropertyRelationship"
  ],
  "relationshipKind": "equation",
  "toProperty": "ind:floating-wind-reef-biomass",
  "equation": "B_{reef} = \\sum_i (A_{sub} \\cdot D_{pre,i} \\cdot AF_i \\cdot C_t)",
  "targetDefinition": {
    "id": "ind:floating-wind-reef-biomass",
    "type": "prov:Entity",
    "mathExpression": "B_{reef} = \\sum_i (A_{sub} \\cdot D_{pre,i} \\cdot AF_i \\cdot C_t)",
    "wasDerivedFrom": [
      "indo:submerged-infrastructure-area",
      "indo:baseline-benthic-biomass-density",
      "indo:reef-aggregation-index",
      "indo:colonisation-time-factor"
    ],
    "aggregation": {
      "type": "prop-rel:Aggregation",
      "operator": "prop-rel:Sum",
      "aggregatesOver": "tc:TaxonConcept",
      "indexSymbol": "i"
    }
  },
  "symbols": [
    {
      "symbol": "A_{sub}",
      "symbolAliases": ["A_sub", "A_s"],
      "fromProperty": "indo:submerged-infrastructure-area",
      "variableKind": "featureOfInterest",
      "dimensionKind": "quantitykind:Area",
      "indexed": false,
      "equationRole": "input",
      "operator": "product",
      "bindings": [
        { "variable": "indo:submerged-infrastructure-area-utsira-design",
          "bindingRole": "primary",
          "validityScope": "Utsira Nord engineering design (60 × 15 MW units, wetted hull + mooring + anchor surfaces)",
          "evidence": "https://veiledere.nve.no/havvind/strategisk-konsekvensutredning-av-vindkraft-til-havs/" }
      ]
    },
    {
      "symbol": "D_{pre,i}",
      "symbolAliases": ["D_pre_i", "D_pre,i", "D_pre"],
      "fromProperty": "indo:baseline-benthic-biomass-density",
      "variableKind": "intensiveQuantity",
      "dimensionKind": "quantitykind:SurfaceDensity",
      "indexed": true,
      "index": "i",
      "indexedBy": "tc:TaxonConcept",
      "equationRole": "input",
      "operator": "product",
      "bindings": [
        { "variable": "indo:benthic-biomass-density-mareano",
          "bindingRole": "primary",
          "validityScope": "Norwegian shelf, MAREANO programme",
          "evidence": "https://mareano.no/" },
        { "variable": "indo:benthic-biomass-density-imr-baseline",
          "bindingRole": "fallback",
          "validityScope": "regional default when MAREANO has no taxon coverage at i",
          "evidence": "https://www.hi.no/" }
      ]
    },
    {
      "symbol": "AF_i",
      "fromProperty": "indo:reef-aggregation-index",
      "variableKind": "adjustmentFactor",
      "dimensionKind": "quantitykind:Dimensionless",
      "indexed": true,
      "index": "i",
      "indexedBy": "tc:TaxonConcept",
      "equationRole": "coefficient",
      "operator": "product",
      "bindings": [
        { "variable": "indo:reef-aggregation-index-mytilus",
          "indexValue": "Mytilus edulis",
          "bindingRole": "expansion",
          "validityScope": "North Sea, depth 0-30 m",
          "evidence": "https://doi.org/10.5670/oceanog.2020.405" },
        { "variable": "indo:reef-aggregation-index-buccinum",
          "indexValue": "Buccinum undatum",
          "bindingRole": "expansion",
          "evidence": "https://www.windfloat-atlantic.com/" },
        { "variable": "indo:reef-aggregation-index-asterias",
          "indexValue": "Asterias rubens",
          "bindingRole": "expansion" }
      ]
    },
    {
      "symbol": "C_t",
      "symbolAliases": ["C_{t}", "C_time"],
      "fromProperty": "indo:colonisation-time-factor",
      "variableKind": "timeCoefficient",
      "dimensionKind": "quantitykind:Dimensionless",
      "indexed": false,
      "equationRole": "coefficient",
      "operator": "product",
      "bindings": [
        { "variable": "indo:colonisation-time-factor-default",
          "bindingRole": "primary",
          "validityScope": "default sigmoid colonisation curve, saturating at t = 24 months",
          "evidence": "https://doi.org/10.5670/oceanog.2020.405" }
      ]
    }
  ],
  "model": {
    "id": "utsira-biomass-upscaler-v1",
    "name": "Utsira biomass upscaler v1",
    "uri": "https://example.org/norwegian-ses/utsira-biomass-upscaler-v1"
  },
  "evidence": "ind:floating-wind-reef-biomass",
  "explanation": "Equation-level record for the reef-biomass equation. `symbols[]` enumerates every term (A_{sub} feature-of-interest, D_{pre,i} intensive density per taxon, AF_i adjustment factor per taxon, C_t time coefficient) with its abstract Rainbow IRI, kind, dimension and concrete bindings. No top-level `fromProperty`: the record describes the equation as a whole."
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "indo": "https://w3id.org/indicators/marine/obs/",
      "ind": "https://w3id.org/indicators/marine/"
    },
    "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/equation-property-relationship/context.jsonld"
  ],
  "id": "indo:eqrel/reef-biomass-effect",
  "type": [
    "PropertyRelationship",
    "EquationPropertyRelationship"
  ],
  "relationshipKind": "equation",
  "toProperty": "ind:floating-wind-reef-biomass",
  "equation": "B_{reef} = \\sum_i (A_{sub} \\cdot D_{pre,i} \\cdot AF_i \\cdot C_t)",
  "targetDefinition": {
    "id": "ind:floating-wind-reef-biomass",
    "type": "prov:Entity",
    "mathExpression": "B_{reef} = \\sum_i (A_{sub} \\cdot D_{pre,i} \\cdot AF_i \\cdot C_t)",
    "wasDerivedFrom": [
      "indo:submerged-infrastructure-area",
      "indo:baseline-benthic-biomass-density",
      "indo:reef-aggregation-index",
      "indo:colonisation-time-factor"
    ],
    "aggregation": {
      "type": "prop-rel:Aggregation",
      "operator": "prop-rel:Sum",
      "aggregatesOver": "tc:TaxonConcept",
      "indexSymbol": "i"
    }
  },
  "symbols": [
    {
      "symbol": "A_{sub}",
      "symbolAliases": [
        "A_sub",
        "A_s"
      ],
      "fromProperty": "indo:submerged-infrastructure-area",
      "variableKind": "featureOfInterest",
      "dimensionKind": "quantitykind:Area",
      "indexed": false,
      "equationRole": "input",
      "operator": "product",
      "bindings": [
        {
          "variable": "indo:submerged-infrastructure-area-utsira-design",
          "bindingRole": "primary",
          "validityScope": "Utsira Nord engineering design (60 \u00d7 15 MW units, wetted hull + mooring + anchor surfaces)",
          "evidence": "https://veiledere.nve.no/havvind/strategisk-konsekvensutredning-av-vindkraft-til-havs/"
        }
      ]
    },
    {
      "symbol": "D_{pre,i}",
      "symbolAliases": [
        "D_pre_i",
        "D_pre,i",
        "D_pre"
      ],
      "fromProperty": "indo:baseline-benthic-biomass-density",
      "variableKind": "intensiveQuantity",
      "dimensionKind": "quantitykind:SurfaceDensity",
      "indexed": true,
      "index": "i",
      "indexedBy": "tc:TaxonConcept",
      "equationRole": "input",
      "operator": "product",
      "bindings": [
        {
          "variable": "indo:benthic-biomass-density-mareano",
          "bindingRole": "primary",
          "validityScope": "Norwegian shelf, MAREANO programme",
          "evidence": "https://mareano.no/"
        },
        {
          "variable": "indo:benthic-biomass-density-imr-baseline",
          "bindingRole": "fallback",
          "validityScope": "regional default when MAREANO has no taxon coverage at i",
          "evidence": "https://www.hi.no/"
        }
      ]
    },
    {
      "symbol": "AF_i",
      "fromProperty": "indo:reef-aggregation-index",
      "variableKind": "adjustmentFactor",
      "dimensionKind": "quantitykind:Dimensionless",
      "indexed": true,
      "index": "i",
      "indexedBy": "tc:TaxonConcept",
      "equationRole": "coefficient",
      "operator": "product",
      "bindings": [
        {
          "variable": "indo:reef-aggregation-index-mytilus",
          "indexValue": "Mytilus edulis",
          "bindingRole": "expansion",
          "validityScope": "North Sea, depth 0-30 m",
          "evidence": "https://doi.org/10.5670/oceanog.2020.405"
        },
        {
          "variable": "indo:reef-aggregation-index-buccinum",
          "indexValue": "Buccinum undatum",
          "bindingRole": "expansion",
          "evidence": "https://www.windfloat-atlantic.com/"
        },
        {
          "variable": "indo:reef-aggregation-index-asterias",
          "indexValue": "Asterias rubens",
          "bindingRole": "expansion"
        }
      ]
    },
    {
      "symbol": "C_t",
      "symbolAliases": [
        "C_{t}",
        "C_time"
      ],
      "fromProperty": "indo:colonisation-time-factor",
      "variableKind": "timeCoefficient",
      "dimensionKind": "quantitykind:Dimensionless",
      "indexed": false,
      "equationRole": "coefficient",
      "operator": "product",
      "bindings": [
        {
          "variable": "indo:colonisation-time-factor-default",
          "bindingRole": "primary",
          "validityScope": "default sigmoid colonisation curve, saturating at t = 24 months",
          "evidence": "https://doi.org/10.5670/oceanog.2020.405"
        }
      ]
    }
  ],
  "model": {
    "id": "utsira-biomass-upscaler-v1",
    "name": "Utsira biomass upscaler v1",
    "uri": "https://example.org/norwegian-ses/utsira-biomass-upscaler-v1"
  },
  "evidence": "ind:floating-wind-reef-biomass",
  "explanation": "Equation-level record for the reef-biomass equation. `symbols[]` enumerates every term (A_{sub} feature-of-interest, D_{pre,i} intensive density per taxon, AF_i adjustment factor per taxon, C_t time coefficient) with its abstract Rainbow IRI, kind, dimension and concrete bindings. No top-level `fromProperty`: the record describes the equation as a whole."
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ind: <https://w3id.org/indicators/marine/> .
@prefix indo: <https://w3id.org/indicators/marine/obs/> .
@prefix prop-rel: <https://w3id.org/ogc/hosted/seadots/prop-rel/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix quantitykind: <http://qudt.org/vocab/quantitykind/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix tc: <http://rs.tdwg.org/ontology/voc/TaxonConcept#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/indicators/marine/obs/eqrel/reef-biomass-effect> a prop-rel:EquationPropertyRelationship,
        prop-rel:PropertyRelationship ;
    rdfs:comment "Equation-level record for the reef-biomass equation. `symbols[]` enumerates every term (A_{sub} feature-of-interest, D_{pre,i} intensive density per taxon, AF_i adjustment factor per taxon, C_t time coefficient) with its abstract Rainbow IRI, kind, dimension and concrete bindings. No top-level `fromProperty`: the record describes the equation as a whole." ;
    prov:wasAttributedTo <https://example.org/norwegian-ses/utsira-biomass-upscaler-v1> ;
    prov:wasDerivedFrom ind:floating-wind-reef-biomass ;
    schema:additionalType "equation" ;
    prop-rel:hasEquation "B_{reef} = \\sum_i (A_{sub} \\cdot D_{pre,i} \\cdot AF_i \\cdot C_t)" ;
    prop-rel:hasEquationSymbol [ prop-rel:fromProperty indo:baseline-benthic-biomass-density ;
            prop-rel:hasBinding [ prov:wasDerivedFrom <https://www.hi.no/> ;
                    prop-rel:bindingRole <file:///github/workspace/fallback> ;
                    prop-rel:bindingValidityScope "regional default when MAREANO has no taxon coverage at i" ;
                    prop-rel:bindingVariable indo:benthic-biomass-density-imr-baseline ],
                [ prov:wasDerivedFrom <https://mareano.no/> ;
                    prop-rel:bindingRole <file:///github/workspace/primary> ;
                    prop-rel:bindingValidityScope "Norwegian shelf, MAREANO programme" ;
                    prop-rel:bindingVariable indo:benthic-biomass-density-mareano ] ;
            prop-rel:hasDimensionKind quantitykind:SurfaceDensity ;
            prop-rel:hasEquationRole <file:///github/workspace/input> ;
            prop-rel:hasIndex "i" ;
            prop-rel:hasIndexedBy tc:TaxonConcept ;
            prop-rel:hasOperator <file:///github/workspace/product> ;
            prop-rel:hasSymbol "D_{pre,i}" ;
            prop-rel:hasSymbolAlias "D_pre",
                "D_pre,i",
                "D_pre_i" ;
            prop-rel:hasVariableKind <file:///github/workspace/intensiveQuantity> ;
            prop-rel:isIndexed true ],
        [ prop-rel:fromProperty indo:reef-aggregation-index ;
            prop-rel:hasBinding [ prov:wasDerivedFrom <https://www.windfloat-atlantic.com/> ;
                    prop-rel:bindingIndexValue "Buccinum undatum" ;
                    prop-rel:bindingRole <file:///github/workspace/expansion> ;
                    prop-rel:bindingVariable indo:reef-aggregation-index-buccinum ],
                [ prop-rel:bindingIndexValue "Asterias rubens" ;
                    prop-rel:bindingRole <file:///github/workspace/expansion> ;
                    prop-rel:bindingVariable indo:reef-aggregation-index-asterias ],
                [ prov:wasDerivedFrom <https://doi.org/10.5670/oceanog.2020.405> ;
                    prop-rel:bindingIndexValue "Mytilus edulis" ;
                    prop-rel:bindingRole <file:///github/workspace/expansion> ;
                    prop-rel:bindingValidityScope "North Sea, depth 0-30 m" ;
                    prop-rel:bindingVariable indo:reef-aggregation-index-mytilus ] ;
            prop-rel:hasDimensionKind quantitykind:Dimensionless ;
            prop-rel:hasEquationRole <file:///github/workspace/coefficient> ;
            prop-rel:hasIndex "i" ;
            prop-rel:hasIndexedBy tc:TaxonConcept ;
            prop-rel:hasOperator <file:///github/workspace/product> ;
            prop-rel:hasSymbol "AF_i" ;
            prop-rel:hasVariableKind <file:///github/workspace/adjustmentFactor> ;
            prop-rel:isIndexed true ],
        [ prop-rel:fromProperty indo:colonisation-time-factor ;
            prop-rel:hasBinding [ prov:wasDerivedFrom <https://doi.org/10.5670/oceanog.2020.405> ;
                    prop-rel:bindingRole <file:///github/workspace/primary> ;
                    prop-rel:bindingValidityScope "default sigmoid colonisation curve, saturating at t = 24 months" ;
                    prop-rel:bindingVariable indo:colonisation-time-factor-default ] ;
            prop-rel:hasDimensionKind quantitykind:Dimensionless ;
            prop-rel:hasEquationRole <file:///github/workspace/coefficient> ;
            prop-rel:hasOperator <file:///github/workspace/product> ;
            prop-rel:hasSymbol "C_t" ;
            prop-rel:hasSymbolAlias "C_time",
                "C_{t}" ;
            prop-rel:hasVariableKind <file:///github/workspace/timeCoefficient> ;
            prop-rel:isIndexed false ],
        [ prop-rel:fromProperty indo:submerged-infrastructure-area ;
            prop-rel:hasBinding [ prov:wasDerivedFrom <https://veiledere.nve.no/havvind/strategisk-konsekvensutredning-av-vindkraft-til-havs/> ;
                    prop-rel:bindingRole <file:///github/workspace/primary> ;
                    prop-rel:bindingValidityScope "Utsira Nord engineering design (60 × 15 MW units, wetted hull + mooring + anchor surfaces)" ;
                    prop-rel:bindingVariable indo:submerged-infrastructure-area-utsira-design ] ;
            prop-rel:hasDimensionKind quantitykind:Area ;
            prop-rel:hasEquationRole <file:///github/workspace/input> ;
            prop-rel:hasOperator <file:///github/workspace/product> ;
            prop-rel:hasSymbol "A_{sub}" ;
            prop-rel:hasSymbolAlias "A_s",
                "A_sub" ;
            prop-rel:hasVariableKind <file:///github/workspace/featureOfInterest> ;
            prop-rel:isIndexed false ] ;
    prop-rel:targetDefinition ind:floating-wind-reef-biomass ;
    prop-rel:toProperty ind:floating-wind-reef-biomass .

<https://example.org/norwegian-ses/utsira-biomass-upscaler-v1> rdfs:label "Utsira biomass upscaler v1" ;
    dct:identifier "utsira-biomass-upscaler-v1" .

ind:floating-wind-reef-biomass a prov:Entity ;
    prov:wasDerivedFrom indo:baseline-benthic-biomass-density,
        indo:colonisation-time-factor,
        indo:reef-aggregation-index,
        indo:submerged-infrastructure-area ;
    schema:mathExpression "B_{reef} = \\sum_i (A_{sub} \\cdot D_{pre,i} \\cdot AF_i \\cdot C_t)" ;
    prop-rel:hasAggregation [ a prop-rel:Aggregation ;
            prop-rel:aggregatesOver tc:TaxonConcept ;
            prop-rel:aggregationOperator prop-rel:Sum ;
            prop-rel:indexSymbol "i" ] .


```


### Quality-adjusted biomass equation (equation-level record)
Equation-level record for `B_{qa} = B_{total} \cdot (1 - U)`. `symbols[]` carries the two
terms: B_{total} chained from a sibling equation (`ind:wind-park-biomass-effect`) and U the
data-quality uncertainty factor computed at run-time from QI_* scores.

#### json
```json
{
  "id": "indo:eqrel/quality-adjusted-biomass-effect",
  "type": [
    "PropertyRelationship",
    "EquationPropertyRelationship"
  ],
  "relationshipKind": "equation",
  "toProperty": "ind:quality-adjusted-biomass-effect",
  "equation": "B_{qa} = B_{total} \\cdot (1 - U)",
  "targetDefinition": {
    "id": "ind:quality-adjusted-biomass-effect",
    "type": "prov:Entity",
    "mathExpression": "B_{qa} = B_{total} \\cdot (1 - U)",
    "wasDerivedFrom": [
      "ind:wind-park-biomass-effect",
      "indo:data-quality-uncertainty-factor"
    ]
  },
  "symbols": [
    {
      "symbol": "B_{total}",
      "symbolAliases": ["B_total"],
      "fromProperty": "ind:wind-park-biomass-effect",
      "variableKind": "extensiveQuantity",
      "dimensionKind": "quantitykind:Mass",
      "indexed": false,
      "equationRole": "input",
      "operator": "product",
      "bindings": [
        { "variable": "ind:wind-park-biomass-effect",
          "bindingRole": "primary",
          "validityScope": "Output of the wind-park biomass equation (B_total = B_reef + B_reserve − B_lost_soft_sediment). Chained input.",
          "evidence": "ind:wind-park-biomass-effect" }
      ],
      "explanation": "Chained input: B_total is itself a derived indicator computed by a sibling equation."
    },
    {
      "symbol": "U",
      "symbolAliases": ["U_{data}", "U_data"],
      "fromProperty": "indo:data-quality-uncertainty-factor",
      "variableKind": "uncertaintyFactor",
      "dimensionKind": "quantitykind:Dimensionless",
      "indexed": false,
      "equationRole": "uncertaintyTerm",
      "operator": "product",
      "bindings": [
        { "variable": "indo:data-quality-uncertainty-factor",
          "bindingRole": "primary",
          "validityScope": "Computed at run-time as 1 - mean(QI_lineage, QI_representativeness, QI_temporal, QI_spatial, QI_method, QI_uncertainty); see dataset-qa skill output for per-input values.",
          "evidence": "ind:quality-adjusted-biomass-effect" }
      ]
    }
  ],
  "model": {
    "id": "utsira-biomass-upscaler-v1",
    "name": "Utsira biomass upscaler v1",
    "uri": "https://example.org/norwegian-ses/utsira-biomass-upscaler-v1"
  },
  "evidence": "ind:quality-adjusted-biomass-effect",
  "explanation": "Equation-level record for the quality-adjusted biomass equation. B_{total} is a chained input from the wind-park biomass equation; U is the data-quality uncertainty factor computed at run-time. No top-level `fromProperty`: the record describes the equation as a whole."
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "indo": "https://w3id.org/indicators/marine/obs/",
      "ind": "https://w3id.org/indicators/marine/"
    },
    "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/equation-property-relationship/context.jsonld"
  ],
  "id": "indo:eqrel/quality-adjusted-biomass-effect",
  "type": [
    "PropertyRelationship",
    "EquationPropertyRelationship"
  ],
  "relationshipKind": "equation",
  "toProperty": "ind:quality-adjusted-biomass-effect",
  "equation": "B_{qa} = B_{total} \\cdot (1 - U)",
  "targetDefinition": {
    "id": "ind:quality-adjusted-biomass-effect",
    "type": "prov:Entity",
    "mathExpression": "B_{qa} = B_{total} \\cdot (1 - U)",
    "wasDerivedFrom": [
      "ind:wind-park-biomass-effect",
      "indo:data-quality-uncertainty-factor"
    ]
  },
  "symbols": [
    {
      "symbol": "B_{total}",
      "symbolAliases": [
        "B_total"
      ],
      "fromProperty": "ind:wind-park-biomass-effect",
      "variableKind": "extensiveQuantity",
      "dimensionKind": "quantitykind:Mass",
      "indexed": false,
      "equationRole": "input",
      "operator": "product",
      "bindings": [
        {
          "variable": "ind:wind-park-biomass-effect",
          "bindingRole": "primary",
          "validityScope": "Output of the wind-park biomass equation (B_total = B_reef + B_reserve \u2212 B_lost_soft_sediment). Chained input.",
          "evidence": "ind:wind-park-biomass-effect"
        }
      ],
      "explanation": "Chained input: B_total is itself a derived indicator computed by a sibling equation."
    },
    {
      "symbol": "U",
      "symbolAliases": [
        "U_{data}",
        "U_data"
      ],
      "fromProperty": "indo:data-quality-uncertainty-factor",
      "variableKind": "uncertaintyFactor",
      "dimensionKind": "quantitykind:Dimensionless",
      "indexed": false,
      "equationRole": "uncertaintyTerm",
      "operator": "product",
      "bindings": [
        {
          "variable": "indo:data-quality-uncertainty-factor",
          "bindingRole": "primary",
          "validityScope": "Computed at run-time as 1 - mean(QI_lineage, QI_representativeness, QI_temporal, QI_spatial, QI_method, QI_uncertainty); see dataset-qa skill output for per-input values.",
          "evidence": "ind:quality-adjusted-biomass-effect"
        }
      ]
    }
  ],
  "model": {
    "id": "utsira-biomass-upscaler-v1",
    "name": "Utsira biomass upscaler v1",
    "uri": "https://example.org/norwegian-ses/utsira-biomass-upscaler-v1"
  },
  "evidence": "ind:quality-adjusted-biomass-effect",
  "explanation": "Equation-level record for the quality-adjusted biomass equation. B_{total} is a chained input from the wind-park biomass equation; U is the data-quality uncertainty factor computed at run-time. No top-level `fromProperty`: the record describes the equation as a whole."
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ind: <https://w3id.org/indicators/marine/> .
@prefix indo: <https://w3id.org/indicators/marine/obs/> .
@prefix prop-rel: <https://w3id.org/ogc/hosted/seadots/prop-rel/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix quantitykind: <http://qudt.org/vocab/quantitykind/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/indicators/marine/obs/eqrel/quality-adjusted-biomass-effect> a prop-rel:EquationPropertyRelationship,
        prop-rel:PropertyRelationship ;
    rdfs:comment "Equation-level record for the quality-adjusted biomass equation. B_{total} is a chained input from the wind-park biomass equation; U is the data-quality uncertainty factor computed at run-time. No top-level `fromProperty`: the record describes the equation as a whole." ;
    prov:wasAttributedTo <https://example.org/norwegian-ses/utsira-biomass-upscaler-v1> ;
    prov:wasDerivedFrom ind:quality-adjusted-biomass-effect ;
    schema:additionalType "equation" ;
    prop-rel:hasEquation "B_{qa} = B_{total} \\cdot (1 - U)" ;
    prop-rel:hasEquationSymbol [ rdfs:comment "Chained input: B_total is itself a derived indicator computed by a sibling equation." ;
            prop-rel:fromProperty ind:wind-park-biomass-effect ;
            prop-rel:hasBinding [ prov:wasDerivedFrom ind:wind-park-biomass-effect ;
                    prop-rel:bindingRole <file:///github/workspace/primary> ;
                    prop-rel:bindingValidityScope "Output of the wind-park biomass equation (B_total = B_reef + B_reserve − B_lost_soft_sediment). Chained input." ;
                    prop-rel:bindingVariable ind:wind-park-biomass-effect ] ;
            prop-rel:hasDimensionKind quantitykind:Mass ;
            prop-rel:hasEquationRole <file:///github/workspace/input> ;
            prop-rel:hasOperator <file:///github/workspace/product> ;
            prop-rel:hasSymbol "B_{total}" ;
            prop-rel:hasSymbolAlias "B_total" ;
            prop-rel:hasVariableKind <file:///github/workspace/extensiveQuantity> ;
            prop-rel:isIndexed false ],
        [ prop-rel:fromProperty indo:data-quality-uncertainty-factor ;
            prop-rel:hasBinding [ prov:wasDerivedFrom ind:quality-adjusted-biomass-effect ;
                    prop-rel:bindingRole <file:///github/workspace/primary> ;
                    prop-rel:bindingValidityScope "Computed at run-time as 1 - mean(QI_lineage, QI_representativeness, QI_temporal, QI_spatial, QI_method, QI_uncertainty); see dataset-qa skill output for per-input values." ;
                    prop-rel:bindingVariable indo:data-quality-uncertainty-factor ] ;
            prop-rel:hasDimensionKind quantitykind:Dimensionless ;
            prop-rel:hasEquationRole <file:///github/workspace/uncertaintyTerm> ;
            prop-rel:hasOperator <file:///github/workspace/product> ;
            prop-rel:hasSymbol "U" ;
            prop-rel:hasSymbolAlias "U_data",
                "U_{data}" ;
            prop-rel:hasVariableKind <file:///github/workspace/uncertaintyFactor> ;
            prop-rel:isIndexed false ] ;
    prop-rel:targetDefinition ind:quality-adjusted-biomass-effect ;
    prop-rel:toProperty ind:quality-adjusted-biomass-effect .

<https://example.org/norwegian-ses/utsira-biomass-upscaler-v1> rdfs:label "Utsira biomass upscaler v1" ;
    dct:identifier "utsira-biomass-upscaler-v1" .

ind:quality-adjusted-biomass-effect a prov:Entity ;
    prov:wasDerivedFrom indo:data-quality-uncertainty-factor,
        ind:wind-park-biomass-effect ;
    schema:mathExpression "B_{qa} = B_{total} \\cdot (1 - U)" .


```

## Schema

```yaml
type: object
required:
- toProperty
- equation
- symbols
- model
properties:
  id:
    $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
    description: Identifier (IRI or CURIE) for this equation record.
    x-jsonld-id: '@id'
  type:
    description: Relationship type. Use EquationPropertyRelationship, optionally alongside
      PropertyRelationship.
    oneOf:
    - const: EquationPropertyRelationship
    - type: array
      contains:
        const: EquationPropertyRelationship
      items:
        type: string
    x-jsonld-id: '@type'
  relationshipKind:
    const: equation
    description: Discriminator for equation-based relationships.
    x-jsonld-id: https://schema.org/additionalType
  fromProperty:
    $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
    description: "Optional. Use when the record focuses on one specific symbol-edge
      of the equation (a sensitivity / cross-impact reading); it must then match exactly
      one entry in `symbols[]` by its `fromProperty`. Omit when the record describes
      the equation as a whole \u2014 the full table is in `symbols[]` and there is
      no single \"from\".\n"
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/fromProperty
    x-jsonld-type: '@id'
  toProperty:
    $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
    description: IRI or CURIE of the derived target property calculated by the equation.
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/toProperty
    x-jsonld-type: '@id'
  equation:
    type: string
    minLength: 1
    description: Canonical mathematical expression. It should match schema:mathExpression
      on the target property definition.
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/hasEquation
  symbols:
    type: array
    minItems: 1
    description: 'Complete symbol table for `equation`: one entry per symbol used
      in the expression. For equation-level records, top-level `fromProperty` is omitted
      and `symbols[]` is the full computable table. For symbol-centred records, the
      primary symbol is the entry whose `fromProperty` equals top-level `fromProperty`;
      the other entries remain in the table so the record is computationally self-contained.

      '
    items:
      type: object
      required:
      - symbol
      - fromProperty
      - bindings
      properties:
        symbol:
          type: string
          minLength: 1
          description: LaTeX symbol as it occurs literally in `equation`.
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/hasSymbol
        symbolAliases:
          type: array
          description: Alternative renderings (ASCII variants, plain forms).
          items:
            type: string
            minLength: 1
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/hasSymbolAlias
          x-jsonld-container: '@set'
        fromProperty:
          $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
          description: Abstract Rainbow IRI for this symbol.
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/fromProperty
          x-jsonld-type: '@id'
        variableKind:
          type: string
          enum:
          - featureOfInterest
          - intensiveQuantity
          - extensiveQuantity
          - adjustmentFactor
          - timeCoefficient
          - rateCoefficient
          - uncertaintyFactor
          - aggregationIndex
          description: 'Semantic role of the symbol in the equation.

            '
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/hasVariableKind
          x-jsonld-type: '@vocab'
        dimensionKind:
          $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
          description: 'Unit-abstract dimensional type as a QUDT QuantityKind URI
            (e.g. `quantitykind:Area`, `quantitykind:SurfaceDensity`, `quantitykind:Dimensionless`,
            `quantitykind:Time`, `quantitykind:Frequency`). Decouples dimensional
            analysis from unit selection.

            '
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/hasDimensionKind
          x-jsonld-type: '@id'
        indexed:
          type: boolean
          default: false
          description: 'True if the term is iterated under the aggregation index of
            toProperty (e.g. per-taxon `D_{pre,i}`).

            '
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/isIndexed
        index:
          type: string
          description: Index symbol, e.g. "i". Only meaningful when `indexed` is true.
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/hasIndex
        indexedBy:
          $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
          description: 'IRI of the entity class whose instances enumerate the index
            (e.g. `odd:TaxonGroup`). Required when `indexed` is true.

            '
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/hasIndexedBy
          x-jsonld-type: '@id'
        equationRole:
          type: string
          enum:
          - input
          - coefficient
          - normaliser
          - lossTerm
          - uncertaintyTerm
          - qualityTerm
          - output
          - other
          description: Role this symbol plays in the equation.
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/hasEquationRole
          x-jsonld-type: '@vocab'
        operator:
          type: string
          enum:
          - sum
          - product
          - subtract
          - divide
          - transform
          - weightedSum
          - other
          description: Main operation connecting this symbol to the equation.
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/hasOperator
          x-jsonld-type: '@vocab'
        bindings:
          type: array
          minItems: 1
          description: 'Concrete vocabulary IRIs that realise the abstract `fromProperty`
            of this symbol. Use when one symbol expands over an index (per-taxon,
            per-region), or when alternate / fallback measurements exist.

            '
          items:
            type: object
            required:
            - variable
            properties:
              variable:
                $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
                description: Concrete Rainbow IRI realising the entry's fromProperty.
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/bindingVariable
                x-jsonld-type: '@id'
              indexValue:
                type: string
                description: Value of the equation index variable (e.g. "Mytilus edulis").
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/bindingIndexValue
              bindingRole:
                type: string
                enum:
                - primary
                - alternate
                - fallback
                - expansion
                default: primary
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/bindingRole
                x-jsonld-type: '@vocab'
              validityScope:
                type: string
                description: Short scope note (region, scenario, season).
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/bindingValidityScope
              evidence:
                oneOf:
                - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
                - type: array
                  items:
                    $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
                x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
                x-jsonld-type: '@id'
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/hasBinding
          x-jsonld-container: '@set'
        explanation:
          type: string
          description: Human-readable note about this symbol.
          x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#comment
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/hasEquationSymbol
    x-jsonld-container: '@set'
  weight:
    description: Optional sensitivity or coefficient value. In this profile it is
      not a causal cross-impact weight.
    type: object
    required:
    - value
    properties:
      value:
        type: number
        description: Numeric sensitivity or coefficient value.
        x-jsonld-id: http://qudt.org/schema/qudt/numericValue
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/hasWeight
    x-jsonld-type: '@id'
  model:
    description: Model that defines or evaluates this equation relationship (prov:wasAttributedTo).
    type: object
    required:
    - id
    properties:
      id:
        type: string
        description: Identifier of the model (dct:identifier).
        x-jsonld-id: http://purl.org/dc/terms/identifier
      name:
        type: string
        description: Human-readable label of the model (rdfs:label).
        x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#label
      uri:
        type: string
        description: URI of the model resource.
        x-jsonld-id: '@id'
    x-jsonld-id: http://www.w3.org/ns/prov#wasAttributedTo
  experiment:
    description: Experiment activity that evaluated this relationship (prov:wasGeneratedBy).
    type: object
    required:
    - id
    properties:
      id:
        type: string
        description: Identifier of the experiment (dct:identifier).
        x-jsonld-id: http://purl.org/dc/terms/identifier
      name:
        type: string
        description: Human-readable label of the experiment (rdfs:label).
        x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#label
      uri:
        type: string
        description: URI of the experiment resource.
        x-jsonld-id: '@id'
      start:
        type: string
        format: date-time
        pattern: ^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})?$
        description: Date and time when the experiment started (prov:startedAtTime).
        x-jsonld-id: http://www.w3.org/ns/prov#startedAtTime
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
      end:
        type: string
        format: date-time
        pattern: ^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})?$
        description: Date and time when the experiment ended (prov:endedAtTime).
        x-jsonld-id: http://www.w3.org/ns/prov#endedAtTime
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
    x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
  evidence:
    oneOf:
    - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
    - type: array
      items:
        $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
    description: Evidence or definition source for the equation relationship.
    x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
    x-jsonld-type: '@id'
  explanation:
    type: string
    description: Human-readable explanation of how the primary fromProperty participates
      in the equation.
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#comment
additionalProperties: true
x-jsonld-extra-terms:
  PropertyRelationship: https://w3id.org/ogc/hosted/seadots/prop-rel/PropertyRelationship
  EquationPropertyRelationship: https://w3id.org/ogc/hosted/seadots/prop-rel/EquationPropertyRelationship
  targetDefinition:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/targetDefinition
    x-jsonld-context:
      id: '@id'
      type: '@type'
      name: http://www.w3.org/2000/01/rdf-schema#label
      mathExpression: https://schema.org/mathExpression
      wasDerivedFrom:
        '@id': http://www.w3.org/ns/prov#wasDerivedFrom
        '@type': '@id'
        '@container': '@set'
      aggregation:
        '@id': https://w3id.org/ogc/hosted/seadots/prop-rel/hasAggregation
        '@context':
          type: '@type'
          operator:
            '@id': https://w3id.org/ogc/hosted/seadots/prop-rel/aggregationOperator
            '@type': '@id'
          aggregatesOver:
            '@id': https://w3id.org/ogc/hosted/seadots/prop-rel/aggregatesOver
            '@type': '@id'
          indexSymbol: https://w3id.org/ogc/hosted/seadots/prop-rel/indexSymbol
x-jsonld-prefixes:
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  prop-rel: https://w3id.org/ogc/hosted/seadots/prop-rel/
  schema: https://schema.org/
  prov: http://www.w3.org/ns/prov#
  qudt: http://qudt.org/schema/qudt/
  dct: http://purl.org/dc/terms/
  xsd: http://www.w3.org/2001/XMLSchema#
  quantitykind: http://qudt.org/vocab/quantitykind/
  odd: https://w3id.org/iliad/odd#
  tc: http://rs.tdwg.org/ontology/voc/TaxonConcept#
  indo: https://w3id.org/indicators/marine/obs/
  ind: https://w3id.org/indicators/marine/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/equation-property-relationship/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/equation-property-relationship/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "PropertyRelationship": "prop-rel:PropertyRelationship",
    "EquationPropertyRelationship": "prop-rel:EquationPropertyRelationship",
    "targetDefinition": {
      "@id": "prop-rel:targetDefinition",
      "@context": {
        "name": "rdfs:label",
        "mathExpression": "schema:mathExpression",
        "wasDerivedFrom": {
          "@id": "prov:wasDerivedFrom",
          "@type": "@id",
          "@container": "@set"
        },
        "aggregation": {
          "@id": "prop-rel:hasAggregation",
          "@context": {
            "operator": {
              "@id": "prop-rel:aggregationOperator",
              "@type": "@id"
            },
            "aggregatesOver": {
              "@id": "prop-rel:aggregatesOver",
              "@type": "@id"
            },
            "indexSymbol": "prop-rel:indexSymbol"
          }
        }
      }
    },
    "id": "@id",
    "type": "@type",
    "relationshipKind": "schema:additionalType",
    "fromProperty": {
      "@id": "prop-rel:fromProperty",
      "@type": "@id"
    },
    "toProperty": {
      "@id": "prop-rel:toProperty",
      "@type": "@id"
    },
    "equation": "prop-rel:hasEquation",
    "symbols": {
      "@context": {
        "symbol": "prop-rel:hasSymbol",
        "symbolAliases": {
          "@id": "prop-rel:hasSymbolAlias",
          "@container": "@set"
        },
        "variableKind": {
          "@id": "prop-rel:hasVariableKind",
          "@type": "@vocab"
        },
        "dimensionKind": {
          "@id": "prop-rel:hasDimensionKind",
          "@type": "@id"
        },
        "indexed": "prop-rel:isIndexed",
        "index": "prop-rel:hasIndex",
        "indexedBy": {
          "@id": "prop-rel:hasIndexedBy",
          "@type": "@id"
        },
        "equationRole": {
          "@id": "prop-rel:hasEquationRole",
          "@type": "@vocab"
        },
        "operator": {
          "@id": "prop-rel:hasOperator",
          "@type": "@vocab"
        },
        "bindings": {
          "@context": {
            "variable": {
              "@id": "prop-rel:bindingVariable",
              "@type": "@id"
            },
            "indexValue": "prop-rel:bindingIndexValue",
            "bindingRole": {
              "@id": "prop-rel:bindingRole",
              "@type": "@vocab"
            },
            "validityScope": "prop-rel:bindingValidityScope"
          },
          "@id": "prop-rel:hasBinding",
          "@container": "@set"
        }
      },
      "@id": "prop-rel:hasEquationSymbol",
      "@container": "@set"
    },
    "weight": {
      "@context": {
        "value": "qudt:numericValue"
      },
      "@id": "prop-rel:hasWeight",
      "@type": "@id"
    },
    "model": {
      "@context": {
        "id": "dct:identifier",
        "name": "rdfs:label",
        "uri": "@id"
      },
      "@id": "prov:wasAttributedTo"
    },
    "experiment": {
      "@context": {
        "id": "dct:identifier",
        "name": "rdfs:label",
        "uri": "@id",
        "start": {
          "@id": "prov:startedAtTime",
          "@type": "xsd:dateTime"
        },
        "end": {
          "@id": "prov:endedAtTime",
          "@type": "xsd:dateTime"
        }
      },
      "@id": "prov:wasGeneratedBy"
    },
    "evidence": {
      "@id": "prov:wasDerivedFrom",
      "@type": "@id"
    },
    "explanation": "rdfs:comment",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "prop-rel": "https://w3id.org/ogc/hosted/seadots/prop-rel/",
    "schema": "https://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "qudt": "http://qudt.org/schema/qudt/",
    "dct": "http://purl.org/dc/terms/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "quantitykind": "http://qudt.org/vocab/quantitykind/",
    "odd": "https://w3id.org/iliad/odd#",
    "tc": "http://rs.tdwg.org/ontology/voc/TaxonConcept#",
    "indo": "ind:obs/",
    "ind": "https://w3id.org/indicators/marine/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/equation-property-relationship/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/equation-property-relationship`

