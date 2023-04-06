from logic.interface.component import Component
from typing import Tuple


class TransformComponent(Component):

    def __init__(self, is_async: bool = True):
        super(TransformComponent, self).__init__(is_async)
        self.position: Tuple[float, float] = (0.0, 0.0)
        self.last_position: Tuple[float, float] = (0.0, 0.0)



