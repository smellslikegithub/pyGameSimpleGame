import pygame


class Asset:

    def __init__(self):
        self._background = pygame.image.load('playerPackage/images/Background/treeBg.png')
        self._brick = pygame.image.load('AssetCollection/Images/Bricks/brick.png')

    @property
    def background(self):
        return self._background
