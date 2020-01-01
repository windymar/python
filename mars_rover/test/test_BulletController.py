import unittest
from bullet import Bullet
from bullet_controller import BulletController


class BulletControllerTestCase(unittest.TestCase):
    def setUp(self):
        self._map_width = 10
        self._map_height = 10
        self._map_size = {"Width": self._map_width, "Height": self._map_height}

    def _can_update_bullet_position(self, starting, expected):
        bullet = Bullet(starting)
        bullet_controller = BulletController(bullet, self._map_size)
        bullet_controller.update()
        self.assertEqual(expected, bullet.get_position())

    def test_can_move_bullet(self):
        starting = {"X": 0, 'Y': 0, 'Facing': 'N'}
        expected = {"X": 0, 'Y': 1, 'Facing': 'N'}
        self._can_update_bullet_position(starting, expected)


if __name__ == '__main__':
    unittest.main()