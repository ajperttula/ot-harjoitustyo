class Level:
    def __init__(self, block, grid, score):
        self.__grid = grid
        self.__block = block
        self.__score = score

    def move_block(self, delta_x: int):
        self.__block.x_pos += delta_x

        if self.__block_collides():
            self.__block.x_pos -= delta_x

    def rotate_block(self):
        self.__block.rotate_clockwise()

        if self.__block_collides():
            self.__block.rotate_anticlockwise()

    def lower_block(self):
        def update_grid():
            self.__grid.update_grid(self.__block)

        def check_for_full_rows():
            count = self.__grid.check_for_full_rows()
            if count:
                self.__score.add_score(count)

        def reset_block_position():
            self.__block.reset_position()

        self.__block.y_pos += 1
        if self.__block_collides():
            self.__block.y_pos -= 1
            update_grid()
            check_for_full_rows()
            reset_block_position()
            return False
        return True

    def drop_block(self):
        while self.lower_block():
            continue

    def __block_collides(self):
        def position_is_block(row, col):
            return self.__block.shape[row][col] == 1

        def position_is_occupied(row, col):
            return self.__grid.grid[self.__block.y_pos+row][self.__block.x_pos+col] != 0

        def position_is_past_left_border():
            return self.__block.x_pos < 0

        def position_is_past_right_border():
            return self.__block.x_pos + self.__block.width > self.__grid.width

        def position_is_past_floor():
            return self.__block.y_pos + self.__block.height > self.__grid.height

        if (position_is_past_left_border() or
            position_is_past_right_border() or
                position_is_past_floor()):
            return True

        for row in range(self.__block.height):
            for col in range(self.__block.width):
                if position_is_block(row, col) and position_is_occupied(row, col):
                    return True
        return False
