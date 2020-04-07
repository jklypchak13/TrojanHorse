from typing import List, Tuple

import pygame  # type: ignore

from assets import PLAYER

from ..levels import load_level
from .entity import GameObject, PhysicsObject, Player, Star

PLAYER_DIMENSIONS: Tuple[int, int] = (50, 50)


class GameState:
    """
    GameState

    Singleton class, stores state of the game
    """

    static_objects: List[GameObject] = []
    physics_objects: List[PhysicsObject] = []
    player: Player = None
    goal: Star = None
    level: int = 1

    @classmethod
    def load_level(cls) -> None:
        """
        Loads a Level from JSON

        sets all corresponding values to setup the level
        """
        try:
            start_pos, cls.static_objects, cls.physics_objects, cls.goal = load_level(
                cls.level
            )
            cls.player = Player(
                pygame.Rect(*start_pos, *PLAYER_DIMENSIONS), PLAYER, 0.0, 0.0
            )
        except FileNotFoundError:
            # You win
            pass

    @classmethod
    def next_level(cls) -> None:
        """
        Move to next level

        Loads the next level from JSON
        """
        cls.level += 1
        cls.load_level()
