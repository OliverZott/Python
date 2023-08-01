import os

from dotenv import load_dotenv

load_dotenv()

DATA_BASE_PATH = str(os.getenv("DATA_BASE_PATH"))
IMAGE_BASE_PATH = str(os.getenv("IMAGE_BASE_PATH"))


def get_filepath(filename: str) -> str:
    return os.path.join(DATA_BASE_PATH, filename)


def get_imagepath(imagename: str) -> str:
    return os.path.join(IMAGE_BASE_PATH, imagename)
