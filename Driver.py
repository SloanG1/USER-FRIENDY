from GameWindow import Game_Window
import os
import pygame


def main():
    game_window = Game_Window(900, 700, 60)
    game_window.draw_window()
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()  # quits the game loop and exits window


if __name__ == '__main__':
    main()
