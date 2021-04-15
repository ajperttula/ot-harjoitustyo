import pygame

FPS = 60

class GameLoop:
    def __init__(self, level, clock, event_queue, renderer):
        self.__counter = 0
        self.__level = level
        self.__clock = clock
        self.__event_queue = event_queue
        self.__renderer = renderer

    def start(self):
        while True:
            self.__increase_counter()
            self.__check_events()
            self.__render()
            self.__clock.tick(FPS)

    def __check_events(self):
        for event in self.__event_queue.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.__level.move_block(-1)
                if event.key == pygame.K_RIGHT:
                    self.__level.move_block(1)
                if event.key == pygame.K_UP:
                    self.__level.rotate_block()

    def __render(self):
        self.__renderer.draw()

    def __increase_counter(self):
        self.__counter += 2
        if self.__counter%FPS == 0:
            self.__level.lower_block()