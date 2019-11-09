"""
Exercise 3: Download Data

ToDo:   - Exception handling
        -
        - how to check if DL ongoing or finished ???
        - urllib OR request ???
        - import ir in sub-folder in PyCharm --> .util

Example: - file_dl(10, 45)


Author: Oliver Zott
Date: 16.10.2019
"""


import os
import urllib.request
import sys


def file_dl():

    longitude = int(sys.argv[1])
    latitude = int(sys.argv[2])

    link, file_name = convert_input(longitude, latitude)

    if check_existence(file_name):
        raise Exception(f"File '{file_name}' already exists")

    cwd = os.getcwd()
    if check_directory(cwd):
        urllib.request.urlretrieve(link, file_name)
        print(f"Done saving file '{file_name}' to directory {cwd}.")
    else:
        raise Exception(f"Location '{cwd}' not valid! ")


def convert_input(lon, lat):

    longitude = lon - lon % 5
    latitude = lat - lat % 5

    file_ending = "srtm_"
    link_base = "http://srtm.csi.cgiar.org/wp-content/uploads/files/srtm_5x5/TIFF/"

    # dictionary for longitude value-assignment
    long_key_gen = (i * 5 for i in range(-36, 37, 1))
    long_key = list(long_key_gen)
    long_val_gen = (i for i in range(1, len(long_key), 1))  # generator
    long_val = list(long_val_gen)
    long_dict = dict(zip(long_key, long_val))

    # dictionary for latitude value-assignment
    lat_key_gen = (i * -5 for i in range(-12, 14, 1))
    lat_key = list(lat_key_gen)
    lat_val_gen = (i for i in range(1, len(lat_key), 1))  # generator
    lat_val = list(lat_val_gen)
    lat_dict = dict(zip(lat_key, lat_val))

    # print(long_dict)
    # print(lat_dict)

    latitude_val = lat_dict[latitude]
    longitude_val = long_dict[longitude]

    if longitude_val < 10:
        file_ending += "0" + str(longitude_val) + "_"
    else:
        file_ending += str(longitude_val) + "_"

    if latitude_val < 10:
        file_ending += "0" + str(latitude_val)
    else:
        file_ending += str(latitude_val)

    link = link_base + file_ending + ".zip"

    # print(link)

    return link, file_ending + ".zip"


def check_directory(cwd):
    return os.access(cwd, os.F_OK or os.X_OK or os.R_OK | os.W_OK)   # also possible use |  ???


def check_existence(file_name):
    return os.path.isfile(file_name)


if __name__ == "__main__":
    file_dl()

# ---------------------------------------------------------
# test

# convert_input(10, 45)
# convert_input(-180, 60)

# file_dl(10, 45)
