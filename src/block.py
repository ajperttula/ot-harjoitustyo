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
        self.__x = 4
        self.__y = 0
        self.__new_shape()
        self.__new_color()

    def __new_shape(self):
        self.__shape = self.SHAPES[randint(0,len(self.SHAPES)-1)]

    def __new_color(self):
        self.__color = self.COLORS[randint(0,len(self.COLORS)-1)]

    def rotate_clockwise(self):
        new = []
        for y in range(len(self.__shape[0])):
            new.append([])
            for x in range(len(self.__shape)-1,-1,-1):
                new[y].append(self.__shape[x][y])
        self.__shape = new

    def rotate_anticlockwise(self):
        new = []
        i = -1
        for y in range(-1,-len(self.__shape[0])-1,-1):
            i += 1
            new.append([])
            for x in range(len(self.__shape)):
                new[i].append(self.__shape[x][y])
        self.__shape = new

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def shape(self):
        return self.__shape

    @property
    def color(self):
        return self.__color

    @property
    def height(self):
        return len(self.__shape)

    @property
    def width(self):
        return len(self.__shape[0])