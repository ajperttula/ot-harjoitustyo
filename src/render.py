import pygame


class Render:
    def __init__(self, display, block, grid, cell_size, corner, bg_color):
        self.__display = display
        self.__block = block
        self.__grid = grid
        self.__cell_size = cell_size
        self.__corner = corner
        self.__bg_color = bg_color

    def draw(self):
        self.__draw_background()
        self.__draw_block()
        self.__draw_grid()
        self.__init_changes()

    def __draw_background(self):
        self.__display.fill(self.__bg_color)

    def __draw_block(self):
        def position_is_block(row, col):
            return self.__block.shape[row][col] == 1

        for row in range(self.__block.height):
            for col in range(self.__block.width):
                if position_is_block(row, col):
                    self.__draw_rectangle("block", row, col, self.__block.color)

    def __draw_grid(self):
        def position_is_occupied(row, col):
            return self.__grid.grid[row][col] != 0

        for row in range(self.__grid.height):
            for col in range(self.__grid.width):
                if position_is_occupied(row, col):
                    color = self.__grid.grid[row][col]
                    self.__draw_rectangle("grid", row, col, color)
                self.__draw_rectangle("grid", row, col, self.__grid.color, 1)

    def __init_changes(self):
        pygame.display.flip()

    def __draw_rectangle(self, name, row, col, color, border=0):
        if name == "block":
            x_pos = self.__corner + (self.__block.x_pos+col) * self.__cell_size
            y_pos = self.__corner + (self.__block.y_pos+row) * self.__cell_size
        elif name == "grid":
            x_pos = self.__corner + col * self.__cell_size
            y_pos = self.__corner + row * self.__cell_size
        width = self.__cell_size
        height = self.__cell_size

        pygame.draw.rect(self.__display,
                         color,
                         pygame.Rect(x_pos, y_pos, width, height),
                         border)
