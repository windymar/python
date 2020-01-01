class Bullet:
    def __init__(self, position={'X': 0, 'Y': 0, 'Facing': 'N'}):
        self._pos = position

    def get_position(self):
        return self._pos

    def make_step(self):
        if self._pos['Facing'] == 'N':
            self._pos['Y'] += 1
        elif self._pos['Facing'] == 'E':
            self._pos['X'] += 1
        elif self._pos['Facing'] == 'S':
            self._pos['Y'] -= 1
        elif self._pos['Facing'] == 'W':
            self._pos['X'] -= 1
