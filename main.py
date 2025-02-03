# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroidfield import *
from shot import Shot



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots= pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Player.containers = (updateable, drawable)
    Shot.containers = (shots, updateable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updateable:
            thing.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over")
                sys.exit(0)
        
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.kill()

        screen.fill("black")

        for thing in drawable:
           thing.draw(screen)

        pygame.display.flip()
        

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
