"""
Main-Function for data-logging

TODO:   - add relative paths instead full
        - path as argument
        - makedir for each day/month/year
        - date/time in detached script !!!  --> import filename 
        - file name in detached script !!! --> import timeANDshit

Created on 04.06.2019
@author: Oliver Zott
"""


import DataLogging
import MeasurementPlot
import datetime
import time

# Loop for measurement
print("Loop for data-logging starts...")

while True:
    t_s = datetime.datetime.now().second
    t_h = datetime.datetime.now().hour
    t_m = datetime.datetime.now().minute
    if 6 <= t_h <= 21 and t_s == 59:
        data_string = DataLogging.serial_open_rec()
        values_string = DataLogging.values_rec(data_string)
        value_temp = DataLogging.values_rec(data_string)[0]
        value_hum = DataLogging.values_rec(data_string)[1]
        value_lux = DataLogging.values_rec(data_string)[2]
        DataLogging.file_io(value_temp, value_hum, value_lux)
        time.sleep(40)
        continue
    elif t_h == 22 and t_m == 10:  # t_h == 20 and
        print("Plot values")
        filename = DataLogging.filename()
        MeasurementPlot.proj_plot(filename)
        print("Loop for data-logging starts...")
        time.sleep(50)  # 3550
        continue
