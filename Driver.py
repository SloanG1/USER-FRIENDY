import draw_window
import pygame
# import Task_Master


def main():
    run = True
    while run:
        for event in pygame.event.get():  # For loop looks for events
            if event.type == pygame.QUIT:  # User quit window
                run = False

        draw_window.draw_window()  # Call function
    #    Task_Master.task_master_window()

    pygame.quit()  # quits the game loop and exits window


if __name__ == '__main__':
    main()
