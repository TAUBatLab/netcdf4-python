# init for netCDF4 package
# Docstring comes from extension module _netCDF4
from ._netCDF4 import *
# Need explicit imports for names beginning with underscores
from ._netCDF4 import __doc__
from ._netCDF4 import (__version__, __netcdf4libversion__, __hdf5libversion__,
                       __has_rename_grp__, __has_nc_inq_path__,
                       __has_nc_inq_format_extended__)
__all__ =\
['Dataset','Variable','Dimension','Group','MFDataset','MFTime','CompoundType','VLType','date2num','num2date','date2index','stringtochar','chartostring','stringtoarr','getlibversion']
__pdoc__={}
__pdoc__['Dataset.path'] = \
"""The `path` attribute shows the location of the `netCDF4.Group` in
the `netCDF4.Dataset` in a unix directory format (the names of groups in the
hierarchy separated by backslashes). A `netCDF4.Dataset` instance is the root
group, so the path is simply `'/'`."""
