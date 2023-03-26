from interface.view import IView
from interface.context import IContext
from pygame import K_w, K_a, K_s, K_d
from common.logger import logger


class TankView(IView):

    def __init__(self, context: IContext):
        super(TankView, self).__init__(context)

    def init_view(self):
        pass

    async def handle_event(self, operation: int):
        if operation == K_w:
            logger.debug("w key down")
        elif operation == K_a:
            logger.debug("a key down")
        elif operation == K_s:
            logger.debug("s key down")
        elif operation == K_d:
            logger.debug("d key down")
