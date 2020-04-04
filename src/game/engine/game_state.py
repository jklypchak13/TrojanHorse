import pygame  # type: ignore
from .player import Player

class GameState:
    """
    GameState

    Store references to the current GameObjects.
    DrawManager, InputManager, CollisionManager, and other objects need these
    references.
    """

    #List of GameObjects that don't have physics. (i.e. they don't move)
    static_objects=[]

    #List of GameObjects that extend PhysicsObject and have physics
    physics_objects=[]

    #Reference to the player GameObject
    player: Player
