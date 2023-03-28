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
        logger.info(f"MoveCommand IN {self.eid}-{self.direction} exceute")
        entity.mod_index = self.direction
        if not entity.transform or not entity.move:
            return
        
        if entity.mod_index == UP:
            entity.transform.position.y -= entity.move.speed
        elif entity.mod_index == DOWN:
            entity.transform.position.y += entity.move.speed
        elif entity.mod_index == LEFT:
            entity.transform.position.x -= entity.move.speed
        elif entity.mod_index == RIGHT:
            entity.transform.position.x += entity.move.speed
        logger.info(f"MoveCommand OUT {self.eid}-{entity.transform.position.x}-{entity.transform.position.y} exceute")
