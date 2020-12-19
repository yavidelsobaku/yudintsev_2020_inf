#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
from pygame.draw import *
from random import randint
import sys
import time
pygame.font.init()
pygame.init()
clock = pygame.time.Clock()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

FPS = 2
pygame.init()
sc = pygame.display.set_mode((1200, 850))
bg1 = pygame.image.load('bg1.jpg')
t1 = pygame.font.Font(None, 70)
text1 = t1.render("Начать игру", True, (BLACK))
t1_rect = text1.get_rect(bottomright=(740, 465))
sc.blit(bg1, (0, 0))
sc.blit(text1, t1_rect)
pygame.display.update()

start = False
while start == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] >= 550 and event.pos[0] <= 750 and event.pos[1] >= 375 and event.pos[1] <= 475:
                    start = True
pygame.display.quit                    
def bg():
    bg2 = pygame.image.load('bg2.jpg')
    sc.blit(bg2, (0, 0))
    pygame.draw.rect(sc, (BLACK), (0, 0, 1200, 5))
    pygame.draw.rect(sc, (BLACK), (0, 150, 1200, 5))
    pygame.draw.rect(sc, (BLACK), (0, 300, 1200, 5))
    pygame.draw.rect(sc, (BLACK), (0, 450, 1200, 5))
    pygame.draw.rect(sc, (BLACK), (0, 600, 1200, 5))
    pygame.draw.rect(sc, (BLACK), (0, 0, 5, 600))
    pygame.draw.rect(sc, (BLACK), (100, 0, 5, 600))
    pygame.draw.rect(sc, (BLACK), (300, 0, 5, 600))
    pygame.draw.rect(sc, (BLACK), (500, 0, 5, 600))
    pygame.draw.rect(sc, (BLACK), (850, 0, 5, 600))
    pygame.draw.rect(sc, (BLACK), (1195, 0, 5, 600))
    n1 = pygame.font.Font(None, 100)
    num1 = n1.render("1", True, (BLACK))
    n1_rect = num1.get_rect(topleft=(35, 200))
    sc.blit(num1, n1_rect)
    n2 = pygame.font.Font(None, 100)
    num2 = n2.render("2", True, (BLACK))
    n2_rect = num2.get_rect(topleft=(35, 350))
    sc.blit(num2, n2_rect)
    n3 = pygame.font.Font(None, 100)
    num3 = n3.render("3", True, (BLACK))
    n3_rect = num3.get_rect(topleft=(35, 500))
    sc.blit(num3, n3_rect)
    h1 = pygame.font.Font(None, 70)
    head1 = h1.render("СХЕМА", True, (BLACK))
    h1_rect = head1.get_rect(topleft=(115, 50))
    sc.blit(head1, h1_rect)
    h2 = pygame.font.Font(None, 70)
    head2 = h2.render("ЭТАП", True, (BLACK))
    h2_rect = head2.get_rect(topleft=(335, 50))
    sc.blit(head2, h2_rect)
    h3 = pygame.font.Font(None, 70)
    head3 = h3.render("ПРОЦЕССЫ", True, (BLACK))
    h3_rect = head3.get_rect(topleft=(535, 50))
    sc.blit(head3, h3_rect)
    h4 = pygame.font.Font(None, 70)
    head4 = h4.render("ФУНКЦИИ", True, (BLACK))
    h4_rect = head4.get_rect(topleft=(895, 50))
    sc.blit(head4, h4_rect)
    ch = pygame.font.Font(None, 80)
    check = ch.render("ПРОВЕРКА", True, (BLACK))
    ch_rect = check.get_rect(topleft=(870, 790))
    sc.blit(check, ch_rect)


#1.1
drag11 = 0    
x11 = 0
y11 = 655
img11 = pygame.image.load('11.png')
imgWidth11 = 100
imgHeight11 = 100

def image11(imgX11,imgY11):
    sc.blit(img11, (imgX11, imgY11))
    
