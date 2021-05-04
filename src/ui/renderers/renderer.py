import pygame


BG_COLOR = (235, 235, 235)
TEXT_COLOR = (0, 0, 0)


class Renderer:
    def __init__(self, display):
        self._display = display
        self._display_height = display.get_height()
        self._display_width = display.get_width()
        self._font_small = pygame.font.SysFont("Lucida Console", 20)
        self._font_big = pygame.font.SysFont("Lucida Console", 50)
        self.main_menu_button = self._create_button(290, 480, 120, 40)

    def _draw_background(self):
        self._display.fill(BG_COLOR)

    def _init_changes(self):
        pygame.display.flip()

    def _create_button(self, pos_x, pos_y, width, height):
        return pygame.Rect(pos_x, pos_y, width, height)

    def _draw_button(self, button, text):
        text = self._font_small.render(text, True, TEXT_COLOR)
        pygame.draw.rect(self._display,
                         (255, 0, 0),
                         button)
        text_width = text.get_width()
        text_height = text.get_height()
        pos_x = button.x + (button.width-text_width)/2
        pos_y = button.y + (button.height-text_height)/2
        self._display.blit(text, (pos_x, pos_y))
