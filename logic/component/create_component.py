from logic.interface.component import Component


class CreateComponent(Component):

    def __init__(self):
        super(CreateComponent, self).__init__()
        self.create_status: bool = False
        self.node_data: dict = {}


