import unittest
from rover import Rover


class RoverTestCase(unittest.TestCase):
    def rover_is_able_to_make_move(self, starting_position, expected_position):
        rover = Rover(starting_position)
        rover.make_move()
        self.assertEqual(expected_position, rover.get_position())

    def rover_is_able_to_turn_left(self, starting_position, expected_position):
        rover = Rover(starting_position)
        rover.turn_left()
        self.assertEqual(expected_position, rover.get_position())

    def rover_is_able_to_turn_right(self, starting_position, expected_position):
        rover = Rover(starting_position)
        rover.turn_right()
        self.assertEqual(expected_position, rover.get_position())

    def test_rover_can_be_created_with_starting_position(self):
        starting_position = {'X': 0, 'Y': 0, 'Facing': 'N'}
        self.assertEqual(starting_position, Rover().get_position())

    def test_rover_can_move_forward_north(self):
        starting_position = {'X': 0, 'Y': 0, 'Facing': 'N'}
        expected_position = {'X': 0, 'Y': 1, 'Facing': 'N'}
        self.rover_is_able_to_make_move(starting_position, expected_position)

    def test_rover_can_move_forward_east(self):
        starting_position = {'X': 0, 'Y': 0, 'Facing': 'E'}
        expected_position = {'X': 1, 'Y': 0, 'Facing': 'E'}
        self.rover_is_able_to_make_move(starting_position, expected_position)

    def test_rover_can_move_forward_south(self):
        starting_position = {'X': 0, 'Y': 1, 'Facing': 'S'}
        expected_position = {'X': 0, 'Y': 0, 'Facing': 'S'}
        self.rover_is_able_to_make_move(starting_position, expected_position)

    def test_rover_can_move_forward_west(self):
        starting_position = {'X': 1, 'Y': 0, 'Facing': 'W'}
        expected_position = {'X': 0, 'Y': 0, 'Facing': 'W'}
        self.rover_is_able_to_make_move(starting_position, expected_position)

    def test_rover_can_turn_left_to_west(self):
        starting_position = {'X': 0, 'Y': 0, 'Facing': 'N'}
        expected_position = {'X': 0, 'Y': 0, 'Facing': 'W'}
        self.rover_is_able_to_turn_left(starting_position, expected_position)

    def test_rover_can_turn_left_to_south(self):
        starting_position = {'X': 0, 'Y': 0, 'Facing': 'W'}
        expected_position = {'X': 0, 'Y': 0, 'Facing': 'S'}
        self.rover_is_able_to_turn_left(starting_position, expected_position)

    def test_rover_can_turn_left_to_east(self):
        starting_position = {'X': 0, 'Y': 0, 'Facing': 'S'}
        expected_position = {'X': 0, 'Y': 0, 'Facing': 'E'}
        self.rover_is_able_to_turn_left(starting_position, expected_position)

    def test_rover_can_turn_left_to_north(self):
        starting_position = {'X': 0, 'Y': 0, 'Facing': 'E'}
        expected_position = {'X': 0, 'Y': 0, 'Facing': 'N'}
        self.rover_is_able_to_turn_left(starting_position, expected_position)

    def test_rover_can_turn_right_to_west(self):
        starting_position = {'X': 0, 'Y': 0, 'Facing': 'S'}
        expected_position = {'X': 0, 'Y': 0, 'Facing': 'W'}
        self.rover_is_able_to_turn_right(starting_position, expected_position)

    def test_rover_can_turn_right_to_south(self):
        starting_position = {'X': 0, 'Y': 0, 'Facing': 'E'}
        expected_position = {'X': 0, 'Y': 0, 'Facing': 'S'}
        self.rover_is_able_to_turn_right(starting_position, expected_position)

    def test_rover_can_turn_right_to_east(self):
        starting_position = {'X': 0, 'Y': 0, 'Facing': 'N'}
        expected_position = {'X': 0, 'Y': 0, 'Facing': 'E'}
        self.rover_is_able_to_turn_right(starting_position, expected_position)

    def test_rover_can_turn_right_to_north(self):
        starting_position = {'X': 0, 'Y': 0, 'Facing': 'W'}
        expected_position = {'X': 0, 'Y': 0, 'Facing': 'N'}
        self.rover_is_able_to_turn_right(starting_position, expected_position)


if __name__ == '__main__':
    unittest.main()
