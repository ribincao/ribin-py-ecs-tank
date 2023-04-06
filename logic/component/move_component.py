from logic.interface.component import Component


class MoveComponent(Component):

    def __init__(self, is_async: bool = True):
        super(MoveComponent, self).__init__(is_async)
        self.speed: float = 5

