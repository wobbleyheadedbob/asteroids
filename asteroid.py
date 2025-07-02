from constants import *
from circleshape import CircleShape
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position , self.radius)

    def move(self, dt):
       self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)
    
    def split(self):
        angle = random.uniform(20, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid_1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid_1.velocity = self.velocity.rotate(angle) * 1.2

        asteroid_2 = Asteroid(self.position.x, self.position.y, radius)
        asteroid_2.velocity = self.velocity.rotate(-angle) * 1.2
        
        self.kill()