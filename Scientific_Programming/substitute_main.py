"""
Main function for substitute-cipher implementation

Author: Group 1
Version: 1.0
Date: 08.10.2019
"""

from util import input
from util.cipher import cipher


def run():

    text, method, seed = input.input_function()
    print(cipher(text, method, seed))

    print(__name__)


if __name__ == "__main__":
    run()
