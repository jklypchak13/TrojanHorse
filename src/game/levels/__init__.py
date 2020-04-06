from typing import Tuple, List, Dict, Any
from game.engine.enemy import Enemy
from game.engine.platform import Platform
from game.engine.game_object import GameObject
from game.engine.physics_object import PhysicsObject

import json
import os
from pygame import Rect
import pathlib
from pathlib import Path

# Intialize Useful Constants
PATH_TO_LEVELS: str = pathlib.Path(__file__).parent.absolute()
PLATFORM_IMAGE_URL: str = Path(
    __file__
).parent.parent.parent.absolute().__str__() + os.path.sep + "assets" + os.path.sep + "game" + os.path.sep + "GRASS_TILE.png"
ENEMY_IMAGE_URL: str = Path(
    __file__
).parent.parent.parent.absolute().__str__() + os.path.sep + "assets" + os.path.sep + "game" + os.path.sep + "greek_soldier.png"
ENEMY_WIDTH: int = 30
ENEMY_HEIGHT: int = 30


def load_level(
    level_number: int,
) -> Tuple[Tuple[int, int], List[GameObject], List[PhysicsObject]]:
    """Get the game objects of the corresponding level.

    Arguments:
        level_number {int} -- The number of the desired level.
    Returns:
        Tuple[Tuple[int, int], List[int], List[int]] -- Returns the starting position,
         static objects, and physics objects.

        Tuple[int,int]: starting position
        List[GameObject]: the static objects of the levels
        List[PhysicsObject]: the list of non-player Physics Objects
    """

    # Read Level Data
    level_data: Dict[str, Any] = {}
    with open(f"{PATH_TO_LEVELS}{os.path.sep}level_{level_number}.json", "r") as fp:
        level_data = json.load(fp)

    # Initialize Data Structures
    static_objects: List[int] = []
    physics_objects: List[int] = []
    starting_position: Tuple[int, int] = (
        level_data["starting_position"][0],
        level_data["starting_position"][1],
    )

    # Read Static Objects/Platforms
    for static_object in level_data["static_objects"]:
        x: int = static_object[0]
        y: int = static_object[1]
        width: int = static_object[2]
        height: int = static_object[3]

        current_rect: Rect = Rect(x, y, width, height)
        static_objects.append(Platform(current_rect, PLATFORM_IMAGE_URL, True))

    # Read Physics Objects/Enemies
    for physics_object in level_data["physics_objects"]:
        x: int = physics_object[0]
        y: int = physics_object[1]
        x_velocity: int = physics_object[2]

        current_rect: Rect = Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
        physics_objects.append(Enemy(current_rect, ENEMY_IMAGE_URL, x_velocity, 0))

    return starting_position, static_objects, physics_objects
