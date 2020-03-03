import pygame  # type: ignore
import os
import pathlib

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

    position: pygame.Rect

    image: pygame.image

    def __init__(self, position: pygame.Rect, image_path: str):

        self.position = position
        self.image = pygame.transform.scale(
            pygame.image.load(
                f"{PATH_TO_DIR}{os.sep}assets{os.sep}game{os.sep}redSquare.png"
            ),
            (position.width, position.height),
        )

    def draw(self, screen):
        """
        Renders the Player as a Rectangle

        Parameters
        ----------

        screen: Any
             The screen to draw the player onto
        """
        screen.blit(self.image, self.position)
