import xarray as xr


def read_data(file_name):
    """
    Reads data from a GRIB file.
    """
    ds = xr.open_dataset(file_name, engine='cfgrib')
    return ds


if __name__ == '__main__':
    ds = read_data('download.grib')
    print(ds)
