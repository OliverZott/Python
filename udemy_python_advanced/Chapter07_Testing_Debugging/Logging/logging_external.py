"""
Log Levels:

DEBUG: Detailed debug infos
INFO: Things working as intended
WARNING: Unexpected stuff happened
ERROR: Program cannot perfom some function
CRITICAL: Program crashes
"""


import sys
from datetime import date
from pathlib import Path
from typing import Union

from loguru import logger  # https://github.com/Delgan/loguru

# Setup logger
filepath = Path(__file__).parent.joinpath(f"{date.today()}_loguru.log")

logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")
logger.add(filepath, format="{time} : {level} : {message}", level="DEBUG", rotation="1 days")


# Decorator for exception-catching
@logger.catch
def devide_integers(a: int, b: int) -> Union[None, float]:
    logger.info("info-log: gonna devide some integers...")
    logger.debug(f"debug-log: a={a}, b={b}")
    result = a / b
    return result


def main() -> None:
    for i in range(3):
        print(devide_integers(10, i))


if __name__ == "__main__":
    main()
