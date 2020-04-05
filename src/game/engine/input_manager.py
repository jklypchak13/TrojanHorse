import pygame  # type: ignore
from .game_state import GameState

class InputManager:


    def handle_input(self):
        """
        Handle user keyboard input.
        """
        #reset horizontal velocity so that releasing a button stops walking
        GameState.player.x_vel = 0

        #player controls
        pressedKeys = pygame.key.get_pressed()
        if (pressedKeys[pygame.K_RIGHT]):
            self.right()
        if (pressedKeys[pygame.K_LEFT]):
            self.left()
        if (self.newKeyDown(pygame.K_SPACE, pressedKeys)):
            self.jump()

        self.previous_pressed_keys = pressedKeys

    def right(self):
        GameState.player.x_vel=1.0
    def left(self):
        GameState.player.x_vel=-1.0
    def jump(self):
        GameState.player.y_vel=-10.0

    def newKeyDown(self, key, currentPressedKeys) -> bool:
        return (currentPressedKeys[key]) and (not self.previous_pressed_keys[key])
