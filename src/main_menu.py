from os import sys
import pygame


class MainMenu:
    def __init__(self, renderer, event_queue, name_input, gameloop):
        self.__renderer = renderer
        self.__event_queue = event_queue
        self.__name_input = name_input
        self.__gameloop = gameloop

    def start(self):
        while True:
            self.__check_events()
            self.__render()

    def __check_events(self):
        for event in self.__event_queue.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__renderer.new_game_button.collidepoint(event.pos):
                    self.__new_game()
                if self.__renderer.exit_button.collidepoint(event.pos):
                    sys.exit()

    def __render(self):
        self.__renderer.draw_menu()

    def __new_game(self):
        player = self.__name_input.loop()
        self.__gameloop.new_game(player)
