from logic.component.component import Component


class MoveDirection:
    STOP = -1
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class MoveComponent(Component):

    def __init__(self):
        super(MoveComponent, self).__init__()
        self.speed: float = 5
        self.direction: int = -1

