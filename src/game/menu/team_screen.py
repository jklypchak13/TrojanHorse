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

def team_screen(window, main_clock):
    running = True
    
    print("FROM TEAM_SCREEN: running =", running)
    while running:
        window.fill(cval.white)
     
        team_members = [
                'Aidan Globus', 'Cameron Millspaugh','Jarod Klypchak',
                'Kat Husar','Nick Dewey','Nick Hackman'
                ]
        
        draw_text('Team Name: Undecided', text.default_font, cval.black, window, 20, 20)
        
        loc_x = 20
        loc_y = 20
        vert_space = 20
        for mem in team_members:
            loc_y += vert_space
            draw_text(mem, text.default_font, cval.black, window, loc_x, loc_y)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        main_clock.tick(60)
        
    print("FROM TEAM_SCREEN: running =", running)

