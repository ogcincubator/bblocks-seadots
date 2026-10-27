"""Reusable model calculations for the Baltic SES exercise notebooks.

This module contains model mechanics and calibration transformations only. The
notebooks own file/API input, source selection, and execution order.
"""
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).parent / "data"
YEARS = np.arange(2025, 2051)


def simulate(P, harvest, invest, T=26, start_year=0):
    """Run the Excel Main-sheet model for T years.

    ``harvest`` may be a scalar, a length-T sequence, or ``f(t, x, w, P)``.
    ``invest`` is annual new capacity in GW.
    """
    x, w, rows = P["x0"], P["w0"], []
    for t in range(T):
        growth = (P["alpha"] - P["eps1"] * w) * x - P["beta"] * x**2
        q_try = harvest(t, x, w, P) if callable(harvest) else (harvest[t] if np.ndim(harvest) else harvest)
        q = min(max(q_try, 0.0), max(x + growth, 0.0))
        Iw = max(invest[t], -w)
        bf = P["p"] * q - (P["cof1"] + P["eps2"] * w) * q**P["cof2"] / max(x, 1e-9)
        bw = P["pe"] * w - P["cofe1"] * w**P["cofe2"] - P["Iwp"] * Iw
        bp = P["pu1"] * (x + 1) ** P["pu2"] * (w + 1) ** P["pu3"]
        rows.append((start_year + t, x, w, q, Iw, bf, bw, bp))
        x, w = max(x + growth - q, 0.0), w + Iw - P["dl"] * w
    result = pd.DataFrame(rows, columns=["year", "x", "w", "q", "Iw", "bf", "bw", "bp"])
    result["B"] = result.bf + result.bw + result.bp
    result["disc"] = (1 + P["roi"]) ** -(np.arange(T) + 1)
    return result


def present_values(result, P=None, terminal=False):
    """Return discounted sector and total benefits; optionally include terminal wind value."""
    pv = pd.Series({key: (result[key] * result.disc).sum() for key in ["bf", "bw", "bp", "B"]})
    if terminal:
        terminal_value = P["Iwp"] * result.w.iloc[-1] * (1 - P["dl"]) * result.disc.iloc[-1]
        pv[["bw", "B"]] += terminal_value
    return pv


def fit_surplus_production(ices, fit_from=1974):
    """Fit S = alpha*x - beta*x² to ICES rows already expressed as x and q in Mt."""
    history = ices.dropna(subset=["x"]).reset_index(drop=True).copy()
    history["S"] = history.x.shift(-1) - history.x + history.q
    fit = history[(history.Year >= fit_from) & history.S.notna()]
    design = np.c_[fit.x, -fit.x**2]
    (alpha, beta), *_ = np.linalg.lstsq(design, fit.S, rcond=None)
    residual = fit.S - design @ [alpha, beta]
    r2 = 1 - (residual**2).sum() / ((fit.S - fit.S.mean())**2).sum()
    return {"history": history, "fit": fit, "alpha": alpha, "beta": beta, "R2": r2,
            "K": alpha / beta, "Bmsy": alpha / (2 * beta), "MSY": alpha**2 / (4 * beta)}


def build_parameter_set(ices, econ, alpha, beta, assumptions=None):
    """Translate loaded ICES/economic inputs into the parameter dictionary used by simulate().

    ``ices`` has x and q columns in Mt; ``econ`` is indexed by parameter and has a value column.
    Assumption overrides are explicit so a notebook can expose the values learners may change.
    """
    a = {"cof2": 1.1, "cofe2": 1.0, "pu2": 0.9, "pu3": -0.05,
         "eps1": 0.0, "eps2_share": 0.01, "w0": 0.0}
    if assumptions:
        a.update(assumptions)
    x24, q24 = ices.loc[ices.Year == 2024, ["x", "q"]].iloc[0]
    price_fish = econ.loc["sprat_first_sale_price_PL_2024", "value"] * 1000
    cof1 = econ.loc["fishing_cost_share", "value"] * price_fish * q24 * x24 / q24**a["cof2"]
    wind_price = econ.loc["offshore_wind_auction_price_2025", "value"]
    capacity_factor = econ.loc["capacity_factor", "value"]
    pe = wind_price * 8760 * capacity_factor * 1000 / 1e6
    investment_cost = econ.loc["baltica2_investment", "value"] / (econ.loc["baltica2_capacity", "value"] / 1000)
    depreciation = 1 / econ.loc["turbine_lifetime", "value"]
    Bmsy = alpha / (2 * beta)
    P = dict(alpha=alpha, beta=beta, p=price_fish, cof1=cof1, cof2=a["cof2"], pe=pe,
             cofe1=econ.loc["wind_opex", "value"], cofe2=a["cofe2"], Iwp=investment_cost,
             dl=depreciation, pu1=100 / (Bmsy + 1) ** a["pu2"], pu2=a["pu2"], pu3=a["pu3"],
             eps1=a["eps1"], eps2=a["eps2_share"] * cof1,
             x0=float(ices.loc[ices.Year == 2025, "x"].iloc[0]), w0=a["w0"],
             roi=econ.loc["discount_rate", "value"])
    return P


