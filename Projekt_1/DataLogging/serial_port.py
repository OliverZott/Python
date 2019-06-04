''' 
serial_port:    - open serial_port
                - use reg_ex to save data in str

TODO:           - Automation of port recognition 

@Date 04.06.2019
@author: Oliver Zott
'''

import serial               # for serial port communication 
import re                   # for regular expressions



# Check port if necessary
'''
port = serial.Serial()
print ("Port:", port);
#print ("Type port:info: ", type(port))
'''



# open port and decode/save data in string
def serial_open():
    port = serial.Serial()
    port.baudrate = 9600
    port.port = 'COM6'
    port.open()
    port_out = port.read(75)  #(72 min)
    
    # Decode byte stream (byte --> str)
    data_str = port_out.decode("utf-8","replace")
 
    return data_str



# store data in string with specific format
# Bem: statt in C umzusetzen hier allgemein gehalten (für beliebeige data_str möglich!!!
def values_re(data_str):
    temp_re = re.search(r"\d*\s\*C", data_str).group(0)             # group(0), for str (<class 're.Match'>)
    temp = temp_re.rstrip(" *C")

    hum_re = re.search(r"\d*\s\%", data_str).group(0)
    hum = hum_re.rstrip(" %")

    lux_re = re.search(r"\d*\.", data_str).group(0)                 # Error if used:  r"\d*\.\d*\slux" 
    lux = lux_re.rstrip(".")
    
    return temp, hum, lux
    