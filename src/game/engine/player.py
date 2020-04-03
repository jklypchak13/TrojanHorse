import pygame  # type: ignore
from .physics_object import PhysicsObject


class Player(PhysicsObject):
    """
    Player class is the physics object that represents the player.
    """

    def __init__(self, position: pygame.Rect, image_path: str, x_vel: float, y_vel: float):
        super().__init__(position, image_path, x_vel, y_vel)
        self.life = 1

    def kill(self):
        """
        Kill this player. Remove a life/health or end the game.
        """
        # TODO end the game/remove life
        # TODO remove self from all game_objects lists
        # TODOLATER death animation?
        self.life = 0
