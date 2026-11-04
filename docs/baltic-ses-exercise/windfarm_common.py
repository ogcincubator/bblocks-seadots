"""Wind farms and turbines for the production extension, in the harmonised data model.

The production extension does not read raw wind-farm sources. It reads GeoJSON FeatureCollections of
the common building blocks, already transformed:

* ``common-windfarm-designated-area``: one feature per source record (a project, farm or area), with
  source and location provenance;
* ``common-windfarm-turbine``: one Point feature per turbine.

Each collection is produced from a raw snapshot by the source block's own transform, declared in its
``transforms.yaml`` and driven by the alignment in its ``ontology.ttl``:

==============  ===========================================  ====================================================
key             source block / transform                     common collection (data/)
==============  ===========================================  ====================================================
national        crowdsourced-designated-area-pl              polish_offshore_wind_pipeline_windfarm_areas.geojson
emodnet         windfarm-designated-area-emodnet (points)    emodnet_windfarms_PL_windfarm_areas.geojson
emodnet-zones   windfarm-designated-area-emodnet (polygons)  emodnet_windfarmspoly_PL_windfarm_areas.geojson
osm             windfarm-openstreetmap (areas)               osm_polish_offshore_wind_windfarm_areas.geojson
osm-turbines    windfarm-openstreetmap (turbines)            osm_polish_offshore_wind_turbines.geojson
==============  ===========================================  ====================================================

``build()`` re-runs the transforms on the raw snapshots and rewrites the files; ``areas()``,
``turbines()`` and ``projects()`` load the stored collections as GeoDataFrames.
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

EXERCISE = Path(__file__).resolve().parent                      # docs/baltic-ses-exercise
REPO = EXERCISE.parents[1]                                      # bblocks-seadots
BLOCKS = REPO / "_sources" / "windfarms"
DATA = EXERCISE / "data"
OSM_SNAPSHOT = BLOCKS / "windfarm-openstreetmap" / "examples" / "osm-polish-offshore-wind-2026-10-27.json"

SOURCES = {
    "national": {"block": "crowdsourced-designated-area-pl", "transform": "to-windfarm-designated-area",
                 "input": DATA / "polish_offshore_wind_pipeline.csv",
                 "output": DATA / "polish_offshore_wind_pipeline_windfarm_areas.geojson"},
    "emodnet": {"block": "windfarm-designated-area-emodnet", "transform": "to-windfarm-designated-area",
                "input": DATA / "emodnet_windfarms_PL_wfs_2026-10-30.geojson",
                "output": DATA / "emodnet_windfarms_PL_windfarm_areas.geojson"},
    "emodnet-zones": {"block": "windfarm-designated-area-emodnet", "transform": "to-windfarm-designated-area",
                      "input": DATA / "emodnet_windfarmspoly_PL_wfs_2026-10-30.geojson",
                      "output": DATA / "emodnet_windfarmspoly_PL_windfarm_areas.geojson"},
    "osm": {"block": "windfarm-openstreetmap", "transform": "to-windfarm-designated-area",
            "input": OSM_SNAPSHOT, "output": DATA / "osm_polish_offshore_wind_windfarm_areas.geojson"},
    "osm-turbines": {"block": "windfarm-openstreetmap", "transform": "to-windfarm-turbine",
                     "input": OSM_SNAPSHOT, "output": DATA / "osm_polish_offshore_wind_turbines.geojson"},
}


# ------------------------------------------------------------------ block transforms
def run_transform(block, transform_id, input_data, **metadata):
    """Run a transform declared in a block's transforms.yaml the way the OGC Building Blocks tooling does:
    the script gets ``input_data`` and ``metadata`` (repository paths resolved) and assigns ``output_data``."""
    spec = yaml.safe_load((BLOCKS / block / "transforms.yaml").read_text(encoding="utf-8"))
    t = next(t for t in spec["transforms"] if t["id"] == transform_id)
    meta = {k: (str(REPO / v) if isinstance(v, str) and (REPO / v).exists() else v)
            for k, v in (t.get("metadata") or {}).items()}
    script = BLOCKS / block / t["ref"]
    scope = {"input_data": input_data, "metadata": {**meta, **metadata}, "__file__": str(script)}
    exec(compile(script.read_text(encoding="utf-8"), str(script), "exec"), scope)
    out = scope["output_data"]
    return json.loads(out) if isinstance(out, str) else out


def build(keys=None):
    """Re-run the block transforms on the raw snapshots and write the common collections to data/."""
    out = {}
    for key in keys or SOURCES:
        s = SOURCES[key]
        out[key] = run_transform(s["block"], s["transform"], s["input"].read_text(encoding="utf-8"))
        s["output"].write_text(json.dumps(out[key], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return out


# ------------------------------------------------------------------ loading
def collection(key):
    """The stored common FeatureCollection of one source (dict)."""
    return json.loads(SOURCES[key]["output"].read_text(encoding="utf-8"))


def _gdf(fc, list_columns=()):
    import viz
    gdf = viz.to_gdf(fc)
    for col in list_columns:                                     # viz.to_gdf writes lists as JSON text
        if col in gdf:
            gdf[col] = [f["properties"].get(col) for f in fc["features"]]
    return gdf


AREA_SOURCES = ("national", "emodnet", "emodnet-zones", "osm")


def areas(*keys):
    """Wind farm areas of one or more sources (default: all) as one GeoDataFrame in the common model.

    Every source is read the same way, because every collection is in the same block; a ``source``
    column names the collection each row comes from."""
    import geopandas as gpd
    import pandas as pd
    frames = [_gdf(collection(k), ("same_as", "operator", "admin_units")).assign(source=k) for k in keys or AREA_SOURCES]
    return gpd.GeoDataFrame(pd.concat(frames, ignore_index=True), geometry="geometry", crs=frames[0].crs)


def turbines():
    """OSM turbines in the common model (common-windfarm-turbine) as a GeoDataFrame."""
    return _gdf(collection("osm-turbines"), ("operator",))


def projects():
    """The national project list (the investment pipeline) in the common model, indexed by project name."""
    return areas("national").set_index("name", drop=False).rename_axis(None)


def with_turbines(farm_areas, turbine_points, predicate="intersects"):
    """Farm areas that contain (intersect) at least one turbine, with the number of turbines found.

    Both inputs are GeoDataFrames in the common model (``areas()``, ``turbines()``). A geopandas spatial
    join decides; areas without geometry are left out. Point records (EMODnet farm points, located national
    projects) intersect a turbine only if they lie exactly on one, so in practice the result holds the
    polygon sources (OSM farm areas, EMODnet zones)."""
    located = farm_areas[farm_areas.geometry.notna() & ~farm_areas.geometry.is_empty]
    hits = located.sjoin(turbine_points[[turbine_points.geometry.name]], predicate=predicate, how="inner")
    counts = hits.groupby(level=0).size()
    return located.loc[counts.index].assign(turbines_inside=counts.values)
