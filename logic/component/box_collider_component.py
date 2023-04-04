from logic.component.component import Component



class BoxColliderComponent(Component):

    def __init__(self):
        super(BoxColliderComponent, self).__init__()
        self.width: float = 0.0
        self.height: float = 0.0
