import pygame
from block import Block
from level import Level
from grid import Grid
from clock import Clock
from event import Event
from render import Render
from pace import Pace
from gameloop import GameLoop

CELL_SIZE = 25
CORNER = 20
GRID_HEIGHT = 20
GRID_WIDTH = 10
SCREEN_HEIGHT = 550
SCREEN_WIDTH = 400
BKGD_COLOR = (255, 255, 255)


def main():
    pygame.init()

    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TETRIS")

    block = Block()
    grid = Grid(GRID_WIDTH, GRID_HEIGHT)
    level = Level(block, grid)
    clock = Clock()
    event_queue = Event()
    renderer = Render(display, block, grid, CELL_SIZE, CORNER, BKGD_COLOR)
    pace = Pace()
    gameloop = GameLoop(level, clock, event_queue, renderer, pace)

    gameloop.start()


if __name__ == "__main__":
    main()
