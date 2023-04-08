from common.logger import logger
from common.common import signal_handler
import asyncio
from logic.interface.logic import Logic
from logic.context import Context
from logic.tank_logic import TankLogic
from net.tcp import Tcp


class Server(object):

    def __init__(self):
        self.context: Context = Context()
        self.tcp: Tcp = Tcp(8888, 'tank', self.context)  # 网络层
        self.logic: Logic = TankLogic('tank', self.context)  # 逻辑层
        self._loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
        
    def init_game(self):
        # self.tcp.init_socket()
        self.logic.init_logic()

    async def play(self):
        while True:
            await self.logic.update()
            await asyncio.sleep(20e-3)
        
    def run(self):
        self._loop.create_task(self.tcp.run_server())
        self._loop.create_task(self.play())
        self._loop.run_forever()


if __name__ == '__main__':
    def initialize():
        logger.init_logger()
        signal_handler()
    initialize()

    srv = Server()
    srv.init_game()
    srv.run()
