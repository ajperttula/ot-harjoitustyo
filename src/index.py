import pygame
from level_elements.block import Block
from level_elements.grid import Grid
from level_elements.pace import Pace
from level_elements.score import Score
from level import Level
from clock import Clock
from event import Event
from game_renderer import GameRenderer
from ui_renderer import UIRenderer
from gameloop import GameLoop
from repository.score_repository import score_repository
from player_name_view import PlayerNameView
from main_menu import MainMenu
from high_scores import HighScores


SCREEN_HEIGHT = 540
SCREEN_WIDTH = 430


def main():
    pygame.init()

    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TETRIS")

    block = Block()
    pace = Pace()
    score = Score()
    grid = Grid()
    level = Level(block, grid, score, pace)
    clock = Clock()
    event_queue = Event()
    game_renderer = GameRenderer(display, level)
    ui_renderer = UIRenderer(display)

    name_input = PlayerNameView(ui_renderer, event_queue)
    gameloop = GameLoop(level, clock, event_queue, game_renderer, score_repository)
    high_scores = HighScores(ui_renderer, event_queue, score_repository)
    main_menu = MainMenu(ui_renderer, event_queue, name_input, gameloop, high_scores)

    main_menu.start()


if __name__ == "__main__":
    main()
