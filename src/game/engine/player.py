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
        self.horizontal_vel=50
        self.position = position
<<<<<<< HEAD
        self.image_path= pygame.transform.scale(pygame.image.load(f"{PATH_TO_DIR}{os.sep}assets{os.sep}game{os.sep}whiteSquare.png"),(position.width,position.height))
        self.controls = {pygame.K_RIGHT:"right",pygame.K_LEFT:"left",  pygame.K_SPACE:"jump"}
        # TODO: create Asset for Player
        # self.image = pygame.image.load(image_path)
=======
        self.image = pygame.transform.scale(
            pygame.image.load(image_path), (position.width, position.height),
        )
        self.controls = {pygame.K_RIGHT: self.right, pygame.K_SPACE: self.jump, pygame.K_LEFT: self.left}
>>>>>>> dd84a16d73aa8ed77d76d6b76d6c96efa8a3bcce

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
<<<<<<< HEAD
        x, y, width, height = self.position
        self.position = self.position.move(Player.vel*5,0)
        print(f"player position {self.position=}")
=======
        self.position = self.position.move(self.horizontal_vel, 0)
>>>>>>> dd84a16d73aa8ed77d76d6b76d6c96efa8a3bcce

    def left(self):
        """
        Moves the Player to the Right by a constant factor
        """
<<<<<<< HEAD
        x, y, width, height = self.position
        self.position = self.position.move(-Player.vel*5,0)
        print(f"player position {self.position=}")

=======
        self.position = self.position.move(-1*self.horizontal_vel, 0)
>>>>>>> dd84a16d73aa8ed77d76d6b76d6c96efa8a3bcce

    def draw(self, screen, offset):
        """
        Renders the Player as a Rectangle

        Parameters
        ----------

        screen: Any
             The screen to draw the player onto
        """
<<<<<<< HEAD
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
=======
        draw_position=self.position.move(offset[0],offset[1])
        screen.blit(self.image, draw_position)

    def kill(self):
        """
        Kill this player. Remove a life/health or end the game.
        """
        #TODO end the game/remove life
        #TODO remove self from all game_objects lists
        #TODOLATER death animation?
        pass
>>>>>>> dd84a16d73aa8ed77d76d6b76d6c96efa8a3bcce
