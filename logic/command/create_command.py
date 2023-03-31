from logic.command.icommand import ICommand
from logic.entity.entity import GameLogicEntity
from common.logger import logger
from typing import Tuple
from common.common import Vector2


class CreateCmd(ICommand):

    def __init__(self, eid: int):
        super(CreateCmd, self).__init__(eid)
        self.mod_name: str = ""
        self.mod_index: int = 0
        self.position: Tuple[float, float] = (0.0, 0.0)
        self.layer: int = 0
        self.speed: float = 0

    async def execute(self, entity: GameLogicEntity):
        logger.debug(f"CreateCmd IN {entity.uid} exceute")
        if not self.mod_name:
            return
        
        entity.mod_index = self.mod_index
        entity.layer = self.layer
        entity.add_create(self.mod_name)
        entity.add_transform(Vector2(self.position[0], self.position[1]))
        entity.add_move(self.speed)

