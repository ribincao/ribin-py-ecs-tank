from common.logger import logger
from interface.system import ISystem
from interface.context import IContext


class CommandSystem(ISystem):

    def __init__(self, context: IContext):
        super(CommandSystem, self).__init__(context)

    async def update(self):
        logger.debug("CommandSystem Update")
        pass
