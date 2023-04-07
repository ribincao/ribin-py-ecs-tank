from logic.interface.component import Component


class MoveComponent(Component):

    def __init__(self):
        super(MoveComponent, self).__init__()
        self.speed: float = 5

