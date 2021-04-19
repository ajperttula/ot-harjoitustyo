import pygame


class Render:
    def __init__(self, display, block, grid, cell_size, corner, bkgd_color):
        self.__display = display
        self.__block = block
        self.__grid = grid
        self.__cell_size = cell_size
        self.__corner = corner
        self.__bg_color = bkgd_color

    def draw(self):
        self.__draw_background()
        self.__draw_block()
        self.__draw_grid()
        self.__init_changes()

    def __draw_background(self):
        self.__display.fill(self.__bg_color)

    def __draw_block(self):
        for row in range(self.__block.height):
            for col in range(self.__block.width):
                if self.__block.shape[row][col] == 1:
                    pygame.draw.rect(
                        self.__display,
                        self.__block.color,
                        pygame.Rect(
                            self.__corner+(self.__block.x_pos +
                                           col)*self.__cell_size,
                            self.__corner+(self.__block.y_pos +
                                           row)*self.__cell_size,
                            self.__cell_size,
                            self.__cell_size
                        )
                    )

    def __draw_grid(self):
        for row in range(self.__grid.height):
            for col in range(self.__grid.width):
                if self.__grid.grid[row][col] != 0:
                    color = self.__grid.grid[row][col]
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
                    self.__grid.color,
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
