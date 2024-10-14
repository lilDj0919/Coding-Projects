# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400,400))

rect = pygame.Rect(175,0,50,400)
rect1 =pygame.Rect(175,175, 50,50)

rect_speed = [5,0]

surf = pygame.Surface((rect.w,rect.h))
surf.fill(color=(255,0,0))

surf1 = pygame.Surface((rect1.w,rect1.h))
surf1.fill(color=(0,0,255))




run = True
while run:

    if (rect.colliderect(rect1)):
        surf.fill(color=(0,255,0))

    else:
        surf.fill(color=(255,0,0))

    if (rect1.x<0 or rect1.x>350):
        rect_speed[0] = -rect_speed[0]
    rect1 = rect1.move(rect_speed)

    screen.fill(color=(0, 0, 0))

    screen.blit(surf, (rect.x, rect.y))
    screen.blit(surf1, (rect1.x, rect1.y))
    clock.tick(60)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


