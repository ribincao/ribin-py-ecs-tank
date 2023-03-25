from interface.context import IContext
from interface.entity import IEntity
from typing import List, Dict


class Context(IContext):

    def __init__(self):
        self.entities: Dict[int, IEntity] = {}

    def create_entity(self, eid: int) -> IEntity:
        if eid in self.entities:
            print(f"warning: {eid} already exist.")
        entity = IEntity(eid)
        self.entities[eid] = entity
        return entity

    def filter_entity(self, component_name: str, entities: List[IEntity]):
        if not entities:
            entities = list(self.entities.values())
        result = []
        for entity in entities:
            if not entity.__getattribute__(component_name):
                continue
            result.append(entity)
        return result

    def remove_entity(self, eid: int):
        if eid not in self.entities:
            return
        del self.entities[eid]


