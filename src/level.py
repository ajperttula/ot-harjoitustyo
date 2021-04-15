class Level:
    def __init__(self, block):
        self.__grid = [[0 for j in range(10)] for i in range(20)]
        self.cell_size = 25
        self.__block = block
        self.__reset_block_position()

    def move_block(self, delta_x: int):
        for y in range(self.__block.height):
            for x in range(self.__block.width):
                if (self.__block.shape[y][x] == 1 and
                    (self.__block_grid_x + delta_x < 0 or
                    self.__block_grid_x + self.__block.width + delta_x > 10 or
                    self.__grid[self.__block_grid_y+y][self.__block_grid_x+x+delta_x] != 0)):
                    return
        
        self.__block_grid_x += delta_x
        self.__block.x += delta_x * self.cell_size

    def rotate_block(self):
        self.__block.rotate_clockwise()
        for y in range(self.__block.height):
            for x in range(self.__block.width):
                if (self.__block.shape[y][x] == 1 and
                    (self.__block_grid_x < 0 or
                    self.__block_grid_x + self.__block.width > 10 or
                    self.__block_grid_y + self.__block.height > 20 or
                    self.__grid[self.__block_grid_y+y][self.__block_grid_x+x] != 0)):
                    self.__block.rotate_anticlockwise()
                    return

    def lower_block(self):
        for y in range(self.__block.height):
            for x in range(self.__block.width):
                if (self.__block.shape[y][x] == 1 and
                    (self.__block_grid_y + self.__block.height + 1 > 20 or
                    self.__grid[self.__block_grid_y+y+1][self.__block_grid_x+x] != 0)):
                    self.__update_grid()
                    self.__reset_block_position()
                    return False
        
        self.__block_grid_y += 1
        self.__block.y += self.cell_size
        return True

    def drop_block(self):
        while self.lower_block():
            continue

    def __update_grid(self):
        for y in range(self.__block.height):
            for x in range(self.__block.width):
                if self.__block.shape[y][x] == 1:
                    self.__grid[self.__block_grid_y+y][self.__block_grid_x+x] = self.__block.color

    def __reset_block_position(self):
        self.__block_grid_x = 4
        self.__block_grid_y = 0
        self.__block.x = 120
        self.__block.y = 20
        self.__block.new_shape()
        self.__block.new_color()

    @property
    def grid(self):
        return self.__grid