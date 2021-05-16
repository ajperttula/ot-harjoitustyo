import pygame
from game_loop.block import Block
from game_loop.grid import Grid
from game_loop.pace import Pace
from game_loop.score import Score
from game_loop.level import Level
from game_loop.clock import Clock
from game_loop.event import Event
from game_loop.game_loop import GameLoop
from repository.score_repository import score_repository
from ui.renderers.game_renderer import GameRenderer
from ui.renderers.ui_renderer import UIRenderer
from ui.player_name import PlayerName
from ui.main_menu import MainMenu
from ui.high_scores import HighScores
from config import SCREEN_WIDTH, SCREEN_HEIGHT


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

    name_input = PlayerName(ui_renderer, event_queue)
    game_loop = GameLoop(level, clock, event_queue,
                         game_renderer, score_repository)
    high_scores = HighScores(ui_renderer, event_queue, score_repository)
    main_menu = MainMenu(ui_renderer, event_queue,
                         name_input, game_loop, high_scores)

    main_menu.start()


if __name__ == "__main__":
    main()
