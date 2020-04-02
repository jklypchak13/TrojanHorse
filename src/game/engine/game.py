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
        
        Player.update(player)
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

        collision_manager.check_all_collisions()

        draw_manager.adjust_screen()
        draw_manager.draw_all()

        main_clock.tick(60)
        if player.life == 0:
            running = False
            print("game over")
            screen.fill((0, 0, 0))
            font = pygame.font.Font('Papyrus.ttf', 30)
            text_surface = font.render("Game Over", True, (255,255,255))
            text_rect = text_surface.get_rect()
            text_rect.center = (250, 250)
            screen.blit(text_surface, text_rect)
            pygame.display.update()

    print("FROM GAME: running =", running)

    return
