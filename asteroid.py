import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # Split the asteroid into two smaller asteroids
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            obj1_vector = self.velocity.rotate(random_angle)
            obj2_vector = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            obj1 = Asteroid(self.position.x, self.position.y, new_radius)
            obj2 = Asteroid(self.position.x, self.position.y, new_radius)
            obj1.velocity = obj1_vector * 1.2
            obj2.velocity = obj2_vector * 1.2
            return [obj1, obj2]