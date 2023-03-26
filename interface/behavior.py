from interface.entity import IEntity
from pygame import Surface, Rect
from typing import Dict
from abc import abstractmethod


class IBehavior(object):

    def __init__(self, entity: IEntity):
        self.entity: IEntity = entity
        self.models: Dict[str, Surface] = {}
        self.state: str = ''

    @abstractmethod
    def init_modes(self):
        pass

    def get_mode(self) -> Surface:
        return self.models[self.state]

    def get_rect(self) -> Rect:
        rect = self.get_mode().get_rect()
        rect.left, rect.top = self.entity.get_position()
        return rect
