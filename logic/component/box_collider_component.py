from logic.interface.component import Component
from typing import Tuple


class BoxColliderComponent(Component):

    def __init__(self, is_async: bool = True):
        super(BoxColliderComponent, self).__init__(is_async)
        self.width: float = 0.0
        self.height: float = 0.0
        self.collider_direction: Tuple[float, float] = (0, 0)
        self.layer: int = 0

