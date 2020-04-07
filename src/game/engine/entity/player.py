from typing import Tuple

import pygame  # type: ignore

from .physics_object import Direction, PhysicsObject


class Player(PhysicsObject):
    """
    Player class is the physics object that represents the player.
    """

    def __init__(
        self, position: pygame.Rect, image_path: str, x_vel: float, y_vel: float,
    ):
        super().__init__(position, image_path, x_vel, y_vel)
        self.lives: int = 3
        self.start_position: Tuple[int, int] = (self.position.x, self.position.y)
        # Make horsey go right
        self.image: pygame.Surface = pygame.transform.flip(self.image, True, False)
        self.direction: Direction = Direction.Right
        self.jumping: bool = False
        self.immunity: bool = False
        self.collision_time = 0

    def hit(self) -> None:
        """
        Hits this player. Remove a life/health or end the game.
        """
        self.immunity = True
        self.collision_time = pygame.time.get_ticks()
        self.image.set_alpha(127.5)
        self.lives -= 1

    def left(self) -> None:
        """
        Moves player left by setting x_vel to -4.0
        """
        self.x_vel = -4.0

    def right(self) -> None:
        """
        Moves player right by setting x_vel to 4.0
        """
        self.x_vel = 4.0

    def update_x(self) -> None:
        """
        Updates X Movement

        After being hit immune for 3 seconds and then immunity wears off
        """
        if self.immunity and pygame.time.get_ticks() - self.collision_time > 1500:
            self.image.set_alpha(255)
            self.immunity = False
        super().update_x()

    def update_y(self) -> None:
        """
        Update Vertical position

        Handles player falling off the map
        """
        width, height = pygame.display.get_surface().get_size()
        if self.position.y > height:
            self.position.x, self.position.y = self.start_position
            self.hit()
        super().update_y()

    def alive(self) -> bool:
        """
        Check to see if Player is alive

        Returns
        -------

        bool
          self.lives > 0
        """
        return self.lives > 0

    def jump(self) -> None:
        """
        Moves player up by setting y_vel to -15.0
        """
        if not self.jumping:
            self.jumping = True
            self.y_vel = -15.0
