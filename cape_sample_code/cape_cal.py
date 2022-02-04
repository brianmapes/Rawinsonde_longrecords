import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import array as arr
from collections import OrderedDict
import seaborn as sns
from matplotlib.widgets import Slider
import datetime as dt
from netCDF4 import date2num,num2date
from dateutil import rrule
from datetime import datetime
import pandas as pd
import datetime
from scipy import stats
import glob 
import errno
import os
import csv
import functools
import operator
import metpy.calc as mpcalc
from metpy.units import units
import metpy
#######################################
os.chdir('/home/sree/cape_mapes_test/')

missing_values=[-999]

missing_value_formats = [-999,"?","NA","n/a", "na", "--"]

#================================reading individual files and variables
f1 = []

f1= [pd.read_csv(file,delimiter=',',
               na_values = missing_value_formats) for file in glob.glob(os.path.join("*432*.txt"))]

pressure = []

temperature=[]

dewpoint=[]

parcel_temp=[]

for i in range(int(len(f1))):

    pressure.append(f1[i].iloc[:,0].tolist())

    temperature.append(f1[i].iloc[:,2].tolist())

    dewpoint.append(f1[i].iloc[:,3].tolist())

#================================CAPE calculation

cape=[]

for i in range(0,10):
  cape.append(metpy.calc.surface_based_cape_cin(pressure[i]* units.hPa, temperature[i]* units.degC,dewpoint[i]* units.degC))

cape_val=(list(zip(*cape))[0])


cape_list=list(cape_val)


test_list=[]

for i in cape_list :
    test_list.append(i)

d=np.array(test_list, dtype=object)

tst=[]

my_df = pd.DataFrame(d)

my_df.to_csv('cape_sample.txt', index=False, header=False)

#======================================