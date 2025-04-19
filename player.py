import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.color = (255, 255, 255)  # White color
        self.speed = PLAYER_SPEED
        self.rotation = 0

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.angle = (self.angle + dx + dy) % 360

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # Draw the triangle representing the player
        points = self.triangle()
        pygame.draw.polygon(screen, self.color, points, 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Rotate left
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            # Rotate right
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            # Move forward
            self.move(dt)
        if keys[pygame.K_s]:
            # Move backward
            self.move(-dt)
        if keys[pygame.K_ESCAPE]:   # Exit the game
            pygame.quit()
            exit()
    
     