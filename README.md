# SOARS 2025
Code for research project, evaluating CESM2.2 CAM-chem ozone concentration output in comparison to OMI/MLS measurements.
Contains all necessary files and scripts.

Directories:

input: Location for direct input from NASA webpage for OMI/MLS ground-to-300hPa and ground-to-100hPa TCO. Model output not included because too large for GitHub storage
scripts: Contains all code for OMI/MLS climatology, unit converting and model/measurement matching, and plots
data: Self-made netCDF files for easy use in scripts. {
    datasets_full: Used in time series and certain maps, all latitudes/longitudes of available data are stored here
    OMI_MLS_climatology_files: Used in zonal averages. Also contains truncated netCDF files used in DOI
}
figures: All relevant figures here
utils: Self-made modules used in plotting. Not necessary in ADF but can be found helpful
temp: Temporary files to be deleted. Not necessary in ADF