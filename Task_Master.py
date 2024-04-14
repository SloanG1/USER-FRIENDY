import pygame

WIDTH = 600
HEIGHT = 500
py_window = pygame.display.set_mode((WIDTH, HEIGHT))  # Create py window
pygame.display.set_caption("USER FRIENDY")  # Window Game Caption


running = True
task_master_state = "Task Master"

font = pygame.font.Font('freesansbold.ttf', 32)
TEXT_COLOR = (0, 0, 0)

# Images for buttons
taskmaster_img = pygame.image.load('C:\Users\rw318\OneDrive\Desktop\taskmaster2.png')
credits_img = pygame.image.load('C:\Users\rw318\OneDrive\Desktop\tcredits.png')
settings_img = pygame.image.load('C:\Users\rw318\OneDrive\Desktop\tsettings.png')

py_window.blit(taskmaster_img, (304, 125))
py_window.blit(settings_img, (297, 250))
py_window.blit(credits_img, (336, 375))

pygame.display.update()


def task_master_window():
    text_rect = text.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)

    py_window.blit(text, text_rect)
    py_window.fill((255, 178, 102))  # Set Background color
    pygame.display.flip()


while running:

    py_window.fill((255, 178, 102))  # Set Background color
    text = font.render("User Friendy", True, (0, 0, 0), (0, 0, 0))

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
