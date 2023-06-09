from abc import abstractmethod
from logic.logic_entity import GameLogicEntity
import json


class Command(object):

    def __init__(self, uid: int):
        self.uid: int = uid
        self.name: str = ""

    @abstractmethod
    def execute(self, entity: GameLogicEntity):
        pass

    def encode(self):
        d = self.__dict__
        d["name"] = self.__class__.__name__[:-3].lower()
        return json.dumps(d) 

