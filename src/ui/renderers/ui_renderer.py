import pygame
from ui.renderers.renderer import Renderer


TEXT_COLOR = (0, 0, 0)


class UIRenderer(Renderer):
    """Class responsible for rendering user interface windows.

    Args:
        Renderer: Inherited renderer class.

    Attributes:
        new_game_button: Pygame rect object to represent a button.
        high_scores_button: Pygame rect object to represent a button.
        exit_button: Pygame rect object to represent a button.
    """
    def __init__(self, display):
        """Creates a new ui_renderer and sets attributes.

        Args:
            display: Pygame display object.
        """
        super().__init__(display)
        self.__create_buttons()

    def draw(self, page: str, player_name="", scores=[]):
        """Draws background, buttons, titles and results if any.

        Args:
            page (str): To determine, which page content to draw.
            player_name (str, optional): To draw player name. Defaults to "".
            scores (list, optional): List containing top 10 scores. Defaults to [].
        """
        self._draw_background()
        if page == "main":
            self.__draw_buttons()
        elif page == "name_input":
            self.__draw_text_input(player_name)
        elif page == "high_scores":
            self.__draw_score_table(scores)
            self._draw_button(self.main_menu_button, "Main menu")
        self._init_changes()

    def __create_buttons(self):
        """Creates main manu buttons.
        """
        self.new_game_button = self._create_button((self._display_width-200)/2,
                                                   (self._display_height-40)/2,
                                                   200,
                                                   40)

        self.high_scores_button = self._create_button(self.new_game_button.x,
                                                      self.new_game_button.y+50,
                                                      200,
                                                      40)

        self.exit_button = self._create_button(self.new_game_button.x,
                                               self.high_scores_button.y+50,
                                               200,
                                               40)

    def __draw_buttons(self):
        """Draws main menu buttons.
        """
        self._draw_button(self.new_game_button, "New game")
        self._draw_button(self.high_scores_button, "High scores")
        self._draw_button(self.exit_button, "Exit")

    def __draw_score_table(self, scores: list):
        """Draws score table.

        Titles are drawn on fixed positions on the screen. Then the
        score list is iterated and drawn having 30 pixels between
        each other.

        Args:
            scores (list): Contains top 10 scores in tuples (rank, player name, score)
        """
        title = self._font_small.render("TOP 10 Scores", True, TEXT_COLOR)
        self._display.blit(title, ((self._display.get_width()-title.get_width())/2, 30))

        rank = self._font_small.render("Rank", True, TEXT_COLOR)
        self._display.blit(rank, (60, 100))

        player = self._font_small.render("Player", True, TEXT_COLOR)
        self._display.blit(player, (130, 100))

        score = self._font_small.render("Score", True, TEXT_COLOR)
        self._display.blit(score, (300, 100))

        pos_y = 100 + rank.get_height()

        for result in scores:
            pos_y += 30

            rank = self._font_small.render(f"{result[0]}", True, TEXT_COLOR)
            self._display.blit(rank, (60, pos_y))

            player = self._font_small.render(f"{result[1]}", True, TEXT_COLOR)
            self._display.blit(player, (130, pos_y))

            score = self._font_small.render(f"{result[2]}", True, TEXT_COLOR)
            self._display.blit(score, (300, pos_y))

    def __draw_text_input(self, player_name: str):
        """Draws text input box.

        Args:
            player_name (str): player name, which player is inputting.
        """
        title = self._font_small.render("Player name:", True, TEXT_COLOR)
        title_position = ((self._display_width-title.get_width())/2,
                          (self._display_height-title.get_height())/2)

        player_name = self._font_small.render(player_name, True, TEXT_COLOR)
        input_box = pygame.Rect((self._display_width-200)/2,
                                title_position[1]+title.get_height()+10,
                                200,
                                30)
        input_text_pos = (input_box.x+(input_box.width-player_name.get_width())/2,
                          input_box.y+(input_box.height-player_name.get_height())/2)

        self._display.blit(title, title_position)
        pygame.draw.rect(self._display,
                         TEXT_COLOR,
                         input_box, 1)
        self._display.blit(player_name, input_text_pos)
