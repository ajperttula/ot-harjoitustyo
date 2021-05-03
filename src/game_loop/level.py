class Level:
    """Class responsible for handling game play events.

    Attributes:
        block (Block): Block that falls on the grid.
        grid (Grid): Gameplay grid.
        score (Score): Object that keeps track of score.
        pace (Pace): Object that controls game pace.
        game_over (bool): States if game is over or not.
    """
    def __init__(self, block: "Block", grid: "Grid", score: "Score", pace: "Pace"):
        """Constructor creates a new level object.

        Args:
            block (Block): Block object.
            grid (Grid): Grid object.
            score (Score): Score object.
            pace (Pace): Pace object.
        """
        self.__block = block
        self.__grid = grid
        self.__score = score
        self.__pace = pace
        self.__game_over = False

    def move_block(self, delta_x: int):
        """Moves block sideways.

        Block's x position is changed according to delta_x value.
        Then, a collision check is made by calling block_collides function.
        If change caused a collision, it is reversed.

        Args:
            delta_x (int): Describes direction to move (+- 1).
        """
        self.__block.x_pos += delta_x

        if self.__block_collides():
            self.__block.x_pos -= delta_x

    def rotate_block(self):
        """Rotates block clockwise.

        Block's method rotate_clockwise is called.
        Then, a collision check is made by calling block_collides function.
        If change caused a collision, it is reversed by rotating the block
        anticlockwise.
        """
        self.__block.rotate_clockwise()

        if self.__block_collides():
            self.__block.rotate_anticlockwise()

    def lower_block(self) -> bool:
        """Lowers block position by one.

        Block's y position is added by one. Then, a collision check is made
        by calling block_collides function. If collision occurs, block's position
        is reversed. Then another check is made to see if game is over.
        If not, helper methods are called to update grid color, check full rows and
        reset block position back to initial position.

        Returns:
            bool: True if block didn't collide, else False.
        """
        def update_grid():
            """Calls grid method update_grid.
            """
            self.__grid.update_grid(self.__block)

        def check_for_full_rows():
            """Gets a count of full rows and adds them to score.
            """
            count = self.__grid.check_for_full_rows()
            if count:
                self.__score.add_score(count)

        def game_over() -> bool:
            """Checks if still after reversing the block position, collision occurs.

            This function makes another call to block_collides function to find out
            if game is over and sets variable game_over to True accordingly.

            Returns:
                bool: True if collision still occurs, else False.
            """
            if self.__block_collides():
                self.__game_over = True
                return True
            return False

        def reset_block_position():
            """Calls block's reset_position method
            """
            self.__block.reset_position()

        self.__block.y_pos += 1
        if self.__block_collides():
            self.__block.y_pos -= 1
            if not game_over():
                update_grid()
                check_for_full_rows()
                reset_block_position()
            return False
        return True

    def drop_block(self):
        """Drops block immediately as far down as possible.
        """
        while self.lower_block():
            continue

    def increase_speed(self):
        """Calls pace method increase_speed
        """
        self.__pace.increase_speed()

    def decrease_speed(self):
        """Calls pace method decrease_speed
        """
        self.__pace.decrease_speed()

    def reset_game_state(self):
        """Resets attribute objects and variables to their initial state.
        """
        self.__game_over = False
        self.__block.reset_position()
        self.__grid.reset_grid()
        self.__score.reset_score()
        self.__pace.reset_pace()

    def __block_collides(self) -> bool:
        """Checks block collision with grid borders and another blocks.

        Returns:
            bool: True if one of the collition checks return True, else False.
        """
        def position_is_block(row: int, col: int) -> bool:
            """Checks if given position in block's shape list has value 1.

            Args:
                row (int): Row number in the block's shape list.
                col (int): Column number in the block's shape list.

            Returns:
                bool: True if given position is 1, else False.
            """
            return self.__block.shape[row][col] == 1

        def position_is_occupied(row: int, col: int) -> bool:
            """Checks if position that block would occupy next is already occupied.

            Position is occupied if that grid coordinate value is not zero.

            Args:
                row (int): Row number in the block's shape list.
                col (int): Column number in the block's shape list.

            Returns:
                bool: True if position is occupied, else False.
            """
            return self.__grid.grid[self.__block.y_pos+row][self.__block.x_pos+col] != 0

        def position_is_past_left_border() -> bool:
            """Checks if block's x coordinate is less than zero.

            Returns:
                bool: True if less than zero, else False.
            """
            return self.__block.x_pos < 0

        def position_is_past_right_border() -> bool:
            """Checks if block's leftmost coordinate is greater than grid width.

            Returns:
                bool: True if greater, else False.
            """
            return self.__block.x_pos + self.__block.width > self.__grid.width

        def position_is_past_floor() -> bool:
            """Checks if block coordinate is greater than grid height.

            Returns:
                bool: True if greater, else False.
            """
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

    @property
    def game_over(self):
        return self.__game_over

    @property
    def block(self):
        return self.__block

    @property
    def grid(self):
        return self.__grid

    @property
    def score(self):
        return self.__score

    @property
    def pace(self):
        return self.__pace
