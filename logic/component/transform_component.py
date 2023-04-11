from logic.matrix.component import Component
from typing import Tuple


class TransformComponent(Component):

    def __init__(self):
        super(TransformComponent, self).__init__()
        self.position: Tuple[float, float] = (0.0, 0.0)
        self.rotation: float = 0.0
        self.last_position: Tuple[float, float] = (0.0, 0.0)

    def add_position(self, delta_x: float, delta_y: float):
        self.position = (self.position[0] + delta_x, self.position[1] + delta_y)



