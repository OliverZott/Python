#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 02-02

Author: Group 1
Date: 10.10.2019
"""

# -----------------------------------------------------------------------------
# library import
import random


# -----------------------------------------------------------------------------
# definition of functions


# now we define a function that asks for the inputs and returns sentence, method and seed
def input_function():
    """ Function for terminal user input. """
    sentence = input("Please enter a sentence: ")
    method = input("Please enter 'e' for encryption or 'd' for decryption: ")
    seed = input("Please enter a seed (integer value): ")
    return sentence, method, seed


# now we define a function that encrypts/decrypts the sentence and returns an encrypted/decrypted sentence
def cipher(sentence, method, seed):
    """ Function to decrypt / encrypt, based on user input. """
    alphabet = list(r"""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ [\]^_`abcdefghijklmnopqrstuvwxyz{|}~""")
    
    # this provides a 'key' to make the random function work in the same way on every computer
    random.seed(seed)

    # need copy, variable assignment wont work because of reference
    alphabet_shuffle = alphabet[:]
    random.shuffle(alphabet_shuffle)

    # this condition decides whether the function should encrypt or decrypt
    if method == 'e':
        dict_cipher = dict(zip(alphabet, alphabet_shuffle))    
    elif method == 'd':
        dict_cipher = dict(zip(alphabet_shuffle, alphabet))
    
    # initialize output (new sentence) and adds every single encrypted/decrypted character to the output            
    sentence_new = ""
    for char in sentence:
        sentence_new += dict_cipher[char]
    
    return sentence_new


# -----------------------------------------------------------------------------
# script execution:
sentence, method, seed = input_function()
sentence_new = cipher(sentence, method, seed)
print(sentence_new)