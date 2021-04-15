class Level:
    def __init__(self, block):
        self.grid = [[0 for j in range(10)] for i in range(20)]
        self.cell_size = 25
        self.block = block
        self.__reset_block_position()

    def move_block(self, delta_x: int):
        for y in range(self.block.height):
            for x in range(self.block.width):
                if (self.block.shape[y][x] == 1 and
                    (self.block_grid_x + delta_x < 0 or
                    self.block_grid_x + self.block.width + delta_x > 10 or
                    self.grid[self.block_grid_y+y][self.block_grid_x+x+delta_x] != 0)):
                    return
        
        self.block_grid_x += delta_x
        self.block.x += delta_x * self.cell_size

    def rotate_block(self):
        self.block.rotate_clockwise()
        for y in range(self.block.height):
            for x in range(self.block.width):
                if (self.block.shape[y][x] == 1 and
                    (self.block_grid_x < 0 or
                    self.block_grid_x + self.block.width > 10 or
                    self.block_grid_y + self.block.height > 20 or
                    self.grid[self.block_grid_y+y][self.block_grid_x+x] != 0)):
                    self.block.rotate_anticlockwise()
                    return

    def lower_block(self):
        for y in range(self.block.height):
            for x in range(self.block.width):
                if (self.block.shape[y][x] == 1 and
                    (self.block_grid_y + self.block.height + 1 > 20 or
                    self.grid[self.block_grid_y+y+1][self.block_grid_x+x] != 0)):
                    self.__update_grid()
                    self.__reset_block_position()
                    return
        
        self.block_grid_y += 1
        self.block.y += self.cell_size 

    def __update_grid(self):
        for y in range(self.block.height):
            for x in range(self.block.width):
                if self.block.shape[y][x] == 1:
                    self.grid[self.block_grid_y+y][self.block_grid_x+x] = self.block.color

    def __reset_block_position(self):
        self.block_grid_x = 4
        self.block_grid_y = 0
        self.block.x = 120
        self.block.y = 20
        self.block.new_shape()
        self.block.new_color()