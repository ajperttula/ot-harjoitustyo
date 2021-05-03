from random import randint


class Block:
    """Class representing a single Tetris Block.

    Block object has always knowledge of it's current shape and color and
    how it's going to be looking next. This allows rendering of the next
    block during gameplay.

    Attributes:
        x_pos: X position as integer.
        y_pos: Y position as integer.
        shape:
            Shape represented as a 2-dimentional list filled with ones and zeros.
            Positions with ones represent the block, zeros just fill the empty space.
        color: Color represented as RGB-value.
        next_shape: Shape that block is going to be next.
        next_color: Color that block is going to be next.
        height: Length of the shape list.
        width: Length of the shape list's nested list.
        next_height: Length of the next_shape list.
        next_width: Length of the next_shape list's nested list.
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

    COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

    def __init__(self):
        """Constructor creates a new Block object.

        Calls methods to reset block position, create next shape and next color for the block.
        """
        self.__create_next_shape()
        self.__create_next_color()
        self.reset_position()

    def reset_position(self):
        """Resets block's x and y position and calls methods to change block shape and color.
        """
        self.__y_pos = 0
        self.__x_pos = 4
        self.__new_shape()
        self.__new_color()

    def __new_shape(self):
        """Sets shape value to next_shape and calls method to create next shape.
        """
        self.__shape = self.__next_shape
        self.__create_next_shape()

    def __new_color(self):
        """Sets color value to next_color and calls method to create next color.
        """
        self.__color = self.__next_color
        self.__create_next_color()

    def __create_next_shape(self):
        """Sets a random shape from the SHAPES list as a value to next_shape.
        """
        self.__next_shape = Block.SHAPES[randint(0, len(Block.SHAPES)-1)]

    def __create_next_color(self):
        """Sets a random color from the COLORS list as a value to next_color.
        """
        self.__next_color = Block.COLORS[randint(0, len(Block.COLORS)-1)]

    def rotate_clockwise(self):
        """Changes shape's 2-dimentional list presentation.

        Columns from old shape become rows in new shape.
        """
        new_shape = []
        for y_value in range(self.width):
            new_shape.append([])
            for x_value in range(self.height-1, -1, -1):
                new_shape[y_value].append(self.shape[x_value][y_value])
        self.shape = new_shape

    def rotate_anticlockwise(self):
        """Changes shape's 2-dimentional list presentation.

        Rows from old shape become columns in new shape.
        """
        new_shape = []
        i = -1
        for y_value in range(-1, -self.width-1, -1):
            i += 1
            new_shape.append([])
            for x_value in range(self.height):
                new_shape[i].append(self.shape[x_value][y_value])
        self.shape = new_shape

    @property
    def x_pos(self):
        return self.__x_pos

    @x_pos.setter
    def x_pos(self, new_x_pos: int):
        self.__x_pos = new_x_pos

    @property
    def y_pos(self):
        return self.__y_pos

    @y_pos.setter
    def y_pos(self, new_y_pos: int):
        self.__y_pos = new_y_pos

    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, new_shape: list):
        self.__shape = new_shape

    @property
    def color(self):
        return self.__color

    @property
    def next_shape(self):
        return self.__next_shape

    @property
    def next_color(self):
        return self.__next_color

    @property
    def next_height(self):
        return len(self.__next_shape)

    @property
    def next_width(self):
        return len(self.__next_shape[0])

    @property
    def height(self):
        return len(self.__shape)

    @property
    def width(self):
        return len(self.__shape[0])
