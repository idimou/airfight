import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Variable to keep our main loop running
running = True

# start of the game loop
while running:
    
    # Check if the user clicked the window close button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white        
    screen.fill((255,255,255))

    # Create a surface and pass in a tuple containing its length and width
    surf = pygame.Surface((100, 50))
    # Give the surface a color to separate it from the background
    surf.fill((0, 0, 0))
    screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    
    # Flip everything to the display
    pygame.display.flip() 

# end of the game loop

pygame.quit()
