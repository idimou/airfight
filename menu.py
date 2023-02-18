import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MenuLoopRunning = True

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class MenuButton(pygame.sprite.Sprite):
    def __init__(self): 
        super(MenuButton).__init__()
        self.surf = pygame.Surface((100,100))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect()

pygame.init()
menuButton = MenuButton()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255,255,255))

screen.blit(menuButton.surf, menuButton.rect)



while MenuLoopRunning:
    pygame.display.flip() 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MenuLoopRunning = False

# end of the game loop __________________________________
pygame.quit()