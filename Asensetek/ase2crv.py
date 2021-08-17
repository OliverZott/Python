"""
Converting Asensetek lighting Passport Pro .txt file to crv file

Arguments: Asensetek input file
Arguments (optional): output file

Author:     Oliver Zott
Date:       25.07.2019
"""

import re
import argparse
import numpy as np
import crv.io
import os


def ase2crv(file: str, outfile: str):
    try:
        with open(file, "r", encoding="utf-8") as f:
            raw_str = f.read()
    except IOError as e:
        print("I/O error({0}): {1} - {2}".format(e.errno, e.strerror,
                                                 e.filename))

    # separate values using regex
    data_front = re.split(r'"spectrumPoints":\[', raw_str)  # split at front
    data_end = re.split(r'\],"radarPoints', data_front[1])  # split at end
    data = data_end[0]
    data_list = re.split(',', data)

    # create numpy array
    arr = np.zeros((401, 2))

    # write values np.array

    for i, elem in enumerate(data_list):
        val = re.findall("\d+\.*\d*", elem[7:])
        arr[i] = [380 + i, val[0]]

    crv.io.write(outfile, arr,
                 info="created using 'ase2crv' from original file: " + file)


def main():
    parser = argparse.ArgumentParser(prog='ase2crv',
                                     description='Converts Asensetek '
                                     'LightingPassport .txt files to .crv '
                                     'files.')

    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s 1.0')

    parser.add_argument("infile",
                        metavar="Input_file",
                        help='Set input file.')

    parser.add_argument("-o", "--outfile",
                        action="store",
                        dest="outfile",
                        default=None,
                        help="Define output file name.")

    args = parser.parse_args()

    # check  optional outfile ending
    outfile = args.outfile
    if not outfile:
        pre, ext = os.path.splitext(args.infile)
        outfile = pre + '.crv'
    elif not outfile[-4:] == '.crv':
        pre, ext = os.path.splitext(args.outfile)
        outfile = pre + '.crv'
    print('Convert input file to: ' + outfile)

    ase2crv(args.infile, outfile)


if __name__ == '__main__':
    main()
