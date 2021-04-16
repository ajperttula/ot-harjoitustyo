import pygame


class Clock:
    def __init__(self):
        self.__clock = pygame.time.Clock()

    def tick(self, fps):
        self.__clock.tick(fps)
