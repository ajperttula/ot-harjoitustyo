from os import sys
import pygame


class PlayerNameView:
    def __init__(self, renderer, event_queue):
        self.__renderer = renderer
        self.__event_queue = event_queue
        self.__reset_variables()

    def loop(self):
        while not self.__ready:
            self.__check_events()
            self.__render()
        player = self.__player_name
        self.__reset_variables()
        return player

    def __reset_variables(self):
        self.__player_name = ""
        self.__ready = False

    def __check_events(self):
        for event in self.__event_queue.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.__ready = True
                if len(self.__player_name) < 16:
                    self.__player_name += event.unicode
                if event.key == pygame.K_BACKSPACE:
                    self.__player_name = self.__player_name[:-1]

    def __render(self):
        self.__renderer.draw_name_input(self.__player_name)
