""" Client-Server Example 1

Author: Oliver Zott
Date: 2019-11-11
"""

import socket
import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
date = datetime.datetime.now().strftime("%Y-%m-%d")
date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    s.bind(("", 50000))

    while True:
        data, addr = s.recvfrom(1024)
        print("[{}]-[{}]: {}".format(date_time, addr[0], data.decode()))
finally:
    s.close()
