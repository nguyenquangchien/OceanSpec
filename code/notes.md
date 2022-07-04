## For integ.nc (size 112.3 MB)
(file size on Mac OS X)
```
<xarray.Dataset>
Dimensions:    (longitude: 720, latitude: 361, time: 24)
Coordinates:
  * longitude  (longitude) float32 0.0 0.5 1.0 1.5 ... 358.0 358.5 359.0 359.5
  * latitude   (latitude) float32 90.0 89.5 89.0 88.5 ... -89.0 -89.5 -90.0
  * time       (time) datetime64[ns] 2022-03-01 ... 2022-03-01T23:00:00
Data variables:
    mwd        (time, latitude, longitude) float32 ...
    wmb        (time, latitude, longitude) float32 ...
    swh        (time, latitude, longitude) float32 ...
    wdw        (time, latitude, longitude) float32 ...
    dwps       (time, latitude, longitude) float32 ...
    dwww       (time, latitude, longitude) float32 ...
    wsk        (time, latitude, longitude) float32 ...
    wsp        (time, latitude, longitude) float32 ...
    wss        (time, latitude, longitude) float32 ...
Attributes:
    Conventions:  CF-1.6
    history:      2022-06-12 07:31:05 GMT by grib_to_netcdf-2.24.3: /opt/ecmw...
```


## For integ.grib (size 70.8 MB)

```
<xarray.Dataset>
Dimensions:     (time: 24, latitude: 361, longitude: 720)
Coordinates:
    number      int64 ...
  * time        (time) datetime64[ns] 2022-03-01 ... 2022-03-01T23:00:00
    step        timedelta64[ns] ...
    meanSea     float64 ...
  * latitude    (latitude) float64 90.0 89.5 89.0 88.5 ... -89.0 -89.5 -90.0
  * longitude   (longitude) float64 0.0 0.5 1.0 1.5 ... 358.0 358.5 359.0 359.5
    valid_time  (time) datetime64[ns] ...
Data variables:
    mwd         (time, latitude, longitude) float32 ...
    wmb         (time, latitude, longitude) float32 ...
    swh         (time, latitude, longitude) float32 ...
    wdw         (time, latitude, longitude) float32 ...
    dwps        (time, latitude, longitude) float32 ...
    dwww        (time, latitude, longitude) float32 ...
    wsk         (time, latitude, longitude) float32 ...
    wsp         (time, latitude, longitude) float32 ...
    wss         (time, latitude, longitude) float32 ...
Attributes:
    GRIB_edition:            1
    GRIB_centre:             ecmf
    GRIB_centreDescription:  European Centre for Medium-Range Weather Forecasts
    GRIB_subCentre:          0
    Conventions:             CF-1.7
    institution:             European Centre for Medium-Range Weather Forecasts
    history:                 2022-06-12T07:30 GRIB to CDM+CF via cfgrib-0.9.1...
```


## Dissecting integ.grib

```
>>> ds.number
<xarray.DataArray 'number' ()>
array(0)
Coordinates:
    number   int64 0
    step     timedelta64[ns] ...
    meanSea  float64 ...
Attributes:
    long_name:      ensemble member numerical id
    units:          1
    standard_name:  realization
>>> ds.time
<xarray.DataArray 'time' (time: 24)>
array(['2022-03-01T00:00:00.000000000', '2022-03-01T01:00:00.000000000',
       '2022-03-01T02:00:00.000000000', '2022-03-01T03:00:00.000000000',
       '2022-03-01T04:00:00.000000000', '2022-03-01T05:00:00.000000000',
       '2022-03-01T06:00:00.000000000', '2022-03-01T07:00:00.000000000',
       '2022-03-01T08:00:00.000000000', '2022-03-01T09:00:00.000000000',
       '2022-03-01T10:00:00.000000000', '2022-03-01T11:00:00.000000000',
       '2022-03-01T12:00:00.000000000', '2022-03-01T13:00:00.000000000',
       '2022-03-01T14:00:00.000000000', '2022-03-01T15:00:00.000000000',
       '2022-03-01T16:00:00.000000000', '2022-03-01T17:00:00.000000000',
       '2022-03-01T18:00:00.000000000', '2022-03-01T19:00:00.000000000',
       '2022-03-01T20:00:00.000000000', '2022-03-01T21:00:00.000000000',
       '2022-03-01T22:00:00.000000000', '2022-03-01T23:00:00.000000000'],
      dtype='datetime64[ns]')
Coordinates:
    number      int64 0
  * time        (time) datetime64[ns] 2022-03-01 ... 2022-03-01T23:00:00
    step        timedelta64[ns] ...
    meanSea     float64 ...
    valid_time  (time) datetime64[ns] ...
Attributes:
    long_name:      initial time of forecast
    standard_name:  forecast_reference_time
>>> ds.latitude
<xarray.DataArray 'latitude' (latitude: 361)>
array([ 90. ,  89.5,  89. , ..., -89. , -89.5, -90. ])
Coordinates:
    number    int64 0
    step      timedelta64[ns] ...
    meanSea   float64 ...
  * latitude  (latitude) float64 90.0 89.5 89.0 88.5 ... -88.5 -89.0 -89.5 -90.0
Attributes:
    units:             degrees_north
    standard_name:     latitude
    long_name:         latitude
    stored_direction:  decreasing
>>> ds.longitude
<xarray.DataArray 'longitude' (longitude: 720)>
array([  0. ,   0.5,   1. , ..., 358.5, 359. , 359.5])
Coordinates:
    number     int64 0
    step       timedelta64[ns] ...
    meanSea    float64 ...
  * longitude  (longitude) float64 0.0 0.5 1.0 1.5 ... 358.0 358.5 359.0 359.5
Attributes:
    units:          degrees_east
    standard_name:  longitude
    long_name:      longitude
>>> ds.mwd
<xarray.DataArray 'mwd' (time: 24, latitude: 361, longitude: 720)>
[6238080 values with dtype=float32]
Coordinates:
    number      int64 0
  * time        (time) datetime64[ns] 2022-03-01 ... 2022-03-01T23:00:00
    step        timedelta64[ns] ...
    meanSea     float64 ...
  * latitude    (latitude) float64 90.0 89.5 89.0 88.5 ... -89.0 -89.5 -90.0
  * longitude   (longitude) float64 0.0 0.5 1.0 1.5 ... 358.0 358.5 359.0 359.5
    valid_time  (time) datetime64[ns] ...
Attributes: (12/30)
    GRIB_paramId:                             140230
    GRIB_dataType:                            an
    GRIB_numberOfPoints:                      259920
    GRIB_typeOfLevel:                         meanSea
    GRIB_stepUnits:                           1
    GRIB_stepType:                            instant
    ...                                       ...
    GRIB_shortName:                           mwd
    GRIB_totalNumber:                         0
    GRIB_units:                               Degree true
    long_name:                                Mean wave direction
    units:                                    Degree true
    standard_name:                            unknown
>>> 

```


