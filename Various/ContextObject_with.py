"""
Context Objects: 'with'

Author: Oliver Zott
Date: 20.09.2019
"""

# imports for example 3
import contextlib
import time


# -------------------------------------------------------
# Example 1 (page 435)
def read_classic():

    f = open("test.txt", "r")

    try:
        print(f.read())
    finally:
        f.close()


def read_with():

    with open("test.txt", "r") as f:
        print(f.read())


# -------------------------------------------------------
# Example 2 (page 436)

class MyLogfile:

    def __init__(self, logfile):
        self.logfile = logfile
        self.f = None

    def entry(self, text):
        self.f.write("==> {}\n".format(text))

    def __enter__(self):
        self.f = open(self.logfile, "w")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


# -------------------------------------------------------
# Example 3 (page 438)

@contextlib.contextmanager
def laufzeit():
    """
    - Parameter-less function with contextmanager decorated.
    - Now it has to return Generator with one element!
    - This is accomplished by 'yield' ... now function body can be seen as
      separated in 2 parts
    - Part before 'yield' is like __enter__, part after is like __exit__

    --> Program can be used to measure runtime
    """

    start = time.perf_counter()
    try:
        yield
    finally:
        print("Laufzeit: {:.2f}  s".format(time.perf_counter() - start))


# -------------------------------------------------------
# Test: MAIN
if __name__ == "__main__":

    # Example 3
    with laufzeit():
        x = 0
        for i in range(6000000):
            x += (-1)**i * i

    # Example 2
    with MyLogfile("logfile.txt") as log:
        log.entry("TITLE")
        log.entry("Hello Zwugu")

    '''
    print("Call 'read_classic': ")
    read_classic()
    print()

    print("Call 'read_with': ")
    read_with()
    '''
