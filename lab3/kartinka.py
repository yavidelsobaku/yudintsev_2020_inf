import pygame
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 30
screen = pygame.display.set_mode((477, 674))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (1, 1, 1)
GREEN = (0, 255, 0)
DBLUE = (0, 0, 153)
YELLOW = (255, 242, 0)

rect(screen, (0, 153, 204), (0, 0, 477, 674))
rect(screen, (255, 165, 20), (0, 0, 477, 337))
rect(screen, (255, 158, 204), (0, 0, 477, 260))
rect(screen, (255, 153, 255), (0, 0, 477, 170))
rect(screen, (171, 140, 255), (0, 0, 477, 100))
rect(screen, (10, 10, 180), (0, 0, 477, 50))

def ptichka(y, a, h1, h2):
    surface1 = pygame.Surface((4*y, y))
    arc(surface1, WHITE, (0, 0, 2*y, y), 0, np.pi)
    arc(surface1, WHITE, (2*y, 0, 2*y, y), 0, np.pi)
    surface2 = pygame.transform.rotate(surface1, a)
    surface2.set_colorkey(BLACK)
    screen.blit(surface2, (h1, h2))

ptichka(25, 345, 350, 200)
ptichka(20, 15, 100, 100)
ptichka(22, 345, 340, 50)
ptichka(18, 320, 50, 50)
ptichka(5, 30, 400, 20)

def ribka(r, q1, q2):
    surface1r = pygame.Surface((36*r, 16*r))
    polygon(surface1r, WHITE, [[20*r, 0], [30*r, 2*r], [26*r, 6*r]])
    polygon(surface1r, WHITE, [[18*r, 8*r], [20*r, 14*r], [14*r, 14*r]])
    polygon(surface1r, WHITE, [[20*r, 8*r], [34*r, 12*r], [28*r, 16*r]])
    ellipse(surface1r, DBLUE, (12*r, 4*r, 24*r, 8*r))
    circle(surface1r, GREEN, (28*r, 8*r), 2*r, r)
    polygon(surface1r, WHITE, [[0, 0], [12*r, 8*r], [4*r, 12*r]])
    surface1r.set_colorkey(BLACK)
    screen.blit(surface1r, (q1, q2))


ribka(4, 320, 600)
ribka(4, 50, 600)
ribka(3, 360, 520)

