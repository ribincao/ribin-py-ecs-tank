from logic.component.icomponent import IComponent


EARTH_GRAVITY = 9.8

class MoveComponent(IComponent):

    def __init__(self):
        super(MoveComponent, self).__init__()
        self.gravity: float = 0
        self.speed: float = 5
