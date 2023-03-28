from logic.component.icomponent import IComponent


class MoveComponent(IComponent):

    def __init__(self):
        super(MoveComponent, self).__init__()
        self.speed: float = 5
