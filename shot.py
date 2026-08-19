from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, surface: object):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
