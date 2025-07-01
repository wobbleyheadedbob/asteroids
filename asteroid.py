from constants import *
from circleshape import CircleShape
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position , self.radius)

    def move(self, dt):
       self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)