from logic.command.icommand import ICommand
from logic.entity.entity import GameLogicEntity
from common.logger import logger
from logic.entity.state import EntityState


STOP = -1
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


class MoveCmd(ICommand):

    def __init__(self, eid: int):
        super(MoveCmd, self).__init__(eid)
        self.direction = STOP

    async def execute(self, entity: GameLogicEntity):
        logger.debug(f"MoveCommand IN {entity.uid}-{self.direction} exceute")
        if not entity.move or entity.move.speed <= 0:
            return
        if UP <= self.direction <= RIGHT:
            entity.state = EntityState.move
            entity.mod_index = self.direction
        else:
            entity.state = EntityState.normal

