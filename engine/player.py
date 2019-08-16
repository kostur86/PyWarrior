import os.path
import pygame.image
import pygame.transform
import pygame.time

from engine.engine import TILE_SIZE


class Player(object):
    def __init__(self):
        """
        """
        self.image_path = os.path.join("assets", "red_ball_sprite.png")
        self.image = pygame.image.load(self.image_path)

        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

        self.position = [0, 0]

        # movement
        self.speed = 5
        self._move_destination = self.position

    def set_position(self, x, y):
        self.position = [x, y]
        self._move_destination = self.position
        self._real_pos = [self.position[0] * TILE_SIZE,
                          self.position[1] * TILE_SIZE]

    def on_loop(self, dt):
        """
        """
        if self._move_destination != self.position:
            newPosition = [0, 0]
            for pos in (0, 1):
                newPosition[pos] = \
                    self.position[pos] * TILE_SIZE + \
                    (self._move_destination[pos] - self.position[pos]) * dt

            for pos in (0, 1):
                diff = self._real_pos[pos] - self.position[pos] * TILE_SIZE
                if abs(diff) < 5:
                    self._move_destination[pos] = self.position[pos]

            self._real_pos = newPosition

    def on_render(self, bf):
        """
        """
        bf.blit(
            self.image, self._real_pos)

    def move(self, x, y):
        """
        """
        self._move_destination = [x, y]

    def move_up(self, distance=1):
        self.move(self.position[0], self.position[1] - distance)

    def move_down(self, distance=1):
        self.move_up(-distance)

    def move_left(self, distance=1):
        self.move(self.position[0] - distance, self.position[1])

    def move_right(self, distance=1):
        self.move_left(-distance)
