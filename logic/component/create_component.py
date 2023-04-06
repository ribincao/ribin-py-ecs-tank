from logic.interface.component import Component


class CreateComponent(Component):

    def __init__(self, is_async: bool = True):
        super(CreateComponent, self).__init__(is_async)
        self.create_status: bool = False
        self.node_data: dict = {}


