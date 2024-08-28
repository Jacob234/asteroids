import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20.0, 50.0)
            inv_random_angle = -1 * random_angle
            vector_1 = self.velocity.rotate(random_angle)
            vector_2 = self.velocity.rotate(inv_random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_one.velocity = vector_1 * 1.2

            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two.velocity = vector_2 * 1.2
        



