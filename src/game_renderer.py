import pygame


CELL_SIZE = 25
CORNER = 20
BG_COLOR = (235, 235, 235)
TEXT_COLOR = (0, 0, 0)


class GameRenderer:
    def __init__(self, display, level):
        self.__display = display
        self.__level = level
        self.__font_small = pygame.font.SysFont("Lucida Console", 20)
        self.__font_big = pygame.font.SysFont("Lucida Console", 50)
        self.__main_menu_button = self.__create_main_menu_button()

    def draw(self):
        self.__draw_background()
        self.__draw_block()
        self.__draw_next_block()
        self.__draw_grid()
        self.__draw_score()
        self.__draw_main_menu()
        if self.__level.game_over:
            self.__draw_game_over()
        self.__init_changes()

    def __draw_background(self):
        self.__display.fill(BG_COLOR)

    def __draw_block(self):
        def position_is_block(row, col):
            return self.__level.block.shape[row][col] == 1

        for row in range(self.__level.block.height):
            for col in range(self.__level.block.width):
                if position_is_block(row, col):
                    self.__draw_rectangle("block", row, col, self.__level.block.color)

    def __draw_next_block(self):
        def position_is_block(row, col):
            return self.__level.block.next_shape[row][col] == 1

        text = self.__font_small.render("next:", True, TEXT_COLOR)
        self.__display.blit(text, (290, 100))

        for row in range(self.__level.block.next_height):
            for col in range(self.__level.block.next_width):
                if position_is_block(row, col):
                    self.__draw_rectangle("next_block", row, col, self.__level.block.next_color)
                    self.__draw_rectangle("next_block", row, col, self.__level.grid.color, 1)

    def __draw_grid(self):
        def position_is_occupied(row, col):
            return self.__level.grid.grid[row][col] != 0

        for row in range(self.__level.grid.height):
            for col in range(self.__level.grid.width):
                if position_is_occupied(row, col):
                    color = self.__level.grid.grid[row][col]
                    self.__draw_rectangle("grid", row, col, color)
                self.__draw_rectangle("grid", row, col, self.__level.grid.color, 1)

    def __draw_score(self):
        score = self.__font_small.render(f"score: {self.__level.score.score}", True, TEXT_COLOR)
        self.__display.blit(score, (290, 20))

    def __draw_game_over(self):
        display_height = self.__display.get_height()
        display_width = self.__display.get_width()
        game_over = self.__font_big.render("GAME OVER", True, TEXT_COLOR)
        text_width = game_over.get_width()
        text_height = game_over.get_height()
        position = ((display_width-text_width)/2, (display_height-text_height)/2)
        instruction = self.__font_small.render("Press ENTER for new game", True, TEXT_COLOR)
        position2 = (position[0], position[1]+text_height+10)

        self.__display.blit(game_over, position)
        self.__display.blit(instruction, position2)

    def __draw_main_menu(self):
        main_menu_text = self.__font_small.render("Main menu", True, TEXT_COLOR)
        pygame.draw.rect(self.__display,
                         (255, 0, 0),
                         self.__main_menu_button)
        self.__display.blit(main_menu_text, (self.__main_menu_button.x+5, self.__main_menu_button.y+5))

    def __init_changes(self):
        pygame.display.flip()

    def __create_main_menu_button(self):
        return pygame.Rect(290, 480, 120, 40)

    def __draw_rectangle(self, name, row, col, color, border=0):
        if name == "block":
            x_pos = CORNER + (self.__level.block.x_pos+col) * CELL_SIZE
            y_pos = CORNER + (self.__level.block.y_pos+row) * CELL_SIZE
        elif name == "next_block":
            x_pos = 305 + col * CELL_SIZE
            y_pos = 150 + row * CELL_SIZE
        elif name == "grid":
            x_pos = CORNER + col * CELL_SIZE
            y_pos = CORNER + row * CELL_SIZE
        width = CELL_SIZE
        height = CELL_SIZE

        pygame.draw.rect(self.__display,
                         color,
                         pygame.Rect(x_pos, y_pos, width, height),
                         border)

    @property
    def main_menu_button(self):
        return self.__main_menu_button