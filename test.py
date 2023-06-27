import pygame, sys
from pygame.locals import*

pygame.init()
pygame.display.set_caption("first Proram")
screen = pygame.display.set_mode((640,480))
xpos = 50
ypos = 50
clock = pygame.time.Clock()
while 1:
    clock.tick(60)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pressed_key = pygame.key.get_pressed()
    if pressed_key[K_RIGHT]:
        xpos += 5

    if pressed_key[K_LEFT]:
        xpos -= 5
        
    if pressed_key[K_UP]:
        ypos -= 5
        
    if pressed_key[K_DOWN]:
        ypos += 5
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,255,0), (xpos,ypos), 20)
    pygame.display.update()

