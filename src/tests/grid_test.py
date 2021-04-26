import unittest
from level_elements.grid import Grid
from level_elements.block import Block


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()

    def test_constructor_sets_right_width(self):
        self.assertEqual(self.grid.width, 10)

    def test_constructor_sets_right_height(self):
        self.assertEqual(self.grid.height, 20)

    def test_update_grid_sets_block_color_as_value_to_block_coordinates(self):
        # initial block coordinates are (0, 4), (0, 5), (1, 4), (1, 5)

        block = Block()
        block.shape = [[1, 1],
                       [0, 1]]

        # following coordinates should be colored: (0, 4), (0, 5) and (1, 5)

        self.grid.update_grid(block)

        colored = []
        for row in range(2):
            colored.append([])
            for col in range(4, 6):
                pos = self.grid.grid[row][col]
                colored[row].append(pos)

        color = block.color
        assumed = [[color, color],
                   [0, color]]

        self.assertEqual(colored, assumed)

    def test_check_for_full_rows_deletes_full_row(self):
        self.grid.grid[0] = [1 for col in range(self.grid.width)]
        self.grid.check_for_full_rows()
        assumed = [0 for col in range(self.grid.width)]
        self.assertEqual(self.grid.grid[0], assumed)

    def test_check_for_full_rows_deletes_multiple_full_rows(self):
        for i in range(2):
            self.grid.grid[i] = [1 for col in range(self.grid.width)]
        self.grid.check_for_full_rows()
        assumed = [[0 for col in range(self.grid.width)] for row in range(2)]
        self.assertEqual([self.grid.grid[0], self.grid.grid[1]], assumed)

    def test_check_for_full_rows_doesnt_delete_rows_that_are_not_full(self):
        self.grid.grid[0] = [0, 1, 1, 0, 1, 1, 0, 0, 0, 1]
        self.grid.check_for_full_rows()
        assumed = [0, 1, 1, 0, 1, 1, 0, 0, 0, 1]
        self.assertEqual(self.grid.grid[0], assumed)
