# Import files/modules
import draw_window
import pygame

WIDTH = 600
HEIGHT = 500
def init_name():
    pygame.init()
    # Initial Name input
    font = font.Font('freesansbold.ttf', 32)
    text = font.render('Please enter your first name', True, (0, 0, 0), (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    draw_window.Py_Window.blit(text, textRect)


