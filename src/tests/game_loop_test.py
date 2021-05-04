import unittest
import pygame
from game_loop.game_loop import GameLoop
from game_loop.level import Level
from game_loop.block import Block
from game_loop.grid import Grid
from game_loop.score import Score
from game_loop.pace import Pace


class StubClock:
    def tick(self, fps):
        pass


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self.__events = events

    def get(self):
        return self.__events


class StubRenderer:
    def draw(self):
        pass


class StubScoreRepository:
    def save_score(self, player, score):
        pass


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.level = Level(Block(), Grid(), Score(), Pace())

    def test_can_move_block_left(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_LEFT)]

        game_loop = GameLoop(self.level,
                             StubClock(),
                             StubEventQueue(events),
                             StubRenderer(),
                             StubScoreRepository())

        game_loop._GameLoop__check_events()
        x_pos = self.level.block.x_pos
        self.assertEqual(x_pos, 3)

    def test_can_move_block_right(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_RIGHT)]

        game_loop = GameLoop(self.level,
                             StubClock(),
                             StubEventQueue(events),
                             StubRenderer(),
                             StubScoreRepository())

        game_loop._GameLoop__check_events()
        x_pos = self.level.block.x_pos
        self.assertEqual(x_pos, 5)

    def test_cannot_move_block_past_left_border(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_LEFT) for i in range(10)]
        game_loop = GameLoop(self.level,
                             StubClock(),
                             StubEventQueue(events),
                             StubRenderer(),
                             StubScoreRepository())

        game_loop._GameLoop__check_events()
        x_pos = self.level.block.x_pos
        self.assertEqual(x_pos, 0)

    def test_cannot_move_block_past_right_border(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_RIGHT) for i in range(10)]
        game_loop = GameLoop(self.level,
                             StubClock(),
                             StubEventQueue(events),
                             StubRenderer(),
                             StubScoreRepository())

        game_loop._GameLoop__check_events()
        x_pos = self.level.block.x_pos
        assumed_pos = self.level.grid.width - self.level.block.width()

        self.assertEqual(x_pos, assumed_pos)

    def test_can_rotate_block(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_UP)]
        game_loop = GameLoop(self.level,
                             StubClock(),
                             StubEventQueue(events),
                             StubRenderer(),
                             StubScoreRepository())

        self.level.block.shape = [[1, 1]]
        game_loop._GameLoop__check_events()
        assumed_shape = [[1],
                         [1]]
        self.assertEqual(self.level.block.shape, assumed_shape)

    def test_can_increase_speed(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_DOWN)]
        game_loop = GameLoop(self.level,
                             StubClock(),
                             StubEventQueue(events),
                             StubRenderer(),
                             StubScoreRepository())

        game_loop._GameLoop__check_events()
        self.assertTrue(self.level.pace._Pace__go_fast)

    def test_can_decrease_speed(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_DOWN),
                  StubEvent(pygame.KEYUP, pygame.K_DOWN)]
        game_loop = GameLoop(self.level,
                             StubClock(),
                             StubEventQueue(events),
                             StubRenderer(),
                             StubScoreRepository())

        game_loop._GameLoop__check_events()
        self.assertFalse(self.level.pace._Pace__go_fast)

    def test_can_drop_block(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_SPACE)]
        game_loop = GameLoop(self.level,
                             StubClock(),
                             StubEventQueue(events),
                             StubRenderer(),
                             StubScoreRepository())

        #initial block coordinates are (0, 4) and (0, 5)
        self.level.block.shape = [[1, 1]]
        color = self.level.block.color
        game_loop._GameLoop__check_events()

        #dropped block should be at coordinates (19, 4) and (19, 5)

        grid = self.level.grid.grid[19][4], self.level.grid.grid[19][5]
        assumed = color, color
        self.assertEqual(grid, assumed)