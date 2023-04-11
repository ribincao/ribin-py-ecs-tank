from abc import abstractmethod
from logic.matrix.ilogic import Context


class System(object):

    def __init__(self, context: Context):
        self.context: Context = context

    @abstractmethod
    def update(self):
        pass

