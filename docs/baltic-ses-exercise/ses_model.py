"""The Case-example II model and the Baltic calibration of baltic_ses_exercise.ipynb, as a module.

Used by the spatial extension notebook so that it starts from exactly the same model and parameters
as the main exercise (parts 1 and 3). Read the main notebook for the explanation of every step.
"""
from pathlib import Path
import numpy as np
import pandas as pd

DATA = Path(__file__).parent / "data"
YEARS = np.arange(2025, 2051)


def simulate(P, harvest, invest, T=26, start_year=0):
    """Excel model (Main sheet). harvest: number, list or f(t, x, w, P); invest: list of T values."""
    x, w, rows = P["x0"], P["w0"], []
    for t in range(T):
        G = (P["alpha"] - P["eps1"] * w) * x - P["beta"] * x**2
        q_try = harvest(t, x, w, P) if callable(harvest) else (harvest[t] if np.ndim(harvest) else harvest)
        q = min(max(q_try, 0.0), max(x + G, 0.0))
        Iw = max(invest[t], -w)
        bf = P["p"] * q - (P["cof1"] + P["eps2"] * w) * q**P["cof2"] / max(x, 1e-9)
        bw = P["pe"] * w - P["cofe1"] * w**P["cofe2"] - P["Iwp"] * Iw
        bp = P["pu1"] * (x + 1)**P["pu2"] * (w + 1)**P["pu3"]
        rows.append((start_year + t, x, w, q, Iw, bf, bw, bp))
        x, w = max(x + G - q, 0.0), w + Iw - P["dl"] * w
    d = pd.DataFrame(rows, columns=["year", "x", "w", "q", "Iw", "bf", "bw", "bp"])
    d["B"] = d.bf + d.bw + d.bp
    d["disc"] = (1 + P["roi"]) ** -(np.arange(T) + 1)
    return d


def present_values(d, P=None, terminal=False):
    pv = pd.Series({k: (d[k] * d.disc).sum() for k in ["bf", "bw", "bp", "B"]})
    if terminal:
        pv[["bw", "B"]] += P["Iwp"] * d.w.iloc[-1] * (1 - P["dl"]) * d.disc.iloc[-1]
    return pv


def calibrate(fit_from=1974):
    """Rebuild the calibrated parameter set P of the main notebook (part 3) from the bundled snapshot."""
    ices = pd.read_csv(DATA / "ices_sprat_spr.27.22-32_2025_summary.csv").astype(float)
    r = pd.read_csv(DATA / "ices_sprat_spr.27.22-32_2025_refpoints.csv").iloc[0]
    ref = {k: float(r[k]) for k in ["Blim", "Bpa", "MSYBtrigger", "FMSY", "Fpa"]}
    ices["x"], ices["q"] = ices.SSB / 1e6, ices.Catches / 1e6
    h = ices.dropna(subset=["x"]).reset_index(drop=True)
    h["S"] = h.x.shift(-1) - h.x + h.q
    fit = h[(h.Year >= fit_from) & h.S.notna()]
    (alpha, beta), *_ = np.linalg.lstsq(np.c_[fit.x, -fit.x**2], fit.S, rcond=None)
    Bmsy = alpha / (2 * beta)

    econ = pd.read_csv(DATA / "economic_inputs.csv").set_index("parameter")["value"]
    x24, q24 = ices.loc[ices.Year == 2024, ["x", "q"]].iloc[0]
    p_fish = econ["sprat_first_sale_price_PL_2024"] * 1000
    cof2 = 1.1
    cof1 = econ["fishing_cost_share"] * p_fish * q24 * x24 / q24**cof2
    P = dict(alpha=alpha, beta=beta, p=p_fish, cof1=cof1, cof2=cof2,
             pe=econ["offshore_wind_auction_price_2025"] * 8760 * econ["capacity_factor"] * 1000 / 1e6,
             cofe1=econ["wind_opex"], cofe2=1.0,
             Iwp=econ["baltica2_investment"] / (econ["baltica2_capacity"] / 1000),
             dl=1 / econ["turbine_lifetime"],
             pu1=100 / (Bmsy + 1) ** 0.9, pu2=0.9, pu3=-0.05,
             eps1=0.0, eps2=0.01 * cof1,
             x0=float(ices.loc[ices.Year == 2025, "x"].iloc[0]), w0=0.0,
             roi=econ["discount_rate"])

    national = pd.read_csv(DATA / "polish_offshore_wind_pipeline.csv")
    g = national[national.farm != "Baltic West"].groupby("first_power_or_completion_year").capacity_mw.sum() / 1000
    Iw_contracted = [float(g.get(y, 0.0)) for y in YEARS]

    def ices_rule(t, x, w, P):
        h_msy = (P["alpha"] - P["eps1"] * w) / 2
        return h_msy * min(1.0, x / (ref["MSYBtrigger"] / 1e6)) * x

    return dict(P=P, ref=ref, ices=ices, Bmsy=Bmsy, Iw_contracted=Iw_contracted, ices_rule=ices_rule,
                price_eur_mwh=float(econ["offshore_wind_auction_price_2025"]))


if __name__ == "__main__":
    c = calibrate()
    d = simulate(c["P"], c["ices_rule"], c["Iw_contracted"], start_year=2025)
    print(present_values(d, c["P"], terminal=True).round(0))   # main notebook, S1: 594 / -118 / 1219 / 1695
