from logic.interface.component import Component


class ModelComponent(Component):

    def __init__(self, is_async: bool = True):
        super(ModelComponent, self).__init__(is_async)
        self.model_index: str = ""
        self.model_name: str = ''

