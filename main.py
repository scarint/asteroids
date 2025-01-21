# this allows us to use code from the open-source pygame library throughout this file
import pygame

import sys

# import constants
from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # print(f"Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0
    
    # pygame groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Group Assignments
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # Instantiate objects
    player = Player(SCREEN_WIDTH / 2, 
                    SCREEN_HEIGHT / 2, )
    asteroid_field = AsteroidField()

    game_loop = True

    while game_loop:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If window closed
                return


        screen.fill((0,0,0)) # Black screen



        for item in updatable:
            item.update(dt)
 
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print(f"Game over!")
                sys.exit()
            for bullet in shots:
                if asteroid.is_colliding(bullet):
                    asteroid.split()
                    bullet.kill()


        for item in drawable:
            item.draw(screen)



        pygame.display.flip()




        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
