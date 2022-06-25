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
