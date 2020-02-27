import sys
import pygame
from game.style import color as cval
from game.style import text 

# Team Name
# Team Members


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def team_screen(window):
    running = True
    window.fill(cval.white)

    next_screen = team_screen
 
    draw_text('options', text.default_font, cval.black, window, 20, 20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                next_screen = None
    print("FROM TEAM_SCREEN: running =", running)
    
    return next_screen