def update_ices_dependent_parameters(P, ices, econ, alpha, beta):
    """Update parameters recalculated when the ICES assessment edition changes."""
    updated = dict(P, alpha=alpha, beta=beta)
    x24, q24 = ices.loc[ices.Year == 2024, ["x", "q"]].iloc[0]
    updated["x0"] = float(ices.loc[ices.Year == 2025, "x"].iloc[0])
    updated["cof1"] = econ.loc["fishing_cost_share", "value"] * P["p"] * q24 * x24 / q24**P["cof2"]
    updated["eps2"] = P["eps2"] / P["cof1"] * updated["cof1"]
    updated["pu1"] = 100 / (alpha / (2 * beta) + 1) ** P["pu2"]
    return updated


def investment_path(national, years=YEARS, exclude_farms=()):
    """Aggregate pipeline MW by first-power year and return annual additions in GW."""
    selected = national[~national.farm.isin(exclude_farms)]
    grouped = selected.groupby("first_power_or_completion_year").capacity_mw.sum() / 1000
    return [float(grouped.get(year, 0.0)) for year in years]


def ices_harvest_rule(ref):
    """Create the ICES-style harvest rule using MSY Btrigger from the loaded reference points."""
    biomass_trigger = ref["MSYBtrigger"] / 1e6

    def rule(t, x, w, P):
        h_msy = (P["alpha"] - P["eps1"] * w) / 2
        return h_msy * min(1.0, x / biomass_trigger) * x

    return rule


def fixed_catch(level):
    """Create a harvest policy that requests the same catch each year."""
    return lambda t, x, w, P: level


def strong_interaction_parameters(P, investment, growth_effect=0.05, cost_share=0.05):
    """Apply scenario assumptions for growth and fishing-cost effects at full build-out."""
    total_capacity = sum(investment)
    return {**P, "eps1": growth_effect * P["alpha"] / total_capacity,
            "eps2": cost_share * P["cof1"]}


def run_scenarios(scenarios, start_year=2025):
    """Run a mapping of key -> (label, parameters, harvest policy, investment path)."""
    runs = {key: simulate(params, harvest, investment, start_year=start_year)
            for key, (_, params, harvest, investment) in scenarios.items()}
    pvs = pd.DataFrame({key: present_values(result, scenarios[key][1], terminal=True)
                        for key, result in runs.items()}).T
    return runs, pvs


def sustainable_fishery_returns(P, biomass, wind_capacity):
    """Return logistic sustainable catch and fishery net benefit at each biomass value."""
    biomass = np.asarray(biomass)
    catch = np.clip((P["alpha"] - P["eps1"] * wind_capacity) * biomass - P["beta"] * biomass**2, 0, None)
    benefit = P["p"] * catch - (P["cof1"] + P["eps2"] * wind_capacity) * catch**P["cof2"] / biomass
    return catch, benefit


def wind_steady_state_returns(P, capacity):
    """Return annual wind revenue, O&M plus replacement/capital cost, and net benefit."""
    capacity = np.asarray(capacity)
    revenue = P["pe"] * capacity
    cost = P["cofe1"] * capacity**P["cofe2"] + (P["dl"] + P["roi"]) * P["Iwp"] * capacity
    return revenue, cost, revenue - cost
