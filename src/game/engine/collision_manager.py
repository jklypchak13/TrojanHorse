import pygame  # type: ignore


class CollisionManager:

    def __init__(self, player, static_objects, dynamic_objects):
        self.player = player
        self.dynamic_objects = dyanmic_objects
        self.static_objects = static_objects

    def check_all_collisions(self):
        #Check dynamic and player against static
        for s in self.static_objects:
            for d in self.dyanmic_objects:
                if s.contains(d):
                    s.handle_collision(d)
            if s.contains(self.player):
                s.handle_collision(self.player)

        #Check dyanmic objects against Player
        for d in self.dyanmic_objects:
            if d.contains(self.player):
                d.handle_collision(player)


    def draw_all(self):
        for o in self.game_objects:
            o.draw(self.screen, self.screen_offset)
        self.player.draw(self.screen, self.screen_offset)
        pygame.display.update()
