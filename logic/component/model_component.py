from logic.interface.component import Component


class ModelComponent(Component):

    def __init__(self):
        super(ModelComponent, self).__init__()
        self.model_index: str = ""
        self.model_name: str = ''

