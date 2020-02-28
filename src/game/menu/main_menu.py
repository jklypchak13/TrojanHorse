# Setup Python ----------------------------------------------- #
import sys
import pygame
import os
import pathlib

# Relative Imports
from game.engine.game import game
from game.menu.team_screen import team_screen
from game.style import color as cval
from game.style import text


PATH_TO_DIR = pathlib.Path(__file__).parent.absolute()

background = pygame.image.load(
    f"{PATH_TO_DIR}{os.sep}..{os.sep}..{os.sep}assets{os.sep}menu{os.sep}main_menu_background.png"
)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu(window, main_clock):
    while True:
        window.fill(cval.black)  # fill window with black
        window.blit(background, [0, 0])

        draw_text("main menu", text.default_font, cval.black, window, 400, 200)

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)

        pygame.draw.rect(window, cval.green, button_1)
        pygame.draw.rect(window, cval.blue, button_2)

        mx, my = pygame.mouse.get_pos()

        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.button)
                if event.button == 1:
                    clicked = True

        if clicked:
            # check for click location
            if button_1.collidepoint((mx, my)):
                game(window, main_clock)
            if button_2.collidepoint((mx, my)):
                team_screen(window, main_clock)

        pygame.display.update()
        main_clock.tick(60)
