class BulletController:
    def __init__(self, bullet, map_size, callback = None):
        self._bullet = bullet
        self._map_size = map_size
        self._callback = callback

    def update(self):
        self._bullet.make_step()
        position = self._bullet.get_position()
        if self._callback:
            self._callback.position_updated_event(position)
            if position['X'] > self._map_size['Width'] or position['X'] < 0\
               or position['Y'] > self._map_size['Height'] or position['Y'] < 0:
                self._callback.map_edge_reached_event()
