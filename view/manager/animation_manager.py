from view.interface.pygame_behavior import PyGameBehavior
from common.singleton import Singleton
from logic.entity.entity import GameLogicEntity
from pygame import Surface, Rect
from typing import Optional, List, Tuple
import pygame
import pygame.image as img
from view.resource.gltf import GLTF


class Animation(object):

    def __init__(self, position: Tuple[float, float], rotation: float):
        self.models: List[Surface] = []
        self.cur_index: int = 0
        self.position: Tuple[float, float] = position
        self.rotation: float = rotation

    def init_animation(self, gid: str, model_name: str):
        gltf = GLTF()
        models = gltf.load_models(gid, model_name)
        for model in models:
            model_index = model.get("model_index", '')
            if not model_index:
                continue
            path = model.get("model", "")
            if not path:
                continue
            self.models.append(img.load(path))

    @property
    def animation(self) -> Tuple[Optional[Surface], Optional[Rect]]:
        if not self.models or not 0<= self.cur_index < len(self.models):
            return None, None
        surface = self.models[self.cur_index]
        self.cur_index += 1
        if not surface:
            return None, None
        model = pygame.transform.rotate(surface, self.rotation)
        rect = model.get_rect(center=self.position)
        return model, rect


class AnimationManager(Singleton):

    def __init__(self):
        pass

    def get_animation(self, entity: GameLogicEntity, model_name: str) -> Optional[Animation]:
        if not entity.model or not entity.model.model_name:
            return None
        animation = Animation(entity.transform.position, entity.transform.rotation)
        animation.init_animation("tank", model_name)
        return animation


animation_manager = AnimationManager()
