from abc import abstractmethod
from interface.view import IView


class IWindow(object):

    def __init__(self, window_name: str, view: IView):
        self.window_name: str = window_name
        self.view: IView = view

    @abstractmethod
    async def update(self):
        pass

    def init_window(self):
        pass
