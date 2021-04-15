class Level:
    def __init__(self, block):
        self.__grid = [[0 for j in range(10)] for i in range(20)]
        self.__block = block

    def move_block(self, delta_x: int):
        for y in range(self.__block.height):
            for x in range(self.__block.width):
                if (self.__block.shape[y][x] == 1 and
                    (self.__block.x + delta_x < 0 or
                    self.__block.x + self.__block.width + delta_x > 10 or
                    self.__grid[self.__block.y+y][self.__block.x+x+delta_x] != 0)):
                    return
        self.__block.x += delta_x

    def rotate_block(self):
        self.__block.rotate_clockwise()
        for y in range(self.__block.height):
            for x in range(self.__block.width):
                if (self.__block.shape[y][x] == 1 and
                    (self.__block.x < 0 or
                    self.__block.x + self.__block.width > 10 or
                    self.__block.y + self.__block.height > 20 or
                    self.__grid[self.__block.y+y][self.__block.x+x] != 0)):
                    self.__block.rotate_anticlockwise()
                    return

    def lower_block(self):
        for y in range(self.__block.height):
            for x in range(self.__block.width):
                if (self.__block.shape[y][x] == 1 and
                    (self.__block.y + self.__block.height + 1 > 20 or
                    self.__grid[self.__block.y+y+1][self.__block.x+x] != 0)):
                    self.__update_grid()
                    self.__reset_block_position()
                    return False
        
        self.__block.y += 1
        return True

    def drop_block(self):
        while self.lower_block():
            continue

    def __update_grid(self):
        for y in range(self.__block.height):
            for x in range(self.__block.width):
                if self.__block.shape[y][x] == 1:
                    self.__grid[self.__block.y+y][self.__block.x+x] = self.__block.color
                
    def check_for_full_rows(self):
        for row in range(20):
            if self.__grid[row].count(0) == 0:
                self.__grid.pop(row)
                self.__grid.insert(0, [0 for x in range(10)])

    def __reset_block_position(self):
        self.__block.reset_position()

    @property
    def grid(self):
        return self.__grid