import sys
import os
from pathlib import Path

import pygame  # type: ignore
from game.levels import load_level
from .game_state import GameState
from .player import Player
from .draw_manager import DrawManager
from .collision_manager import CollisionManager
from .physics_object import PhysicsObject
from .input_manager import InputManager
from .obstacle import Obstacle
from .platform import Axis
from game.style import color as cval  # type: ignore
from game.style import text

PATH_TO_ASSETS: str = f"{Path(__file__).parent.parent.parent.absolute()}{os.sep}assets{os.sep}game{os.sep}"

Gofont = pygame.font.SysFont("Arial", 70)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def game(screen, main_clock, PATH_TO_ROOT):
    running = True

    print("FROM GAME: running =", running)
    PLAYER_IMAGE = f"{PATH_TO_ASSETS}horsey.png"
    BACKGROUND_IMAGE_PATH = f"{PATH_TO_ASSETS}sky.png"
    player_start_pos, static_objects, physics_objects = load_level(1)
    player = Player(
        pygame.Rect(player_start_pos[0], player_start_pos[1], 50, 50),
        PLAYER_IMAGE,
        0.0,
        0.0,
    )
    GameState.static_objects = static_objects
    GameState.physics_objects = physics_objects
    GameState.player = player
    draw_manager = DrawManager(screen, BACKGROUND_IMAGE_PATH)
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

        draw_manager.adjust_screen()
        if not player.life == 0:
            input_manager.handle_input()
            physics_tick(collision_manager)
            # Check collisions
            collision_manager.check_all_collisions()
            draw_manager.draw_all()
        else:
            cbackground = pygame.image.load(f"{PATH_TO_ASSETS}redSquare.png")
            screen.fill(cval.black)
            screen.blit(cbackground, (0, 0))  # Overlay background image
            draw_text("Game Over", Gofont, cval.white, screen, 250, 250)
            pygame.display.update()

        main_clock.tick(60)

    print("FROM GAME: running =", running)

    return


def physics_tick(collision_manager: CollisionManager) -> None:
    """
    Perform a single tick for all physics objects

    Parameters
    ----------

    collision_manager: CollisionManager
          Handles Collisions between GameObjects
    """
    GameState.player.update_x()
    collision_manager.player_collides_static(Axis.XAxis)
    GameState.player.update_y()
    collision_manager.player_collides_static(Axis.YAxis)
    for phys_obj in GameState.physics_objects:
        update_physics_obj(phys_obj, collision_manager)


def update_physics_obj(obj: PhysicsObject, collision_manager: CollisionManager) -> None:
    """
    Update Physics Objects X and Y values

    handling collisions with static objects

    Parameters
    ----------

    obj: PhysicsObject
      Object to update

    collision_manager: CollisionManager
      Handle collisions between objects and static objects
    """
    obj.update_x()
    collision_manager.phys_collides_static(Axis.XAxis)
    obj.update_y()
    collision_manager.phys_collides_static(Axis.YAxis)
