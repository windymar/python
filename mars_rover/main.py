import pygame
import sys
from settings import Settings
from rover_controller import RoverController
from rover import Rover
from bullet_view import BulletView
import logging


class MarsRoverGame:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, filename='syslog.log', filemode='w')
        pygame.display.init()
        pygame.display.set_caption("Mars Rover")
        self._settings = Settings()
        self._screen = pygame.display.set_mode((self._settings.screen_width, self._settings.screen_height))
        self._screen_rect = self._screen.get_rect()
        self._rover_image = pygame.image.load('images/rover.bmp')
        self._rover_rect = self._rover_image.get_rect()
        self._rover_rect.x = 0
        self._rover_rect.y = self._settings.screen_height - self._rover_rect.height
        self._rover = Rover()
        self._rover_controller = RoverController(self._rover,
                                                 {'Width': self._settings.screen_width / self._settings.step_factor,
                                                  'Height': self._settings.screen_height / self._settings.step_factor},
                                                 self)
        self._bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self._bullets.update()
            self._update_screen()

            for bullet in self._bullets.copy():
                if bullet.is_out_of_map:
                    self._bullets.remove(bullet)
                    logging.info(F'Bullet removed. Bullets alive: {len(self._bullets)}')

    def position_updated_event(self, position):
        self._rover_rect.x = position['X'] * self._settings.step_factor
        self._rover_rect.y = self._settings.screen_height - self._rover_rect.height - (position['Y'] * self._settings.step_factor)

    def turned_left(self):
        self._rover_image = pygame.transform.rotate(self._rover_image, 90)

    def turned_right(self):
        self._rover_image = pygame.transform.rotate(self._rover_image, -90)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self._rover_controller.execute_command("R")
                elif event.key == pygame.K_LEFT:
                    self._rover_controller.execute_command('L')
                elif event.key == pygame.K_UP:
                    self._rover_controller.execute_command('M')
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()

    def _update_screen(self):
        self._screen.fill(self._settings.background_color)
        self._screen.blit(self._rover_image, self._rover_rect)
        for bullet in self._bullets:
            bullet.draw()
        pygame.display.flip()

    def _fire_bullet(self):
        bullet = BulletView(self._screen, self._settings, self._rover.get_position())
        self._bullets.add(bullet)
        logging.info(F'New bullet fired. Bullets alive: {len(self._bullets)}')


if __name__ == '__main__':
    mars_rover_game = MarsRoverGame()
    mars_rover_game.run_game()
