from logic.context import Context
from abc import abstractmethod


class View(object):
    VIEW_RATE = 20e-3

    def __init__(self, context: Context):
        self.context: Context = context

    @abstractmethod
    async def update(self):
        pass

    @abstractmethod
    def init_view(self):
        pass

    @abstractmethod
    async def handler(self, operation: str):
        pass

