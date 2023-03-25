from interface.window import IWindow
from common.logger import logger
import asyncio


class PyGameWindow(IWindow):
    RENDER_RATE = 100e-3

    def __init__(self):
        super(PyGameWindow, self).__init__()

    async def update(self):
        while True:
            logger.debug("PyGameWindow Update.")
            await asyncio.sleep(self.RENDER_RATE)

    def init_window(self):
        pass
