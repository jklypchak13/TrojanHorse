import pygame

# Relative Imports
from game.menu.main_menu import main_menu


if __name__ == "__main__":
    # Setup pygame/window ---------------------------------------- #
    mainClock = pygame.time.Clock()
    
    # initialize pygame window
    pygame.init()
    window = pygame.display.set_mode((800, 600),0,32)
    pygame.display.set_caption('HORSE')
    window_icon = pygame.image.load(r".\assets\menu\app_icon.png")
    pygame.display.set_icon(window_icon)


    screen = main_menu

    while True:
        if screen == None:
            # set default screen
            screen = main_menu
        
        # call the function that runs the next screen
        screen = screen(window)
        
        pygame.display.update()
        mainClock.tick(60)