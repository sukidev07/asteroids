# python
import pygame
from constants import *
from player import Player
from circleshape import CircleShape

def main():
    # pygame.init()  <- Comment this out or delete it
    pygame.display.init() # <- Add this line
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # <- Keep this line
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) # instantiate a player
    dt = 0  # <- Keep this line
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # inside main()

        screen.fill("black")
        player.draw(screen) # draw the player
        pygame.display.flip() # update the display

        # limit to 60 frames per second
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds



if __name__ == "__main__":
    main()
