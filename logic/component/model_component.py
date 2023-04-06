from logic.interface.component import Component


class ModelIndex:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class ModelComponent(Component):

    def __init__(self):
        self.model_index: int = ModelIndex.UP
        self.mod_name: str = ''

