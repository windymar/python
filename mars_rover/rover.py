class Rover:
    def __init__(self, position = {'X': 0, 'Y': 0, 'Facing': 'N'}):
        self._position = position

    def get_position(self):
        return self._position

    def get_position_y(self):
        return self._position['Y']

    def get_position_x(self):
        return self._position['X']

    def get_facing(self):
        return self._position['Facing']

    def make_move(self):
        if self.is_facing_north():
            self.move_north()
        elif self.is_facing_west():
            self.move_west()
        elif self.is_facing_east():
            self.move_east()
        elif self.is_facing_south():
            self.move_south()

    def turn_left(self):
        if self.is_facing_north():
            self.set_facing_west()
        elif self.is_facing_west():
            self.set_facing_south()
        elif self.is_facing_south():
            self.set_facing_east()
        elif self.is_facing_east():
            self.set_facing_north()

    def turn_right(self):
        if self.is_facing_north():
            self.set_facing_east()
        elif self.is_facing_east():
            self.set_facing_south()
        elif self.is_facing_south():
            self.set_facing_west()
        elif self.is_facing_west():
            self.set_facing_north()

    def is_facing_north(self):
        return self.is_facing('N')

    def is_facing_west(self):
        return self.is_facing('W')

    def is_facing_south(self):
        return self.is_facing('S')

    def is_facing_east(self):
        return self.is_facing('E')

    def move_north(self):
        self.make_step_position_y(1)

    def move_south(self):
        self.make_step_position_y(-1)

    def move_east(self):
        self.make_step_position_x(1)

    def move_west(self):
        self.make_step_position_x(-1)

    def set_facing_north(self):
        self.change_facing('N')

    def set_facing_west(self):
        self.change_facing('W')

    def set_facing_south(self):
        self.change_facing('S')

    def set_facing_east(self):
        self.change_facing('E')

    def is_facing(self, facing):
        return self._position['Facing'] == facing

    def change_facing(self, facing):
        self._position['Facing'] = facing

    def make_step_position_x(self, step):
        self._position['X'] += step

    def make_step_position_y(self, step):
        self._position['Y'] += step
