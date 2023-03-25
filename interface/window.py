from abc import abstractmethod
from interface.context import IContext


class IWindow(object):

    def __init__(self, window_name: str, context: IContext):
        self.window_name: str = window_name
        self.context: IContext = context

    @abstractmethod
    async def update(self):
        pass

    def init_window(self):
        pass
