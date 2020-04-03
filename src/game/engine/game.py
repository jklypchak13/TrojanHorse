import sys
import os
from pathlib import Path

import pygame  # type: ignore
from game.levels import load_level
from .game_state import GameState
from .player import Player
from .draw_manager import DrawManager
from .collision_manager import CollisionManager
from .input_manager import InputManager
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
        player_start_pos[0], player_start_pos[1], 100, 100), PLAYER_IMAGE, 0.0, 0.0)
    GameState.static_objects = static_objects
    GameState.physics_objects = physics_objects
    GameState.player = player
    draw_manager = DrawManager(screen)
    collision_manager = CollisionManager()
    input_manager = InputManager()
    while running:
        running = True

        screen.fill(cval.black)

        draw_text("game", text.default_font, cval.white, screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check collisions
        input_manager.handle_input()

        collision_manager.check_all_collisions()

        draw_manager.adjust_screen()
        draw_manager.draw_all()

        main_clock.tick(60)

    print("FROM GAME: running =", running)

    return
