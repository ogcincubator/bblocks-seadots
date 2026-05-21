"""Pull NOAA OISST v2.1 highres monthly SST 2010-2020 over the
north-of-Gotland bbox via OPeNDAP, compute annual mean and anomaly.

NOAA OISST is used as a Copernicus BAL SST proxy because the Copernicus ARCO
Zarr chunks are auth-gated; OISST is on PSL THREDDS, open, no credentials.
0.25 degree resolution daily; monthly mean here.
"""
import os
import numpy as np
import xarray as xr

OUT = "/tmp/poseidon-run/experiments/her-2010-2020/data"
URL = "https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.mon.mean.nc"

# bbox uses lon 0..360 in OISST
BBOX = dict(lat_min=56.5, lat_max=60.0, lon_min=16.0, lon_max=21.5)

print("Opening OISST monthly via OPeNDAP ...", flush=True)
ds = xr.open_dataset(URL, engine="netcdf4", decode_times=True)
sst = ds["sst"].sel(
    time=slice("2010-01-01", "2020-12-31"),
    lat=slice(BBOX["lat_min"], BBOX["lat_max"]),
    lon=slice(BBOX["lon_min"], BBOX["lon_max"]),
)
print("Subset dims:", dict(sst.sizes))
sst = sst.load()

annual = sst.groupby("time.year").mean("time")
# climatology = mean over 2010-2020 baseline
clim = annual.mean("year")
anom = annual - clim
print("Annual SST (°C) and anomaly per year (area mean):")
for y in annual.year.values:
    am = float(annual.sel(year=int(y)).mean(["lat","lon"]).values)
    an = float(anom.sel(year=int(y)).mean(["lat","lon"]).values)
    print(f"  {int(y)}: mean={am:.3f}  anom={an:+.3f}")

annual.to_netcdf(f"{OUT}/sst_annual_2010_2020.nc")
anom.to_netcdf(f"{OUT}/sst_anom_2010_2020.nc")
print(f"\nWrote {OUT}/sst_annual_2010_2020.nc and sst_anom_2010_2020.nc")
