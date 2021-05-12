from random import randint
from config import BLOCK_COLOR_1, BLOCK_COLOR_2, BLOCK_COLOR_3


class Block:
    """Class representing a single Tetris Block.

    Block object has always knowledge of it's current shape and color and
    how it's going to be looking next. This allows rendering of the next
    block during gameplay.

    Attributes:
        x_pos (int): X position on the gameplay grid.
        y_pos (int): Y position on the gameplay grid.
        shape (list):
            Shape represented as a 2-dimentional list filled with ones and zeros.
            Positions with ones represent the block, zeros just fill the empty space.
        color (tuple): Color represented as RGB-value.
        next_shape (list): Shape that block is going to be next.
        next_color (tuple): Color that block is going to be next.
    """
    SHAPES = [[[1, 1, 1, 1]],

              [[1, 1, 1],
               [0, 1, 0]],

              [[1, 0, 0],
               [1, 1, 1]],

              [[0, 0, 1],
               [1, 1, 1]],

              [[1, 1, 0],
               [0, 1, 1]],

              [[0, 1, 1],
               [1, 1, 0]],

              [[1, 1],
               [1, 1]]]

    COLORS = [BLOCK_COLOR_1, BLOCK_COLOR_2, BLOCK_COLOR_3]

    def __init__(self):
        """Constructor creates a new Block object.

        Sets attributes to their initial state.
        """
        self.y_pos = 0
        self.x_pos = 4
        self.shape = Block.SHAPES[randint(0, len(Block.SHAPES)-1)]
        self.color = Block.COLORS[randint(0, len(Block.COLORS)-1)]
        self.next_shape = Block.SHAPES[randint(0, len(Block.SHAPES)-1)]
        self.next_color = Block.COLORS[randint(0, len(Block.COLORS)-1)]

    def reset_position(self):
        """Resets block's position, changes block shape and color and creates next ones.
        """
        self.y_pos = 0
        self.x_pos = 4
        self.__change_shape()
        self.__change_color()
        self.__create_next_shape()
        self.__create_next_color()

    def rotate_clockwise(self):
        """Changes shape's 2-dimentional list presentation.

        Columns from old shape become rows in new shape.
        """
        new_shape = []
        for y_value in range(self.width()):
            new_shape.append([])
            for x_value in range(self.height()-1, -1, -1):
                new_shape[y_value].append(self.shape[x_value][y_value])
        self.shape = new_shape

    def rotate_anticlockwise(self):
        """Changes shape's 2-dimentional list presentation.

        Rows from old shape become columns in new shape.
        """
        new_shape = []
        i = -1
        for y_value in range(-1, -self.width()-1, -1):
            i += 1
            new_shape.append([])
            for x_value in range(self.height()):
                new_shape[i].append(self.shape[x_value][y_value])
        self.shape = new_shape

    def height(self) -> int:
        """Returns height of the block shape.

        Returns:
            int: Length of the shape list.
        """
        return len(self.shape)

    def width(self) -> int:
        """Returns width of the block shape.

        Returns:
            int: Length of the shape list's nested list.
        """
        return len(self.shape[0])

    def next_height(self) -> int:
        """Returns height of the block's next shape.

        Returns:
            int: Length of the next_shape list.
        """
        return len(self.next_shape)

    def next_width(self) -> int:
        """Returns width of the block's next shape.

        Returns:
            int: Length of the next_shape list's nested list.
        """
        return len(self.next_shape[0])

    def __change_shape(self):
        """Changes shape to next shape.
        """
        self.shape = self.next_shape

    def __change_color(self):
        """Changes color to next color.
        """
        self.color = self.next_color

    def __create_next_shape(self):
        """Sets a random shape from the SHAPES list as a value to next shape.
        """
        self.next_shape = Block.SHAPES[randint(0, len(Block.SHAPES)-1)]

    def __create_next_color(self):
        """Sets a random color from the COLORS list as a value to next color.
        """
        self.next_color = Block.COLORS[randint(0, len(Block.COLORS)-1)]
