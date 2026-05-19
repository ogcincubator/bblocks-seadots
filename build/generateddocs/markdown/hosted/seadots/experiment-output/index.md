
# Computational Experiment Output (Schema)

`ogc.hosted.seadots.experiment-output` *v0.2*

OGC API Records profile for describing a single output artefact produced by a computational experiment. Captures the kind of output (primary result, catalog, provenance), the format, the vocabulary term for the produced quantity, and the URI of the experiment that produced it. Carries inline result values with mandatory provenance (computed / retrieved / illustrative / mixed). Designed to be referenced by an `experiment` record so that one output definition can be reused across runs and audits.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Computational Experiment Output

OGC API Records profile for one output artefact produced by a computational experiment.

Each instance describes a single output — a primary result file, a catalog, or a provenance record. The schema is intentionally narrow so that an `experiment` record can reference many `experiment-output` records by URI and an audit pipeline can resolve each artefact independently.

Captured fields:

1. **Role** — `primary result`, `catalog`, `provenance`, `diagnostic`. Mirrors the `role` field used on the per-class input records.
2. **Format** — media type or URI for the artefact's format profile (e.g. `application/json`, `application/ld+json`, `application/x-netcdf`, or an OGC format URI). Pick the value that matches what the file *is*, not what it conceptually describes.
3. **Vocabulary term** — concept URI for the produced quantity (e.g. `floating-wind-reef-biomass`).
4. **Experiment** — URI of the `experiment` record that produced this output.
5. **Conformance** — optional list of conformance class URIs (e.g. the SeaDOTs EDITO output conventions, STAC version).
6. **Inline data** — every example MUST embed representative result values inside the `data` object so a reader can see what the output actually carries. Same `provenance` requirement as the per-class input bblocks — see the worked example below.

Outputs may be self-contained datasets, references to STAC collections, or PROV-O records that close the loop back to the experiment's inputs and the modelled equation.

---

## Worked example — reef-biomass result for the Utsira surroundings experiment

The example `examples/reef_biomass_result.json` is the primary result of the experiment described in `_sources/experiment/examples/utsira_surroundings_experiment.json`. It evaluates the reef-biomass equation

$$B_{reef}(t) \;=\; \sum_i \bigl( A_{sub} \cdot D_{pre,i} \cdot AF_i \cdot C_t \bigr)$$

over the scenario time span (2026-05-13 → 2028-05-13, 24 months) using the input records in the six per-input bblocks (`_sources/area-of-interest`, `floating-wind-infrastructure`, `benthic-biomass-density-mareano`, `benthic-biomass-density-imr`, `reef-aggregation-index`, `colonisation-time-factor`). Every variable is traceable to a specific input record; every value below carries an explicit provenance flag.

### Inputs and where they come from

| Symbol | Value | Source record | Field path | Provenance tag |
|---|---:|---|---|---|
| `A_sub` | 109 500 m² | `infrastructure_layout_60x15mw.json` | `data.aggregate.submerged_area_total_m2` | mixed (60 units × 1825 m²; design real, per-unit area illustrative) |
| `D_pre,Mytilus` | 0.42 kg m⁻² | `mareano_baseline_density.json` | `data.perTaxon[0].density_kg_m2` | illustrative |
| `D_pre,Buccinum` | 0.11 kg m⁻² | `mareano_baseline_density.json` | `data.perTaxon[1].density_kg_m2` | illustrative |
| `D_pre,Asterias` | 0.28 kg m⁻² | `mareano_baseline_density.json` | `data.perTaxon[2].density_kg_m2` | illustrative |
| `AF_Mytilus` | 12.0 | `reef_aggregation_index_bindings.json` | `data.perTaxon[0].AF_i` | illustrative |
| `AF_Buccinum` | 3.5 | same | `data.perTaxon[1].AF_i` | illustrative |
| `AF_Asterias` | 5.0 | same | `data.perTaxon[2].AF_i` | illustrative |
| `C_t(24 mo)` | 0.9918 | `colonisation_time_factor.json` | analytic from `data.parameters` (L=1.0, k=0.30, t₀=8 mo) | illustrative |

### Step-by-step calculation at t = 24 months

```
B_Mytilus   = 109 500 · 0.42 · 12.0 · 0.9918 = 547 375 kg
B_Buccinum  = 109 500 · 0.11 ·  3.5 · 0.9918 =  41 813 kg
B_Asterias  = 109 500 · 0.28 ·  5.0 · 0.9918 = 152 049 kg
                                              ─────────
B_reef(24)  =                                  741 237 kg  ≈ 741.2 t
```

### Time series

Refactor as $B_{reef}(t) = A_{sub} \cdot C_t \cdot S$ with $S = \sum_i D_{pre,i} \cdot AF_i = 6.825$ kg m⁻². Evaluate at the sigmoid-lookup points published in `colonisation_time_factor.json → data.lookup`:

| t (months) | C_t | B_reef (t) |
|---:|---:|---:|
| 0 | 0.08 | 59.8 |
| 6 | 0.32 | 239.1 |
| 12 | 0.71 | 530.6 |
| 18 | 0.93 | 695.0 |
| 24 | 0.99 | 739.9 |

### Uncertainty propagation

**Method.** Log-linear coefficient-of-variation (CV) propagation. For multiplicative terms under independence: $\text{CV}^2(XY) \approx \text{CV}^2(X) + \text{CV}^2(Y)$. Valid while CVs remain ≲ 0.5; for the assumed AF CV of exactly 0.5, the linearisation slightly under-states the upper tail — a Monte Carlo cross-check would be the obvious refinement.

**Refactoring for shared factors.** `A_sub` and `C_t` are scalar factors shared across all taxa, so they enter once (not three times). `D_pre,i` and `AF_i` vary per taxon and are treated independent across i.

$$B_{reef} = A_{sub} \cdot C_t \cdot \underbrace{\textstyle\sum_i D_{pre,i} \cdot AF_i}_{S}$$

**Per-variable σ and CV.**

| Variable | σ (absolute) | CV = σ/μ | σ source |
|---|---|---:|---|
| `A_sub` | 16 425 m² | 0.150 | **assumed** — no σ in input file; 15 % is a typical engineering tolerance for floating-platform wetted area. |
| `D_pre,Mytilus` | 0.09 kg m⁻² | 0.214 | `imr_baseline_density_fallback.json → data.perTaxon[0].uncertainty_kg_m2` (proxy — MAREANO row carries no σ) |
| `D_pre,Buccinum` | 0.03 kg m⁻² | 0.273 | same, row [1] |
| `D_pre,Asterias` | 0.06 kg m⁻² | 0.214 | same, row [2] |
| `AF_i` (all taxa) | — | 0.500 | **assumed** — no σ in input file; Degraer 2020 cites a single value with no spread; CV ≈ 0.5 reflects literature-wide variance. |
| `C_t(24 mo)` | 0.02 | 0.020 | **assumed** — near sigmoid saturation, σ small. |

**Variance accumulation.**

$$\sigma^2(D_i \cdot AF_i) \;=\; (D_i \cdot AF_i)^2 \cdot \bigl(\text{CV}^2(D_i) + \text{CV}^2(AF_i)\bigr)$$

| Taxon | (D·AF)² | CV²_D + CV²_AF | σ²(D·AF) |
|---|---:|---:|---:|
| Mytilus | 25.40 | 0.046 + 0.250 = 0.296 | **7.517** |
| Buccinum | 0.148 | 0.074 + 0.250 = 0.324 | **0.048** |
| Asterias | 1.96 | 0.046 + 0.250 = 0.296 | **0.580** |
| **σ²(S)** | | | **8.145** |

$\sigma(S) = 2.854$, $\text{CV}(S) = 0.418$.

$$\text{CV}^2(B_{reef}) \;=\; 0.0225 \;+\; 0.0004 \;+\; 0.1749 \;=\; 0.1978$$

$$\text{CV}(B_{reef}) \;=\; 0.445 \quad\Rightarrow\quad \sigma(B_{reef}) \;=\; 329.6 \ \text{t}$$

### Headline result

$$\boxed{\ B_{reef}(24\ \text{mo}) \;=\; 741 \;\pm\; 330 \ \text{t}\ \ (1\sigma) \;=\; 741 \ \text{t}\ \bigl[95\%\ \text{CI}:\ 95\!-\!1\,387\ \text{t}\bigr]\ }$$

### Variance attribution

| Term | Share of CV²(B_reef) |
|---|---:|
| `A_sub` | 11.4 % |
| `C_t` | 0.2 % |
| `S = Σᵢ Dᵢ·AFᵢ` | **88.4 %** |
| └─ *Mytilus edulis* contribution within S | 92.3 % |
| └─ *Asterias rubens* contribution within S | 7.1 % |
| └─ *Buccinum undatum* contribution within S | 0.6 % |

≈ **80 % of total uncertainty in B_reef comes from `AF_Mytilus`** (the assumed CV = 0.5 against the dominant D·AF product). Tightening that single prior pays back ~4× more than tightening any other input.

### Caveats — read before quoting any number

- Every headline value above is downstream of `illustrative` inputs. The 741 ± 330 t result is a *demonstration that the pipeline propagates correctly*, not a measurement.
- Three σ values are **assumed** (`σ(A_sub)/A_sub`, `σ(AF_i)/AF_i`, `σ(C_t)`). They are flagged in the example's `data.uncertainty.inputs[*].sigmaSource`.
- The MAREANO row has no σ; IMR's σ is borrowed as a proxy.
- Independence is optimistic — AF_i errors plausibly correlate across taxa (shared monitoring programmes, depth bands). Correlated AF errors would inflate σ(S) above 2.854.
- B_reef is a standing-stock quantity. A time-integrated "reef-effect-years" requires integrating the sigmoid; central-value estimate ≈ 9 800 t·month over 24 months.

## Examples

