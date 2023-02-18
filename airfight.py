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

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GameLoopRunning = True
TimesShot = 0
Lives = 3

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("Sprites/Plane/pavlos.jpg").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
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
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("Sprites/Bullet/missile-40x10.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

def RemoveAllEnemies():
    enemies.clear(screen, screen)
    for enemy in enemies:
        enemy.kill()

# initialization code ______________________________________________
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("Sounds/Apoxode_-_Electric_1.mp3")
pygame.mixer.music.play(loops=-1)
move_up_sound = pygame.mixer.Sound("Sounds/Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("Sounds/Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("Sounds/Collision.ogg")

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)

player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# start of the game loop ___________________________________
while GameLoopRunning:
    pygame.display.set_caption(str(TimesShot))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()    
    screen.fill((100,200,255))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):       
        TimesShot = TimesShot + 1
        RemoveAllEnemies()
        if TimesShot == Lives:
            move_up_sound.stop()
            move_down_sound.stop()
            collision_sound.play()
            player.kill()
            running = False   

    pygame.display.flip() 
    clock.tick(30)

# end of the game loop __________________________________
pygame.quit()