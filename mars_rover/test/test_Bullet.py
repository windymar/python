import unittest
from bullet import Bullet


class BulletTestCase(unittest.TestCase):
    def _bullet_can_make_step(self, starting, expected):
        bullet = Bullet(starting)
        bullet.make_step()
        self.assertEqual(expected, bullet.get_position())

    def test_bullet_can_be_created_with_starting_position(self):
        starting = {'X': 0, 'Y': 0, 'Facing': 'N'}
        bullet = Bullet(starting)
        self.assertEqual(starting, bullet.get_position())

    def test_bullet_can_go_forward_north(self):
        starting = {'X': 0, 'Y': 0, 'Facing': 'N'}
        expected = {'X': 0, 'Y': 1, 'Facing': 'N'}
        self._bullet_can_make_step(starting, expected)

    def test_bullet_can_go_forward_east(self):
        starting = {'X': 0, 'Y': 0, 'Facing': 'E'}
        expected = {'X': 1, 'Y': 0, 'Facing': 'E'}
        self._bullet_can_make_step(starting, expected)

    def test_bullet_can_go_forward_south(self):
        starting = {'X': 0, 'Y': 1, 'Facing': 'S'}
        expected = {'X': 0, 'Y': 0, 'Facing': 'S'}
        self._bullet_can_make_step(starting, expected)

    def test_bullet_can_go_forward_west(self):
        starting = {'X': 1, 'Y': 0, 'Facing': 'W'}
        expected = {'X': 0, 'Y': 0, 'Facing': 'W'}
        self._bullet_can_make_step(starting, expected)

if __name__ == '__main__':
    unittest.main()
