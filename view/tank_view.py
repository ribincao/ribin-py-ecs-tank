from view.iview import IView
from logic.context import Context
from common.logger import logger
from logic.entity.entity import GameLogicEntity
from view.behavior.tank_behavior import TankBehavior
from common.data_util import data_util
import asyncio


class TankView(IView):

    def __init__(self, context: Context):
        super(TankView, self).__init__(context)

    async def update(self):
        while True:
            behaviors = {}
            for entity in self.context.get_entities():
                behavior = self.behaviors.get(entity.uid, None)
                if behavior:
                    behavior.entity = entity
                    behaviors[entity.uid] = behavior
                    logger.debug(f"update_behavior {behavior.mode}")
                    continue
                behavior = self.create_behavior(entity)
                behaviors[entity.uid] = behavior
            self.behaviors = behaviors
            await asyncio.sleep(self.VIEW_RATE)

    def create_behavior(self, entity: GameLogicEntity):
        behavior = TankBehavior(entity)
        behavior.init_models(entity.create.mod_id)
        self.behaviors[entity.uid] = behavior
        return behavior

    def init_view(self):
        scene_maps = data_util.load_from_json('./view/scene/tank.json')
        logger.info(f"view_load_tank_scene {scene_maps}")

    async def handle_event(self, operation: str):
        if operation == 'w':
            logger.info("w key down")
        elif operation == 'a':
            logger.info("a key down")
        elif operation == 's':
            logger.info("s key down")
        elif operation == 'd':
            logger.info("d key down")
