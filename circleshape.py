import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        #print("this should not run")
        # sub-classes must override
        pass

    def update(self, dt):
        #print("this should not run")
        # sub-classes must override
        pass

    def collison(self, CircleShape):
        if (self.radius + CircleShape.radius) > self.position.distance_to(CircleShape.position):
            return True
        return False