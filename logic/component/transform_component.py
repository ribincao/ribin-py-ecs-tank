from interface.component import IComponent
from common.common import Vector2


class TransformComponent(IComponent):

    def __init__(self):
        super(TransformComponent, self).__init__()
        self.position: Vector2 = Vector2.zero()


