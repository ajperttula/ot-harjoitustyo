from os import sys
import pygame


class MainMenu:
    """Class responsible for running the main menu loop.

    Attributes:
        renderer: Does the actula drawing.
        event_queue: Handles user events.
        name_input: Player name input view.
        gameloop: Gameloop view.
        high_scores: High scores view.
    """
    def __init__(self, renderer: "UIRenderer", event_queue: "Event",
                 name_input: "PlayerName", gameloop: "GameLoop", high_scores: "HighScores"):
        """Creates a new main menu object and sets attributes.

        Args:
            renderer (UIRenderer): UIRenderer object.
            event_queue (Event): Event object.
            name_input (PlayerName): PlayerName object.
            gameloop (GameLoop): GameLoop object.
            high_scores (HighScores): HighScores object.
        """
        self.__renderer = renderer
        self.__event_queue = event_queue
        self.__name_input = name_input
        self.__gameloop = gameloop
        self.__high_scores = high_scores

    def start(self):
        """Checks user events and draws the screen in infinite loop.
        """
        while True:
            self.__check_events()
            self.__render()

    def __check_events(self):
        """Checks user events.
        """
        for event in self.__event_queue.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__renderer.new_game_button.collidepoint(event.pos):
                    self.__new_game()
                if self.__renderer.high_scores_button.collidepoint(event.pos):
                    self.__high_scores.loop()
                if self.__renderer.exit_button.collidepoint(event.pos):
                    sys.exit()

    def __render(self):
        """Calls renderer to draw the main menu view.
        """
        self.__renderer.draw("main")

    def __new_game(self):
        """First calls name input view and then starts the gameloop.

        The player name user has entered is saved and passed as an parameter to
        the gameloop.
        """
        player = self.__name_input.loop()
        self.__gameloop.new_game(player)
