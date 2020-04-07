import json
import os
import pathlib
from typing import Any, Dict, List, Tuple

from pygame import Rect

from assets import ENEMY, ENEMY_SPRITE, GRASS, HAY, PLATFORM, STAR

from ..engine.entity import Enemy, GameObject, PhysicsObject, Platform, Star

# Intialize Useful Constants
PATH_TO_LEVELS: str = pathlib.Path(__file__).parent.absolute()

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
        static_objects.append(Platform(current_rect, GRASS, True))

    # Read Static Objects/Platforms
    for static_object in level_data["static_objects"]:
        current_rect: Rect = Rect(*static_object)
        image_url: str = PLATFORM

        if current_rect.y == 500:
            image_url = HAY
        static_objects.append(Platform(current_rect, image_url, True))

    # Read Physics Objects/Enemies
    for physics_object in level_data["physics_objects"]:
        x: int = physics_object[0]
        y: int = physics_object[1]
        x_velocity: int = physics_object[2]

        current_rect: Rect = Rect(x, y, *ENEMY_DIMENSIONS)

        e = Enemy(current_rect, ENEMY, x_velocity, 0)
        e.set_animation_frames(ENEMY_SPRITE)
        physics_objects.append(e)

    end_position: Tuple[int, int] = tuple(level_data["goal"])
    star: Star = Star(Rect(*end_position, *STAR_DIMENSIONS), STAR)

    return starting_position, static_objects, physics_objects, star