### Reef-associated biomass — structured result (JSON)
#### json
```json
{
  "id": "https://example.org/norwegian-ses/experiment-output/reef-biomass-result",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [4.20, 59.10],
      [5.30, 59.10],
      [5.30, 59.70],
      [4.20, 59.70],
      [4.20, 59.10]
    ]]
  },
  "properties": {
    "type": "Dataset",
    "title": "Reef-associated biomass result — Utsira surroundings, scenario T0+24 mo (with uncertainty)",
    "description": "Primary scientific output of the Utsira surroundings reef-biomass experiment. Headline value: 741 ± 330 t standing reef-associated biomass at scenario end (24 months). This file is an OGC API Records Feature (JSON) carrying the full structured result inline: (a) the headline scalar with 1σ and 95 % CI, (b) the per-taxon decomposition at t=24 mo, (c) the time series at the sigmoid-lookup points, (d) full variance attribution by input, and (e) per-variable provenance. All input values are illustrative; this record demonstrates equation evaluation and uncertainty propagation, not a measurement of Utsira.",
    "created": "2026-05-19",
    "updated": "2026-05-19",
    "language": { "code": "en" },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "themes": [
      { "concepts": [{ "id": "reef-effect", "label": "Floating-wind reef effect" }], "scheme": "https://id3.seadots.eu/themes" }
    ],
    "keywords": ["reef biomass", "Utsira", "floating wind", "uncertainty", "CV propagation"],
    "formats": [{ "mediaType": "application/json" }],
    "experimentOutput": {
      "name": "Reef-associated biomass (structured result)",
      "description": "B_reef headline scalar, per-taxon decomposition, time series, and variance attribution. Sum-over-taxa of A_sub · D_pre,i · AF_i · C_t evaluated at scenario end. All values emitted inline as JSON.",
      "role": "primary result",
      "format": "application/json",
      "vocabularyTerm": "https://id3.seadots.eu/indicator/floating-wind-reef-biomass",
      "experiment": "https://example.org/norwegian-ses/experiment/utsira-reef-biomass-surroundings-v1",
      "observedProperty": "https://id3.seadots.eu/indicator/floating-wind-reef-biomass",
      "hasSimpleResult": 741237,
      "hasSimpleResultUnit": "kg",
      "resultTime": "2028-05-13T00:00:00Z",
      "phenomenonTime": { "start": "2026-05-13T00:00:00Z", "end": "2028-05-13T00:00:00Z" },
      "hasFeatureOfInterest": "https://example.org/norwegian-ses/area-of-interest/utsira-surroundings",
      "conformsTo": [
        "https://ogcincubator.github.io/geodcat-ogcapi-records/",
        "https://w3id.org/ogc/hosted/iliad/oim-obs",
        "http://www.w3.org/ns/sosa/Observation",
        "https://id3.seadots.eu/conventions/edito-output"
      ],
      "aggregation": "sum-over-i",
      "data": {
        "equation": "B_reef(t) = Σ_i (A_sub · D_pre,i · AF_i · C_t)",
        "asOf_months": 24,
        "scenarioInterval": ["2026-05-13", "2028-05-13"],
        "units": "kg",

        "headline": {
          "B_reef_kg": 741237,
          "B_reef_tonnes": 741.2,
          "sigma_kg": 329632,
          "sigma_tonnes": 329.6,
          "CV": 0.445,
          "ci95_tonnes": [95, 1387],
          "ci95_kg": [95198, 1387276]
        },

        "perTaxonAtT24": [
          {
            "scientificName": "Mytilus edulis",
            "aphiaID": 140480,
            "A_sub_m2": 109500,
            "D_pre_kg_m2": 0.42,
            "AF_i": 12.0,
            "C_t": 0.9918,
            "B_kg": 547375,
            "shareOfTotal": 0.7385
          },
          {
            "scientificName": "Buccinum undatum",
            "aphiaID": 138878,
            "A_sub_m2": 109500,
            "D_pre_kg_m2": 0.11,
            "AF_i": 3.5,
            "C_t": 0.9918,
            "B_kg": 41813,
            "shareOfTotal": 0.0564
          },
          {
            "scientificName": "Asterias rubens",
            "aphiaID": 123776,
            "A_sub_m2": 109500,
            "D_pre_kg_m2": 0.28,
            "AF_i": 5.0,
            "C_t": 0.9918,
            "B_kg": 152049,
            "shareOfTotal": 0.2051
          }
        ],

        "timeSeries": [
          { "t_months": 0,  "C_t": 0.08, "B_reef_kg":  59787, "B_reef_tonnes":  59.8 },
          { "t_months": 6,  "C_t": 0.32, "B_reef_kg": 239148, "B_reef_tonnes": 239.1 },
          { "t_months": 12, "C_t": 0.71, "B_reef_kg": 530610, "B_reef_tonnes": 530.6 },
          { "t_months": 18, "C_t": 0.93, "B_reef_kg": 695024, "B_reef_tonnes": 695.0 },
          { "t_months": 24, "C_t": 0.99, "B_reef_kg": 739864, "B_reef_tonnes": 739.9 }
        ],
        "timeSeriesNote": "B_reef_kg above uses the rounded C_t values from `colonisation_time_factor.json → data.lookup`. The `headline` and `perTaxonAtT24` use the analytic C(24)=0.9918 from the sigmoid; the two agree at three significant figures.",

        "uncertainty": {
          "method": "log-linear CV propagation",
          "methodDetail": "B_reef = A_sub · C_t · S, with S = Σᵢ Dᵢ·AFᵢ. For each multiplicative pair under independence: CV²(XY) ≈ CV²(X) + CV²(Y). For S: σ²(S) = Σᵢ σ²(Dᵢ·AFᵢ) with the three taxa treated independent. AF_i errors are not in fact independent across taxa (likely correlated through shared monitoring programmes) — this is acknowledged in `caveats` and inflates the reported σ as an upper-bound estimate of total uncertainty.",
          "totalCV": 0.445,
          "totalSigma_kg": 329632,
          "totalSigma_tonnes": 329.6,

          "inputs": [
            {
              "variable": "A_sub",
              "value": 109500, "valueUnits": "m^2",
              "sigma": 16425, "CV": 0.150,
              "valueSource": "infrastructure_layout_60x15mw.json:data.aggregate.submerged_area_total_m2",
              "valueKind": "mixed",
              "sigmaSource": "assumed (15% engineering tolerance for floating-platform wetted area; no σ in input record)",
              "sigmaKind": "assumed"
            },
            {
              "variable": "D_pre,Mytilus edulis",
              "value": 0.42, "valueUnits": "kg m^-2",
              "sigma": 0.09, "CV": 0.214,
              "valueSource": "mareano_baseline_density.json:data.perTaxon[0].density_kg_m2",
              "valueKind": "illustrative",
              "sigmaSource": "imr_baseline_density_fallback.json:data.perTaxon[0].uncertainty_kg_m2 (proxy — MAREANO row carries no σ)",
              "sigmaKind": "illustrative-proxy"
            },
            {
              "variable": "D_pre,Buccinum undatum",
              "value": 0.11, "valueUnits": "kg m^-2",
              "sigma": 0.03, "CV": 0.273,
              "valueSource": "mareano_baseline_density.json:data.perTaxon[1].density_kg_m2",
              "valueKind": "illustrative",
              "sigmaSource": "imr_baseline_density_fallback.json:data.perTaxon[1].uncertainty_kg_m2",
              "sigmaKind": "illustrative-proxy"
            },
            {
              "variable": "D_pre,Asterias rubens",
              "value": 0.28, "valueUnits": "kg m^-2",
              "sigma": 0.06, "CV": 0.214,
              "valueSource": "mareano_baseline_density.json:data.perTaxon[2].density_kg_m2",
              "valueKind": "illustrative",
              "sigmaSource": "imr_baseline_density_fallback.json:data.perTaxon[2].uncertainty_kg_m2",
              "sigmaKind": "illustrative-proxy"
            },
            {
              "variable": "AF_Mytilus edulis",
              "value": 12.0, "valueUnits": "dimensionless",
              "sigma": 6.0, "CV": 0.500,
              "valueSource": "reef_aggregation_index_bindings.json:data.perTaxon[0].AF_i",
              "valueKind": "illustrative",
              "sigmaSource": "assumed (CV=0.5 reflects wide literature variance; Degraer 2020 cites a single Mytilus value with no published spread)",
              "sigmaKind": "assumed"
            },
            {
              "variable": "AF_Buccinum undatum",
              "value": 3.5, "valueUnits": "dimensionless",
              "sigma": 1.75, "CV": 0.500,
              "valueSource": "reef_aggregation_index_bindings.json:data.perTaxon[1].AF_i",
              "valueKind": "illustrative",
              "sigmaSource": "assumed (CV=0.5; no published value for Buccinum in Degraer 2020)",
              "sigmaKind": "assumed"
            },
            {
              "variable": "AF_Asterias rubens",
              "value": 5.0, "valueUnits": "dimensionless",
              "sigma": 2.5, "CV": 0.500,
              "valueSource": "reef_aggregation_index_bindings.json:data.perTaxon[2].AF_i",
              "valueKind": "illustrative",
              "sigmaSource": "assumed (CV=0.5; no published value for Asterias in Degraer 2020)",
              "sigmaKind": "assumed"
            },
            {
              "variable": "C_t(24 mo)",
              "value": 0.9918, "valueUnits": "dimensionless",
              "sigma": 0.02, "CV": 0.020,
              "valueSource": "colonisation_time_factor.json:data.formula evaluated with parameters {L:1.0, k:0.30, t0_months:8}",
              "valueKind": "illustrative",
              "sigmaSource": "assumed (near sigmoid saturation; small σ)",
              "sigmaKind": "assumed"
            }
          ],

          "perTaxonVariance": [
            {
              "scientificName": "Mytilus edulis",
              "D_times_AF": 5.040,
              "var_D_times_AF": 7.517,
              "shareWithinS": 0.9229
            },
            {
              "scientificName": "Buccinum undatum",
              "D_times_AF": 0.385,
              "var_D_times_AF": 0.048,
              "shareWithinS": 0.0059
            },
            {
              "scientificName": "Asterias rubens",
              "D_times_AF": 1.400,
              "var_D_times_AF": 0.580,
              "shareWithinS": 0.0712
            }
          ],
          "S_value_kg_m2": 6.825,
          "S_sigma_kg_m2": 2.854,
          "S_CV": 0.418,

          "varianceAttribution": [
            { "term": "A_sub",          "CV_squared": 0.0225, "shareOfTotal": 0.1137 },
            { "term": "C_t",            "CV_squared": 0.0004, "shareOfTotal": 0.0020 },
            { "term": "S = Σᵢ Dᵢ·AFᵢ",  "CV_squared": 0.1749, "shareOfTotal": 0.8842 }
          ],
          "dominantUncertainty": "AF_Mytilus edulis accounts for ≈80 % of total CV²(B_reef). Tightening that single prior pays back ~4× more than tightening any other input."
        },

        "caveats": [
          "Every headline number is downstream of illustrative inputs. This record demonstrates equation evaluation and CV propagation; it is NOT a measurement of Utsira.",
          "Three σ values are assumed (σ(A_sub)=15%, σ(AF_i)/AF_i=0.5 for all taxa, σ(C_t)=0.02). Flagged in `data.uncertainty.inputs[*].sigmaKind`.",
          "The MAREANO row carries no σ; IMR's σ is borrowed as a proxy. Real σ should come from the same retrieval that produced the density.",
          "Independence across taxa is optimistic. AF_i errors plausibly correlate through shared monitoring programmes; correlated errors would inflate σ(S) above 2.854.",
          "B_reef is a standing-stock quantity. A time-integrated 'reef-effect-years' (∫₀²⁴ B_reef(t) dt) is ≈ 9800 t·month at central values."
        ],

        "provenance": {
          "values": "computed",
          "derivedFrom": [
            "https://example.org/norwegian-ses/floating-wind-infrastructure/utsira-nord-60x15mw",
            "https://example.org/norwegian-ses/benthic-biomass-density-mareano/norwegian-shelf",
            "https://example.org/norwegian-ses/benthic-biomass-density-imr/ices-iva-fallback",
            "https://example.org/norwegian-ses/reef-aggregation-index/degraer2020-bindings",
            "https://example.org/norwegian-ses/colonisation-time-factor/default-sigmoid",
            "https://example.org/norwegian-ses/area-of-interest/utsira-surroundings"
          ],
          "equationRecord": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
          "computedOn": "2026-05-19",
          "computeCode": "../../experiment/scripts/utsira_reef_biomass.py",
          "computeCodeNote": "Standalone Python script. Loads the six per-class input records, evaluates the equation at t=24 mo, propagates uncertainty by log-linear CV, and emits this output. Run: `python3 _sources/experiment/scripts/utsira_reef_biomass.py --json` to regenerate this JSON.",
          "uncertaintyMethod": "log-linear CV propagation; B_reef = A_sub · C_t · Σᵢ Dᵢ·AFᵢ; taxa treated independent within S",
          "note": "Values are deterministic results of applying the cited equation to the input records listed in `derivedFrom`. Input values are themselves illustrative (see each input record's `data.provenance`), so this output's `values: computed` flag refers to the calculation chain, not to a real-world measurement."
        }
      }
    }
  },
  "links": [
    { "rel": "describedby", "href": "bblocks://ogc.hosted.seadots.experiment-output", "type": "application/schema+json", "title": "Experiment-output bblock" },
    { "rel": "derivedFrom", "href": "https://example.org/norwegian-ses/experiment/utsira-reef-biomass-surroundings-v1", "type": "application/json", "title": "Experiment record this output belongs to" },
    { "rel": "cite-as",    "href": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation", "type": "application/ld+json", "title": "Equation evaluated to produce this result" }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/experiment-output/context.jsonld",
  "id": "https://example.org/norwegian-ses/experiment-output/reef-biomass-result",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          4.2,
          59.1
        ],
        [
          5.3,
          59.1
        ],
        [
          5.3,
          59.7
        ],
        [
          4.2,
          59.7
        ],
        [
          4.2,
          59.1
        ]
      ]
    ]
  },
  "properties": {
    "type": "Dataset",
    "title": "Reef-associated biomass result \u2014 Utsira surroundings, scenario T0+24 mo (with uncertainty)",
    "description": "Primary scientific output of the Utsira surroundings reef-biomass experiment. Headline value: 741 \u00b1 330 t standing reef-associated biomass at scenario end (24 months). This file is an OGC API Records Feature (JSON) carrying the full structured result inline: (a) the headline scalar with 1\u03c3 and 95 % CI, (b) the per-taxon decomposition at t=24 mo, (c) the time series at the sigmoid-lookup points, (d) full variance attribution by input, and (e) per-variable provenance. All input values are illustrative; this record demonstrates equation evaluation and uncertainty propagation, not a measurement of Utsira.",
    "created": "2026-05-19",
    "updated": "2026-05-19",
    "language": {
      "code": "en"
    },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "themes": [
      {
        "concepts": [
          {
            "id": "reef-effect",
            "label": "Floating-wind reef effect"
          }
        ],
        "scheme": "https://id3.seadots.eu/themes"
      }
    ],
    "keywords": [
      "reef biomass",
      "Utsira",
      "floating wind",
      "uncertainty",
      "CV propagation"
    ],
    "formats": [
      {
        "mediaType": "application/json"
      }
    ],
    "experimentOutput": {
      "name": "Reef-associated biomass (structured result)",
      "description": "B_reef headline scalar, per-taxon decomposition, time series, and variance attribution. Sum-over-taxa of A_sub \u00b7 D_pre,i \u00b7 AF_i \u00b7 C_t evaluated at scenario end. All values emitted inline as JSON.",
      "role": "primary result",
      "format": "application/json",
      "vocabularyTerm": "https://id3.seadots.eu/indicator/floating-wind-reef-biomass",
      "experiment": "https://example.org/norwegian-ses/experiment/utsira-reef-biomass-surroundings-v1",
      "observedProperty": "https://id3.seadots.eu/indicator/floating-wind-reef-biomass",
      "hasSimpleResult": 741237,
      "hasSimpleResultUnit": "kg",
      "resultTime": "2028-05-13T00:00:00Z",
      "phenomenonTime": {
        "start": "2026-05-13T00:00:00Z",
        "end": "2028-05-13T00:00:00Z"
      },
      "hasFeatureOfInterest": "https://example.org/norwegian-ses/area-of-interest/utsira-surroundings",
      "conformsTo": [
        "https://ogcincubator.github.io/geodcat-ogcapi-records/",
        "https://w3id.org/ogc/hosted/iliad/oim-obs",
        "http://www.w3.org/ns/sosa/Observation",
        "https://id3.seadots.eu/conventions/edito-output"
      ],
      "aggregation": "sum-over-i",
      "data": {
        "equation": "B_reef(t) = \u03a3_i (A_sub \u00b7 D_pre,i \u00b7 AF_i \u00b7 C_t)",
        "asOf_months": 24,
        "scenarioInterval": [
          "2026-05-13",
          "2028-05-13"
        ],
        "units": "kg",
        "headline": {
          "B_reef_kg": 741237,
          "B_reef_tonnes": 741.2,
          "sigma_kg": 329632,
          "sigma_tonnes": 329.6,
          "CV": 0.445,
          "ci95_tonnes": [
            95,
            1387
          ],
          "ci95_kg": [
            95198,
            1387276
          ]
        },
        "perTaxonAtT24": [
          {
            "scientificName": "Mytilus edulis",
            "aphiaID": 140480,
            "A_sub_m2": 109500,
            "D_pre_kg_m2": 0.42,
            "AF_i": 12.0,
            "C_t": 0.9918,
            "B_kg": 547375,
            "shareOfTotal": 0.7385
          },
          {
            "scientificName": "Buccinum undatum",
            "aphiaID": 138878,
            "A_sub_m2": 109500,
            "D_pre_kg_m2": 0.11,
            "AF_i": 3.5,
            "C_t": 0.9918,
            "B_kg": 41813,
            "shareOfTotal": 0.0564
          },
          {
            "scientificName": "Asterias rubens",
            "aphiaID": 123776,
            "A_sub_m2": 109500,
            "D_pre_kg_m2": 0.28,
            "AF_i": 5.0,
            "C_t": 0.9918,
            "B_kg": 152049,
            "shareOfTotal": 0.2051
          }
        ],
        "timeSeries": [
          {
            "t_months": 0,
            "C_t": 0.08,
            "B_reef_kg": 59787,
            "B_reef_tonnes": 59.8
          },
          {
            "t_months": 6,
            "C_t": 0.32,
            "B_reef_kg": 239148,
            "B_reef_tonnes": 239.1
          },
          {
            "t_months": 12,
            "C_t": 0.71,
            "B_reef_kg": 530610,
            "B_reef_tonnes": 530.6
          },
          {
            "t_months": 18,
            "C_t": 0.93,
            "B_reef_kg": 695024,
            "B_reef_tonnes": 695.0
          },
          {
            "t_months": 24,
            "C_t": 0.99,
            "B_reef_kg": 739864,
            "B_reef_tonnes": 739.9
          }
        ],
        "timeSeriesNote": "B_reef_kg above uses the rounded C_t values from `colonisation_time_factor.json \u2192 data.lookup`. The `headline` and `perTaxonAtT24` use the analytic C(24)=0.9918 from the sigmoid; the two agree at three significant figures.",
        "uncertainty": {
          "method": "log-linear CV propagation",
          "methodDetail": "B_reef = A_sub \u00b7 C_t \u00b7 S, with S = \u03a3\u1d62 D\u1d62\u00b7AF\u1d62. For each multiplicative pair under independence: CV\u00b2(XY) \u2248 CV\u00b2(X) + CV\u00b2(Y). For S: \u03c3\u00b2(S) = \u03a3\u1d62 \u03c3\u00b2(D\u1d62\u00b7AF\u1d62) with the three taxa treated independent. AF_i errors are not in fact independent across taxa (likely correlated through shared monitoring programmes) \u2014 this is acknowledged in `caveats` and inflates the reported \u03c3 as an upper-bound estimate of total uncertainty.",
          "totalCV": 0.445,
          "totalSigma_kg": 329632,
          "totalSigma_tonnes": 329.6,
          "inputs": [
            {
              "variable": "A_sub",
              "value": 109500,
              "valueUnits": "m^2",
              "sigma": 16425,
              "CV": 0.15,
              "valueSource": "infrastructure_layout_60x15mw.json:data.aggregate.submerged_area_total_m2",
              "valueKind": "mixed",
              "sigmaSource": "assumed (15% engineering tolerance for floating-platform wetted area; no \u03c3 in input record)",
              "sigmaKind": "assumed"
            },
            {
              "variable": "D_pre,Mytilus edulis",
              "value": 0.42,
              "valueUnits": "kg m^-2",
              "sigma": 0.09,
              "CV": 0.214,
              "valueSource": "mareano_baseline_density.json:data.perTaxon[0].density_kg_m2",
              "valueKind": "illustrative",
              "sigmaSource": "imr_baseline_density_fallback.json:data.perTaxon[0].uncertainty_kg_m2 (proxy \u2014 MAREANO row carries no \u03c3)",
              "sigmaKind": "illustrative-proxy"
            },
            {
              "variable": "D_pre,Buccinum undatum",
              "value": 0.11,
              "valueUnits": "kg m^-2",
              "sigma": 0.03,
              "CV": 0.273,
              "valueSource": "mareano_baseline_density.json:data.perTaxon[1].density_kg_m2",
              "valueKind": "illustrative",
              "sigmaSource": "imr_baseline_density_fallback.json:data.perTaxon[1].uncertainty_kg_m2",
              "sigmaKind": "illustrative-proxy"
            },
            {
              "variable": "D_pre,Asterias rubens",
              "value": 0.28,
              "valueUnits": "kg m^-2",
              "sigma": 0.06,
              "CV": 0.214,
              "valueSource": "mareano_baseline_density.json:data.perTaxon[2].density_kg_m2",
              "valueKind": "illustrative",
              "sigmaSource": "imr_baseline_density_fallback.json:data.perTaxon[2].uncertainty_kg_m2",
              "sigmaKind": "illustrative-proxy"
            },
            {
              "variable": "AF_Mytilus edulis",
              "value": 12.0,
              "valueUnits": "dimensionless",
              "sigma": 6.0,
              "CV": 0.5,
              "valueSource": "reef_aggregation_index_bindings.json:data.perTaxon[0].AF_i",
              "valueKind": "illustrative",
              "sigmaSource": "assumed (CV=0.5 reflects wide literature variance; Degraer 2020 cites a single Mytilus value with no published spread)",
              "sigmaKind": "assumed"
            },
            {
              "variable": "AF_Buccinum undatum",
              "value": 3.5,
              "valueUnits": "dimensionless",
              "sigma": 1.75,
              "CV": 0.5,
              "valueSource": "reef_aggregation_index_bindings.json:data.perTaxon[1].AF_i",
              "valueKind": "illustrative",
              "sigmaSource": "assumed (CV=0.5; no published value for Buccinum in Degraer 2020)",
              "sigmaKind": "assumed"
            },
            {
              "variable": "AF_Asterias rubens",
              "value": 5.0,
              "valueUnits": "dimensionless",
              "sigma": 2.5,
              "CV": 0.5,
              "valueSource": "reef_aggregation_index_bindings.json:data.perTaxon[2].AF_i",
              "valueKind": "illustrative",
              "sigmaSource": "assumed (CV=0.5; no published value for Asterias in Degraer 2020)",
              "sigmaKind": "assumed"
            },
            {
              "variable": "C_t(24 mo)",
              "value": 0.9918,
              "valueUnits": "dimensionless",
              "sigma": 0.02,
              "CV": 0.02,
              "valueSource": "colonisation_time_factor.json:data.formula evaluated with parameters {L:1.0, k:0.30, t0_months:8}",
              "valueKind": "illustrative",
              "sigmaSource": "assumed (near sigmoid saturation; small \u03c3)",
              "sigmaKind": "assumed"
            }
          ],
          "perTaxonVariance": [
            {
              "scientificName": "Mytilus edulis",
              "D_times_AF": 5.04,
              "var_D_times_AF": 7.517,
              "shareWithinS": 0.9229
            },
            {
              "scientificName": "Buccinum undatum",
              "D_times_AF": 0.385,
              "var_D_times_AF": 0.048,
              "shareWithinS": 0.0059
            },
            {
              "scientificName": "Asterias rubens",
              "D_times_AF": 1.4,
              "var_D_times_AF": 0.58,
              "shareWithinS": 0.0712
            }
          ],
          "S_value_kg_m2": 6.825,
          "S_sigma_kg_m2": 2.854,
          "S_CV": 0.418,
          "varianceAttribution": [
            {
              "term": "A_sub",
              "CV_squared": 0.0225,
              "shareOfTotal": 0.1137
            },
            {
              "term": "C_t",
              "CV_squared": 0.0004,
              "shareOfTotal": 0.002
            },
            {
              "term": "S = \u03a3\u1d62 D\u1d62\u00b7AF\u1d62",
              "CV_squared": 0.1749,
              "shareOfTotal": 0.8842
            }
          ],
          "dominantUncertainty": "AF_Mytilus edulis accounts for \u224880 % of total CV\u00b2(B_reef). Tightening that single prior pays back ~4\u00d7 more than tightening any other input."
        },
        "caveats": [
          "Every headline number is downstream of illustrative inputs. This record demonstrates equation evaluation and CV propagation; it is NOT a measurement of Utsira.",
          "Three \u03c3 values are assumed (\u03c3(A_sub)=15%, \u03c3(AF_i)/AF_i=0.5 for all taxa, \u03c3(C_t)=0.02). Flagged in `data.uncertainty.inputs[*].sigmaKind`.",
          "The MAREANO row carries no \u03c3; IMR's \u03c3 is borrowed as a proxy. Real \u03c3 should come from the same retrieval that produced the density.",
          "Independence across taxa is optimistic. AF_i errors plausibly correlate through shared monitoring programmes; correlated errors would inflate \u03c3(S) above 2.854.",
          "B_reef is a standing-stock quantity. A time-integrated 'reef-effect-years' (\u222b\u2080\u00b2\u2074 B_reef(t) dt) is \u2248 9800 t\u00b7month at central values."
        ],
        "provenance": {
          "values": "computed",
          "derivedFrom": [
            "https://example.org/norwegian-ses/floating-wind-infrastructure/utsira-nord-60x15mw",
            "https://example.org/norwegian-ses/benthic-biomass-density-mareano/norwegian-shelf",
            "https://example.org/norwegian-ses/benthic-biomass-density-imr/ices-iva-fallback",
            "https://example.org/norwegian-ses/reef-aggregation-index/degraer2020-bindings",
            "https://example.org/norwegian-ses/colonisation-time-factor/default-sigmoid",
            "https://example.org/norwegian-ses/area-of-interest/utsira-surroundings"
          ],
          "equationRecord": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
          "computedOn": "2026-05-19",
          "computeCode": "../../experiment/scripts/utsira_reef_biomass.py",
          "computeCodeNote": "Standalone Python script. Loads the six per-class input records, evaluates the equation at t=24 mo, propagates uncertainty by log-linear CV, and emits this output. Run: `python3 _sources/experiment/scripts/utsira_reef_biomass.py --json` to regenerate this JSON.",
          "uncertaintyMethod": "log-linear CV propagation; B_reef = A_sub \u00b7 C_t \u00b7 \u03a3\u1d62 D\u1d62\u00b7AF\u1d62; taxa treated independent within S",
          "note": "Values are deterministic results of applying the cited equation to the input records listed in `derivedFrom`. Input values are themselves illustrative (see each input record's `data.provenance`), so this output's `values: computed` flag refers to the calculation chain, not to a real-world measurement."
        }
      }
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.experiment-output",
      "type": "application/schema+json",
      "title": "Experiment-output bblock"
    },
    {
      "rel": "derivedFrom",
      "href": "https://example.org/norwegian-ses/experiment/utsira-reef-biomass-surroundings-v1",
      "type": "application/json",
      "title": "Experiment record this output belongs to"
    },
    {
      "rel": "cite-as",
      "href": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
      "type": "application/ld+json",
      "title": "Equation evaluated to produce this result"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix dwc: <http://rs.tdwg.org/dwc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix indo: <https://id3.seadots.eu/indicator/> .
@prefix ns1: <https://w3id.org/ogc/hosted/seadots/experiment#> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/experiment-output#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix w3ctime: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/norwegian-ses/experiment-output/reef-biomass-result> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Experiment record this output belongs to" ;
            dcterms:format "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/derivedFrom> ;
            oa:hasTarget <https://example.org/norwegian-ses/experiment/utsira-reef-biomass-surroundings-v1> ],
        [ rdfs:label "Experiment-output bblock" ;
            dcterms:format "application/schema+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.experiment-output> ],
        [ rdfs:label "Equation evaluated to produce this result" ;
            dcterms:format "application/ld+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation> ] ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 4.2e+00 5.91e+01 ) ( 5.3e+00 5.91e+01 ) ( 5.3e+00 5.97e+01 ) ( 4.2e+00 5.97e+01 ) ( 4.2e+00 5.91e+01 ) ) ) ] ;
    geojson:properties [ a seadots:Dataset ;
            dcterms:created "2026-05-19" ;
            dcterms:description "Primary scientific output of the Utsira surroundings reef-biomass experiment. Headline value: 741 ± 330 t standing reef-associated biomass at scenario end (24 months). This file is an OGC API Records Feature (JSON) carrying the full structured result inline: (a) the headline scalar with 1σ and 95 % CI, (b) the per-taxon decomposition at t=24 mo, (c) the time series at the sigmoid-lookup points, (d) full variance attribution by input, and (e) per-variable provenance. All input values are illustrative; this record demonstrates equation evaluation and uncertainty propagation, not a measurement of Utsira." ;
            dcterms:license "https://creativecommons.org/licenses/by/4.0/" ;
            dcterms:modified "2026-05-19" ;
            dcterms:title "Reef-associated biomass result — Utsira surroundings, scenario T0+24 mo (with uncertainty)" ;
            dcat:keyword "CV propagation",
                "Utsira",
                "floating wind",
                "reef biomass",
                "uncertainty" ;
            seadots:output [ dcterms:conformsTo sosa:Observation,
                        <https://id3.seadots.eu/conventions/edito-output>,
                        <https://ogcincubator.github.io/geodcat-ogcapi-records/>,
                        <https://w3id.org/ogc/hosted/iliad/oim-obs> ;
                    dcterms:description "B_reef headline scalar, per-taxon decomposition, time series, and variance attribution. Sum-over-taxa of A_sub · D_pre,i · AF_i · C_t evaluated at scenario end. All values emitted inline as JSON." ;
                    dcterms:format "application/json" ;
                    dcterms:title "Reef-associated biomass (structured result)" ;
                    qudt:unit "kg" ;
                    skos:exactMatch indo:floating-wind-reef-biomass ;
                    sosa:hasFeatureOfInterest <https://example.org/norwegian-ses/area-of-interest/utsira-surroundings> ;
                    sosa:hasSimpleResult 741237 ;
                    sosa:observedProperty indo:floating-wind-reef-biomass ;
                    sosa:phenomenonTime [ w3ctime:hasBeginning "2026-05-13T00:00:00+00:00"^^xsd:dateTime ;
                            w3ctime:hasEnd "2028-05-13T00:00:00+00:00"^^xsd:dateTime ] ;
                    sosa:resultTime "2028-05-13T00:00:00+00:00"^^xsd:dateTime ;
                    ns1:experiment <https://example.org/norwegian-ses/experiment/utsira-reef-biomass-surroundings-v1> ;
                    seadots:aggregation "sum-over-i" ;
                    seadots:data [ dcterms:temporal "2026-05-13",
                                "2028-05-13" ;
                            qudt:unit "kg" ;
                            skos:note "B_reef is a standing-stock quantity. A time-integrated 'reef-effect-years' (∫₀²⁴ B_reef(t) dt) is ≈ 9800 t·month at central values.",
                                "B_reef_kg above uses the rounded C_t values from `colonisation_time_factor.json → data.lookup`. The `headline` and `perTaxonAtT24` use the analytic C(24)=0.9918 from the sigmoid; the two agree at three significant figures.",
                                "Every headline number is downstream of illustrative inputs. This record demonstrates equation evaluation and CV propagation; it is NOT a measurement of Utsira.",
                                "Independence across taxa is optimistic. AF_i errors plausibly correlate through shared monitoring programmes; correlated errors would inflate σ(S) above 2.854.",
                                "The MAREANO row carries no σ; IMR's σ is borrowed as a proxy. Real σ should come from the same retrieval that produced the density.",
                                "Three σ values are assumed (σ(A_sub)=15%, σ(AF_i)/AF_i=0.5 for all taxa, σ(C_t)=0.02). Flagged in `data.uncertainty.inputs[*].sigmaKind`." ;
                            prov:wasDerivedFrom [ dcterms:date "2026-05-19" ;
                                    skos:note "Standalone Python script. Loads the six per-class input records, evaluates the equation at t=24 mo, propagates uncertainty by log-linear CV, and emits this output. Run: `python3 _sources/experiment/scripts/utsira_reef_biomass.py --json` to regenerate this JSON.",
                                        "Values are deterministic results of applying the cited equation to the input records listed in `derivedFrom`. Input values are themselves illustrative (see each input record's `data.provenance`), so this output's `values: computed` flag refers to the calculation chain, not to a real-world measurement." ;
                                    prov:hadPlan <https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation> ;
                                    prov:wasDerivedFrom <https://example.org/norwegian-ses/area-of-interest/utsira-surroundings>,
                                        <https://example.org/norwegian-ses/benthic-biomass-density-imr/ices-iva-fallback>,
                                        <https://example.org/norwegian-ses/benthic-biomass-density-mareano/norwegian-shelf>,
                                        <https://example.org/norwegian-ses/colonisation-time-factor/default-sigmoid>,
                                        <https://example.org/norwegian-ses/floating-wind-infrastructure/utsira-nord-60x15mw>,
                                        <https://example.org/norwegian-ses/reef-aggregation-index/degraer2020-bindings> ;
                                    seadots:computeCode <file:///experiment/scripts/utsira_reef_biomass.py> ;
                                    seadots:provenanceValues "computed" ;
                                    seadots:uncertaintyMethod "log-linear CV propagation; B_reef = A_sub · C_t · Σᵢ Dᵢ·AFᵢ; taxa treated independent within S" ] ;
                            seadots:asOf_months 24 ;
                            seadots:equation "B_reef(t) = Σ_i (A_sub · D_pre,i · AF_i · C_t)" ;
                            seadots:headline [ qudt:coefficientOfVariation 4.45e-01 ;
                                    qudt:standardUncertainty 3.296e+02,
                                        329632 ;
                                    indo:floating-wind-reef-biomass "741.2"^^qudt:QuantityValue,
                                        "741237"^^qudt:QuantityValue ;
                                    seadots:ci95_kg 95198,
                                        1387276 ;
                                    seadots:ci95_tonnes 95,
                                        1387 ] ;
                            seadots:perTaxonAtT24 [ dwc:scientificName "Asterias rubens" ;
                                    dwc:taxonID 123776 ;
                                    indo:benthic-biomass-density "0.28"^^qudt:QuantityValue ;
                                    indo:colonisation-time-factor "0.9918"^^qudt:DimensionlessQuantity ;
                                    indo:floating-wind-reef-biomass "152049"^^qudt:QuantityValue ;
                                    indo:reef-aggregation-index "5.0"^^qudt:DimensionlessQuantity ;
                                    indo:submerged-infrastructure-area "109500"^^qudt:QuantityValue ;
                                    seadots:shareOfTotal 2.051e-01 ],
                                [ dwc:scientificName "Mytilus edulis" ;
                                    dwc:taxonID 140480 ;
                                    indo:benthic-biomass-density "0.42"^^qudt:QuantityValue ;
                                    indo:colonisation-time-factor "0.9918"^^qudt:DimensionlessQuantity ;
                                    indo:floating-wind-reef-biomass "547375"^^qudt:QuantityValue ;
                                    indo:reef-aggregation-index "12.0"^^qudt:DimensionlessQuantity ;
                                    indo:submerged-infrastructure-area "109500"^^qudt:QuantityValue ;
                                    seadots:shareOfTotal 7.385e-01 ],
                                [ dwc:scientificName "Buccinum undatum" ;
                                    dwc:taxonID 138878 ;
                                    indo:benthic-biomass-density "0.11"^^qudt:QuantityValue ;
                                    indo:colonisation-time-factor "0.9918"^^qudt:DimensionlessQuantity ;
                                    indo:floating-wind-reef-biomass "41813"^^qudt:QuantityValue ;
                                    indo:reef-aggregation-index "3.5"^^qudt:DimensionlessQuantity ;
                                    indo:submerged-infrastructure-area "109500"^^qudt:QuantityValue ;
                                    seadots:shareOfTotal 5.64e-02 ] ;
                            seadots:timeSeries ( [ indo:colonisation-time-factor "0.08"^^qudt:DimensionlessQuantity ;
                                        indo:floating-wind-reef-biomass "59.8"^^qudt:QuantityValue,
                                            "59787"^^qudt:QuantityValue ;
                                        seadots:t_months 0 ] [ indo:colonisation-time-factor "0.32"^^qudt:DimensionlessQuantity ;
                                        indo:floating-wind-reef-biomass "239.1"^^qudt:QuantityValue,
                                            "239148"^^qudt:QuantityValue ;
                                        seadots:t_months 6 ] [ indo:colonisation-time-factor "0.71"^^qudt:DimensionlessQuantity ;
                                        indo:floating-wind-reef-biomass "530.6"^^qudt:QuantityValue,
                                            "530610"^^qudt:QuantityValue ;
                                        seadots:t_months 12 ] [ indo:colonisation-time-factor "0.93"^^qudt:DimensionlessQuantity ;
                                        indo:floating-wind-reef-biomass "695.0"^^qudt:QuantityValue,
                                            "695024"^^qudt:QuantityValue ;
                                        seadots:t_months 18 ] [ indo:colonisation-time-factor "0.99"^^qudt:DimensionlessQuantity ;
                                        indo:floating-wind-reef-biomass "739.9"^^qudt:QuantityValue,
                                            "739864"^^qudt:QuantityValue ;
                                        seadots:t_months 24 ] ) ;
                            seadots:uncertainty [ dcterms:methodology "log-linear CV propagation" ;
                                    qudt:coefficientOfVariation 4.45e-01 ;
                                    qudt:standardUncertainty 3.296e+02,
                                        329632 ;
                                    skos:definition "B_reef = A_sub · C_t · S, with S = Σᵢ Dᵢ·AFᵢ. For each multiplicative pair under independence: CV²(XY) ≈ CV²(X) + CV²(Y). For S: σ²(S) = Σᵢ σ²(Dᵢ·AFᵢ) with the three taxa treated independent. AF_i errors are not in fact independent across taxa (likely correlated through shared monitoring programmes) — this is acknowledged in `caveats` and inflates the reported σ as an upper-bound estimate of total uncertainty." ;
                                    seadots:S_CV 4.18e-01 ;
                                    seadots:S_sigma_kg_m2 2.854e+00 ;
                                    seadots:S_value_kg_m2 6.825e+00 ;
                                    seadots:dominantUncertainty "AF_Mytilus edulis accounts for ≈80 % of total CV²(B_reef). Tightening that single prior pays back ~4× more than tightening any other input." ;
                                    seadots:perTaxonVariance [ dwc:scientificName "Buccinum undatum" ;
                                            seadots:D_times_AF 3.85e-01 ;
                                            seadots:shareWithinS 5.9e-03 ;
                                            seadots:var_D_times_AF 4.8e-02 ],
                                        [ dwc:scientificName "Asterias rubens" ;
                                            seadots:D_times_AF 1.4e+00 ;
                                            seadots:shareWithinS 7.12e-02 ;
                                            seadots:var_D_times_AF 5.8e-01 ],
                                        [ dwc:scientificName "Mytilus edulis" ;
                                            seadots:D_times_AF 5.04e+00 ;
                                            seadots:shareWithinS 9.229e-01 ;
                                            seadots:var_D_times_AF 7.517e+00 ] ;
                                    seadots:uncertaintyInput [ dcterms:source "imr_baseline_density_fallback.json:data.perTaxon[0].uncertainty_kg_m2 (proxy — MAREANO row carries no σ)",
                                                "mareano_baseline_density.json:data.perTaxon[0].density_kg_m2" ;
                                            qudt:coefficientOfVariation 2.14e-01 ;
                                            qudt:standardUncertainty 9e-02 ;
                                            qudt:unit "kg m^-2" ;
                                            qudt:value 4.2e-01 ;
                                            seadots:sigmaKind "illustrative-proxy" ;
                                            seadots:valueKind "illustrative" ;
                                            seadots:variable "D_pre,Mytilus edulis" ],
                                        [ dcterms:source "imr_baseline_density_fallback.json:data.perTaxon[2].uncertainty_kg_m2",
                                                "mareano_baseline_density.json:data.perTaxon[2].density_kg_m2" ;
                                            qudt:coefficientOfVariation 2.14e-01 ;
                                            qudt:standardUncertainty 6e-02 ;
                                            qudt:unit "kg m^-2" ;
                                            qudt:value 2.8e-01 ;
                                            seadots:sigmaKind "illustrative-proxy" ;
                                            seadots:valueKind "illustrative" ;
                                            seadots:variable "D_pre,Asterias rubens" ],
                                        [ dcterms:source "assumed (15% engineering tolerance for floating-platform wetted area; no σ in input record)",
                                                "infrastructure_layout_60x15mw.json:data.aggregate.submerged_area_total_m2" ;
                                            qudt:coefficientOfVariation 1.5e-01 ;
                                            qudt:standardUncertainty 16425 ;
                                            qudt:unit "m^2" ;
                                            qudt:value 109500 ;
                                            seadots:sigmaKind "assumed" ;
                                            seadots:valueKind "mixed" ;
                                            seadots:variable "A_sub" ],
                                        [ dcterms:source "assumed (CV=0.5 reflects wide literature variance; Degraer 2020 cites a single Mytilus value with no published spread)",
                                                "reef_aggregation_index_bindings.json:data.perTaxon[0].AF_i" ;
                                            qudt:coefficientOfVariation 5e-01 ;
                                            qudt:standardUncertainty 6e+00 ;
                                            qudt:unit "dimensionless" ;
                                            qudt:value 1.2e+01 ;
                                            seadots:sigmaKind "assumed" ;
                                            seadots:valueKind "illustrative" ;
                                            seadots:variable "AF_Mytilus edulis" ],
                                        [ dcterms:source "assumed (CV=0.5; no published value for Asterias in Degraer 2020)",
                                                "reef_aggregation_index_bindings.json:data.perTaxon[2].AF_i" ;
                                            qudt:coefficientOfVariation 5e-01 ;
                                            qudt:standardUncertainty 2.5e+00 ;
                                            qudt:unit "dimensionless" ;
                                            qudt:value 5e+00 ;
                                            seadots:sigmaKind "assumed" ;
                                            seadots:valueKind "illustrative" ;
                                            seadots:variable "AF_Asterias rubens" ],
                                        [ dcterms:source "assumed (near sigmoid saturation; small σ)",
                                                "colonisation_time_factor.json:data.formula evaluated with parameters {L:1.0, k:0.30, t0_months:8}" ;
                                            qudt:coefficientOfVariation 2e-02 ;
                                            qudt:standardUncertainty 2e-02 ;
                                            qudt:unit "dimensionless" ;
                                            qudt:value 9.918e-01 ;
                                            seadots:sigmaKind "assumed" ;
                                            seadots:valueKind "illustrative" ;
                                            seadots:variable "C_t(24 mo)" ],
                                        [ dcterms:source "imr_baseline_density_fallback.json:data.perTaxon[1].uncertainty_kg_m2",
                                                "mareano_baseline_density.json:data.perTaxon[1].density_kg_m2" ;
                                            qudt:coefficientOfVariation 2.73e-01 ;
                                            qudt:standardUncertainty 3e-02 ;
                                            qudt:unit "kg m^-2" ;
                                            qudt:value 1.1e-01 ;
                                            seadots:sigmaKind "illustrative-proxy" ;
                                            seadots:valueKind "illustrative" ;
                                            seadots:variable "D_pre,Buccinum undatum" ],
                                        [ dcterms:source "assumed (CV=0.5; no published value for Buccinum in Degraer 2020)",
                                                "reef_aggregation_index_bindings.json:data.perTaxon[1].AF_i" ;
                                            qudt:coefficientOfVariation 5e-01 ;
                                            qudt:standardUncertainty 1.75e+00 ;
                                            qudt:unit "dimensionless" ;
                                            qudt:value 3.5e+00 ;
                                            seadots:sigmaKind "assumed" ;
                                            seadots:valueKind "illustrative" ;
                                            seadots:variable "AF_Buccinum undatum" ] ;
                                    seadots:varianceAttribution [ skos:notation "C_t" ;
                                            seadots:CV_squared 4e-04 ;
                                            seadots:shareOfTotal 2e-03 ],
                                        [ skos:notation "S = Σᵢ Dᵢ·AFᵢ" ;
                                            seadots:CV_squared 1.749e-01 ;
                                            seadots:shareOfTotal 8.842e-01 ],
                                        [ skos:notation "A_sub" ;
                                            seadots:CV_squared 2.25e-02 ;
                                            seadots:shareOfTotal 1.137e-01 ] ] ] ;
                    seadots:role "primary result" ] ;
            rec:format [ dcterms:format "application/json" ] ;
            rec:language [ rec:languageCode "en" ] ;
            rec:themes [ rec:concept [ skos:prefLabel "Floating-wind reef effect" ;
                            rec:conceptID "reef-effect"^^xsd:string ] ;
                    rec:scheme "https://id3.seadots.eu/themes" ] ] .


```


