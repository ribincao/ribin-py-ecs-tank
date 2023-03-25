from interface.component import IComponent


class Vector2(object):

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    @staticmethod
    def zero():
        return Vector2(0.0, 0.0)


class TransformComponent(IComponent):

    def __init__(self):
        super(TransformComponent, self).__init__()
        self.position: Vector2 = Vector2.zero()


