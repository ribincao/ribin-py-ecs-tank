from interface.context import IContext
from interface.entity import IEntity
from interface.command import ICommand
from typing import List, Dict


class Context(IContext):

    def __init__(self):
        self.entities: Dict[int, IEntity] = {}
        self.commands: List[ICommand] = []

    def create_entity(self, eid: int) -> IEntity:
        if eid in self.entities:
            print(f"warning: {eid} already exist.")
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
        if eid not in self.entities:
            return
        del self.entities[eid]

    def input_command(self, command: ICommand):
        self.commands.append(command)


