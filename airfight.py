import pygame

# variable and class definitions ___________________________________
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

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect()

# initialization code ______________________________________________
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Variable to keep our main loop running
running = True

# start of the game loop ___________________________________________
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
    # screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    
    # screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    # Draw the player on the screen
    screen.blit(player.surf, player.rect)



    # Flip everything to the display
    pygame.display.flip() 

# end of the game loop

pygame.quit()
