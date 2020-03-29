import pygame  # type: ignore
import os
import pathlib

PATH_TO_DIR = pathlib.Path(__file__).parent.parent.parent.absolute()


class Player:
    """
    Player class allows for movement of player character and rendering

    Parameters
    ----------

    position: pygame.Rect
         Pygame representation of a Rectangle

    image_path: str
         path to image to use as player image
    """

    position: pygame.Rect

    image: pygame.image

    def __init__(self, position, image_path: str):
        self.horizontal_vel=50
        self.position = position
        self.image = pygame.transform.scale(
            pygame.image.load(image_path), (position.width, position.height),
        )
        self.controls = {pygame.K_RIGHT: self.right, pygame.K_SPACE: self.jump, pygame.K_LEFT: self.left}

    def is_collided_with(self, sprite):
        return self.position.colliderect(sprite.position)

    def jump(self):
        """
        Makes the player jump into the air

        TODO: gravity and physics
        """
        self.position = self.position.move(0, -10)

    def right(self):
        """
        Moves the Player to the Right by a constant factor
        """
        self.position = self.position.move(self.horizontal_vel, 0)

    def left(self):
        """
        Moves the Player to the Right by a constant factor
        """
        self.position = self.position.move(-1*self.horizontal_vel, 0)

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
