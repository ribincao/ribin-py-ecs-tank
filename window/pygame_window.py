from window.interface.window import Window
import asyncio
import pygame
from typing import Optional
from view.interface.pygame_view import PyGameView


class PyGameWindow(Window):

    def __init__(self, window_name: str, view: PyGameView):
        super(PyGameWindow, self).__init__(window_name)
        self.window: Optional[pygame.Surface] = None
        self.view: PyGameView = view

    async def update(self):
        if not self.window:
            return
        self.window.fill(self.view.back_ground)
        await self.listen_event()

        for behavior in self.view.get_behaviors():
            if not behavior.models:
                continue
            if not behavior.model or not behavior.rect:
                continue
            self.window.blit(behavior.model, behavior.rect)
            pygame.draw.rect(self.window, (255, 0, 0), behavior.rect, 1)

        pygame.display.update()

    def init_window(self):
        pygame.display.init()
        pygame.display.set_caption(self.window_name)
        self.window = pygame.display.set_mode(self.view.window_size)

    async def listen_event(self):
        event_list = pygame.event.get()
        for event in event_list:
            operation = ''
            if event.type == pygame.QUIT:
                import sys
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    operation = 'w'
                if event.key == pygame.K_a:
                    operation = 'a'
                if event.key == pygame.K_s:
                    operation = 's'
                if event.key == pygame.K_d:
                    operation = 'd'
                if event.key == pygame.K_n:
                    operation = 'n'
                if event.key == pygame.K_j:
                    operation = 'j'
                if event.key == pygame.K_t:
                    operation = 't'

            if event.type == pygame.KEYUP:
                operation = '-'

            if operation == '':
                continue
            await self.view.handler(operation)

