from common.logger import logger
from logic.system.isystem import ISystem
from logic.context import Context


class CreateSystem(ISystem):

    def __init__(self, context: Context):
        super(CreateSystem, self).__init__(context)

    async def update(self):
        logger.debug("CreateSystem Update")
        pass
