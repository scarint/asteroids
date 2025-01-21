import pygame
import random
from circleshape import CircleShape
from constants import *

# player class
class Asteroid(CircleShape):
    # Class Variables


    # Class Initiation
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 
                            (255, 255, 255),
                            self.position,
                            self.radius,
                            2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vector1 = pygame.Vector2(0, 0)
        vector1 = self.velocity.rotate(-angle)
        vector2 = pygame.Vector2(0, 0)
        vector2 = self.velocity.rotate(angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = vector1 * 1.2
        asteroid2.velocity = vector2 * 1.2

        