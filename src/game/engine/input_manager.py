import pygame  # type: ignore
from .game_state import GameState


class InputManager:
    def handle_input(self):
        """
        Handle user keyboard input.
        """
        # reset horizontal velocity so that releasing a button stops walking
        GameState.player.x_vel = 0

        # player controls
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_RIGHT]:
            GameState.player.right()
        if pressedKeys[pygame.K_LEFT]:
            GameState.player.left()
        if pressedKeys[pygame.K_SPACE]:
            GameState.player.jump()
