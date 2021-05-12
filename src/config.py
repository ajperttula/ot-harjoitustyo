import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "scores.db"
BG_COLOR = os.getenv("BG_COLOR") or "#EBEBEB"
TEXT_COLOR = os.getenv("TEXT_COLOR") or "#000000"
BUTTON_COLOR = os.getenv("BUTTON_COLOR") or "#FF0000"
GRID_COLOR = os.getenv("GRID_COLOR") or "#7D7D7D"
BLOCK_COLOR_1 = os.getenv("BLOCK_COLOR_1") or "#FF0000"
BLOCK_COLOR_2 = os.getenv("BLOCK_COLOR_2") or "#00FF00"
BLOCK_COLOR_3 = os.getenv("BLOCK_COLOR_3") or "#0000FF"
SCREEN_WIDTH = 430
SCREEN_HEIGHT = 540
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 25
CORNER = 20
