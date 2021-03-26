import pygame

class Render:
    def __init__(self, display, level):
        display.fill((255,255,255))
        self.__draw_block(display, level)
        self.__draw_grid(display, level)
        self.__init_changes()

    def __draw_block(self, display, level):
        for i in range(level.block.height):
            for j in range(level.block.width):
                if level.block.shape[i][j] == 1:
                    pygame.draw.rect(display, level.block.color, pygame.Rect(level.block.x+j*25,level.block.y+i*25,25,25))

    def __draw_grid(self, display, level):
        for i in range(20):
            for j in range(10):
                pygame.draw.rect(display, (120,120,120), pygame.Rect(20+j*25,20+i*25,25,25), 1)
            
    def __init_changes(self):
        pygame.display.flip()