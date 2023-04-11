from logic.matrix.component import Component


class CreateComponent(Component):

    def __init__(self):
        super(CreateComponent, self).__init__()
        self.is_created: bool = False
        self.node_data: dict = {}

    def serialize(self) -> dict:
        return {}


