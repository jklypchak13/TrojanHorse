import pygame  # type: ignore
import os
import pathlib
from .physics_object import PhysicsObject
from .player import Player

PATH_TO_DIR = pathlib.Path(__file__).parent.parent.parent.absolute()


class Obstacle:
    """
    Obstacle class

    Parameters
    ----------

    position: pygame.Rect
         Pygame representation of a Rectangle

    image_path: str
         path to image to use as player image
    """

    def __init__(self, position: pygame.Rect, image_path: str):

        self.position = position
        self.image = pygame.transform.scale(
            pygame.image.load(
                f"{PATH_TO_DIR}{os.sep}assets{os.sep}game{os.sep}redSquare.png"
            ),
            (position.width, position.height),
        )

    def draw(self, screen, offset):
        """
        Renders the Player as a Rectangle

        Parameters
        ----------

        screen: Any
             The screen to draw the player onto
        """
        draw_position=self.position.move(offset[0],offset[1])
        screen.blit(self.image, draw_position)

    def handle_collision(self, player:Player):
        """
        Does nothing.
        """
        pass

    def handle_collision(self, physics_object:PhysicsObject):
        #TODO collide with phys object
        pass
