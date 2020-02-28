import pygame
import os
import pathlib

# Relative Imports
from game.menu.main_menu import main_menu

PATH_TO_DIR = pathlib.Path(__file__).parent.absolute()

# load image assets
main_menu_bkground = pygame.image.load(
    f"{PATH_TO_DIR}{os.sep}assets{os.sep}menu{os.sep}main_menu_background.png"
)

if __name__ == "__main__":
    # Initialize pygame and the main clock
    pygame.init()
    main_clock = pygame.time.Clock()

    # Create a window with 4:3 aspect ratio
    window = pygame.display.set_mode((800, 600), 0, 32)
    pygame.display.set_caption("HORSE")
    window_icon = pygame.image.load(
        f"{PATH_TO_DIR}{os.sep}assets{os.sep}menu{os.sep}app_icon.png"
    )
    pygame.display.set_icon(window_icon)

    # Start the main menu
    main_menu(window, main_clock, main_menu_bkground)

    # Clean up
    pygame.quit()
