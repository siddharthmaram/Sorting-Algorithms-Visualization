import pygame_menu
import pygame
import os

pygame.init()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Sorting Visualizer")

algo = 1


def set_algo(value, difficulty):
    global algo
    algo = value[0][1]


def start_the_game():
    if algo == 1:
        os.system("python quick_sort_vis.py")
    elif algo == 2:
        os.system("python bubble_sort_vis.py")
    elif algo == 3:
        os.system("python selection_sort_vis.py")
    else:
        os.system("python heap_sort_vis.py")


menu = pygame_menu.Menu('Welcome', 600, 400, theme=pygame_menu.themes.THEME_ORANGE)

menu.add.selector('Sorting Algorithm :', [('Quick Sort', 1), ('Bubble Sort', 2), ('Selection Sort', 3), ('Heap Sort', 4)], onchange=set_algo)
menu.add.button('Start', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
