import pygame


CELL_SIZE = 25
CORNER = 20
BG_COLOR = (255, 255, 255)


class Renderer:
    def __init__(self, display, block, grid, score):
        self.__display = display
        self.__block = block
        self.__grid = grid
        self.__score = score
        self.__font = pygame.font.SysFont("Lucida Console", 20)

    def draw(self):
        self.__draw_background()
        self.__draw_block()
        self.__draw_grid()
        self.__init_changes()

    def __draw_background(self):
        self.__display.fill(BG_COLOR)

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
        score = self.__font.render(f"score: {self.__score.score}", True, (0, 0, 0))
        self.__display.blit(score, (280, 20))
        pygame.display.flip()

    def __draw_rectangle(self, name, row, col, color, border=0):
        if name == "block":
            x_pos = CORNER + (self.__block.x_pos+col) * CELL_SIZE
            y_pos = CORNER + (self.__block.y_pos+row) * CELL_SIZE
        elif name == "grid":
            x_pos = CORNER + col * CELL_SIZE
            y_pos = CORNER + row * CELL_SIZE
        width = CELL_SIZE
        height = CELL_SIZE

        pygame.draw.rect(self.__display,
                         color,
                         pygame.Rect(x_pos, y_pos, width, height),
                         border)
