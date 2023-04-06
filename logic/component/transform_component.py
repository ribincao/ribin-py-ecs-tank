from logic.interface.component import Component
from typing import Tuple


class Vector2(object):

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    @staticmethod
    def zero():
        return Vector2(0.0, 0.0)

    def to_tuple(self) -> Tuple[float, float]:
        return self.x, self.y


class TransformComponent(Component):

    def __init__(self):
        super(TransformComponent, self).__init__()
        self.position: Vector2 = Vector2.zero()
        self.last_position: Vector2 = Vector2.zero()



