# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
from player import *
from asteroidfield import *
import pygame
import sys

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        black = (0,0,0)
        screen.fill(black)
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        asteroidfield.update(dt)
        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collisions(shot):
                    asteroid.split(asteroids)
                    asteroid.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000
	
    
    
if __name__ == "__main__":
    main()



