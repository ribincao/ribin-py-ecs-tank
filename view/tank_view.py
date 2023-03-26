from interface.view import IView
from interface.context import IContext
from common.logger import logger
from interface.behavior import IBehavior
from typing import List
from interface.entity import IEntity
from view.behavior.tank_behavior import TankBehavior


class TankView(IView):

    def __init__(self, context: IContext):
        super(TankView, self).__init__(context)

    async def update(self):
        behaviors = {}
        for entity in self.context.get_entities():
            behavior = self.behaviors.get(entity.uid, None)
            if behavior:
                behavior.entity = entity
                behaviors[entity.uid] = behavior
                continue
            behavior = self.create_behavior(entity)
            behaviors[entity.uid] = behavior
        self.behaviors = behaviors

    def create_behavior(self, entity: IEntity):
        # todo: 根据类型创建不同的behavior
        behavior = TankBehavior(entity)
        self.behaviors[entity.uid] = behavior
        return behavior

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
