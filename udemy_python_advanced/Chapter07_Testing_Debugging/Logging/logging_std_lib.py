"""
Log Levels:

DEBUG: Detailed debug infos
INFO: Things working as intended
WARNING: Unexpected stuff happened
ERROR: Program cannot perfom some function
CRITICAL: Program crashes
"""

import logging
from datetime import date
from pathlib import Path
from typing import Union

# Setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Formater (optional), FileHandler
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(funcName)s:%(message)s")
file_path = Path(__file__).parent.joinpath(f"{date.today()}_stdlib.log")

file_handler = logging.FileHandler(file_path)
file_handler.setLevel(logging.DEBUG)  # if here ERROR ---> overrules loglevel from above (always the smallest log level is taken!!!)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def devide_integers(a: int, b: int) -> Union[None, float]:
    logger.info("info-log: gonna devide some integers...")
    try:
        logger.debug(f"debug-log: a={a}, b={b}")
        result = a / b
        return result
    except ZeroDivisionError as e:
        logger.exception(f"error-log: {e}")  # log-level ERROR
        return None


def main() -> None:
    for i in range(3):
        print(devide_integers(10, i))


if __name__ == "__main__":
    main()
