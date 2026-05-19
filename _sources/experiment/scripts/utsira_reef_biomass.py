#!/usr/bin/env python3
"""
utsira_reef_biomass.py — deterministic reproducibility artefact for the
worked example documented in:

  ../examples/utsira_surroundings_experiment.json
  ../../experiment-output/examples/reef_biomass_result.json

Evaluates the reef-biomass equation

  B_reef(t) = sum_i ( A_sub * D_pre,i * AF_i * C_t )

from `equation-property-relationship/examples/reef-biomass-equation.json`
at the scenario end (t = 24 months) using six input records from the
per-input bblocks. Propagates uncertainty by
log-linear CV propagation under the refactoring

  B_reef = A_sub * C_t * S         with  S = sum_i (D_pre,i * AF_i)

so the scalar factors common to all taxa enter once, not three times.

This script IS the experiment's executable. It is linked from the
experiment record's `application` field and from each output record's
`data.provenance.computeCode` field.

Run:
    python3 utsira_reef_biomass.py            # prints summary + JSON
    python3 utsira_reef_biomass.py --json     # prints structured JSON only

Provenance: every input value carries a `provenance` block in its source
record. All sigma values used here are either pulled from the IMR row's
`uncertainty_kg_m2` field (used as a proxy for the MAREANO row, which
has no sigma) or assumed (sigma_A_rel, sigma_AF_rel, sigma_C). The
`assumed` ones are flagged in the script output.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

# ─── Paths ───────────────────────────────────────────────────────────────
HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]                       # .../bblocks-seadots
SOURCES = REPO_ROOT / "_sources"

# Each input now lives in its own bblock under `_sources/<bblock>/examples/<file>`.
# The keys here name the property under which `data` sits in that bblock's record.
INPUT_FILES = {
    "infrastructure": (SOURCES / "floating-wind-infrastructure/examples/utsira_nord_60x15mw.json",
                       "floatingWindInfrastructure"),
    "mareano":        (SOURCES / "benthic-biomass-density-mareano/examples/mareano_norwegian_shelf.json",
                       "benthicBiomassDensity"),
    "imr":            (SOURCES / "benthic-biomass-density-imr/examples/imr_ices_iva_fallback.json",
                       "benthicBiomassDensity"),
    "af":             (SOURCES / "reef-aggregation-index/examples/degraer2020_bindings.json",
                       "reefAggregationIndex"),
    "ct":             (SOURCES / "colonisation-time-factor/examples/default_sigmoid.json",
                       "colonisationTimeFactor"),
}


def load_input(key: str) -> dict:
    """Load the `data` block from an input record by logical key."""
    path, prop = INPUT_FILES[key]
    rec = json.loads(path.read_text())
    return rec["properties"][prop]["data"]


# ─── Assumed sigma values (not in any input record) ─────────────────────
SIGMA_A_REL = 0.15      # engineering tolerance for submerged area
SIGMA_AF_REL = 0.50     # wide literature variance on aggregation index
SIGMA_C_ABS = 0.02      # near sigmoid saturation at t = 24 mo

ASSUMED_SIGMAS = {
    "sigma_A_rel":  (SIGMA_A_REL,  "engineering tolerance, no source in input record"),
    "sigma_AF_rel": (SIGMA_AF_REL, "wide literature variance; Degraer 2020 gives no spread"),
    "sigma_C_abs":  (SIGMA_C_ABS,  "near sigmoid saturation; small sigma assumed"),
}


def compute() -> dict:
    """Run the worked B_reef calculation and return a structured result."""

    infra = load_input("infrastructure")
    mareano = load_input("mareano")
    imr = load_input("imr")
    af = load_input("af")
    ct = load_input("ct")

    # ─── Variables ──────────────────────────────────────────────────────
    A_sub = infra["aggregate"]["submerged_area_total_m2"]      # 109_500 m²

    D = {row["scientificName"]: row["density_kg_m2"] for row in mareano["perTaxon"]}
    # IMR row carries `uncertainty_kg_m2`; MAREANO row does not — use IMR
    # as a proxy for sigma until MAREANO retrieval is wired up.
    sigma_D = {row["scientificName"]: row["uncertainty_kg_m2"] for row in imr["perTaxon"]}

    AF = {row["scientificName"]: row["AF_i"] for row in af["perTaxon"]}

    L = ct["parameters"]["L"]
    k = ct["parameters"]["k"]
    t0 = ct["parameters"]["t0_months"]

    def C(t: float) -> float:
        return L / (1 + math.exp(-k * (t - t0)))

    C24 = C(24)

    # ─── Per-taxon contributions at t = 24 ──────────────────────────────
    per_taxon = []
    for taxon in D:
        B = A_sub * D[taxon] * AF[taxon] * C24
        per_taxon.append({
            "scientificName": taxon,
            "A_sub_m2": A_sub,
            "D_pre_kg_m2": D[taxon],
            "AF_i": AF[taxon],
            "C_t": round(C24, 4),
            "B_kg": round(B, 0),
        })

    B_reef_kg = sum(t["B_kg"] for t in per_taxon)
    for t in per_taxon:
        t["shareOfTotal"] = round(t["B_kg"] / B_reef_kg, 4)

    # ─── Time series ────────────────────────────────────────────────────
    S = sum(D[t] * AF[t] for t in D)
    time_series = []
    for row in ct["lookup"]:
        time_series.append({
            "t_months": row["t_months"],
            "C_t": row["C_t"],
            "B_reef_kg": round(A_sub * row["C_t"] * S, 0),
        })

    # ─── Uncertainty propagation ────────────────────────────────────────
    # σ²(Dᵢ·AFᵢ) = (Dᵢ·AFᵢ)² · (CV²_D + CV²_AF)   — independent
    per_taxon_var = []
    var_S = 0.0
    for taxon in D:
        cv_D = sigma_D[taxon] / D[taxon]
        cv_AF = SIGMA_AF_REL
        product = D[taxon] * AF[taxon]
        var_DAF = product**2 * (cv_D**2 + cv_AF**2)
        per_taxon_var.append({
            "scientificName": taxon,
            "D_times_AF": round(product, 3),
            "var_D_times_AF": round(var_DAF, 3),
        })
        var_S += var_DAF
    sigma_S = math.sqrt(var_S)
    cv_S = sigma_S / S
    for r in per_taxon_var:
        r["shareWithinS"] = round(r["var_D_times_AF"] / var_S, 4)

    # CV²(B_reef) = CV²(A_sub) + CV²(C_t) + CV²(S)    — independent
    cv_C = SIGMA_C_ABS / C24
    cv_B_sq = SIGMA_A_REL**2 + cv_C**2 + cv_S**2
    cv_B = math.sqrt(cv_B_sq)
    sigma_B = cv_B * B_reef_kg

    attribution = [
        {"term": "A_sub", "CV_squared": round(SIGMA_A_REL**2, 4),
         "shareOfTotal": round(SIGMA_A_REL**2 / cv_B_sq, 4)},
        {"term": "C_t", "CV_squared": round(cv_C**2, 4),
         "shareOfTotal": round(cv_C**2 / cv_B_sq, 4)},
        {"term": "S = sum_i (D_i*AF_i)", "CV_squared": round(cv_S**2, 4),
         "shareOfTotal": round(cv_S**2 / cv_B_sq, 4)},
    ]

    return {
        "equation": "B_reef(t) = sum_i (A_sub * D_pre,i * AF_i * C_t)",
        "asOf_months": 24,
        "headline": {
            "B_reef_kg": round(B_reef_kg, 0),
            "B_reef_tonnes": round(B_reef_kg / 1000, 1),
            "sigma_kg": round(sigma_B, 0),
            "sigma_tonnes": round(sigma_B / 1000, 1),
            "CV": round(cv_B, 3),
            "ci95_tonnes": [round((B_reef_kg - 1.96 * sigma_B) / 1000),
                            round((B_reef_kg + 1.96 * sigma_B) / 1000)],
        },
        "perTaxonAtT24": per_taxon,
        "timeSeries": time_series,
        "uncertainty": {
            "method": "log-linear CV propagation; B_reef = A_sub * C_t * S",
            "S_value_kg_m2": round(S, 4),
            "S_sigma_kg_m2": round(sigma_S, 3),
            "S_CV": round(cv_S, 3),
            "perTaxonVariance": per_taxon_var,
            "varianceAttribution": attribution,
            "assumedSigmas": [
                {"name": k, "value": v[0], "rationale": v[1]}
                for k, v in ASSUMED_SIGMAS.items()
            ],
        },
        "provenance": {
            "values": "computed",
            "derivedFrom": [
                str(p.relative_to(SOURCES)) for p, _ in INPUT_FILES.values()
            ],
            "equationRecord": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
            "computeCode": "experiment/scripts/utsira_reef_biomass.py",
            "uncertaintyMethod": "log-linear CV propagation; taxa treated independent within S",
            "note": "Inputs are illustrative (see each input record's data.provenance). `values: computed` refers to the calculation chain, not to a real-world measurement.",
        },
    }


def main(argv: list[str]) -> int:
    result = compute()
    if "--json" in argv:
        print(json.dumps(result, indent=2))
        return 0

    h = result["headline"]
    print(f"B_reef(24 mo) = {h['B_reef_tonnes']} ± {h['sigma_tonnes']} t   "
          f"(CV={h['CV']}, 95% CI {h['ci95_tonnes']} t)")
    print()
    print("Per-taxon at t = 24 mo:")
    for t in result["perTaxonAtT24"]:
        print(f"  {t['scientificName']:20s}  B = {t['B_kg']:>10,.0f} kg  "
              f"({100*t['shareOfTotal']:.1f}% of total)")
    print()
    print("Time series (lookup C_t):")
    for t in result["timeSeries"]:
        print(f"  t = {t['t_months']:>2} mo  C_t = {t['C_t']:.2f}  "
              f"B_reef = {t['B_reef_kg']:>10,.0f} kg")
    print()
    print("Variance attribution (share of CV²(B_reef)):")
    for a in result["uncertainty"]["varianceAttribution"]:
        print(f"  {a['term']:22s}  {a['CV_squared']:.4f}  ({100*a['shareOfTotal']:.1f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
