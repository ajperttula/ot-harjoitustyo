import unittest
from level import Level
from block import Block


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(Block())
        self.level._Level__block.shape = [[1],
                                          [1],
                                          [1],
                                          [1]]

    def test_can_move_block_right(self):
        old_x = self.level._Level__block.x_value
        self.level.move_block(1)
        new_x = self.level._Level__block.x_value
        self.assertEqual(new_x, old_x+1)

    def test_can_move_block_left(self):
        old_x = self.level._Level__block.x_value
        self.level.move_block(-1)
        new_x = self.level._Level__block.x_value
        self.assertEqual(new_x, old_x-1)

    def test_cannot_move_past_left_wall(self):
        for i in range(15):
            self.level.move_block(-1)
        new_x = self.level._Level__block.x_value
        self.assertEqual(new_x, 0)

    def test_cannot_move_past_right_wall(self):
        for i in range(15):
            self.level.move_block(1)
        new_x = self.level._Level__block.x_value
        width = self.level._Level__block.width
        self.assertEqual(new_x, 10-width)

    def test_can_rotate_block(self):
        self.level.rotate_block()
        new_shape = self.level._Level__block.shape
        self.assertEqual(new_shape, [[1, 1, 1, 1]])

    def test_cannot_rotate_block_if_too_close_to_a_wall(self):
        for i in range(15):
            self.level.move_block(1)
        old_shape = self.level._Level__block.shape
        self.level.rotate_block()
        new_shape = self.level._Level__block.shape
        self.assertEqual(new_shape, old_shape)
