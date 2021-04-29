import pygame
from level_elements.block import Block
from level_elements.grid import Grid
from level_elements.pace import Pace
from level_elements.score import Score
from level import Level
from clock import Clock
from event import Event
from renderer import Renderer
from gameloop import GameLoop
from repository.score_repository import score_repository


SCREEN_HEIGHT = 550
SCREEN_WIDTH = 430


def main():
    pygame.init()

    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TETRIS")

    block = Block()
    pace = Pace()
    score = Score()
    grid = Grid()
    level = Level(block, grid, score)
    clock = Clock()
    event_queue = Event()
    renderer = Renderer(display, level)
    gameloop = GameLoop(level, clock, event_queue, renderer, pace, score_repository)

    gameloop.new_game()


if __name__ == "__main__":
    main()
