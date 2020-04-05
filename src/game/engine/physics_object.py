from .game_object import GameObject
import pygame


class PhysicsObject(GameObject):

    """
    PhysicsObject

    Parameters
    ----------

    x_vel: float
    initial x velocity

    y_vel: float
        initial y velocity
    """

    def __init__(
        self, position: pygame.Rect, image_path: str, x_vel: float, y_vel: float
    ):
        super().__init__(position, image_path)
        self.x_vel = x_vel
        self.y_vel = y_vel
        image = pygame.image.load(image_path)
        self.image_right: pygame.Surface = self.image
        self.image_left: pygame.Surface = pygame.transform.flip(self.image, True, False)
        self.gravity = 0.9

    def update_x(self) -> None:
        """
        Update the position of this object based on its velocity x values.
        """
        if self.x_vel < 0:
            self.image = self.image_left
        elif self.x_vel > 0:
            self.image = self.image_right
        self.position.x += self.x_vel

    def update_y(self) -> None:
        """
        Update the position of this object based on its velocity y values.
        """
        self.y_vel += self.gravity
        self.position.y += self.y_vel

    def handle_collision(self, otherPhysicsObject):
        """
        Stub to be implemented in child classes
        """
        pass