def movableImg11():
    global drag11, x11, y11
    mouse11 = pygame.mouse.get_pos()
    click11 = pygame.mouse.get_pressed()
    image11(x11, y11)
    if click11[0] == 1 and x11 + imgWidth11 + 70 > mouse11[0] > x11 + 70 and y11 + imgHeight11 + 70 > mouse11[1] > y11 + 70 and drag21!=1 and drag31!=1 and drag12!=1 and drag22!=1 and drag32!=1 and drag13!=1 and drag23!=1 and drag33!=1 and drag14!=1 and drag24!=1 and drag34!=1:
        drag11 = 1 
    if click11[0] == 0:
        drag11 = 0
    if drag11 == 1:
        x11 = mouse11[0] - (2*imgWidth11 / 2)
        y11 = mouse11[1] - (2*imgHeight11 / 2)

def main_loop11():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    movableImg11()


#2.1
drag21 = 0    
x21 = 465
y21 = 705
img21 = pygame.image.load('21.png')
imgWidth21 = 100
imgHeight21 = 100

def image21(imgX21,imgY21):
    sc.blit(img21, (imgX21, imgY21))
    
def movableImg21():
    global drag21, x21, y21
    mouse21 = pygame.mouse.get_pos()
    click21 = pygame.mouse.get_pressed()
    image21(x21, y21)
    if click21[0] == 1 and x21 + imgWidth21 + 70 > mouse21[0] > x21 + 70 and y21 + imgHeight21 + 70 > mouse21[1] > y21 + 70 and drag11!=1 and drag31!=1 and drag12!=1 and drag22!=1 and drag32!=1 and drag13!=1 and drag23!=1 and drag33!=1 and drag14!=1 and drag24!=1 and drag34!=1:
        drag21 = 1 
    if click21[0] == 0:
        drag21 = 0
    if drag21 == 1:
        x21 = mouse21[0] - (2*imgWidth21 / 2)
        y21 = mouse21[1] - (2*imgHeight21 / 2)

def main_loop21():    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    movableImg21()


#3.1
drag31 = 0    
x31 = 980
y31 = 655
img31 = pygame.image.load('31.png')
imgWidth31 = 100
imgHeight31 = 100

def image31(imgX31,imgY31):
    sc.blit(img31, (imgX31, imgY31))
    
def movableImg31():
    global drag31, x31, y31
    mouse31 = pygame.mouse.get_pos()
    click31 = pygame.mouse.get_pressed()
    image31(x31, y31)
    if click31[0] == 1 and x31 + imgWidth31 + 70 > mouse31[0] > x31 + 70 and y31 + imgHeight31 + 70 > mouse31[1] > y31 + 70 and drag21!=1 and drag11!=1 and drag12!=1 and drag22!=1 and drag32!=1 and drag13!=1 and drag23!=1 and drag33!=1 and drag14!=1 and drag24!=1 and drag34!=1:
        drag31 = 1 
    if click31[0] == 0:
        drag31 = 0
    if drag31 == 1:
        x31 = mouse31[0] - (2*imgWidth31 / 2)
        y31 = mouse31[1] - (2*imgHeight31 / 2)

def main_loop31():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    movableImg31()


#1.2
drag12 = 0    
x12 = 290
y12 = 620
img12 = pygame.image.load('12.jpg')
imgWidth12 = 100
imgHeight12 = 100

def image12(imgX12,imgY12):
    sc.blit(img12, (imgX12, imgY12))
    
def movableImg12():
    global drag12, x12, y12
    mouse12 = pygame.mouse.get_pos()
    click12 = pygame.mouse.get_pressed()
    image12(x12, y12)
    if click12[0] == 1 and x12 + imgWidth12 -30 > mouse12[0] > x12 -30 and y12 + imgHeight12 -30 > mouse12[1] > y12 -30 and drag21!=1 and drag31!=1 and drag11!=1 and drag22!=1 and drag32!=1 and drag13!=1 and drag23!=1 and drag33!=1 and drag14!=1 and drag24!=1 and drag34!=1:
        drag12 = 1 
    if click12[0] == 0:
        drag12 = 0
    if drag12 == 1:
        x12 = mouse12[0] - (2*imgWidth12 / 2)
        y12 = mouse12[1] - (1*imgHeight12 / 2)

