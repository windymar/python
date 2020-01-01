class RoverController:
    def __init__(self, rover, map_size, callback=None):
        self._rover = rover
        self._map_size = map_size
        self._callback = callback

    def get_rover(self):
        return self._rover

    def get_map_size(self):
        return self._map_size

    def execute_command(self, command):
        for c in command:
            if c == 'M':
                self.make_move()
                if self._callback is not None:
                    self._callback.position_updated_event(self._rover.get_position())
            elif c == 'L':
                self._rover.turn_left()
                if self._callback is not None:
                    self._callback.turned_left()
            elif c == 'R':
                self._rover.turn_right()
                if self._callback is not None:
                    self._callback.turned_right()

    def make_move(self):
        if self._rover.is_facing_north() and self._rover.get_position_y() < self._map_size['Height'] - 1:
            self._rover.make_move()
        elif self._rover.is_facing_west() and self._rover.get_position_x() > 0:
            self._rover.make_move()
        elif self._rover.is_facing_east() and self._rover.get_position_x() < self._map_size['Width'] - 1:
            self._rover.make_move()
        elif self._rover.is_facing_south() and self._rover.get_position_y() > 0:
            self._rover.make_move()
