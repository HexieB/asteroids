# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from AsteroidField import AsteroidField

def main():
    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
    # Clear the screen
        screen.fill((0, 0, 0))
    
    # Update positions
        updatable.update(dt)
    
    # Check for collisions
        for sprite in asteroids:
            if sprite.get_collide(player):
                print("Game over!")
                pygame.quit()
                sys.exit()
    
    # Draw everything
        for sprite in drawable:
            sprite.draw(screen)
    
    # Update the display
        pygame.display.flip()
    
    # Calculate dt for next frame (only call tick once)
        dt = clock.tick(60) / 1000.0
    
if __name__ == "__main__":
    main()