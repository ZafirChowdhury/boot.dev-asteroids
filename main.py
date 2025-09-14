import pygame

from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    # clock
    dt = 0
    clock = pygame.time.Clock()

    # screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    # player
    X = SCREEN_WIDTH / 2
    Y = SCREEN_HEIGHT / 2
    player = Player(X, Y)

    # asteroid fields
    asteroidField = AsteroidField()

    # game loop
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    

        screen.fill("black")

        # update
        for entity in updatable:
            entity.update(dt)

        # draw
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
