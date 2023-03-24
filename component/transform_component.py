

class Vector2(object):

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    @staticmethod
    def zero():
        return Vector2(0.0, 0.0)


if __name__ == '__main__':
    position1 = Vector2(1.0, 2.0)
    position2 = Vector2.zero()

    print(position1.x, position2.x)
    print(position1.y, position2.y)

