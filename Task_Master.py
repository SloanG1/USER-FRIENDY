import pygame
import sys

WIDTH = 600
HEIGHT = 500
py_window = pygame.display.set_mode((WIDTH, HEIGHT))  # Create py window
pygame.display.set_caption("USER FRIENDY")  # Window Game Caption


def screen_text(text, font, text_col, x, y):
    screen_txt = font.render(text, True, text_col)
    py_window.blit(screen_txt, (x, y))


running = True
task_master_state = "main"

font = pygame.font.Font('freesansbold.ttf', 32)
TEXT_COLOR = (0, 0, 0)

while running:

    py_window.fill((255, 178, 102))  # Set Background color
    text = font.render("Taskmaster", True, (0, 0, 0), (0, 0, 0))

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()


def task_master_window():
    text_rect = text.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)

    py_window.blit(text, text_rect)
    py_window.fill((255, 178, 102))  # Set Background color
    pygame.display.flip()
