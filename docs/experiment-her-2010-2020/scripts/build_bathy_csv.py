"""Resample the Copernicus BAL bathymetry to a POSEIDON-friendly CSV grid.

Input : data/bathy_subset.nc  (Copernicus BAL static mask & bathymetry, EDITO)
Output: inputs/bathy.csv       (POSEIDON From File Map, header=x,y,depth)

Grid: ~0.07° lon x 0.075° lat -> roughly 7 km cells over the bbox
[16.0, 56.5, 21.5, 60.0]. depth = -bathy (POSEIDON convention: negative = sea
floor below surface, land = positive or NaN).

Provenance: bathy_subset.nc derived from
  https://s3.waw3-1.cloudferro.com/mdl-native-11/native/BALTICSEA_MULTIYEAR_PHY_003_011/cmems_mod_bal_phy_my_static_202303/BAL-MFC_003_011_mask_bathy.nc
  (Copernicus Marine Service product BALTICSEA_MULTIYEAR_PHY_003_011 static).
"""
import csv
import numpy as np
import xarray as xr

BBOX = dict(lon_min=16.0, lon_max=21.5, lat_min=56.5, lat_max=60.0)
DLON = 0.10   # ~6 km at 58N
DLAT = 0.10   # ~11 km
OUT = "/tmp/poseidon-run/experiments/her-2010-2020/inputs/bathy.csv"

ds = xr.open_dataset("/tmp/poseidon-run/experiments/her-2010-2020/data/bathy_subset.nc")
print("Vars:", list(ds.data_vars))
print("Coords:", list(ds.coords))
print("Dims:", dict(ds.sizes))

# detect variable name
bcand = [v for v in ds.data_vars if "deptho" in v.lower() or "bathy" in v.lower() or v.lower()=="h"]
bvar = bcand[0]
print("Using bathy var:", bvar)

# build target grid
lons = np.arange(BBOX["lon_min"], BBOX["lon_max"] + 1e-9, DLON)
lats = np.arange(BBOX["lat_min"], BBOX["lat_max"] + 1e-9, DLAT)
print(f"Target grid: {len(lons)} lon x {len(lats)} lat = {len(lons)*len(lats)} cells")

# nearest-neighbour interpolation onto the target grid
b = ds[bvar]
lat_name = "latitude" if "latitude" in b.coords else "lat"
lon_name = "longitude" if "longitude" in b.coords else "lon"
bi = b.interp({lat_name: ("y", lats), lon_name: ("x", lons)}, method="nearest")

# POSEIDON convention: depth negative for sea, positive/large for land (we use NaN -> 1)
arr = bi.values  # shape (y, x) if order matches
print("Resampled shape:", arr.shape)

n_sea = 0
n_land = 0
rows = []
for j, lat in enumerate(lats):
    for i, lon in enumerate(lons):
        v = arr[j, i] if arr.shape[0] == len(lats) else arr[i, j]
        if np.isnan(v) or v <= 0:
            depth = 1   # land sentinel
            n_land += 1
        else:
            depth = -float(v)
            n_sea += 1
        rows.append((float(lon), float(lat), depth))

with open(OUT, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["x", "y", "depth"])
    for r in rows:
        w.writerow([f"{r[0]:.4f}", f"{r[1]:.4f}", f"{r[2]:.1f}"])

print(f"Wrote {OUT}  (sea cells: {n_sea}, land cells: {n_land})")
print(f"Grid dims for YAML: width={len(lons)} cells, height={len(lats)} cells")
