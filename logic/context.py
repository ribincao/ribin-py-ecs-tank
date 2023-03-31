from logic.entity.entity import GameLogicEntity
from logic.command.icommand import ICommand
from typing import List, Dict, Optional
from common.logger import logger
import json


class Context(object):

    def __init__(self):
        self.entities: Dict[int, GameLogicEntity] = {}
        self.commands: List[ICommand] = []
        self.messages: List[ICommand] = []

    def create_entity(self, eid: int) -> GameLogicEntity:
        if eid in self.entities:
            logger.warning(f"{eid} entity already exist.")
        entity = GameLogicEntity(eid)
        self.entities[eid] = entity
        return entity

    def get_entity(self, eid: int) -> Optional[GameLogicEntity]:
        return self.entities.get(eid, None)

    def filter_entity(self, component: str, entities: List[GameLogicEntity]):
        if not entities:
            entities = list(self.entities.values())
        result = []
        for entity in entities:
            if not entity.__getattribute__(component):
                continue
            result.append(entity)
        return result

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
            if uid not in self.entities:
                continue
            entity = self.entities[uid]
            entity.transform.position.x = info["transform"]["position"][0]
            entity.transform.position.y = info["transform"]["position"][1]
            entity.mod_index = info.get("mod_index", 0)
