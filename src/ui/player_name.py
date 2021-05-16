from os import sys
import pygame


class PlayerName:
    """Class responsible for running the player name input view.

    Attributes:
        renderer: Does the actual drawing
        event_queue: Handles user events
        player (str): Player name to render
        running (bool): To stop the loop
    """

    def __init__(self, renderer: "UIRenderer", event_queue: "Event"):
        """Creates a new high score object and sets attributes.

        Args:
            renderer (UIRenderer): UIRenderer object
            event_queue (Event): Event object
        """
        self.__renderer = renderer
        self.__event_queue = event_queue
        self.__player = ""
        self.__running = True

    def loop(self) -> str:
        """Checks user events and renders the screen.

        Returns:
            str: Player name that player has entered
        """
        while self.__running:
            self.__check_events()
            self.__render()
        return self.__player_name()

    def __player_name(self) -> str:
        """Returns and resets the player name.

        Returns:
            str: Player name that player has entered
        """
        player = self.__player
        self.__reset_variables()
        return player

    def __reset_variables(self):
        """Resets player name and running values.
        """
        self.__player = ""
        self.__running = True

    def __check_events(self):
        """Checks user events.
        """
        for event in self.__event_queue.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.__running = False
                elif event.key == pygame.K_BACKSPACE:
                    self.__player = self.__player[:-1]
                elif len(self.__player) < 12:
                    self.__player += event.unicode

    def __render(self):
        """Calls renderer to draw player text input.
        """
        self.__renderer.draw("name_input", player_name=self.__player)
