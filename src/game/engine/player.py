from typing import Tuple, Final

import pygame  # type: ignore
import os
import pathlib

class Player:
    jumps = False
    vel = 10
    """
    Player class allows for movement of player character and rendering

    Parameters
    ----------

    position: Tuple[int, int, int, int]
         starting (x, y, width, height) of player

    image_path: str
         path to image to use as player image
    """

    image: pygame.image

    def __init__(self, position, image_path: str):

        PATH_TO_DIR = pathlib.Path(__file__).parent.parent.parent.absolute()
        self.position = position
        self.image= pygame.transform.scale(pygame.image.load(f"{PATH_TO_DIR}{os.sep}assets{os.sep}game{os.sep}whiteSquare.png"),(position.width,position.height))
        self.controls = {pygame.K_RIGHT:"right",pygame.K_LEFT:"left",  pygame.K_SPACE:"jump"}
        # TODO: create Asset for Player
        # self.image = pygame.image.load(image_path)

    def is_collided_with(self, sprite):
        return self.position.colliderect(sprite.position)

    def jump(self):
        """
        Makes the player jump into the air
        """
        self.jumps = True

    def right(self):
        """
        Moves the Player to the Right by a constant factor
        """
        x, y, width, height = self.position
        self.position = self.position.move(Player.vel*5,0)
        print(f"player position {self.position=}")

    def left(self):
        """
        Moves the Player to the Right by a constant factor
        """
        x, y, width, height = self.position
        self.position = self.position.move(-Player.vel*5,0)
        print(f"player position {self.position=}")


    def draw(self, screen):
        """
        Renders the Player as a Rectangle

        TODO: render image

        Parameters
        ----------

        screen: Any
             The screen to draw the player onto
        """
        screen.blit(self.image,self.position)
    
    def updateJump(self):
        x, y, width, height = self.position
        if self.jumps:
            if self.vel >= -10:
                dy =  -(self.vel * abs(self.vel))/2
                self.position = self.position.move(0, dy)
                self.vel -= 1
                self.controls[pygame.K_SPACE]
            else: 
                self.vel = 10
                self.jumps = False
            print(f"player position {self.position=}")

