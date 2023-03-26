from common.logger import logger
from interface.system import ISystem
from interface.context import IContext


class MoveSystem(ISystem):

    def __init__(self, context: IContext):
        super(MoveSystem, self).__init__(context)

    async def update(self):
        logger.debug("MoveSystem Update")
        pass
