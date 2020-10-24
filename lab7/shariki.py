import pygame
import math
from pygame.draw import *
from random import randint
import time

pygame.init()
name=input()
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

def another_thing():
    '''рисует другую фигуру
    a1,b1:coordinates
       h1:hight'''
    global a1, b1, h1, b11, b21
    a1 = randint(100, 900)
    b1 = randint(100, 400)
    h1 = randint(20, 100)
    color = COLORS[randint(0, 5)]
    b11 = b1 + int(h1*math.tan(math.pi/6))
    b21 = b1 - int(h1*math.tan(math.pi/6))
    while (x-a1)**2+(y-b1)**2<(r+(h1+b1-b21))**2:
        a1 = randint(100, 900)
        b1 = randint(100, 400)
        h1 = randint(20, 200)
        b11 = b1 + int(h1 * math.tan(math.pi / 6))
        b21 = b1 - int(h1 * math.tan(math.pi / 6))
    polygon(screen,color,[(a1,b1),(a1+h1,b11),(a1+h1,b21)])
    pygame.display.update()

pygame.display.update()
clock = pygame.time.Clock()
finished = False
k1 = 0
k2 = 0
d1 = 0
d2 = 0
n = 0


while finished == False:
    strike = False
    clock.tick(FPS)
    k = 0
    new_ball()
    new_ball1()
    another_thing()
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if strike == False:
        #координаты смещения для другой фигуры
        a_change = randint(-15, 15)
        b_change = randint(-15, 15)

        while k <= 10 and strike == False:

            a1+=a_change
            b1+=b_change
            b11 = b1 + int(h1 * math.tan(math.pi/6))
            b21 = b1 - int(h1 * math.tan(math.pi/6))
            color = COLORS[randint(0, 5)]
            polygon(screen, color, [(a1, b1), (a1 + h1, b11), (a1 + h1, b21)])
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

            # movement of the another figure
            if (a1 + h1) >= 1200 or x <= 0:
                a_change = 0 - a_change
            elif b11 >= 600 or b21 <= 0:
                b_change = 0 - b_change

            #about clicking these balls
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(n)
                    finished = True
                    strike = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if (abs(event.pos[0] - x))^2 + (abs(event.pos[1] - y))^2 <= r:
                            n += 1
                            strike = True
                        if (abs(event.pos[0] - a))^2 + (abs(event.pos[1] - b))^2 <= c:
                            n += 1
                            strike = True
                        if (a1 <= event.pos[0] <= a1 + h1) and (b21 <= event.pos[1] <= b11) and ((b1 + (event.pos[0] - a1) * math.tan(math.pi / 6)) >= event.pos[1]
                                                                                                 or (b1 - (event.pos[0] - a1) * math.tan(math.pi / 6)) <= event.pos[1]):
                            n += 2
                            strike = True
    else:
        break
        pygame.quit()

#writing in the file
inp = open('table.txt', 'r')
s = inp.read()
inp.close()
out = open('table.txt', 'w')
out.write(s+'\n'+ name + '=' + str(n))
out.close()
