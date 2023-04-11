from common.logger import logger
from logic.matrix.system import System
from logic.matrix.context import Context
from logic.matrix.entity import GameLogicEntity
from typing import List
from logic.component.state_component import State


class DestroySystem(System):

    def __init__(self, context: Context):
        super(DestroySystem, self).__init__(context)

    def update(self):
        destroy: List[GameLogicEntity] = []
        entities = list(self.context.entities)
        for entity in entities:
            if entity.state.state != State.destroy:
                continue
            destroy.append(entity)

        for entity in destroy:
            logger.debug(f"destroy entity {entity.uid}")
            self.context.destroy_entity(entity.uid)

