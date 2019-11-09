
def f2c(tf):
    """Converts degree to   Fahrenheit"""
    if tf < -459.67:
        raise ValueError("Input value below absolute zero!")
    r = (tf - 32 ) * 5/9
    return r


if __name__ == "__main__":
    print(f2c(24))
