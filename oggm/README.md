# OGGM
- https://oggm.org/
- https://docs.oggm.org/en/stable/
- https://oggm.org/tutorials/stable/notebooks/welcome.html


# Step by step

### Setup **Virtual Env**

- `sudo apt install python3.8-venv` (if necessary)
- `python -m venv venv`
- `source ./venv/bin/activate`
- `deactivate`


### Install packages

   - dependencies (**pandas**, ...)  
     `pip install numpy scipy pandas shapely matplotlib pyproj \
    rasterio Pillow geopandas netcdf4 scikit-image configobj joblib \
    xarray progressbar2 pytest motionless dask bottleneck toolz descartes \
    tables`

  - **oggm**  
    `pip install oggm`


### Git versioning

### First tutorial example