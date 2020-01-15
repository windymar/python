import pygame
from pygame.sprite import Sprite
from rover import Rover
from rover_controller import RoverController


class RoverView(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self._screen = screen
        self._settings = settings
        self._rover_image = pygame.image.load('images/tankwithshadow.png')
        self._rover_image = pygame.transform.scale(self._rover_image, (self._settings.rover_width, self._settings.rover_height))
        self._rover_rect = self._rover_image.get_rect()
        self._rover_rect.x = 0
        self._rover_rect.y = self._settings.screen_height - self._rover_rect.height
        self._rover = Rover()
        self._rover_controller = RoverController(self._rover,
                                                 {'Width': (self._settings.screen_width / self._settings.step_factor) - (self._settings.rover_width / self._settings.step_factor) + 1,
                                                  'Height': (self._settings.screen_height / self._settings.step_factor) - (self._settings.rover_height / self._settings.step_factor) + 1},
                                                 self)

    def draw(self):
        self._screen.blit(self._rover_image, self._rover_rect)

    def move(self):
        self._rover_controller.execute_command('M')

    def turn_right(self):
        self._rover_controller.execute_command("R")

    def turn_left(self):
        self._rover_controller.execute_command('L')

    def get_position(self):
        return self._rover.get_position()

    def turned_left(self):
        self._rover_image = pygame.transform.rotate(self._rover_image, 90)

    def turned_right(self):
        self._rover_image = pygame.transform.rotate(self._rover_image, -90)

    def position_updated_event(self, position):
        self._rover_rect.x = position['X'] * self._settings.step_factor
        self._rover_rect.y = self._settings.screen_height - self._rover_rect.height - (position['Y'] * self._settings.step_factor)
