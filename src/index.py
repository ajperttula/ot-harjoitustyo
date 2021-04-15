import pygame
from block import Block
from level import Level
from event import Event
from render import Render
from clock import Clock
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
    gameloop = GameLoop(level, clock, event_queue, renderer)

    gameloop.start()

if __name__ == "__main__":
    main()