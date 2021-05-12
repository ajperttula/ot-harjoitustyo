from os import sys
import pygame


class HighScores:
    """Class responsible for running the high scores view.

    Attributes:
        renderer: Does the actual drawing.
        event_queue: Handles user events.
        score_repository: Communicates with SQL database.
        running (bool): To stop the loop.
    """
    def __init__(self, renderer: "UIRenderer", event_queue: "Event",
                 score_repository: "ScoreRepository"):
        """Creates a new high score object and sets attributes.

        Args:
            renderer (UIRenderer): UIRenderer object.
            event_queue (Event): Event object.
            score_repository (ScoreRepository): ScoreRepository object.
        """
        self.__renderer = renderer
        self.__event_queue = event_queue
        self.__score_repository = score_repository
        self.__running = True

    def loop(self):
        """Checks user events and renders the screen.

        Loop is continued until running is set to false by clicking the
        main menu button. After that running is set back to true for next
        time.
        """
        while self.__running:
            self.__check_events()
            self.__render()
        self.__reset_variables()

    def __reset_variables(self):
        """Sets running to true.
        """
        self.__running = True

    def __check_events(self):
        """Checks user events.
        """
        for event in self.__event_queue.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__renderer.main_menu_button.collidepoint(event.pos):
                    self.__running = False

    def __render(self):
        """Gets scores from database and calls renderer to draw them.
        """
        scores = self.__score_repository.get_high_scores()
        self.__renderer.draw("high_scores", scores=scores)
