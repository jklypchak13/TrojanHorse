import pygame  # type: ignore

from .game_state import GameState
from game.style import color as cval  # type: ignore
from game.style import text


class DrawManager:
    screen_offset = [0, 0]

    def __init__(self, screen, BACKGROUND_IMAGE_PATH):
        self.screen = screen
        self.background = pygame.transform.scale(
            pygame.image.load(BACKGROUND_IMAGE_PATH).convert_alpha(),
            (screen.get_width(), screen.get_height()),
        )

    def adjust_screen(self):
        rbuffer=300
        lbuffer=100
        w, h = pygame.display.get_surface().get_size()
        if GameState.player.position.x + self.screen_offset[0] < lbuffer:
            self.screen_offset[0] = lbuffer - GameState.player.position.x
        if GameState.player.position.right + self.screen_offset[0] > w - rbuffer:
            self.screen_offset[0] = w - rbuffer - GameState.player.position.right

    @staticmethod
    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def draw_all(self):
        self.screen.blit(self.background, [0, 0])
        for obj in GameState.static_objects:
            obj.draw(self.screen, self.screen_offset)
        for obj in GameState.physics_objects:
            obj.draw(self.screen, self.screen_offset)
        GameState.player.draw(self.screen, self.screen_offset)
        self.draw_text(
            f"Lives: {GameState.player.lives}",
            text.default_font,
            cval.black,
            self.screen,
            745,
            5,
        )
        pygame.display.update()