def albatros(d, i1, i2):
    surface1d = pygame.Surface((120*d, 100*d))
    polygon(surface1d, WHITE, [[1*d, 42*d], [7*d, 44*d], [8*d, 45*d], [11*d, 46*d], [12*d, 47*d], [16*d, 47*d], [17*d, 48*d],
                               [22*d, 48*d], [24*d, 44*d], [12*d, 24*d], [8*d, 26*d], [7*d, 27*d], [7*d, 28*d], [6*d, 29*d],
                               [6*d, 30*d], [5*d, 31*d], [5*d, 32*d], [4*d, 33*d], [4*d, 36*d], [2*d, 37*d], [1*d, 40*d]])
    polygon(surface1d, WHITE, [[34*d, 36*d], [40*d, 34*d], [37*d, 24*d], [35*d, 20*d], [32*d, 19*d], [24*d, 18*d],
                               [16*d, 18*d], [4*d, 14*d], [0, 12*d], [2*d, 18*d], [8*d, 22*d], [11*d, 28*d],
                               [14*d, 31*d], [20*d, 34*d]])
    aalines(surface1d, BLACK, False, [[8*d, 22*d], [11*d, 28*d], [14*d, 31*d], [20*d, 34*d]])
    polygon(surface1d, WHITE, [[40*d, 38*d], [48*d, 34*d], [47*d, 24*d], [46*d, 18*d], [44*d, 12*d], [36*d, 10*d],
                               [30*d, 10*d], [20*d, 9*d], [14*d, 7*d], [8*d, 4*d], [2*d, 1*d], [6*d, 11*d],
                               [12*d, 14*d], [20*d, 15*d], [24*d, 18*d]])
    aalines(surface1d, BLACK, False, [[40*d, 34*d], [37*d, 24*d], [35*d, 20*d], [32*d, 19*d], [24*d, 18*d]])
    ellipse(surface1d, WHITE, (28*d, 10*d, 16*d, 4*d))
    ellipse(surface1d, WHITE, (20*d, 32*d, 46*d, 28*d))
    ellipse(surface1d, WHITE, (60*d, 36*d, 24*d, 12*d))
    ellipse(surface1d, YELLOW, (104*d, 34*d, 12*d, 4*d))
    polygon(surface1d, YELLOW, [[96 * d, 33 * d], [117 * d, 36 * d], [116 * d, 33 * d],
                                [114 * d, 31 * d], [112 * d, 30 * d], [104 * d, 31 * d]])
    polygon(surface1d, YELLOW, [[96 * d, 33 * d], [96 * d, 35 * d], [104 * d, 36 * d], [110*d, 34*d], [104 * d, 31 * d]])
    line(surface1d, DARKGREY, [96*d, 33*d], [117*d, 36*d])
    ellipse(surface1d, WHITE, (78*d, 28*d, 20*d, 12*d))
    ellipse(surface1d, DARKGREY, (90*d, 32*d, 4*d, 2*d))
    surface2d = pygame.Surface((26*d, 18*d))
    ellipse(surface2d, WHITE, (0, 0, 26*d, 12*d))
    ellipse(surface2d, WHITE, (0, 6*d, 26*d, 12*d))
    arc(surface2d, DARKGREY, (0, 6*d, 26*d, 12*d), 1, np.pi)
    surface2d.set_colorkey(BLACK)
    surface2de = pygame.transform.rotate(surface2d,(360 - (90 - 180*np.arctan(5/12)/np.pi)))
    surface1d.blit(surface2de, (40*d, 50*d))
    polygon(surface1d, WHITE, [[52*d, 78*d], [56*d, 76*d], [64*d, 82*d], [68*d, 90*d], [66*d, 92*d], [64*d, 92*d], [56*d, 86*d]])
    polygon(surface1d, WHITE, [[56*d, 74*d], [60*d, 72*d], [68*d, 78*d], [72*d, 86*d], [70*d, 88*d], [68*d, 88*d], [60*d, 78*d]])
    aalines(surface1d, DARKGREY, False, [[56*d, 76*d], [64*d, 82*d], [68*d, 90*d]])
    polygon(surface1d, YELLOW, [[68*d, 90*d], [76*d, 88*d], [78*d, 89*d], [79*d, 90*d], [79*d, 91*d], [78*d, 90*d],
                                [70*d, 90*d], [76*d, 91*d], [78*d, 92*d], [79*d, 93*d], [79*d, 94*d], [78*d, 93*d],
                                [76*d, 92*d], [70*d, 92*d], [74*d, 93*d], [77*d, 96*d], [77*d, 98*d], [76*d, 96*d],
                                [70*d, 93*d], [66*d, 95*d], [66*d, 98*d], [64*d, 96*d], [66*d, 92*d]])
    polygon(surface1d, YELLOW, [[72*d, 86*d], [80*d, 84*d], [82*d, 85*d], [83*d, 86*d], [83*d, 87*d], [82*d, 86*d],
                                [74*d, 86*d], [80*d, 87*d], [82*d, 88*d], [83*d, 89*d], [83*d, 90*d], [82*d, 89*d],
                                [80*d, 88*d], [74*d, 88*d], [78*d, 89*d], [81*d, 92*d], [81*d, 94*d], [80*d, 92*d],
                                [74*d, 89*d], [70*d, 91*d], [70*d, 94*d], [68*d, 92*d], [70*d, 88*d]])
    aalines(surface1d, DARKGREY, False, [[68*d, 90*d], [76*d, 88*d], [78*d, 89*d], [79*d, 90*d], [79*d, 91*d], [78*d, 90*d]])
    surface1d.set_colorkey(BLACK)
    screen.blit(surface1d, (i1, i2))

