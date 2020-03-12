import pygame

# Relative Imports
from game.menu.main_menu import main_menu

# load image assets
main_menu_bkground = pygame.image.load(r".\assets\menu\main_menu_background.png")
#img_twitter = pygame.image.load(r".\assets\menu\twitter_icon.png")

if __name__ == "__main__":
    # Initialize pygame and the main clock
    pygame.init()
    main_clock = pygame.time.Clock()
    
    # Create a window with 4:3 aspect ratio
    window = pygame.display.set_mode((800, 600),0,32)
    pygame.display.set_caption('HORSE')
    window_icon = pygame.image.load(r".\assets\menu\app_icon.png")
    pygame.display.set_icon(window_icon)

    # Start the main menu
    main_menu(window, main_clock, main_menu_bkground)
    
    # Clean up
    pygame.quit()
    
