from typing import Tuple, List, Dict, Any
from ..engine.enemy import Enemy
from ..engine.platform import Platform
from ..engine.game_object import GameObject
from ..engine.physics_object import PhysicsObject
from ..engine.star import Star

import json
import os
from pygame import Rect
import pathlib
from pathlib import Path

# Intialize Useful Constants
PATH_TO_LEVELS: str = pathlib.Path(__file__).parent.absolute()
ASSET_PATH: str = Path(
    __file__
).parent.parent.parent.absolute().__str__() + os.path.sep + "assets" + os.path.sep + "game" + os.path.sep
PLATFORM_IMAGE_URL: str = ASSET_PATH + "wood_platform.png"
HAY_IMAGE_URL: str = ASSET_PATH + "hay_bale.png"
GROUND_IMAGE_URL: str = ASSET_PATH + "GRASS_TILE.png"
ENEMY_IMAGE_URL_1: str = ASSET_PATH + "greek_soldier_walk1.png"
ENEMY_IMAGE_URL_2: str = ASSET_PATH + "greek_soldier_walk2.png"
ENEMY_IMAGE_URL_3: str = ASSET_PATH + "greek_soldier_walk3.png"
STAR_IMAGE_URL: str = ASSET_PATH + "star.png"

ENEMY_DIMENSIONS: Tuple[int, int] = (30, 50)
STAR_DIMENSIONS: Tuple[int, int] = (48, 48)


def load_level(
    level_number: int,
) -> Tuple[Tuple[int, int], List[GameObject], List[PhysicsObject], Star]:
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
    starting_position: Tuple[int, int] = tuple(level_data["starting_position"])

    # Read Ground Objects (as platforms)
    for ground in level_data["ground"]:
        current_rect: Rect = Rect(*ground)
        static_objects.append(Platform(current_rect, GROUND_IMAGE_URL, True))

    # Read Static Objects/Platforms
    for static_object in level_data["static_objects"]:
        current_rect: Rect = Rect(*static_object)
        image_url: str = PLATFORM_IMAGE_URL

        if current_rect.y == 500:
            image_url = HAY_IMAGE_URL
        static_objects.append(Platform(current_rect, image_url, True))

    # Read Physics Objects/Enemies
    for physics_object in level_data["physics_objects"]:
        x: int = physics_object[0]
        y: int = physics_object[1]
        x_velocity: int = physics_object[2]

        current_rect: Rect = Rect(x, y, *ENEMY_DIMENSIONS)

        e = Enemy(current_rect, ENEMY_IMAGE_URL_1, x_velocity, 0)
        e.set_animation_frames(
            [ENEMY_IMAGE_URL_1, ENEMY_IMAGE_URL_2, ENEMY_IMAGE_URL_3]
        )
        physics_objects.append(e)

    end_position: Tuple[int, int] = tuple(level_data["goal"])
    star: Star = Star(Rect(*end_position, *STAR_DIMENSIONS), STAR_IMAGE_URL)

    return starting_position, static_objects, physics_objects, star
