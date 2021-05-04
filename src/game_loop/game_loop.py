import sys
import pygame


class GameLoop:
    """Class responsible for organizing game events.

    This class ties together the the game logic and it's elements.

    Attributes:
        level (Level): Handles events on the gameplay grid.
        clock (Clock): Controls game frame rate.
        event_queue (Event): Handles user events.
        renderer (GameRenderer): Draws the game display.
        score_repository (ScoreRepository): Handles communication with score database.
    """
    def __init__(self, level: "Level", clock: "Clock", event_queue: "Event",
                 renderer: "GameRenderer", score_repository: "ScoreRepository"):
        """Constructor creates a new gameloop object and sets attributes.

        Args:
            level (Level): Level object.
            clock (Clock): Clock object.
            event_queue (Event): Event object.
            renderer (GameRenderer): GameRenderer object.
            score_repository (ScoreRepository): ScoreRepository object.
        """
        self.__level = level
        self.__clock = clock
        self.__event_queue = event_queue
        self.__renderer = renderer
        self.__score_repository = score_repository
        self.__running = True
        self.__player = ""

    def new_game(self, player: str):
        """Starts a new game.

        Before starting the actual game loop, this method resets all it's elements
        by calling reset_game method.

        Args:
            player (str):
                Player name is used to store it together with the score
                to the database when game is over.
        """
        self.__player = player
        self.__reset_game()
        self.__start()

    def __start(self):
        """Checks user inputs, game state and draws the display.
        """
        while self.__running:
            self.__check_counter()
            self.__check_game_over()
            self.__check_score()
            self.__check_events()
            self.__render_game()
            self.__clock.tick(60)

    def __finished(self):
        """Checks user inputs and draws the display.
        """
        while self.__running:
            self.__check_events()
            self.__render_game()

    def __check_game_over(self):
        """Checks game state.

        If game is over, score and player name are stored and
        finished loop is initiated.
        """
        if self.__level.game_over:
            self.__save_score()
            self.__finished()

    def __save_score(self):
        """Saves player name and score to database if score is greater than zero.
        """
        score = self.__level.score.score
        if score:
            self.__score_repository.save_score(self.__player, score)

    def __check_counter(self):
        """Checks if it is time for block to move.
        """
        if self.__level.pace.check_counter():
            self.__level.lower_block()

    def __check_score(self):
        """Checks if it is time to increase difficulty.
        """
        if self.__level.score.check_score():
            self.__level.pace.increase_difficulty()

    def __check_events(self):
        """Checks user inputs.
        """
        for event in self.__event_queue.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.__check_key_down_events(event)
            self.__check_key_up_events(event)
            self.__check_mouse_click_events(event)

    def __check_key_down_events(self, event):
        """Checks key down inputs.

        Args:
            event: Single user event, like key press etc.
        """
        if event.type == pygame.KEYDOWN:
            if not self.__level.game_over:
                if event.key == pygame.K_LEFT:
                    self.__level.move_block(-1)
                if event.key == pygame.K_RIGHT:
                    self.__level.move_block(1)
                if event.key == pygame.K_UP:
                    self.__level.rotate_block()
                if event.key == pygame.K_DOWN:
                    self.__level.increase_speed()
                if event.key == pygame.K_SPACE:
                    self.__level.drop_block()
            if event.key == pygame.K_RETURN:
                self.new_game(self.__player)

    def __check_key_up_events(self, event):
        """Checks key up inputs.

        Args:
            event: Single user event, like key press etc.
        """
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.__level.decrease_speed()

    def __check_mouse_click_events(self, event):
        """Checks mouse click inputs.

        Args:
            event: Single user event, like key press etc.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.__renderer.main_menu_button.collidepoint(event.pos):
                self.__running = False

    def __render_game(self):
        """Calls renderer to draw current game state.
        """
        self.__renderer.draw()

    def __reset_game(self):
        """Resets game running and calls level to reset it's elements.
        """
        self.__running = True
        self.__level.reset_game_state()
