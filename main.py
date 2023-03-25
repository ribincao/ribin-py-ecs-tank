from common.logger import logger
from common.common import signal_handler
import asyncio
from typing import Optional
from interface.game import IGame
from manager.context import Context
from manager.system_manager import SystemManager


class Client(object):

    def __init__(self):
        self.game: Optional[IGame] = None
        self._loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()


    def run(self):
        self._loop.create_task(self.game.update())
        self._loop.run_forever()


if __name__ == '__main__':
    def initialize():
        logger.init_logger()
        signal_handler()
    initialize()

    srv = Client()
    srv.run()
