import pygame  # type: ignore
from .game_state import GameState


class CollisionManager:

    def check_all_collisions(self):
        # Check dynamic and player against static
        self.phys_collides_static()
        self.player_collides_static()
        self.player_collides_phys()

    def phys_collides_static(self):
        for s in GameState.static_objects:
            for p in GameState.physics_objects:
                if s in p:
                    s.handle_collision(p)

    def player_collides_static(self):
        for s in GameState.static_objects:
            if s in GameState.player:
                s.handle_collision(GameState.player)

    def player_collides_phys(self):
        # Check dyanmic objects against Player
        for p in GameState.physics_objects:
                p.handle_collision(GameState.player)