def main_loop12():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    movableImg12()

    
#2.2
drag22 = 0    
x22 = 925
y22 = 605
img22 = pygame.image.load('22.jpg')
imgWidth22 = 100
imgHeight22 = 100

def image22(imgX22,imgY22):
    sc.blit(img22, (imgX22, imgY22))
    
def movableImg22():
    global drag22, x22, y22
    mouse22 = pygame.mouse.get_pos()
    click22 = pygame.mouse.get_pressed()
    image22(x22, y22)
    if click22[0] == 1 and x22 + imgWidth22 -30 > mouse22[0] > x22 -30 and y22 + imgHeight22 -30 > mouse22[1] > y22 -30 and drag21!=1 and drag31!=1 and drag11!=1 and drag12!=1 and drag32!=1 and drag13!=1 and drag23!=1 and drag33!=1 and drag14!=1 and drag24!=1 and drag34!=1:
        drag22 = 1 
    if click22[0] == 0:
        drag22 = 0
    if drag22 == 1:
        x22 = mouse22[0] - (2*imgWidth22 / 2)
        y22 = mouse22[1] - (1*imgHeight22 / 2)

def main_loop22():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    movableImg22()


#3.2
drag32 = 0    
x32 = 750
y32 = 610
img32 = pygame.image.load('32.jpg')
imgWidth32 = 100
imgHeight32 = 100

def image32(imgX32,imgY32):
    sc.blit(img32, (imgX32, imgY32))
    
def movableImg32():
    global drag32, x32, y32
    mouse32 = pygame.mouse.get_pos()
    click32 = pygame.mouse.get_pressed()
    image32(x32, y32)
    if click32[0] == 1 and x32 + imgWidth32 -30 > mouse32[0] > x32 -30 and y32 + imgHeight32 -30 > mouse32[1] > y32 -30 and drag21!=1 and drag31!=1 and drag11!=1 and drag12!=1 and drag22!=1 and drag13!=1 and drag23!=1 and drag33!=1 and drag14!=1 and drag24!=1 and drag34!=1:
        drag32 = 1 
    if click32[0] == 0:
        drag32 = 0
    if drag32 == 1:
        x32 = mouse32[0] - (2*imgWidth32 / 2)
        y32 = mouse32[1] - (1*imgHeight32 / 2)

def main_loop32():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    movableImg32()

    
#1.3
drag13 = 0    
x13 = 440
y13 = 610
img13 = pygame.image.load('13.png')
imgWidth13 = 100
imgHeight13 = 100

def image13(imgX13,imgY13):
    sc.blit(img13, (imgX13, imgY13))
    
def movableImg13():
    global drag13, x13, y13
    mouse13 = pygame.mouse.get_pos()
    click13 = pygame.mouse.get_pressed()
    image13(x13, y13)
    if click13[0] == 1 and x13 + imgWidth13 -30 > mouse13[0] > x13 -30 and y13 + imgHeight13 -30 > mouse13[1] > y13 -30 and drag21!=1 and drag31!=1 and drag11!=1 and drag12!=1 and drag22!=1 and drag32!=1 and drag23!=1 and drag33!=1 and drag14!=1 and drag24!=1 and drag34!=1:
        drag13 = 1 
    if click13[0] == 0:
        drag13 = 0
    if drag13 == 1:
        x13 = mouse13[0] - (2*imgWidth13 / 2)
        y13 = mouse13[1] - (1*imgHeight13 / 2)

def main_loop13():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    movableImg13()

      
#2.3
drag23 = 0    
x23 = 135
y23 = 770
img23 = pygame.image.load('23.png')
imgWidth23 = 100
imgHeight23 = 100

def image23(imgX23,imgY23):
    sc.blit(img23, (imgX23, imgY23))
    
