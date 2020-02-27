import pygame
import sys
from game.style import color as cval
from game.style import text
from game.menu import main_menu

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def game(screen):
    next_screen = game

    running = True

    screen.fill(cval.black)
   
    draw_text('game', text.default_font, cval.white, screen, 20, 20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                next_screen = None
                running = False
    
    print("FROM GAME: running =", running)
    
    return next_screen

