import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 605))
pygame.display.set_caption('Quick Sort Visualizer')

black = (40, 40, 40)
red = (255, 0, 0)
green = (0, 255, 0)
font = pygame.font.Font("OdibeeSans-Regular.ttf", 25)
txt = font.render("Visualize", True, (0, 0, 0))

a = list(range(1, 20))
random.shuffle(a)


def draw_arrow(i, j):
    i = 40*i - 5
    j = 40*j - 5
    pygame.draw.line(screen, (0, 0, 255), (i, 575), (i, 596), 6)
    pygame.draw.polygon(screen, (0, 0, 255), [(i - 7, 575), (i + 7, 575), (i, 568)])
    pygame.draw.line(screen, (0, 0, 255), (j, 575), (j, 596), 6)
    pygame.draw.polygon(screen, (0, 0, 255), [(j - 7, 575), (j + 7, 575), (j, 568)])
    pygame.draw.line(screen, (0, 0, 255), (i-1, 596), (j+2, 596), 6)
    pygame.display.update()


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                sys.exit()
        if arr[j] < pivot:
            i += 1
            if i != j:
                display(arr, (i, j), p=high)
                draw_arrow(i + 1, j + 1)
                pygame.time.wait(300)
                arr[i], arr[j] = arr[j], arr[i]
                display(arr, p=high)
                pygame.display.update()
                pygame.time.wait(300)
    if i+1 != high:
        display(arr, (i+1, high), p=high)
        draw_arrow(i + 2, high + 1)
        pygame.time.wait(300)
        arr[i+1], arr[high] = arr[high], arr[i+1]
        display(arr)
        pygame.display.update()
        pygame.time.wait(300)
    return i+1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def display(arr, r=(), p=None):
    screen.fill((211, 211, 211))
    for i in range(19):
        if i == p:
            color = green
        elif i in r:
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

        quick_sort(a, 0, len(a)-1)
        vis = False

    screen.blit(txt, (360, 20))
    pygame.display.update()