## For spect.grib (size 3.09 GB)

```
<xarray.Dataset>
Dimensions:          (time: 24, directionNumber: 24, frequencyNumber: 30, values: 315258)
Coordinates:
    number           int64 ...
  * time             (time) datetime64[ns] 2022-03-01 ... 2022-03-01T23:00:00
    step             timedelta64[ns] ...
    meanSea          float64 ...
  * directionNumber  (directionNumber) int64 1 2 3 4 5 6 7 ... 19 20 21 22 23 24
  * frequencyNumber  (frequencyNumber) int64 1 2 3 4 5 6 7 ... 25 26 27 28 29 30
    latitude         (values) float64 ...
    longitude        (values) float64 ...
    valid_time       (time) datetime64[ns] ...
Dimensions without coordinates: values
Data variables:
    d2fd             (time, directionNumber, frequencyNumber, values) float32 ...
Attributes:
    GRIB_edition:            1
    GRIB_centre:             ecmf
    GRIB_centreDescription:  European Centre for Medium-Range Weather Forecasts
    GRIB_subCentre:          0
    Conventions:             CF-1.7
    institution:             European Centre for Medium-Range Weather Forecasts
    history:                 2022-06-12T07:31 GRIB to CDM+CF via cfgrib-0.9.1...
```

Querying the first element of `d2fd` in `spect.grib`:
```
<xarray.DataArray 'd2fd' (directionNumber: 24, frequencyNumber: 30, values: 315258)>
[226985760 values with dtype=float32]
Coordinates:
    number           int64 ...
    time             datetime64[ns] 2022-03-01
    step             timedelta64[ns] ...
    meanSea          float64 ...
  * directionNumber  (directionNumber) int64 1 2 3 4 5 6 7 ... 19 20 21 22 23 24
  * frequencyNumber  (frequencyNumber) int64 1 2 3 4 5 6 7 ... 25 26 27 28 29 30
    latitude         (values) float64 ...
    longitude        (values) float64 ...
    valid_time       datetime64[ns] ...
Dimensions without coordinates: values
Attributes: (12/27)
    GRIB_paramId:                            140251
    GRIB_dataType:                           an
    GRIB_numberOfPoints:                     315258
    GRIB_typeOfLevel:                        meanSea
    GRIB_stepUnits:                          1
    GRIB_stepType:                           instant
    ...                                      ...
    GRIB_shortName:                          2dfd
    GRIB_totalNumber:                        0
    GRIB_units:                              m**2 s radian**-1
    long_name:                               2D wave spectra (single)
    units:                                   m**2 s radian**-1
    standard_name:                           unknown
```

For different time layers:

* `d2fd[0]` --> `time             datetime64[ns] 2022-03-01`
* `d2fd[1]` --> `time             datetime64[ns] 2022-03-01T01:00:00`

Fixing the direction: 

* `ds.d2fd[1][0]` --> `directionNumber  int64 1`

Fixing both the direction and the frequency: 

* `ds.d2fd[1][0]` --> 

```
    directionNumber  int64 1
    frequencyNumber  int64 1
```

Array organization:

* `arr = ds.d2fd[5][3].values` --> shape `(30, 315258)`.
* `arr = ds.d2fd[5][3][2].values` --> shape `(315258,)`.

Is `315258` associated with latitude and longitude?
315258 = 2 × 3 × 52543.
259200 = 180 × 360 × 4 (resolution 0.5 degrees).
259920 = 361 × 720 = shape of ds.swh[0] used for plotting.

There is a discrepancy between the data density and geographical density.


# Session Windows 10

```
    # Failed without pygrib, on Windows 10
    # ds = read_file('spect.grib')
    # specdata = ds.d2fd[1][0][0].values
    # print(len(specdata))  # d2fd[timeidx][diridx][freqidx]


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
```