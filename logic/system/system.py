from abc import abstractmethod
from logic.context import Context


class System(object):

    def __init__(self, context: Context):
        self.context: Context = context

    @abstractmethod
    async def update(self):
        pass

