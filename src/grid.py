class Grid:
    COLOR = (125, 125, 125)
    GRID_HEIGHT = 20
    GRID_WIDTH = 10

    def __init__(self):
        self.reset_grid()

    def __create_grid(self):
        return [[0 for col in range(Grid.GRID_WIDTH)] for row in range(Grid.GRID_HEIGHT)]

    def update_grid(self, block):
        def position_is_block(row, col):
            return block.shape[row][col] == 1

        def color_position(row, col):
            self.__grid[block.y_pos+row][block.x_pos+col] = block.color

        for row in range(block.height):
            for col in range(block.width):
                if position_is_block(row, col):
                    color_position(row, col)

    def check_for_full_rows(self):
        def row_is_full(row):
            return self.__grid[row].count(0) == 0

        def delete_row(row):
            self.__grid.pop(row)
            self.__grid.insert(0, [0 for col in range(self.width)])

        count = 0
        for row in range(self.height):
            if row_is_full(row):
                delete_row(row)
                count += 1
        return count

    def reset_grid(self):
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