def albatros_naoborot(d, i1, i2):
    surface1d = pygame.Surface((120*d, 100*d))
    polygon(surface1d, WHITE, [[120*d - 1*d, 42*d], [120*d - 7*d, 44*d], [120*d - 8*d, 45*d], [120*d - 11*d, 46*d],
                               [120*d - 12*d, 47*d], [120*d - 16*d, 47*d], [120*d - 17*d, 48*d], [120*d - 22*d, 48*d],
                               [120*d - 24*d, 44*d], [120*d - 12*d, 24*d], [120*d - 8*d, 26*d], [120*d - 7*d, 27*d],
                               [120*d - 7*d, 28*d], [120*d - 6*d, 29*d], [120*d - 6*d, 30*d], [120*d - 5*d, 31*d],
                               [120*d - 5*d, 32*d], [120*d - 4*d, 33*d], [120*d - 4*d, 36*d], [120*d - 2*d, 37*d],
                               [120*d - 1*d, 40*d]])
    polygon(surface1d, WHITE, [[120*d - 34*d, 36*d], [120*d - 40*d, 34*d], [120*d - 37*d, 24*d], [120*d - 35*d, 20*d],
                               [120*d - 32*d, 19*d], [120*d - 24*d, 18*d], [120*d - 16*d, 18*d], [120*d - 4*d, 14*d],
                               [120*d - 0, 12*d], [120*d - 2*d, 18*d], [120*d - 8*d, 22*d], [120*d - 11*d, 28*d],
                               [120*d - 14*d, 31*d], [120*d - 20*d, 34*d]])
    aalines(surface1d, BLACK, False, [[120*d - 8*d, 22*d], [120*d - 11*d, 28*d], [120*d - 14*d, 31*d], [120*d - 20*d, 34*d]])
    polygon(surface1d, WHITE, [[120*d - 40*d, 38*d], [120*d - 48*d, 34*d], [120*d - 47*d, 24*d], [120*d - 46*d, 18*d],
                               [120*d - 44*d, 12*d], [120*d - 36*d, 10*d], [120*d - 30*d, 10*d], [120*d - 20*d, 9*d],
                               [120*d - 14*d, 7*d], [120*d - 8*d, 4*d], [120*d - 2*d, 1*d], [120*d - 6*d, 11*d],
                               [120*d - 12*d, 14*d], [120*d - 20*d, 15*d], [120*d - 24*d, 18*d]])
    aalines(surface1d, BLACK, False, [[120*d - 40*d, 34*d], [120*d - 37*d, 24*d], [120*d - 35*d, 20*d],
                                      [120*d - 32*d, 19*d], [120*d - 24*d, 18*d]])
    ellipse(surface1d, WHITE, (120*d - 28*d - 16*d, 10*d, 16*d, 4*d))
    ellipse(surface1d, WHITE, (120*d - 20*d - 46*d, 32*d, 46*d, 28*d))
    ellipse(surface1d, WHITE, (120*d - 60*d - 24*d, 36*d, 24*d, 12*d))
    ellipse(surface1d, YELLOW, (120*d - 104*d - 12*d, 34*d, 12*d, 4*d))
    polygon(surface1d, YELLOW, [[120*d - 96 * d, 33 * d], [120*d - 117 * d, 36 * d], [120*d - 116 * d, 33 * d],
                                [120*d - 114 * d, 31 * d], [120*d - 112 * d, 30 * d], [120*d - 104 * d, 31 * d]])
    polygon(surface1d, YELLOW, [[120*d - 96 * d, 33 * d], [120*d - 96 * d, 35 * d], [120*d - 104 * d, 36 * d],
                                [120*d - 110*d, 34*d], [120*d - 104 * d, 31 * d]])
    line(surface1d, DARKGREY, [120*d - 96*d, 33*d], [120*d - 117*d, 36*d])
    ellipse(surface1d, WHITE, (120*d - 78*d - 20*d, 28*d, 20*d, 12*d))
    ellipse(surface1d, DARKGREY, (120*d - 90*d - 4*d, 32*d, 4*d, 2*d))
    surface2d = pygame.Surface((26*d, 18*d))
    ellipse(surface2d, WHITE, (0, 0, 26*d, 12*d))
    ellipse(surface2d, WHITE, (0, 6*d, 26*d, 12*d))
    arc(surface2d, DARKGREY, (0, 6*d, 26*d, 12*d), 1, np.pi)
    surface2d.set_colorkey(BLACK)
    surface2de = pygame.transform.rotate(surface2d,(90 - 180*np.arctan(5/12)/np.pi))
    surface1d.blit(surface2de, (120*d - 40*d - 25*d, 50*d))
    polygon(surface1d, WHITE, [[120*d - 52*d, 78*d], [120*d - 56*d, 76*d], [120*d - 64*d, 82*d], [120*d - 68*d, 90*d],
                               [120*d - 66*d, 92*d], [120*d - 64*d, 92*d], [120*d - 56*d, 86*d]])
    polygon(surface1d, WHITE, [[120*d - 56*d, 74*d], [120*d - 60*d, 72*d], [120*d - 68*d, 78*d], [120*d - 72*d, 86*d],
                               [120*d - 70*d, 88*d], [120*d - 68*d, 88*d], [120*d - 60*d, 78*d]])
    aalines(surface1d, DARKGREY, False, [[120*d - 56*d, 76*d], [120*d - 64*d, 82*d], [120*d - 68*d, 90*d]])
    polygon(surface1d, YELLOW, [[120*d - 68*d, 90*d], [120*d - 76*d, 88*d], [120*d - 78*d, 89*d], [120*d - 79*d, 90*d],
                                [120*d - 79*d, 91*d], [120*d - 78*d, 90*d], [120*d - 70*d, 90*d], [120*d - 76*d, 91*d],
                                [120*d - 78*d, 92*d], [120*d - 79*d, 93*d], [120*d - 79*d, 94*d], [120*d - 78*d, 93*d],
                                [120*d - 76*d, 92*d], [120*d - 70*d, 92*d], [120*d - 74*d, 93*d], [120*d - 77*d, 96*d],
                                [120*d - 77*d, 98*d], [120*d - 76*d, 96*d], [120*d - 70*d, 93*d], [120*d - 66*d, 95*d],
                                [120*d - 66*d, 98*d], [120*d - 64*d, 96*d], [120*d - 66*d, 92*d]])
    polygon(surface1d, YELLOW, [[120*d - 72*d, 86*d], [120*d - 80*d, 84*d], [120*d - 82*d, 85*d], [120*d - 83*d, 86*d],
                                [120*d - 83*d, 87*d], [120*d - 82*d, 86*d], [120*d - 74*d, 86*d], [120*d - 80*d, 87*d],
                                [120*d - 82*d, 88*d], [120*d - 83*d, 89*d], [120*d - 83*d, 90*d], [120*d - 82*d, 89*d],
                                [120*d - 80*d, 88*d], [120*d - 74*d, 88*d], [120*d - 78*d, 89*d], [120*d - 81*d, 92*d],
                                [120*d - 81*d, 94*d], [120*d - 80*d, 92*d], [120*d - 74*d, 89*d], [120*d - 70*d, 91*d],
                                [120*d - 70*d, 94*d], [120*d - 68*d, 92*d], [120*d - 70*d, 88*d]])
    aalines(surface1d, DARKGREY, False, [[120*d - 68*d, 90*d], [120*d - 76*d, 88*d], [120*d - 78*d, 89*d],
                                         [120*d - 79*d, 90*d], [120*d - 79*d, 91*d], [120*d - 78*d, 90*d]])
    surface1d.set_colorkey(BLACK)
    screen.blit(surface1d, (i1, i2))

albatros_naoborot(2, 220, 250)
albatros(3, 20, 290)
albatros(1, 70, 180)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()