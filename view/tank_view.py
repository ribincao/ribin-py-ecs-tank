from interface.view import IView
from interface.context import IContext
from common.logger import logger


class TankView(IView):

    def __init__(self, context: IContext):
        super(TankView, self).__init__(context)

    def init_view(self):
        pass

    async def handle_event(self, operation: str):
        if operation == 'w':
            logger.debug("w key down")
        elif operation == 'a':
            logger.debug("a key down")
        elif operation == 's':
            logger.debug("s key down")
        elif operation == 'd':
            logger.debug("d key down")
