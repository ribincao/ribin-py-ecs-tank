from abc import abstractmethod
from view.view import View


class IWindow(object):

    def __init__(self, window_name: str, view: View):
        self.window_name: str = window_name
        self.view: View = view

    @abstractmethod
    async def update(self):
        pass

    def init_window(self):
        pass

