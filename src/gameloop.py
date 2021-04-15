import pygame

FPS = 60

class GameLoop:
    def __init__(self, level, clock, event_queue, renderer, pace):
        self.__level = level
        self.__clock = clock
        self.__event_queue = event_queue
        self.__renderer = renderer
        self.__pace = pace

    def start(self):
        while True:
            self.__pace.increase_counter()
            self.__check_counter()
            self.__check_events()
            self.__renderer.draw()
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
                if event.key == pygame.K_DOWN:
                    self.__pace.increase_speed()
                if event.key == pygame.K_SPACE:
                    self.__level.drop_block()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.__pace.decrease_speed()
    
    def __check_counter(self):
        if self.__pace.check_counter(FPS):
            self.__level.lower_block()