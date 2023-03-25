from common.logger import logger
from common.common import signal_handler
import asyncio
from interface.logic import ILogic
from context import Context
from logic.tank_logic import TankLogic


class Client(object):

    def __init__(self):
        self.context: Context = Context()
        self.logic: ILogic = TankLogic(1, self.context)
        # self.connection = None # 用于网络连接
        # self.window = None #用来监听和渲染ui
        self._loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
        
    def init_game(self):
        self.logic.init_system()
        
    def run(self):
        self._loop.create_task(self.logic.update())
        self._loop.run_forever()


if __name__ == '__main__':
    def initialize():
        logger.init_logger()
        signal_handler()
    initialize()

    srv = Client()
    srv.init_game()
    srv.run()
