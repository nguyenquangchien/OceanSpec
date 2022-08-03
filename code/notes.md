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

An irregular grid has been used. There are 315258 sampling locations on earth.

```
>>> ds
<xarray.Dataset>
Dimensions:          (time: 24, directionNumber: 24, frequencyNumber: 30, values: 315258)
Coordinates:
    number           int64 ...
  * time             (time) datetime64[ns] 2022-03-01 ... 2022-03-01T23:00:00
    step             timedelta64[ns] 00:00:00
    meanSea          float64 0.0
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
    history:                 2022-07-18T22:19 GRIB to CDM+CF via cfgrib-0.9.1...
>>> idx = 9999
>>> ds.longitude[idx].values
array(37.84090909)
>>> ds.longitude[idx].values + 2
39.84090909090911
>>> ds.latitude[idx].values
array(69.48)
>>> len(ds.d2fd)
24
>>> len(ds.d2fd[0])
24
>>> len(ds.d2fd[0][0][0])
315258
>>> ds.d2fd[0][0][0][idx].values
array(nan, dtype=float32)
>>> idx = 999
>>> ds.d2fd[0][0][0][idx].values
array(nan, dtype=float32)
>>> idx = 2400
>>> ds.d2fd[0][0][0][idx].values
array(nan, dtype=float32)
>>> idx = 9999
>>> idx = 99999
>>> ds.d2fd[0][0][0][idx].values
array(nan, dtype=float32)
>>> ds.longitude[idx].values, ds.latitude[idx].values
(array(281.25), array(21.96))
>>> idx = 34567
>>> ds.longitude[idx].values, ds.latitude[idx].values
(array(105.57692308), array(51.48))
>>> ds.d2fd[0][10][10][idx].values
array(nan, dtype=float32)
>>> idx = 99999
>>> ds.d2fd[0][10][10][idx].values
array(nan, dtype=float32)
>>> ds.d2fd[0][20][10][idx].values
array(nan, dtype=float32)
>>> idx = 76543
>>> ds.longitude[idx].values, ds.latitude[idx].values
(array(193.48946136), array(31.32))
>>> ds.d2fd[0][20][10][idx].values
array(-0.29671097, dtype=float32)
```

In finding the rule of longitudinal spacing which depends on the latitude:

