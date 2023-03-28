from common.logger import logger
from logic.system.isystem import ISystem
from logic.context import Context


class MoveSystem(ISystem):

    def __init__(self, context: Context):
        super(MoveSystem, self).__init__(context)

    async def update(self):
        logger.debug("MoveSystem Update")
        entities = self.context.get_entities()
        for entity in entities:
            if not entity.rigibody or not entity.transform:
                continue
            entity.transform.position.y += entity.rigibody.gravity
