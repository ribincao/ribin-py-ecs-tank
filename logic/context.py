from logic.entity.entity import GameLogicEntity
from logic.interface.command import Command
from typing import List, Dict, Callable, Tuple
import json
from logic.event.event import EventDispatch, IEvent, EntityCreateEvent, EntityDestroyEvent


class Context(object):

    def __init__(self):
        self.uid_cnt: int = 1
        self.entities: Dict[int, GameLogicEntity] = {}
        self.commands: List[Command] = []
        self.messages: List[Command] = []
        self.event_dispatch: EventDispatch = EventDispatch()
        
        self.is_connected: bool = False
        self.player_uid: int = 0
        self.edge_size: Tuple[float, float] = (780, 780)

    def create_entity(self, is_async: bool = True) -> GameLogicEntity:
        entity = GameLogicEntity(self.uid_cnt, is_async)
        self.entities[self.uid_cnt] = entity

        self.uid_cnt += 1
        return entity
    
    def get_entity(self, uid: int, is_async: bool = True) -> GameLogicEntity:
        entity = self.entities.get(uid, None)
        if not entity:
            entity = self.create_entity(is_async)
            entity.uid = uid
        return entity

    def get_player_count(self):
        cnt = 0
        for entity in self.get_entities():
            if not entity.player:
                continue
            cnt += 1
        return cnt

    def destroy_entity(self, uid: int):
        uid_index = 0
        for uid_cnt, entity in self.entities.items():
            if entity.uid != uid:
                continue
            uid_index = uid_cnt
        if uid_index:
            self.dispatch_event(EntityDestroyEvent(self.uid_cnt))
            del self.entities[uid_index]

    def input_command(self, command: Command):
        self.commands.append(command)

    def input_message(self, command: Command):
        self.messages.append(command)

    def get_entities(self) -> List[GameLogicEntity]:
        return list(self.entities.values())

    def export_world(self) -> str:
        d = dict()
        d["uid_cnt"] = self.uid_cnt
        d["entities"] = {}
        entities = dict()
        for entity in self.get_entities():
            snap = entity.export()
            entities[entity.uid] = entity
            if not snap:
                continue
            d["entities"][entity.uid] = snap
        self.entities = entities
        return json.dumps(d)

    def import_world(self, s: str):
        d = json.loads(s)
        entities = dict()
        for s_uid, info in d.get("entities", {}).items():
            uid = int(s_uid)
            if uid < 0:
                continue
            entity = self.get_entity(uid)
            entity.update(info)
            entities[uid] = entity
        self.entities = entities
        self.uid_cnt = d.get("uid_cnt", self.uid_cnt)

    def dispatch_event(self, event: IEvent):
        self.event_dispatch.dispatch_event(event)

    def register_event(self, event_name: str, func: Callable):
        self.event_dispatch.register_event(event_name, func)

