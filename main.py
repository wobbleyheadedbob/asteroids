from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

def main():
    pygame.init()
    print("Starting Asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
 
    asteroids = pygame.sprite.Group() # All the asteroid objects that are spawned
    updatable = pygame.sprite.Group() # All the objects that can be updated
    drawable = pygame.sprite.Group() # All the objects that can be drawn
    
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
        
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black", rect=None, special_flags=0)

        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
                if asteroid.collides_with(player):
                    raise SystemExit("Game over!")

        pygame.display.flip()
        
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()