import unittest
from block import Block

class TestBlock(unittest.TestCase):
    def setUp(self):
        self.block = Block(0,0)

    def test_constructor_sets_right_x_value(self):
        self.assertEqual(self.block.x, 0)

    def test_constructor_sets_right_y_value(self):
        self.assertEqual(self.block.y, 0)

    def test_constructor_sets_one_of_the_shapes_defined_in_class_variable(self):
        self.assertIn(self.block.shape, self.block.SHAPES)

    def test_constructor_sets_one_of_the_colors_defined_in_class_variable(self):
        self.assertIn(self.block.color, self.block.COLORS)

    def test_block_height_equals_block_width_after_rotation(self):
        height = self.block.height
        self.block.rotate()
        self.assertEqual(self.block.width, height)

    def test_block_width_equals_block_height_after_rotation(self):
        width = self.block.width
        self.block.rotate()
        self.assertEqual(self.block.height, width)