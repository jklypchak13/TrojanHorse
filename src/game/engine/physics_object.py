from enum import Enum, auto

import pygame

from .game_object import GameObject


class Direction(Enum):
    """
    Direction the image is moving
    """

    Left = auto()
    Right = auto()


class PhysicsObject(GameObject):

    """
    PhysicsObject

    Parameters
    ----------

    x_vel: float
    initial x velocity

    y_vel: float
        initial y velocity
    """

    def __init__(
        self, position: pygame.Rect, image_path: str, x_vel: float, y_vel: float
    ):
        super().__init__(position, image_path)
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.direction = Direction.Left
        self.gravity = 0.9

    def update_x(self) -> None:
        """
        Update the position of this object based on its velocity x values.
        """
        self.position.x += self.x_vel
        if self.x_vel < 0 and self.direction is not Direction.Left:
            self.image = pygame.transform.flip(self.image, True, False)
            self.direction = Direction.Left
        elif self.x_vel > 0 and self.direction is not Direction.Right:
            self.image = pygame.transform.flip(self.image, True, False)
            self.direction = Direction.Right

    def update_y(self) -> None:
        """
        Update the position of this object based on its velocity y values.
        """
        self.y_vel += self.gravity
        self.position.y += self.y_vel

    def handle_collision(self, otherPhysicsObject):
        """
        Stub to be implemented in child classes
        """
        pass
