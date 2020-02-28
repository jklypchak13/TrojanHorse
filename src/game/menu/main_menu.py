# Package imports
import pygame

# Relative Imports
from game.engine.game import game
from game.menu.hacked_screen import hacked_screen
from game.menu.team_screen import team_screen
from common.button import Button
from game.style import color as cval
from game.style import text as txt


def main_menu(window, main_clock, background):
    # Set variables
    title = txt.menu_title.render("HORSE", 1, cval.black)
    running = True

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
        loc_x = win_width * 3 / 4 - btn_width / 2
        loc_y = win_height * 2 / 3 - btn_height / 2
        team_menu_btn = Button(
            cval.white, loc_x, loc_y, btn_width, btn_height, "Credits"
        )

        # Display menu buttons
        play_btn.draw(window)
        team_menu_btn.draw(window)

        hacked_screen_btn = Button(cval.white, 20, 20, btn_width, btn_height, "Hacked")
        hacked_screen_btn.draw(window)

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

        pygame.display.update()
        main_clock.tick(60)
