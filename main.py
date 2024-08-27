# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
pygame.init

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


clock = pygame.time.Clock()
player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)


def main():
    dt = 0
    print("Starting asteroids!")


    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        player.update(dt)
        screen.fill(000)
        player.draw(screen)
        dt = clock.tick(60)/1000
        pygame.display.flip()



if __name__ == "__main__":
    main()
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")