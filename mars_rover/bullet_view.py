import pygame
from pygame.sprite import Sprite
from bullet import Bullet
from bullet_controller import BulletController
import copy
import logging


class BulletView(Sprite):
    def __init__(self, game, settings, rover_position):
        super().__init__()
        self._game = game
        self._settings = settings
        self._starting_bullet_position = copy.deepcopy(rover_position)
        self._starting_bullet_position['X'] *= 50
        self._starting_bullet_position['Y'] *= 50
        self._bullet = Bullet(self._starting_bullet_position)
        self._bullet_controller = BulletController(self._bullet,
                                             {'Width': self._settings.screen_width,
                                              'Height': self._settings.screen_height},
                                             self)
        self._x = 0
        self._y = 0
        self._width = 0
        self._height = 0

        self.is_out_of_map = False

        if rover_position['Facing'] == 'N' or rover_position['Facing'] == 'S':
            self._x = self._starting_bullet_position['X'] + (50 / 2)
            self._width = 3
            self._height = 15
        elif rover_position['Facing'] == 'W' or rover_position['Facing'] == 'E':
            self._y = self._settings.screen_height - self._starting_bullet_position['Y'] - (50 / 2)
            self._width = 15
            self._height = 3

        self._rect = pygame.Rect(self._x, self._y, self._width, self._height)

    def update(self):
        self._bullet_controller.update()

    def position_updated_event(self, position):
        if position['Facing'] == 'N' or position['Facing'] == 'S':
            if position['Facing'] == 'N':
                self._y = self._settings.screen_height - position['Y'] - 50
            elif position['Facing'] == 'S':
                self._y = self._settings.screen_height - position['Y']
        elif position['Facing'] == 'E' or position['Facing'] == 'W':
            if position['Facing'] == 'E':
                self._x = position['X'] + 50
            elif position['Facing'] == 'W':
                self._x = position['X']
        self._rect.x = self._x
        self._rect.y = self._y
        pygame.draw.rect(self._game._screen, (60, 60, 60), self._rect)

    def map_edge_reached_event(self):
        self.is_out_of_map = True
        logging.info('Bullet reached map edge')
