import pygame  # type: ignore
from .physics_object import PhysicsObject


class Player(PhysicsObject):
    """
    Player class is the physics object that represents the player.
    """

    def __init__(
        self, position: pygame.Rect, image_path: str, x_vel: float, y_vel: float
    ):
        super().__init__(position, image_path, x_vel, y_vel)
        self.life = 1
        self.jumping: bool = False

    def kill(self):
        """
        Kill this player. Remove a life/health or end the game.
        """
        # TODO end the game/remove life
        # TODO remove self from all game_objects lists
        # TODOLATER death animation?
        self.life = 0

    def left(self):
        """
        Moves player left by setting x_vel to -4.0
        """
        self.x_vel = -4.0

    def right(self):
        """
        Moves player right by setting x_vel to 4.0
        """
        self.x_vel = 4.0

    def jump(self):
        """
        Moves player up by setting y_vel to -15.0
        """
        if not self.jumping:
            self.jumping = True
            self.y_vel = -15.0
