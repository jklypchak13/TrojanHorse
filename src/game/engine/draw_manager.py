import pygame  # type: ignore


class DrawManager:
    screen_offset = [0,0]

    def __init__(self, screen, player, game_objects):
        self.player = player
        self.game_objects = game_objects
        self.screen=screen

    def adjust_screen(self):
        w, h = pygame.display.get_surface().get_size()
        if self.player.position.x+self.screen_offset[0]<20:
            self.screen_offset[0]=20-self.player.position.x
        if self.player.position.right+self.screen_offset[0]>w-20:
            self.screen_offset[0]=w-20-self.player.position.right


    def draw_all(self):
        for o in self.game_objects:
            o.draw(self.screen, self.screen_offset)
        self.player.draw(self.screen, self.screen_offset)
        pygame.display.update()
