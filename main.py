# python
import pygame
from constants import *

def main():
    # pygame.init()  <- Comment this out or delete it
    pygame.display.init() # <- Add this line
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # inside main()

        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
