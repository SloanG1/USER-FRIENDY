# Import files/modules
import pygame
import sys

pygame.init()

WIDTH = 600
HEIGHT = 500
Py_Window = pygame.display.set_mode((WIDTH, HEIGHT))  # Create py window
pygame.display.set_caption("USER FRIENDY")  # Window Game Caption
name_dict = {'test':23}


class Stage_One:
    # Data Attributes
    __Name_Dict = {}

    # Init
    def __init__(self, name_dict):
        self.set_name_dict(name_dict)

    # Helpers
    @staticmethod
    def update_init_name(self=None):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Please enter your first name', True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 3)
        Py_Window.blit(text, textRect)

        name_box = pygame.Rect(200, 200, 140, 32)
        user_text = ''
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    # Check for backspace
                    if event.key == pygame.K_RETURN:
                        return False
                    else:
                        user_text += event.unicode

            pygame.draw.rect(Py_Window, [0, 0, 0], name_box)

            text_surface = pygame.font.Font('freesansbold.ttf', 32).render(user_text, True, (255, 255, 255))

            # render at position stated in arguments
            Py_Window.blit(text_surface, (WIDTH//2, HEIGHT//2))

            # set width of textfield so that text cannot get
            # outside of user's text input
            name_box.w = max(100, text_surface.get_width() + 10)
            self.__init_name = user_text
            pygame.display.update()

    @staticmethod
    def update_validate_name():
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Validate name', True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 1.5)
        Py_Window.blit(text, textRect)
        name_box = pygame.Rect(200, 200, 140, 32)
        user_text = ''
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    # Check for backspace
                    if event.key == pygame.K_RETURN:
                        if user_text in name_dict:
                            Stage_One.update_DoB()
                            return False
                        else:
                            return False

                    else:
                        user_text += event.unicode

            pygame.draw.rect(Py_Window, [0, 0, 0], name_box)

            text_surface = pygame.font.Font('freesansbold.ttf', 32).render(user_text, True, (255, 255, 255))

            # render at position stated in arguments
            Py_Window.blit(text_surface, (WIDTH // 2, HEIGHT // 1.2))

            # set width of textfield so that text cannot get
            # outside of user's text input
            name_box.w = max(100, text_surface.get_width() + 10)
            pygame.display.update()

    @staticmethod
    def update_DoB():
        Py_Window.fill((0, 0, 0))  # Set Background color
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Enter DoB', True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 3)
        Py_Window.blit(text, textRect)

        name_box = pygame.Rect(200, 200, 140, 32)
        user_text = ''
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    # Check for backspace
                    if event.key == pygame.K_RETURN:
                        return False
                    else:
                        user_text += event.unicode

            pygame.draw.rect(Py_Window, [0, 0, 0], name_box)

            text_surface = pygame.font.Font('freesansbold.ttf', 32).render(user_text, True, (255, 255, 255))

            # render at position stated in arguments
            Py_Window.blit(text_surface, (WIDTH // 2, HEIGHT // 2))

            # set width of textfield so that text cannot get
            # outside of user's text input
            name_box.w = max(100, text_surface.get_width() + 10)
            pygame.display.update()

    # Getters
    def get_name_dict(self):
        return self.__Name_Dict

    # Setters
    def set_name_dict(self, name_dict):
        self.__Name_Dict = name_dict

    # To String
    def __str__(self):
        stage_one_string = ""
        stage_one_string += ("Stage One Object Details->" +
                             "\n\tName Dict: " + str(self.get_name_dict()))
