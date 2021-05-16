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
        color (str): color in hex-format

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
BG_COLOR = check(os.getenv("BG_COLOR")) or "#BFDBF7"
TEXT_COLOR = check(os.getenv("TEXT_COLOR")) or "#022B3A"
BUTTON_COLOR = check(os.getenv("BUTTON_COLOR")) or "#1F7A8C"
GRID_BG_COLOR = check(os.getenv("GRID_BG_COLOR")) or "#FCFCFC"
GRID_COLOR = check(os.getenv("GRID_COLOR")) or "#E1E5F2"
BLOCK_COLOR_1 = check(os.getenv("BLOCK_COLOR_1")) or "#F94144"
BLOCK_COLOR_2 = check(os.getenv("BLOCK_COLOR_2")) or "#F3722C"
BLOCK_COLOR_3 = check(os.getenv("BLOCK_COLOR_3")) or "#90BE6D"
BLOCK_COLOR_4 = check(os.getenv("BLOCK_COLOR_4")) or "#277DA1"
BLOCK_COLOR_5 = check(os.getenv("BLOCK_COLOR_5")) or "#577590"
BLOCK_COLOR_6 = check(os.getenv("BLOCK_COLOR_6")) or "#F9C74F"
BLOCK_COLORS = [BLOCK_COLOR_1, BLOCK_COLOR_2, BLOCK_COLOR_3,
                BLOCK_COLOR_4, BLOCK_COLOR_5, BLOCK_COLOR_6]
SCREEN_WIDTH = 430
SCREEN_HEIGHT = 540
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 25
CORNER = 20
