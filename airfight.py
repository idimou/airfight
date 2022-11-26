import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,0,255),(250,250),75)
    pygame.draw.rect(screen, (0,0,0), (30,30,60,60),10 )

    pygame.display.flip()

pygame.quit()