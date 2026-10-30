"""Turbine-level production calculations for baltic_ses_production_extension.ipynb.

Pure functions only: the notebook loads the data files and chooses the assumptions.
Wind speeds are in m/s, power in kW, distances in metres, directions in degrees
(meteorological: the direction the wind blows FROM, clockwise from north).
"""
import numpy as np
import pandas as pd

BIN_CENTRES = np.arange(31) + 0.5          # 1 m/s histogram bins 0-1, 1-2, ... 30+


# ---------------------------------------------------------------- power curves
def reference_curve(ref):
    """Power (kW) and thrust coefficient of a published table, as functions of wind speed."""
    v, p, ct = ref.wind_speed_ms.to_numpy(), ref.power_kw.to_numpy(), ref.ct.to_numpy()
    lo, hi = v.min(), v.max()

    def power(speed):
        speed = np.asarray(speed, float)
        return np.where((speed >= lo) & (speed <= hi), np.interp(speed, v, p), 0.0)

    def thrust(speed):
        speed = np.asarray(speed, float)
        return np.where((speed >= lo) & (speed <= hi), np.interp(speed, v, ct), 0.0)

    return power, thrust


def spec_anchored_curve(ref, rated_kw, cut_in, rated_speed, cut_out,
                        ref_cut_in=3.0, ref_rated=10.6, ref_cut_out=25.0):
    """Datasheet-anchored power and thrust curves built on a reference turbine's shape.

    The reference curve is stretched so that its cut-in, rated speed and cut-out
    coincide with the datasheet values, and scaled to the datasheet rated power.
    This is an ASSUMPTION standing in for the manufacturer's curve, which is not public.
    """
    ref_power, ref_thrust = reference_curve(ref)
    ref_rated_kw = ref.power_kw.max()

    def to_reference_speed(speed):
        speed = np.asarray(speed, float)
        below = ref_cut_in + (speed - cut_in) * (ref_rated - ref_cut_in) / (rated_speed - cut_in)
        above = ref_rated + (speed - rated_speed) * (ref_cut_out - ref_rated) / (cut_out - rated_speed)
        return np.where(speed <= rated_speed, below, above)

    def power(speed):
        speed = np.asarray(speed, float)
        p = ref_power(to_reference_speed(speed)) / ref_rated_kw * rated_kw
        p = np.where(speed >= rated_speed, rated_kw, p)
        return np.where((speed >= cut_in) & (speed <= cut_out), p, 0.0)

    def thrust(speed):
        speed = np.asarray(speed, float)
        ct = ref_thrust(np.clip(to_reference_speed(speed), ref_cut_in, ref_cut_out))
        return np.where((speed >= cut_in) & (speed <= cut_out), ct, 0.0)

    return power, thrust


def rotor_physics_curve(ref, rated_kw, swept_area_m2, cut_in, cut_out, rho=1.225,
                        ref_cut_in=3.0, ref_rated=10.6, ref_cut_out=25.0):
    """Power and thrust curves from the turbine's own rotor area and the reference aerodynamics.

    Below rated power P = Cp_ref(v) * 0.5 * rho * A * v^3, with the reference turbine's
    below-rated power coefficient; capped at the datasheet rated power. Rated speed follows
    from the physics instead of the datasheet. An ASSUMPTION: it presumes the rotor is as
    efficient as the IEA reference design, so it brackets the datasheet-anchored curve from above.
    """
    ref_power, ref_thrust = reference_curve(ref)
    below = ref[ref.wind_speed_ms <= ref_rated]
    cp_max = below.cp.max()

    def cp(speed):
        return np.interp(speed, below.wind_speed_ms, below.cp, left=below.cp.iloc[0], right=cp_max)

    rated_speed = (rated_kw * 1000 / (0.5 * rho * swept_area_m2 * cp_max))**(1 / 3)

    def power(speed):
        speed = np.asarray(speed, float)
        p = np.minimum(cp(speed) * 0.5 * rho * swept_area_m2 * speed**3 / 1000, rated_kw)
        return np.where((speed >= cut_in) & (speed <= cut_out), p, 0.0)

    def thrust(speed):
        speed = np.asarray(speed, float)
        v_ref = np.where(speed <= rated_speed, speed * ref_rated / rated_speed,
                         ref_rated + (speed - rated_speed) * (ref_cut_out - ref_rated) / (cut_out - rated_speed))
        ct = ref_thrust(np.clip(v_ref, ref_cut_in, ref_cut_out))
        return np.where((speed >= cut_in) & (speed <= cut_out), ct, 0.0)

    power.rated_speed = rated_speed
    return power, thrust


