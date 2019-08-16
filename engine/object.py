import os.path
import pygame.image
import pygame.transform

from engine.engine import TILE_SIZE


class Object(object):

    def __init__(self, image):
        """
        """
        self.image_path = os.path.join("assets", image)
        self.image = pygame.image.load(self.image_path)

        self.image = pygame.transform.scale(self.image, (32, 32))

        self.position = (0, 0)

    def set_position(self, x, y):
        self.position = (x, y)

    def on_render(self, bf):
        """
        """
        bf.blit(
            self.image,
            (self.position[0] * TILE_SIZE, self.position[1] * TILE_SIZE)
        )

    def on_loop(self, dt):
        """
        """

class Tree(Object):
    """
    """
