from circleshape import *
from constants import *

class shot(CircleShape):
    def __init__(self, position, radius):
        #print("__init__")
        self.position = position
        self.radius = radius
        super().__init__(self.position.x, self.position.y, self.radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt