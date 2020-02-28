from typing import Tuple, Final

import pygame  # type: ignore
import os
import pathlib


class Obstacle:
    """
    Obstacle class

    Parameters
    ----------

    position: Tuple[int, int, int, int]
         starting (x, y, width, height) of player

    image_path: str
         path to image to use as player image
    """

    image: pygame.image

    def __init__(self, position, image_path: str):

        PATH_TO_DIR = pathlib.Path(__file__).parent.parent.parent.absolute()
        self.position = position
        self.image= pygame.transform.scale(pygame.image.load(f"{PATH_TO_DIR}{os.sep}assets{os.sep}game{os.sep}redSquare.png"),(position.width,position.height))
        # TODO: create Asset for Player
        # self.image = pygame.image.load(image_path)


    def draw(self, screen):
        """
        Renders the Player as a Rectangle

        TODO: render image

        Parameters
        ----------

        screen: Any
             The screen to draw the player onto
        """
        screen.blit(self.image,self.position)
