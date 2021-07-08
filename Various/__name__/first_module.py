print("Firs modules name:  {}".format(__name__))


def main():
    """Method should just be called if module is run directly"""
    print("Inside 'main-method' of 'first module'")


if __name__ == "__main__":
    main()
else:
    print("First module run from import.")
