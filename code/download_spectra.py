#!/usr/bin/env python
import cdsapi


c = cdsapi.Client()

maxLat = 90
maxLon = 180
minLat = -90
minLon = -179
c.retrieve(
'reanalysis-era5-complete',{
'class': 'ea',
'date': '2022-03-01',
'direction': '1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24',
'domain': 'g',
'expver': '1',
'frequency': '1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30',
'number': '0/1/2/3/4/5/6/7/8/9',
'param': '251.140',
'stream': 'ewda',
'time': '00:00:00/01:00:00/02:00:00/03:00:00/04:00:00/05:00:00/06:00:00/07:00:00/08:00:00/09:00:00/10:00:00/11:00:00/12:00:00/13:00:00/14:00:00/15:00:00/16:00:00/17:00:00/18:00:00/19:00:00/20:00:00/21:00:00/22:00:00/23:00:00',
# 'area': str(maxLat) + '/' + str(maxLon) + '/' + str(minLat) + '/' + str(minLon), # North, West, South, East. Default: global
'grid': '0.5/0.5', # Latitude/longitude. Default: spherical harmonics or reduced Gaussian grid
'type': 'an',
'format': 'netcdf', # Output needs to be regular lat-lon, so only works in combination with 'grid'!
}, 'ISSM_Trial_ERA5_Data_NEW.nc')


# c.retrieve(
# 'reanalysis-era5-complete',{
# 'class': 'ea',
# 'date': '2003' + '-' + '02' + '-20/to/' + '2003' + '-' + '03' + '-01',
# 'direction': '1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24',
# 'domain': 'g',
# 'expver': '1',
# 'frequency': '1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30',
# 'number': '0/1/2/3/4/5/6/7/8/9',
# 'param': '251.140',
# 'stream': 'ewda',
# 'time': '00:00:00/03:00:00/06:00:00/09:00:00/12:00:00/15:00:00/18:00:00/21:00:00',
# 'area': str(maxLat) + '/' + str(maxLon) + '/' + str(minLat) + '/' + str(minLon), # North, West, South, East. Default: global
# 'grid': '0.5/0.5', # Latitude/longitude. Default: spherical harmonics or reduced Gaussian grid
# 'type': 'an',
# 'format': 'netcdf', # Output needs to be regular lat-lon, so only works in combination with 'grid'!
# }, 'ISSM_Trial_ERA5_Data_NEW.nc')


# c.retrieve('reanalysis-era5-complete', {
#     'class': 'ea',
#     'date': '2022-03-01',
#     'direction': '1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24',
#     'domain': 'g',
#     # 'area': [61, 356.5, 51, 7,],  # not implemented
#     'expver': '1',
#     'frequency': '1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30',
#     'param': '251.140',
#     'stream': 'wave',
#     'time': '00:00:00/01:00:00/02:00:00/03:00:00/04:00:00/05:00:00/06:00:00/07:00:00/08:00:00/09:00:00/10:00:00/11:00:00/12:00:00/13:00:00/14:00:00/15:00:00/16:00:00/17:00:00/18:00:00/19:00:00/20:00:00/21:00:00/22:00:00/23:00:00',
#     'type': 'an',
#     'format': 'grib',  # 'netcdf',  # TODO: error with netCDF because First GRIB is not on a regular lat/lon grid or on a regular Gaussian grid
# }, 'spect.grib')
