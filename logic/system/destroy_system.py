from common.logger import logger
from logic.matrix.system import System
from logic.matrix.context import Context
from logic.matrix.entity import GameLogicEntity
from typing import List
from logic.component.state_component import State
from logic.matrix.group import Group
from logic.matrix.matcher import Matcher


class DestroySystem(System):

    def __init__(self, context: Context):
        super(DestroySystem, self).__init__(context)
        self.state_group: Group = self.context.get_group(Matcher("state"))

    def update(self):
        destroy: List[GameLogicEntity] = []
        for entity in self.state_group.entities:
            if entity.get_component("state").state != State.destroy:
                continue
            destroy.append(entity)

        for entity in destroy:
            logger.debug(f"destroy entity {entity.uid}")
            self.context.destroy_entity(entity.uid)