def blend_curves(*curves):
    """Average several (power, thrust) curve pairs, e.g. a central estimate between two bounds."""
    def power(speed):
        return np.mean([c[0](speed) for c in curves], axis=0)

    def thrust(speed):
        return np.mean([c[1](speed) for c in curves], axis=0)

    return power, thrust


def generic_curve(rated_kw=15000, cut_in=3.0, rated_speed=10.6, cut_out=25.0):
    """The cubic curve of the spatial extension (no thrust curve; Ct fixed at 0.8 below rated)."""
    def power(speed):
        speed = np.asarray(speed, float)
        p = np.where(speed < rated_speed, (speed**3 - cut_in**3) / (rated_speed**3 - cut_in**3), 1.0)
        return np.where((speed >= cut_in) & (speed <= cut_out), p * rated_kw, 0.0)

    def thrust(speed):
        speed = np.asarray(speed, float)
        ct = np.where(speed < rated_speed, 0.8, 0.8 * (rated_speed / np.maximum(speed, 1e-9))**3)
        return np.where((speed >= cut_in) & (speed <= cut_out), ct, 0.0)

    return power, thrust


def implied_cp(power_fn, swept_area_m2, speed, rho=1.225):
    """Power coefficient implied by a curve: P / (0.5 rho A v^3); a physics sanity check (< 0.593)."""
    speed = np.asarray(speed, float)
    return power_fn(speed) * 1000 / (0.5 * rho * swept_area_m2 * speed**3)


# ------------------------------------------------------------ wind statistics
def parse_counts(series):
    """Turn space-separated count strings into an integer array (rows x 31 bins)."""
    return np.array([np.array(s.split(), dtype=int) for s in series])


def gross_capacity_factor(counts, power_fn, rated_kw):
    """Capacity factor of a single free-standing turbine from a wind-speed histogram."""
    counts = np.asarray(counts, float)
    return float((counts * power_fn(BIN_CENTRES)).sum() / counts.sum() / rated_kw)


def shear_exponent(mean_low, mean_high, z_low, z_high):
    """Power-law shear exponent alpha from mean speeds at two heights."""
    return np.log(mean_high / mean_low) / np.log(z_high / z_low)


# --------------------------------------------------------------------- layouts
def local_xy(lon, lat, lon0=None, lat0=None):
    """Equirectangular projection to metres around the layout centre (adequate over ~50 km)."""
    lon, lat = np.asarray(lon, float), np.asarray(lat, float)
    lon0 = lon.mean() if lon0 is None else lon0
    lat0 = lat.mean() if lat0 is None else lat0
    return np.c_[(lon - lon0) * 111_320 * np.cos(np.radians(lat0)), (lat - lat0) * 110_570]


def _overlap_fraction(distance, wake_radius, rotor_radius):
    """Share of the downstream rotor disc inside the wake circle."""
    d, R, r = np.broadcast_arrays(np.asarray(distance, float), np.asarray(wake_radius, float),
                                  np.asarray(rotor_radius, float))
    out = np.zeros(d.shape)
    inside = d <= R - r
    out[inside] = 1.0
    partial = (d < R + r) & ~inside
    if partial.any():
        dp, Rp, rp = d[partial], R[partial], r[partial]
        a1 = rp**2 * np.arccos(np.clip((dp**2 + rp**2 - Rp**2) / (2 * dp * rp), -1, 1))
        a2 = Rp**2 * np.arccos(np.clip((dp**2 + Rp**2 - rp**2) / (2 * dp * Rp), -1, 1))
        a3 = 0.5 * np.sqrt(np.clip((-dp + rp + Rp) * (dp + rp - Rp) * (dp - rp + Rp) * (dp + rp + Rp), 0, None))
        out[partial] = (a1 + a2 - a3) / (np.pi * rp**2)
    return out


