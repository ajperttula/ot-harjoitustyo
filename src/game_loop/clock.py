import pygame


class Clock:
    """Class responsible for controlling game's frame rate.

    Attributes:
        clock: Pygame clock object
    """
    def __init__(self):
        """Constructor creates a new Clock object
        """
        self.__clock = pygame.time.Clock()

    def tick(self, fps: int):
        """Controls game's frame rate.

        Args:
            fps (int): Chosen frame rate.
        """
        self.__clock.tick(fps)
