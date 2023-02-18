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
        self.surf = pygame.image.load("Sprites/Plane/pavlos.jpg").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -15)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,15)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-15, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10, 0)

      #  Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("Sprites/Bullet/missile-40x10.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf = pygame.Surface((30, 10))
        # self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

def resetPositions():
    enemies.clear(screen, screen)
    for enemy in enemies:
        enemy.kill()
    # enemies.draw(screen)


# initialization code ______________________________________________
pygame.mixer.init()
pygame.init()

pygame.mixer.music.load("Sounds/Apoxode_-_Electric_1.mp3")
pygame.mixer.music.play(loops=-1)

# Load all sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound("Sounds/Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("Sounds/Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("Sounds/Collision.ogg")

clock = pygame.time.Clock()
# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)

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
TimesShot = 0
Lives = 3

# start of the game loop ___________________________________________
while running:
    pygame.display.set_caption(str(TimesShot))
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
    # surf = pygame.Surface((100, 50))
    # Give the surface a color to separate it from the background
    # surf.fill((0, 0, 0))
    # screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    
    # screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    # Draw the player on the screen
    # screen.blit(player.surf, player.rect)

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

     # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
    # If so, then remove the player and stop the loop
        
        TimesShot = TimesShot + 1
        resetPositions()

        if TimesShot == Lives:
            move_up_sound.stop()
            move_down_sound.stop()
            collision_sound.play()
            player.kill()
            running = False   

    # Flip everything to the display
    pygame.display.flip() 
    clock.tick(30)

# end of the game loop

pygame.quit()
