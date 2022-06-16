import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',  # 'grib',
        'year': '2022',
        'month': '03',
        'day': [
            '01', 
        ],
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],
        # 'area': [  61, -3.5, 51, 7, ], # North Sea, comment out to set global
        'variable': [
            'mean_wave_direction', 'model_bathymetry', 'significant_height_of_combined_wind_waves_and_swell',
            'wave_spectral_directional_width', 'wave_spectral_directional_width_for_swell', 'wave_spectral_directional_width_for_wind_waves',
            'wave_spectral_kurtosis', 'wave_spectral_peakedness', 'wave_spectral_skewness',
        ],
    },
    'integ.nc'    # 'integ.grib'
    )