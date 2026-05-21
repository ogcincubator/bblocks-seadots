"""Pull Copernicus BAL bathymetry (native NetCDF) and monthly SST (ARCO Zarr)
for 2010-2020, subset to the north-of-Gotland bbox, persist locally.

Source: EDITO Data Lake STAC catalogue, public CloudFerro endpoints.
"""
import os
import sys
import urllib.request

import xarray as xr

BBOX = dict(lon_min=16.0, lon_max=21.5, lat_min=56.5, lat_max=60.0)
OUT = "/tmp/poseidon-run/experiments/her-2010-2020/data"

BATHY_NC_URL = "https://s3.waw3-1.cloudferro.com/mdl-native-11/native/BALTICSEA_MULTIYEAR_PHY_003_011/cmems_mod_bal_phy_my_static_202303/BAL-MFC_003_011_mask_bathy.nc"
SST_ZARR = "https://s3.waw3-1.cloudferro.com/mdl-arco-time-002/arco/BALTICSEA_MULTIYEAR_PHY_003_011/cmems_mod_bal_phy_my_P1M-m_202303/timeChunked.zarr"

os.makedirs(OUT, exist_ok=True)

bathy_local = f"{OUT}/baltic_bathy_full.nc"
if not os.path.exists(bathy_local):
    print(f"Downloading bathymetry NetCDF ({BATHY_NC_URL}) ...", flush=True)
    urllib.request.urlretrieve(BATHY_NC_URL, bathy_local)
print("Bathy file size MB:", os.path.getsize(bathy_local) / 1e6)

print("Opening bathymetry ...", flush=True)
b = xr.open_dataset(bathy_local)
print("Bathy variables:", list(b.data_vars))
print("Bathy coords:", list(b.coords))
print("Bathy dims:", dict(b.sizes))

lat_name = "latitude" if "latitude" in b.coords else ("lat" if "lat" in b.coords else "y")
lon_name = "longitude" if "longitude" in b.coords else ("lon" if "lon" in b.coords else "x")
print(f"Using coords: {lat_name}, {lon_name}")

# determine lat order to slice correctly
lat_vals = b[lat_name].values
lat_ascending = lat_vals[0] < lat_vals[-1]
lat_slice = slice(BBOX["lat_min"], BBOX["lat_max"]) if lat_ascending else slice(BBOX["lat_max"], BBOX["lat_min"])

b_sub = b.sel({lat_name: lat_slice, lon_name: slice(BBOX["lon_min"], BBOX["lon_max"])})
print("Bathy subset shape:", dict(b_sub.sizes))
b_sub.to_netcdf(f"{OUT}/bathy_subset.nc")
print(f"Wrote {OUT}/bathy_subset.nc")

print("\nOpening monthly physics Zarr (timeChunked) ...", flush=True)
s = xr.open_zarr(SST_ZARR, consolidated=True, zarr_format=2)
print("SST variables:", list(s.data_vars))
print("SST coords:", list(s.coords))
print("SST dims:", dict(s.sizes))

lat_name = "latitude" if "latitude" in s.coords else "lat"
lon_name = "longitude" if "longitude" in s.coords else "lon"

tcandidates = [v for v in s.data_vars if v.lower() in ("sst","thetao","tos","sea_surface_temperature","bottomt","sob")]
print("SST candidates:", tcandidates)
# prefer thetao (potential temp) at surface, or sst directly
tvar = "thetao" if "thetao" in s.data_vars else tcandidates[0]

lat_vals = s[lat_name].values
lat_ascending = lat_vals[0] < lat_vals[-1]
lat_slice = slice(BBOX["lat_min"], BBOX["lat_max"]) if lat_ascending else slice(BBOX["lat_max"], BBOX["lat_min"])

s_sub = s[[tvar]].sel({
    lat_name: lat_slice,
    lon_name: slice(BBOX["lon_min"], BBOX["lon_max"]),
    "time": slice("2010-01-01", "2020-12-31"),
})
for d in ("depth", "elevation"):
    if d in s_sub.dims:
        s_sub = s_sub.isel({d: 0})
print("SST subset dims:", dict(s_sub.sizes))
print("Loading SST subset into memory ...", flush=True)
s_sub.load().to_netcdf(f"{OUT}/sst_2010_2020.nc")
print(f"Wrote {OUT}/sst_2010_2020.nc ({tvar})")
