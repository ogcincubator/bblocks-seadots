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
