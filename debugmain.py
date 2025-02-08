from constants import *
from player import *
import pygame

def main():
    print("Starting game initialization...")
    
    pygame.init()
    print("Pygame initialized")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Screen created")
    
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    print("Player created")
    
    running = True
    while running:
        print("Game loop running")  # This will help us see if the loop runs at all
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    print("Game ended")

if __name__ == "__main__":
    main()
