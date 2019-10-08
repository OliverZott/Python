"""
Main function for substitute-cipher implementation

Author: Group 1
Version: 1.0
Date: 08.10.2019
"""

from util import input_func
from util.cipher_func import cipher


def main():

    text, method, seed = input_func.input_function()
    print(cipher(text, method, seed))

    '''
    print(__name__)
    '''


if __name__ == "__main__":
    main()
