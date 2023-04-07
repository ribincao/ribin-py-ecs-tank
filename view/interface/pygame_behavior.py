from view.interface.behavior import Behavior
from logic.entity.entity import GameLogicEntity
import pygame
from pygame import Surface, Rect
from typing import Dict, Optional, Tuple
from abc import abstractmethod
import pygame.image as img


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
    def model(self) -> Optional[Surface]:
        if not self.entity.model:
            return None
        model = self.models.get(self.entity.model.model_index, None)
        if not model:
            return model
        return pygame.transform.rotate(model, self.entity.transform.rotation)

    @property
    def rect(self) -> Optional[Rect]:
        if not self.model:
            return None
        rect = self.model.get_rect(center=self.entity.transform.position)
        return rect

    @abstractmethod
    async def update(self):
        pass
    
    def get_forward(self) -> Tuple[Tuple[float, float], float]:
        position = self.entity.transform.position
        if not self.entity.model or not self.rect:
            return (0.0, 0.0), 0.0

        if self.entity.transform.rotation == 0:
            return (position[0], position[1] - self.rect.height / 2), self.entity.transform.rotation
        elif self.entity.transform.rotation == 180:
            return (position[0], position[1] + self.rect.height / 2), self.entity.transform.rotation
        elif self.entity.transform.rotation == 90:
            return (position[0] - self.rect.width / 2, position[1]), self.entity.transform.rotation
        elif self.entity.transform.rotation == 270:
            return (position[0] + self.rect.width / 2, position[1]), self.entity.transform.rotation

        return (0.0, 0.0), 0.0

