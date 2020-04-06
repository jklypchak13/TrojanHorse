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

import time


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
        self.__animated = False
        if repeat_texture:
            self.image = pygame.Surface((self.position.width, self.position.height))
            self.image.fill((255, 0, 0))
            texture = pygame.image.load(image_path).convert()
            for x in range(0, self.image.get_width(), texture.get_width()):
                for y in range(0, self.image.get_height(), texture.get_height()):
                    self.image.blit(texture, (x, y))
        else:
            self.image = pygame.transform.scale(
                pygame.image.load(image_path).convert(),
                (self.position.width, self.position.height),
            )
        self.image.set_colorkey((0, 0, 0))

    def draw(self, screen: pygame.Surface, screen_offset: Tuple[int, int]) -> None:
        """
        Renders the GameObject to the screen. Animates if animation is active
        for this GameObject.

        Parameters
        ----------

        screen: pygame.Surface
              Screen to draw to

        screen_offset
              Offset of the screen
        """
        if self.__animated:
            if time.time() - self.prev_update_time > 1.0 / self.fps:
                self.prev_update_time = time.time()
                self.current_frame_index = (self.current_frame_index + 1) % len(
                    self.frames
                )
                self.image = self.frames[self.current_frame_index]

        draw_position = self.position.move(screen_offset[0], screen_offset[1])
        screen.blit(self.image, draw_position)

    def set_animation_frames(self, frame_paths):
        """
        Sets the frames for the animation, and initializes necessary variables.

        Parameters
        ----------

        frame_paths: str[]
            list of file paths to the images for the frames (in order of animation)
        """
        self.__animated = True
        self.frames = []
        self.fps = 7
        self.prev_update_time = time.time()
        self.current_frame_index = 0
        for image_path in frame_paths:
            frame = pygame.transform.scale(
                pygame.image.load(image_path).convert(),
                (self.position.width, self.position.height),
            )
            frame.set_colorkey((0, 0, 0))
            self.frames.append(frame)

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
