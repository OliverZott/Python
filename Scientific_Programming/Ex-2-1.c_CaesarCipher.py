""""
Exercise 02-01 c)

Author: Group 1
Date: 10.10.2019
"""


# -------------------------------------------------------
# Exercise 02-01 c)
def caesar_cipher_encrypt(input_text, shift):
    """ Function to encrypt a given sentence. """

    sentence_encrypted = ''

    for i in input_text:
        if i.isupper():
            sentence_encrypted += chr((ord(i) - 65 + shift) % 26 + 65)
        elif i.islower():
            sentence_encrypted += chr((ord(i) - 97 + shift) % 26 + 97)
        else:
            sentence_encrypted += i
    return sentence_encrypted


def caesar_cipher_decrypt():
    """
    Function to decrypt a sentence which is given by input.
    A brute force method (iteration over alphabet) is used to find the unknown encryption-key.
    """

    input_text = input("Please enter text to decrypt.")

    for j in range(0, 26, 1):
        sentence_decrypted = ''
        for i in input_text:
            if i.isupper():
                sentence_decrypted += chr((ord(i) - 65 - j) % 26 + 65)
            elif i.islower():
                sentence_decrypted += chr((ord(i) - 97 - j) % 26 + 97)
            else:
                sentence_decrypted += i
        print(j)
        print(sentence_decrypted + "\n")


# -------------------------------------------------------
# Test:

# Gwc uivioml bw nqvl bpm zqopb apqnb
caesar_cipher_decrypt()
