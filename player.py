import pygame 
from circleshape import CircleShape
from constants import *
from shot import Shot

# player class
class Player(CircleShape):
    # Class Variables

    # Class Initiation
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.__shot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 
                            (255, 255, 255), 
                            self.triangle(), 
                            2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1 )
            #print("a pressed")
        if keys[pygame.K_d]:
            self.rotate(dt)
            #print("d pressed")
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1 )
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.__shot_timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        if self.position.x == 0:
            self.position.x = SCREEN_WIDTH
        if self.position.x == SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y == 0:
            self.position.y = SCREEN_HEIGHT
        if self.position.y == SCREEN_HEIGHT:
            self.position.y = 0

    def shoot(self):
        if self.__shot_timer > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

        self.__shot_timer = PLAYER_SHOOT_COOLDOWN
