from os import sys
import pygame


class PlayerName:
    def __init__(self, renderer, event_queue):
        self.__renderer = renderer
        self.__event_queue = event_queue
        self.__player = ""
        self.__running = True

    def loop(self):
        while self.__running:
            self.__check_events()
            self.__render()
        return self.__player_name()

    def __player_name(self):
        player = self.__player
        self.__reset_variables()
        return player

    def __reset_variables(self):
        self.__player = ""
        self.__running = True

    def __check_events(self):
        for event in self.__event_queue.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.__running = False
                if len(self.__player) < 12:
                    self.__player += event.unicode
                if event.key == pygame.K_BACKSPACE:
                    self.__player = self.__player[:-1]

    def __render(self):
        self.__renderer.draw("name_input", player_name=self.__player)
