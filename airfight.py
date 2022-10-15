import pygame
pygame.init()

height=950
width=1800


screen = pygame.display.set_mode([width,height])
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255,0,0),(width/2,height/2),75)

    pygame.display.flip()

pygame.quit()