```
>>> ds = read_file('spect.grib')
>>> for idx in range(76540, 76546):
...     print(idx, ds.longitude[idx].values, ds.latitude[idx].values)
... 
76540 192.22482435597112 31.320000000000093
76541 192.64637002341843 31.320000000000093
76542 193.06791569086573 31.320000000000093
76543 193.48946135831304 31.320000000000093
76544 193.91100702576034 31.320000000000093
76545 194.33255269320765 31.320000000000093

In [2]: for idx in range(36540, 36546): 
   ...:     print(idx, ds.longitude[idx].values, ds.latitude[idx].values) 
   ...:                                                                         
36540 152.35109717868391 50.40000000000006
36541 152.91536050156793 50.40000000000006
36542 153.47962382445195 50.40000000000006
36543 154.04388714733597 50.40000000000006
36544 154.60815047021998 50.40000000000006
36545 155.172413793104 50.40000000000006

In [3]: for idx in range(16540, 16546): 
   ...:     print(idx, ds.longitude[idx].values, ds.latitude[idx].values) 
   ...:                                                                         
16540 215.67567567567508 63.72000000000004
16541 216.4864864864859 63.72000000000004
16542 217.2972972972967 63.72000000000004
16543 218.1081081081075 63.72000000000004
16544 218.9189189189183 63.72000000000004
16545 219.72972972972912 63.72000000000004


In [7]: for idx in range(157626, 157632): 
   ...:     print(idx, ds.longitude[idx].values, ds.latitude[idx].values) 
   ...:                                                                         
157626 300.2400000000063 0.7200000000001266
157627 300.60000000000633 0.7200000000001266
157628 300.96000000000635 0.7200000000001266
157629 301.32000000000636 0.7200000000001266
157630 301.6800000000064 0.7200000000001266
157631 302.0400000000064 0.7200000000001266

In [8]: for idx in range(157666, 157672): 
   ...:     print(idx, ds.longitude[idx].values, ds.latitude[idx].values) 
   ...:                                                                         
157666 314.64000000000686 0.7200000000001266
157667 315.0000000000069 0.7200000000001266
157668 315.3600000000069 0.7200000000001266
157669 315.7200000000069 0.7200000000001266
157670 316.0800000000069 0.7200000000001266
157671 316.44000000000693 0.7200000000001266

In [9]: for idx in range(157766, 157772): 
   ...:     print(idx, ds.longitude[idx].values, ds.latitude[idx].values) 
   ...:                                                                         
157766 350.64000000000823 0.7200000000001266
157767 351.00000000000824 0.7200000000001266
157768 351.36000000000826 0.7200000000001266
157769 351.72000000000827 0.7200000000001266
157770 352.0800000000083 0.7200000000001266
157771 352.4400000000083 0.7200000000001266

In [10]: for idx in range(157866, 157872): 
    ...:     print(idx, ds.longitude[idx].values, ds.latitude[idx].values) 
    ...:                                                                        
157866 26.639999999999976 0.36000000000012666
157867 26.999999999999975 0.36000000000012666
157868 27.359999999999975 0.36000000000012666
157869 27.719999999999974 0.36000000000012666
157870 28.079999999999973 0.36000000000012666
157871 28.439999999999973 0.36000000000012666

In [11]: for idx in range(158066, 158072): 
    ...:     print(idx, ds.longitude[idx].values, ds.latitude[idx].values) 
    ...:                                                                        
158066 98.63999999999987 0.36000000000012666
158067 98.99999999999987 0.36000000000012666
158068 99.35999999999987 0.36000000000012666
158069 99.71999999999987 0.36000000000012666
158070 100.07999999999987 0.36000000000012666
158071 100.43999999999987 0.36000000000012666

In [12]: for idx in range(160066, 160072): 
    ...:     print(idx, ds.longitude[idx].values, ds.latitude[idx].values) 
    ...:                                                                        
160066 98.63999999999987 -0.3599999999998733
160067 98.99999999999987 -0.3599999999998733
160068 99.35999999999987 -0.3599999999998733
160069 99.71999999999987 -0.3599999999998733
160070 100.07999999999987 -0.3599999999998733
160071 100.43999999999987 -0.3599999999998733

In [13]: for idx in range(315250, 315258): 
    ...:     print(idx, ds.longitude[idx].values, ds.latitude[idx].values) 
    ...:                                                                        
315250 346.0194174757285 -78.11999999999978
315251 347.7669902912625 -78.11999999999978
315252 349.5145631067965 -78.11999999999978
315253 351.2621359223305 -78.11999999999978
315254 353.0097087378645 -78.11999999999978
315255 354.7572815533985 -78.11999999999978
315256 356.5048543689325 -78.11999999999978
315257 358.2524271844665 -78.11999999999978

In [14]: for idx in range(0, 8): 
    ...:     print(idx, ds.longitude[idx].values, ds.latitude[idx].values) 
    ...:                                                                        
0 0.0 90.0
1 180.0 90.0
2 0.0 89.64
3 60.0 89.64
4 120.0 89.64
5 180.0 89.64
6 240.0 89.64
7 300.0 89.64

In [15]: for idx in range(1000, 1008): 
    ...:     print(idx, ds.longitude[idx].values, ds.latitude[idx].values) 
    ...:                                                                        
1000 88.42105263157896 83.52000000000001
1001 91.57894736842107 83.52000000000001
1002 94.73684210526318 83.52000000000001
1003 97.89473684210529 83.52000000000001
1004 101.0526315789474 83.52000000000001
1005 104.21052631578951 83.52000000000001
1006 107.36842105263162 83.52000000000001
1007 110.52631578947373 83.52000000000001

In [23]: for idx in range(306000, 306008): 
    ...:     print(idx, ds.longitude[idx].values, ds.latitude[idx].values) 
    ...:                                                                        
306000 319.591836734694 -66.9599999999998
306001 320.5102040816328 -66.9599999999998
306002 321.4285714285716 -66.9599999999998
306003 322.3469387755104 -66.9599999999998
306004 323.2653061224492 -66.9599999999998
306005 324.183673469388 -66.9599999999998
306006 325.1020408163268 -66.9599999999998
306007 326.0204081632656 -66.9599999999998

In [24]: for idx in range(308000, 308008): 
    ...:     print(idx, ds.longitude[idx].values, ds.latitude[idx].values) 
    ...:                                                                        
308000 86.96629213483142 -69.11999999999979
308001 87.9775280898876 -69.11999999999979
308002 88.98876404494378 -69.11999999999979
308003 89.99999999999996 -69.11999999999979
308004 91.01123595505614 -69.11999999999979
308005 92.02247191011232 -69.11999999999979
308006 93.0337078651685 -69.11999999999979
308007 94.04494382022467 -69.11999999999979

In [25]: dlons = [0.36, 0.4215, 0.5643, 0.8108, 1.0112, 1.7475, 3.1579]         

In [26]: lats = [0.72, 31.32, 50.4, 63.72, 69.12, 78.12, 83.52]                 

In [29]: ax = plt.scatter(lats, dlons); plt.grid(True); plt.xlabel('ϕ (°)'); plt
    ...: .ylabel('Δλ (°)'); plt.show()                                          

# Ref https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html 
In [30]: from scipy.optimize import curve_fit                                   

In [32]: import numpy as np                                                            

In [50]: def func(x, a): 
    ...:     return a / np.cos(np.radians(x)) 
    ...:                                                                        

In [51]: popt, pcov = curve_fit(func, lats, dlons)                              

In [52]: popt                                                                   
Out[52]: array([0.35756356])

In [55]: ax = plt.scatter(lats, dlons); plt.grid(True); plt.xlabel('ϕ (°)'); plt
    ...: .ylabel('Δλ (°)'); ser=np.linspace(0,84,85); plt.plot(ser, func(ser, *p
    ...: opt), '-', color='orange', label='fit: Δλ = %.4f / cosϕ' % tuple(popt) 
    ...: ); plt.legend();  plt.show()                                           

```

* The index 158792 correspond to location lon = 0 and lat = 0.
* Latitude spacing Δϕ = 0.36°
* Longitude spacing Δλ = 0.36°/cosϕ

# Building table long lat for fast retrieval

Function `table_lon_lat`

along with the creation of `tags` saved into a `pickle` file:

```
>>> newtags = []
>>> count = 0
>>> for t in tags:
...     _, idx, lat, dlon = t
...     newtags.append((count, idx, round(lat+0.0,2), dlon+0.0))
...     count += 1

>>> newtags
[(0, 0, 90.0, 180.0), (1, 2, 89.64, 60.0), (2, 8, 89.28, 25.714285714285715), (3, 22, 88.92, 18.0), (4, 42, 88.56, 13.846153846153847), (5, 68, 88.2, 11.25), (6, 100, 87.84, 9.473684210526315), ... ]

>>> with open('tags.pkl', 'wb') as openfile:
...     pickle.dump(newtags, openfile, protocol=pickle.HIGHEST_PROTOCOL)
```

* Find latitude index = round((90 - lat)/0.36)
* Adjust longitude = 0 if longitude > 360 - 0.5*delta_lon
* index = index + round(adjsut_lon / delta_lon)

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