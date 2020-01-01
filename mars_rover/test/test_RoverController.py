import unittest
from rover import Rover
from rover_controller import RoverController


class RoverControllerTestCase(unittest.TestCase):
    def setUp(self):
        self._max_size_x = 10
        self._max_size_y = 10
        self._map_size = {'Width': self._max_size_x, 'Height': self._max_size_y}

    def _rover_controller_is_able_to_execute_command(self, starting_position, command, expected_position):
        rover = Rover(starting_position)
        rover_controller = RoverController(rover, self._map_size)
        rover_controller.execute_command(command)
        self.assertEqual(expected_position, rover.get_position())

    def test_can_execute_command_move_forward(self):
        starting_position = {'X': 0, 'Y': 0, 'Facing': 'N'}
        expected_position = {'X': 0, 'Y': 1, 'Facing': 'N'}
        self._rover_controller_is_able_to_execute_command(starting_position, 'M', expected_position)

    def test_can_execute_command_turn_left_and_move_forward(self):
        starting_position = {'X': 1, 'Y': 0, 'Facing': 'N'}
        expected_position = {'X': 0, 'Y': 0, 'Facing': 'W'}
        self._rover_controller_is_able_to_execute_command(starting_position, 'LM', expected_position)

    def test_can_execute_command_turn_right_and_move_forward(self):
        starting_position = {'X': 0, 'Y': 0, 'Facing': 'N'}
        expected_position = {'X': 1, 'Y': 0, 'Facing': 'E'}
        self._rover_controller_is_able_to_execute_command(starting_position, 'RM', expected_position)

    def test_cannot_make_move_north_when_on_north_edge(self):
        starting_position = {'X': 0, 'Y': self._max_size_y - 1, 'Facing': 'N'}
        expected_position = {'X': 0, 'Y': self._max_size_y - 1, 'Facing': 'N'}
        self._rover_controller_is_able_to_execute_command(starting_position, 'M', expected_position)

    def test_cannot_make_move_west_when_on_west_edge(self):
        starting_position = {'X': 0, 'Y': 0, 'Facing': 'W'}
        expected_position = {'X': 0, 'Y': 0, 'Facing': 'W'}
        self._rover_controller_is_able_to_execute_command(starting_position, 'M', expected_position)

    def test_cannot_make_move_south_when_on_south_edge(self):
        starting_position = {'X': 0, 'Y': 0, 'Facing': 'S'}
        expected_position = {'X': 0, 'Y': 0, 'Facing': 'S'}
        self._rover_controller_is_able_to_execute_command(starting_position, 'M', expected_position)

    def test_cannot_make_move_east_when_on_east_edge(self):
        starting_position = {'X': self._max_size_x - 1, 'Y': 0, 'Facing': 'E'}
        expected_position = {'X': self._max_size_x - 1, 'Y': 0, 'Facing': 'E'}
        self._rover_controller_is_able_to_execute_command(starting_position, 'M', expected_position)

    def test_moving(self):
        starting_position = {'X': 0, 'Y': 0, 'Facing': 'N'}
        expected_position = {'X': 8, 'Y': 2, 'Facing': 'W'}
        self._rover_controller_is_able_to_execute_command(starting_position, 'RMMMLMRMMMMMMMLMLM', expected_position)


if __name__ == '__main__':
    unittest.main()
