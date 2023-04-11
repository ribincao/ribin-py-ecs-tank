from logic.matrix.component import Component


class BulletComponent(Component):

    def __init__(self):
        super(BulletComponent, self).__init__()
        self.belong: int = 0

