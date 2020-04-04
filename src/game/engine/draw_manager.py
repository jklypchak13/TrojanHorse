import pygame  # type: ignore
from .game_state import GameState


class DrawManager:
    screen_offset = [0,0]

    def __init__(self, screen):
        self.screen=screen

    def adjust_screen(self):
        w, h = pygame.display.get_surface().get_size()
        if GameState.player.position.x+self.screen_offset[0]<20:
            self.screen_offset[0]=20-GameState.player.position.x
        if GameState.player.position.right+self.screen_offset[0]>w-20:
            self.screen_offset[0]=w-20-GameState.player.position.right


    def draw_all(self):
        for obj in GameState.static_objects:
            obj.draw(self.screen, self.screen_offset)
        for obj in GameState.physics_objects:
            obj.draw(self.screen, self.screen_offset)
        GameState.player.draw(self.screen, self.screen_offset)
        pygame.display.update()
