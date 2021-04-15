import pygame

class Render:
    def __init__(self, display, level):
        self.__display = display
        self.__level = level

    def draw(self):
        self.__display.fill((255,255,255))
        self.__draw_block()
        self.__draw_grid()
        self.__init_changes()

    def __draw_block(self):
        for i in range(self.__level.block.height):
            for j in range(self.__level.block.width):
                if self.__level.block.shape[i][j] == 1:
                    pygame.draw.rect(
                        self.__display,
                        self.__level.block.color,
                        pygame.Rect(self.__level.block.x+j*25, self.__level.block.y+i*25, 25, 25)
                    )

    def __draw_grid(self):
        for i in range(20):
            for j in range(10):
                if self.__level.grid[i][j] != 0:
                    color = self.__level.grid[i][j]
                    pygame.draw.rect(
                        self.__display,
                        color,
                        pygame.Rect(20+j*25, 20+i*25, 25, 25)
                    )
                pygame.draw.rect(
                    self.__display,
                    (120,120,120),
                    pygame.Rect(20+j*25, 20+i*25, 25, 25),
                    1
                )
            
    def __init_changes(self):
        pygame.display.flip()