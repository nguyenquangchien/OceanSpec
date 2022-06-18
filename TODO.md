## Features

### Major
* Load the `grib` spectra file and spectral matrices of all grid points for the current time layer.

### Minor
* Shift the map so that the prime meridian is in the centre.
* Snap the cursors to the grid and make it slower
* Draw also the spectrum (with transparency) of the previously visited grid point, so that we can compare to the present sprectrum.

## Bugs

* Module `download_data`: Only the last option (`grib`) works. But we prefer netCDF format and try following a code sample to download the netCDF file and save as `ISSM_Trial_ERA5_Data_NEW.nc`. This causes a run-time error. 
Part of the error is as follows
```
2022-06-16 11:33:50,491 ERROR   home.cds.cdsservices.services.mars.__init__.py.exceptions.MarsException: Expected 172800, got 57600.; Request failed; Some errors reported (last error -1)
Traceback (most recent call last):
  File "e:\Progs\Github-repos\OceanSpec\code\download_spectra.py", line 11, in <module>
    c.retrieve(
  File "D:\Anaconda3\lib\site-packages\cdsapi\api.py", line 348, in retrieve
    result = self._api("%s/resources/%s" % (self.url, name), request, "POST")
  File "D:\Anaconda3\lib\site-packages\cdsapi\api.py", line 506, in _api
    raise Exception(
Exception: the request you have submitted is not valid. Expected 172800, got 57600.; Request failed; Some errors reported (last error -1).
```

* (This is more platform-specific) Cannot read `spect.grib` as `pip install` failed on Windows 10. The following error message appears:
```
File "e:\Progs\Github-repos\OceanSpec\code\read_data.py", line 83, in <module>
    ds = read_file('spect.grib')
  File "e:\Progs\Github-repos\OceanSpec\code\read_data.py", line 16, in read_file
    ds = xr.open_dataset(file_name, engine='cfgrib')
  File "D:\Anaconda3\lib\site-packages\xarray\backends\api.py", line 481, in open_dataset
    backend = plugins.get_backend(engine)
  File "D:\Anaconda3\lib\site-packages\xarray\backends\plugins.py", line 156, in get_backend      
    raise ValueError(
ValueError: unrecognized engine cfgrib must be one of: ['netcdf4', 'scipy', 'store']
```