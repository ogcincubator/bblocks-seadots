"""Standard visualisation helpers for the Baltic SES notebooks.

Every function takes standard data: GeoDataFrames, GeoJSON (dict or file), GeoParquet files, or pandas
DataFrames. Maps use geopandas' ``explore`` (folium / Leaflet), which renders interactively in Jupyter;
``plot_layers`` gives the same layers as a static matplotlib figure for exported or printed notebooks.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

WGS84 = "EPSG:4326"


# ------------------------------------------------------------------ data
def to_gdf(data, crs=WGS84, flatten=()):
    """GeoDataFrame from a GeoDataFrame, GeoJSON dict / feature list, or a .geojson/.json/.parquet path.

    ``flatten`` names nested-object properties (e.g. OSM ``tags``) whose keys become columns.
    Nested values (lists, dicts) are turned into JSON strings so that every column can be shown in tooltips.
    Features without geometry are kept with an empty geometry.
    """
    import geopandas as gpd
    if isinstance(data, gpd.GeoDataFrame):
        gdf = data
    elif isinstance(data, (str, Path)) and Path(data).suffix in (".parquet", ".geoparquet"):
        gdf = gpd.read_parquet(data)
    else:
        if isinstance(data, (str, Path)):
            data = json.loads(Path(data).read_text(encoding="utf-8"))
        features = data["features"] if isinstance(data, dict) and "features" in data else list(data)
        rows = [{"id": f.get("id"), **(f.get("properties") or {})} for f in features]
        from shapely.geometry import shape
        geoms = [shape(f["geometry"]) if f.get("geometry") else None for f in features]
        gdf = gpd.GeoDataFrame(rows, geometry=geoms, crs=crs)
    gdf = gdf.copy()
    for col in flatten:
        expanded = pd.json_normalize(gdf[col].map(lambda v: v if isinstance(v, dict) else {}).tolist())
        expanded.index = gdf.index
        gdf = gdf.drop(columns=col).join(expanded, rsuffix=f"_{col}")
    for col in gdf.columns:
        if col != gdf.geometry.name and gdf[col].map(lambda v: isinstance(v, (list, dict))).any():
            gdf[col] = gdf[col].map(lambda v: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v)
    if gdf.crs is None:
        gdf = gdf.set_crs(crs)
    return gdf


def _layer(spec):
    """A layer is data, or a dict {'data': ..., <GeoDataFrame.explore / plot keyword arguments>}."""
    if isinstance(spec, dict) and "data" in spec:
        spec = dict(spec)
        return to_gdf(spec.pop("data")), spec
    return to_gdf(spec), {}


# ------------------------------------------------------------------ maps
def explore(layers, tiles="OpenStreetMap", zoom_start=None, height=480, **map_kwargs):
    """Interactive map: one toggleable layer per entry of ``layers`` ({name: data or {data, style...}}).

    Style keywords are passed to ``GeoDataFrame.explore`` (``color``, ``column``, ``cmap``, ``tooltip``,
    ``marker_kwds``, ``style_kwds``, ``legend``...). Features without geometry are skipped on the map.
    """
    import folium
    m = None
    for name, spec in layers.items():
        gdf, style = _layer(spec)
        gdf = gdf[~gdf.geometry.is_empty & gdf.geometry.notna()]
        if gdf.empty:
            continue
        style = {"tooltip": [c for c in gdf.columns if c != gdf.geometry.name][:8], **style}
        if m is None:
            m = gdf.explore(name=name, tiles=tiles, height=height, **style, **map_kwargs)
        else:
            gdf.explore(m=m, name=name, **style)
    if m is not None:
        folium.LayerControl(collapsed=False).add_to(m)
        if zoom_start:
            m.options["zoom"] = zoom_start
    return m


def plot_layers(layers, ax=None, title=None, figsize=(10, 5), legend=True):
    """Static version of ``explore``: the same layer specification drawn with ``GeoDataFrame.plot``."""
    import matplotlib.pyplot as plt
    if ax is None:
        _, ax = plt.subplots(figsize=figsize)
    for name, spec in layers.items():
        gdf, style = _layer(spec)
        gdf = gdf[~gdf.geometry.is_empty & gdf.geometry.notna()]
        if gdf.empty:
            continue
        plot_style = {k: v for k, v in style.items() if k in ("color", "column", "cmap", "markersize", "alpha",
                                                                  "edgecolor", "facecolor", "linewidth", "marker",
                                                                  "vmin", "vmax", "legend")}
        gdf.plot(ax=ax, label=name, **plot_style)
    ax.set_aspect(1 / np.cos(np.radians(55)))
    if title:
        ax.set_title(title, fontsize=10)
    if legend:
        ax.legend(fontsize=7, loc="upper left")
    return ax


# ------------------------------------------------------------------ charts
def heatmap_table(df, fmt="{:.3f}", title=None, ax=None, cmap="YlGnBu"):
    """Annotated heat map of a numeric DataFrame (rows x columns), text colour adapted to the cell."""
    import matplotlib.pyplot as plt
    if ax is None:
        _, ax = plt.subplots(figsize=(1.6 * df.shape[1] + 2, 0.55 * df.shape[0] + 1))
    values = df.to_numpy(dtype=float)
    ax.imshow(values, cmap=cmap, aspect="auto")
    ax.grid(False)
    ax.set_xticks(range(df.shape[1]), [str(c).replace(": ", ":\n") for c in df.columns], fontsize=8)
    ax.set_yticks(range(df.shape[0]), df.index, fontsize=8)
    span = np.ptp(values) or 1
    for (i, j), v in np.ndenumerate(values):
        ax.text(j, i, fmt.format(v), ha="center", va="center", fontsize=8.5,
                color="white" if (v - values.min()) / span > .6 else "black")
    if title:
        ax.set_title(title, fontsize=10)
    return ax


def profile_plot(profile, ax=None, title=None, xlabel="mean wind speed (m/s)", ylabel="height above sea (m)"):
    """Vertical profiles: ``profile`` has a height index and one column per line (NaN where not available)."""
    import matplotlib.pyplot as plt
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 4))
    for name, col in profile.items():
        col = col.dropna()
        ax.plot(col.values, col.index, marker="o", label=name)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    ax.legend(fontsize=7)
    if title:
        ax.set_title(title, fontsize=10)
    return ax


def curve_bands(x, curves, ax=None, title=None, xlabel=None, ylabel=None):
    """Lines with uncertainty bands: ``curves`` = {name: (low, mid, high)} arrays over ``x`` (low/high may be None)."""
    import matplotlib.pyplot as plt
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 4))
    for name, (low, mid, high) in curves.items():
        line, = ax.plot(x, mid, label=name)
        if low is not None and high is not None:
            ax.fill_between(x, low, high, color=line.get_color(), alpha=.18, lw=0)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    ax.legend(fontsize=7)
    if title:
        ax.set_title(title, fontsize=10)
    return ax


def wind_rose(sector_shares, ax=None, title=None):
    """Polar bars: ``sector_shares`` = DataFrame indexed by sector centre (degrees), one column per series."""
    import matplotlib.pyplot as plt
    if ax is None:
        _, ax = plt.subplots(subplot_kw={"projection": "polar"}, figsize=(4.5, 4.5))
    width = np.radians(360 / len(sector_shares))
    for k, (name, col) in enumerate(sector_shares.items()):
        ax.bar(np.radians(sector_shares.index.to_numpy(float)), col.values, width=width * (0.85 - 0.4 * k),
               label=name, alpha=.85)
    ax.set_theta_zero_location("N"); ax.set_theta_direction(-1)
    ax.legend(fontsize=7, loc="lower left", bbox_to_anchor=(-.2, -.2))
    if title:
        ax.set_title(title, fontsize=10)
    return ax
