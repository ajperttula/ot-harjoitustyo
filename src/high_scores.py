from os import sys
import pygame


class HighScores:
    def __init__(self, renderer, event_queue):
        self.__renderer = renderer
        self.__event_queue = event_queue
        self.__running = True

    def loop(self):
        while self.__running:
            self.__check_events()
            self.__render()
        self.__reset_variables()

    def __reset_variables(self):
        self.__running = True

    def __check_events(self):
        for event in self.__event_queue.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__renderer.main_menu_button.collidepoint(event.pos):
                    self.__running = False

    def __render(self):
        self.__renderer.draw_high_scores("d")
