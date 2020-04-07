"""
Exports all assets
"""
import os
from pathlib import Path
from typing import List

PATH: str = f"{Path(__file__).parent.absolute()}"

# Game Assets
GAME_PATH: str = f"{PATH}{os.sep}game{os.sep}"

GAME_OVER: str = f"{GAME_PATH}GameOver.jpg"
GRASS: str = f"{GAME_PATH}GRASS_TILE.png"
HAY: str = f"{GAME_PATH}hay_bale.png"
PLAYER: str = f"{GAME_PATH}horsey.png"
SKY: str = f"{GAME_PATH}sky.png"
STAR: str = f"{GAME_PATH}star.png"
PLATFORM: str = f"{GAME_PATH}wood_platform.png"
ENEMY: str = f"{GAME_PATH}wood_platform.png"
ENEMY_SPRITE: List[str] = [
    f"{GAME_PATH}greek_soldier_walk1.png",
    f"{GAME_PATH}greek_soldier_walk2.png",
    f"{GAME_PATH}greek_soldier_walk3.png",
]


# Menu Assets
MENU_PATH: str = f"{PATH}{os.sep}menu{os.sep}"
