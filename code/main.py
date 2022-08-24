import os
import pickle
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


def plot_integ(integ):
    """ Plot a map of the integrated wave properties.
        Previously the function takes two arguments: integ and spect
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
    # cbar = map.colorbar(shrink=.5, aspect=15, pad=.05)
    # print('Shape of wave height data array: ', Hs_array.shape)
    binding_id = plt.connect('motion_notify_event', on_mousemove)
    plt.connect('button_press_event', on_click)
    # global spectrum
    # spectrum = spect
    plt.show()


def read_spec_grib(file_name):
    """ Read the spectral data from a GRIB file.
    """
    ds = read_file(file_name)
    return ds


def spectral_matrix(ds, idx):
    time_idx = 0
    specmat = np.zeros((len(ds.directionNumber), len(ds.frequencyNumber)))
    for i in range(specmat.shape[0]):
        for j in range(specmat.shape[1]):
            specmat[i, j] = ds.d2fd[time_idx][i][j][idx].values

    specmat = 10 ** specmat
    specmat = np.nan_to_num(specmat)
    return specmat


def mapping_dict(ds):
    """ Creates dictionary `d` such that `d[(lon100,lat100)]` returns the index
        of the location in the GRIB dataset. Here we use lon100 and lat100
        which are longitude*100 and latitude*100, to avoid floating point
        comparison errors.
        
        The dictionary is prepared before the GUI event loop.
        This is the explicit way of mapping the locations to the indices.
    """
    IDX_START = 0   # location Lat = 90.0, Lon = 0.0
    IDX_COUNT = ds.d2fd[0][0][0].values.shape[0]  # 315258

    d = {}
    tags = []
    count = 0
    for i in range(IDX_START, IDX_COUNT):
        if i % 10000 == 0:
            print(f'{i}/{IDX_COUNT}')
        lon, lat = ds.longitude[i].values, ds.latitude[i].values
        d[(round(lon*100), round(lat*100))] = i
        if lon == 0:
            assert i < IDX_COUNT - 1    # last index cannot have lon = 0
            newlon = ds.longitude[i+1].values
            tags.append((count, i, lat, newlon))  # store location where a new latitude starts together with the longitude spacing
            count += 1
    
    assert d[(6000,  8964)] == 3
    assert d[(9050, -6876)] == 307643
    assert d[(9000, -6912)] == 308003
    assert d[(9000, -6948)] == 308358

    assert tags[-1][2] == -78.12    # southernmost latitude
    assert tags[-2][2] - tags[-1][2] == 0.36    # latitude spacing
    assert tags[-2][2] < tags[-1][2]    # longitude spacing

    return d, tags


def mapping_dict_formulate(ds):
    """ Creates dictionary `d` such that `d[(lon100,lat100)]` returns the index
        of the location in the GRIB dataset. Here we use lon100 and lat100.
        
        This way uses formulation to create the dictionary.
        For the explicit way, see mapping_dict.
    """
    IDX0  = 158792  # location Lat = 0, Lon = 0.
    IDX_START = 2   # location Lat = 89.64, Lon = 0.
    IDX_END = 315258
    assert ds.d2fd[5][3][2].values.shape[0] == IDX_END
    DLON0 = 0.36  # 0.35756356  # longitude spacing at equator
    DLAT  = 0.36  # equidistant

    d = {(0, 900): 0}    # singularity point - north pole
    d = {(1800, 900): 1}    # another singularity point - north pole

    # For the southern hemisphere
    lon = 0.0
    lat = 0.0
    dlon = DLON0 / np.cos(np.radians(lat))  # incorrect, needs to search explicit ds.longitude[idx].values to find out the spacing corresponding to each latitude
    for idx in range(IDX0, IDX_END+1):
        lon100 = round(lon*100)
        lat100 = round(lat*100)
        d[(lon100, lat100)] = idx
        lon += dlon
        if lon > 359.8:
            # reset longitude and jump to the next latitude level
            lon = 0.0
            lat -= DLAT
            dlon = DLON0 / np.cos(np.radians(lat))

    assert d[(0, -36)] == IDX0 + 1000
    # assert d[(9000, -6912)] == 308003

    # Similar for the northern hemisphere
    lon = 0.0
    lat = 89.64
    dlon = DLON0 / np.cos(np.radians(lat))  # incorrect, needs to search explicit ds.longitude[idx].values to find out the spacing corresponding to each latitude
    for idx in range(IDX_START, IDX0):
        lon100 = round(lon*100)
        lat100 = round(lat*100)
        d[(lon100, lat100)] = idx
        if lat100 > 8856:
            print(lon100, lat100, '->', d[(lon100, lat100)], end='  ')
        lon += dlon
        if lon > 359.9:
            # reset longitude and jump to the next latitude level
            lon = 0.0
            lat -= DLAT
            dlon = DLON0 / np.cos(np.radians(lat))
            

    assert d[(0, 8964)] == IDX_START
    assert d[(0, 8928)] == IDX_START + 6
    assert d[(0, 0)] == IDX0
    
    print(len(d))
    print(list(d.keys())[-10:])
    
    return d


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
        
        global table_lon_lat, tags
        
        DLAT = 0.36
        latrow = round((90 - y) / DLAT)    # scanning by latitude
        idx = tags[latrow][1]
        delta_lon = tags[latrow][3]
        x_adj = 0 if x > 360 - 0.5 * delta_lon else x
        loncol = round(x_adj / delta_lon)
        idx += loncol
        print(f'Fetch data at latitude row {latrow}, longitude column {loncol}, index {idx}')
        # spectrum = spectral_matrix(ds, idx)  # slicing directly from spec_cube instead
        spectrum = spec_cube[:, :, idx]
        # no need to use table_lon_lat?
        # spectrum = spectral_matrix(ds, table_lon_lat[lon100, lat100])
        polar_plot(spectrum)


def polar_plot(spec_data):
    """ Plot the wave spectrum based on the data obtained from `read_spec`.
        Try imitating https://www.youtube.com/watch?v=DyPjsj6azY4 
        and https://stackoverflow.com/a/9083017/4956603
        https://stackoverflow.com/questions/32462881/add-colorbar-to-existing-axis
        https://stackoverflow.com/questions/15908371/matplotlib-colorbars-and-its-text-labels
    """
    angles = np.radians(np.arange(7.5, 352.5 + 15, 15))
    assert len(angles) == spec_data.shape[0]
    n_freq_bins = spec_data.shape[1]
    freqs = np.full(n_freq_bins, 0.03453) * (1.1 ** np.arange(0, n_freq_bins))
    r, theta = np.meshgrid(freqs, angles)

    fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
    ctr = ax.contourf(theta, r, spec_data, 10, cmap='OrRd')
    ax.set_xticklabels(['E', '', 'N', '', 'W', '', 'S', ''])
    cbar = fig.colorbar(ctr, ax=ax)
    cbar.set_label('Spectral density, m²s rad⁻¹', rotation=270)
    print('Done')
    fig.show()


if __name__ == '__main__':
    ds = read_spec_grib('spect.grib')
    intg = read_file('integ.nc')      # 'integ.grib' 'integ.nc'
    print('Finished reading files GRIB (spectra) and netCDF (integral quantities).')
    
    global table_lon_lat, tags
    
    if os.path.exists('table_lon_lat.pickle'):
        with open('table_lon_lat.pickle', 'rb') as f:
            table_lon_lat = pickle.load(f)
        with open('tags.pkl', 'rb') as f:
            tags = pickle.load(f)
    else:
        table_lon_lat, tags = mapping_dict(ds)
    
    # trying to transform spectral data in advance
    spec_cube = np.zeros((len(ds.directionNumber), len(ds.frequencyNumber), 315258))
    spec_cube = np.nan_to_num(10**ds.d2fd[0])
    print(f"Size of spec_cube: {spec_cube.shape}")

    plot_integ(intg)  # previously plot_integ(intg, spec)
