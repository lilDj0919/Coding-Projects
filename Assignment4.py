# Class: 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanan
# Name: D'Aveon Jackson

import pygame, sys
from pygame.locals import K_RIGHT
from pygame.locals import K_LEFT
import random
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

#rect = pygame.Rect(0,0,800,600)
basket = pygame.Rect(350,580,100,20)
basket_speed = [0,0]
fruit = pygame.Rect(400,0,20,20)
fruit_speed = [0,3]

score = 0
#s = pygame.Surface((rect.w,rect.h))

surf = pygame.Surface((basket.w,basket.h))
surf.fill(color=(255,255,255))

surf1 = pygame.Surface((fruit.w,fruit.h))
surf1.fill(color=(255,0,0))

#print(rect.center)

run = True
while run:

    for events in pygame.event.get():
        pass
    keys = pygame.key.get_pressed()
    if keys[K_RIGHT]:
        if basket.right < 800: # prevent rect from moving off the right side
            basket.x += 5 # move right 5 if key 'right arrow' is pressed
    if keys[K_LEFT]:
        if basket.left > 0: # prevent rect from moving off the left side
            basket.x -= 5 # move left 5 if key 'a' is pressed

    # creates fruits and controls movements
    if fruit.y > 600:
        fruit.x = random.randint(380,580)
        fruit.y = 0 # telling the code always spawn here
    fruit = fruit.move(fruit_speed)


    if (basket.colliderect(fruit)):
        score += 1
        print(f"Score: {score}")
        fruit.x = random.randint(350,780)
        fruit.y = 0




    screen.fill(color=(0, 0, 0))
    screen.blit(surf, (basket.x, basket.y))
    screen.blit(surf1, (fruit.x,fruit.y))
    clock.tick(60)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False