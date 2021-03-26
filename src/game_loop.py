import pygame
from block import Block

class Clock:
    def __init__(self):
        self.clock = pygame.time.Clock()

    def tick(self):
        self.clock.tick(60)

class Event:
    def get(self):
        return pygame.event.get()

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

class Level:
    def __init__(self):
        self.level = [[0 for j in range(10)] for i in range(20)]
        self.cell_size = 25
        self.block = Block(120,20)

    def move_block(self, dx: int):
        self.block.x += dx * self.cell_size

def main():
    pygame.init()

    display = pygame.display.set_mode((400, 550))

    clock = Clock()
    level = Level()
    event_queue = Event()

    pygame.display.set_caption("TETRIS")

    while True:
        for event in event_queue.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    level.move_block(-1)
                if event.key == pygame.K_RIGHT:
                    level.move_block(1)

        Render(display, level)
        clock.tick()

if __name__ == "__main__":
    main()