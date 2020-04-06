"""
Base Game Object

Goals
-----

Detecting Collision

Rendering

Non-Goals
---------

Handle movement
      GameObjects immediate subclasses are static objects, reference PhyiscsObject
      for moving objects
"""
from __future__ import annotations

from typing import Tuple

import pygame  # type: ignore


class GameObject:
    """
    GameObject

    Parameters
    ----------

    position: pygame.Rect
          Pygame representation of (x, y, width, height)

    image_path: str
          Path to image
    """

    def __init__(self, position: pygame.Rect, image_path: str, repeat_texture=False):
        self.position = position
        if repeat_texture:
            self.image = pygame.Surface((self.position.width, self.position.height))
            self.image.fill((255,0,0))
            texture= pygame.image.load(image_path)
            for x in range(0, self.image.get_width(), texture.get_width()):
                print("Current it "+str(x))
                for y in range(0, self.image.get_height(), texture.get_height()):
                    self.image.blit(texture, (x,y))
        else:
            self.image = pygame.transform.scale(
            pygame.image.load(image_path), (self.position.width, self.position.height)
        )

    def draw(self, screen: pygame.Surface, screen_offset: Tuple[int, int]) -> None:
        """
        Renders the GameObject to the screen

        Parameters
        ----------

        screen: pygame.Surface
              Screen to draw to

        screen_offset
              Offset of the screen
        """
        draw_position=self.position.move(screen_offset[0],screen_offset[1])
        screen.blit(self.image, draw_position)

    def __contains__(self, game_object: GameObject) -> bool:
        """
        Detects a collision between self and another GameObject

        Parameters
        ----------

        game_object: GameObject
              Detects if they've collided

        Returns
        -------

        bool
              True if they have, false otherwise
        """
        return self.position.colliderect(game_object.position)
