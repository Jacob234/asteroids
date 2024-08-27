# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
pygame.init

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



def main():
    print("Starting asteroids!")

    while(True):
        screen.fill(000)
        pygame.display.flip()


if __name__ == "__main__":
    main()
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")