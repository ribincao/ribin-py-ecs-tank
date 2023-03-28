from logic.command.icommand import ICommand
from logic.entity.entity import GameLogicEntity
from common.logger import logger


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
class MoveCmd(ICommand):

    def __init__(self, eid: int):
        super(MoveCmd, self).__init__(eid)
        self.direction = UP

    async def execute(self, entity: GameLogicEntity):
        logger.info(f"MoveCommand {self.eid}-{self.direction} exceute")
        entity.state = self.direction
