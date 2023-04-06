from common.logger import logger
from logic.interface.system import System
from logic.context import Context
from logic.entity.entity import GameLogicEntity
from typing import List


class GCSystem(System):
    """
    删除entity的system
    """
    DELTA = 100

    def __init__(self, context: Context):
        super(GCSystem, self).__init__(context)

    async def update(self):
        remove: List[GameLogicEntity] = []
        for entity in self.context.get_entities():
            x, y = entity.transform.position.to_tuple()
            if not -self.DELTA <= x <= self.context.edge_size[0] + self.DELTA:
                remove.append(entity)
            if not -self.DELTA <= y <= self.context.edge_size[1] + self.DELTA:
                remove.append(entity)

        for entity in remove:
            logger.info(f"remove entity {entity.uid} {entity.create.mod_name}")
            self.context.remove_entity(entity.uid)

