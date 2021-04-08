class Level:
    def __init__(self):
        self.grid = [[0 for j in range(10)] for i in range(20)]
        self.cell_size = 25
        self.block = None
        self.collision = False
        self.block_grid_y = 0
        self.block_grid_x = 4

    def move_block(self, delta_x: int):
        new_x = self.block.x + delta_x * self.cell_size
        if self.__block_can_move(new_x):
            self.block.x = new_x
            self.block_grid_x += delta_x

    def __block_can_move(self, new_x):
        if new_x < 20 or new_x > 20+(10-self.block.width)*self.cell_size:
            return False
        return True

    def rotate_block(self):
        if (self.block.x <= 20+(10-self.block.height)*self.cell_size and 
           self.block.y <= 20+(20-self.block.width)*self.cell_size):
            self.block.rotate()

    def lower_block(self):
        new_y = self.block.y + self.cell_size
        if new_y <= 20+(20-self.block.height)*self.cell_size:
            self.block.y = new_y
            self.block_grid_y += 1
        else:
            self.collision = True
            self.update_grid()

    def update_grid(self):
        for y in range(self.block.height):
            for x in range(self.block.width):
                if self.block.shape[y][x] == 1:
                    self.grid[self.block_grid_y+y][self.block_grid_x+x] = self.block.color
        self.block_grid_x = 4
        self.block_grid_y = 0

    def new_block(self, block):
        self.block = block
        self.collision = False