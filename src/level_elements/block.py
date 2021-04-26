from random import randint


class Block:
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
        self.__create_next_shape()
        self.__create_next_color()
        self.reset_position()

    def reset_position(self):
        self.__y_pos = 0
        self.__x_pos = 4
        self.__new_shape()
        self.__new_color()

    def __new_shape(self):
        self.__shape = self.__next_shape
        self.__create_next_shape()

    def __new_color(self):
        self.__color = self.__next_color
        self.__create_next_color()

    def __create_next_shape(self):
        self.__next_shape = Block.SHAPES[randint(0, len(Block.SHAPES)-1)]

    def __create_next_color(self):
        self.__next_color = Block.COLORS[randint(0, len(Block.COLORS)-1)]

    def rotate_clockwise(self):
        new_shape = []
        for y_value in range(self.width):
            new_shape.append([])
            for x_value in range(self.height-1, -1, -1):
                new_shape[y_value].append(self.shape[x_value][y_value])
        self.shape = new_shape

    def rotate_anticlockwise(self):
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
    def x_pos(self, new_x_pos):
        self.__x_pos = new_x_pos

    @property
    def y_pos(self):
        return self.__y_pos

    @y_pos.setter
    def y_pos(self, new_y_pos):
        self.__y_pos = new_y_pos

    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, new_shape):
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
