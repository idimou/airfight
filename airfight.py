import pygame
import random

# variable and class definitions ___________________________________
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

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("Sprites/Plane/tomcat_black_small.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

      #  Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH/2
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("Sprites/Bullet/missile-150x51.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf = pygame.Surface((20, 10))
        # self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(1, 5)/5

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# initialization code ______________________________________________
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variable to keep our main loop running
running = True

# start of the game loop ___________________________________________
while running:
    
    # Check if the user clicked the window close button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Update enemy position
    enemies.update()

    # Fill the background with white        
    screen.fill((100,200,255))

    # Create a surface and pass in a tuple containing its length and width
    surf = pygame.Surface((100, 50))
    # Give the surface a color to separate it from the background
    surf.fill((0, 0, 0))
    # screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    
    # screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

     # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
    # If so, then remove the player and stop the loop
        player.kill()
        running = False   

    # Flip everything to the display
    pygame.display.flip() 


# end of the game loop

pygame.quit()
