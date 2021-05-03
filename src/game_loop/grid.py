class Grid:
    """Class representing a Tetris gameplay grid.

    Attributes:
        grid: Gameplay grid represented as a 2-dimentional list filled with zeros.
        width: Length of the grid list's nested list.
        height: Length of the grid list.
        color: Color of the grid borders as RGB-value.
    """
    COLOR = (125, 125, 125)
    GRID_HEIGHT = 20
    GRID_WIDTH = 10

    def __init__(self):
        """Constructor creates a new grid object and calls method to reset grid attributes.
        """
        self.reset_grid()

    def __create_grid(self) -> list:
        """Creates a 2-dimensional list based on GRID_WIDTH and GRID_HEIGHT values.

        Returns:
            list: 2-dimentional list full of zeros.
        """
        return [[0 for col in range(Grid.GRID_WIDTH)] for row in range(Grid.GRID_HEIGHT)]

    def update_grid(self, block: "Block"):
        """Updates grid coordinates with block color.

        When block collides to another block or grid floor, the default grid value zero
        is changed to RGB-value of the block so that renderer knows how to draw the grid
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
            self.__grid[block.y_pos+row][block.x_pos+col] = block.color

        for row in range(block.height):
            for col in range(block.width):
                if position_is_block(row, col):
                    color_position(row, col)

    def check_for_full_rows(self) -> int:
        """Checks and deletes full rows on the grid.

        If the row is full, all the values on that particular row
        are RGB-values from previous blocks.

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
            return self.__grid[row].count(0) == 0

        def delete_row(row: int):
            """Deletes full rows.

            Pops the full row from the grid list and inserts a new empty row
            full of zeros to the beginning of the grid list.

            Args:
                row (int): Row number in the grid.
            """
            self.__grid.pop(row)
            self.__grid.insert(0, [0 for col in range(self.width)])

        count = 0
        for row in range(self.height):
            if row_is_full(row):
                delete_row(row)
                count += 1
        return count

    def reset_grid(self):
        """Resets the grid full of zeros and sets grid color.
        """
        self.__grid = self.__create_grid()
        self.__color = Grid.COLOR

    @property
    def grid(self):
        return self.__grid

    @property
    def width(self):
        return len(self.__grid[0])

    @property
    def height(self):
        return len(self.__grid)

    @property
    def color(self):
        return self.__color
