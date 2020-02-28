from typing import Tuple, Final

import pygame  # type: ignore
import os


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

    # position: x, y, width, height
    position: Tuple[int, int, int, int]
    image: pygame.image

    def __init__(self, position: Tuple[int, int, int, int], image_path: str):
        self.position = position
        self.image= pygame.image.load(os.path.join('assets\game','redSquare.png'))
        self.rect=self.image.get_rect()
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
