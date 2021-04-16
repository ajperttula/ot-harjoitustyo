import pygame


class Render:
    def __init__(self, display, block, level, cell_size, corner):
        self.__display = display
        self.__block = block
        self.__level = level
        self.__cell_size = cell_size
        self.__corner = corner

    def draw(self):
        self.__draw_background()
        self.__draw_block()
        self.__draw_grid()
        self.__init_changes()

    def __draw_background(self):
        self.__display.fill((255, 255, 255))

    def __draw_block(self):
        for row in range(self.__block.height):
            for col in range(self.__block.width):
                if self.__block.shape[row][col] == 1:
                    pygame.draw.rect(
                        self.__display,
                        self.__block.color,
                        pygame.Rect(
                            self.__corner+(self.__block.x_value +
                                           col)*self.__cell_size,
                            self.__corner+(self.__block.y_value +
                                           row)*self.__cell_size,
                            self.__cell_size,
                            self.__cell_size
                        )
                    )

    def __draw_grid(self):
        for row in range(20):
            for col in range(10):
                if self.__level.grid[row][col] != 0:
                    color = self.__level.grid[row][col]
                    pygame.draw.rect(
                        self.__display,
                        color,
                        pygame.Rect(
                            self.__corner+col*self.__cell_size,
                            self.__corner+row*self.__cell_size,
                            self.__cell_size,
                            self.__cell_size
                        )
                    )
                pygame.draw.rect(
                    self.__display,
                    (120, 120, 120),
                    pygame.Rect(
                        self.__corner+col*self.__cell_size,
                        self.__corner+row*self.__cell_size,
                        self.__cell_size,
                        self.__cell_size
                    ),
                    1
                )

    def __init_changes(self):
        pygame.display.flip()
