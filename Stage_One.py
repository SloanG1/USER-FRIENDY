# Import files/modules
import pygame
import sys
import time

pygame.init()

WIDTH = 600
HEIGHT = 500
Py_Window = pygame.display.set_mode((WIDTH, HEIGHT))  # Create py window
pygame.display.set_caption("USER FRIENDY")  # Window Game Caption
name_dict = {'Gavin': 'June 16', 'Rebecca': 'June 16',
             'James': 'June 3', 'Joseph': 'June 25',
             'Robert': 'July 4', 'Benjamin': 'July 11',
             'Emma': 'July 19', 'Liam': 'July 30',
             'Ava': 'August 1', 'Thomas': 'August 29',
             'William': 'August 18', 'Henry': 'August 5',
             'Lucas': 'September 2', 'David': 'September 10',
             'Frank': 'September 13', 'Noah': 'September 27',
             'Charlotte': 'October 6', 'Amelia': 'October 9',
             'Charles': 'October 24', 'Olivia': 'October 17',
             'Theodore': 'November 3', 'Edward': 'November 8',
             'George': 'November 12', 'John': 'November 26',
             'Daniel': 'December 1', 'Paul': 'December 10',
             'Mary': 'December 14', 'Andrew': 'December 25',
             'Jennifer': 'January 22', 'Richard': 'January 3',
             'Sarah': 'January 19', 'Christopher': 'January 31',
             'Matthew': 'February 5', 'Lisa': 'February 11',
             'Margaret': 'February 20', 'Steven': 'February 29',
             'Klayton': 'March 10', 'Ashley': 'March 13',
             'Timothy': 'March 4', 'Brian': 'March 28',
             'Michelle': 'April 2', 'Laura': 'April 8',
             'Jason': 'April 16', 'Ryan': 'April 27',
             'Jacob': 'May 1', 'Nicholas': 'May 7',
             'Anna': 'May 21', 'Katherine': 'May 29'}

letter_dict = {'A': 'g', 'B': 'C', 'C': 'x', 'D': 'F', 'E': 's',
               'F': 'i', 'G': 'I', 'H': 'm', 'I': 'Z', 'J': 'M',
               'K': 'G', 'L': 'P', 'M': 'r', 'N': 'a', 'O': 'B',
               'P': 'X', 'Q': 'A', 'R': 'n', 'S': 'J', 'T': 'e',
               'U': 'f', 'V': 't', 'W': 'l', 'X': 'H', 'Y': 'w',
               'Z': 'U', 'a': 'y', 'b': 'q', 'c': 'N', 'd': 'j',
               'e': 'o', 'f': 'D', 'g': 'c', 'h': 'd', 'i': 'K',
               'j': 'v', 'k': 'u', 'l': 'O', 'm': 'L', 'n': 'h',
               'o': 'z', 'p': 'Q', 'q': 'k', 'r': 'E', 's': 'T',
               't': 'R', 'u': 'W', 'v': 'b', 'w': 'Y', 'x': 'V',
               'y': 'S', 'z': 'p'}


class Stage_One:
    # Data Attributes
    __name = ''

    # Init
    def __init__(self, name_dict):
        self.set_name_dict(name_dict)


    # Helper
    def update_init_name(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Enter your first name", True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 3)
        Py_Window.blit(text, text_rect)

        name_box = pygame.Rect(200, 200, 140, 32)
        user_init_text = ''
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
                        user_init_text += event.unicode
                        self.set_name = user_init_text

            pygame.draw.rect(Py_Window, [0, 0, 0], name_box)

            text_surface = pygame.font.Font('freesansbold.ttf', 32).render(user_init_text, True, (255, 255, 255))

            # render at position stated in arguments
            Py_Window.blit(text_surface, (WIDTH//2, HEIGHT//2))

            # set width of textfield so that text cannot get
            # outside of user's text input
            name_box.w = max(100, text_surface.get_width() + 10)
            pygame.display.update()

    def update_validate_name(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Validate name', True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 1.5)
        Py_Window.blit(text, text_rect)
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
                            if user_text == self.get_name():
                                Stage_One.update_dob()

                            else:
                                Py_Window.fill((0, 0, 0))  # Set Background color
                                text = font.render('NAMES DO NOT MATCH', True, (255, 0, 0), (0, 0, 0))
                                Py_Window.blit(text, text_rect)
                                pygame.display.update()
                                time.sleep(1)
                            return False
                        else:
                            Py_Window.fill((0, 0, 0))  # Set Background color
                            text = font.render('NAME IS NOT REAL', True, (255, 0, 0), (0, 0, 0))
                            Py_Window.blit(text, text_rect)
                            pygame.display.update()
                            time.sleep(1)
                            return True

                    else:
                        try:
                            user_text += letter_dict.get(event.unicode)

                        except TypeError:
                            pass

            pygame.draw.rect(Py_Window, [0, 0, 0], name_box)

            text_surface = pygame.font.Font('freesansbold.ttf', 32).render(user_text, True, (255, 255, 255))

            # render at position stated in arguments
            Py_Window.blit(text_surface, (WIDTH // 2, HEIGHT // 1.2))

            # set width of textfield so that text cannot get
            # outside of user's text input
            name_box.w = max(100, text_surface.get_width() + 10)
            pygame.display.update()

    @staticmethod
    def update_dob():
        Py_Window.fill((0, 0, 0))  # Set Background color
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Enter DoB', True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 3)
        Py_Window.blit(text, text_rect)

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
        return self.__name_dict

    def get_name(self):
        return self.__name

    # Setters
    def set_name_dict(self, name_dict):
        self.__name_dict = name_dict

    def set_name(self, name):
        self.name = name

    # To String
    def __str__(self):
        stage_one_string = ""
        stage_one_string += ("Stage One Object Details->" +
                             "\n\tName Dict: " + str(self.get_name_dict()) +
                             "\n\tName: " + str(self.get_name()))
