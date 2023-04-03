from logic.entity.entity import GameLogicEntity
from logic.command.icommand import ICommand
from typing import List, Dict, Callable
import json
from logic.event.event import EventDispatch, IEvent, EntityCreateEvent


class Context(object):

    def __init__(self):
        self.uid_cnt: int = 1
        self.entities: Dict[int, GameLogicEntity] = {}
        self.commands: List[ICommand] = []
        self.messages: List[ICommand] = []
        self.event_dispatch: EventDispatch = EventDispatch()
        
        self.is_connected: bool = False

    def create_entity(self) -> GameLogicEntity:
        entity = GameLogicEntity(self.uid_cnt)
        self.entities[self.uid_cnt] = entity
        self.dispatch_event(EntityCreateEvent(self.uid_cnt))

        self.uid_cnt += 1
        return entity
    
    def get_entity(self, eid: int) -> GameLogicEntity:
        entity = self.entities.get(eid, None)
        if not entity:
            entity = self.create_entity()
            entity.uid = eid
        return entity

    def remove_entity(self, eid: int):
        if eid not in self.entities:
            return
        del self.entities[eid]

    def input_command(self, command: ICommand):
        self.commands.append(command)

    def input_message(self, command: ICommand):
        self.messages.append(command)

    def get_entities(self) -> List[GameLogicEntity]:
        return list(self.entities.values())

    def export_world(self) -> str:
        d = {}
        for entity in self.get_entities():
            snap = entity.export()
            if not snap:
                continue
            d[entity.uid] = entity.export()
        return json.dumps(d)

    def import_world(self, s: str):
        d = json.loads(s)
        for _, info in d.items():
            uid = info.get("uid", -1)
            if uid < 0:
                continue
            entity = self.get_entity(uid)
            entity = self.entities[uid]
            entity.refresh(info)
            if uid > self.uid_cnt:
                self.uid_cnt = uid + 1  #  确保客户端和服务端uid尽可能一致

    def dispatch_event(self, event: IEvent):
        self.event_dispatch.dispatch_event(event)

    def register_event(self, event_name: str, func: Callable):
        self.event_dispatch.register_event(event_name, func)

