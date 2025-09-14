import pygame

from constants import * 
from player import Player

def main():
    pygame.init()

    # clock
    dt = 0
    clock = pygame.time.Clock()

    # screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # player
    X = SCREEN_WIDTH / 2
    Y = SCREEN_HEIGHT / 2
    player = Player(X, Y)

    # game loop
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    

        screen.fill("black")

        player.update(dt)
        player.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
