from abc import abstractmethod
from view.iview import IView
from net.tcp import Tcp
from net.connection import Connection
from typing import Optional


class IWindow(object):

    def __init__(self, window_name: str, view: IView, tcp: Tcp):
        self.window_name: str = window_name
        self.view: IView = view
        self.tcp: Tcp = tcp

    @abstractmethod
    async def update(self):
        pass

    def init_window(self):
        pass

