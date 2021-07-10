"""
Using class for context manager
https://www.youtube.com/watch?v=-aKFBoZpiqA
"""
from datetime import datetime


class Open_File():

    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)

        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close


if __name__ == "__main__":
    with Open_File('test.txt', 'w') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        string: str = 'Test - ' + timestamp
        f.write(string)
