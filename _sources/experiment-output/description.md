# Computational Experiment Output

OGC API Records profile for one output artefact produced by a computational experiment.

Each instance describes a single output — a primary result file, a catalog, or a provenance record. The schema is intentionally narrow so that an `experiment` record can reference many `experiment-output` records by URI and an audit pipeline can resolve each artefact independently.

Captured fields:

1. **Role** — `primary result`, `catalog`, `provenance`, `diagnostic`. Mirrors the `role` field on `experiment-input`.
2. **Format** — media type or URI for the artefact's format profile (e.g. `https://geoparquet.org/`, `application/ld+json`).
3. **Vocabulary term** — concept URI for the produced quantity (e.g. `floating-wind-reef-biomass`).
4. **CWL binding** — `cwlOutput` port name and the consuming experiment URI.
5. **Conformance** — optional list of conformance class URIs (e.g. the SeaDOTs EDITO output conventions, STAC version).
6. **Inline data** — every example MUST embed representative result values inside the `data` object so a reader can see what the output actually carries. Same `provenance` requirement as `experiment-input` — see the worked example below.

Outputs may be self-contained datasets, references to STAC collections, or PROV-O records that close the loop back to the experiment's inputs and the modelled equation.

---

## Worked example — reef-biomass result for the Utsira surroundings experiment

The example `examples/reef_biomass_geoparquet.json` is the primary result of the experiment described in `_sources/experiment/examples/utsira_surroundings_experiment.json`. It evaluates the reef-biomass equation

$$B_{reef}(t) \;=\; \sum_i \bigl( A_{sub} \cdot D_{pre,i} \cdot AF_i \cdot C_t \bigr)$$

over the scenario time span (2026-05-13 → 2028-05-13, 24 months) using the input records in `_sources/experiment-input/examples/`. Every variable is traceable to a specific input record; every value below carries an explicit provenance flag.

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
