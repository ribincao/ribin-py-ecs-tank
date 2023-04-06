from common.logger import logger
from logic.interface.system import System
from logic.context import Context
from logic.entity.entity import GameLogicEntity
from typing import List
from logic.component.state_component import State


class DestroySystem(System):
    """
    删除entity的system
    """
    DELTA = 100

    def __init__(self, context: Context):
        super(DestroySystem, self).__init__(context)

    async def update(self):
        destroy: List[GameLogicEntity] = []
        for entity in self.context.get_entities():
            if not entity.state or entity.state.state != State.destroy:
                continue
            destroy.append(entity)

        for entity in destroy:
            logger.info(f"destroy entity {entity.uid}")
            self.context.destroy_entity(entity.uid)

