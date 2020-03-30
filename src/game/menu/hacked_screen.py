# Package imports
import sys
import os
import pygame

# Relative imports
from game.style import color as cval
from game.style import text as txt


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def hacked_screen(window, main_clock, PATH_TO_ROOT):
    hacked_icon = pygame.image.load(
        f"{PATH_TO_ROOT}{os.sep}assets{os.sep}menu{os.sep}hacked_icon.png"
    )
    
    bkg_img = pygame.image.load(
        f"{PATH_TO_ROOT}{os.sep}assets{os.sep}menu{os.sep}hacked_background.jpg"
    )
    
    msg = txt.hacked_title.render("You've been hacked!", 1, cval.white)

    running = True
    print("FROM HACKED_SCREEN: running =", running)
    while running:
        window.fill(cval.black)
        window.blit(bkg_img, (0, 0))

        # Window height and width
        win_width, win_height = window.get_size()

        # Place hacked_icon in top center
        loc_x = win_width / 2 - hacked_icon.get_width() / 2
        loc_y = win_height / 3 - hacked_icon.get_height() / 2
        window.blit(hacked_icon, (loc_x, loc_y))

        # Place hacked_icon in top center
        loc_x = win_width / 2 - msg.get_width() / 2
        loc_y = win_height * 2 / 3 - msg.get_height() / 2
        window.blit(msg, (loc_x, loc_y))

        # Respond to click or keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Update window and set clock speed
        pygame.display.update()
        main_clock.tick(60)

    print("FROM TEAM_SCREEN: running =", running)
