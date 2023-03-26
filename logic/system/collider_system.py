from interface.system import ISystem
from interface.context import IContext
from common.logger import logger


class ColliderSystem(ISystem):

    def __init__(self, context: IContext):
        super(ColliderSystem, self).__init__(context)

    async def update(self):
        logger.debug("ColliderSystem Update")
        pass
