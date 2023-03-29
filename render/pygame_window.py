from render.iwindow import IWindow
import asyncio
import pygame
from typing import Optional
from view.iview import IView
from common.logger import logger
from net.tcp import Tcp


class PyGameWindow(IWindow):
    RENDER_RATE = 100e-3
    SIZE = (1024, 900)

    def __init__(self, window_name: str, view: IView, tcp: Tcp):
        super(PyGameWindow, self).__init__(window_name, view, tcp)
        self.window: Optional[pygame.Surface] = None

    async def update(self):
        while True:
            if not self.window:
                return
            self.window.fill(self.view.back_ground)
            await self.listen_event()

            for behavior in self.view.get_behaviors():
                logger.debug(f"window update behavior {behavior}")
                if not behavior.models:
                    continue
                self.window.blit(behavior.mode, behavior.rect)

            pygame.display.update()
            await asyncio.sleep(self.RENDER_RATE)

    def init_window(self):
        pygame.display.init()
        pygame.display.set_caption(self.window_name)
        self.window = pygame.display.set_mode(self.SIZE)

    async def listen_event(self):
        event_list = pygame.event.get()
        for event in event_list:
            operation = ''
            if event.type == pygame.QUIT:
                import sys
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                operation = ''
                if event.key == pygame.K_w:
                    operation = 'w'
                if event.key == pygame.K_a:
                    operation = 'a'
                if event.key == pygame.K_s:
                    operation = 's'
                if event.key == pygame.K_d:
                    operation = 'd'
            if event.type == pygame.KEYUP:
                operation = '-'

            if operation == '':
                continue
            await self.view.handle_event(operation)
            # if self.tcp.connection:
            #     await self.tcp.connection.send_message(operation)

