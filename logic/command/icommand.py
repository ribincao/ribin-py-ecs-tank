from abc import abstractmethod
from logic.entity.entity import GameLogicEntity


class ICommand(object):

    def __init__(self, eid: int):
        self.eid: int = eid

    @abstractmethod
    async def execute(self, entity: GameLogicEntity):
        pass

