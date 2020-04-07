from typing import Any

from .game_object import GameObject
from .physics_object import PhysicsObject

import pygame  # type: ignore


class Star(GameObject):
    """
    Star

    Goal object in a level to go to the next level or beat the game

    TODO: possible have the star start near the player then fly to the end of the level
    """
