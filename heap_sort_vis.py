import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 605))
pygame.display.set_caption('Heap Sort Visualizer')

black = (40, 40, 40)
red = (255, 0, 0)
purple = (128, 0, 128)
font = pygame.font.Font("OdibeeSans-Regular.ttf", 25)
txt = font.render("Visualize", True, (0, 0, 0))

a = list(range(1, 20))
random.shuffle(a)

compl = []


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        display(arr, (i, largest), completed=compl)
        draw_arrow(i + 1, largest + 1)
        pygame.time.wait(300)
        arr[i], arr[largest] = arr[largest], arr[i]
        display(arr, completed=compl)
        pygame.display.update()
        pygame.time.wait(300)

        heapify(arr, n, largest)


def heap_sort(arr):
    global compl
    compl = []
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        display(arr, (i, 0), completed=compl)
        draw_arrow(i + 1, 1)
        pygame.time.wait(300)
        arr[i], arr[0] = arr[0], arr[i]
        compl.append(i)
        display(arr, completed=compl)
        pygame.display.update()
        pygame.time.wait(300)
        heapify(arr, i, 0)
    compl.append(0)

    return arr


def display(arr, r=(), completed=()):
    screen.fill((211, 211, 211))
    for i in range(19):
        if i in completed:
            color = purple
        elif i in r:
            color = red
        else:
            color = black
        pygame.draw.rect(screen, color, pygame.Rect(20 + 40*i, 560-arr[i]*25, 30, arr[i]*25))


def draw_arrow(i, j):
    i = 40*i - 5
    j = 40*j - 5
    pygame.draw.line(screen, (0, 0, 255), (i, 575), (i, 596), 6)
    pygame.draw.polygon(screen, (0, 0, 255), [(i - 7, 575), (i + 7, 575), (i, 568)])
    pygame.draw.line(screen, (0, 0, 255), (j, 575), (j, 596), 6)
    pygame.draw.polygon(screen, (0, 0, 255), [(j - 7, 575), (j + 7, 575), (j, 568)])
    pygame.draw.line(screen, (0, 0, 255), (i-1, 596), (j+2, 596), 6)
    pygame.display.update()


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

        display(a, completed=compl)

        pygame.time.wait(200)

        heap_sort(a)
        vis = False

    screen.blit(txt, (360, 20))
    pygame.display.update()