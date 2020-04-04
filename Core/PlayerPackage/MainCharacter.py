from Core.PlayerPackage.player import Player
import pygame
import os


class MainCharacter(Player):
    _image_library = ['playerPackage/images/MainCharacterWalk/']

    def __init__(self):

        super().__init__(0, 453, 33, 47) #calling the parent classes constructor
        self._walk_animation_left = [
            pygame.image.load(self._image_library[0] + 'w1.png'),
            pygame.image.load(self._image_library[0] + 'w2.png'),
            pygame.image.load(self._image_library[0] + 'w3.png'),
            pygame.image.load(self._image_library[0] + 'w4.png'),
            pygame.image.load(self._image_library[0] + 'w5.png'),
            pygame.image.load(self._image_library[0] + 'w6.png'),
            pygame.image.load(self._image_library[0] + 'w7.png'),
            pygame.image.load(self._image_library[0] + 'w8.png'),
            pygame.image.load(self._image_library[0] + 'w9.png')
        ]
        self._wal_animation_right - [
            
        ]
        self.__current_stage = 0

    def set__current_stage(self, current_stage):
        self.__current_stage = current_stage

    def get__current_stage(self):
        return self.__current_stage



