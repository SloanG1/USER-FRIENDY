# Import files/modules
import pygame


class Name_Game:
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

    def init_name(self):
        # Create Game Window
        pygame.init()
        Py_Window = pygame.display.set_mode((self.get_width(), self.get_height()))  # Create py window
        pygame.display.set_caption("USER FRIENDY")  # Window Game Caption
        Py_Window.fill((255, 255, 255)) # Set Background color

        # Initial Name input
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Please enter your first name', True, (0, 0, 0), (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (self.get_width() // 2, self.get_height() // 2)
        Py_Window.blit(text, textRect)
        pygame.display.update()

        font = pygame.font.SysFont('freesansbold.ttf', 32)

        def draw_text(text, font, text_col, x, y):
            img = font.render(text, True, text_col)
            width = img.get_width()
            Py_Window.blit(img, (x - (width / 2), y))

            pygame.display.update()

        run = True
        while run:

            draw_text(text, font, (0, 0, 0), self.get_width() / 2, 200)
            for event in pygame.event.get():

                if event.type == pygame.TEXTINPUT:
                    text += event.text
                if event.type == pygame.QUIT:
                    run = False

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