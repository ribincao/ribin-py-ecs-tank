from logic.interface.component import Component


EARTH_GRAVITY = 9.8


class RigibodyComponent(Component):

    def __init__(self):
        super(RigibodyComponent, self).__init__()
        self.gravity: float = EARTH_GRAVITY

