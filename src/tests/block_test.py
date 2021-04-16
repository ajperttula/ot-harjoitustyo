import unittest
from block import Block


class TestBlock(unittest.TestCase):
    def setUp(self):
        self.block = Block()

    def test_constructor_sets_right_x_value(self):
        self.assertEqual(self.block.x_value, 4)

    def test_constructor_sets_right_y_value(self):
        self.assertEqual(self.block.y_value, 0)

    def test_constructor_sets_one_of_the_shapes_defined_in_class_variable(self):
        self.assertIn(self.block.shape, Block.SHAPES)

    def test_constructor_sets_one_of_the_colors_defined_in_class_variable(self):
        self.assertIn(self.block.color, Block.COLORS)

    def test_block_height_equals_block_width_after_clockwise_rotation(self):
        height = self.block.height
        self.block.rotate_clockwise()
        self.assertEqual(self.block.width, height)

    def test_block_width_equals_block_height_after_clockwise_rotation(self):
        width = self.block.width
        self.block.rotate_clockwise()
        self.assertEqual(self.block.height, width)

    def test_block_height_equals_block_width_after_anticlockwise_rotation(self):
        height = self.block.height
        self.block.rotate_anticlockwise()
        self.assertEqual(self.block.width, height)

    def test_block_width_equals_block_height_after_anticlockwise_rotation(self):
        width = self.block.width
        self.block.rotate_anticlockwise()
        self.assertEqual(self.block.height, width)
