import logging

logging.basicConfig(filename="employee.log", level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Employee:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
        logging.info(
            'Inside constructor: creating employee: "{}"'.format(self.full_name))

    @property
    def full_name(self):
        return '{}, {}'.format(self.last, self.first)

    @property
    def email(self):
        return '{}.{}@mail.com'.format(self.first, self.last)
