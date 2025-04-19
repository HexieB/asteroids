# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    dt = 0
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000.0
        

if __name__ == "__main__":
    main()