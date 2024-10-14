# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

import pygame, sys
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,500))

rect = pygame.Rect(225,225,50,50)
rect_speed = [0,0]

surf = pygame.Surface((rect.w,rect.h))
surf.fill(color=(0,0,255))


run = True
while run:

    for events in pygame.event.get():
        pass
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        if rect.top > 0: # prevent rect from moving off the top
            rect.y -= 5 # move up 5 if key 'w' is pressed
    if keys[K_s]:
        if rect.bottom < 500: # prevent rect from moving off the bottom
            rect.y += 5 # move down 5 if key 's' is pressed
    if keys[K_d]:
        if rect.right < 500: # prevent rect from moving off the right side
            rect.x += 5 # move right 5 if key 'd' is pressed
    if keys[K_a]:
        if rect.left > 0: # prevent rect from moving off the left side
            rect.x -= 5 # move left 5 if key 'a' is pressed
    if keys[K_r]:
        rect.x = 225
        rect.y = 225

    rect = rect.move(rect_speed)

    if (rect.x<0 or rect.x>450):
        rect_speed[0] = -rect_speed[0]
    rect = rect.move(rect_speed)

    screen.fill(color=(0, 0, 0))

    screen.blit(surf, (rect.x, rect.y))

    clock.tick(60)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
