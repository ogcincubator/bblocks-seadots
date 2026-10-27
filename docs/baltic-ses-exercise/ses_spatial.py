"""Pure spatial model calculations used by baltic_ses_spatial_extension.ipynb.

The notebook owns API/file access and chooses inputs/assumptions; these helpers
turn loaded observations into site metrics and model parameters.
"""
import numpy as np
import pandas as pd
from matplotlib.path import Path as MplPath


def hist_from_speeds(speeds):
    """Convert hourly wind speeds to integer-m/s bins, mean speed and sample count."""
    values = np.asarray([speed for speed in speeds if speed is not None], float)
    return np.bincount(np.minimum(values.astype(int), 30), minlength=31), values.mean(), len(values)


def power_curve(speed, cut_in=3.0, rated=10.6, cut_out=25.0):
    """Generic normalized turbine power curve for speeds in m/s."""
    speed = np.asarray(speed)
    return np.where(speed < cut_in, 0, np.where(speed < rated,
        (speed**3 - cut_in**3) / (rated**3 - cut_in**3), np.where(speed <= cut_out, 1, 0)))


def capacity_factor(histogram, cut_in=3.0, rated=10.6, cut_out=25.0, losses=0.15):
    """Estimate net capacity factor from a 31-bin hourly wind-speed histogram."""
    bin_centres = np.arange(31) + 0.5
    return (histogram * power_curve(bin_centres, cut_in, rated, cut_out)).sum() / histogram.sum() * (1 - losses)


def _to_km(lon, lat, lon0=17.0, lat0=55.0):
    return np.c_[(np.asarray(lon) - lon0) * 111.32 * np.cos(np.radians(lat0)),
                 (np.asarray(lat) - lat0) * 110.57]


def _distance_to_ring(lon, lat, ring):
    ring_xy = _to_km(*np.asarray(ring).T)
    point = _to_km(lon, lat)[0]
    if MplPath(ring_xy).contains_point(point):
        return 0.0
    starts, ends = ring_xy[:-1], ring_xy[1:]
    segments = ends - starts
    fraction = np.clip(((point - starts) * segments).sum(1) / np.maximum((segments * segments).sum(1), 1e-12), 0, 1)
    return np.hypot(*(starts + fraction[:, None] * segments - point).T).min()


def _nearest_protected_area(lon, lat, natura2000):
    return min(((_distance_to_ring(lon, lat, polygon[0]), feature["properties"]["sitename"])
                for feature in natura2000["features"] for polygon in feature["geometry"]["coordinates"]),
               key=lambda item: item[0])


def _nearby_obis_records(lon, lat, cells, radius=0.25):
    longitudes = cells.index.get_level_values(0)
    latitudes = cells.index.get_level_values(1)
    nearby = cells[(abs(longitudes - lon) <= radius + 1e-6) & (abs(latitudes - lat) <= radius + 1e-6)]
    return int(nearby.sum())


def add_site_sensitivity(farms, natura2000, obis, protected_weight=0.6, decay_km=10.0):
    """Return farms augmented with nearest protected area, nearby OBIS counts and sensitivity."""
    result = farms.copy()
    nearest = [_nearest_protected_area(lon, lat, natura2000) for lon, lat in zip(result.lon, result.lat)]
    result["d_n2k_km"] = [float(distance) for distance, _ in nearest]
    result["nearest_n2k"] = [name for _, name in nearest]
    cells = obis.groupby(["lon", "lat"]).n_records.sum()
    result["obis_records"] = [_nearby_obis_records(lon, lat, cells) for lon, lat in zip(result.lon, result.lat)]
    log_records = np.log1p(result.obis_records)
    result["S"] = protected_weight * np.exp(-result.d_n2k_km / decay_km) + (1 - protected_weight) * log_records / log_records.max()
    return result


def spatial_portfolio_parameters(P, price_eur_mwh, capacity_factor, capex_factor, sensitivity, reference_sensitivity):
    """Replace wind revenue, investment cost and public sensitivity parameters for a portfolio."""
    return {**P,
            "pe": price_eur_mwh * 8760 * capacity_factor * 1000 / 1e6,
            "Iwp": P["Iwp"] * capex_factor,
            "pu3": P["pu3"] * sensitivity / reference_sensitivity}


def greedy_portfolio(scores, site_capacity_mw, target_mw):
    """Fill sites in descending score order up to target MW; partially use the last site."""
    allocation = pd.Series(0.0, index=site_capacity_mw.index)
    for index in scores.sort_values(ascending=False).index:
        allocation[index] = min(site_capacity_mw.loc[index], target_mw - allocation.sum())
        if allocation.sum() >= target_mw - 1e-6:
            break
    return allocation


def coastal_capex_factor(distance_km, premium_per_km=0.004, base_distance_km=30.0):
    """Assumed multiplicative capex adjustment by distance from the coast."""
    return 1 + premium_per_km * (np.asarray(distance_km) - base_distance_km)
