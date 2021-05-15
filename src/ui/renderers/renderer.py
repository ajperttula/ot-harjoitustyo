import pygame
from config import BG_COLOR, TEXT_COLOR, BUTTON_COLOR


class Renderer:
    """Class responsible for rendering the display.

    Atributes:
        display: Pygame display object.
        display_height: Display height in pixels.
        display_width: Display width in pixels.
        font_small: Pygame font to render small text.
        font_big: Pygame font to render bigger text.
        main_menu_button: Pygame rect object to represent a button.
    """
    def __init__(self, display):
        """Creates a new renderer and sets attributes.

        Args:
            display: Pygame display object.
        """
        self._display = display
        self._display_height = display.get_height()
        self._display_width = display.get_width()
        self._font_small = pygame.font.SysFont("Lucida Console", 20)
        self._font_big = pygame.font.SysFont("Lucida Console", 50)
        self.main_menu_button = self._create_button(290, 480, 120, 40)

    def _draw_background(self):
        """Fills display background with BG_COLOR.
        """
        self._display.fill(BG_COLOR)

    def _init_changes(self):
        """Updates the display surface.
        """
        pygame.display.flip()

    def _create_button(self, pos_x: int, pos_y: int, width: int, height: int):
        """Creates a pygame rect object to represent a button.

        Args:
            pos_x (int): Distance from the left border of the display.
            pos_y (int): Distance from the top border of the display.
            width (int): Width of the button in pixels.
            height (int): Height of the button in pixels.

        Returns:
            Rect: Pygame rect object.
        """
        return pygame.Rect(pos_x, pos_y, width, height)

    def _draw_button(self, button, text: str):
        """Draws a button to the display surface.

        Text is drawn on the middle of the button.

        Args:
            button: Pygame rect object.
            text (str): Text on the button.
        """
        text = self._font_small.render(text, True, TEXT_COLOR)
        pygame.draw.rect(self._display,
                         BUTTON_COLOR,
                         button,
                         0,
                         3)
        text_width = text.get_width()
        text_height = text.get_height()
        pos_x = button.x + (button.width-text_width)/2
        pos_y = button.y + (button.height-text_height)/2
        self._display.blit(text, (pos_x, pos_y))
