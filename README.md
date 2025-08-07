# SOARS 2025
Code for research project, evaluating CESM2.2 CAM-chem ozone concentration output in comparison to OMI/MLS measurements.
Contains all necessary files and scripts.

Directories:

1. input: Location for direct input from NASA webpage for OMI/MLS ground-to-300hPa and ground-to-100hPa TCO. Model output not included because too large for GitHub storage

2. scripts: Contains all code for OMI/MLS climatology, unit converting and model/measurement matching, and plots

3. data: Self-made netCDF files for easy use in scripts. {
    datasets_full: Used in time series and certain maps, all latitudes/longitudes of available data are stored here
    OMI_MLS_climatology_files: Used in zonal averages. Also contains truncated (75°S-75°N) netCDF files used in DOI
}

4. figures: All relevant figures here

5. utils: Self-made modules used in plotting. Not necessary in ADF but can be found helpful

6. temp: Temporary files to be deleted. Not necessary in ADF