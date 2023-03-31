from logic.entity.entity import GameLogicEntity
from pygame import Surface, Rect
from typing import Dict, List
from abc import abstractmethod
from common.logger import logger


class IBehavior(object):

    def __init__(self, entity: GameLogicEntity):
        self.entity: GameLogicEntity = entity
        self.models: List[object] = []

    @abstractmethod
    def init_models(self, module: str, mod_name: str):
        pass

    @abstractmethod
    def mode(self) -> object:
        pass

    @abstractmethod
    def rect(self) -> object:
        pass


class IPyGameBehavior(IBehavior):

    def __init__(self, entity: GameLogicEntity):
        super(IPyGameBehavior, self).__init__(entity)
        self.models: List[Surface] = []

    @abstractmethod
    def init_models(self, module: str, mod_name: str):
        from view.resource.gltf import GLTF
        import pygame.image as img
        gltf = GLTF()
        paths = gltf.load_models(module, mod_name)
        self.models = []
        for path in paths:
            self.models.append(img.load(path))

    @property
    def layer(self) -> int:
        return self.entity.layer

    @property
    def mode(self) -> Surface:
        return self.models[self.entity.mod_index]

    @property
    def rect(self) -> Rect:
        rect = self.mode.get_rect()
        x, y = self.entity.transform.position.to_tuple()
        rect.left, rect.top = x, y
        return rect
