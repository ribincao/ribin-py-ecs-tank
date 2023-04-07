from logic.interface.component import Component
from typing import Tuple


class TransformComponent(Component):

    def __init__(self, is_async: bool = True):
        super(TransformComponent, self).__init__(is_async)
        self.position: Tuple[float, float] = (0.0, 0.0)
        self.rotation: float = 0.0
        self.last_position: Tuple[float, float] = (0.0, 0.0)

    def add_position(self, delta_x: float, delta_y: float):
        self.position = (self.position[0] + delta_x, self.position[1] + delta_y)



