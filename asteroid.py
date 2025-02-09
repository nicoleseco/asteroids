from circleshape import *
import pygame
from constants import *
import random
from main import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        white = (255, 255, 255)
        center = (self.position.x, self.position.y)
        pygame.draw.circle(screen, white, center, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self, asteroids):
        self.kill()
        if self.radius <=ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(random_angle)
            v2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = v1 * 1.2
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2.velocity = v2 * 1.2
            asteroids.add(new_asteroid_1, new_asteroid_2)