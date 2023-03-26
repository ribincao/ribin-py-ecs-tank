from interface.window import IWindow
from common.logger import logger
import asyncio
import pygame
from typing import Optional
from interface.context import IContext


class PyGameWindow(IWindow):
    RENDER_RATE = 100e-3

    def __init__(self, window_name: str, context: IContext):
        super(PyGameWindow, self).__init__(window_name, context)
        self.window: Optional[pygame.Surface] = None

        self.t_img = pygame.image.load("./resource/tank/imge/player/p1tankD.gif")
        self.t_rect = self.t_img.get_rect()
        self.t_rect.left = 0
        self.t_rect.top = 0

    async def update(self):
        while True:
            self.window.fill(pygame.Color(0, 0, 0))
            self.listen_event()

            self.window.blit(self.t_img, self.t_rect)
            pygame.display.update()
            await asyncio.sleep(self.RENDER_RATE)

    def init_window(self):
        pygame.display.init()
        pygame.display.set_caption(self.window_name)
        self.window = pygame.display.set_mode((1024, 980))

    def listen_event(self):
        # StartScene
        # if not self.in_game:
        #     return self.start_scene()
        return self.game_scene()

    def game_scene(self):
        # GameScene
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                import sys
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    logger.debug("w keydown")
                    self.t_rect.top -= 1
                elif event.key == pygame.K_a:
                    logger.debug("a keydown")
                    self.t_rect.left -= 1
                elif event.key == pygame.K_s:
                    logger.debug("s keydown")
                    self.t_rect.top += 1
                elif event.key == pygame.K_d:
                    logger.debug("d keydown")
                    self.t_rect.left += 1

    def start_scene(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                import sys
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    logger.debug("w keydown")
                    self.t_rect.top -= 1
                elif event.key == pygame.K_a:
                    logger.debug("a keydown")
                    self.t_rect.left -= 1
                elif event.key == pygame.K_s:
                    logger.debug("s keydown")
                    self.t_rect.top += 1
                elif event.key == pygame.K_d:
                    logger.debug("d keydown")
                    self.t_rect.left += 1
