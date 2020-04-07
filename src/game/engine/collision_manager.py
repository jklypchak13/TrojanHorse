import pygame  # type: ignore
from .game_state import GameState
from .platform import Axis


class CollisionManager:
    def check_all_collisions(self):
        # Check dynamic and player against PhysicsObjects
        self.player_collides_phys()

    def player_collides_goal(self) -> bool:
        """
        Player collides with the goal of this level

        Returns
        -------

        bool
          if they collided
        """
        return GameState.player in GameState.goal

    def phys_collides_static(self, axis: Axis):
        for s in GameState.static_objects:
            for p in GameState.physics_objects:
                if s in p:
                    s.handle_collision(p, axis)

    def player_collides_static(self, axis: Axis):
        for s in GameState.static_objects:
            if s in GameState.player:
                s.handle_collision(GameState.player, axis)

    def player_collides_phys(self):
        # Check dyanmic objects against Player
        for p in GameState.physics_objects:
            if p in GameState.player and not GameState.player.immunity:
                p.handle_player_collision(GameState.player)
