from Core.PlayerPackage.player import Player
import pygame
import os


class MainCharacter(Player):
    _image_library = ['playerPackage/images/MainCharacterWalk/',
                      'playerPackage/images/MainCharacterWalk/walkLeft/',
                      'playerPackage/images/MainCharacterWalk/standing/'
                      ]

    def __init__(self):

        super().__init__(0, 453, 33, 47) #calling the parent classes constructor
        self._walk_animation_right = [
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
        self._walk_animation_left = [
            pygame.image.load(self._image_library[1] + 'walkLeft1.png'),
            pygame.image.load(self._image_library[1] + 'walkLeft2.png'),
            pygame.image.load(self._image_library[1] + 'walkLeft3.png'),
            pygame.image.load(self._image_library[1] + 'walkLeft4.png'),
            pygame.image.load(self._image_library[1] + 'walkLeft5.png'),
            pygame.image.load(self._image_library[1] + 'walkLeft6.png'),
            pygame.image.load(self._image_library[1] + 'walkLeft7.png'),
            pygame.image.load(self._image_library[1] + 'walkLeft8.png'),
            pygame.image.load(self._image_library[1] + 'walkLeft9.png')
        ]

        self._standing_animation = pygame.image.load(self._image_library[2] + 'standing.png')
        self.__current_stage = 0

    def set__current_stage(self, current_stage):
        self.__current_stage = current_stage

    def get__current_stage(self):
        return self.__current_stage

    def get__walk_animation_left(self):
        return self._walk_animation_left

    def get__walk_animation_right(self):
        return self._walk_animation_right

    def get__standing_animation(self):
        return self._standing_animation

