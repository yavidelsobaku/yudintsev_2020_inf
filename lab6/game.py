import pygame
from pygame.draw import *
from random import randint
import time
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 500)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    pygame.display.update()

def new_ball1():
    '''рисует новый шарик отличный от предыдущего'''
    global a, b, c
    a = randint(100, 1100)
    b = randint(100, 500)
    c = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (a, b), c)
    pygame.display.update()

pygame.display.update()
clock = pygame.time.Clock()
finished = False
k1 = 0
k2 = 0
d1 = 0
d2 = 0
n = 0
while not finished:
    strike = False
    clock.tick(FPS)
    k = 0
    new_ball()
    new_ball1()
    screen.fill(BLACK)

    if strike == False:
        while k <= 10 and strike == False:
            color = COLORS[randint(0, 5)]
            circle(screen, color, (x, y), r)
            circle(screen, color, (a, b), c)
            pygame.display.update()
            screen.fill(BLACK)
            time.sleep(0.3)
            #movement of the first ball
            if (k1 == 0) and (k2 == 0):
                if x < 1150:
                    x += randint(0, 20)
                if x >= 1150:
                    k1 = 1
                if y < 550:
                    y += randint(0, 20)
                if y >= 550:
                    k2 = 1
            if (k1 == 0) and (k2 == 1):
                if x < 1150:
                    x += randint(0, 20)
                if x >= 1150:
                    k1 = 1
                if y > 30:
                    y -= randint(0, 20)
                if y <= 100:
                    k2 = 0
            if (k1 == 1) and (k2 == 0):
                if x > 30:
                    x -= randint(0, 20)
                if x <= 100:
                    k1 = 0
                if y < 550:
                    y += randint(0, 20)
                if y >= 550:
                    k2 = 1
            if (k1 == 1) and (k2 == 1):
                if x > 30:
                    x -= randint(0, 20)
                if x <= 100:
                    k1 = 0
                if y > 30:
                    y -= randint(0, 20)
                if y <= 100:
                    k2 = 0
            #size of the first ball
            if r < 11:
                r += randint(0, 20)
            if r > 80:
                r -= randint(0, 15)
            #movement of the second ball
            if (d1 == 1) and (d2 == 1):
                if a < 1150:
                    a += randint(0, 20)
                if a >= 1150:
                    d1 = 0
                if b < 550:
                    b += randint(0, 20)
                if b >= 550:
                    d2 = 0
            if (d1 == 1) and (d2 == 0):
                if a < 1150:
                    a += randint(0, 20)
                if a >= 1150:
                    d1 = 0
                if b > 30:
                    b -= randint(0, 20)
                if b <= 100:
                    d2 = 1
            if (d1 == 0) and (d2 == 1):
                if a > 30:
                    a -= randint(0, 20)
                if a <= 100:
                    d1 = 1
                if b < 550:
                    b += randint(0, 20)
                if b >= 550:
                    d2 = 0
            if (d1 == 0) and (d2 == 0):
                if a > 30:
                    a -= randint(0, 20)
                if b <= 100:
                    d1 = 1
                if b > 30:
                    b -= randint(0, 20)
                if b <= 100:
                    d2 = 1
            #size of the second ball
            if c < 11:
                c += randint(0, 20)
            if c > 80:
                c -= randint(0, 15)
            #about clicking these balls
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(n)
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if (abs(event.pos[0] - x))^2 + (abs(event.pos[1] - y))^2 <= r:
                            n += 1
                            strike = True
                        if (abs(event.pos[0] - a))^2 + (abs(event.pos[1] - b))^2 <= c:
                            n += 1
                            strike = True
    else: break
#leaving the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
