## ECMWF's ERA5 data documentation - Wave spectra

The ocean wave model used in ERA5 (WAM, which is included in the IFS) provides wave spectra with 24 directions and 30 frequencies (see "2D wave spectra (single)", Table 7). To decode the 2D wave spectra:

### Download from ERA5

ERA5 wave spectra data is not available from the CDS disks. However, it is available in MARS and can be accessed through the CDS API. For more information see ![Data organisation and how to download ERA5](https://confluence.ecmwf.int/display/CKB/ERA5%3A+data+documentation#ERA5:datadocumentation-DataorganisationandhowtodownloadERA5) and ![How to download ERA5](https://confluence.ecmwf.int/display/CKB/How+to+download+ERA5) (![Option B: Download ERA5 family data that is NOT listed in the CDS online catalogue - SLOW ACCESS](https://confluence.ecmwf.int/display/CKB/How+to+download+ERA5#HowtodownloadERA5-OptionB:DownloadERA5familydatathatisNOTlistedintheCDSonlinecatalogue-SLOWACCESS)).


### Decoding 2D wave spectra in GRIB

To decode wave spectra in GRIB format we recommend ![ecCodes](https://confluence.ecmwf.int/display/ECC/ecCodes+Home). Wave spectra are encoded in a specific way that other tools might not decode correctly.

In GRIB, the parameter is called 2d wave spectra (single) because in GRIB, the data are stored as a single global field per each spectral bin (a given frequency and direction), but in NetCDF, the fields are nicely recombined to produce a 2d matrix representing the discretized spectra at each grid point.

The wave spectra are encoded in GRIB using a local table specific to ECMWF. Because of this, the conversion of the meta data containing the information about the frequencies and the directions are not properly converted from GRIB to NetCDF format. So rather than having the actual values of the frequencies and directions, values show index numbers (1,1) : first frequency, first direction, (1,2) first frequency, second direction, etc ....

For ERA, because there are a total of 24 directions, the direction increment is 15 degrees with the first direction given by half the increment, namely 7.5 degree, where direction 0. means going towards the north and 90 towards the east (Oceanographic convention), or more precisely, this should be expressed in gradient since the spectra are in m^2 /(Hz radian)
The first frequency is 0.03453 Hz and the following ones are : f(n) = f(n-1)×1.1, n=2,30

Also note that it is NOT the spectral density that is encoded but rather log10 of it, so to recover the spectral density, expressed in m^2 /(radian Hz), one has to take the power 10 (10^) of the NON missing decoded values. Missing data are for all land points, but also, as part of the GRIB compression, all small values below a certain threshold have been discarded and so those missing spectral values are essentially 0. m^2 /(gradient Hz).


### Decoding 2D wave spectra in NetCDF

The NetCDF wave spectra file will have the dimensions longitude, latitude, direction, frequency and time.

However, the direction and frequency bins are simply given as 1 to 24 and 1 to 30, respectively.

The direction bins start at 7.5 degree and increase by 15 degrees until 352.5, with 90 degree being towards the east (Oceanographic convention).

The frequency bins are non-linearly spaced. The first bin is 0.03453 Hz and the following bins are: f(n) = f(n-1)×1.1; n=2,30. The data provided is the log10 of spectra density. To obtain the spectral density one has to take to the power 10 (10 ^ data). This will give the units 2D wave spectra as m^2 s radian^-1 . Very small values are discarded and set as missing values. These are essentially 0 m^2 s radian^-1.

This recoding can be done with the Python ![xarray](http://xarray.pydata.org/en/stable/) package, for example:

```python
import xarray as xr
import numpy as np
da = xr.open_dataarray('2d_spectra_201601.nc')
da = da.assign_coords(direction=np.arange(7.5, 352.5 + 15, 15))
da = da.assign_coords(frequency=np.full(30, 0.03453) * (1.1 ** np.arange(0, 30)))
da = 10 ** da
da = da.fillna(0)
da.to_netcdf(path='2d_spectra_201601_recoded.nc')
```

### Units of 2D wave spectra

Once decoded, the units of 2D wave spectra are m<sup>2</sup> s radian<sup>-1</sup>