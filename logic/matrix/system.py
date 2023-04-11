from abc import abstractmethod
from logic.matrix.logic import Context


class System(object):

    def __init__(self, context: Context):
        self.context: Context = context

    @abstractmethod
    def update(self):
        pass

