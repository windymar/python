import pygame
import sys
from settings import Settings
from rover_view import RoverView
from bullet_view import BulletView
import logging
import os


class MarsRoverGame:
    def __init__(self):
        self._settings = Settings()
        logging.basicConfig(level=logging.INFO, filename='syslog.log', filemode='w')
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.mixer.init(buffer=64)
        pygame.init()
        pygame.display.set_caption("Mars Rover")

        self._screen = pygame.display.set_mode((self._settings.screen_width, self._settings.screen_height))

        self._rover_view = RoverView(self._screen, self._settings)
        self._bullets = pygame.sprite.Group()

        self._shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")

    def run_game(self):
        while True:
            self._check_events()
            self._bullets.update()
            self._update_screen()

            for bullet in self._bullets.copy():
                if bullet.is_out_of_map:
                    self._bullets.remove(bullet)
                    logging.info(F'Bullet removed. Bullets alive: {len(self._bullets)}')

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self._rover_view.turn_right()
                elif event.key == pygame.K_LEFT:
                    self._rover_view.turn_left()
                elif event.key == pygame.K_UP:
                    self._rover_view.move()
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()

    def _update_screen(self):
        self._screen.fill(self._settings.background_color)
        self._rover_view.draw()
        for bullet in self._bullets:
            bullet.draw()
        pygame.display.flip()

    def _fire_bullet(self):
        pygame.mixer.Sound.play(self._shoot_sound)
        bullet = BulletView(self._screen, self._settings, self._rover_view.get_position())
        self._bullets.add(bullet)
        logging.info(F'New bullet fired. Bullets alive: {len(self._bullets)}')


if __name__ == '__main__':
    mars_rover_game = MarsRoverGame()
    mars_rover_game.run_game()
