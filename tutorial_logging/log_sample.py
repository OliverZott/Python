import logging


logging.basicConfig(filename='./log.txt', level=logging.DEBUG,
                    format='%(asctime)s: %(levelname)s: %(message)s')



def add(x, y):
    """Add function"""
    return x+y


def subtract(x, y):
    """Substract function"""
    return x-y


def multiply(x, y):
    """Multiply function"""
    return x*y


def divide(x, y):
    """Divide function"""
    return x/y


num1 = 2
num2 = 5

add_result = add(num1, num2)
logging.info('{} + {} = {}'.format(num1, num2, add_result))

sub_result = subtract(num1, num2)
logging.debug('{} + {} = {}'.format(num1, num2, add_result))

mul_result = multiply(num1, num2)
logging.warning('{} + {} = {}'.format(num1, num2, add_result))

div_result = divide(num1, num2)
logging.error('{} + {} = {}'.format(num1, num2, add_result))
