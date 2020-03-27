import pygame  # type: ignore
import os
import pathlib
from pipenv.vendor.pexpect import screen

PATH_TO_DIR = pathlib.Path(__file__).parent.parent.parent.absolute()


class Player:
    jumps = False
    vel = 10
    """
    Player class allows for movement of player character and rendering

    Parameters
    ----------

    position: pygame.Rect
         Pygame representation of a Rectangle

    image_path: str
         path to image to use as player image
    """

    position: pygame.Rect

    image: pygame.image

    def __init__(self, position, image_path: str):

        self.position = position
<<<<<<< HEAD
        self.image= pygame.transform.scale(pygame.image.load(f"{PATH_TO_DIR}{os.sep}assets{os.sep}game{os.sep}whiteSquare.png"),(position.width,position.height))
        self.controls = {pygame.K_RIGHT:"right",pygame.K_LEFT:"left",  pygame.K_SPACE:"jump"}
        # TODO: create Asset for Player
        # self.image = pygame.image.load(image_path)
=======
        self.image = pygame.transform.scale(
            pygame.image.load(image_path), (position.width, position.height),
        )
        self.controls = {pygame.K_RIGHT: self.right, pygame.K_SPACE: self.jump}
>>>>>>> f5a9a6c55bf2d61a8276c55f9ded615b344a9e43

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


    ##screen.blit(self.image, self.position)
