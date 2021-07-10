import os
from contextlib import contextmanager


# example situation
# cwd = os.getcwd()
# os.chdir('sample_dir_one')
# print(os.listdir())
# os.chdir(cwd)


@contextmanager
def change_dir(directory: str) -> None:
    try:
        cwd = os.getcwd()
        os.chdir(directory)
        yield
    except:
        print("Directory '{}'does not exist!".format(directory))
    finally:
        os.chdir()


if __name__ == "__main__":

    change_dir('blub')

    with change_dir('blub'):
        print(os.listdir())
