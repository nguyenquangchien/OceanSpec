import magpye
# import cmocean
import numpy as np
import xarray as xr
# import cartopy.crs as ccrs
# import ecmwf.data as ecdata
import matplotlib.pyplot as plt 
# from wavespectra import read_era5
from mpl_toolkits.basemap import Basemap


def read_file(file_name):
    """ Reads data from a GRIB or netCDF file.
    """
    if file_name.endswith('grib'):
        ds = xr.open_dataset(file_name, engine='cfgrib')
        # ds = cfgrib.open_dataset(file_name)
    else:
        ds = xr.open_dataset(file_name)
    return ds


def plot_integ(ds):
    """ Plot a map of the integrated wave properties.
    """
    map = Basemap(projection='cyl',lon_0=180,lat_0=0,
                  resolution='c', area_thresh = 50, 
                  llcrnrlon=0, llcrnrlat=-89, urcrnrlon=360, urcrnrlat=89)
    map.drawcoastlines(linewidth=0.25)
    map.drawmeridians(np.arange(0, 361, 30))
    map.drawparallels(np.arange(-90, 91, 30))
    ds.swh[0].plot(cmap=plt.cm.coolwarm)
    # ds.swh[0].plot(projection=ccrs.UTM(), cmap=plt.cm.coolwarm)
    plt.connect('motion_notify_event', mouse_move)
    polar_plot()
    # plt.savefig('Hs_map.png')
    plt.show()


def plot_magpye(file_name):
    geomap = magpye.Geomap()    # AttributeError: module 'magpye' has no attribute 'Geomap'


# def read_ecdata(file_name):
#     """ Read the data using ECMWF API.
#     """
#     data = ecdata.read(file_name)
#     return data.describe()


def read_spec_grib(file_name):
    """ Read the spectral data from a GRIB file.
    """
    # dset = read_era5("_static/era5file.nc").isel(time=0) # only applicable for netCDF files
    ds = read_file(file_name)
    layer_init = ds.d2fd[0]


def mouse_move(event):
    x, y = event.xdata, event.ydata
    print(x, y)


def polar_plot():
    """ Plot the wave spectrum based on the data obtained from `read_spec`."""
    # Failed without pygrib
    # ds = read_file('spect.grib')  # (3GB), downloaded using the third chunk in `download_spectra.py`
    # ds.d2fd[0]
    # print(len(ds.d2fd[0]))


if __name__ == '__main__':
    # plot_magpye('integ.grib')
    ds = read_file('integ.nc')      # 'integ.grib' 'integ.nc'
    plot_integ(ds)
    print(f'Max wave height: {np.max(ds.swh[0][0]):5.2}')
    # plot_magpye('integ.grib')

    # Failed without pygrib
    # ds = read_file('spect.grib')
    # ds.d2fd[0]
    # print(ds.d2fd[0])

