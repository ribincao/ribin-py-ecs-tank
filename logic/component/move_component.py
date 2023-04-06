from logic.interface.component import Component


class MoveDirection:
    STOP = -1
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class MoveComponent(Component):

    def __init__(self, is_async: bool = True):
        super(MoveComponent, self).__init__(is_async)
        self.speed: float = 5
        self.direction: int = MoveDirection.STOP

