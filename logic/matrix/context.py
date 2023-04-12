from logic.matrix.entity import GameLogicEntity
from logic.matrix.command import Command
from typing import List, Dict, Tuple, Set, Optional
import json
from logic.matrix.matcher import Matcher
from logic.matrix.group import Group
from logic.matrix.component import Component
from common.logger import logger


class Context(object):

    def __init__(self):
        self._uid_cnt: int = 1
        self.commands: List[Command] = []
        self.messages: List[Command] = []

        self.is_connected: bool = False
        self.player_uid: int = 0
        self.edge_size: Tuple[float, float] = (780, 780)

        self._groups: Dict[Matcher, Group] = {}
        self._entities: Set[GameLogicEntity] = set()
        # self._reusable_entities: deque = deque()

    @property
    def entities(self) -> Set[GameLogicEntity]:
        return self._entities

    def create_entity(self, is_async: bool = True) -> GameLogicEntity:
        # entity = self._reusable_entities.pop() if self._reusable_entities else GameLogicEntity()
        entity = GameLogicEntity()
        entity.activate(self._uid_cnt, is_async)
        self._uid_cnt += 1
        self._entities.add(entity)

        entity.on_component_add += self._comp_added_or_removed
        entity.on_component_remove += self._comp_added_or_removed
        entity.on_component_replace += self._comp_replaced
        return entity

    def has_entity(self, entity: GameLogicEntity) -> bool:
        return entity in self._entities

    def destroy_entity(self, uid: int):
        entity = self.get_entity(uid)
        if not entity:
            return
        if not self.has_entity(entity):
            logger.warning(f"Entity.{entity.uid} not exist.")
            return
        self._entities.remove(entity)
        # entity.destroy()
        # self._reusable_entities.append(entity)

    def get_entity(self, uid: int) -> Optional[GameLogicEntity]:
        for entity in self._entities:
            if entity.uid == uid:
                return entity
        return None

    def get_or_create_entity(self, uid: int, is_async: bool = True) -> GameLogicEntity:
        entity = self.get_entity(uid)
        if not entity:
            return self.create_entity(is_async)
        return entity

    def get_player_count(self) -> int:
        cnt = 0
        for entity in self._entities:
            if not entity.has("player"):
                continue
            cnt += 1
        return cnt

    def input_command(self, command: Command):
        self.commands.append(command)

    def input_message(self, command: Command):
        self.messages.append(command)

    def export_world(self) -> str:
        d = dict()
        d["uid_cnt"] = self._uid_cnt
        d["entities"] = {}
        for entity in self._entities:
            snap = entity.export()
            if not snap:
                continue
            d["entities"][entity.uid] = snap
        return json.dumps(d)

    def import_world(self, s: str):
        d = json.loads(s)
        entities = set()
        for s_uid, info in d.get("entities", {}).items():
            uid = int(s_uid)
            if uid < 0:
                continue
            entity = self.get_or_create_entity(uid)
            entity.update(info)
            entities.add(entity)
        self._entities = entities
        self._uid_cnt = d.get("uid_cnt", self._uid_cnt)

    def get_group(self, matcher: Matcher) -> Group:
        if matcher in self._groups:
            return self._groups[matcher]

        group = Group(matcher)
        for entity in self._entities:
            group.init_entity(entity)

        self._groups[matcher] = group
        return group

    def _comp_added_or_removed(self, entity: GameLogicEntity, comp: Component):
        for matcher in self._groups:
            self._groups[matcher].handle_entity(entity, comp)

    def _comp_replaced(self, entity: GameLogicEntity, old_comp: Component, new_comp: Component):
        for matcher in self._groups:
            group = self._groups[matcher]
            group.update_entity(entity, old_comp, new_comp)

