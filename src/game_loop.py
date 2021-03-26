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

class Grid:
    def __init__(self, display, level, block):
        self._display = display
        self._level = level
        self._block = block

    def draw(self):
        for i in range(self._block.height()):
            for j in range(self._block.width()):
                if self._block.shape()[i][j] == 1:
                    pygame.draw.rect(self._display, self._block.color(), pygame.Rect(self._block.x+j*25,self._block.y+i*25,25,25))
                    
        for i in range(20):
            for j in range(10):
                pygame.draw.rect(self._display, (120,120,120), pygame.Rect(20+j*25,20+i*25,25,25), 1)




def main():
    cell_size = 20
    level = [[0 for j in range(10)] for i in range(20)]

    pygame.init()

    display = pygame.display.set_mode((400, 550))
    clock = Clock()
    block = Block(120,20)
    grid = Grid(display, level, block)

    pygame.display.set_caption("TETRIS")
    display.fill((255,255,255))

    event_queue = Event()

    while True:
        for event in event_queue.get():
            if event.type == pygame.QUIT:
                exit()

        grid.draw()

        pygame.display.flip()

if __name__ == "__main__":
    main()