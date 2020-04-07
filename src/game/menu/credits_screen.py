# Package imports
import sys

import pygame

from assets import CREDITS
from game.style import color as cval
from game.style import text as txt


def credits_screen(window, main_clock, PATH_TO_ROOT):
    running = True

    # Window height and width
    win_width, win_height = window.get_size()

    bkg_img = pygame.image.load(CREDITS)

    team_members = [
        "Aidan Globus",
        "Cameron Millspaugh",
        "Jarod Klypchak",
        "Kat Husar",
        "Nick Dewey",
        "Nick Hackman",
    ]

    team_name = txt.default_font.render("Team Name: Undecided", 1, cval.white)
    member_names = []

    for name in team_members:
        member_names.append(txt.default_font.render(name, 1, cval.white))

    while running:
        window.fill(cval.white)
        window.blit(bkg_img, (0, 0))

        txt.default_font.render("Enter verification code", 1, cval.white)

        loc_x = win_width / 2 - team_name.get_width() / 2
        loc_y = win_height / 3 - team_name.get_height() / 2
        y_offset = 24

        window.blit(team_name, (loc_x, loc_y))

        for name in member_names:
            loc_x = win_width / 2 - name.get_width() / 2
            loc_y += y_offset
            window.blit(name, (loc_x, loc_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        main_clock.tick(60)
