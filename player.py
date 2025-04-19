import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.color = (255, 255, 255)  # White color
        self.speed = 5
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
        
  