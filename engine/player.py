import os.path
import pygame.image
import pygame.transform


class Player(object):
    def __init__(self):
        """
        """
        self.image_path = os.path.join("assets", "red_ball_sprite.png")
        self.image = pygame.image.load(self.image_path)

        self.image = pygame.transform.scale(self.image, (32, 32))

    def on_render(self, bf):
        """
        """
        bf.blit(self.image, (0, 0))
