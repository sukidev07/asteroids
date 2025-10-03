# python
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    # pygame.init()  <- Comment this out or delete it
    pygame.display.init() # <- Add this line
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # <- Keep this line

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updateable, drawable, asteroids)
    Shot.containers = (updateable, drawable, shots)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) # instantiate a player
    
    dt = 0  # <- Keep this line

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # inside main()

        updateable.update(dt)  # update all updateable objects
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                sys.exit()

        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
                

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()  # update the display


        # limit to 60 frames per second
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds



if __name__ == "__main__":
    main()
