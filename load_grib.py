import xarray as xr
import numpy as np

da = xr.open_dataarray('integ.grib')
da = da.assign_coords(direction=np.arange(7.5, 352.5 + 15, 15))
da = da.assign_coords(frequency=np.full(30, 0.03453) * (1.1 ** np.arange(0, 30)))
da = 10 ** da
da = da.fillna(0)
da.to_netcdf(path='integ__.nc')