### STAC catalog — Utsira surroundings reef-biomass run
#### json
```json
{
  "id": "https://example.org/norwegian-ses/experiment-output/stac-catalog",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "type": "Catalog",
    "title": "STAC catalog — Utsira surroundings reef-biomass run",
    "description": "STAC catalog indexing the inputs, the run, and the JSON result output. Follows the SeaDOTs EDITO output conventions.",
    "created": "2026-05-18",
    "updated": "2026-05-18",
    "language": { "code": "en" },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "themes": [
      { "concepts": [{ "id": "catalog", "label": "STAC catalog" }], "scheme": "https://id3.seadots.eu/themes" }
    ],
    "keywords": ["STAC", "catalog", "reef biomass", "EDITO"],
    "formats": [{ "mediaType": "application/json" }],
    "experimentOutput": {
      "name": "STAC catalog for the run",
      "description": "STAC catalog indexing input rasters, the run, and the JSON result output.",
      "role": "catalog",
      "format": "application/json",
      "vocabularyTerm": "https://stacspec.org/v1.0.0/catalog-spec/json-schema/catalog.json",
      "experiment": "https://example.org/norwegian-ses/experiment/utsira-reef-biomass-surroundings-v1",
      "conformsTo": [
        "https://stacspec.org/v1.0.0",
        "https://id3.seadots.eu/conventions/edito-output"
      ]
    }
  },
  "links": [
    { "rel": "describedby", "href": "bblocks://ogc.hosted.seadots.experiment-output", "type": "application/schema+json", "title": "Experiment-output bblock" }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/experiment-output/context.jsonld",
  "id": "https://example.org/norwegian-ses/experiment-output/stac-catalog",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "type": "Catalog",
    "title": "STAC catalog \u2014 Utsira surroundings reef-biomass run",
    "description": "STAC catalog indexing the inputs, the run, and the JSON result output. Follows the SeaDOTs EDITO output conventions.",
    "created": "2026-05-18",
    "updated": "2026-05-18",
    "language": {
      "code": "en"
    },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "themes": [
      {
        "concepts": [
          {
            "id": "catalog",
            "label": "STAC catalog"
          }
        ],
        "scheme": "https://id3.seadots.eu/themes"
      }
    ],
    "keywords": [
      "STAC",
      "catalog",
      "reef biomass",
      "EDITO"
    ],
    "formats": [
      {
        "mediaType": "application/json"
      }
    ],
    "experimentOutput": {
      "name": "STAC catalog for the run",
      "description": "STAC catalog indexing input rasters, the run, and the JSON result output.",
      "role": "catalog",
      "format": "application/json",
      "vocabularyTerm": "https://stacspec.org/v1.0.0/catalog-spec/json-schema/catalog.json",
      "experiment": "https://example.org/norwegian-ses/experiment/utsira-reef-biomass-surroundings-v1",
      "conformsTo": [
        "https://stacspec.org/v1.0.0",
        "https://id3.seadots.eu/conventions/edito-output"
      ]
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.experiment-output",
      "type": "application/schema+json",
      "title": "Experiment-output bblock"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <https://w3id.org/ogc/hosted/seadots/experiment#> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/experiment-output#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/norwegian-ses/experiment-output/stac-catalog> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Experiment-output bblock" ;
            dcterms:format "application/schema+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.experiment-output> ] ;
    geojson:properties [ a seadots:Catalog ;
            dcterms:created "2026-05-18" ;
            dcterms:description "STAC catalog indexing the inputs, the run, and the JSON result output. Follows the SeaDOTs EDITO output conventions." ;
            dcterms:license "https://creativecommons.org/licenses/by/4.0/" ;
            dcterms:modified "2026-05-18" ;
            dcterms:title "STAC catalog — Utsira surroundings reef-biomass run" ;
            dcat:keyword "EDITO",
                "STAC",
                "catalog",
                "reef biomass" ;
            seadots:output [ dcterms:conformsTo <https://id3.seadots.eu/conventions/edito-output>,
                        <https://stacspec.org/v1.0.0> ;
                    dcterms:description "STAC catalog indexing input rasters, the run, and the JSON result output." ;
                    dcterms:format "application/json" ;
                    dcterms:title "STAC catalog for the run" ;
                    skos:exactMatch <https://stacspec.org/v1.0.0/catalog-spec/json-schema/catalog.json> ;
                    ns1:experiment <https://example.org/norwegian-ses/experiment/utsira-reef-biomass-surroundings-v1> ;
                    seadots:role "catalog" ] ;
            rec:format [ dcterms:format "application/json" ] ;
            rec:language [ rec:languageCode "en" ] ;
            rec:themes [ rec:concept [ skos:prefLabel "STAC catalog" ;
                            rec:conceptID "catalog"^^xsd:string ] ;
                    rec:scheme "https://id3.seadots.eu/themes" ] ] .


```


