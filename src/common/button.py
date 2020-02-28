import pygame

# Relative imports
from game.style import text as txt

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
