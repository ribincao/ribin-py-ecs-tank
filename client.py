from common.logger import logger
from common.common import signal_handler
import asyncio
from interface.logic import ILogic
from interface.window import IWindow
from context import Context
from logic.tank_logic import TankLogic
from view.pygame_window import PyGameWindow


class Client(object):

    def __init__(self):
        self.context: Context = Context()
        self.logic: ILogic = TankLogic(1, self.context) # 逻辑层
        self.window: IWindow = PyGameWindow() # 表现层
        # self.connection = None # 用于网络连接
        self._loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
        
    def init_game(self):
        self.logic.init_logic()
        self.window.init_window()
        
    def run(self):
        self._loop.create_task(self.logic.update())
        self._loop.create_task(self.window.update())
        self._loop.run_forever()


if __name__ == '__main__':
    def initialize():
        logger.init_logger()
        signal_handler()
    initialize()

    srv = Client()
    srv.init_game()
    srv.run()
