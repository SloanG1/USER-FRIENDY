# Import files/modules
from Name_Game import Name_Game
import pygame
import os


class Game_Window:
    # Data Attributes
    __WIDTH = -1
    __HEIGHT = -1
    __FPS = -1

    # Init
    def __init__(self, width=900, height=600, fps=60):
        self.set_width(width)
        self.set_height(height)
        self.set_fps(fps)

    # Helpers
    def draw_window(self):
        pygame.init()
        Name_game = Name_Game(23, 23, 23)
        Py_Window = pygame.display.set_mode((self.get_width(), self.get_height()))  # Create py window
        pygame.display.set_caption("USER FRIENDY")  # Window Game Caption
        Py_Window.fill((255, 255, 255))
        pygame.display.update()

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Please enter your first name', True, (0, 0, 0), (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (self.get_width() // 2, self.get_height() // 2)
        Py_Window.blit(text, textRect)
        pygame.display.update()


    # Getters
    def get_width(self):
        return self.__WIDTH

    def get_height(self):
        return self.__HEIGHT

    def get_FPS(self):
        return self.__FPS

    # Setters
    def set_width(self, width):
        self.__WIDTH = width

    def set_height(self, height):
        self.__HEIGHT = height

    def set_fps(self, fps):
        self.__FPS = fps

    # To String

