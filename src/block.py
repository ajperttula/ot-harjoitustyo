import pygame
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

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__shape = self.SHAPES[randint(0,len(self.SHAPES)-1)]
        self.__color = self.COLORS[randint(0,len(self.COLORS)-1)]

    def rotate(self):
        new = []
        for y in range(len(self.__shape[0])):
            new.append([])
            for x in range(len(self.__shape)-1,-1,-1):
                new[y].append(self.__shape[x][y])
        self.__shape = new

    def shape(self):
        return self.__shape

    def color(self):
        return self.__color

    def height(self):
        return len(self.__shape)

    def width(self):
        return len(self.__shape[0])