def movableImg23():
    global drag23, x23, y23
    mouse23 = pygame.mouse.get_pos()
    click23 = pygame.mouse.get_pressed()
    image23(x23, y23)
    if click23[0] == 1 and x23 + imgWidth23 -30 > mouse23[0] > x23 -30 and y23 + imgHeight23 -30 > mouse23[1] > y23 -30 and drag21!=1 and drag31!=1 and drag11!=1 and drag12!=1 and drag22!=1 and drag32!=1 and drag13!=1 and drag33!=1 and drag14!=1 and drag24!=1 and drag34!=1:
        drag23 = 1 
    if click23[0] == 0:
        drag23 = 0
    if drag23 == 1:
        x23 = mouse23[0] - (2*imgWidth23 / 2)
        y23 = mouse23[1] - (1*imgHeight23 / 2)

def main_loop23():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    movableImg23()

 
#3.3
drag33 = 0    
x33 = 590
y33 = 760
img33 = pygame.image.load('33.png')
imgWidth33 = 100
imgHeight33 = 100

def image33(imgX33,imgY33):
    sc.blit(img33, (imgX33, imgY33))
    
def movableImg33():
    global drag33, x33, y33
    mouse33 = pygame.mouse.get_pos()
    click33 = pygame.mouse.get_pressed()
    image33(x33, y33)
    if click33[0] == 1 and x33 + imgWidth33 -30 > mouse33[0] > x33 -30 and y33 + imgHeight33 -30 > mouse33[1] > y33 -30 and drag21!=1 and drag31!=1 and drag11!=1 and drag12!=1 and drag22!=1 and drag32!=1 and drag13!=1 and drag23!=1 and drag14!=1 and drag24!=1 and drag34!=1:
        drag33 = 1 
    if click33[0] == 0:
        drag33 = 0
    if drag33 == 1:
        x33 = mouse33[0] - (2*imgWidth33 / 2)
        y33 = mouse33[1] - (1*imgHeight33 / 2)

def main_loop33():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    movableImg33()


#1.4
drag14 = 0    
x14 = 655
y14 = 655
img14 = pygame.image.load('14.png')
imgWidth14 = 100
imgHeight14 = 100

def image14(imgX14,imgY14):
    sc.blit(img14, (imgX14, imgY14))
    
def movableImg14():
    global drag14, x14, y14
    mouse14 = pygame.mouse.get_pos()
    click14 = pygame.mouse.get_pressed()
    image14(x14, y14)
    if click14[0] == 1 and x14 + imgWidth14 -30 > mouse14[0] > x14 -30 and y14 + imgHeight14 -30 > mouse14[1] > y14 -30 and drag21!=1 and drag31!=1 and drag11!=1 and drag12!=1 and drag22!=1 and drag32!=1 and drag13!=1 and drag23!=1 and drag33!=1 and drag24!=1 and drag34!=1:
        drag14 = 1 
    if click14[0] == 0:
        drag14 = 0
    if drag14 == 1:
        x14 = mouse14[0] - (2*imgWidth14 / 2)
        y14 = mouse14[1] - (1*imgHeight14 / 2)

def main_loop14():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    movableImg14()

     
#2.4
drag24 = 0    
x24 = 160
y24 = 665
img24 = pygame.image.load('24.png')
imgWidth24 = 100
imgHeight24 = 100

def image24(imgX24,imgY24):
    sc.blit(img24, (imgX24, imgY24))
    
def movableImg24():
    global drag24, x24, y24
    mouse24 = pygame.mouse.get_pos()
    click24 = pygame.mouse.get_pressed()
    image24(x24, y24)
    if click24[0] == 1 and x24 + imgWidth24 -30 > mouse24[0] > x24 -30 and y24 + imgHeight24 -30 > mouse24[1] > y24 -30 and drag21!=1 and drag31!=1 and drag11!=1 and drag12!=1 and drag22!=1 and drag32!=1 and drag13!=1 and drag23!=1 and drag33!=1 and drag14!=1 and drag34!=1:
        drag24 = 1 
    if click24[0] == 0:
        drag24 = 0
    if drag24 == 1:
        x24 = mouse24[0] - (2*imgWidth24 / 2)
        y24 = mouse24[1] - (1*imgHeight24 / 2)

