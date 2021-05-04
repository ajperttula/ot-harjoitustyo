import unittest
from game_loop.level import Level
from game_loop.block import Block
from game_loop.grid import Grid
from game_loop.score import Score
from game_loop.pace import Pace


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(Block(), Grid(), Score(), Pace())
        self.level.block.shape = [[1],
                                  [1],
                                  [1],
                                  [1]]

    def test_can_move_block_right(self):
        old_x = self.level.block.x_pos
        self.level.move_block(1)
        new_x = self.level.block.x_pos
        self.assertEqual(new_x, old_x+1)

    def test_can_move_block_left(self):
        old_x = self.level.block.x_pos
        self.level.move_block(-1)
        new_x = self.level.block.x_pos
        self.assertEqual(new_x, old_x-1)

    def test_cannot_move_past_left_border(self):
        for i in range(15):
            self.level.move_block(-1)
        new_x = self.level.block.x_pos
        self.assertEqual(new_x, 0)

    def test_cannot_move_past_right_border(self):
        for i in range(15):
            self.level.move_block(1)
        new_x = self.level.block.x_pos
        width = self.level.block.width()
        grid_width = self.level.grid.width
        self.assertEqual(new_x+width, grid_width)

    def test_cannot_move_block_if_touching_another_block(self):
        # initial block coordinates are (0, 4)
        # set coordinate (0, 5) occupied
        self.level.grid.grid[0][5] = 1
        old_x = self.level.block.x_pos
        self.level.move_block(1)
        new_x = self.level.block.x_pos
        self.assertEqual(new_x, old_x)

    def test_can_rotate_block(self):
        self.level.rotate_block()
        new_shape = self.level.block.shape
        self.assertEqual(new_shape, [[1, 1, 1, 1]])

    def test_cannot_rotate_block_if_too_close_to_right_border(self):
        for i in range(15):
            self.level.move_block(1)
        old_shape = self.level.block.shape
        self.level.rotate_block()
        new_shape = self.level.block.shape
        self.assertEqual(new_shape, old_shape)

    def test_cannot_rotate_block_if_rotation_would_cause_collision_with_another_block(self):
        # initial block coordinates are (0, 4)
        # set coordinate (0, 5) occupied
        self.level.grid.grid[0][5] = 1
        old_shape = self.level.block.shape
        self.level.rotate_block()
        new_shape = self.level.block.shape
        self.assertEqual(new_shape, old_shape)

    def test_reset_game_state_sets_game_over_false(self):
        self.level.game_over = True
        self.level.reset_game_state()
        self.assertFalse(self.level.game_over)

    def test_reset_game_state_resets_block_x_position(self):
        self.level.block.x_pos = 7
        self.level.reset_game_state()
        self.assertEqual(self.level.block.x_pos, 4)

    def test_reset_game_state_resets_block_y_position(self):
        self.level.block.y_pos = 5
        self.level.reset_game_state()
        self.assertEqual(self.level.block.y_pos, 0)

    def test_lower_block_adds_block_y_pos_by_one_if_no_collision(self):
        self.level.lower_block()
        y_pos = self.level.block.y_pos
        self.assertEqual(y_pos, 1)

    def test_lower_block_returns_true_if_no_collision(self):
        self.assertTrue(self.level.lower_block())

    def test_drop_block_drops_block_to_bottom_if_no_collision_to_another_block(self):
        # Function loops lower block, until collision to floor. Block coordinates are transferred
        # to grid, which updates those coordinates with block color. After that, block coordinates
        # are reset to initial position (0, 4) and block color is updated. Let's test that
        # grid coordinates (16, 4), (17, 4), (18, 4) and (19, 4) have block color as value.

        color = self.level.block.color
        self.level.drop_block()

        colored = []
        i = 0
        for row in range(16, 20):
            colored.append([])
            for col in range(4, 5):
                pos = self.level.grid.grid[row][col]
                colored[i].append(pos)
            i += 1

        assumed = [[color],
                   [color],
                   [color],
                   [color]]

        self.assertEqual(colored, assumed)