from logic.entity.entity import GameLogicEntity
from logic.command.icommand import ICommand
from typing import List, Dict, Optional
from common.logger import logger


class Context(object):

    def __init__(self):
        self.entities: Dict[int, GameLogicEntity] = {}
        self.commands: List[ICommand] = []

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

    def get_entities(self) -> List[GameLogicEntity]:
        return list(self.entities.values())
