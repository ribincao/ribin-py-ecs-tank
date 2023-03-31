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

    async def execute(self, entity: GameLogicEntity):
        logger.debug(f"CreateCmd IN {entity.uid} exceute")
        entity.create.mod_name = self.mod_name
        entity.mod_index = self.mod_index
        entity.transform.position = Vector2(self.position[0], self.position[1])
        entity.layer = self.layer

