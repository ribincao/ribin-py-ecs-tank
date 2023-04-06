from logic.interface.component import Component


class State:

    normal = 0
    move = 1


class StateComponent(Component):

    def __init__(self):
        self.state: int = State.normal

