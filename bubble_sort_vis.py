import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 605))
pygame.display.set_caption('Bubble Sort Visualizer')

black = (40, 40, 40)
red = (255, 0, 0)
green = (0, 255, 0)
purple = (128, 0, 128)
font = pygame.font.Font("OdibeeSans-Regular.ttf", 25)
txt = font.render("Visualize", True, (0, 0, 0))

a = list(range(1, 20))
random.shuffle(a)
compl = []


def bubble(arr):
    global compl
    n = len(arr)
    i = n-1
    while i > 0:
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                sys.exit()
        if arr[i] < arr[i-1]:
            display(arr, (i, i-1), compl)
            pygame.display.update()
            pygame.time.wait(250)
            arr[i], arr[i-1] = arr[i-1], arr[i]
            display(arr, completed=compl)
            pygame.display.update()
            pygame.time.wait(250)

        if sorted(arr) == arr:
            compl = list(range(len(arr)))
            display(arr, completed=compl)
            pygame.display.update()
            pygame.time.wait(250)
            break

        i -= 1


def bubble_sort(arr):
    global compl
    compl = []
    n = len(arr)
    i = 0
    while i < n-1:
        if sorted(arr) == arr:
            break
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                sys.exit()
        bubble(arr)
        compl.append(i)
        display(arr, completed=compl)
        pygame.display.update()
        pygame.time.wait(250)
        i += 1
    compl.append(n-1)
    return arr


def display(arr, r=(), completed=(), g=()):
    screen.fill((211, 211, 211))
    for i in range(19):
        if i in completed:
            color = purple
        elif i in r:
            color = red
        elif i in g:
            color = green
        else:
            color = black
        pygame.draw.rect(screen, color, pygame.Rect(20 + 40*i, 580-arr[i]*25, 30, arr[i]*25))


vis = False
while True:
    screen.fill((211, 211, 211))
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 320 <= mouse[0] <= 470 and 10 <= mouse[1] <= 60:
                vis = True

    display(a, completed=compl)

    if 320 <= mouse[0] <= 470 and 10 <= mouse[1] <= 60:
        pygame.draw.rect(screen, (174, 225, 70), pygame.Rect(320, 10, 150, 50), border_radius=5)
    else:
        pygame.draw.rect(screen, (149, 200, 45), pygame.Rect(320, 10, 150, 50), border_radius=5)

    if vis:
        a = list(range(1, 20))
        random.shuffle(a)

        display(a)

        pygame.time.wait(200)

        bubble_sort(a)
        vis = False

    screen.blit(txt, (360, 20))
    pygame.display.update()
