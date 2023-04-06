from logic.interface.component import Component


EARTH_GRAVITY = 9.8


class RigibodyComponent(Component):

    def __init__(self, is_async: bool = True):
        super(RigibodyComponent, self).__init__(is_async)
        self.gravity: float = EARTH_GRAVITY

