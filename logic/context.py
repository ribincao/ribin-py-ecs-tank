from logic.entity.entity import GameLogicEntity
from logic.interface.command import Command
from typing import List, Dict, Callable, Tuple
import json
from logic.event.event import EventDispatch, IEvent, EntityCreateEvent


class Context(object):

    def __init__(self):
        self.uid_cnt: int = 1
        self.entities: Dict[int, GameLogicEntity] = {}
        self.commands: List[Command] = []
        self.messages: List[Command] = []
        self.event_dispatch: EventDispatch = EventDispatch()
        
        self.is_connected: bool = False
        self.edge_size: Tuple[float, float] = (780, 780)

    def create_entity(self, is_async: bool = True) -> GameLogicEntity:
        entity = GameLogicEntity(self.uid_cnt, is_async)
        self.entities[self.uid_cnt] = entity
        self.dispatch_event(EntityCreateEvent(self.uid_cnt))

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
        if uid not in self.entities:
            return
        del self.entities[uid]

    def input_command(self, command: Command):
        self.commands.append(command)

    def input_message(self, command: Command):
        self.messages.append(command)

    def get_entities(self) -> List[GameLogicEntity]:
        return list(self.entities.values())

    def export_world(self) -> str:
        d = {}
        for entity in self.get_entities():
            snap = entity.export()
            if not snap:
                continue
            d[entity.uid] = snap
        if not d:
            return ''
        return json.dumps(d)

    def import_world(self, s: str):
        d = json.loads(s)
        if not d:
            return
        for s_uid, info in d.items():
            uid = int(s_uid)
            if uid < 0:
                continue
            entity = self.get_entity(uid)
            entity.update(info)
            if uid > self.uid_cnt:
                self.uid_cnt = uid + 1  # 确保客户端和服务端uid尽可能一致

    def dispatch_event(self, event: IEvent):
        self.event_dispatch.dispatch_event(event)

    def register_event(self, event_name: str, func: Callable):
        self.event_dispatch.register_event(event_name, func)

