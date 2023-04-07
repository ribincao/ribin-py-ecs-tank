from logic.entity.entity import GameLogicEntity
from pygame import Surface, Rect
from typing import Dict, List, Tuple, Optional
from abc import abstractmethod
import pygame
from view.resource.gltf import GLTF
import pygame.image as img


class Behavior(object):

    def __init__(self, entity: GameLogicEntity):
        self.entity: GameLogicEntity = entity
        self.models: Dict[str, object] = {}
        self.gltf: GLTF = GLTF()

    @abstractmethod
    def init_models(self):
        pass

    @abstractmethod
    async def update(self):
        pass

    @abstractmethod
    def mode(self) -> object:
        pass

    @abstractmethod
    def rect(self) -> object:
        pass


class PyGameBehavior(Behavior):

    def __init__(self, entity: GameLogicEntity):
        super(PyGameBehavior, self).__init__(entity)
        self.models: Dict[str, Surface] = {}

    def _load_models(self, module: str, model_name: str):
        models = self.gltf.load_models(module, model_name)
        self.models = {}
        for model in models:
            model_index = model.get("model_index", '')
            if not model_index:
                continue
            path = model.get("model", "")
            if not path:
                continue
            self.models[model_index] = img.load(path)
    
    @abstractmethod
    def init_models(self):
        pass

    @property
    def layer(self) -> int:
        if not self.entity.box_collider:
            return 0
        return self.entity.box_collider.layer

    @property
    def mode(self) -> Optional[Surface]:
        if not self.entity.model:
            return None
        model = self.models[self.entity.model.model_index]
        return pygame.transform.rotate(model, self.entity.transform.rotation)

    @property
    def rect(self) -> Optional[Rect]:
        if not self.mode:
            return None
        rect = self.mode.get_rect(center=self.entity.transform.position)
        return rect

    def get_bullet_position(self) -> Tuple[float, float]:
        return 0.0, 0.0

    @abstractmethod
    async def update(self):
        pass
