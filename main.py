# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH }")
    print(f"Screen height: {SCREEN_HEIGHT }")


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updateble = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    player.containers = (updateble, drawable)
    Asteroid.containers = (asteroids, updateble, drawable)
    AsteroidField.containers = (updateble)
    shot.containers = (bullets, updateble, drawable)


    game_player = player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    
    run = 1
    while run == 1: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for unit in updateble:
            unit.update(dt)
        
        for unit in drawable:
            unit.draw(screen)

        for asteroid in asteroids:
            if game_player.collison(asteroid) == True:
                print("Game over!")
                event.type == pygame.QUIT
                return
            for bullet in bullets:
                if asteroid.collison(bullet) == True:
                    asteroid.split()
                    bullet.kill()


        pygame.display.flip()
        
        dt = (clock.tick(60)) / 1000
        

        clock.tick(60)


if __name__ == "__main__":
    main()