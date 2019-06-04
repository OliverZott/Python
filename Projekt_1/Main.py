'''
Main-Function for data-logging

TODO:   - add relative paths instead full
        - path as argument
        - makedir for each day/month/year

Created on 04.06.2019
@author: Oliver Zott
'''


import DataLogging
from DataLogging.file_io import dateANDtime
import MeasurementPlot

import datetime
import time



# =================================================================================================
# Call Data Logging
# =================================================================================================


# string from serial port
data_string = DataLogging.serial_open()


# formated data string with 
values_string=  DataLogging.values_re(data_string)
value_temp = DataLogging.values_re(data_string)[0]
value_hum = DataLogging.values_re(data_string)[1]
value_lux = DataLogging.values_re(data_string)[2]


# store measurement values to file
DataLogging.file_io(value_temp, value_hum, value_lux)


# Current Time and vale for sleep-time (conversion str ->  int)
t_s = int(dateANDtime[0])                               
t_m = int(dateANDtime[1])
t_h = int(dateANDtime[2])
t_sleep = int(dateANDtime[3])

#file_name = DataLogging.filename()

# Loop for measurement
print("Loop for data-logging starts...")

while True:
	t_s = datetime.datetime.now().second
	t_h = datetime.datetime.now().hour
	t_m = datetime.datetime.now().minute
	if 6 <= t_h <= 23 and t_s == 57:
		DataLogging.file_io(value_temp, value_hum, value_lux)
		time.sleep(40)
    elif t_h > 23:
        print("Creating plot")
        MeasurementPlot.proj_plot(file_name)
        continue   