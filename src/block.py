from random import randint

class Block:
    SHAPES = [[[1,1,1,1]],

              [[1,1,1],
               [0,1,0]],

              [[1,0,0],
               [1,1,1]],

              [[0,0,1],
               [1,1,1]],

              [[1,1,0],
               [0,1,1]],

              [[0,1,1],
               [1,1,0]],

              [[1,1],
               [1,1]]]

    COLORS = [(255,0,0), (0,255,0), (0,0,255)]

    def __init__(self):
        self.reset_position()

    def reset_position(self):
        self.__y_value = 0
        self.__x_value = 4
        self.__shape = self.__new_shape()
        self.__color = self.__new_color()

    def __new_shape(self):
        return Block.SHAPES[randint(0,len(Block.SHAPES)-1)]

    def __new_color(self):
        return Block.COLORS[randint(0,len(Block.COLORS)-1)]

    def rotate_clockwise(self):
        new_shape = []
        for y_value in range(self.width):
            new_shape.append([])
            for x_value in range(self.height-1,-1,-1):
                new_shape[y_value].append(self.shape[x_value][y_value])
        self.shape = new_shape

    def rotate_anticlockwise(self):
        new_shape = []
        i = -1
        for y_value in range(-1,-self.width-1,-1):
            i += 1
            new_shape.append([])
            for x_value in range(self.height):
                new_shape[i].append(self.shape[x_value][y_value])
        self.shape = new_shape

    @property
    def x_value(self):
        return self.__x_value

    @x_value.setter
    def x_value(self, new_x_value):
        self.__x_value = new_x_value

    @property
    def y_value(self):
        return self.__y_value

    @y_value.setter
    def y_value(self, new_y_value):
        self.__y_value = new_y_value

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
    def height(self):
        return len(self.__shape)

    @property
    def width(self):
        return len(self.__shape[0])
