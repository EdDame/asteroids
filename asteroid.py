import pygame
import random
from circleshape import CircleShape
from player import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        old_radius = self.radius
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20, 50)
        ast_angle_1, ast_angle_2 = self.velocity.rotate(rand_angle), self.velocity.rotate(-rand_angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        new_ast_1, new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius), Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_1.velocity = ast_angle_1 * 1.2
        new_ast_2.velocity = ast_angle_2 * 1.2
        #logic for splitting asteroids