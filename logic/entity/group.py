from logic.match.matcher import Matcher
from typing import Set
from logic.entity.entity import GameLogicEntity
from logic.event.event import Event
from enum import Enum
from logic.interface.component import Component


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
    def entities(self):
        return self._entities

    def handle_entity(self, entity: GameLogicEntity, component: Component , g_event: GroupEventType = GroupEventType.NONE):
        if self._matcher.matches(entity):
            is_ok = self._add_entity(entity)
        else:
            is_ok = self._remove_entity(entity)

        if not is_ok:
            return

        if g_event == GroupEventType.ADD:
            self.on_entity_add(entity, component)
        if g_event == GroupEventType.REMOVE:
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
