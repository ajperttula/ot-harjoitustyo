class Grid:
    COLOR = (125, 125, 125)

    def __init__(self, width, height):
        self.__grid = self.__create_grid(width, height)
        self.__width = width
        self.__grid_height = height
        self.__color = Grid.COLOR

    def __create_grid(self, width, height):
        return [[0 for col in range(width)] for row in range(height)]

    def update_grid(self, block):
        for y_value in range(block.height):
            for x_value in range(block.width):
                if block.shape[y_value][x_value] == 1:
                    self.__color_grid(y_value, x_value, block)

    def __color_grid(self, y_value, x_value, block):
        self.__grid[block.y_pos+y_value][block.x_pos+x_value] = block.color

    def check_for_full_rows(self):
        for row in range(self.height):
            if self.__grid[row].count(0) == 0:
                self.__grid.pop(row)
                self.__grid.insert(0, [0 for col in range(self.width)])

    @property
    def grid(self):
        return self.__grid

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__grid_height

    @property
    def color(self):
        return self.__color
