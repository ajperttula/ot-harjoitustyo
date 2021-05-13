from config import GRID_WIDTH, GRID_HEIGHT, GRID_COLOR


class Grid:
    """Class representing a Tetris gameplay grid.

    Attributes:
        grid (list): Gameplay grid represented as a 2-dimentional list filled with zeros.
        width (int): Length of the grid list's nested list.
        height (int): Length of the grid list.
        color (str): Color of the grid borders as hex-value.
    """
    def __init__(self):
        """Constructor creates a new grid object and sets grid attributes.
        """
        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT
        self.color = GRID_COLOR
        self.grid = self.__create_grid()

    def __create_grid(self) -> list:
        """Creates a 2-dimensional list based on GRID_WIDTH and GRID_HEIGHT values.

        Returns:
            list: 2-dimentional list full of zeros.
        """
        return [[0 for col in range(self.width)] for row in range(self.height)]

    def update_grid(self, block: "Block"):
        """Updates grid coordinates with block color.

        When block collides to another block or grid floor, the default grid value zero
        is changed to hex-value of the block so that renderer knows how to draw the grid
        and full rows can be identified later on.

        Args:
            block (Block): Block object.
        """
        def position_is_block(row: int, col: int) -> bool:
            """Checks if given position in block's shape list has value 1.

            Args:
                row (int): Row number in the block's shape list.
                col (int): Column number in the block's shape list.

            Returns:
                bool: True if given position is 1, else False.
            """
            return block.shape[row][col] == 1

        def color_position(row: int, col: int):
            """Colors those grid coordinates where block is at.

            Args:
                row (int): Row number on the block's shape list.
                col (int): Column number on the block's shape list.
            """
            self.grid[block.y_pos+row][block.x_pos+col] = block.color

        for row in range(block.height()):
            for col in range(block.width()):
                if position_is_block(row, col):
                    color_position(row, col)

    def check_for_full_rows(self) -> int:
        """Checks and deletes full rows on the grid.

        If the row is full, all the values on that particular row
        are hex-values from previous blocks.

        Returns:
            int: Number of full rows deleted.
        """
        def row_is_full(row: int) -> bool:
            """Checks if row doesn't have any zero values.

            Args:
                row (int): Row number on the grid.

            Returns:
                bool: True if row doesn't have zeros in it, else False
            """
            return self.grid[row].count(0) == 0

        def delete_row(row: int):
            """Deletes full rows.

            Pops the full row from the grid list and inserts a new empty row
            full of zeros to the beginning of the grid list.

            Args:
                row (int): Row number in the grid.
            """
            self.grid.pop(row)
            self.grid.insert(0, [0 for col in range(self.width)])

        count = 0
        for row in range(self.height):
            if row_is_full(row):
                delete_row(row)
                count += 1
        return count

    def reset_grid(self):
        """Resets the grid full of zeros.
        """
        self.grid = self.__create_grid()

    def __getitem__(self, index: int):
        """Enables referring to grid coordinates without 'grid' prefix.

        If Grid is called only with one index e.g. grid[0], this function
        returns the first row of the grid (list).

        If Grid is called with two indexes e.g. grid[0][0], this function
        returns the content of the first column on the first row.

        Args:
            index (int): Determines which index to return.

        Returns:
            (int/str/list): Grid's content on index.
        """
        return self.grid[index]

    def __setitem__(self, index: int, value):
        """Enables changing grid values without 'grid' prefix.

        Args:
            index (int): Determines which index to change.
            value (int/str/list): Content to save on index.
        """
        self.grid[index] = value
