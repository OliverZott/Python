'''
Main-Function for data-logging

TODO:   - add relative paths instead full
        - path as argument
        - makedir for each day/month/year

Created on 04.06.2019
@author: Oliver Zott
'''


import DataLogging
from DataLogging.file_io import dateTimeSleep
import MeasurementPlot

import datetime
import time

# Loop for measurement
print("Loop for data-logging starts...")

while True:
    t_s = datetime.datetime.now().second
    t_h = datetime.datetime.now().hour
    t_m = datetime.datetime.now().minute
    if 0 <= t_m <= 30 and t_s == 57:
        data_string = DataLogging.serial_open()
        values_string=  DataLogging.values_re(data_string)
        value_temp = DataLogging.values_re(data_string)[0]
        value_hum = DataLogging.values_re(data_string)[1]
        value_lux = DataLogging.values_re(data_string)[2]
        DataLogging.file_io(value_temp, value_hum, value_lux)
        time.sleep(40)
        continue
    elif t_m > 30:
        print("Plot values")
        filename = DataLogging.filename()
        MeasurementPlot.proj_plot(filename)
        time.sleep(40)
        continue