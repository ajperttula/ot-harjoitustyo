import pygame
from block import Block
from level import Level
from event import Event
from render import Render
from clock import Clock

def main():
    pygame.init()

    display = pygame.display.set_mode((400, 550))

    clock = Clock()
    block = Block(120,20)
    level = Level(block)
    event_queue = Event()
    counter = 0
    fps = 60

    pygame.display.set_caption("TETRIS")

    while True:
        counter += 1

        if counter%fps == 0:
            level.lower_block()

        for event in event_queue.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    level.move_block(-1)
                if event.key == pygame.K_RIGHT:
                    level.move_block(1)

        Render(display, level)
        clock.tick(fps)

if __name__ == "__main__":
    main()