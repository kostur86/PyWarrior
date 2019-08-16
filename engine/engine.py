import pygame
from pygame.locals import *

TILE_SIZE = 32

class Engine(object):
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400

        # Game objects
        self._objects = []
        self._player = None

    def quit(self):
        self._running = False
        pygame.quit()
        self._display_surf = None

    def add_player(self, obj):
        self._player = obj
        self.add_object(obj)

    def get_player(self):
        return self._player

    def add_object(self, obj):
        self._objects.append(obj)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        return True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.quit()

    def on_loop(self):
        dt = pygame.time.get_ticks()

        for obj in self._objects:
            obj.on_loop(dt)

    def on_render(self):
        if not self._display_surf:
            return

        self._display_surf.fill((0, 0, 0))

        for obj in self._objects:
            obj.on_render(self._display_surf)

        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if not self.on_init():
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def get_buffer(self):
        return self._display_surf
