from employee import Employee
from log_sample import divide
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s:%(name)s:%(levelname)s: %(message)s')

# logging to the same log file as employee!!!
file_handler = logging.FileHandler('./program.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def main():
    logger.debug("Inside program.py MAIN!")
    emp1 = Employee("Oliver", "Zott")
    emp1 = Employee("John", "Smith")

    divide(2, 0)


if __name__ == "__main__":
    main()
