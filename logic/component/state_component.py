from logic.interface.component import Component


class State:
    normal = 0
    move = 1


class StateComponent(Component):

    def __init__(self, is_async: bool = True):
        super(StateComponent, self).__init__(is_async)
        self.state: int = State.normal

