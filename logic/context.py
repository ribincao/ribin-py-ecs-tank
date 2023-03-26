from interface.context import IContext
from interface.entity import IEntity
from interface.behavior import IBehavior
from interface.command import ICommand
from typing import List, Dict
from common.logger import logger


class Context(IContext):

    def __init__(self):
        super(Context, self).__init__()
        self.entities: Dict[int, IEntity] = {}
        self.behaviors: Dict[int, IBehavior] = {}
        self.commands: List[ICommand] = []

    def create_entity(self, eid: int) -> IEntity:
        if eid in self.entities:
            logger.debug(f"warning: {eid} entity already exist.")
        entity = IEntity(eid)
        self.entities[eid] = entity
        return entity

    def filter_entity(self, component: str, entities: List[IEntity]):
        if not entities:
            entities = list(self.entities.values())
        result = []
        for entity in entities:
            if not entity.__getattribute__(component):
                continue
            result.append(entity)
        return result

    def remove_entity(self, eid: int):
        if eid not in self.entities and eid not in self.behaviors:
            return
        del self.entities[eid]
        del self.behaviors[eid]

    def input_command(self, command: ICommand):
        self.commands.append(command)

    def get_entities(self) -> List[IEntity]:
        return list(self.entities.values())