### PROV-O provenance record (JSON-LD)
#### json
```json
{
  "id": "https://example.org/norwegian-ses/experiment-output/prov-record",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "type": "Dataset",
    "title": "PROV-O provenance record (JSON-LD)",
    "description": "Provenance record linking the run to the ODD demonstrator, the canonical reef-biomass equation record, and the per-taxon bindings resolved at run time.",
    "created": "2026-05-18",
    "updated": "2026-05-18",
    "language": { "code": "en" },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "themes": [
      { "concepts": [{ "id": "provenance", "label": "PROV-O provenance" }], "scheme": "https://id3.seadots.eu/themes" }
    ],
    "keywords": ["PROV-O", "provenance", "JSON-LD"],
    "formats": [{ "mediaType": "application/ld+json" }],
    "experimentOutput": {
      "name": "PROV-O provenance (JSON-LD)",
      "description": "PROV record linking the run to the ODD record, the equation record, the Python script that produced the result, and the resolved bindings per taxon.",
      "role": "provenance",
      "format": "application/ld+json",
      "vocabularyTerm": "http://www.w3.org/ns/prov#Entity",
      "experiment": "https://example.org/norwegian-ses/experiment/utsira-reef-biomass-surroundings-v1",
      "conformsTo": [
        "http://www.w3.org/TR/prov-o/"
      ]
    }
  },
  "links": [
    { "rel": "describedby", "href": "bblocks://ogc.hosted.seadots.experiment-output", "type": "application/schema+json", "title": "Experiment-output bblock" }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/experiment-output/context.jsonld",
  "id": "https://example.org/norwegian-ses/experiment-output/prov-record",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "type": "Dataset",
    "title": "PROV-O provenance record (JSON-LD)",
    "description": "Provenance record linking the run to the ODD demonstrator, the canonical reef-biomass equation record, and the per-taxon bindings resolved at run time.",
    "created": "2026-05-18",
    "updated": "2026-05-18",
    "language": {
      "code": "en"
    },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "themes": [
      {
        "concepts": [
          {
            "id": "provenance",
            "label": "PROV-O provenance"
          }
        ],
        "scheme": "https://id3.seadots.eu/themes"
      }
    ],
    "keywords": [
      "PROV-O",
      "provenance",
      "JSON-LD"
    ],
    "formats": [
      {
        "mediaType": "application/ld+json"
      }
    ],
    "experimentOutput": {
      "name": "PROV-O provenance (JSON-LD)",
      "description": "PROV record linking the run to the ODD record, the equation record, the Python script that produced the result, and the resolved bindings per taxon.",
      "role": "provenance",
      "format": "application/ld+json",
      "vocabularyTerm": "http://www.w3.org/ns/prov#Entity",
      "experiment": "https://example.org/norwegian-ses/experiment/utsira-reef-biomass-surroundings-v1",
      "conformsTo": [
        "http://www.w3.org/TR/prov-o/"
      ]
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.experiment-output",
      "type": "application/schema+json",
      "title": "Experiment-output bblock"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <https://w3id.org/ogc/hosted/seadots/experiment#> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/experiment-output#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/norwegian-ses/experiment-output/prov-record> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Experiment-output bblock" ;
            dcterms:format "application/schema+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.experiment-output> ] ;
    geojson:properties [ a seadots:Dataset ;
            dcterms:created "2026-05-18" ;
            dcterms:description "Provenance record linking the run to the ODD demonstrator, the canonical reef-biomass equation record, and the per-taxon bindings resolved at run time." ;
            dcterms:license "https://creativecommons.org/licenses/by/4.0/" ;
            dcterms:modified "2026-05-18" ;
            dcterms:title "PROV-O provenance record (JSON-LD)" ;
            dcat:keyword "JSON-LD",
                "PROV-O",
                "provenance" ;
            seadots:output [ dcterms:conformsTo <http://www.w3.org/TR/prov-o/> ;
                    dcterms:description "PROV record linking the run to the ODD record, the equation record, the Python script that produced the result, and the resolved bindings per taxon." ;
                    dcterms:format "application/ld+json" ;
                    dcterms:title "PROV-O provenance (JSON-LD)" ;
                    skos:exactMatch prov:Entity ;
                    ns1:experiment <https://example.org/norwegian-ses/experiment/utsira-reef-biomass-surroundings-v1> ;
                    seadots:role "provenance" ] ;
            rec:format [ dcterms:format "application/ld+json" ] ;
            rec:language [ rec:languageCode "en" ] ;
            rec:themes [ rec:concept [ skos:prefLabel "PROV-O provenance" ;
                            rec:conceptID "provenance"^^xsd:string ] ;
                    rec:scheme "https://id3.seadots.eu/themes" ] ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Computational Experiment Output
description: 'OGC API Records profile for a single output artefact produced by a computational
  experiment. Extends GeoDCAT-Records with an `experimentOutput` sub-object that ties
  the artefact to an output role, a format, a vocabulary term for the produced quantity,
  the experiment it belongs to, and optional conformance classes.

  '
allOf:
- $ref: https://ogcincubator.github.io/geodcat-ogcapi-records/build/annotated/geo/geodcat/geodcat-records/schema.yaml
properties:
  properties:
    type: object
    required:
    - experimentOutput
    properties:
      experimentOutput:
        type: object
        required:
        - name
        - role
        - format
        properties:
          name:
            type: string
            x-jsonld-id: http://purl.org/dc/terms/title
          description:
            type: string
            x-jsonld-id: http://purl.org/dc/terms/description
          role:
            type: string
            description: '`primary result`, `catalog`, `provenance`, `diagnostic`.

              '
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment-output#role
          format:
            type: string
            description: Media type or format profile URI.
            x-jsonld-id: http://purl.org/dc/terms/format
          vocabularyTerm:
            type: string
            format: uri
            description: Concept URI for the produced quantity.
            x-jsonld-id: http://www.w3.org/2004/02/skos/core#exactMatch
            x-jsonld-type: '@id'
          experiment:
            type: string
            format: uri
            description: URI of the experiment record that produced this output.
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment#experiment
            x-jsonld-type: '@id'
          observedProperty:
            type: string
            format: uri
            description: 'SOSA-aligned. URI of the property observed by this output.
              For the reef-biomass result this is the `floating-wind-reef-biomass`
              indicator URI. Carrying this field aligns the record with the OIM-OBS
              / SOSA observation profile.

              '
            x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
            x-jsonld-type: '@id'
          hasSimpleResult:
            description: 'SOSA-aligned. The simple (scalar or short structured) result
              of the observation/calculation. Type follows the observed property;
              for B_reef this is the headline scalar in kg with units carried by `hasSimpleResultUnit`.

              '
            x-jsonld-id: http://www.w3.org/ns/sosa/hasSimpleResult
          hasSimpleResultUnit:
            type: string
            description: Units of `hasSimpleResult` (e.g. `kg`, `t`, `kg m-2`).
            x-jsonld-id: http://qudt.org/schema/qudt/unit
          resultTime:
            type: string
            format: date-time
            description: 'SOSA-aligned. Time at which the result was produced or applies.
              For a standing-stock calculation, the end-of-scenario instant.

              '
            x-jsonld-id: http://www.w3.org/ns/sosa/resultTime
            x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
          phenomenonTime:
            description: 'SOSA-aligned. Time interval over which the observed phenomenon
              occurred (e.g. the scenario interval). String, or object with `start`
              and `end` keys.

              '
            x-jsonld-id: http://www.w3.org/ns/sosa/phenomenonTime
          hasFeatureOfInterest:
            type: string
            format: uri
            description: 'SOSA-aligned. URI of the feature of interest (typically
              the AOI `area-of-interest` record, typically).

              '
            x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
            x-jsonld-type: '@id'
          conformsTo:
            type: array
            description: Conformance classes the output is expected to satisfy.
            items:
              type: string
              format: uri
            x-jsonld-id: http://purl.org/dc/terms/conformsTo
            x-jsonld-type: '@id'
            x-jsonld-container: '@set'
          aggregation:
            type: string
            description: 'How the output aggregates over the equation index, when
              applicable (e.g. `sum-over-i`, `per-taxon`, `scalar`).

              '
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment-output#aggregation
          data:
            type: object
            required:
            - provenance
            description: 'Representative inline result of this output. For a primary
              result, typically a `headline` scalar/CI plus `perTaxon`, `timeSeries`,
              and `uncertainty` sub-objects. For a catalog or provenance record, may
              be a small structural sample. Shape is format-specific and not further
              constrained.

              '
            properties:
              provenance:
                type: object
                required:
                - values
                description: 'Source pointer for every concrete value in this `data`
                  block. Required on every example.

                  '
                properties:
                  values:
                    type: string
                    enum:
                    - computed
                    - retrieved
                    - illustrative
                    - mixed
                    description: "`computed` \u2014 values are the deterministic result
                      of applying the documented equation to the cited input records
                      (must list `derivedFrom`). `retrieved` \u2014 values came from
                      the cited API call. `illustrative` \u2014 placeholders for schema
                      shape. `mixed` \u2014 some are computed/retrieved and the rest
                      are illustrative, annotated in-line.\n"
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment-output#provenanceValues
                  derivedFrom:
                    type: array
                    description: 'URIs of the input records that drive these values.
                      Required when `values=computed`.

                      '
                    items:
                      type: string
                      format: uri
                    x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
                    x-jsonld-type: '@id'
                    x-jsonld-container: '@set'
                  equationRecord:
                    type: string
                    format: uri
                    description: 'URI of the equation-property-relationship record
                      that defines the closed-form expression evaluated here.

                      '
                    x-jsonld-id: http://www.w3.org/ns/prov#hadPlan
                    x-jsonld-type: '@id'
                  computedOn:
                    type: string
                    format: date
                    description: ISO date the values were last computed.
                    x-jsonld-id: http://purl.org/dc/terms/date
                  computeCode:
                    type: string
                    format: uri
                    description: 'URI of the script / notebook that produced these
                      values.

                      '
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment-output#computeCode
                    x-jsonld-type: '@id'
                  uncertaintyMethod:
                    type: string
                    description: 'Name of the uncertainty-propagation method applied
                      (e.g. `log-linear CV`, `Monte Carlo`, `analytic first-order`).

                      '
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment-output#uncertaintyMethod
                  note:
                    type: string
                    x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
                x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment-output#data
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment-output#output
    x-jsonld-id: https://purl.org/geojson/vocab#properties
x-jsonld-extra-terms:
  id: '@id'
  type: '@type'
  geometry: https://purl.org/geojson/vocab#geometry
  coordinates: https://purl.org/geojson/vocab#coordinates
  Feature: https://purl.org/geojson/vocab#Feature
  Polygon: https://purl.org/geojson/vocab#Polygon
  links:
    x-jsonld-id: http://www.w3.org/ns/iana/link-relations/relation
    x-jsonld-container: '@set'
  href: '@id'
  rel: https://purl.org/geojson/vocab#rel
  title: http://purl.org/dc/terms/title
  created: http://purl.org/dc/terms/created
  updated: http://purl.org/dc/terms/modified
  language: http://purl.org/dc/terms/language
  license: http://purl.org/dc/terms/license
  keywords:
    x-jsonld-id: http://www.w3.org/ns/dcat#keyword
    x-jsonld-container: '@set'
  themes:
    x-jsonld-id: http://www.w3.org/ns/dcat#theme
    x-jsonld-container: '@set'
  concepts:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#Concept
    x-jsonld-container: '@set'
  scheme: http://www.w3.org/2004/02/skos/core#inScheme
  label: http://www.w3.org/2004/02/skos/core#prefLabel
  formats:
    x-jsonld-id: http://purl.org/dc/terms/format
    x-jsonld-container: '@set'
  mediaType: http://purl.org/dc/terms/format
  start:
    x-jsonld-id: http://www.w3.org/2006/time#hasBeginning
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  end:
    x-jsonld-id: http://www.w3.org/2006/time#hasEnd
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  equation: https://w3id.org/ogc/hosted/seadots/experiment-output#equation
  asOf_months: https://w3id.org/ogc/hosted/seadots/experiment-output#asOf_months
  scenarioInterval: http://purl.org/dc/terms/temporal
  units: http://qudt.org/schema/qudt/unit
  headline: https://w3id.org/ogc/hosted/seadots/experiment-output#headline
  B_reef_kg:
    x-jsonld-id: https://id3.seadots.eu/indicator/floating-wind-reef-biomass
    x-jsonld-type: http://qudt.org/schema/qudt/QuantityValue
  B_reef_tonnes:
    x-jsonld-id: https://id3.seadots.eu/indicator/floating-wind-reef-biomass
    x-jsonld-type: http://qudt.org/schema/qudt/QuantityValue
  sigma_kg: http://qudt.org/schema/qudt/standardUncertainty
  sigma_tonnes: http://qudt.org/schema/qudt/standardUncertainty
  totalSigma_kg: http://qudt.org/schema/qudt/standardUncertainty
  totalSigma_tonnes: http://qudt.org/schema/qudt/standardUncertainty
  CV: http://qudt.org/schema/qudt/coefficientOfVariation
  totalCV: http://qudt.org/schema/qudt/coefficientOfVariation
  ci95_kg: https://w3id.org/ogc/hosted/seadots/experiment-output#ci95_kg
  ci95_tonnes: https://w3id.org/ogc/hosted/seadots/experiment-output#ci95_tonnes
  perTaxonAtT24:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment-output#perTaxonAtT24
    x-jsonld-container: '@set'
  scientificName: http://rs.tdwg.org/dwc/terms/scientificName
  aphiaID: http://rs.tdwg.org/dwc/terms/taxonID
  A_sub_m2:
    x-jsonld-id: https://id3.seadots.eu/indicator/submerged-infrastructure-area
    x-jsonld-type: http://qudt.org/schema/qudt/QuantityValue
  D_pre_kg_m2:
    x-jsonld-id: https://id3.seadots.eu/indicator/benthic-biomass-density
    x-jsonld-type: http://qudt.org/schema/qudt/QuantityValue
  AF_i:
    x-jsonld-id: https://id3.seadots.eu/indicator/reef-aggregation-index
    x-jsonld-type: http://qudt.org/schema/qudt/DimensionlessQuantity
  C_t:
    x-jsonld-id: https://id3.seadots.eu/indicator/colonisation-time-factor
    x-jsonld-type: http://qudt.org/schema/qudt/DimensionlessQuantity
  B_kg:
    x-jsonld-id: https://id3.seadots.eu/indicator/floating-wind-reef-biomass
    x-jsonld-type: http://qudt.org/schema/qudt/QuantityValue
  shareOfTotal: https://w3id.org/ogc/hosted/seadots/experiment-output#shareOfTotal
  timeSeries:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment-output#timeSeries
    x-jsonld-container: '@list'
  t_months: https://w3id.org/ogc/hosted/seadots/experiment-output#t_months
  timeSeriesNote: http://www.w3.org/2004/02/skos/core#note
  uncertainty: https://w3id.org/ogc/hosted/seadots/experiment-output#uncertainty
  method: http://purl.org/dc/terms/methodology
  methodDetail: http://www.w3.org/2004/02/skos/core#definition
  inputs:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment-output#uncertaintyInput
    x-jsonld-container: '@set'
  variable: https://w3id.org/ogc/hosted/seadots/experiment-output#variable
  value: http://qudt.org/schema/qudt/value
  valueUnits: http://qudt.org/schema/qudt/unit
  sigma: http://qudt.org/schema/qudt/standardUncertainty
  valueSource: http://purl.org/dc/terms/source
  valueKind: https://w3id.org/ogc/hosted/seadots/experiment-output#valueKind
  sigmaSource: http://purl.org/dc/terms/source
  sigmaKind: https://w3id.org/ogc/hosted/seadots/experiment-output#sigmaKind
  perTaxonVariance:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment-output#perTaxonVariance
    x-jsonld-container: '@set'
  D_times_AF: https://w3id.org/ogc/hosted/seadots/experiment-output#D_times_AF
  var_D_times_AF: https://w3id.org/ogc/hosted/seadots/experiment-output#var_D_times_AF
  shareWithinS: https://w3id.org/ogc/hosted/seadots/experiment-output#shareWithinS
  S_value_kg_m2: https://w3id.org/ogc/hosted/seadots/experiment-output#S_value_kg_m2
  S_sigma_kg_m2: https://w3id.org/ogc/hosted/seadots/experiment-output#S_sigma_kg_m2
  S_CV: https://w3id.org/ogc/hosted/seadots/experiment-output#S_CV
  varianceAttribution:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/experiment-output#varianceAttribution
    x-jsonld-container: '@set'
  term: http://www.w3.org/2004/02/skos/core#notation
  CV_squared: https://w3id.org/ogc/hosted/seadots/experiment-output#CV_squared
  dominantUncertainty: https://w3id.org/ogc/hosted/seadots/experiment-output#dominantUncertainty
  caveats:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
    x-jsonld-container: '@set'
  computeCodeNote: http://www.w3.org/2004/02/skos/core#note
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/experiment-output#
x-jsonld-prefixes:
  dcterms: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#
  skos: http://www.w3.org/2004/02/skos/core#
  seadots: https://w3id.org/ogc/hosted/seadots/experiment-output#
  sosa: http://www.w3.org/ns/sosa/
  qudt: http://qudt.org/schema/qudt/
  indo: https://id3.seadots.eu/indicator/
  dwc: http://rs.tdwg.org/dwc/terms/
  prov: http://www.w3.org/ns/prov#
  ssn: http://www.w3.org/ns/ssn/
  unit: http://qudt.org/vocab/unit/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/experiment-output/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/experiment-output/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/experiment-output#",
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "features": {
      "@container": "@set",
      "@id": "geojson:features"
    },
    "type": "@type",
    "id": "@id",
    "properties": {
      "@context": {
        "experimentOutput": {
          "@context": {
            "name": "dct:title",
            "role": "seadots:role",
            "format": "dct:format",
            "vocabularyTerm": {
              "@id": "skos:exactMatch",
              "@type": "@id"
            },
            "experiment": {
              "@id": "https://w3id.org/ogc/hosted/seadots/experiment#experiment",
              "@type": "@id"
            },
            "observedProperty": {
              "@id": "sosa:observedProperty",
              "@type": "@id"
            },
            "hasSimpleResult": "sosa:hasSimpleResult",
            "hasSimpleResultUnit": "qudt:unit",
            "resultTime": {
              "@id": "sosa:resultTime",
              "@type": "xsd:dateTime"
            },
            "phenomenonTime": "sosa:phenomenonTime",
            "hasFeatureOfInterest": {
              "@id": "sosa:hasFeatureOfInterest",
              "@type": "@id"
            },
            "aggregation": "seadots:aggregation",
            "data": {
              "@context": {
                "provenance": {
                  "@context": {
                    "values": "seadots:provenanceValues",
                    "derivedFrom": {
                      "@id": "prov:wasDerivedFrom",
                      "@type": "@id",
                      "@container": "@set"
                    },
                    "equationRecord": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    },
                    "computedOn": "dct:date",
                    "computeCode": {
                      "@id": "seadots:computeCode",
                      "@type": "@id"
                    },
                    "uncertaintyMethod": "seadots:uncertaintyMethod",
                    "note": "skos:note"
                  },
                  "@id": "prov:wasDerivedFrom"
                }
              },
              "@id": "seadots:data"
            }
          },
          "@id": "seadots:output"
        }
      },
      "@id": "geojson:properties"
    },
    "geometry": {
      "@context": {
        "coordinates": {
          "@container": "@list",
          "@id": "geojson:coordinates"
        }
      },
      "@id": "geojson:geometry"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "links": {
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:format",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "conformsTo": {
      "@container": "@set",
      "@id": "dct:conformsTo",
      "@type": "@id"
    },
    "time": "dct:temporal",
    "linkTemplates": {
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:format",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent",
        "uriTemplate": {
          "@type": "xsd:string",
          "@id": "rec:uriTemplate"
        },
        "varBase": "rec:varBase",
        "variables": {
          "@id": "rec:hasVariable",
          "@container": "@index",
          "@index": "dct:identifier"
        }
      },
      "@id": "rec:hasLinkTemplate"
    },
    "created": "dct:created",
    "updated": "dct:modified",
    "title": {
      "@container": "@set",
      "@id": "dct:title"
    },
    "description": {
      "@container": "@set",
      "@id": "dct:description"
    },
    "keywords": {
      "@container": "@set",
      "@id": "dcat:keyword"
    },
    "language": {
      "@id": "rec:language",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "languages": {
      "@container": "@set",
      "@id": "rec:languages",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "resourceLanguages": {
      "@container": "@set",
      "@id": "rec:resourceLanguages",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "externalIds": {
      "@container": "@set",
      "@id": "rec:scopedIdentifier",
      "@context": {
        "scheme": "rec:scheme",
        "value": "rec:id"
      }
    },
    "themes": {
      "@container": "@set",
      "@id": "rec:themes",
      "@context": {
        "concepts": {
          "@id": "rec:concept",
          "@context": {
            "id": {
              "@type": "xsd:string",
              "@id": "rec:conceptID"
            },
            "url": {
              "@type": "@id",
              "@id": "dcat:theme"
            }
          }
        },
        "scheme": "rec:scheme"
      }
    },
    "formats": {
      "@id": "rec:format",
      "@context": {
        "name": "rec:name"
      }
    },
    "contacts": {
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "license": "dct:license",
    "accessrights": "dct:accessRights",
    "variables": {
      "@container": "@id",
      "@id": "rec:hasVariable",
      "@context": {
        "@base": "http://example.com/variables/",
        "@vocab": "https://www.opengis.net/def/ogc-api/records/"
      }
    },
    "coordinates": "geojson:coordinates",
    "href": "@id",
    "rel": "geojson:rel",
    "concepts": {
      "@id": "skos:Concept",
      "@container": "@set"
    },
    "scheme": "skos:inScheme",
    "label": "skos:prefLabel",
    "mediaType": "dct:format",
    "start": {
      "@id": "w3ctime:hasBeginning",
      "@type": "xsd:dateTime"
    },
    "end": {
      "@id": "w3ctime:hasEnd",
      "@type": "xsd:dateTime"
    },
    "equation": "seadots:equation",
    "asOf_months": "seadots:asOf_months",
    "scenarioInterval": "dct:temporal",
    "units": "qudt:unit",
    "headline": "seadots:headline",
    "B_reef_kg": {
      "@id": "indo:floating-wind-reef-biomass",
      "@type": "qudt:QuantityValue"
    },
    "B_reef_tonnes": {
      "@id": "indo:floating-wind-reef-biomass",
      "@type": "qudt:QuantityValue"
    },
    "sigma_kg": "qudt:standardUncertainty",
    "sigma_tonnes": "qudt:standardUncertainty",
    "totalSigma_kg": "qudt:standardUncertainty",
    "totalSigma_tonnes": "qudt:standardUncertainty",
    "CV": "qudt:coefficientOfVariation",
    "totalCV": "qudt:coefficientOfVariation",
    "ci95_kg": "seadots:ci95_kg",
    "ci95_tonnes": "seadots:ci95_tonnes",
    "perTaxonAtT24": {
      "@id": "seadots:perTaxonAtT24",
      "@container": "@set"
    },
    "scientificName": "dwc:scientificName",
    "aphiaID": "dwc:taxonID",
    "A_sub_m2": {
      "@id": "indo:submerged-infrastructure-area",
      "@type": "qudt:QuantityValue"
    },
    "D_pre_kg_m2": {
      "@id": "indo:benthic-biomass-density",
      "@type": "qudt:QuantityValue"
    },
    "AF_i": {
      "@id": "indo:reef-aggregation-index",
      "@type": "qudt:DimensionlessQuantity"
    },
    "C_t": {
      "@id": "indo:colonisation-time-factor",
      "@type": "qudt:DimensionlessQuantity"
    },
    "B_kg": {
      "@id": "indo:floating-wind-reef-biomass",
      "@type": "qudt:QuantityValue"
    },
    "shareOfTotal": "seadots:shareOfTotal",
    "timeSeries": {
      "@id": "seadots:timeSeries",
      "@container": "@list"
    },
    "t_months": "seadots:t_months",
    "timeSeriesNote": "skos:note",
    "uncertainty": "seadots:uncertainty",
    "method": "dct:methodology",
    "methodDetail": "skos:definition",
    "inputs": {
      "@id": "seadots:uncertaintyInput",
      "@container": "@set"
    },
    "variable": "seadots:variable",
    "value": "qudt:value",
    "valueUnits": "qudt:unit",
    "sigma": "qudt:standardUncertainty",
    "valueSource": "dct:source",
    "valueKind": "seadots:valueKind",
    "sigmaSource": "dct:source",
    "sigmaKind": "seadots:sigmaKind",
    "perTaxonVariance": {
      "@id": "seadots:perTaxonVariance",
      "@container": "@set"
    },
    "D_times_AF": "seadots:D_times_AF",
    "var_D_times_AF": "seadots:var_D_times_AF",
    "shareWithinS": "seadots:shareWithinS",
    "S_value_kg_m2": "seadots:S_value_kg_m2",
    "S_sigma_kg_m2": "seadots:S_sigma_kg_m2",
    "S_CV": "seadots:S_CV",
    "varianceAttribution": {
      "@id": "seadots:varianceAttribution",
      "@container": "@set"
    },
    "term": "skos:notation",
    "CV_squared": "seadots:CV_squared",
    "dominantUncertainty": "seadots:dominantUncertainty",
    "caveats": {
      "@id": "skos:note",
      "@container": "@set"
    },
    "computeCodeNote": "skos:note",
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "rec": "https://www.opengis.net/def/ogc-api/records/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "w3ctime": "http://www.w3.org/2006/time#",
    "dctype": "http://purl.org/dc/dcmitype/",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "prov": "http://www.w3.org/ns/prov#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "thns": "https://w3id.org/ogc/stac/themes/",
    "dcterms": "http://purl.org/dc/terms/",
    "seadots": "https://w3id.org/ogc/hosted/seadots/experiment-output#",
    "sosa": "http://www.w3.org/ns/sosa/",
    "qudt": "http://qudt.org/schema/qudt/",
    "indo": "https://id3.seadots.eu/indicator/",
    "dwc": "http://rs.tdwg.org/dwc/terms/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "unit": "http://qudt.org/vocab/unit/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/experiment-output/context.jsonld)

## Sources

* [GeoDCAT mapping for OGC API Records](https://ogcincubator.github.io/geodcat-ogcapi-records/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/experiment-output`

