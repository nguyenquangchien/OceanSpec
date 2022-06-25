# import magpye
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
    print(ds.swh[0].shape)
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
    if x is not None and y is not None:
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
    # print(f'Max wave height: {np.max(ds.swh[0][0]):5:2}')

    # Failed without pygrib, on Windows 10
    ds = read_file('spect.grib')
    specdata = ds.d2fd[1][0][0].values
    print(len(specdata))  # d2fd[timeidx][diridx][freqidx]


    # Refer to file ECMWF_guide_ERA5.md for more information.
    # In GRIB, the parameter is called 2d wave spectra (single) because in GRIB, 
    # the data are stored as a single global field per each spectral bin 
    # (a given frequency and direction).
    #
    # The wave spectra are encoded in GRIB using a local table specific to ECMWF. 
    # Because of this, the conversion of the metadata containing the information 
    # about the frequencies and the directions are not properly converted 
    # from GRIB to NetCDF format. So rather than having the actual values of 
    # the frequencies and directions, values show index numbers (1,1) : first frequency, 
    # first direction, (1,2) first frequency, second direction, etc ....

    # For ERA, because there are a total of 24 directions, the direction increment 
    # is 15 degrees with the first direction given by half the increment, namely 7.5 degree, 
    # where direction 0. means going towards the north and 90 towards the east 
    # (Oceanographic convention), or more precisely, this should be expressed in gradient 
    # since the spectra are in m^2 /(Hz radian)
    #
    # The first frequency is 0.03453 Hz and the following ones are : f(n) = f(n-1)×1.1, n=2,30

    # Also note that it is NOT the spectral density that is encoded but rather log10 of it, 
    # so to recover the spectral density, expressed in m^2 /(radian Hz), one has to take 
    # the power 10 (10^) of the NON missing decoded values. Missing data are for all 
    # land points, but also, as part of the GRIB compression, all small values below 
    # a certain threshold have been discarded and so those missing spectral values 
    # are essentially 0. m^2 /(gradient Hz).
    #
    # GRIB files may be tricky, try using eccodes
    # import eccodes
    # eccodes.codes_grib_set_long(ds.d2fd[0][0][0], 'typeOfFirstFixedSurface', 1)
    # >>> dir(eccodes)
    # ['ArrayTooSmallError', 'AttributeClashError', 'AttributeNotFoundError', 
    # 'BufferTooSmallError', 'CODES_CHECK', 'CODES_GRIB_NEAREST_SAME_DATA', 
    # 'CODES_GRIB_NEAREST_SAME_GRID', 'CODES_GRIB_NEAREST_SAME_POINT', 
    # 'CODES_MISSING_DOUBLE', 'CODES_MISSING_LONG', 'CODES_PRODUCT_ANY', 
    # 'CODES_PRODUCT_BUFR', 'CODES_PRODUCT_GRIB', 'CODES_PRODUCT_GTS', 
    # 'CODES_PRODUCT_METAR', 'CodeNotFoundInTableError', 'CodesInternalError', 
    # 'ConceptNoMatchError', 'ConstantFieldError', 'CorruptedIndexError', 
    # 'DecodingError', 'DifferentEditionError', 'EncodingError', 'EndError', 
    # 'EndOfFileError', 'EndOfIndexError', 'FileNotFoundError', 
    # 'FunctionNotImplementedError', 'FunctionalityNotEnabledError', 
    # 'GeocalculusError', 'GribInternalError', 'HashArrayNoMatchError', 
    # 'IOProblemError', 'InternalArrayTooSmallError', 'InternalError', 
    # 'InvalidArgumentError', 'InvalidBitsPerValueError', 'InvalidFileError', 
    # 'InvalidGribError', 'InvalidIndexError', 'InvalidIteratorError', 
    # 'InvalidKeyValueError', 'InvalidKeysIteratorError', 'InvalidNearestError', 
    # 'InvalidOrderByError', 'InvalidSectionNumberError', 'InvalidTypeError', 
    # 'KeyValueNotFoundError', 'MemoryAllocationError', 'MessageEndNotFoundError', 
    # 'MessageInvalidError', 'MessageMalformedError', 'MessageTooLargeError', 
    # 'MissingBufrEntryError', 'MissingKeyError', 'NoDefinitionsError', 
    # 'NoMoreInSetError', 'NoValuesError', 'NullHandleError', 'NullIndexError', 
    # 'NullPointerError', 'OutOfAreaError', 'OutOfRangeError', 'PrematureEndOfFileError', 
    # 'ReadOnlyError', 'StringTooSmallError', 'SwitchNoMatchError', 
    # 'TooManyAttributesError', 'UnderflowError', 'UnsupportedEditionError', 
    # 'ValueCannotBeMissingError', 'ValueDifferentError', 'WrongArraySizeError', 
    # 'WrongBitmapSizeError', 'WrongConversionError', 'WrongGridError', 
    # 'WrongLengthError', 'WrongStepError', 'WrongStepUnitError', 'WrongTypeError', 
    # '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
    # '__package__', '__path__', '__spec__', '__version__', 'bindings_version', 
    # 'codes_any_new_from_file', 'codes_bufr_copy_data', 'codes_bufr_extract_headers', 
    # 'codes_bufr_key_is_header', 'codes_bufr_keys_iterator_delete', 
    # 'codes_bufr_keys_iterator_get_name', 'codes_bufr_keys_iterator_new', 
    # 'codes_bufr_keys_iterator_next', 'codes_bufr_keys_iterator_rewind', 
    # 'codes_bufr_multi_element_constant_arrays_off', 'codes_bufr_multi_element_constant_arrays_on', 
    # 'codes_bufr_new_from_file', 'codes_bufr_new_from_samples', 'codes_clone', 'codes_context_delete', 
    # 'codes_copy_namespace', 'codes_count_in_file', 'codes_definition_path', 
    # 'codes_dump', 'codes_extract_offsets', 'codes_get', 'codes_get_api_version', 
    # 'codes_get_array', 'codes_get_double', 'codes_get_double_array', 
    # 'codes_get_double_element', 'codes_get_double_elements', 'codes_get_elements', 
    # 'codes_get_library_path', 'codes_get_long', 'codes_get_long_array', 
    # 'codes_get_message', 'codes_get_message_offset', 'codes_get_message_size', 
    # 'codes_get_native_type', 'codes_get_size', 'codes_get_string', 'codes_get_string_array', 
    # 'codes_get_string_length', 'codes_get_values', 'codes_get_version_info', 
    # 'codes_grib_find_nearest', 'codes_grib_find_nearest_multiple', 'codes_grib_get_data', 
    # 'codes_grib_iterator_delete', 'codes_grib_iterator_new', 'codes_grib_iterator_next', 
    # 'codes_grib_multi_append', 'codes_grib_multi_new', 'codes_grib_multi_release', 
    # 'codes_grib_multi_support_off', 'codes_grib_multi_support_on', 'codes_grib_multi_support_reset_file', 
    # 'codes_grib_multi_write', 'codes_grib_nearest_delete', 'codes_grib_nearest_find', 
    # 'codes_grib_nearest_new', 'codes_grib_new_from_file', 'codes_grib_new_from_samples', 
    # 'codes_gribex_mode_off', 'codes_gribex_mode_on', 'codes_gts_header', 'codes_gts_new_from_file', 
    # 'codes_index_add_file', 'codes_index_get', 
    # 'codes_index_get_double', 'codes_index_get_long', 'codes_index_get_size', 
    # 'codes_index_get_string', 'codes_index_new_from_file', 'codes_index_read', 
    # 'codes_index_release', 'codes_index_select', 'codes_index_select_double', 
    # 'codes_index_select_long', 'codes_index_select_string', 'codes_index_write', 
    # 'codes_is_defined', 'codes_is_missing', 'codes_keys_iterator_delete', 
    # 'codes_keys_iterator_get_name', 'codes_keys_iterator_new', 'codes_keys_iterator_next', 
    # 'codes_keys_iterator_rewind', 'codes_metar_new_from_file', 'codes_new_from_file', 
    # 'codes_new_from_index', 'codes_new_from_message', 'codes_new_from_samples', 
    # 'codes_no_fail_on_wrong_length', 'codes_release', 'codes_samples_path', 
    # 'codes_set', 'codes_set_array', 'codes_set_definitions_path', 'codes_set_double', 
    # 'codes_set_double_array', 'codes_set_key_vals', 'codes_set_long', 
    # 'codes_set_long_array', 'codes_set_missing', 'codes_set_samples_path', 
    # 'codes_set_string', 'codes_set_string_array', 'codes_set_values', 
    # 'codes_skip_coded', 'codes_skip_computed', 'codes_skip_duplicates', 
    # 'codes_skip_edition_specific', 'codes_skip_function', 'codes_skip_read_only', 
    # 'codes_write', 'eccodes']

