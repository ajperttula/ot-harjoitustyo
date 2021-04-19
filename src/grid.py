class Grid:
    COLOR = (125, 125, 125)

    def __init__(self, width, height):
        self.__grid = self.__create_grid(width, height)
        self.__width = width
        self.__height = height
        self.__color = Grid.COLOR

    def __create_grid(self, width, height):
        return [[0 for col in range(width)] for row in range(height)]

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

        for row in range(self.height):
            if row_is_full(row):
                delete_row(row)

    @property
    def grid(self):
        return self.__grid

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def color(self):
        return self.__color
