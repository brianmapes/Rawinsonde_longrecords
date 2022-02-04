#Code for downloading sonde data from Wyoming at Mangalore station

import datetime 
import os
from metpy.units import units
from siphon.simplewebservice.wyoming import WyomingUpperAir


os.chdir('/home/sree/Documents/back_up_june9_2021/MRR/0_isotherm')
#  Set the download window （ Here is UTC moment ）
start = datetime.datetime(2010, 6, 1, 0)
end = datetime.datetime(2010, 9, 30, 0)

datelist = []
while start<=end:
    datelist.append(start)
    start+=datetime.timedelta(hours=12)

#  Select the download site （ Take Beijing for example ）
stationlist = ['43285']

#  Bulk download 
for station in stationlist:
    for date in datelist:
        try:
            df = WyomingUpperAir.request_data(date, station)
            df.to_csv(station+'_'+date.strftime('%Y%m%d%H')+'.txt',index=False)
            print(f'{date.strftime("%Y%m%d_%H")} Download successful ')
        except Exception as e:
            print(f'{date.strftime("%Y%m%d_%H")} Download failed : {e}')
            pass
