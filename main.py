from constants import *
from player import Player
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

def main():
    pygame.init()
    print("Starting Asteroids!")

    updatable = pygame.sprite.Group() # All the objects that can be updated
    drawable = pygame.sprite.Group() # All the objects that can be drawn
    
    # Set both groups as containers for the Player
    Player.containers = (updatable, drawable)

    my_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    game_clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black", rect=None, special_flags=0)

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()