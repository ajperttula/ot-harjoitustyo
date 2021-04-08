class Level:
    def __init__(self, block):
        self.level = [[0 for j in range(10)] for i in range(20)]
        self.cell_size = 25
        self.block = block

    def move_block(self, delta_x: int):
        new_x = self.block.x + delta_x * self.cell_size
        if self.__block_can_move(new_x):
            self.block.x = new_x

    def __block_can_move(self, new_x):
        if new_x < 20 or new_x > 20+(10-self.block.width)*self.cell_size:
            return False
        return True

    def rotate_block(self):
        if self.block.x <= 20+(10-self.block.height)*self.cell_size:
            self.block.rotate()

    def lower_block(self):
        self.block.y += self.cell_size