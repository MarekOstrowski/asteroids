import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def split(self):
        random_angle = random.uniform(20, 50)


        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            self.kill()
            self.spawn(self.radius - ASTEROID_MIN_RADIUS, self.position ,self.velocity.rotate(random_angle) * 1.2)
            self.spawn(self.radius - ASTEROID_MIN_RADIUS, self.position ,self.velocity.rotate(-random_angle))
            #  self.spawn(self.radius - ASTEROID_MIN_RADIUS, self.position ,self.velocity.rotate(-random_angle*random_angle))
        





