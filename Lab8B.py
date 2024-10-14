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
rect2 =pygame.Rect(175,350,50,50)
rect3 =pygame.Rect(175,0,50,50)


rect_speed = [5,0]
rect2_speed = [20,0]
rect3_speed = [10,0]

surf = pygame.Surface((rect.w,rect.h))
surf.fill(color=(255,0,0))

surf1 = pygame.Surface((rect1.w,rect1.h))
surf1.fill(color=(0,0,255))

surf2 = pygame.Surface((rect2.w,rect2.h))
surf2.fill(color=(0,0,255))

surf3 = pygame.Surface((rect3.w,rect3.h))
surf3.fill(color=(0,0,225))



run = True
while run:

    rect_list = [rect1,rect2,rect3]

    if (rect.collidelist(rect_list)) == -1:
        surf.fill(color=(255,0,0))

    else:
        surf.fill(color=(0,255,0))

    if (rect1.x<0 or rect1.x>350):
        rect_speed[0] = -rect_speed[0]
    rect1 = rect1.move(rect_speed)

    if (rect2.x<0 or rect2.x>350):
        rect2_speed[0] = -rect2_speed[0]
    rect2 = rect2.move(rect2_speed)

    if (rect3.x<0 or rect3.x>350):
        rect3_speed[0] = -rect3_speed[0]
    rect3 = rect3.move(rect3_speed)

    screen.fill(color=(0, 0, 0))


    screen.blit(surf, (rect.x, rect.y))
    screen.blit(surf1, (rect1.x, rect1.y))
    screen.blit(surf2,(rect2.x,rect2.y))
    screen.blit(surf3, (rect3.x,rect3.y))
    clock.tick(60)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


