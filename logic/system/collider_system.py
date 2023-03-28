from logic.system.isystem import ISystem
from logic.context import Context
from common.logger import logger


class ColliderSystem(ISystem):

    def __init__(self, context: Context):
        super(ColliderSystem, self).__init__(context)

    async def update(self):
        logger.debug("ColliderSystem Update")
        pass
