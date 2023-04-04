from logic.component.component import Component
from common.common import Vector2


class TransformComponent(Component):

    def __init__(self):
        super(TransformComponent, self).__init__()
        self.position: Vector2 = Vector2.zero()


