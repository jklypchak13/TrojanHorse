import pygame  # type: ignore
from .physics_object import PhysicsObject


class Player(PhysicsObject):
    """
    Player class is the physics object that represents the player.
    """

    def kill(self):
        """
        Kill this player. Remove a life/health or end the game.
        """
        # TODO end the game/remove life
        # TODO remove self from all game_objects lists
        # TODOLATER death animation?
        pass
