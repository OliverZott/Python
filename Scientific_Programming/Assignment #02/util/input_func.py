"""
Input function

https://docs.python.org/3/library/functions.html?highlight=int#int

"""


def input_function():

    input_text = input("Please enter text to encrypt // decrypt.")

    while True:
        try:
            seed = int(input("Please enter seed (integer value)."))
        except ValueError as e:
            print("Error... pleas enter integer value. {}".format(e))
            continue
        break

    method = input("Please press 'e' for encrypt or 'd' for decrypt.")
    while method != 'd' and method != 'e':
        print("Error... only 'e' and 'd' allowed")
        method = input("Please press 'e' for encrypt or 'd' for decrypt.")

    return input_text, method, seed


if __name__ == "__main__":
    pass