def jensen_geometry(xy, rotor_d, direction_deg, k=0.04):
    """Wake geometry factor G[i, j] of upstream turbine i on turbine j (Jensen / Park model).

    The velocity deficit at j caused by i is (1 - sqrt(1 - Ct_i)) * G[i, j].
    """
    theta = np.radians(direction_deg)
    downwind = -np.array([np.sin(theta), np.cos(theta)])        # the wind blows towards this unit vector
    rel = xy[None, :, :] - xy[:, None, :]                       # i -> j vectors
    along = rel @ downwind
    across = np.abs(rel[..., 0] * downwind[1] - rel[..., 1] * downwind[0])
    d_i = np.asarray(rotor_d, float)[:, None]
    r_j = np.asarray(rotor_d, float)[None, :] / 2
    wake_radius = d_i / 2 + k * np.clip(along, 0, None)
    expansion = (d_i / (d_i + 2 * k * np.clip(along, 0, None)))**2
    geometry = np.where(along > 1.0, expansion * _overlap_fraction(across, wake_radius, r_j), 0.0)
    np.fill_diagonal(geometry, 0.0)
    return geometry


def wake_energy(xy, turbine_type, curves, rotor_d, rose, k=0.04, sub_directions=5, iterations=3):
    """Energy with and without wakes for a layout and a direction x speed wind rose.

    ``turbine_type`` names a key of ``curves`` (power_fn, thrust_fn) for each turbine;
    ``rose`` is a (sectors x 31) array of hour counts, sector i centred on i*360/sectors.
    Wake deficits are combined as the root-sum-square (Katic et al. 1986). Returns per-turbine
    energy (kWh) with wakes and without wakes, and per-sector energy with wakes.
    """
    rose = np.asarray(rose, float)
    n_sectors = rose.shape[0]
    width = 360 / n_sectors
    offsets = (np.arange(sub_directions) + 0.5) / sub_directions * width - width / 2
    types = np.asarray(turbine_type)
    U = BIN_CENTRES[:, None] * np.ones(len(xy))[None, :]        # bins x turbines
    free = np.zeros((31, len(xy)))
    for name, (power_fn, _) in curves.items():
        free[:, types == name] = power_fn(U[:, types == name])

    with_wakes = np.zeros(len(xy))
    by_sector = np.zeros(n_sectors)
    for s in range(n_sectors):
        sector_energy = np.zeros(len(xy))
        for offset in offsets:
            G2 = jensen_geometry(xy, rotor_d, s * width + offset, k)**2
            u = U.copy()
            for _ in range(iterations):
                a = np.zeros_like(u)
                for name, (_, thrust_fn) in curves.items():
                    a[:, types == name] = 1 - np.sqrt(1 - np.clip(thrust_fn(u[:, types == name]), 0, 0.99))
                u = U * (1 - np.sqrt((a**2) @ G2))
            power = np.zeros_like(u)
            for name, (power_fn, _) in curves.items():
                power[:, types == name] = power_fn(u[:, types == name])
            sector_energy += (rose[s][:, None] * power).sum(0) / sub_directions
        with_wakes += sector_energy
        by_sector[s] = sector_energy.sum()
    without = (rose.sum(0)[:, None] * free).sum(0)
    return with_wakes, without, by_sector


def net_capacity_factor(gross_cf, wake_efficiency, availability=0.95, electrical=0.98):
    """Net capacity factor = gross x wake efficiency x availability x electrical efficiency."""
    return gross_cf * wake_efficiency * availability * electrical


# =============================================================== analysis steps used by the notebook
# Each function is one logical step; the notebook only chooses inputs and assumptions.

def turbines_from_osm(data, rules):
    """OpenStreetMap wind-turbine nodes -> GeoDataFrame with the wind site each turbine belongs to.

    ``rules`` = {site: {"model": ..., "ref_prefix": ..., "relation": "relation/<id>"}}; the first matching
    rule wins. ``data`` is the raw OSM GeoJSON (dict or path).
    """
    import json as _json
    import geopandas as gpd
    from shapely.geometry import shape
    fc = _json.loads(open(data, encoding="utf-8").read()) if not isinstance(data, dict) else data
    members = {}
    for f in fc["features"]:
        if f["properties"].get("osm_type") == "relation":
            members[f["id"]] = {m.split(":")[0] for m in f["properties"].get("members", [])}
    def site_of(f):
        tags = f["properties"]["tags"]
        for site, rule in rules.items():
            if "ref_prefix" in rule and tags.get("ref", "").startswith(rule["ref_prefix"]):
                return site
            if "relation" in rule and f["id"] in members.get(rule["relation"], ()):
                return site
            if "model" in rule and tags.get("model") == rule["model"] and "ref_prefix" not in rule:
                return site
        return None
    rows = [{"osm_id": f["id"], "wind_site": site_of(f), "model": f["properties"]["tags"].get("model"),
             "rotor_d": float(f["properties"]["tags"]["rotor:diameter"]),
             "hub_m_osm": f["properties"]["tags"].get("height:hub"), "ref": f["properties"]["tags"].get("ref"),
             "geometry": shape(f["geometry"])}
            for f in fc["features"] if f["properties"]["tags"].get("power") == "generator"]
    return gpd.GeoDataFrame(rows, geometry="geometry", crs="EPSG:4326")


