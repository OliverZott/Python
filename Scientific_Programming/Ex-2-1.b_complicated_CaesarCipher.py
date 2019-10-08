""""
Exercise 2.1: Caesar Cipher

ToDO:   - exceptions?
        - input function separate?
        - switch!


Author: Oliver Zott
Date: 02.10.2019
"""


def console_input():

    # method = input("Do you want to 'encrypt' [e] or 'decrypt' [d] ? ")
    method = input("Please press 'e' for encrypt or 'd' for decrypt.")
    if method == "d":
        var = "decrypt"
    elif method == "e":
        var = "encrypt"
    else:
        print("Invalid choice, only 'd' and 'e' accepted!")

    text = input("Please enter text to " + var)
    shift = input("Please enter shift for " + var)

    return text, shift, var


def caesar_cipher():

    text, shift, var = console_input()

    blabla = var


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


def caesar_cipher_decrypt(input, shift):
    sentence_decrypted = ''

    for i in input:
        if i.isupper():
            sentence_decrypted += chr((ord(i) - 65 - shift) % 26 + 65)
        elif i.islower():
            sentence_decrypted += chr((ord(i) - 97 - shift) % 26 + 97)
        else:
            sentence_decrypted += i
    return sentence_decrypted


# -------------------------------------------------------
# Test:

caesar_cipher()

encr = caesar_cipher_encrypt("Hallo Weeeelt", 5)
print(encr)
decr = caesar_cipher_decrypt(encr, 5)
print(decr)
test_str1 = "Pbatenghyngvbaf, lbh unir fhpprrqrq va qrpelcgvat gur fgevat"
print(caesar_cipher_decrypt(test_str1, 13))