def main_loop24():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    movableImg24()

    
#3.4
drag34 = 0    
x34 = 0
y34 = 605
img34 = pygame.image.load('34.png')
imgWidth34 = 100
imgHeight34 = 100

def image34(imgX34,imgY34):
    sc.blit(img34, (imgX34, imgY34))
    
def movableImg34():
    global drag34, x34, y34
    mouse34 = pygame.mouse.get_pos()
    click34 = pygame.mouse.get_pressed()
    image34(x34, y34)
    if click34[0] == 1 and x34 + imgWidth34 -30 > mouse34[0] > x34 -30 and y34 + imgHeight34 -30 > mouse34[1] > y34 -30 and drag21!=1 and drag31!=1 and drag11!=1 and drag12!=1 and drag22!=1 and drag32!=1 and drag13!=1 and drag23!=1 and drag33!=1 and drag14!=1 and drag24!=1:
        drag34 = 1 
    if click34[0] == 0:
        drag34 = 0
    if drag34 == 1:
        x34 = mouse34[0] - (2*imgWidth34 / 2)
        y34 = mouse34[1] - (1*imgHeight34 / 2)

def main_loop34():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    movableImg34()


def main_loop():
    checkvar = False
    
    while checkvar == False:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        bg()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if event.pos[0] >= 870 and event.pos[0] <= 1200 and event.pos[1] >= 790 and event.pos[1] <= 850:
                        checkvar = True      
        main_loop21()
        main_loop11()
        main_loop31()
        main_loop12()
        main_loop22()
        main_loop32()
        main_loop13()
        main_loop23()
        main_loop33()
        main_loop14()
        main_loop24()
        main_loop34()
        pygame.display.update()
        clock.tick(30)

def checkbg():
    score = 0
    if 100<x11 + imgWidth11<300 and 150<y11 + imgHeight11<300:
        score += 1
    if 300<x12 + imgWidth12<500 and 150<y12 + imgHeight12-50<300:
        score += 1
    if 500<x13 + imgWidth13<850 and 150<y13 + imgHeight13-50<300:
        score += 1
    if 850<x14 + imgWidth14<1200 and 150<y14 + imgHeight14-50<300:
        score += 1
    if 100<x21 + imgWidth21<300 and 300<y21 + imgHeight21-50<450:
        score += 1
    if 300<x22 + imgWidth22<500 and 300<y22 + imgHeight22-50<450:
        score += 1
    if 500<x23 + imgWidth23<850 and 300<y23 + imgHeight23-50<450:
        score += 1
    if 850<x24 + imgWidth24<1200 and 300<y24 + imgHeight24-50<450:
        score += 1
    if 100<x31 + imgWidth31<300 and 450<y31 + imgHeight31<600:
        score += 1
    if 300<x32 + imgWidth32<500 and 450<y32 + imgHeight32-50<600:
        score += 1
    if 500<x33 + imgWidth33<850 and 450<y33 + imgHeight33-50<600:
        score += 1
    if 850<x34 + imgWidth34<1200 and 450<y34 + imgHeight34-50<600:
        score += 1
    bg3 = pygame.image.load('bg3.jpg')
    sc.blit(bg3, (0, 0))
    if score < 12:
        scnw = pygame.font.Font(None, 60)
        scorenumw = scnw.render("Правильно сопоставлено " + str(score) + " из 12, попробуйте ещё раз", True, (BLACK))
        scnw_rect = scorenumw.get_rect(topleft=(50, 450))
        sc.blit(scorenumw, scnw_rect)
        pygame.display.update()
    elif score == 12:
        scn = pygame.font.Font(None, 60)
        scorenum = scn.render("Всё правильно, молодец!", True, (BLACK))
        scn_rect = scorenum.get_rect(topleft=(300, 450))
        sc.blit(scorenum, scn_rect)
        pygame.display.update()
main_loop()
checkbg()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
pygame.quit()


# In[ ]:




