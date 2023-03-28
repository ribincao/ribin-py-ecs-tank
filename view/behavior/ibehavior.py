from logic.entity.entity import GameLogicEntity
from pygame import Surface, Rect
from typing import Dict, List
from abc import abstractmethod


class IBehavior(object):

    def __init__(self, entity: GameLogicEntity):
        self.entity: GameLogicEntity = entity
        self.models: Dict[str, object] = {}

    @abstractmethod
    def init_models(self, mod_id: int):
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
    def init_models(self, mod_id: int):
        pass

    @property
    def mode(self) -> Surface:
        return self.models[self.entity.state]

    @property
    def rect(self) -> Rect:
        rect = self.mode.get_rect()
        rect.left, rect.top = self.entity.get_position()
        return rect