def layout_summary(turbines, assignment, national):
    """Turbines per wind site with model, rotor, OSM hub height and installed MW vs national MW."""
    summary = turbines.groupby("wind_site").agg(turbines=("osm_id", "size"), model=("model", "first"),
                                                rotor_m=("rotor_d", "first"), hub_m_osm=("hub_m_osm", "first"))
    a = assignment.set_index("wind_site")
    summary = summary.join(a[["project", "unit_mw", "hub_m", "share_of_project"]])
    summary["MW_from_turbines"] = summary.turbines * summary.unit_mw
    summary["MW_national"] = summary.project.map(national.set_index("farm").capacity_mw) * summary.share_of_project
    return summary.drop(columns="share_of_project")


def load_wind_histograms(path):
    """Wind-speed histograms by site, source and height; ``counts`` holds the 31-bin arrays."""
    hist = pd.read_csv(path)
    hist["counts"] = list(parse_counts(hist.counts_0_to_30ms))
    return hist.drop(columns="counts_0_to_30ms")


def load_wind_roses(path):
    """Hub-height wind roses -> {site: (sectors x 31) array}, sectors ordered by direction."""
    rose = pd.read_csv(path)
    return {site: parse_counts(g.sort_values("sector_deg").counts_0_to_30ms) for site, g in rose.groupby("site")}


def counts_at(hist, site, source, height):
    return hist[(hist.site == site) & (hist.source == source) & (hist.height_m == height)].counts.iloc[0]


def mean_profiles(hist):
    """Mean wind speed: rows (site, source), columns height in m."""
    return hist.pivot_table(index=["site", "source"], columns="height_m", values="mean_ms")


def shear_table(profile):
    """Power-law shear exponents of the mean profile per site: ICON-EU 100->180 m and ERA5 10->100 m."""
    icon, era = profile.xs("icon_eu", level="source"), profile.xs("era5", level="source")
    return pd.DataFrame({"ICON 100→180 m": shear_exponent(icon[100], icon[180], 100, 180),
                         "ERA5 10→100 m": shear_exponent(era[10], era[100], 10, 100)})


def build_power_curves(specs, reference):
    """Power and thrust curves per turbine model -> {"low"|"mid"|"high": {model: (power_fn, thrust_fn)}}.

    Published reference curves are used as they are; for commercial turbines without a public curve,
    low = datasheet-anchored, high = rotor physics, mid = their average. A generic 15 MW cubic curve
    (extension 1) is added under ``generic (extension 1)``.
    """
    sets = {"low": {}, "mid": {}, "high": {}}
    for model, s in specs.iterrows():
        if str(s.power_curve).startswith("published"):
            curve = reference_curve(reference)
            for k in sets:
                sets[k][model] = curve
            continue
        low = spec_anchored_curve(reference, s.rated_kw, s.cut_in_ms, s.rated_speed_ms, s.cut_out_ms)
        high = rotor_physics_curve(reference, s.rated_kw, s.swept_area_m2, s.cut_in_ms, s.cut_out_ms)
        sets["low"][model], sets["high"][model], sets["mid"][model] = low, high, blend_curves(low, high)
    for k in sets:
        sets[k]["generic (extension 1)"] = generic_curve(15000, 3.0, 10.6, 25.0)
    return sets


def rated_speeds(specs, curves):
    """Datasheet rated speed next to the speed at which the rotor-physics curve reaches rated power."""
    out = specs[["rated_kw", "rotor_d_m", "cut_in_ms", "rated_speed_ms", "cut_out_ms"]].rename(
        columns={"rated_speed_ms": "rated speed: datasheet"})
    out["rated speed: rotor physics"] = [getattr(curves["high"][m][0], "rated_speed", np.nan) for m in out.index]
    return out


