from interface.window import IWindow
import asyncio
import pygame
from typing import Optional
from interface.view import IView


class PyGameWindow(IWindow):
    RENDER_RATE = 100e-3
    SIZE = (1024, 900)

    def __init__(self, window_name: str, view: IView):
        super(PyGameWindow, self).__init__(window_name, view)
        self.window: Optional[pygame.Surface] = None

    async def update(self):
        while True:
            self.window.fill(self.view.back_ground)
            await self.listen_event()

            for behavior in self.view.get_behaviors():
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
            if event.type == pygame.QUIT:
                import sys
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                operation = ''
                if event.key == pygame.K_w:
                    operation = 'w'

                await self.view.handle_event(operation)
