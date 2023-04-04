from abc import abstractmethod
from logic.entity.entity import GameLogicEntity
import json


class Command(object):

    def __init__(self, uid: int):
        self.uid: int = uid

    @abstractmethod
    async def execute(self, entity: GameLogicEntity):
        pass

    def encode(self):
        d = self.__dict__
        d["__class__"] = self.__class__.__name__
        return json.dumps(d) 

