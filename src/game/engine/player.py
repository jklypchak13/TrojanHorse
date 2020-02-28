from typing import Tuple, Final

import pygame  # type: ignore
import os


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

    image: pygame.image

    def __init__(self, position, image_path: str):
        self.position = position
        self.image= pygame.transform.scale(pygame.image.load(os.path.join('assets\game','whiteSquare.png')),(position.width,position.height))
        self.controls = {pygame.K_RIGHT:"right", pygame.K_SPACE:"jump"}
        # TODO: create Asset for Player
        # self.image = pygame.image.load(image_path)

    def is_collided_with(self, sprite):
        return self.position.colliderect(sprite.position)

    def jump(self):
        """
        Makes the player jump into the air

        TODO: gravity and physics
        """
        x, y, width, height = self.position
        self.position = self.position.move(0,-10)
        print(f"player position {self.position=}")

    def right(self):
        """
        Moves the Player to the Right by a constant factor
        """
        x, y, width, height = self.position
        self.position = self.position.move(10,0)
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
        screen.blit(self.image,self.position)
