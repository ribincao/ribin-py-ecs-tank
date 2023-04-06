from logic.interface.command import Command
from logic.entity.entity import GameLogicEntity
from common.logger import logger
from typing import Tuple
from logic.component.transform_component import Vector2


class CreateCmd(Command):

    def __init__(self, uid: int):
        super(CreateCmd, self).__init__(uid)
        self.mod_name: str = ""
        self.mod_index: int = 0
        self.position: Tuple[float, float] = (0.0, 0.0)
        self.layer: int = 0
        self.speed: float = 0
        self.state: int = 0
        self.box_collider: Tuple[float, float] = (60, 60)

    async def execute(self, entity: GameLogicEntity):
        if not self.mod_name:
            return
        
        entity.mod_index = self.mod_index
        entity.layer = self.layer
        entity.state = self.state
        entity.add_create(self.mod_name)
        entity.add_transform(Vector2(self.position[0], self.position[1]))
        entity.add_move(self.speed)
        if self.mod_name == 'bullet':
            self.box_collider = (12.0, 12.0)
        entity.add_box_collider(self.box_collider[0], self.box_collider[1])
        logger.debug(f"CreateCmd Execute {entity.uid} {self.__dict__}")

