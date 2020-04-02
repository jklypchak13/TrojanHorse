import pygame  # type: ignore


class DrawManager:
    screen_offset = [0,0]

    def __init__(self, screen, player, static_objects, dynamic_objects):
        self.player = player
        self.static_objects = static_objects
        self.dynamic_objects = dynamic_objects
        self.screen=screen

    def adjust_screen(self):
        w, h = pygame.display.get_surface().get_size()
        if self.player.position.x+self.screen_offset[0]<20:
            self.screen_offset[0]=20-self.player.position.x
        if self.player.position.right+self.screen_offset[0]>w-20:
            self.screen_offset[0]=w-20-self.player.position.right


    def draw_all(self):
        for obj in self.static_objects:
            obj.draw(self.screen, self.screen_offset)
        for obj in self.dynamic_objects:
            obj.draw(self.screen, self.screen_offset)
        self.player.draw(self.screen, self.screen_offset)
        pygame.display.update()
