from abc import abstractmethod


class Window(object):
    RENDER_RATE = 20e-3

    def __init__(self, window_name: str):
        self.window_name: str = window_name

    @abstractmethod
    async def update(self):
        pass
    
    @abstractmethod
    def init_window(self):
        pass

