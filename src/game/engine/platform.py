from typing import Tuple
from enum import Enum, auto

from .game_object import GameObject
from .physics_object import PhysicsObject
from .player import Player


class Axis(Enum):
    """
    Axis of collision
    """

    XAxis = auto()
    YAxis = auto()


class Platform(GameObject):
    """
    Platform

    Parameters
    ----------

    position: pygame.Rect
          Pygame representation of (x, y, width, height)

    image_path: str
          Path to image
    """

    def handle_collision(self, obj: PhysicsObject, axis: Axis) -> None:
        """
        Handle collision based on Axis

        Parameters
        ----------

        obj: PhysicsObject
          Object that collided with platform

        axis: Axis
          Axis of collision (either Axis.XAxis, Axis.YAxis)
        """
        if axis is Axis.XAxis:
            if obj.position.right - obj.x_vel > self.position.right:
                obj.position.left = self.position.right
            else:
                obj.position.right = self.position.left
            obj.x_vel = 0
        else:
            if obj.position.top - obj.y_vel < self.position.top:
                obj.position.bottom = self.position.top
                # Ground the player, to prevent infinite jumping
                if isinstance(obj, Player):
                    obj.jumping = False
            else:
                obj.position.top = self.position.bottom
            obj.y_vel = 0
