""""
Exercise 2.1: Caesar Cipher

ToDO:   - exceptions?
        - input function separate?
        - switch!


Author: Oliver Zott
Date: 02.10.2019
"""


def caesar_cipher_encrypt(input_text, shift):

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

    input_text = input("Please enter text to encrypt.")
    shift = int(input("Please enter shift-value."))

    sentence_decrypted = ''

    for i in input_text:
        if i.isupper():
            sentence_decrypted += chr((ord(i) - 65 - shift) % 26 + 65)
        elif i.islower():
            sentence_decrypted += chr((ord(i) - 97 - shift) % 26 + 97)
        else:
            sentence_decrypted += i
    return sentence_decrypted


# -------------------------------------------------------
# Test:
encr = caesar_cipher_encrypt("Hallo Weeeelt", 5)
print(encr)

print(caesar_cipher_decrypt())
