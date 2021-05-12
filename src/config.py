import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass


def check(color: str):
    """Checks that color code from .env file is valid.

    Args:
        color (str): color in hex-format.

    Returns:
        (None/str): None if not valid, color if valid
    """
    if not color:
        return None
    values = "0123456789ABCDEFabcdef"
    if len(color) != 7 or color[0] != "#":
        return None
    for char in color[1:]:
        if char not in values:
            return None
    return color


DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "scores.db"
BG_COLOR = check(os.getenv("BG_COLOR")) or "#EBEBEB"
TEXT_COLOR = check(os.getenv("TEXT_COLOR")) or "#000000"
BUTTON_COLOR = check(os.getenv("BUTTON_COLOR")) or "#FF0000"
GRID_COLOR = check(os.getenv("GRID_COLOR")) or "#7D7D7D"
BLOCK_COLOR_1 = check(os.getenv("BLOCK_COLOR_1")) or "#FF0000"
BLOCK_COLOR_2 = check(os.getenv("BLOCK_COLOR_2")) or "#00FF00"
BLOCK_COLOR_3 = check(os.getenv("BLOCK_COLOR_3")) or "#0000FF"
SCREEN_WIDTH = 430
SCREEN_HEIGHT = 540
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 25
CORNER = 20
