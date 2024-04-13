import pygame
from Stage_One import Stage_One

WIDTH = 600
HEIGHT = 500
Py_Window = pygame.display.set_mode((WIDTH, HEIGHT))  # Create py window
pygame.display.set_caption("USER FRIENDY")  # Window Game Caption
St1 = Stage_One({})


def draw_window():
    Py_Window.fill((0, 0, 0))  # Set Background color
    St1.update_init_name()
    St1.update_validate_name()
