import pygame
from block import Block
from level import Level
from event import Event
from render import Render
from clock import Clock
from pace import Pace
from gameloop import GameLoop

def main():
    pygame.init()

    display = pygame.display.set_mode((400, 550))
    pygame.display.set_caption("TETRIS")

    block = Block()
    level = Level(block)
    clock = Clock()
    event_queue = Event()
    renderer = Render(display, level)
    pace = Pace()
    gameloop = GameLoop(level, clock, event_queue, renderer, pace)

    gameloop.start()

if __name__ == "__main__":
    main()