from logic.interface.command import Command
from logic.entity.entity import GameLogicEntity
from common.logger import logger
from logic.entity.state import EntityState
from logic.component.move_component import MoveDirection


class MoveCmd(Command):

    def __init__(self, uid: int):
        super(MoveCmd, self).__init__(uid)
        self.direction = MoveDirection.STOP

    async def execute(self, entity: GameLogicEntity):
        if not entity.move or entity.move.speed <= 0:
            return
        if MoveDirection.UP <= self.direction <= MoveDirection.RIGHT:
            entity.state = EntityState.move
            entity.mod_index = self.direction
        else:
            entity.state = EntityState.normal