def gross_cf_table(assignment, hist, curves, specs):
    """Gross capacity factor of a free-standing turbine per wind site under alternative data and curves."""
    rows = []
    for _, a in assignment.iterrows():
        rated = specs.loc[a.turbine_model, "rated_kw"]
        cf = lambda source, height, curve_set="mid", model=a.turbine_model, kw=rated: gross_capacity_factor(
            counts_at(hist, a.wind_site, source, height), curves[curve_set][model][0], kw)
        rows.append({"wind_site": a.wind_site, "project": a.project, "turbine": a.turbine_model, "hub_m": a.hub_m,
                     "band at hub (ICON)": f"{cf('icon_eu', a.hub_m, 'low'):.3f}–{cf('icon_eu', a.hub_m, 'high'):.3f}",
                     "generic curve, ERA5 100 m": cf("era5", 100, "mid", "generic (extension 1)", 15000),
                     "turbine curve, ERA5 100 m": cf("era5", 100),
                     "turbine curve, ICON 100 m": cf("icon_eu", 100),
                     "turbine curve, ICON hub": cf("icon_eu", a.hub_m),
                     "turbine curve, DMI hub (2025)": cf("dmi_harmonie", a.hub_m)})
    return pd.DataFrame(rows).set_index("wind_site")


def wake_efficiencies(turbines, roses, curves, k=0.04):
    """Jensen wake efficiency per site, each farm alone and all farms as one cluster.

    Returns (DataFrame per site, turbines with an ``efficiency`` column, cluster energy by sector).
    The cluster uses the mean of the sites' wind roses.
    """
    isolated = {}
    for site, g in turbines.groupby("wind_site"):
        w, wo, _ = wake_energy(local_xy(g.geometry.x, g.geometry.y), g.model.values,
                               {m: curves[m] for m in g.model.unique()}, g.rotor_d.values, roses[site], k=k)
        isolated[site] = w.sum() / wo.sum()
    sites = list(isolated)
    cluster_rose = sum(roses[s] for s in sites) / len(sites)
    w, wo, by_sector = wake_energy(local_xy(turbines.geometry.x, turbines.geometry.y), turbines.model.values,
                                   {m: curves[m] for m in turbines.model.unique()}, turbines.rotor_d.values,
                                   cluster_rose, k=k)
    out = turbines.assign(efficiency=w / wo, energy=w, energy_free=wo)
    in_cluster = out.groupby("wind_site").energy.sum() / out.groupby("wind_site").energy_free.sum()
    table = pd.DataFrame({"isolated": pd.Series(isolated), "in the cluster": in_cluster})
    table["wake loss, isolated (%)"] = 100 * (1 - table.isolated)
    table["wake loss, cluster (%)"] = 100 * (1 - table["in the cluster"])
    shares = pd.DataFrame({"share of hours": cluster_rose.sum(1) / cluster_rose.sum(),
                           "share of energy": by_sector / by_sector.sum()},
                          index=np.arange(len(by_sector)) * 360 / len(by_sector))
    return table, out.drop(columns=["energy", "energy_free"]), shares


def net_cf_by_project(gross, wakes, assignment, national, availability=0.95, electrical=0.98,
                      gross_column="turbine curve, ICON hub"):
    """Net capacity factor per national project; sites without a layout get the mean modelled wake efficiency."""
    mw = assignment.set_index("wind_site").project.map(national.set_index("farm").capacity_mw) * \
         assignment.set_index("wind_site").share_of_project
    modelled = wakes["in the cluster"]
    default = np.average(modelled, weights=mw.loc[modelled.index])
    net = gross[["project", "turbine", "hub_m", gross_column]].rename(columns={gross_column: "gross_cf"})
    net["wake_eff"] = [modelled.get(s, default) for s in net.index]
    net["wake"] = ["OSM layout" if s in modelled.index else "assumed (mean of modelled farms)" for s in net.index]
    net["net_cf"] = net_capacity_factor(net.gross_cf, net.wake_eff, availability, electrical)
    net["MW"] = mw
    by_project = net.groupby("project", sort=False).apply(lambda g: pd.Series({
        "MW": g.MW.sum(), "turbine": g.turbine.iloc[0], "gross_cf": np.average(g.gross_cf, weights=g.MW),
        "wake_eff": np.average(g.wake_eff, weights=g.MW), "net_cf": np.average(g.net_cf, weights=g.MW),
        "wake": g.wake.iloc[0]}), include_groups=False)
    by_project["first power"] = by_project.index.map(national.set_index("farm").first_power_or_completion_year)
    return by_project, default


