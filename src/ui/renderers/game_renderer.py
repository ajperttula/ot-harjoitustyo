import pygame
from ui.renderers.renderer import Renderer


CELL_SIZE = 25
CORNER = 20
TEXT_COLOR = (0, 0, 0)


class GameRenderer(Renderer):
    def __init__(self, display, level):
        super().__init__(display)
        self.__level = level

    def draw(self):
        self._draw_background()
        self.__draw_block()
        self.__draw_next_block()
        self.__draw_grid()
        self.__draw_score()
        self._draw_button(self.main_menu_button, "Main menu")
        if self.__level.game_over:
            self.__draw_game_over()
        self._init_changes()

    def __draw_block(self):
        def position_is_block(row, col):
            return self.__level.block.shape[row][col] == 1

        for row in range(self.__level.block.height()):
            for col in range(self.__level.block.width()):
                if position_is_block(row, col):
                    self.__draw_rectangle("block", row, col, self.__level.block.color)

    def __draw_next_block(self):
        def position_is_block(row, col):
            return self.__level.block.next_shape[row][col] == 1

        text = self._font_small.render("next:", True, TEXT_COLOR)
        self._display.blit(text, (290, 100))

        for row in range(self.__level.block.next_height()):
            for col in range(self.__level.block.next_width()):
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
        score = self._font_small.render(f"score: {self.__level.score.score}", True, TEXT_COLOR)
        self._display.blit(score, (290, 20))

    def __draw_game_over(self):
        title = self._font_big.render("GAME OVER", True, TEXT_COLOR)
        title_position = ((self._display_width-title.get_width())/2,
                          (self._display_height-title.get_height())/2)

        text = self._font_small.render("Press ENTER for new game", True, TEXT_COLOR)
        position = ((self._display_width-text.get_width())/2,
                    title_position[1]+title.get_height()+10)

        self._display.blit(title, title_position)
        self._display.blit(text, position)

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

        pygame.draw.rect(self._display,
                         color,
                         pygame.Rect(x_pos, y_pos, width, height),
                         border)
