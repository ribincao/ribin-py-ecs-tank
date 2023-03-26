from interface.entity import IEntity
from interface.command import ICommand
from typing import List
from abc import abstractmethod


class IContext(object):

    def __init__(self):
        pass

    @abstractmethod
    def get_entities(self) -> List[IEntity]:
        return []
    
    @abstractmethod
    def create_entity(self, eid: int) -> IEntity:
        return IEntity(-1)

    @abstractmethod
    def filter_entity(self, component: str, entities: List[IEntity]):
        pass

    @abstractmethod
    def remove_entity(self, eid: int):
        pass

    @abstractmethod
    def input_command(self, command: ICommand):
        pass
