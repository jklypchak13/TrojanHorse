# New Game
# Team window
#  - about us
# Quit

# Setup Python ----------------------------------------------- #
import sys
import pygame

# Relative Imports
from game.engine.game import game
from game.menu.team_screen import team_screen
from game.style import color as cval
from game.style import text 


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
 
def main_menu(window):
    
    window.fill(cval.black)    #fill window with black
    draw_text('main menu', text.default_font, cval.white, window, 20, 20)
 
    mx, my = pygame.mouse.get_pos()
 
    button_1 = pygame.Rect(50, 100, 200, 50)
    button_2 = pygame.Rect(50, 200, 200, 50)

    pygame.draw.rect(window, cval.green, button_1)
    pygame.draw.rect(window, cval.blue, button_2)
    
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
 
    next_screen = main_menu
    if clicked:
        # check for click location
        if button_1.collidepoint((mx, my)):
            next_screen = game
        if button_2.collidepoint((mx, my)):
            next_screen = team_screen
    
    return next_screen

    
