import xarray as xr
import numpy as np


def grib2nc(filein, fileout):
	""" Convert a GRIB file to a netCDF file.
		Sample code from: ECMWF_guide_ERA5. 
		
		Direction bins: 24. The direction increment is 15 degrees with
		the first direction given by half the increment, namely 7.5 degree, 
		where direction 0. means going towards the north and 90 towards the east 
    	(Oceanographic convention).

		Frequency bins: 30. The first frequency is 0.03453 Hz
		and the following ones are : f(n) = f(n-1)*1.1, n=2,30.

		Values of `da` is log10 of of the spectral density. 
		So to recover the spectral density, expressed in m^2 /(radian Hz), one has to take 
		the power 10 (10^) of the NON missing decoded values. Missing data are for all 
		land points, but also, as part of the GRIB compression, all small values below 
		a certain threshold have been discarded and so those missing spectral values 
		are essentially 0. m^2 /(gradient Hz).
	"""
	da = xr.open_dataset('integ.grib')
	da = da.assign_coords(direction=np.arange(7.5, 352.5 + 15, 15))
	da = da.assign_coords(frequency=np.full(30, 0.03453) * (1.1 ** np.arange(0, 30)))
	da = 10 ** da
	da = da.fillna(0)
	da.to_netcdf(path='integ__.nc')


if __name__ == '__main__':
	grib2nc()