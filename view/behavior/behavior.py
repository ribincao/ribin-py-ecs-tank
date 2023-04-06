from logic.entity.entity import GameLogicEntity
from pygame import Surface, Rect
from typing import Dict, List, Tuple, Optional
from abc import abstractmethod


class Behavior(object):

    def __init__(self, entity: GameLogicEntity):
        self.entity: GameLogicEntity = entity
        self.models: List[object] = []

    @abstractmethod
    def init_models(self, module: str, mod_name: str):
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
        self.models: Dict[int, Surface] = {}

    def init_models(self, module: str, mod_name: str):
        from view.resource.gltf import GLTF
        import pygame.image as img
        gltf = GLTF()
        models = gltf.load_models(module, mod_name)
        self.models = {}
        for model in models:
            model_id = model.get("index", -1)
            if model_id < 0:
                continue
            path = model.get("model", "")
            if not path:
                continue
            self.models[model_id] = img.load(path)

    @property
    def layer(self) -> int:
        if not self.entity.box_collider:
            return 0
        return self.entity.box_collider.layer

    @property
    def mode(self) -> Optional[Surface]:
        if not self.entity.model:
            return None
        return self.models[self.entity.model.model_index]

    @property
    def rect(self) -> Optional[Rect]:
        if not self.mode:
            return None
        rect = self.mode.get_rect()
        x, y = self.entity.transform.position
        rect.left, rect.top = int(x), int(y)
        return rect

    def get_bullet_position(self) -> Tuple[float, float]:
        return 0.0, 0.0

    @abstractmethod
    async def update(self):
        pass
