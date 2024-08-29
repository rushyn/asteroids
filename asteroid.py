import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        #print("__init__")
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = 50
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angel = random.uniform(20, 50)
        asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid.velocity = self.velocity * 1.2
        asteroid.velocity = self.velocity.rotate(angel)
        asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid.velocity = self.velocity * 1.2
        asteroid.velocity = self.velocity.rotate(-angel)
