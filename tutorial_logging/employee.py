"""
Logging example

Instead of root-logger, a more specific logger is uses

Run employee.py directly or program.py
"""
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s:%(name)s:%(levelname)s: %(message)s')

file_handler = logging.FileHandler('./employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# Configuring ROOT - logger  !!!
# logging.basicConfig(filename=f"./employee.log", level=logging.INFO,
#                     format='%(asctime)s: %(name)s:%(levelname)s: %(message)s')


class Employee:

    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last
        logger.info(
            'Inside constructor: creating employee: "{}"'.format(self.full_name))

    @property
    def full_name(self):
        return '{}, {}'.format(self.last, self.first)

    @property
    def email(self):
        return '{}.{}@mail.com'.format(self.first, self.last)


emp1 = Employee("Jane", "Doe")
