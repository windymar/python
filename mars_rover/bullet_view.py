import pygame
from pygame.sprite import Sprite
from bullet import Bullet
from bullet_controller import BulletController
import copy
import logging
from converters import upscale


class BulletView(Sprite):
    def __init__(self, game, settings, position):
        super().__init__()
        self._game = game
        self._settings = settings
        self._starting_bullet_position = copy.deepcopy(position)
        self._starting_bullet_position['X'] *= self._settings.scale_view_factor
        self._starting_bullet_position['Y'] *= self._settings.scale_view_factor
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

        if position['Facing'] == 'N' or position['Facing'] == 'S':
            self._x = self._starting_bullet_position['X'] + (self._settings.rover_width / 2)
            self._width = self._settings.bullet_thickness
            self._height = self._settings.bullet_length
        elif position['Facing'] == 'W' or position['Facing'] == 'E':
            self._y = self._settings.screen_height - self._starting_bullet_position['Y'] - (self._settings.rover_width / 2)
            self._width = self._settings.bullet_length
            self._height = self._settings.bullet_thickness

        self._rect = pygame.Rect(self._x, self._y, self._width, self._height)

    def update(self):
        self._bullet_controller.update()

    def position_updated_event(self, position):
        if position['Facing'] == 'N' or position['Facing'] == 'S':
            if position['Facing'] == 'N':
                self._y = self._settings.screen_height - position['Y'] - self._settings.rover_height - self._settings.bullet_length
            elif position['Facing'] == 'S':
                self._y = self._settings.screen_height - position['Y']
        elif position['Facing'] == 'E' or position['Facing'] == 'W':
            if position['Facing'] == 'E':
                self._x = position['X'] + self._settings.rover_height
            elif position['Facing'] == 'W':
                self._x = position['X'] - self._settings.bullet_length
        self._rect.x = self._x
        self._rect.y = self._y

    def draw(self):
        pygame.draw.rect(self._game._screen, self._settings.bullet_color, self._rect)

    def map_edge_reached_event(self):
        self.is_out_of_map = True
        logging.info('Bullet reached map edge')
