# SOARS_2025
Code used in evaluating CESM in comparison to OMI/MLS observations
Contains all relevant datafiles and figures

Directories:

input: Direct input from NASA, containing ground-to-100 hPa and ground-to-300 hPa TCO data from OMI/MLS. Unfortunately, model output from CESM2.2 CAM-chem is too large to store onto GitHub easily so it is cut out, but the location on NSF NCAR supercomputer for O3 and PS files are: 
    O3:   /glade/campaign/acom/acom-climate/UTLS/shawnh/archive/FCnudged_f09.mam.mar27.2000_2021.002/atm/proc/tseries/month_1/FCnudged_f09.mam.mar27.2000_2021.002.cam.h0.O3.200201-202412.nc
    PS:   /glade/campaign/acom/acom-climate/UTLS/shawnh/archive/FCnudged_f09.mam.mar27.2000_2021.002/atm/proc/tseries/month_1/FCnudged_f09.mam.mar27.2000_2021.002.cam.h0.PS.200201-202412.nc
)
scripts: Code for making OMI/MLS climatology, unit converting & model/measurement m, and scripts for latitude plots & time series
figures: Figures from scripts
data: Self-made netCDF files created from model and observations, to reference/use easily in scripts 
( datasets_full: Full files using all available data latitude and longitude, used in latitude plots & certain maps
  OMI_MLS_climatology_files: Files used in data archives https://doi.org/10.5065/02h2-6c44. Files with "full" in title still contain all available latitude and longitude values, but these are averaged similarly to truncated files. Used in zonal averages
)
temp: Temporary scripts, to be deleted. Not necessary in ADF
utils: Self-made modules to help plot. Not necessary in ADF