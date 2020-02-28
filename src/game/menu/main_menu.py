# Setup Python ----------------------------------------------- #
import pygame

# Relative Imports
from game.engine.game import game
from game.menu.team_screen import team_screen
from game.style import color as cval
from game.style import text as txt

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
            
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = txt.menu_button
            # Create text object from string
            text = font.render(self.text, 1, (0,0,0))
            # Overlay object onto button
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def mouse_over(self, pos):
        # Mouse within allowable x range
        if pos[0] > self.x and pos[0] < self.x + self.width:
            # Mouse within allowable y range
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def main_menu(window, main_clock, background):
    title = "HORSE"
    title = txt.menu_title.render(title, 1, cval.black)
    running = True
    while running:
        window.fill(cval.black)    # Default to fill window with black
        window.blit(background, (0,0))  # Overlay background image

        # window height and width
        win_width, win_height = window.get_size()
        
        # Place Title in top center
        loc_x = win_width/2 - title.get_width()/2
        loc_y = win_height/3 - title.get_height()/2
        window.blit(title, (loc_x, loc_y))
     
        # Create and position play button
        btn_width = 90
        btn_height = 50
        loc_x = win_width/4 - btn_width/2
        loc_y = win_height*2/3 - btn_height/2
        play_btn = Button(cval.white, loc_x, loc_y, btn_width, btn_height, "Play")
        
        # Create and position options button
        loc_x = win_width*3/4 - btn_width/2
        loc_y = win_height*2/3 - btn_height/2
        team_menu_btn = Button(cval.white, loc_x, loc_y, btn_width, btn_height, "Credits")
    
        # Display menu buttons
        play_btn.draw(window)
        team_menu_btn.draw(window)
    
        # Get mouse position
        mx, my = pygame.mouse.get_pos()
        
        # Check for key press or mouse click event
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
     
        # React to mouse click
        if clicked:
            # Check for click location
            if play_btn.mouse_over((mx, my)):
                game(window, main_clock)
            if team_menu_btn.mouse_over((mx, my)):
                team_screen(window, main_clock)

        pygame.display.update()
        main_clock.tick(60)
