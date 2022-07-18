"""
Exercise 3: Download Data

urllib
https://docs.python.org/3/library/urllib.html#module-urllib

request
https://realpython.com/python-requests/#the-get-request

progressbar
https://stackoverflow.com/questions/37748105/how-to-use-progressbar-module-with-urlretrieve
https://mail.python.org/pipermail/python-list/2008-January/509830.html


ToDo:   - Exception handling
        - modularisation
        - how to check if DL ongoing or finished ???
        - urllib OR request ???
        - import ir in sub-folder in PyCharm --> .util

Example:    - file_dl(10, 45)
            - python Ex-3-1_DataDL.py 9 44 11 44
            - python Ex-3-1_DataDL.py 9 44 11 49

Author: Oliver Zott
Date: 20.10.2019
"""


import os
import urllib.request
import sys


def file_dl():

    if len(sys.argv) == 3:
        file_single()
    elif len(sys.argv) == 5:
        file_range()


def download(longitude, latitude):

    link, file_name = convert_input(longitude, latitude)

    """
    if check_existence(file_name):
        raise Exception(f"File '{file_name}' already exists")
    """

    cwd = os.getcwd()
    if check_directory(cwd):
        if check_existence(file_name):
            print(f"File '{file_name}' already exists. Continuing...")
        else:
            urllib.request.urlretrieve(link, file_name)
            print(f"Done saving file '{file_name}' to directory {cwd}.")
            print("File size(byte): ", file_size(file_name))
    else:
        raise Exception(f"Location '{cwd}' not valid! ")


def file_single():

    longitude = int(sys.argv[1])
    latitude = int(sys.argv[2])

    download(longitude, latitude)


def file_range():

    lon1 = int(sys.argv[1])
    lon2 = int(sys.argv[3])
    lat1 = int(sys.argv[2])
    lat2 = int(sys.argv[4])
    lon_lower_boundary = lon1 - lon1 % 5
    lon_upper_boundary = lon2 - lon2 % 5
    lat_lower_boundary = lat1 - lat1 % 5
    lat_upper_boundary = lat2 - lat2 % 5

    num_lon = (lon_upper_boundary - lon_lower_boundary) / 5 + 1
    num_lat = (lat_upper_boundary - lat_lower_boundary) / 5 + 1
    num_tiles = num_lat * num_lon

    # check user input for arbitrary amount of files
    choice = input(f"You have got {num_tiles} files to download. Press 'c' to continue!")
    if choice in ("c", "C"):

        # begin with lower boundary of lon adn lat
        download(lon_lower_boundary, lat_lower_boundary)

        # keep adding up till upper boundary reached
        lon = lon_lower_boundary
        lat = lat_lower_boundary
        while lon <= lon_upper_boundary:
            lon += 5
            while lat <= lat_upper_boundary:
                lat += 5
                download(lon, lat)
    else:
        print("bye bye!")


"""
def file_dl_var():
    num_args = len(sys.argv)

    list_a = []
    list_b = []
    for i in range(1, num_args, 1):
        if i % 2:
            list_a.append(sys.argv[i])
        else:
            list_b.append(sys.argv[i])

    argv_list = list(zip(list_a, list_b))

    for arg_tuple in argv_list:
        longitude = arg_tuple[0]
        latitude = arg_tuple[1]
        file_dl(longitude, latitude)
"""


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


def file_size(file_name):
    # stat_info = os.stat('file_name')
    # stat_info.st_size

    size = os.path.getsize(file_name)

    return size


if __name__ == "__main__":
    file_dl()
    download(9, 46)

# ---------------------------------------------------------
# test

# convert_input(10, 45)
# convert_input(-180, 60)

# file_dl(10, 45)
