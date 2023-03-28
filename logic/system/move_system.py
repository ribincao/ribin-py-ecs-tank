from common.logger import logger
from logic.system.isystem import ISystem
from logic.context import Context


class MoveSystem(ISystem):

    def __init__(self, context: Context):
        super(MoveSystem, self).__init__(context)

    async def update(self):
        logger.debug("MoveSystem Update")
        pass
