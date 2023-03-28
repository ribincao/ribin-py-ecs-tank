from view.iview import IView
from logic.context import Context
from common.logger import logger
from view.behavior.ibehavior import IBehavior
from typing import List
from logic.entity.entity import GameLogicEntity
from view.behavior.tank_behavior import TankBehavior
from common.data_util import data_util


class TankView(IView):

    def __init__(self, context: Context):
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

    def create_behavior(self, entity: GameLogicEntity):
        # todo: 根据类型创建不同的behavior
        behavior = TankBehavior(entity)
        self.behaviors[entity.uid] = behavior
        return behavior

    def init_view(self):
        scene_maps = data_util.load_from_json('./view/scene/tank.json')
        logger.info(f"view_load_tank_scene {scene_maps}")
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
