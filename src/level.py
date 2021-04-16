class Level:
    def __init__(self, block):
        self.__grid = [[0 for column in range(10)] for row in range(20)]
        self.__block = block

    def move_block(self, delta_x: int):
        for y_value in range(self.__block.height):
            for x_value in range(self.__block.width):
                if self.__block_cannot_move(y_value, x_value, delta_x):
                    return
        self.__block.x_value += delta_x

    def __block_cannot_move(self, y_value, x_value, delta_x):
        if (self.__block.shape[y_value][x_value] == 1 and
            (self.__block.x_value + delta_x < 0 or
            self.__block.x_value + self.__block.width + delta_x > 10 or
                self.grid[self.__block.y_value +
                          y_value][self.__block.x_value+x_value+delta_x] != 0)):
            return True
        return False

    def rotate_block(self):
        self.__block.rotate_clockwise()
        for y_value in range(self.__block.height):
            for x_value in range(self.__block.width):
                if self.__block_cannot_rotate(y_value, x_value):
                    self.__block.rotate_anticlockwise()
                    return

    def __block_cannot_rotate(self, y_value, x_value):
        if (self.__block.shape[y_value][x_value] == 1 and
            (self.__block.x_value < 0 or
            self.__block.x_value + self.__block.width > 10 or
            self.__block.y_value + self.__block.height > 20 or
                self.grid[self.__block.y_value+y_value][self.__block.x_value+x_value] != 0)):
            return True
        return False

    def lower_block(self):
        for y_value in range(self.__block.height):
            for x_value in range(self.__block.width):
                if self.__block_collides(y_value, x_value):
                    self.__update_grid()
                    self.__check_for_full_rows()
                    self.__reset_block_position()
                    return False
        self.__block.y_value += 1
        return True

    def __block_collides(self, y_value, x_value):
        if (self.__block.shape[y_value][x_value] == 1 and
            (self.__block.y_value + self.__block.height + 1 > 20 or
                self.grid[self.__block.y_value+y_value+1][self.__block.x_value+x_value] != 0)):
            return True
        return False

    def drop_block(self):
        while self.lower_block():
            continue

    def __update_grid(self):
        for y_value in range(self.__block.height):
            for x_value in range(self.__block.width):
                if self.__block.shape[y_value][x_value] == 1:
                    self.__color_grid(y_value, x_value)

    def __color_grid(self, y_value, x_value):
        self.grid[self.__block.y_value +
                  y_value][self.__block.x_value+x_value] = self.__block.color

    def __check_for_full_rows(self):
        for row in range(20):
            if self.grid[row].count(0) == 0:
                self.grid.pop(row)
                self.grid.insert(0, [0 for x in range(10)])

    def __reset_block_position(self):
        self.__block.reset_position()

    @property
    def grid(self):
        return self.__grid