def capacity_weighted(projects, column="net_cf", exclude=("Baltic West",)):
    sel = projects.drop(index=[p for p in exclude if p in projects.index])
    return float(np.average(sel[column].astype(float), weights=sel.MW.astype(float)))


def contracted_cf_grid(assignment, hist, curves, specs, wakes, national, default_wake,
                       availability=0.95, electrical=0.98, exclude=("Baltic West",)):
    """Net CF of the contracted pipeline for every combination of wind dataset and power-curve choice."""
    choices = {"turbine: datasheet": "low", "turbine: midpoint": "mid", "turbine: rotor physics": "high",
               "IEA 15 MW": "IEA-15-240-RWT", "generic": "generic (extension 1)"}
    sel = assignment[~assignment.project.isin(exclude)]
    weights = [national.set_index("farm").capacity_mw[a.project] * a.share_of_project for _, a in sel.iterrows()]
    grid = {}
    for label, choice in choices.items():
        col = {}
        for source in ["icon_eu", "dmi_harmonie", "era5"]:
            cfs = []
            for _, a in sel.iterrows():
                if choice in ("low", "mid", "high"):
                    model, curve_set = a.turbine_model, choice
                else:
                    model, curve_set = choice, "mid"
                rated = specs.rated_kw.get(model, 15000)
                height = a.hub_m if source != "era5" else 100
                g = gross_capacity_factor(counts_at(hist, a.wind_site, source, height), curves[curve_set][model][0], rated)
                cfs.append(net_capacity_factor(g, wakes["in the cluster"].get(a.wind_site, default_wake), availability, electrical))
            col[f"{source} {'hub' if source != 'era5' else '100 m'}"] = np.average(cfs, weights=weights)
        grid[label] = col
    return pd.DataFrame(grid)


def ses_wind_value(P, cf, price, harvest_rule, investment, start_year=2025):
    """Run the SES model with wind revenue from capacity factor ``cf``; returns (p_e, present values)."""
    from ses_model import simulate, present_values
    Pc = {**P, "pe": price * 8760 * cf * 1000 / 1e6}
    return Pc["pe"], present_values(simulate(Pc, harvest_rule, investment, start_year=start_year), Pc, terminal=True)


def plot_power_curves(curves, specs, speeds=None):
    """Three panels: power curves with their bands, implied power coefficient, thrust coefficient."""
    import matplotlib.pyplot as plt
    from viz import curve_bands
    v = np.linspace(0, 34, 341) if speeds is None else speeds
    fig, ax = plt.subplots(1, 3, figsize=(14, 3.8))
    curve_bands(v, {m: (curves["low"][m][0](v) / 1000, curves["mid"][m][0](v) / 1000, curves["high"][m][0](v) / 1000)
                    for m in specs.index} | {"generic (extension 1)": (None, curves["mid"]["generic (extension 1)"][0](v) / 1000, None)},
                ax=ax[0], title="Power curves (band: datasheet → rotor physics)", xlabel="wind speed (m/s)", ylabel="power (MW)")
    w = v[(v >= 3) & (v <= 15)]
    for m in specs.index:
        line, = ax[1].plot(w, implied_cp(curves["high"][m][0], specs.loc[m, "swept_area_m2"], w), label=m)
        ax[1].plot(w, implied_cp(curves["low"][m][0], specs.loc[m, "swept_area_m2"], w), ls="--", color=line.get_color())
        ax[2].plot(v, curves["mid"][m][1](v), color=line.get_color())
    ax[1].axhline(16 / 27, color="k", ls="--", lw=.8); ax[1].text(4, .6, "Betz limit 0.593", fontsize=8)
    ax[1].set(xlabel="wind speed (m/s)", ylabel="Cp", title="Implied Cp: dashed datasheet, solid rotor", ylim=(0, .65))
    ax[2].set(xlabel="wind speed (m/s)", ylabel="Ct", title="Thrust coefficient (drives the wakes)")
    fig.tight_layout()
    return fig
