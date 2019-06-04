''' 
file_io:        - Store measured values to file (.txt)
                - Time Stamp & Header

TODO:           - combine filename() / file_io

@Date 04.06.2019
@author: Oliver Zott
'''

import datetime
import time
import os



# create header for file
file_headder = "Timestamp;Temperature;Humidity;Illuminance\n"

#path = r'C:\Users\Dura\eclipse-workspace\Python\Projekt_1\Messwerte'   
#f_name = "Messwerte_"  + date +".txt"
#file_name = os.path.join(path, f_name) 

# write data to file
def file_io (temp, hum, lux):
# get time for time stamp
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    dateANDtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # file name 
    path = r'C:\Users\Dura\eclipse-workspace\Python\Projekt_1\Messwerte'   
    #file_name = "Messwerte_"  + date +".txt"
    f_name = "Messwerte_"  + date +".txt"
    file_name = os.path.join(path, f_name) 
    
    
    measurement = dateANDtime + ";" + temp + ";" +  hum + ";" + lux + "\n"
    #file_name = "Messwerte_"  + date +".txt"
    file = open(file_name, "a")
    
    
    
    if file.tell() == 0:                        # check if new file and write header in case
        file.write(file_headder)
    
    file.write(measurement)
    file.close()
 
    return file_name
    
    
def filename():
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    path = r'C:\Users\Dura\eclipse-workspace\Python\Projekt_1\Messwerte' 
    f_name = "Messwerte_"  + date +".txt"
    file_name = os.path.join(path, f_name)
    
    return file_name 
    
    
def dateTimeSleep():
    t_s = datetime.datetime.now().second
    t_m = datetime.datetime.now().minute    
    t_h = datetime.datetime.now().hour
    t_sleep = time.sleep(40)
   
     
    return t_s, t_m, t_h, t_sleep