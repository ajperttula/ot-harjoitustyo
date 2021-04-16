import pygame
from block import Block
from level import Level
from clock import Clock
from event import Event
from render import Render
from pace import Pace
from gameloop import GameLoop

CELL_SIZE = 25
CORNER = 20
WIDTH = 400
HEIGHT = 550

def main():
    pygame.init()

    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("TETRIS")

    block = Block()
    level = Level(block)
    clock = Clock()
    event_queue = Event()
    renderer = Render(display, block, level, CELL_SIZE, CORNER)
    pace = Pace()
    gameloop = GameLoop(level, clock, event_queue, renderer, pace)

    gameloop.start()

if __name__ == "__main__":
    main()