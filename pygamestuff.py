import pygame
import sys
pygame.init()
size = width, height = 960, 540
screen = pygame.display.set_mode(size)
speed = [2, 2]
black = [100, 100, 0]
ball = pygame.image.load("icon.png")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()