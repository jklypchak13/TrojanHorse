import os
import sys
from pathlib import Path

import pygame  # type: ignore

from ..style import color as cval  # type: ignore
from .collision_manager import CollisionManager
from .draw_manager import DrawManager
from .game_state import GameState
from .input_manager import InputManager
from .physics_object import PhysicsObject
from .platform import Axis

PATH_TO_ASSETS: str = f"{Path(__file__).parent.parent.parent.absolute()}{os.sep}assets{os.sep}game{os.sep}"
BACKGROUND_IMAGE_PATH = f"{PATH_TO_ASSETS}sky.png"

GAME_OVER_FONT = pygame.font.SysFont("Arial", 70)


def game(screen, main_clock, PATH_TO_ROOT):
    running = True

    GameState.load_level()
    draw_manager = DrawManager(screen, BACKGROUND_IMAGE_PATH)
    collision_manager = CollisionManager()
    input_manager = InputManager()
    while running:
        running = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_manager.adjust_screen()
        if not GameState.player.lives == 0:
            input_manager.handle_input()
            physics_tick(collision_manager)
            # Check collisions
            collision_manager.check_all_collisions()
            draw_manager.draw_all()
        else:
            cbackground = pygame.image.load(f"{PATH_TO_ASSETS}GameOver.jpg")
            screen.blit(cbackground, (0, 0))  # Overlay background image
            draw_manager.draw_text(
                "Game Over", GAME_OVER_FONT, cval.white, screen, 250, 250
            )
            pygame.display.update()

        main_clock.tick(60)


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
