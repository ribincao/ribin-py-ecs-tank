from logic.interface.component import Component
from typing import Tuple


class TransformComponent(Component):

    def __init__(self):
        super(TransformComponent, self).__init__()
        self.position: Tuple[float, float] = (0.0, 0.0)
        self.last_position: Tuple[float, float] = (0.0, 0.0)



