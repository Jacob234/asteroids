# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
pygame.init

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

AsteroidField.containers = (updatable)
Asteroid.containers = (updatable, drawable, asteroids)
Player.containers = (updatable, drawable)
player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
asteroid_belt = AsteroidField()

Shot.containers = (updatable, drawable, shots)



def main():
    dt = 0
    print("Starting asteroids!")


    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(000)

        
        for entity in updatable:
            entity.update(dt)
            
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game Over!")
                exit()
                    
        for entity in drawable:
            entity.draw(screen)


        dt = clock.tick(60)/1000
        pygame.display.flip()



if __name__ == "__main__":
    main()
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")