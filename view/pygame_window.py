from interface.window import IWindow
from common.logger import logger
import asyncio
import pygame


class PyGameWindow(IWindow):
    RENDER_RATE = 100e-3

    def __init__(self, game_name: str):
        super(PyGameWindow, self).__init__()
        self.game_name: str = game_name
        self.window = None

    async def update(self):
        while True:
            logger.debug("PyGameWindow Update.")
            self.listen_event()
            pygame.display.update()
            await asyncio.sleep(self.RENDER_RATE)

    def init_window(self):
        pygame.display.init()
        pygame.display.set_caption(self.game_name)
        self.window = pygame.display.set_mode((1024, 980))
        self.window.fill(pygame.Color(0, 0, 0))

    def listen_event(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                import sys
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    logger.debug("w keydown")
                elif event.key == pygame.K_a:
                    logger.debug("a keydown")
                elif event.key == pygame.K_s:
                    logger.debug("s keydown")
                elif event.key == pygame.K_d:
                    logger.debug("d keydown")
