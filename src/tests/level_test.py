import unittest
from level import Level
from block import Block
from grid import Grid
from score import Score


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(Block(), Grid(), Score())
        self.level._Level__block.shape = [[1],
                                          [1],
                                          [1],
                                          [1]]

    def test_can_move_block_right(self):
        old_x = self.level._Level__block.x_pos
        self.level.move_block(1)
        new_x = self.level._Level__block.x_pos
        self.assertEqual(new_x, old_x+1)

    def test_can_move_block_left(self):
        old_x = self.level._Level__block.x_pos
        self.level.move_block(-1)
        new_x = self.level._Level__block.x_pos
        self.assertEqual(new_x, old_x-1)

    def test_cannot_move_past_left_border(self):
        for i in range(15):
            self.level.move_block(-1)
        new_x = self.level._Level__block.x_pos
        self.assertEqual(new_x, 0)

    def test_cannot_move_past_right_border(self):
        for i in range(15):
            self.level.move_block(1)
        new_x = self.level._Level__block.x_pos
        width = self.level._Level__block.width
        grid_width = self.level._Level__grid.width
        self.assertEqual(new_x+width, grid_width)

    def test_cannot_move_block_if_touching_another_block(self):
        # initial block coordinates are (0, 4)
        # set coordinate (0, 5) occupied
        self.level._Level__grid.grid[0][5] = 1
        old_x = self.level._Level__block.x_pos
        self.level.move_block(1)
        new_x = self.level._Level__block.x_pos
        self.assertEqual(new_x, old_x)

    def test_can_rotate_block(self):
        self.level.rotate_block()
        new_shape = self.level._Level__block.shape
        self.assertEqual(new_shape, [[1, 1, 1, 1]])

    def test_cannot_rotate_block_if_too_close_to_right_border(self):
        for i in range(15):
            self.level.move_block(1)
        old_shape = self.level._Level__block.shape
        self.level.rotate_block()
        new_shape = self.level._Level__block.shape
        self.assertEqual(new_shape, old_shape)

    def test_cannot_rotate_block_if_rotation_would_cause_collision_with_another_block(self):
        # initial block coordinates are (0, 4)
        # set coordinate (0, 5) occupied
        self.level._Level__grid.grid[0][5] = 1
        old_shape = self.level._Level__block.shape
        self.level.rotate_block()
        new_shape = self.level._Level__block.shape
        self.assertEqual(new_shape, old_shape)

    def test_reset_game_state_sets_game_over_false(self):
        self.level._Level__game_over = True
        self.level.reset_game_state()
        self.assertFalse(self.level._Level__game_over)

    def test_reset_game_state_resets_block_x_position(self):
        self.level.block.x_pos = 7
        self.level.reset_game_state()
        self.assertEqual(self.level.block.x_pos, 4)

    def test_reset_game_state_resets_block_y_position(self):
        self.level.block.y_pos = 5
        self.level.reset_game_state()
        self.assertEqual(self.level.block.y_pos, 0)

    def test_reset_game_state_resets_grid(self):
        