'''
Main-Function for data-logging

TODO:   - add relative paths instead full
        - path as argument
        - makedir for each day/month/year

Created on 04.06.2019
@author: Oliver Zott
'''


import DataLogging
#from DataLogging.file_io import dateTimeSleep
import MeasurementPlot

import datetime
import time
from DataLogging import serial_port

'''
# TESTS
serial_port.check_port()
print(serial_port.serial_open_rec())
data_str = serial_port.serial_open_rec()
val = serial_port.values_rec(data_str)
temp = val[0]
hum = val[1]
lux = val[2]

print(temp + ", " + hum + ", " + lux)
'''




# =================================================================================================
# Call Data Logging
# =================================================================================================
# Loop for measurement
print("Loop for data-logging starts...")

while True:
    t_s = datetime.datetime.now().second
    t_h = datetime.datetime.now().hour
    t_m = datetime.datetime.now().minute
    if 6 <= t_h <=21 and t_s == 59:
        data_string = serial_port.serial_open_rec()
        values_string =  serial_port.values_rec(data_string)
        value_temp = values_string[0]
        value_hum = values_string[1]
        value_lux = values_string[2]
        DataLogging.file_io(value_temp, value_hum, value_lux)
        print("Plot values")
        filename = DataLogging.filename()
        MeasurementPlot.proj_plot(filename)
        time.sleep(40)
        continue
    elif t_h == 22 and t_m == 10: 
    #else:
        print("Plot values")
        filename = DataLogging.filename()
        MeasurementPlot.proj_plot(filename)
        print("Loop for data-logging starts...")
        time.sleep(50)
        #time.sleep(3550)
        continue




'''
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
          
'''