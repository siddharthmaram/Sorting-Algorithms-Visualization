import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 605))
pygame.display.set_caption('Selection Sort Visualizer')

black = (40, 40, 40)
red = (255, 0, 0)
font = pygame.font.Font("OdibeeSans-Regular.ttf", 25)
txt = font.render("Visualize", True, (0, 0, 0))

a = list(range(1, 20))
random.shuffle(a)


def loc_of_smallest(arr, start, end):
    loc = start
    for i in range(start, end+1):
        if arr[i] < arr[loc]:
            loc = i
    return loc


def selection_sort(arr):
    i = 0
    n = len(arr)
    while i < n-1:
        j = loc_of_smallest(arr, i, n-1)
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                sys.exit()
        if i != j:
            display(arr, (i, j))
            draw_arrow(i+1, j+1)
            pygame.time.wait(500)
            arr[i], arr[j] = arr[j], arr[i]
            display(arr)
            pygame.display.update()
            pygame.time.wait(300)
        i += 1
    return arr


def draw_arrow(i, j):
    i = 40*i - 5
    j = 40*j - 5
    pygame.draw.line(screen, (0, 0, 255), (i, 575), (i, 596), 6)
    pygame.draw.polygon(screen, (0, 0, 255), [(i - 7, 575), (i + 7, 575), (i, 568)])
    pygame.draw.line(screen, (0, 0, 255), (j, 575), (j, 596), 6)
    pygame.draw.polygon(screen, (0, 0, 255), [(j - 7, 575), (j + 7, 575), (j, 568)])
    pygame.draw.line(screen, (0, 0, 255), (i-1, 596), (j+2, 596), 6)
    pygame.display.update()


def display(arr, r=()):
    screen.fill((211, 211, 211))
    for i in range(19):
        if i in r:
            color = red
        else:
            color = black
        pygame.draw.rect(screen, color, pygame.Rect(20 + 40*i, 560-arr[i]*25, 30, arr[i]*25))


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

    display(a)

    if 320 <= mouse[0] <= 470 and 10 <= mouse[1] <= 60:
        pygame.draw.rect(screen, (174, 225, 70), pygame.Rect(320, 10, 150, 50), border_radius=5)
    else:
        pygame.draw.rect(screen, (149, 200, 45), pygame.Rect(320, 10, 150, 50), border_radius=5)

    if vis:
        a = list(range(1, 20))
        random.shuffle(a)

        display(a)

        pygame.time.wait(200)

        selection_sort(a)
        vis = False

    screen.blit(txt, (360, 20))
    pygame.display.update()
