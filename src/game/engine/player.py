import pygame  # type: ignore

from .physics_object import PhysicsObject, Direction


class Player(PhysicsObject):
    """
    Player class is the physics object that represents the player.
    """

    def __init__(
        self, position: pygame.Rect, image_path: str, x_vel: float, y_vel: float,
    ):
        super().__init__(position, image_path, x_vel, y_vel)
        self.lives = 3
        # Make horsey go right
        self.image = pygame.transform.flip(self.image, True, False)
        self.direction = Direction.Right
        self.jumping: bool = False
        self.immunity: bool = False
        self.collision_time = 0

    def hit(self) -> None:
        """
        Hits this player. Remove a life/health or end the game.
        """
        # TODO death animation?
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
        if self.immunity and pygame.time.get_ticks() - self.collision_time > 2500:
            self.image.set_alpha(255)
            self.immunity = False
        super().update_x()

    def jump(self) -> None:
        """
        Moves player up by setting y_vel to -15.0
        """
        if not self.jumping:
            self.jumping = True
            self.y_vel = -15.0
