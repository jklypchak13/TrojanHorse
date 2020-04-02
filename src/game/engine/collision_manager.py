import pygame  # type: ignore


class CollisionManager:

    def __init__(self, player, static_objects, dynamic_objects):
        self.player = player
        self.dynamic_objects = dynamic_objects
        self.static_objects = static_objects

    def check_all_collisions(self):
        # Check dynamic and player against static
        self.phys_collides_static()
        self.player_collides_static()
        self.player_collides_phys()

    def phys_collides_static(self):
        for s in self.static_objects:
            for d in self.dynamic_objects:
                if s in d:
                    s.handle_collision(d)

    def player_collides_static(self):
        for s in self.static_objects:
            if s in self.player:
                s.handle_collision(self.player)

    def player_collides_phs(self):
        # Check dyanmic objects against Player
        for d in self.dyanmic_objects:
            if d in self.player:
                d.handle_collision(player)
