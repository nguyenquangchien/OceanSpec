import os
import pickle
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt 
from mpl_toolkits.basemap import Basemap


def read_file(file_name):
    """ Reads data from a GRIB or netCDF file.
        Returns a dataset.
    """
    if file_name.endswith('grib'):
        ds = xr.open_dataset(file_name, engine='cfgrib')
    else:
        ds = xr.open_dataset(file_name)
    return ds


def plot_integ(integ):
    """ Plot a map of the integrated wave properties `integ`.
        Parameter: `integ` - a dataset.
    """
    map = Basemap(projection='cyl',lon_0=180,lat_0=0,
                  resolution='c', area_thresh = 50, 
                  llcrnrlon=0, llcrnrlat=-89, urcrnrlon=360, urcrnrlat=89)
    map.drawcoastlines(linewidth=0.25)
    map.drawmeridians(np.arange(0, 361, 30))
    map.drawparallels(np.arange(-90, 91, 30))

    global Hs_array
    Hs_array = integ.swh[0]
    Hs_array.plot(cmap=plt.cm.coolwarm)
    # TODO: minimise the color bar # cbar = map.colorbar(shrink=.5, aspect=15, pad=.05)
    plt.connect('motion_notify_event', on_mousemove)
    plt.connect('button_press_event', on_click)
    plt.show()


def mapping_dict(ds):
    """ Creates the list `tags` such that `tags[i]` contains the 
        point count, index, latitude and longitude.
        
        The list is prepared before the GUI event loop.
        This is the explicit way of mapping the locations to the indices.
    """
    IDX_START = 0   # location Lat = 90.0, Lon = 0.0
    IDX_COUNT = ds.d2fd[0][0][0].values.shape[0]  # 315258

    tags = []
    count = 0
    for i in range(IDX_START, IDX_COUNT):
        if i % 10000 == 0:
            print(f'{i}/{IDX_COUNT}')
        lon, lat = ds.longitude[i].values, ds.latitude[i].values
        
        if lon == 0:
            assert i < IDX_COUNT - 1    # last index cannot have lon = 0
            newlon = ds.longitude[i+1].values
            tags.append((count, i, lat, newlon))  # store location where a new latitude starts together with the longitude spacing
            count += 1
    
    assert tags[-1][2] == -78.12                # southernmost latitude
    assert tags[-2][2] - tags[-1][2] == 0.36    # latitude spacing
    assert tags[-2][2] < tags[-1][2]            # longitude spacing

    return tags


def on_mousemove(event):
    x, y = event.xdata, event.ydata
    global Hs_array
    if x is not None and y is not None:
        i = int(-y * 2 + 180)
        j = int(x * 2)
        Hs = Hs_array[i][j].values
        if not np.isnan(Hs):
            print('Hs = {:.3} m'.format(Hs))


def on_click(event):
    if event.button == 1:  # left
        x, y = event.xdata, event.ydata
        print(f'click at lon {x:.5}, lat {y:.3}')
        
        global tags
        DLAT = 0.36
        latrow = round((90 - y) / DLAT)    # scanning by latitude
        idx = tags[latrow][1]
        delta_lon = tags[latrow][3]
        x_adj = 0 if x > 360 - 0.5 * delta_lon else x
        loncol = round(x_adj / delta_lon)
        idx += loncol
        print(f'Fetch data at latitude row {latrow}, longitude column {loncol}, index {idx}')
        spectrum = spec_cube[:, :, idx]
        polar_plot(spectrum)


def polar_plot(spec_data):
    """ Plot the wave spectrum based on the data obtained from `read_spec`.
        Try imitating https://www.youtube.com/watch?v=DyPjsj6azY4 
        and https://stackoverflow.com/a/9083017/4956603
        https://stackoverflow.com/questions/32462881/add-colorbar-to-existing-axis
        https://stackoverflow.com/questions/15908371/matplotlib-colorbars-and-its-text-labels
    """
    FREQ_MIN = 0.03453
    FACTOR = 1.1
    ANGLE_MIN = 7.5
    ANGLE_MAX = 352.5
    ANGLE_INC = 15
    angles = np.radians(np.arange(ANGLE_MIN, ANGLE_MAX + ANGLE_INC, ANGLE_INC))
    assert len(angles) == spec_data.shape[0]
    n_freq_bins = spec_data.shape[1]
    freqs = np.full(n_freq_bins, FREQ_MIN) * (FACTOR ** np.arange(0, n_freq_bins))
    r, theta = np.meshgrid(freqs, angles)

    fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
    ctr = ax.contourf(theta, r, spec_data, 10, cmap='OrRd')
    ax.set_xticklabels(['E', '', 'N', '', 'W', '', 'S', ''])
    cbar = fig.colorbar(ctr, ax=ax)  # TODO: a unified color scale
    cbar.set_label('Spectral density, m²s rad⁻¹', rotation=270)
    fig.show()


if __name__ == '__main__':
    ds = read_file('spect.grib')
    intg = read_file('integ.nc')      # either 'integ.grib' or 'integ.nc'
    print('Finished reading files GRIB (spectra) and netCDF (integral quantities).')
    
    global tags
    
    if os.path.exists('tags.pkl'):
        with open('tags.pkl', 'rb') as f:
            tags = pickle.load(f)
    else:
        tags = mapping_dict(ds)
    
    # transform spectral data in advance
    spec_cube = np.zeros((len(ds.directionNumber), len(ds.frequencyNumber), 315258))
    spec_cube = np.nan_to_num(10**ds.d2fd[0])
    print(f"Size of spec_cube: {spec_cube.shape}")

    plot_integ(intg)
