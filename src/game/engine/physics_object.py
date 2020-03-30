from .game_object import GameObject


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
        x_vel: float = 0.0
        y_vel: float = 0.0

    def __init__(self, position: pygame.Rect, image_path: str, x_vel: float, y_vel: float):
        super().__init__(position, image_path)
        self.x_vel = x_vel
        self.y_vel = y_vel

    def update(self) -> None:
        """
        Update the position of this object based on its velocity values.
        """
        self.position.x += x_vel
        self.position.y += y_vel
