from common.logger import logger
from common.common import signal_handler
import asyncio
from logic.interface.logic import Logic
from window.interface.window import Window
from view.interface.view import View
from logic.context import Context
from logic.tank_logic import TankLogic
from view.tank_view import TankView
from window.pygame_window import PyGameWindow
from net.tcp import Tcp


class TankClient(object):

    def __init__(self):
        self.context: Context = Context()
        self.tcp: Tcp = Tcp(8888, 'tank', self.context)  # 网络层
        self.logic: Logic = TankLogic('tank', self.context)  # 逻辑层
        self.view: View = TankView(self.context)  # 表现层
        self.window: Window = PyGameWindow("Tank", self.view)  # 渲染层
        self._loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
        
    def init_game(self):
        # self.tcp.init_socket()
        self.logic.init_logic()
        self.view.init_view()
        self.window.init_window()
        
    def run(self):
        self._loop.create_task(self.tcp.run_client('localhost', 8888))
        self._loop.create_task(self.logic.update())
        self._loop.create_task(self.view.update())
        self._loop.create_task(self.window.update())
        self._loop.run_forever()


if __name__ == '__main__':
    def initialize():
        logger.init_logger()
        signal_handler()
    initialize()

    srv = TankClient()
    srv.init_game()
    srv.run()
