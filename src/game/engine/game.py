import sys
import os
from pathlib import Path

import pygame  # type: ignore
from game.levels import load_level
from .player import Player
from .draw_manager import DrawManager
from .collision_manager import CollisionManager
from .obstacle import Obstacle
from game.style import color as cval  # type: ignore
from game.style import text

PATH_TO_DIR = Path(__file__).parent.absolute()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def game(screen, main_clock, PATH_TO_ROOT):
    running = True

    print("FROM GAME: running =", running)
    PLAYER_IMAGE = (
        f"{PATH_TO_DIR}{os.sep}..{os.sep}..{os.sep}assets{os.sep}game{os.sep}horsey.png"
    )
    player_start_pos, static_objects, physics_objects = load_level(1)
    player = Player(pygame.Rect(
        player_start_pos[0], player_start_pos[1], 100, 100), PLAYER_IMAGE)
    draw_manager = DrawManager(screen, player, static_objects, physics_objects)
    collision_manager = CollisionManager(
        player, static_objects, physics_objects)
    while running:
        running = True

        screen.fill(cval.black)

        draw_text("game", text.default_font, cval.white, screen, 20, 20)
        
        player.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key in player.controls:
                    player.controls[event.key]()

        # Check collisions
        #collision_manager.check_all_collisions()

        draw_manager.adjust_screen()
        draw_manager.draw_all()
       
        if player.life == 0:
            screen.fill(cval.black)
            GOfont = pygame.font.SysFont("Arial", 70)
            draw_text("Game Over", GOfont, cval.white, screen, 200, 200)


        main_clock.tick(60)

            

    print("FROM GAME: running =", running)

    return
