# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
pygame.init

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


clock = pygame.time.Clock()
dt = 0


def main():
    print("Starting asteroids!")

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill(000)
        pygame.display.flip()
        dt = clock.tick(60)



if __name__ == "__main__":
    main()
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")