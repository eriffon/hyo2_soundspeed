import logging
import os

from netCDF4 import Dataset

from hyo2.ssm2.app.gui.soundspeedmanager import AppInfo

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

input_path = "C:\\Users\\gmasetti\\AppData\Local\\HydrOffice\\Sound Speed 0.1.0\\atlases\\woa09"
output_path = "C:\\Users\\gmasetti\\AppData\\Local\\HydrOffice\\Sound Speed 0.1.0\\atlases\\woa09_red"

# """ USED TO REDUCE THE SIZE OF THE FULL WOA09 DATABASE """

# temp annual
file = "temperature_annual_1deg.nc"
i_path = os.path.join(input_path, file)
i = Dataset(i_path, mode='r')
o_path = os.path.join(output_path, file)
if os.path.exists(o_path):
    os.remove(o_path)
o = Dataset(o_path, mode='w')

for name, dim in i.dimensions.iteritems():
    o.createDimension(name, len(dim) if not dim.isunlimited() else None)

for name, var_i in i.variables.iteritems():

    if name in ['t_an', 'depth']:
        # create variable
        var_o = o.createVariable(name, var_i.datatype, var_i.dimensions)
        # copy attributes
        var_o.setncatts({k: var_i.getncattr(k) for k in var_i.ncattrs()})
        # copy data
        var_o[:] = var_i[:]

# temp monthly
file = "temperature_monthly_1deg.nc"
i_path = os.path.join(input_path, file)
i = Dataset(i_path, mode='r')
o_path = os.path.join(output_path, file)
if os.path.exists(o_path):
    os.remove(o_path)
o = Dataset(o_path, mode='w')

for name, dim in i.dimensions.iteritems():
    o.createDimension(name, len(dim) if not dim.isunlimited() else None)

for name, var_i in i.variables.iteritems():

    if name in ['t_an', 't_sd', 'lat', 'lon', 'time']:
        # create variable
        var_o = o.createVariable(name, var_i.datatype, var_i.dimensions)
        # copy attributes
        var_o.setncatts({k: var_i.getncattr(k) for k in var_i.ncattrs()})
        # copy data
        var_o[:] = var_i[:]

# sal monthly
file = "salinity_monthly_1deg.nc"
i_path = os.path.join(input_path, file)
i = Dataset(i_path, mode='r')
o_path = os.path.join(output_path, file)
if os.path.exists(o_path):
    os.remove(o_path)
o = Dataset(o_path, mode='w')

for name, dim in i.dimensions.iteritems():
    o.createDimension(name, len(dim) if not dim.isunlimited() else None)

for name, var_i in i.variables.iteritems():

    if name in ['s_an', 's_sd']:
        # create variable
        var_o = o.createVariable(name, var_i.datatype, var_i.dimensions)
        # copy attributes
        var_o.setncatts({k: var_i.getncattr(k) for k in var_i.ncattrs()})
        # copy data
        var_o[:] = var_i[:]

# temp seasonal
file = "temperature_seasonal_1deg.nc"
i_path = os.path.join(input_path, file)
i = Dataset(i_path, mode='r')
o_path = os.path.join(output_path, file)
if os.path.exists(o_path):
    os.remove(o_path)
o = Dataset(o_path, mode='w')

for name, dim in i.dimensions.iteritems():
    o.createDimension(name, len(dim) if not dim.isunlimited() else None)

for name, var_i in i.variables.iteritems():

    if name in ['depth', 'time', 't_an', 't_sd']:
        # create variable
        var_o = o.createVariable(name, var_i.datatype, var_i.dimensions)
        # copy attributes
        var_o.setncatts({k: var_i.getncattr(k) for k in var_i.ncattrs()})
        # copy data
        var_o[:] = var_i[:]

# sal seasonal
file = "salinity_seasonal_1deg.nc"
i_path = os.path.join(input_path, file)
i = Dataset(i_path, mode='r')
o_path = os.path.join(output_path, file)
if os.path.exists(o_path):
    os.remove(o_path)
o = Dataset(o_path, mode='w')

for name, dim in i.dimensions.iteritems():
    o.createDimension(name, len(dim) if not dim.isunlimited() else None)

for name, var_i in i.variables.iteritems():

    if name in ['s_an', 's_sd']:
        # create variable
        var_o = o.createVariable(name, var_i.datatype, var_i.dimensions)
        # copy attributes
        var_o.setncatts({k: var_i.getncattr(k) for k in var_i.ncattrs()})
        # copy data
        var_o[:] = var_i[:]

print(i)
print(o)
