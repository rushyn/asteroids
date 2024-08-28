from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        print("__init__")
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = 50
        super().__init__(x, y, PLAYER_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
