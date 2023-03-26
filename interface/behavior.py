from interface.entity import IEntity
from pygame import Surface, image, Rect
from typing import List


class IBehavior(object):

    def __init__(self, entity: IEntity):
        self.entity: IEntity = entity
        self.models: List[Surface] = []
        self.state: int = 0

    def init_modes(self, paths: List[str]):
        self.models = []
        for path in paths:
            model = image.load(path)
            self.models.append(model)

    def get_mode(self) -> Surface:
        return self.models[self.state]

    def get_rect(self) -> Rect:
        rect = self.get_mode().get_rect()
        rect.left, rect.top = self.entity.get_position()
        return rect
