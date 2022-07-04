import numpy as np
import xarray as xr
import matplotlib.pyplot as plt 
from mpl_toolkits.basemap import Basemap



def read_file(file_name):
    """ Reads data from a GRIB or netCDF file.
    """
    if file_name.endswith('grib'):
        ds = xr.open_dataset(file_name, engine='cfgrib')
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
    global array_data
    array_data = ds.swh[0]
    print('Shape of data array: ', array_data.shape)
    plt.connect('motion_notify_event', mouse_move)
    polar_plot()
    plt.show()


def read_spec_grib(file_name):
    """ Read the spectral data from a GRIB file.
    """
    ds = read_file(file_name)
    layer_init = ds.d2fd[0]


def mouse_move(event):
    x, y = event.xdata, event.ydata
    global array_data
    if x is not None and y is not None:
        lon = int(x)
        lat = int(y)
        Hs = array_data[lon][lat].values
        if not np.isnan(Hs):
            print('Hs = {:.3} m'.format(Hs))


def polar_plot():
    """ Plot the wave spectrum based on the data obtained from `read_spec`."""
    # Failed without pygrib
    ds = read_file('spect.grib')  # (3GB), downloaded using the third chunk in `download_spectra.py`
    # find a way to extract data
    ds.d2fd[0]
    print(len(ds.d2fd[0]))  # --> 24


if __name__ == '__main__':
    ds = read_file('integ.nc')      # 'integ.grib' 'integ.nc'
    plot_integ(ds)
