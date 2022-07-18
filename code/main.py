import random
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


def plot_integ(integ, spect):
    """ Plot a map of the integrated wave properties.
    """
    map = Basemap(projection='cyl',lon_0=180,lat_0=0,
                  resolution='c', area_thresh = 50, 
                  llcrnrlon=0, llcrnrlat=-89, urcrnrlon=360, urcrnrlat=89)
    map.drawcoastlines(linewidth=0.25)
    map.drawmeridians(np.arange(0, 361, 30))
    map.drawparallels(np.arange(-90, 91, 30))
    integ.swh[0].plot(cmap=plt.cm.coolwarm)
    global Hs_array
    Hs_array = integ.swh[0]
    print('Shape of data array: ', Hs_array.shape)
    plt.connect('motion_notify_event', mouse_move)
    polar_plot(spect)
    plt.show()


def read_spec_grib(file_name):
    """ Read the spectral data from a GRIB file.
    """
    ds = read_file(file_name)
    idx = 76543  # temporary point in Pacific Ocean
    lon, lat = ds.longitude[idx].values, ds.latitude[idx].values
    time_idx = random.randint(0, len(ds.time) - 1)
    specmat = np.zeros((len(ds.directionNumber), len(ds.frequencyNumber)))
    for i in range(specmat.shape[0]):
        for j in range(specmat.shape[1]):
            specmat[i, j] = ds.d2fd[time_idx, i, j, idx].values
    # layer_init = ds.d2fd[0]
    # print('Shape of data array: ', layer_init.shape)
    return specmat


def mouse_move(event):
    x, y = event.xdata, event.ydata
    global Hs_array
    if x is not None and y is not None:
        i = int(-y * 2 + 180)
        j = int(x * 2)
        Hs = Hs_array[i][j].values
        if not np.isnan(Hs):
            print('Hs = {:.3} m'.format(Hs))


def polar_plot(spec_data):
    """ Plot the wave spectrum based on the data obtained from `read_spec`."""
    ax = plt.figure()
    plt.pcolor(spec_data, cmap=plt.cm.coolwarm)



if __name__ == '__main__':
    spec = read_spec_grib('spect.grib')
    intg = read_file('integ.nc')      # 'integ.grib' 'integ.nc'
    plot_integ(intg, spec)
