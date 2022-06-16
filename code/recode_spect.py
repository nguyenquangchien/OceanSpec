import xarray as xr
import numpy as np


def recode(filename):
	""" Recode the file (netCDF) with amplitude replaced by 10^amp
		and NA replaced by 0.
		Write output to a new netCDF file (`recoded_*`).
	"""
	da = xr.open_dataarray(filename)
	da = da.assign_coords(direction=np.arange(7.5, 352.5 + 15, 15))
	da = da.assign_coords(frequency=np.full(30, 0.03453) * (1.1 ** np.arange(0, 30)))
	da = 10 ** da
	da = da.fillna(0)
	da.to_netcdf(path=f'recoded_{filename}')


if __name__ == '__main__':
	recode('spect.grib')
