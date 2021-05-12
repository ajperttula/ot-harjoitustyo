import pygame
from ui.renderers.renderer import Renderer
from config import CELL_SIZE, CORNER, TEXT_COLOR


class GameRenderer(Renderer):
    """Class responsible for rendering gameplay window.

    Args:
        Renderer: Inherited renderer class.

    Attributes:
        level (Level): Handles events on the gameplay grid.
    """
    def __init__(self, display, level: "Level"):
        """Creates a new game_renderer and sets attributes.

        Args:
            display: Pygame display object.
            level (Level): Handles events on the gameplay grid.
        """
        super().__init__(display)
        self.__level = level

    def draw(self, game_over):
        """Draws the gameplay view.

        Args:
            game_over (bool): States if game is over or not.
        """
        self._draw_background()
        self.__draw_block()
        self.__draw_next_block()
        self.__draw_grid()
        self.__draw_score()
        self._draw_button(self.main_menu_button, "Main menu")
        if game_over:
            self.__draw_game_over()
        self._init_changes()

    def __draw_block(self):
        """Draws the block that is falling.
        """
        def position_is_block(row: int, col: int) -> bool:
            """Checks if given position in block's shape list has value 1.

            Args:
                row (int): Row number in the block's shape list.
                col (int): Column number in the block's shape list.

            Returns:
                bool: True if given position is 1, else False.
            """
            return self.__level.block.shape[row][col] == 1

        for row in range(self.__level.block.height()):
            for col in range(self.__level.block.width()):
                if position_is_block(row, col):
                    self.__draw_rectangle("block", row, col, self.__level.block.color)

    def __draw_next_block(self):
        """Draws text 'next' and shape of the next block.
        """
        def position_is_block(row: int, col: int) -> bool:
            """Checks if given position in next block's shape list has value 1.

            Args:
                row (int): Row number in the next block's shape list.
                col (int): Column number in the next block's shape list.

            Returns:
                bool: True if given position is 1, else False.
            """
            return self.__level.block.next_shape[row][col] == 1

        text = self._font_small.render("next:", True, TEXT_COLOR)
        self._display.blit(text, (290, 100))

        for row in range(self.__level.block.next_height()):
            for col in range(self.__level.block.next_width()):
                if position_is_block(row, col):
                    self.__draw_rectangle("next_block", row, col, self.__level.block.next_color)
                    self.__draw_rectangle("next_block", row, col, self.__level.grid.color, 1)

    def __draw_grid(self):
        """Draws the gameplay grid.

        First, the occupied grid coordinates are drawn with the color
        of the block on those coordinates.
        Then, a grid is drawn on top of that.
        """
        def position_is_occupied(row: int, col: int) -> bool:
            """Checks if given position on the grid is occupied.

            Position is occupied if that grid coordinate value is not zero.

            Args:
                row (int): Grid row number.
                col (int): Grid column number.

            Returns:
                bool: True if position is occupied, else False.
            """
            return self.__level.grid[row][col] != 0

        for row in range(self.__level.grid.height):
            for col in range(self.__level.grid.width):
                if position_is_occupied(row, col):
                    color = self.__level.grid[row][col]
                    self.__draw_rectangle("grid", row, col, color)
                self.__draw_rectangle("grid", row, col, self.__level.grid.color, 1)

    def __draw_score(self):
        """Draws score text and current score.
        """
        score = self._font_small.render(f"score: {self.__level.score.score}", True, TEXT_COLOR)
        self._display.blit(score, (290, 20))

    def __draw_game_over(self):
        """Draws game over text and instructions to start a new game.
        """
        title = self._font_big.render("GAME OVER", True, TEXT_COLOR)
        title_position = ((self._display_width-title.get_width())/2,
                          (self._display_height-title.get_height())/2)

        text = self._font_small.render("Press ENTER for new game", True, TEXT_COLOR)
        position = ((self._display_width-text.get_width())/2,
                    title_position[1]+title.get_height()+10)

        self._display.blit(title, title_position)
        self._display.blit(text, position)

    def __draw_rectangle(self, name: str, row: int, col: int, color: tuple, border=0):
        """Draws a rectangle shape based on arguments given.

        Args:
            name (str): Which object to draw.
            row (int): Y coordinate.
            col (int): X coordinate.
            color (tuple): Color of the rectangle as RGB-value.
            border (int, optional): Determines the border width.
                If not given, the whole rectangle is filled with color. Defaults to 0.
        """
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
