from Name_Game import Name_Game
import os
import pygame


def main():
    game_window = Name_Game(900, 700, 60)
    game_window.init_name()

    pygame.quit()  # quits the game loop and exits window


if __name__ == '__main__':
    main()
