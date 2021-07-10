from contextlib import contextmanager


# decorator returns the generator wrapped by the GeneratorContextManager object
@contextmanager
def open_file(file: str, mode: str) -> None:
    try:
        f = open(file, mode)
        yield f
    finally:            # all before yield is equivalent to '__enter__'
        f.close()       # equivalent to '__exit__'


if __name__ == "__main__":
    with open_file('func_test.txt', 'w') as f:
        f.write('test')

    print(f.closed)
