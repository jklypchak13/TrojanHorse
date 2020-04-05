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
            self.right()
        if pressedKeys[pygame.K_LEFT]:
            self.left()
        if pressedKeys[pygame.K_SPACE]:
            self.jump()
        # for event in pygame.event.get():
        #   if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
        #       self.jump()

    def right(self):
        GameState.player.x_vel = 1.0

    def left(self):
        GameState.player.x_vel = -1.0

    def jump(self):
        GameState.player.y_vel = -15.0
