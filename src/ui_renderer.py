import pygame


BG_COLOR = (235, 235, 235)
TEXT_COLOR = (0, 0, 0)


class UIRenderer:
    def __init__(self, display):
        self.__display = display
        self.__font_small = pygame.font.SysFont("Lucida Console", 20)
        self.__new_game_button = self.__create_new_game_button()
        self.__exit_button = self.__create_exit_button()

    def draw_menu(self):
        self.__draw_background()
        self.__draw_buttons()
        self.__init_changes()

    def draw_name_input(self, player_name):
        self.__draw_background()
        self.__draw_text_input(player_name)
        self.__init_changes()

    def __draw_background(self):
        self.__display.fill(BG_COLOR)

    def __draw_buttons(self):
        new_game_text = self.__font_small.render("New Game", True, TEXT_COLOR)
        pygame.draw.rect(self.__display,
                         (255, 0, 0),
                         self.__new_game_button)
        self.__display.blit(new_game_text, (self.__new_game_button.x+5, self.__new_game_button.y+5))

        exit_text = self.__font_small.render("Exit", True, TEXT_COLOR)
        pygame.draw.rect(self.__display,
                         (255, 0, 0),
                         self.__exit_button)
        self.__display.blit(exit_text, (self.__exit_button.x+5, self.__exit_button.y+5))

    def __create_new_game_button(self):
        display_height = self.__display.get_height()
        display_width = self.__display.get_width()
        return pygame.Rect((display_width-200)/2, (display_height-40)/2, 200, 40)

    def __create_exit_button(self):
        return pygame.Rect(self.__new_game_button.x, self.__new_game_button.y+50, 200, 40)

    def __draw_text_input(self, player_name):
        display_height = self.__display.get_height()
        display_width = self.__display.get_width()
        text = self.__font_small.render("Player name:", True, TEXT_COLOR)
        player_name = self.__font_small.render(player_name, True, TEXT_COLOR)
        pos_x, pos_y = ((display_width-text.get_width())/2, (display_height-text.get_height())/2)
        input_box = pygame.Rect((display_width-200)/2, pos_y+text.get_height()+10, 200, 30)
        input_text_pos = (input_box.x+5, input_box.y+5)

        self.__display.blit(text, (pos_x, pos_y))
        pygame.draw.rect(self.__display,
                         TEXT_COLOR,
                         input_box, 1)
        self.__display.blit(player_name, input_text_pos)

    def __init_changes(self):
        pygame.display.flip()

    @property
    def new_game_button(self):
        return self.__new_game_button

    @property
    def exit_button(self):
        return self.__exit_button
