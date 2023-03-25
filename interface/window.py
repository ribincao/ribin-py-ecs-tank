from abc import abstractmethod


class IWindow(object):

    def __init__(self):
        pass

    @abstractmethod
    async def update(self):
        pass

    def init_window(self):
        pass
