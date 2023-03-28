from interface.entity import IEntity
from pygame import Surface, Rect
from typing import Dict
from abc import abstractmethod


class IBehavior(object):

    def __init__(self, entity: IEntity):
        self.entity: IEntity = entity

    @abstractmethod
    def init_modes(self):
        pass

    @abstractmethod
    def mode(self) -> object:
        pass

    @abstractmethod
    def rect(self) -> object:
        pass


class IPyGameBehavior(IBehavior):

    def __init__(self, entity: IEntity):
        super(IPyGameBehavior, self).__init__(entity)
        self.models: Dict[str, Surface] = {}

    @abstractmethod
    def init_modes(self):
        pass

    @property
    def mode(self) -> Surface:
        return self.models[self.entity.state]

    @property
    def rect(self) -> Rect:
        rect = self.mode.get_rect()
        rect.left, rect.top = self.entity.get_position()
        return rect
