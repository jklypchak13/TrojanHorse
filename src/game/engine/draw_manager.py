import pygame  # type: ignore

from assets import GAME_OVER, SKY
from game.style import color as cval  # type: ignore
from game.style import text

from .game_state import GameState

GAME_OVER_FONT = pygame.font.SysFont("Arial", 70)


class DrawManager:
    screen_offset = [0, 0]

    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.transform.scale(
            pygame.image.load(SKY).convert_alpha(),
            (screen.get_width(), screen.get_height()),
        )

    def adjust_screen(self):
        """
        Moves the screen around the Player
        """
        rbuffer = 300
        lbuffer = 100
        w, h = pygame.display.get_surface().get_size()
        if GameState.player.position.x + self.screen_offset[0] < lbuffer:
            self.screen_offset[0] = lbuffer - GameState.player.position.x
        if GameState.player.position.right + self.screen_offset[0] > w - rbuffer:
            self.screen_offset[0] = w - rbuffer - GameState.player.position.right

    @staticmethod
    def draw_text(text: str, font, color, surface, x, y):
        """
        Draws Text to screen

        Parameters
        ----------

        text: str
        """
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def draw_game_over(self):
        """
        Renders GameOver Screen
        """
        cbackground = pygame.image.load(GAME_OVER)
        self.screen.blit(cbackground, (0, 0))  # Overlay background image
        self.draw_text("Game Over", GAME_OVER_FONT, cval.white, self.screen, 250, 250)

    def draw_all(self):
        """
        Draws all entities in GameState
        """
        self.screen.blit(self.background, [0, 0])
        for obj in GameState.static_objects:
            obj.draw(self.screen, self.screen_offset)
        for obj in GameState.physics_objects:
            obj.draw(self.screen, self.screen_offset)
        GameState.goal.draw(self.screen, self.screen_offset)
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
