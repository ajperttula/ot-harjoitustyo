import pygame
from renderers.renderer import Renderer


TEXT_COLOR = (0, 0, 0)


class UIRenderer(Renderer):
    def __init__(self, display):
        super().__init__(display)
        self.__create_buttons()

    def draw(self, page, player_name="", scores=""):
        self._draw_background()
        if page == "main":
            self.__draw_buttons()
        elif page == "name_input":
            self.__draw_text_input(player_name)
        elif page == "high_scores":
            self.__draw_score_table(scores)
            self._draw_button(self._main_menu_button, "Main menu")
        self._init_changes()

    def __create_buttons(self):
        display_height = self._display.get_height()
        display_width = self._display.get_width()

        self.__new_game_button = self._create_button((display_width-200)/2,
                                                     (display_height-40)/2,
                                                     200,
                                                     40)

        self.__high_scores_button = self._create_button(self.__new_game_button.x,
                                                        self.__new_game_button.y+50,
                                                        200,
                                                        40)

        self.__exit_button = self._create_button(self.__new_game_button.x,
                                                 self.__high_scores_button.y+50,
                                                 200,
                                                 40)

    def __draw_buttons(self):
        self._draw_button(self.__new_game_button, "New game")
        self._draw_button(self.__high_scores_button, "High scores")
        self._draw_button(self.__exit_button, "Exit")

    def __draw_score_table(self, scores):
        title_text = self._font_small.render("TOP 10 Scores", True, TEXT_COLOR)
        self._display.blit(title_text, ((self._display.get_width()-title_text.get_width())/2, 30))

        rank_text = self._font_small.render("Rank", True, TEXT_COLOR)
        self._display.blit(rank_text, (60, 100))

        player_text = self._font_small.render("Player", True, TEXT_COLOR)
        self._display.blit(player_text, (130, 100))

        score_text = self._font_small.render("Score", True, TEXT_COLOR)
        self._display.blit(score_text, (300, 100))

        pos_y = 100 + rank_text.get_height() + 20

        for result in scores:
            rank = self._font_small.render(f"{result[0]}", True, TEXT_COLOR)
            self._display.blit(rank, (60, pos_y))

            player = self._font_small.render(f"{result[1]}", True, TEXT_COLOR)
            self._display.blit(player, (130, pos_y))

            score = self._font_small.render(f"{result[2]}", True, TEXT_COLOR)
            self._display.blit(score, (300, pos_y))

            pos_y += rank.get_height()+10

    def __draw_text_input(self, player_name):
        display_height = self._display.get_height()
        display_width = self._display.get_width()
        text = self._font_small.render("Player name:", True, TEXT_COLOR)
        player_name = self._font_small.render(player_name, True, TEXT_COLOR)
        pos_x, pos_y = ((display_width-text.get_width())/2, (display_height-text.get_height())/2)
        input_box = pygame.Rect((display_width-200)/2, pos_y+text.get_height()+10, 200, 30)
        input_text_pos = (input_box.x+5, input_box.y+5)

        self._display.blit(text, (pos_x, pos_y))
        pygame.draw.rect(self._display,
                         TEXT_COLOR,
                         input_box, 1)
        self._display.blit(player_name, input_text_pos)

    @property
    def new_game_button(self):
        return self.__new_game_button

    @property
    def high_scores_button(self):
        return self.__high_scores_button

    @property
    def exit_button(self):
        return self.__exit_button

    @property
    def main_menu_button(self):
        return self._main_menu_button
