class Object(object):

    def __init__(self, image):
        """
        """
        self.image_path = os.path.join("assets", image)
        self.image = pygame.image.load(self.image_path)

        self.image = pygame.transform.scale(self.image, (32, 32))

    def on_render(self, bf):
        """
        """
        bf.blit(self.image, (0, 0))


class Tree(Object):
    """
    """