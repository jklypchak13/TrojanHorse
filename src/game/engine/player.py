from typing import Tuple, Final

import pygame  # type: ignore


class Player:
    """
    Player class allows for movement of player character and rendering

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

        # TODO: create Asset for Plater
        # self.image = pygame.image.load(image_path)

    def jump(self):
        """
        Makes the player jump into the air

        TODO: gravity and physics
        """
        x, y, width, height = self.position
        self.position = (x, y - 10, width, height)
        print(f"player position {self.position=}")

    def right(self):
        """
        Moves the Player to the Right by a constant factor
        """
        x, y, width, height = self.position
        self.position = (x + 10, y, width, height)
        print(f"player position {self.position=}")

    def draw(self, screen):
        """
        Renders the Player as a Rectangle

        TODO: render image

        Parameters
        ----------

        screen: Any
             The screen to draw the player onto
        """
        WHITE: Final[Tuple[int, int, int]] = (255, 255, 255)
        pygame.draw.rect(screen, WHITE, self.position, 0)
