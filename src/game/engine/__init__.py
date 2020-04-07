import os
import sys
from pathlib import Path

import pygame  # type: ignore

from ..style import color as cval  # type: ignore
from .collision_manager import CollisionManager
from .draw_manager import DrawManager
from .game_state import GameState
from .input_manager import InputManager
from .entity import PhysicsObject, Axis


def game(screen: pygame.Surface, main_clock: pygame.time.Clock) -> None:
    """
    Main game loop

    Parameters
    ----------

    screen: pygame.Surface
      Screen to display game on

    main_clock: pygame.time.Clock
      Game clock
    """

    GameState.load_level()
    draw_manager = DrawManager(screen)
    collision_manager = CollisionManager()
    input_manager = InputManager()

    running: bool = True
    while running and GameState.player.alive():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        draw_manager.adjust_screen()
        input_manager.handle_input()
        physics_tick(collision_manager)
        collision_manager.check_all_collisions()
        if collision_manager.player_collides_goal():
            # Level completed
            print(f"Level {GameState.level} completed!")
            GameState.next_level()

        draw_manager.draw_all()
        pygame.display.update()
        main_clock.tick(60)

    if not GameState.player.alive():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
            draw_manager.draw_game_over()
            pygame.display.update()


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
