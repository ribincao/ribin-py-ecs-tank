from logic.matrix.matcher import Matcher
from typing import Set
from logic.logic_entity import GameLogicEntity
from logic.matrix.event import Event
from enum import Enum
from logic.matrix.component import Component


class GroupEventType(Enum):
    NONE = 0
    ADD = 1
    REMOVE = 2
    UPDATE = 3


class Group(object):

    def __init__(self, matcher: Matcher):
        self._matcher: Matcher = matcher
        self._entities: Set[GameLogicEntity] = set()

        self.on_entity_add: Event = Event()
        self.on_entity_remove: Event = Event()
        self.on_entity_update: Event = Event()

    @property
    def entities(self) -> Set[GameLogicEntity]:
        return self._entities

    def init_entity(self, entity: GameLogicEntity):
        if self._matcher.matches(entity):
            self._add_entity(entity)
        else:
            self._remove_entity(entity)

    def handle_entity(self, entity: GameLogicEntity, component: Component):
        if self._matcher.matches(entity):
            if not self._add_entity(entity):
                return
            self.on_entity_add(entity, component)
        else:
            if not self._remove_entity(entity):
                return
            self.on_entity_remove(entity, component)

    def update_entity(self, entity: GameLogicEntity, old_comp: Component, new_comp: Component):
        if entity in self._entities:
            self.on_entity_update(entity, old_comp, new_comp)

    def _add_entity(self, entity: GameLogicEntity) -> bool:
        if entity not in self._entities:
            self._entities.add(entity)
            return True
        return False

    def _remove_entity(self, entity: GameLogicEntity) -> bool:
        if entity in self._entities:
            self._entities.remove(entity)
            return True
        return False
