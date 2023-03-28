from logic.component.icomponent import IComponent


EARTH_GRAVITY = 9.8

class RigibodyComponent(IComponent):

    def __init__(self):
        super(RigibodyComponent, self).__init__()
        self.gravity: float = EARTH_GRAVITY
